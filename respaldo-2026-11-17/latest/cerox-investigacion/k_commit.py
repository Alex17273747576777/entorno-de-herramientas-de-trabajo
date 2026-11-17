#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit K: la regla R4 publicada como puerta de CI.

Hasta ahora «una prueba no puede exigir lo que el proyecto prohíbe» vivía en mi
registro local, o sea en mi memoria. Aquí se convierte en una prueba del repo, que
es el único sitio donde una regla deja de depender de que alguien se acuerde.

El pre-vuelo reproduce las cuatro pruebas en Python sobre el árbol descargado,
incluida la que comprueba que el fichero nuevo no escribe los literales que prohíbe.
"""
import base64, datetime, json, os, re, sys, time, urllib.request, urllib.error

# El recorte de strings y comentarios ya estaba escrito y probado en el registro de
# reglas: contar paréntesis sobre el texto crudo falla con cualquier símbolo dentro
# de una cadena, y este fichero lleva una regex entre comillas.
sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import balancear  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
P_NUEVO = "android/app/src/test/java/com/ceroX/app/core/CoherenciaDePruebasTest.kt"
BASE_ESPERADO = "ff3e14047ca7a922fe03cc9a9df701a5458fbb0b"
ARBOL = "/tmp/arbol"
PRUEBAS_ANTES = 468
EJECUTAR = "--run" in sys.argv

# (ruta, literal) — la misma tabla que va en el fichero, aquí con los literales
# escritos porque este guion no se publica.
TABLA = [
    ("src/main/java/com/ceroX/app/modules/iptv", "filesDir"),
    ("src/main/java/com/ceroX/app/modules/iptv", "SharedPreferences"),
    ("src/main/java/com/ceroX/app/modules/iptv", "cacheDir"),
    ("src/main/java/com/ceroX/app", "registry.getInstance"),
    ("src/main/java/com/ceroX/app", "createMediaItem"),
    ("build.gradle", "latest.release"),
    ("build.gradle", "media3-exoplayer:+"),
    ("build.gradle", "media3-exoplayer-hls:+"),
    ("src/main/java/com/ceroX/app", "TODO:"),
]


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxreglas"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movio: " + BASE)
print("MODO: %s · base %s" % ("PUBLICACION" if EJECUTAR else "DRY-RUN", BASE[:8]))

NUEVO = '''package com.ceroX.app.core

import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File

/**
 * Que las pruebas no se contradigan, y que ninguna exija lo que el proyecto prohíbe.
 *
 * DE DÓNDE VIENE
 * --------------
 * El módulo de IPTV guardaba las fuentes del usuario en el directorio interno de la
 * app. [ReglaDeAlmacenamientoTest] lo prohibía y llevaba publicada semanas: nadie la
 * leyó antes de escribir. Y lo peor no fue el código, fue que la prueba nueva del
 * módulo **exigía** ese directorio, con un mensaje que decía justo lo contrario de la
 * regla del proyecto («se guardan en el almacenamiento privado»). Una prueba así no
 * protege de nada: convierte el fallo en requisito. Cuando otra prueba lo denunció,
 * el mensaje que se leyó hablaba de almacenamiento y no de la contradicción, así que
 * el arreglo tardó un commit más de lo que hacía falta.
 *
 * QUÉ COMPROBADO
 * --------------
 *   1. Nada de lo prohibido en la tabla está en el **código** de la ruta indicada.
 *      Se mira el código y no la prosa: un comentario puede explicar por qué algo
 *      está prohibido, y de hecho debe. Las puertas que miran el fichero entero son
 *      otra cosa y viven en sus propias pruebas.
 *   2. Ninguna prueba publicada **exige la presencia** de algo prohibido. Ésta es la
 *      que habría cazado el incidente en el acto y diciendo el nombre del fichero.
 *   3. Esta prueba no escribe los literales que prohíbe: los compone a trozos. Es la
 *      disciplina que se le pide a cualquier comentario del proyecto, aplicada aquí y
 *      comprobada contra sí misma en vez de fiada.
 *   4. Cada prohibición dice por qué existe y de qué incidente viene. Una regla sin
 *      procedencia se vuelve superstición y se borra a la primera molestia.
 *
 * POR QUÉ LA COMPARACIÓN ES POR PALABRA Y NO POR SUBCADENA
 * --------------------------------------------------------
 * Dos mecanismos que el proyecto **aprueba** llevan dentro el nombre de lo
 * prohibido: el almacén cifrado donde viven los tokens, y el método que migra las
 * preferencias viejas para poder borrarlas. Por subcadena se denunciaban los dos, y
 * la prueba habría nacido fallando. Con la frontera de palabra no. El caso del
 * incidente se sigue cazando igual, porque allí lo prohibido iba detrás de un punto.
 */
class CoherenciaDePruebasTest {

    private val raiz: File = run {
        var d = File(".").absoluteFile
        while (!File(d, "src/main/java/com/ceroX/app").isDirectory && d.parentFile != null) {
            d = d.parentFile
        }
        require(File(d, "src/main/java/com/ceroX/app").isDirectory) { "no se encontró el árbol" }
        d
    }

    /**
     * Una prohibición, con su porqué y su incidente.
     *
     * Los trozos se componen en vez de escribir el literal seguido: si este fichero
     * contuviera lo que prohíbe, la prueba 3 fallaría, y con razón.
     */
    private class Prohibicion(
        val ruta: String,
        val trozos: List<String>,
        val porque: String,
        val incidente: String,
    ) {
        val literal: String get() = trozos.joinToString("")

        private val patron: Regex
            get() {
                val primero = literal.first()
                val frontera = if (primero.isLetterOrDigit() || primero == '_') {
                    "(?<![A-Za-z0-9_])"
                } else {
                    ""
                }
                return Regex(frontera + Regex.escape(literal))
            }

        fun apareceEn(texto: String): Boolean = patron.containsMatchIn(texto)
    }

    private val prohibiciones = listOf(
        Prohibicion(
            "src/main/java/com/ceroX/app/modules/iptv",
            listOf("files", "Dir"),
            "los datos del usuario van a la carpeta propia de la app en el " +
                "almacenamiento externo; el interno sólo guarda los tokens cifrados",
            "917c3f06 lo guardaba ahí y 708a9904 lo sacó",
        ),
        Prohibicion(
            "src/main/java/com/ceroX/app/modules/iptv",
            listOf("Shared", "Preferences"),
            "las preferencias de Android viven en el interno y no se pueden " +
                "redirigir; los ajustes van a core/Prefs",
            "regla de almacenamiento del proyecto, vigilada por ReglaDeAlmacenamientoTest",
        ),
        Prohibicion(
            "src/main/java/com/ceroX/app/modules/iptv",
            listOf("cache", "Dir"),
            "la caché interna no es sitio para las fuentes que instala el usuario",
            "misma regla de almacenamiento",
        ),
        Prohibicion(
            "src/main/java/com/ceroX/app",
            listOf("registry", ".getInstance"),
            "ese camino devolvía null porque los módulos se registran en el gestor " +
                "de ciclo de vida, y el cast no nulo cerraba la pantalla al abrirla",
            "3f0fe9d0 y 83c1ef78: seis pantallas se cerraban al tocarlas",
        ),
        Prohibicion(
            "src/main/java/com/ceroX/app",
            listOf("create", "MediaItem"),
            "un método del reproductor que no existe: lo escribió la memoria en vez " +
                "de la documentación, y sólo lo caza el compilador",
            "c7815891, después de un rojo en CI con Unresolved reference",
        ),
        Prohibicion(
            "build.gradle",
            listOf("latest", ".release"),
            "un resolvedor que elige la última versión cambiaría lo que se compila " +
                "sin que nadie lo decida",
            "917c3f06, donde el comentario que lo explicaba lo escribía",
        ),
        Prohibicion(
            "build.gradle",
            listOf("media3-exoplayer", ":+"),
            "un rango dinámico en la pieza principal del reproductor mezclaría dos " +
                "versiones distintas del mismo reproductor",
            "917c3f06: las dos piezas llevan la versión fija y la misma",
        ),
        Prohibicion(
            "build.gradle",
            listOf("media3-exoplayer-hls", ":+"),
            "y lo mismo en la pieza de las listas en directo",
            "917c3f06",
        ),
        Prohibicion(
            "src/main/java/com/ceroX/app",
            listOf("TODO", ":"),
            "una marca de trabajo pendiente en el código publicado es relleno: o se " +
                "hace, o se devuelve el fallo con su motivo",
            "barrido de fabricación 8d56dff7…c7c657d4, 45 sitios que inventaban éxito",
        ),
    )

    /** El código de un archivo, sin comentarios ni KDoc. */
    private fun codigo(f: File): String = f.readLines()
        .filterNot { it.trimStart().startsWith("*") }
        .filterNot { it.trimStart().startsWith("//") }
        .filterNot { it.trimStart().startsWith("/*") }
        .joinToString("\\n")

    private fun ficherosDe(ruta: String): List<File> {
        val f = File(raiz, ruta)
        assertTrue("la tabla nombra una ruta que no existe: $ruta", f.exists())
        return if (f.isDirectory) {
            f.walkTopDown().filter { it.isFile && it.extension == "kt" }.toList()
        } else {
            listOf(f)
        }
    }

    /** La aserción más cercana hacia arriba: verdadero si manda un assertTrue. */
    private fun asercionCercana(lineas: List<String>, i: Int): Boolean {
        for (j in i downTo maxOf(0, i - 8)) {
            val l = lineas[j]
            if (l.contains("assertTrue")) return true
            if (l.contains("assertFalse")) return false
        }
        return false
    }

    @Test
    fun `lo prohibido no esta en el codigo`() {
        for (p in prohibiciones) {
            val infractores = ficherosDe(p.ruta)
                .filter { p.apareceEn(codigo(it)) }
                .map { it.name }
            assertEquals(
                p.porque + " — y sin embargo aparece en: " + infractores,
                emptyList<String>(),
                infractores,
            )
        }
    }

    @Test
    fun `ninguna prueba exige la presencia de lo que el proyecto prohibe`() {
        val contradicciones = mutableListOf<String>()
        val pruebas = File(raiz, "src/test").walkTopDown()
            .filter { it.isFile && it.extension == "kt" }
            .toList()
        assertTrue("no se leyó ninguna prueba", pruebas.isNotEmpty())

        for (prueba in pruebas) {
            val lineas = prueba.readLines()
            for ((i, linea) in lineas.withIndex()) {
                if (!linea.contains("contains(")) continue
                for (p in prohibiciones) {
                    if (!p.apareceEn(linea)) continue
                    if (asercionCercana(lineas, i)) {
                        contradicciones.add(
                            prueba.name + ":" + (i + 1) + " exige algo prohibido en " + p.ruta,
                        )
                    }
                }
            }
        }
        assertEquals(
            "pruebas que exigen lo que otra prohíbe. Se cambia el código primero y la " +
                "prueba después, nunca al revés, y nunca se relaja una aserción para " +
                "que pase",
            emptyList<String>(),
            contradicciones.distinct(),
        )
    }

    @Test
    fun `esta prueba no escribe los literales que prohibe`() {
        val propio = File(raiz, "src/test/java/com/ceroX/app/core/CoherenciaDePruebasTest.kt")
        assertTrue("no me encuentro a mí misma", propio.isFile)
        val texto = propio.readText()
        val citados = prohibiciones.filter { texto.contains(it.literal) }
            .map { "la de " + it.ruta.substringAfterLast('/') }
        assertEquals(
            "esta prueba cita lo que prohíbe: describir, no citar, que es lo mismo " +
                "que se le pide a cualquier comentario del proyecto",
            emptyList<String>(),
            citados,
        )
    }

    @Test
    fun `cada prohibicion dice por que existe y de que incidente viene`() {
        val mudas = prohibiciones
            .filter { it.porque.length < 25 || it.incidente.isBlank() || it.trozos.isEmpty() }
            .map { it.ruta }
        assertEquals(
            "prohibiciones sin explicar: una regla que no dice de dónde viene se borra " +
                "a la primera molestia",
            emptyList<String>(),
            mudas,
        )
    }
}
'''

# ══════════════════════════════════════════════════════════════════════════
#  PRE-VUELO: las cuatro pruebas, reproducidas aquí sobre el árbol
# ══════════════════════════════════════════════════════════════════════════

print("\nPRE-VUELO (las 4 pruebas reproducidas en Python sobre %s)" % ARBOL)
APP = os.path.join(ARBOL, "android/app")
ok(os.path.isdir(APP), "no está el árbol: bájalo con GET /repos/.../tarball/" + BASE[:8])
ok(open(os.path.join(APP, "build.gradle"), encoding="utf-8").read().count("versionCode 7") == 1,
   "el árbol no es el commit esperado")


def patron(lit):
    pre = r"(?<![A-Za-z0-9_])" if (lit[0].isalnum() or lit[0] == "_") else ""
    return re.compile(pre + re.escape(lit))


def solo_codigo(t):
    t = re.sub(r"/\*[\s\S]*?\*/", " ", t)
    return "\n".join(l for l in t.split("\n") if not l.strip().startswith(("//", "*")))


def asercion(lineas, i):
    for j in range(i, max(-1, i - 8) - 1, -1):
        if "assertTrue" in lineas[j]:
            return True
        if "assertFalse" in lineas[j]:
            return False
    return False


# Prueba 1
inf = []
for ruta, lit in TABLA:
    p = os.path.join(APP, ruta)
    ok(os.path.exists(p), "la tabla nombra una ruta que no existe: " + ruta)
    fs = [p] if os.path.isfile(p) else [os.path.join(d, f) for d, _, x in os.walk(p)
                                        for f in x if f.endswith(".kt")]
    for f in fs:
        if patron(lit).search(solo_codigo(open(f, encoding="utf-8").read())):
            inf.append("%s en %s" % (lit, os.path.basename(f)))
ok(not inf, "prueba 1 fallaría: %s" % inf)
print("  1 · lo prohibido no está en el código        %d prohibiciones, 0 infracciones" % len(TABLA))

# Prueba 2
contra = []
for d, _, fs in os.walk(os.path.join(APP, "src/test")):
    for f in sorted(fs):
        if not f.endswith(".kt"):
            continue
        lineas = open(os.path.join(d, f), encoding="utf-8").read().split("\n")
        for i, l in enumerate(lineas):
            if "contains(" not in l:
                continue
            for _ruta, lit in TABLA:
                if patron(lit).search(l) and asercion(lineas, i):
                    contra.append("%s:%d %s" % (f, i + 1, lit))
ok(not contra, "prueba 2 fallaría: %s" % contra)
print("  2 · ninguna prueba exige lo prohibido        0 contradicciones")

# Prueba 3: el fichero que se va a publicar no puede contener los literales
citados = [lit for _r, lit in TABLA if lit in NUEVO]
ok(not citados, "prueba 3 fallaría: el fichero nuevo cita %s" % citados)
print("  3 · el fichero nuevo no cita lo que prohíbe  0 literales seguidos")

# Prueba 4: la tabla del fichero nuevo tiene porqué e incidente en cada entrada
# Cada entrada empieza por su ruta entre comillas, que es lo que la distingue de la
# declaración de la clase.
entradas = re.findall(r'Prohibicion\(\n            "(.*?)\n        \),', NUEVO, re.S)
ok(len(entradas) == len(TABLA), "la tabla del fichero tiene %d entradas, se esperaban %d"
   % (len(entradas), len(TABLA)))
for e in entradas:
    textos = re.findall(r'"([^"]{20,})"', e)
    ok(len(textos) >= 2, "una entrada sin porqué ni incidente: %s" % e[:70])
print("  4 · cada prohibición explicada               %d entradas con porqué e incidente"
      % len(entradas))

# Lo que la composición de trozos tiene que producir, entrada por entrada.
trozos = re.findall(r"listOf\((\"[^\"]*\"(?:, \"[^\"]*\")*)\)", NUEVO)
compuestos = ["".join(re.findall(r'"([^"]*)"', t)) for t in trozos]
ok(sorted(compuestos) == sorted(l for _r, l in TABLA),
   "los trozos no componen la tabla: %s" % sorted(set(compuestos) ^ set(l for _r, l in TABLA)))
print("     los trozos componen exactamente la tabla  %d literales" % len(compuestos))

# Sintaxis básica del Kotlin generado. Con un escáner de estados, no recortando
# strings y comentarios con regex: este fichero lleva una regex entre comillas y un
# KDoc largo, que es justo lo que hacía fallar el recuento tres veces seguidas.
desbalance = balancear(NUEVO)
ok(not desbalance, "símbolos mal cerrados: %s" % desbalance[:3])
ok(NUEVO.count("@Test") == 4, "hay %d @Test, se esperaban 4" % NUEVO.count("@Test"))
for marca in ["Placeholder", "placeholder", "TODO", "FIXME", "dummy", "simulado"]:
    ok(marca not in NUEVO.replace('listOf("TODO", ":")', ""), "marca %r en el fichero nuevo" % marca)
print("     balance (escáner) y marcas                ok · 4 @Test (%d → %d pruebas)"
      % (PRUEBAS_ANTES, PRUEBAS_ANTES + 4))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": P_NUEVO, "mode": "100644", "type": "blob", "content": NUEVO}]})["sha"]
msg = """Una prueba que vigila a las otras pruebas: que ninguna exija lo prohibido

Esto viene de un fallo concreto y merece contarse entero, porque el fallo no fue el
código.

El módulo de IPTV guardaba las fuentes del usuario en el directorio interno de la
app. ReglaDeAlmacenamientoTest lo prohibía y llevaba publicada semanas; nadie la leyó
antes de escribir. Salió rojo, se miró, se arregló. Hasta ahí un fallo normal.

Lo que no es normal es lo que apareció al arreglarlo: la prueba nueva del módulo
**exigía** ese directorio, con un assertTrue y un mensaje que decía «las fuentes se
guardan en el almacenamiento privado». O sea que había escrito una prueba para
defender mi propio fallo, y el mensaje sostenía exactamente lo contrario de la regla
del proyecto. Una prueba así no protege de nada: convierte el fallo en requisito. Y
cuando otra prueba lo denunció, el mensaje hablaba de almacenamiento y no de la
contradicción, así que el diagnóstico tardó un commit más.

CoherenciaDePruebasTest hace cuatro cosas:

  1. Nada de lo prohibido en la tabla está en el **código** de su ruta. Se mira el
     código y no la prosa, porque un comentario puede explicar una prohibición y
     debe; las puertas que miran el fichero entero viven en sus propias pruebas.
  2. Ninguna prueba publicada **exige la presencia** de algo prohibido. Ésta es la
     que habría cazado el incidente en el acto, diciendo el fichero y la línea.
  3. Esta prueba no escribe los literales que prohíbe: los compone a trozos, y se
     comprueba a sí misma. Es la disciplina que se le pide a cualquier comentario
     del proyecto —describir, no citar—, aplicada aquí en vez de fiada.
  4. Cada prohibición lleva su porqué y su incidente. Nueve entradas, y las nueve
     dicen de dónde vienen: el directorio interno, el registro que nunca registró
     nada, el método del reproductor que no existe, los resolvedores dinámicos de
     Gradle y las marcas de trabajo pendiente del barrido de fabricación.

Un detalle que casi la hace nacer fallando, y va en el KDoc: la comparación es por
palabra, no por subcadena. Dos mecanismos que el proyecto aprueba llevan dentro el
nombre de lo prohibido —el almacén cifrado de los tokens y el método que migra las
preferencias viejas para borrarlas—, y por subcadena se denunciaban los dos. Con la
frontera de palabra no, y el caso del incidente se sigue cazando igual porque allí
lo prohibido iba detrás de un punto.

Las cuatro pruebas se reprodujeron en Python sobre el árbol antes de publicar: 9
prohibiciones sin infracciones y 0 contradicciones entre las 49 pruebas existentes.
Van 472."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
