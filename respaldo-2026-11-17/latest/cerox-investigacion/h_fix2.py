#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit H3: las fuentes IPTV van al almacenamiento externo, no al interno.

ReglaDeAlmacenamientoTest (publicada antes que este módulo, y que yo no leí) exige
que nada escriba datos en el almacenamiento interno salvo los tokens cifrados. Mi
`File(c.filesDir, ...)` la rompía, y mi propia prueba la defendía: tenía un
`assertTrue(t.contains("File(c.filesDir"))`. Se arregla el código Y la prueba.
"""
import base64, datetime, json, os, re, sys, time, urllib.request, urllib.error

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
SRC = "android/app/src/"
MOD = "modules/iptv/IptvModule.kt"
P_MOD = SRC + "main/java/com/ceroX/app/" + MOD
P_INV = SRC + "main/java/com/ceroX/app/core/InventoryStorage.kt"
P_TEST = SRC + "test/java/com/ceroX/app/modules/iptv/IptvReproductorTest.kt"
BASE_ESPERADO = "c78158910b24671d211786b2c6fade2e70800897"
EJECUTAR = "--run" in sys.argv

MARCAS = ["Placeholder", "placeholder", "Simular", "simulado", "TODO:", "FIXME", "dummy",
          "hardcodeado", "sin implementar", "not implemented"]
SOSPECHOSAS = ["compatible", "mejorado", "improved", "stabilized", "estable",
               "verificado", "verified", "funciona", "works", "listo"]


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxiptv"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movio: " + BASE)
print("MODO: %s · base %s\n" % ("PUBLICACION" if EJECUTAR else "DRY-RUN", BASE[:8]))

def leer(p):
    return base64.b64decode(api("/contents/%s?ref=%s" % (p, BASE))["content"]).decode()


def solo_codigo(t):
    """El texto sin strings ni comentarios, para contar llaves y parentesis.

    Contar sobre el texto crudo falla con cualquier paréntesis dentro de una cadena,
    y el inventario tiene muchas. Las comillas escapadas se quitan antes que los
    strings, o un \" dentro de una cadena parte el recorte en el sitio equivocado.
    """
    t = re.sub(r'"""[\s\S]*?"""', " ", t)
    t = t.replace('\\"', " ")
    t = re.sub(r'"[^"\n]*"', " ", t)
    t = re.sub(r"'[^'\n]*'", " ", t)
    t = re.sub(r"/\*[\s\S]*?\*/", " ", t)
    return "\n".join(l for l in t.split("\n") if not l.strip().startswith("//"))


mod = leer(P_MOD)
inv = leer(P_INV)
test = leer(P_TEST)
cambios = {P_MOD: mod, P_INV: inv, P_TEST: test}
nuevo_en = {P_MOD: [], P_INV: [], P_TEST: []}


def sust(p, viejo, nuevo, veces=1):
    t = cambios[p]
    n = t.count(viejo)
    ok(n == veces, "%s: el anclaje aparece %d veces, se esperaban %d" % (p, n, veces))
    cambios[p] = t.replace(viejo, nuevo)
    nuevo_en[p].append(nuevo)


# ── 1 · IptvModule.kt ──────────────────────────────────────────────────────

sust(P_MOD,
     "import com.ceroX.app.core.engine.ModuleHealth",
     "import com.ceroX.app.core.AlmacenExterno\n"
     "import com.ceroX.app.core.engine.ModuleHealth")

sust(P_MOD,
     '''            ultimoMotivo = "No se inyectó el contexto: sin él no hay directorio privado " +
                "donde guardar las fuentes que añada el usuario"''',
     '''            ultimoMotivo = "No se inyectó el contexto: sin él no hay forma de resolver " +
                "dónde guardar las fuentes que añada el usuario"''')

sust(P_MOD,
     '''        contexto = c
        almacen = AlmacenFuentes(File(c.filesDir, NOMBRE_ALMACEN))
        _initialized = true
        return true''',
     '''        contexto = c
        // La regla de almacenamiento del proyecto (core/InventoryStorage, que vigila
        // ReglaDeAlmacenamientoTest) prohíbe escribir datos en el almacenamiento
        // interno salvo los tokens cifrados: lo que la app guarda va a su carpeta
        // propia en el almacenamiento externo, que no pide ningún permiso. Y si esa
        // carpeta no está disponible no se cae al interno, que es justo lo que la
        // regla no admite: se devuelve el fallo con su motivo.
        val destino: File = AlmacenExterno.archivo(c, NOMBRE_ALMACEN) ?: run {
            ultimoMotivo = "No hay almacenamiento externo disponible para la app, así que no " +
                "hay dónde guardar las fuentes que añada el usuario: " + AlmacenExterno.estado(c)
            return false
        }
        almacen = AlmacenFuentes(destino)
        _initialized = true
        return true''')

# ── 2 · la prueba que defendía el fallo ────────────────────────────────────

sust(P_TEST,
     '''        assertTrue(
            "las fuentes se guardan en el almacenamiento privado, no en el APK",
            t.contains("File(c.filesDir"),
        )''',
     '''        assertTrue(
            "las fuentes van a la carpeta propia de la app en el almacenamiento externo, " +
                "que es lo que pide la regla de almacenamiento del proyecto",
            t.contains("AlmacenExterno.archivo(c,"),
        )
        assertFalse(
            "los datos no se escriben en el almacenamiento interno: ahí solo viven los " +
                "tokens cifrados",
            t.contains("filesDir"),
        )
        assertTrue(
            "si no hay almacenamiento externo no se cae al interno, se dice por qué falló",
            t.contains("No hay almacenamiento externo disponible"),
        )''')

# ── 3 · declararlo en el inventario ────────────────────────────────────────

sust(P_INV,
     '''    val sitios: List<Sitio> = listOf(
''',
     '''    val sitios: List<Sitio> = listOf(
        Sitio(
            "modules/iptv/IptvModule.kt",
            "lista de fuentes IPTV que añade el usuario",
            Verdict.FUERA_DEL_INTERNO,
            "Un JSON con las fuentes instaladas: nombre, URL y, si la fuente la declara, la " +
                "huella SHA-256 con la que se comprueba lo descargado. Se resuelve con " +
                "AlmacenExterno.archivo; si el almacenamiento externo no está disponible, " +
                "initialize falla con su motivo en vez de caer al interno. Este archivo no " +
                "lleva ninguna lista de canales ni ninguna guía dentro: las fuentes las pone " +
                "el usuario, una por una, y se descargan en el momento de cargarlas.",
        ),
''')

# ── COMPROBACIONES ─────────────────────────────────────────────────────────

print("COMPROBACIONES")
for p in sorted(cambios):
    t = cambios[p]
    propio = "\n".join(nuevo_en[p])
    ok(len(t) > 500, p + " sospechosamente corto")
    for linea in propio.split("\n"):
        c = linea.strip()
        if "*/" in linea and c != "*/" and not c.endswith("*/"):
            raise SystemExit("%s: un */ a mitad de linea: %s" % (p, c[:80]))
        for m in MARCAS:
            ok(m not in linea, "marca %r en %s" % (m, p))
    # El balance se mide sobre el fichero entero y sin strings ni comentarios: medido
    # sobre el trozo añadido da falso, porque el anclaje puede llevarse un paréntesis
    # que ya estaba abierto (pasa con `val sitios: List<Sitio> = listOf(`).
    cod = solo_codigo(t)
    ok(cod.count("{") == cod.count("}"), "%s: llaves %d/%d" % (p, cod.count("{"), cod.count("}")))
    ok(cod.count("(") == cod.count(")"), "%s: parentesis %d/%d" % (p, cod.count("("), cod.count(")")))
    print("  %7d B · %s" % (len(t.encode()), p.replace(SRC, "…/")))

# Lo que la regla de almacenamiento vigila, repetido aquí sobre el resultado.
ok("filesDir" not in cambios[P_MOD], "IptvModule.kt sigue tocando el almacenamiento interno")
ok("cacheDir" not in cambios[P_MOD] and "SharedPreferences" not in cambios[P_MOD],
   "IptvModule.kt toca cacheDir o preferencias")
for patron in ["?: filesDir", "?: context.filesDir", 'System.getProperty("java.io.tmpdir")']:
    for p in cambios:
        ok(patron not in cambios[p], "caida silenciosa al interno en " + p)
ok("AlmacenExterno.archivo(c, NOMBRE_ALMACEN)" in cambios[P_MOD], "no quedo la llamada buena")
ok("import com.ceroX.app.core.AlmacenExterno" in cambios[P_MOD], "falta el import")

# La prueba publicada y el código tienen que coincidir literal a literal.
exigidos_test = ["AlmacenExterno.archivo(c,", "No hay almacenamiento externo disponible"]
for lit in exigidos_test:
    ok(lit in cambios[P_MOD], "la prueba va a exigir %r y el modulo no lo tiene" % lit)
ok('t.contains("filesDir")' in cambios[P_TEST], "se perdio la prohibicion en la prueba")
ok('t.contains("File(c.filesDir"' not in cambios[P_TEST], "la prueba sigue defendiendo el fallo")
ok('t.contains("No se inyectó el contexto")' in cambios[P_TEST],
   "la prueba exige un literal que se ha cambiado")
ok("No se inyectó el contexto" in cambios[P_MOD], "y ese literal ya no esta en el modulo")

# El inventario: el sitio nuevo existe, no es deuda, y no cita palabras prohibidas.
ok('Verdict.FUERA_DEL_INTERNO' in cambios[P_INV], "el sitio nuevo no dice su veredicto")
ok("modules/iptv/IptvModule.kt" in cambios[P_INV], "el inventario no nombra el fichero")
ok(cambios[P_INV].count("DEUDA_MIGRACION") == inv.count("DEUDA_MIGRACION"),
   "se ha anadido deuda al inventario")
for linea in nuevo_en[P_INV]:
    for clave in SOSPECHOSAS:
        ok(clave not in linea, "palabra sospechosa %r en el inventario" % clave)
    ok('" to true"' not in linea, "afirmacion constante en el inventario")

# Lo que NO cambia: ni el numero de pruebas ni las claves del health check.
ok(cambios[P_TEST].count("@Test") == test.count("@Test"), "cambio el numero de pruebas")
for clave in ["almacen_creado", "fuentes", "canales_cargados", "programas_de_guia",
              "reproductor_creado", "ultimo_motivo", "motivo_del_almacen"]:
    ok('"%s" to' % clave in cambios[P_MOD], "el health check perdio la clave " + clave)
print("  @Test                            %d (sin cambios)" % cambios[P_TEST].count("@Test"))
print("  claves del health check          7 exigidas, presentes")

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": p, "mode": "100644", "type": "blob", "content": cambios[p]}
    for p in sorted(cambios)]})["sha"]
msg = """IPTV: las fuentes van al almacenamiento externo, y mi prueba las defendía mal

Falló `ReglaDeAlmacenamientoTest.todo_sitio_que_escribe_esta_declarado_en_el_inventario`,
una prueba publicada antes que este módulo y que yo no leí antes de escribirlo. Tiene
razón y yo no:

  · `File(c.filesDir, NOMBRE_ALMACEN)` escribía la lista de fuentes del usuario en el
    almacenamiento interno, que es exactamente lo que la regla prohíbe para todo lo que
    no sea un token cifrado.
  · Y lo peor no fue el código: fue que mi propia prueba lo exigía con un
    `assertTrue(t.contains("File(c.filesDir"))`. Escribí una aserción para defender mi
    fallo, con un mensaje que además decía lo contrario de la regla del proyecto
    («se guardan en el almacenamiento privado»). Una prueba así no protege de nada:
    convierte el error en requisito.

Qué cambia:

  1. `IptvModule.initialize` resuelve el archivo con `AlmacenExterno.archivo(c, ...)`,
     el mecanismo que ya usa el resto del proyecto (carpeta propia de la app en el
     almacenamiento compartido, sin pedir permiso, con comprobación real de escritura).
  2. Si el almacenamiento externo no está disponible, la inicialización **falla con su
     motivo** —que incluye lo que dice `AlmacenExterno.estado`— en vez de caerse al
     interno. Es el comportamiento que la regla pide explícitamente.
  3. La prueba cambia de bando: ahora exige `AlmacenExterno.archivo(c,`, exige el motivo
     del fallo cuando no hay externo, y **prohíbe** que aparezca el directorio interno en
     el módulo.
  4. El sitio se declara en `core/InventoryStorage` con veredicto FUERA_DEL_INTERNO, que
     es para lo que existe ese inventario: que se pueda ir a ver qué escribe cada quién y
     con qué derecho.

No se añade deuda al inventario (`deudas()` sigue igual), no cambia el número de pruebas
(461) y el health check conserva sus claves. Tampoco se relaja ninguna aserción para que
pase: se cambia la que estaba mal escrita, y se cambió el código primero.

Sigue sin comprobarse en un dispositivo. Que el almacenamiento externo sea escribible en
un teléfono concreto lo dice el teléfono, no esta prueba."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
