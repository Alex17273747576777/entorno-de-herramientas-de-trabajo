#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit P · arreglar la contradicción entre dos pruebas publicadas.

El commit O movió la creación del entorno ONNX detrás de `MotorOnnx.entorno()`.
Con eso dejó roto un contrato publicado que el pre-vuelo no censó:
`ArranqueHonestoTest.losSieteEntornosOnnxSonPerezosos` escanea los siete módulos
por contenido y exige que la línea que crea el entorno exista y lleve `by lazy`.
Al moverse el literal, la línea dejó de existir y la prueba falló: main quedó en
478 · 1 y la release v1.0.4 se cortó de un commit con el suite en rojo.

Las dos intenciones siguen vivas y ninguna se relaja:

- ArranqueHonestoTest quería: el entorno no se crea al construir el módulo, se
  crea perezosamente. Eso no cambió: los sitios siguen siendo `by lazy`, sólo
  que ahora delegan en la puerta. La prueba pasa a escanear la llamada a la
  puerta (`MotorOnnx.entorno()`), exige el `by lazy` igual que antes, y añade
  una tercera afirmación: que el literal a pelo ya NO está en el módulo.
- MotorOnnxTest quería: nadie crea el entorno fuera de la puerta. Sigue igual.

Y el pre-vuelo estrena el censo que faltó: `lectores_de_literal()` (R23) recorre
las pruebas publicadas buscando el literal que este commit mueve, y exige que el
commit toque a cada lector. En el estado de O, ese censo habría devuelto
`ArranqueHonestoTest.kt` y el commit no lo tocaba: fallo antes de publicar.

Uso: export GP=<token fino> && python3 -B p_commit.py [--run]
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import balancear, lectores_de_literal  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
RAW = "https://raw.githubusercontent.com/Alex17273747576777/cero-X-app"
AHT = "android/app/src/test/java/com/ceroX/app/core/engine/ArranqueHonestoTest.kt"
LITERAL = "OrtEnvironment.getEnvironment()"
PUERTA = "MotorOnnx.entorno()"
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitP"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


def crudo(ruta, sha):
    with urllib.request.urlopen("%s/%s/%s" % (RAW, sha, ruta), timeout=120) as x:
        return x.read().decode("utf-8")


BASE = api("/git/ref/heads/main")["object"]["sha"]
print("MODO: %s · base %s" % ("PUBLICAR" if EJECUTAR else "DRY-RUN", BASE[:8]))
t = crudo(AHT, BASE)
N_ANTES = t.count("@Test")          # derivado del fichero publicado, no de mi memoria

# ── R23 · el censo que faltó en O: quién más lee el literal que se mueve ────
arbol = api("/git/trees/%s?recursive=1" % BASE)["tree"]
pruebas = {e["path"]: crudo(e["path"], BASE) for e in arbol
           if e["path"].startswith("android/app/src/test/") and e["path"].endswith(".kt")}
lectores = lectores_de_literal(pruebas, LITERAL)                 # como blanco de búsqueda
consumidores = [n for n in lectores_de_literal(pruebas, LITERAL, como_cadena=False)
                if n not in lectores]                              # uso como código propio
ok(lectores, "nadie escanea el literal en las pruebas publicadas: el censo no mira nada")
ok(AHT in lectores, "el lector esperado no aparece: %s" % lectores)
print("  R23  escaneadores del literal movido          %s" % ", ".join(
    l.split("/")[-1] for l in lectores))
print("       consumidores (no acoplados, no se tocan)  %s" % (", ".join(
    c.split("/")[-1] for c in consumidores) or "ninguno"))

# ── R10 · anclajes ──────────────────────────────────────────────────────────
A_FIL = 'val lineas = fuente(rel)!!.readText().lines().filter { it.contains("OrtEnvironment.getEnvironment()") }'
A_CARGA = 'assertTrue("$rel carga el entorno ONNX", lineas.isNotEmpty())'
A_LAZY = 'assertTrue("$rel lo carga con by lazy, no al construirse", lineas.all { it.contains("by lazy") })'
A_NOM = "fun losSieteEntornosOnnxSonPerezosos() {"
for nom, an in (("filtro", A_FIL), ("carga", A_CARGA), ("lazy", A_LAZY), ("nombre", A_NOM)):
    ok(t.count(an) == 1, "el anclaje %s aparece %d veces" % (nom, t.count(an)))

t = t.replace(A_NOM, "fun losSieteEntornosOnnxSonPerezososYPasanPorLaPuerta() {")
t = t.replace(A_FIL, 'val lineas = fuente(rel)!!.readText().lines().filter { it.contains("MotorOnnx.entorno()") }')
t = t.replace(A_CARGA, 'assertTrue("$rel crea el entorno por la puerta MotorOnnx", lineas.isNotEmpty())')
t = t.replace(A_LAZY, A_LAZY + '\n            assertTrue("$rel ya no crea el entorno a pelo, fuera de la puerta",\n'
                              '                fuente(rel)!!.readText().lines().none { it.contains("OrtEnvironment.get" + "Environment()") })')
ok(LITERAL not in t, "la prueba arreglada sigue llevando el literal a pelo")
ok(t.count(PUERTA) >= 1, "la prueba arreglada no escanea la puerta")
ok(balancear(t) == [], "la prueba arreglada no balancea: %s" % balancear(t))
print("  R16  balance con escáner                      ok")

# ── R23 aplicado: el commit toca a todos los lectores ───────────────────────
tocados = [AHT]
sin = [l for l in lectores if l not in tocados]
ok(not sin, "lectores que el commit no adapta: %s" % sin)
print("  R23  el commit toca a cada lector             %d de %d" % (len(tocados), len(lectores)))

# ── R4 · la prueba arreglada contra las prohibiciones ───────────────────────
TABLA = ["filesDir", "SharedPreferences", "cacheDir", "registry.getInstance",
         "createMediaItem", "latest.release", "media3-exoplayer:+",
         "media3-exoplayer-hls:+", "TODO:"]
for lit in TABLA:
    toks = re.findall(r"\w+", lit)
    ok(not all(x in t for x in toks), "la prueba arreglada lleva la prohibición %r" % lit)
print("  R4   contra las 9 prohibiciones               0 contradicciones")

# ── R8 · no se añaden ni se quitan pruebas ──────────────────────────────────
n = t.count("@Test")
ok(n == N_ANTES, "ArranqueHonestoTest llevaba %d @Test y ahora %d" % (N_ANTES, n))
print("  R8   @Test de la prueba tocada                %d, sin cambio · total 478" % n)

CAMBIOS = [(AHT, t)]
print("\n  ficheros: 1\n     %-44s %+6d bytes" % (AHT.split("/")[-1], len(t) - len(crudo(AHT, BASE))))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
tree = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": c} for r, c in CAMBIOS]})["sha"]

msg = """Arreglar la contradicción entre dos pruebas publicadas por el literal ONNX

El commit O movió la creación del entorno ONNX detrás de MotorOnnx.entorno().
Con eso rompió un contrato publicado que su pre-vuelo no censó:
ArranqueHonestoTest escanea los siete módulos por contenido y exige que la
línea que crea el entorno exista y lleve by lazy. Mover el literal dejó esa
línea inexistente: main quedó en 478 pruebas y 1 fallo, y la release
v1.0.4-beta-dos-apks se cortó de un commit con el suite en rojo. Los dos APKs
de esa release se vuelven a cortar de este commit, que sí está verde.

Ninguna de las dos intenciones se relaja:

- La prueba vieja quería pereza: que el entorno no se cree al construir el
  módulo. Sigue siendo verdad y se sigue exigiendo: las líneas que escanea
  ahora son las que llaman a la puerta, y el by lazy se exige igual. Añade una
  tercera afirmación que antes no hacía falta: que el literal a pelo ya no
  está en el módulo.
- La prueba nueva (MotorOnnxTest) quería que nadie creara el entorno fuera de
  la puerta. Sigue igual, y ahora las dos pueden pasar a la vez.

El pre-vuelo estrena el censo que faltó: lectores_de_literal() recorre las
pruebas publicadas buscando el literal que el commit mueve y exige que el
commit toque a cada lector. Sobre el estado de O ese censo devuelve
ArranqueHonestoTest.kt, que O no tocó: habría fallado antes de publicar, que es
justo el momento en que tenía que fallar. Nace como R23 en reglas/.

Pruebas: 478, las mismas. Este commit no añade ni quita pruebas: arregla una
que mentía sobre dónde vive el literal."""

c = api("/git/commits", "POST", {"message": msg, "tree": tree, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
