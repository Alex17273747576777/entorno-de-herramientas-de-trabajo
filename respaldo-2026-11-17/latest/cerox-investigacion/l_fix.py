#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit M: arreglar el YAML que L publicó roto, y publicar la regla que lo caza.

Dos cosas, y la segunda es la que importa.

1. L añadió al flujo del APK la derivación de la etiqueta y de la lista de cambios. La
   continuación de una sustitución de mandato se escribió en la columna 0 del fichero,
   dentro de un bloque de varias líneas que pedía diez espacios de sangría. En YAML eso
   cierra el bloque y lo que sigue es una clave que no existe. GitHub lo reportó como un
   run fallido sin ningún job y con el nombre en forma de ruta. Las 472 pruebas salieron
   en verde al lado: ninguna leía los flujos.

2. Se publica `FlujosValidosTest`, que recorre `.github/workflows/*.yml` y comprueba la
   regla estructural que se rompió, sin biblioteca de YAML: dentro de un bloque literal,
   toda línea con menos sangría que el bloque tiene que ser una clave o un elemento de
   lista. Si es otra cosa, cuelga fuera. Lleva su muestra mala —el fallo exacto— y su
   muestra buena, y una prueba de que encuentra los flujos, para que no pueda pasar sin
   haber mirado nada.

Añadir el fichero bajo `android/**` no es un relleno para disparar CI: es lo que hace que
el fallo no vuelva. De paso, `pruebas.yml` sí se dispara y verifica también el flujo
arreglado contra `FirmaNuevaTest`, que lo lee.
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import balancear, bloques_literales, solo_codigo, yaml_valido  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
RAW = "https://raw.githubusercontent.com/Alex17273747576777/cero-X-app"
BASE_ESPERADO = "1d592c6bcd127bc22198b337217d10a2b0defb54"
APK = ".github/workflows/apk.yml"
PRUEBAS_YML = ".github/workflows/pruebas.yml"
TEST_NUEVO = "android/app/src/test/java/com/ceroX/app/core/FlujosValidosTest.kt"
PRUEBAS_ANTES = 472
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitM"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


def crudo(ruta, sha):
    with urllib.request.urlopen("%s/%s/%s" % (RAW, sha, ruta), timeout=120) as x:
        return x.read().decode("utf-8")


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movió: %s (esperado %s)" % (BASE[:8], BASE_ESPERADO[:8]))
print("MODO: %s · base %s" % ("PUBLICACIÓN" if EJECUTAR else "DRY-RUN", BASE[:8]))

apk_antes = crudo(APK, BASE)
pyml = crudo(PRUEBAS_YML, BASE)

# ══════════════════════════════════════════════════════════════════════════
#  1 · el arreglo del flujo
# ══════════════════════════════════════════════════════════════════════════
VIEJO = """          if [ -n "$ANTERIOR" ]; then
            CAMBIOS="Cambios desde $ANTERIOR:
$(git log --oneline --no-decorate "$ANTERIOR"..HEAD | sed 's/^/            · /')"
          else
"""
NUEVO = """          if [ -n "$ANTERIOR" ]; then
            # La línea de abajo lleva la sangría del bloque a propósito. En la columna
            # 0 cierra el bloque literal y el flujo deja de ser YAML válido: GitHub lo
            # reporta como un run fallido sin ningún job, que no dice nada útil. Con la
            # sangría del bloque, el mandato la ve en su columna 0, que es lo que
            # necesita la continuación de una cadena entrecomillada.
            CAMBIOS="Cambios desde $ANTERIOR:
          $(git log --oneline --no-decorate "$ANTERIOR"..HEAD | sed 's/^/  · /')"
          else
"""
n = apk_antes.count(VIEJO)
ok(n == 1, "el ancla del arreglo aparece %d veces, se esperaba 1" % n)
apk = apk_antes.replace(VIEJO, NUEVO)

# ══════════════════════════════════════════════════════════════════════════
#  2 · la prueba que lo vigila desde ahora
# ══════════════════════════════════════════════════════════════════════════
K = '''package com.ceroX.app.core

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File

/**
 * Que los flujos de GitHub Actions se puedan leer.
 *
 * DE DÓNDE VIENE
 * --------------
 * Un commit añadió al flujo del APK la derivación de la etiqueta y de la lista de
 * cambios. La continuación de una sustitución de mandato se escribió en la columna 0 del
 * fichero, dentro de un bloque de varias líneas que pedía diez espacios de sangría. En
 * YAML eso cierra el bloque, y lo que viene después ya no es un mandato: es una clave
 * que no existe. GitHub lo reportó como un run fallido **sin ningún job** y con el nombre
 * en forma de ruta, que es como dice «no he podido ni leer el fichero».
 *
 * Las 472 pruebas salieron en verde al lado del run fallido. Ninguna leía los flujos:
 * una prueba de JVM no los toca y el compilador no los ve. Ésta sí los lee.
 *
 * QUÉ COMPRUEBA
 * -------------
 * La regla estructural que se rompió, sin necesitar una biblioteca de YAML en el
 * classpath: dentro de un bloque literal, toda línea con menos sangría que el bloque
 * tiene que ser una clave o un elemento de lista. Si es otra cosa, cuelga fuera del
 * bloque y el fichero ya no es válido.
 *
 * No es un validador de YAML completo y no pretende serlo: es el detector del fallo que
 * ocurrió, que es lo que una prueba de este proyecto hace con cada fallo que ocurre.
 */
class FlujosValidosTest {

    private val raiz: File = run {
        var d = File(".").absoluteFile
        while (!File(d, ".github/workflows").isDirectory && d.parentFile != null) {
            d = d.parentFile
        }
        require(File(d, ".github/workflows").isDirectory) { "no se encontró el repositorio" }
        d
    }

    private val flujos: List<File>
        get() = File(raiz, ".github/workflows").listFiles { f -> f.extension == "yml" }
            ?.sortedBy { it.name }
            ?: emptyList()

    /** `clave: |` o `clave: |-`, que abre un bloque literal. */
    private val apertura = Regex("""^(\\s*)[^\\s#][^:]*:\\s*\\|[-+]?\\s*$""")

    /** Lo que sí puede aparecer con menos sangría: una clave o un elemento de lista. */
    private val claveOLista = Regex("""^\\s*(?:-\\s)?[^\\s:][^:]*:(?:\\s|$)""")

    /** Líneas que cuelgan fuera de la sangría del bloque literal donde nacieron. */
    private fun colgando(texto: String): List<String> {
        val lineas = texto.split("\\n")
        val problemas = mutableListOf<String>()
        var i = 0
        while (i < lineas.size) {
            val m = apertura.find(lineas[i])
            if (m == null) {
                i++
                continue
            }
            var j = i + 1
            while (j < lineas.size && lineas[j].isBlank()) j++
            if (j >= lineas.size) break
            val sangria = lineas[j].length - lineas[j].trimStart().length
            if (sangria <= m.groupValues[1].length) {
                i = j
                continue
            }
            var k = j
            while (k < lineas.size) {
                val l = lineas[k]
                if (l.isBlank()) {
                    k++
                    continue
                }
                if (l.length - l.trimStart().length >= sangria) {
                    k++
                    continue
                }
                if (claveOLista.containsMatchIn(l) || l.trim() == "...") break
                problemas.add("línea " + (k + 1) + ": " + l.trim().take(60))
                break
            }
            i = maxOf(k, i + 1)
        }
        return problemas
    }

    @Test
    fun `la puerta encuentra los flujos del repo`() {
        // Sin esto la prueba pasaría sin haber mirado nada, que es la forma más tonta
        // de tener una puerta: un recorrido vacío no encuentra culpables.
        assertTrue("no se leyó ningún flujo", flujos.size >= 2)
        assertTrue("falta el flujo del APK", flujos.any { it.name == "apk.yml" })
        assertTrue("falta el flujo de las pruebas", flujos.any { it.name == "pruebas.yml" })
    }

    @Test
    fun `ninguna linea cuelga fuera de la sangria de su bloque`() {
        val culpables = mutableListOf<String>()
        for (f in flujos) {
            for (p in colgando(f.readText())) {
                culpables.add(f.name + " " + p)
            }
        }
        assertEquals(
            "líneas fuera de la sangría de su bloque literal. El flujo deja de ser YAML " +
                "válido y GitHub lo reporta como un run fallido sin ningún job, que no " +
                "dice dónde está el fallo: hay que leer el fichero",
            emptyList<String>(),
            culpables,
        )
    }

    @Test
    fun `la puerta caza la columna cero que rompio el flujo`() {
        // La muestra mala es el fallo exacto, no uno parecido. Una puerta que no caza
        // su propio incidente es decoración.
        val roto = listOf(
            "jobs:",
            "  apk:",
            "    steps:",
            "      - name: Publicar",
            "        run: |",
            "          if [ -n \\"\\$X\\" ]; then",
            "            CAMBIOS=\\"Cambios desde \\$X:",
            "\\$(git log --oneline)",
            "          fi",
        ).joinToString("\\n")
        val bien = roto.replace("\\n\\$(git log", "\\n            \\$(git log")

        assertTrue("no caza el fallo que la produjo", colgando(roto).isNotEmpty())
        assertEquals("acusa un texto que está bien", emptyList<String>(), colgando(bien))
    }
}
'''

# R6 · los escapes se comprueban sobre la forma que Kotlin va a leer, y las cifras se
#      derivan: las dos pasadas anteriores esperaban literales escritos a mano (seis
#      `\$` cuando había cinco; `(\s|$)` cuando el texto lleva `(?:\s|$)`; `"\$X"`
#      cuando en Kotlin va `\"\$X\"`) y fallaron diciendo que el contenido estaba mal
#      estando bien.
crudas = re.findall(r'"""(.*?)"""', K)
ok(len(crudas) == 2, "hay %d cadenas crudas, se esperaban las 2 regex" % len(crudas))
ok(not any("\\\\" in c for c in crudas),
   "una cadena cruda lleva doble barra: Kotlin no la procesa y la regex buscaría una "
   "barra literal")
ok(all(re.search(r"\\[sS]", c) for c in crudas),
   "a las cadenas crudas se les fueron las barras al pasar por Python")
region = K.split("val roto = listOf(")[1].split('assertEquals("acusa')[0]
ok(not re.search(r"(?<!\\)\$", region),
   "hay un dólar sin escapar en la muestra: Kotlin lo leería como interpolación")
ok("\\$X" in region and "\\$(git log" in region,
   "los escapes de la muestra no llegaron al fichero")

CAMBIOS = [(APK, apk), (TEST_NUEVO, K)]

# ══════════════════════════════════════════════════════════════════════════
#  PRE-VUELO
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "═" * 74)
print("PRE-VUELO")
print("═" * 74)

# R20 · YAML válido, y la puerta tiene que acusar al fichero de antes
for ruta, texto in [(APK, apk), (PRUEBAS_YML, pyml)]:
    problemas = yaml_valido(texto) + bloques_literales(texto)
    ok(not problemas, "%s no es YAML válido: %s" % (ruta, problemas[:2]))
ok(yaml_valido(apk_antes) or bloques_literales(apk_antes),
   "la puerta no acusa al fichero roto: no serviría de nada")
print("  R20  YAML de los 2 flujos                     válido · y el de antes falla como debe")

# R16 · balance con escáner en el Kotlin nuevo
des = balancear(K)
ok(not des, "símbolos mal cerrados en la prueba nueva: %s" % des[:2])
print("  R16  balance con escáner                      ok en la prueba nueva")

# R5 · lo que FirmaNuevaTest exige del flujo
EXIGIDOS = ["org.gradle.jvmargs", ":app:assembleRelease", "-PsinModelos", "apksigner",
            "entorno/HUELLA-CERTIFICADO.txt", "onnx", "secrets.CEROX_KEYSTORE_B64"]
prueba = crudo("android/app/src/test/java/com/ceroX/app/core/engine/FirmaNuevaTest.kt", BASE)
for lit in EXIGIDOS:
    ok(lit in prueba, "el literal %r ya no lo exige la prueba: el censo está viejo" % lit)
    ok(lit in apk, "apk.yml perdió %r, que FirmaNuevaTest exige" % lit)
ok("BEGIN PRIVATE KEY" not in apk, "apk.yml ganó la clave en claro")
print("  R5   censo de FirmaNuevaTest                  %d literales preservados" % len(EXIGIDOS))

# R4 · la prueba nueva no puede exigir lo que el proyecto prohíbe. Se reproduce el
#      escaneo de CoherenciaDePruebasTest sobre el fichero nuevo.
TABLA = ["filesDir", "SharedPreferences", "cacheDir", "registry.getInstance",
         "createMediaItem", "latest.release", "media3-exoplayer:+", "media3-exoplayer-hls:+",
         "TODO:"]
contradicciones = []
lineas = K.split("\n")
for i, l in enumerate(lineas):
    if "contains(" not in l:
        continue
    for lit in TABLA:
        pre = r"(?<![A-Za-z0-9_])" if lit[0].isalnum() or lit[0] == "_" else ""
        if re.search(pre + re.escape(lit), l):
            asercion = None
            for j in range(i, max(-1, i - 8) - 1, -1):
                if "assertTrue" in lineas[j]:
                    asercion = True
                    break
                if "assertFalse" in lineas[j]:
                    asercion = False
                    break
            if asercion:
                contradicciones.append("%s:%d" % (TEST_NUEVO, i + 1))
ok(not contradicciones, "la prueba nueva exige algo prohibido: %s" % contradicciones)
print("  R4   la prueba nueva contra las 9 prohibiciones 0 contradicciones")

# R1/R2 · prosa que no cita lo prohibido, ni en el flujo ni en la prueba
for ruta, texto in CAMBIOS:
    for lit in TABLA:
        ok(lit not in texto, "%s cita %r en su prosa" % (ruta, lit))
print("  R1   la prosa describe y no cita              0 citas en los %d ficheros" % len(CAMBIOS))

# R10 · el heredoc de la nota
nota = apk.split("cat > notas.md <<NOTAS")[1].split("\n          NOTAS")[0]
ok("`" not in nota, "backticks dentro del heredoc: se ejecutarían")
sust = sorted(set(re.findall(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)", nota)))
ok(set(sust) <= {"GITHUB_SHA", "ABI", "TAM", "MIB", "SUMA", "HUELLA_TXT", "CAMBIOS"},
   "el heredoc expande variables no previstas: %s" % sust)
print("  R10  heredoc de la nota                       0 backticks · expansiones %s" % sust)

# R6 · el mandato como lo verá el corredor, sacado del parser
import yaml
doc = yaml.safe_load(apk)
paso = [x for x in doc["jobs"]["apk"]["steps"] if x.get("name") == "Publicar la release"]
ok(len(paso) == 1, "hay %d pasos con ese nombre" % len(paso))
mandato = paso[0]["run"]
ok('CAMBIOS="Cambios desde $ANTERIOR:\n$(git log' in mandato,
   "deducida la sangría por el parser, la continuación no queda en la columna 0")
ok("sed 's/^/  · /'" in mandato, "la sangría de la lista no es la del resto de la nota")
print("  R6   el mandato que verá el corredor          la continuación cae en su columna 0")

# R14 · la prueba nueva no afirma más de lo que comprueba
ok("No es un validador de YAML completo" in K, "la prueba se presenta como lo que no es")
print("  R14  la prueba dice lo que no es              ok")

# R8 · el número de pruebas del mensaje se deriva, no se escribe a mano
n_tests = K.count("@Test")
ok(n_tests == 3, "la prueba nueva lleva %d @Test, se esperaban 3" % n_tests)
print("  R8   @Test contados                           %d · pruebas %d → %d"
      % (n_tests, PRUEBAS_ANTES, PRUEBAS_ANTES + n_tests))

print("\n  ficheros: %d" % len(CAMBIOS))
for ruta, texto in CAMBIOS:
    antes = apk_antes if ruta == APK else None
    delta = len(texto) - (len(antes) if antes is not None else 0)
    print("     %-62s %+7d bytes%s"
          % (ruta, delta, "" if antes is not None else "  (NUEVO)"))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arbol = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": t} for r, t in CAMBIOS]})["sha"]

msg = """Arreglar el YAML del flujo del APK, y publicar la prueba que lo caza

Dos cosas, y la segunda es la que importa.

EL FALLO. El commit anterior añadió al flujo del APK la derivación de la etiqueta y de
la lista de cambios. La continuación de una sustitución de mandato se escribió en la
columna 0 del fichero, dentro de un bloque de varias líneas que pedía diez espacios de
sangría. En YAML eso cierra el bloque, y lo que viene después ya no es un mandato: es
una clave que no existe. GitHub lo reportó como un run fallido sin ningún job y con el
nombre en forma de ruta, que es como dice «no he podido ni leer el fichero».

Las 472 pruebas salieron en verde al lado del run fallido. Ninguna prueba de JVM lee un
flujo y el compilador no lo ve. El pre-vuelo del commit tenía balance de símbolos para
los ficheros Kotlin y no tenía nada para los flujos: se comprobaba lo que se sabía
comprobar, no lo que el commit tocaba.

EL ARREGLO. La continuación lleva los diez espacios del bloque. Entonces el YAML la
sigue viendo dentro y el mandato la ve en su columna 0, que es lo que necesita la
continuación de una cadena entrecomillada. Va un comentario encima diciendo por qué esa
línea lleva esa sangría, para que nadie la «arregle» alineándola a la izquierda. De paso
la lista de cambios cambia de sangría propia: antes cada commit salía con doce espacios
delante y ahora con dos más el punto, que es el estilo del resto de la nota.

LA PRUEBA. FlujosValidosTest recorre .github/workflows/*.yml y comprueba la regla
estructural que se rompió, sin necesitar una biblioteca de YAML en el classpath: dentro
de un bloque literal, toda línea con menos sangría que el bloque tiene que ser una clave
o un elemento de lista. Si es otra cosa, cuelga fuera. Tres pruebas:

  1. Que encuentra los flujos. Sin ésta, un recorrido vacío no encuentra culpables y la
     puerta pasa sin haber mirado nada, que es la forma más tonta de tener una puerta.
  2. Que ninguna línea cuelga fuera de la sangría de su bloque, en los flujos del repo.
  3. Que caza el fallo exacto que la produjo, con su muestra buena al lado. Una puerta
     que no caza su propio incidente es decoración.

No es un validador de YAML completo y no se presenta como tal: es el detector del fallo
que ocurrió, que es lo que este proyecto hace con cada fallo que ocurre.

Comprobaciones antes de publicar: el YAML de los dos flujos válido con dos detectores, y
comprobado que el fichero ANTERIOR al arreglo falla —si no falla, la puerta no está
mirando lo que cree mirar, y eso es peor que no tenerla—; balance de símbolos con
escáner en la prueba nueva; los 7 literales que FirmaNuevaTest exige del flujo siguen
ahí, verificados primero contra la prueba que los exige; la prueba nueva pasada por el
escaneo de contradicciones de CoherenciaDePruebasTest contra las 9 prohibiciones; el
heredoc de la nota sin backticks y sin expansiones no previstas; y el mandato de la
release sacado del parser de YAML para ver dónde cae de verdad la continuación, en vez
de deducir la sangría a mano, que fue como la comprobación anterior falló sin decir
dónde.

Pruebas: 472 → 475."""

c = api("/git/commits", "POST", {"message": msg, "tree": arbol, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
