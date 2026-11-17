#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit O · 1.0.4-beta-dos-apks: dos APKs por release, universal sin motor ONNX.

Decisión del usuario, no mía: una release acumula un APK por arquitectura. El
universal va **sin** los .so de ONNX (15,7 MB por arquitectura con cero modelos
dentro); el de arm64 los conserva. Y todos los nativos viajan comprimidos.

Qué toca y por qué:

1. `build.gradle`: versionCode 9, versionName 1.0.4-beta-dos-apks, y un bloque
   de empaquetado condicional (`-PsinOnnxNative`) que excluye los dos .so de
   ONNX. Las clases de onnxruntime4j se quedan: pesan kilobytes y son las que
   dejan que MotorOnnx detecte la ausencia y la diga.
2. `AndroidManifest.xml`: `extractNativeLibs="true"`. Hoy los .so van SIN
   comprimir para que el sistema los mapee del APK; con esto viajan deflate y
   se extraen al instalar. El APK baja; la instalación ocupa lo mismo.
3. `apk.yml`: el universal añade `-PsinOnnxNative`; y cada run sube sus assets
   con nombre de arquitectura (`app-<abi>.apk`, `sha256sums-<abi>.txt`), que es
   lo que faltaba para que el segundo dispatch al mismo tag no pisara al
   primero: el paso ya era idempotente (`gh release view` → upload --clobber),
   pero los dos runs subían el mismo nombre de fichero.
4. `core/MotorOnnx.kt`: la puerta del motor. `estado()` devuelve el motivo por
   el que la biblioteca nativa no está, o null; `entorno()` lanza con ese
   motivo en vez de dejar que un UnsatisfiedLinkError —que es un Error, no un
   Exception— cruce código que sólo caza Exception. Los nueve sitios que crean
   el entorno pasan por ella, y los healthCheck de los tres módulos que lo
   tienen reportan el estado del motor: decir «funcionando» en una variante
   sin motor sería otra verdad vieja publicada.
5. `core/MotorOnnxTest.kt`: 3 @Test, incluida una puerta que recorre las
   fuentes y no deja que nadie cree el entorno a pelo fuera de MotorOnnx.

Uso: export GP=<token fino> && python3 -B o_commit.py [--run]
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import (balancear, bloques_literales, mandato_de_paso,  # noqa: E402
                   sintaxis_de_mandato, yaml_valido)

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
RAW = "https://raw.githubusercontent.com/Alex17273747576777/cero-X-app"
GRADLE = "android/app/build.gradle"
MANIF = "android/app/src/main/AndroidManifest.xml"
APK = ".github/workflows/apk.yml"
MOTOR = "android/app/src/main/java/com/ceroX/app/core/MotorOnnx.kt"
TESTN = "android/app/src/test/java/com/ceroX/app/core/MotorOnnxTest.kt"
ONNX_FICH = [
    "android/app/src/main/java/com/ceroX/app/modules/ai/ModelAssets.kt",
    "android/app/src/main/java/com/ceroX/app/modules/ai/ModelManager.kt",
    "android/app/src/main/java/com/ceroX/app/modules/ai_training/AiTrainingModule.kt",
    "android/app/src/main/java/com/ceroX/app/modules/kisara/KisaraColorizer.kt",
    "android/app/src/main/java/com/ceroX/app/modules/kisara/KisaraNeuralColorizerModule.kt",
    "android/app/src/main/java/com/ceroX/app/modules/kisara/KisaraOcrTranslatorModule.kt",
    "android/app/src/main/java/com/ceroX/app/modules/kisara/KisaraUpscaler.kt",
    "android/app/src/main/java/com/ceroX/app/modules/kisara/MangaOcrEngine.kt",
    "android/app/src/main/java/com/ceroX/app/modules/neural_colorizer/NeuralColorizer.kt",
]
LLAMADA = "OrtEnvironment.getEnvironment()"
PRUEBAS_ANTES = 475          # run 43136625803, línea «475 pruebas · 0 fallos · …»
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitO"})
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

g = crudo(GRADLE, BASE)
mf = crudo(MANIF, BASE)
y = crudo(APK, BASE)
mods = {r: crudo(r, BASE) for r in ONNX_FICH}

# ── R10 · anclajes contados ─────────────────────────────────────────────────
A_VER = '        versionCode 8\n        versionName "1.0.3-beta-notas"'
A_PACK = "        pickFirsts = []\n    }"
A_MAN = '        android:name=".core.CeroXApplication"\n        android:allowBackup="true"'
A_ABI = 'if [ "$ABI" != "universal" ]; then ARGS="$ARGS -PsoloAbi=$ABI"; fi'
A_NOM = 'NOMBRE="$(basename "$APK")"'
A_UP = 'gh release upload "$ETIQUETA" "$APK" sha256sums.txt --clobber'
A_CR = 'gh release create "$ETIQUETA" "$APK" sha256sums.txt \\'
A_NOTA = "          · Arquitectura: $ABI (una sola, no universal)."
for nom, txt, an in (("build.gradle", g, A_VER), ("build.gradle/pack", g, A_PACK),
                     ("manifest", mf, A_MAN), ("apk.yml/abi", y, A_ABI),
                     ("apk.yml/nombre", y, A_NOM), ("apk.yml/upload", y, A_UP),
                     ("apk.yml/create", y, A_CR), ("apk.yml/nota", y, A_NOTA)):
    ok(txt.count(an) == 1, "el anclaje %s aparece %d veces" % (nom, txt.count(an)))

g = g.replace(A_VER, '        versionCode 9\n        versionName "1.0.4-beta-dos-apks"')
g = g.replace(A_PACK, A_PACK + """

    // Variante universal sin el motor ONNX: las clases de onnxruntime4j se
    // quedan (pesan kilobytes y son las que dejan que MotorOnnx detecte la
    // ausencia y la diga); los .so, 15,7 MB por arquitectura con cero modelos
    // dentro, no viajan. Se activa con -PsinOnnxNative, que añade el flujo
    // cuando la arquitectura pedida es universal.
    if (project.hasProperty('sinOnnxNative')) {
        packagingOptions {
            jniLibs {
                excludes += '**/libonnxruntime.so'
                excludes += '**/libonnxruntime4j_jni.so'
            }
        }
    }""")
mf = mf.replace(A_MAN, '        android:name=".core.CeroXApplication"\n'
                       '        android:extractNativeLibs="true"\n'
                       '        android:allowBackup="true"')
y = y.replace(A_ABI, A_ABI + """
          # El universal viaja sin el motor ONNX y con los nativos comprimidos:
          # 15,7 MB por arquitectura con cero modelos dentro no se le suben a
          # nadie. El de arm64 conserva el motor para cuando haya modelos.
          if [ "$ABI" = "universal" ]; then ARGS="$ARGS -PsinOnnxNative"; fi""")
y = y.replace(A_NOM, 'NOMBRE="app-$ABI.apk"\n'
                     '          cp "$APK" "$NOMBRE"\n'
                     '          cp sha256sums.txt "sha256sums-$ABI.txt"')
y = y.replace(A_UP, 'gh release upload "$ETIQUETA" "$NOMBRE" "sha256sums-$ABI.txt" --clobber')
y = y.replace(A_CR, 'gh release create "$ETIQUETA" "$NOMBRE" "sha256sums-$ABI.txt" \\')
y = y.replace(A_NOTA, """          · Arquitectura de este run: $ABI. Esta release acumula un APK por
            arquitectura: cada dispatch con publicar=true sube el suyo con su
            nombre (app-<abi>.apk) y su suma, y no pisa los de los demás runs.
            El universal va sin el motor ONNX; el de arm64 lo conserva.""")

# ── los nueve sitios del entorno, por la puerta ─────────────────────────────
n_sitios = 0
n_health = 0
for r in ONNX_FICH:
    t = mods[r]
    cu = t.count(LLAMADA)
    ok(cu >= 1, "%s ya no crea el entorno: nada que sustituir" % r)
    t = t.replace(LLAMADA, "MotorOnnx.entorno()")
    ok(t.count("import ai.onnxruntime.OrtEnvironment") >= 1,
       "%s no importa OrtEnvironment: no sé dónde poner la puerta" % r)
    t = t.replace("import ai.onnxruntime.OrtEnvironment",
                  "import ai.onnxruntime.OrtEnvironment\nimport com.ceroX.app.core.MotorOnnx", 1)
    if "healthCheck(" in t:
        # El mapOf que hay que tocar es el de DENTRO de healthCheck, no el
        # primero del fichero: meter el estado del motor en otro mapa sería
        # compilar bien y mentir igual.
        i = t.index("healthCheck(")
        cabeza, cola = t[:i], t[i:]
        for ancla in ("mapOf<String, Any?>(", "mapOf("):
            if ancla in cola:
                cola = cola.replace(ancla, ancla + '\n                "motor_onnx" to '
                                                   '(MotorOnnx.estado() ?: "nativo presente"),', 1)
                t = cabeza + cola
                n_health += 1
                break
        else:
            raise SystemExit("FALLO DE COMPROBACION: %s tiene healthCheck sin mapOf" % r)
    mods[r] = t
    n_sitios += cu
ok(n_health == 3, "se cablearon %d healthCheck, se esperaban 3" % n_health)
print("  R10  anclajes y sitios                       %d sitios del entorno · %d healthCheck"
      % (n_sitios, n_health))

# ── la puerta del motor y su prueba ─────────────────────────────────────────
MOTOR_KT = '''package com.ceroX.app.core

import ai.onnxruntime.OrtEnvironment

/**
 * La puerta del motor ONNX.
 *
 * `estado()` dice por qué la biblioteca nativa no está, o null si está. No dice
 * que el motor funcione: decir eso exigiría cargar un modelo y ejecutarlo, y
 * esta puerta no hace ninguna de las dos cosas. `entorno()` devuelve el
 * entorno o lanza con el motivo, porque un [UnsatisfiedLinkError] es un Error y
 * no un Exception: sin esta puerta, una variante sin los .so reventaría cruzando
 * código que sólo caza Exception, que es justo lo que la variante universal
 * necesita no hacer.
 */
object MotorOnnx {

    fun estado(cargador: () -> Any? = { OrtEnvironment.getEnvironment() }): String? =
        try {
            cargador()
            null
        } catch (t: Throwable) {
            "motor ONNX no disponible en esta variante: " +
                (t.message ?: t.javaClass.simpleName)
        }

    fun entorno(): OrtEnvironment {
        val motivo = estado()
        if (motivo != null) throw IllegalStateException(motivo)
        return OrtEnvironment.getEnvironment()
    }
}
'''
TEST_KT = '''package com.ceroX.app.core

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.io.File

/**
 * La puerta del motor, comprobada. La tercera prueba es una puerta publicada:
 * recorre las fuentes y no deja que nadie cree el entorno ONNX a pelo fuera de
 * MotorOnnx, que es la forma de que la variante sin .so no reviente por un
 * camino que nadie vigiló.
 */
class MotorOnnxTest {

    @Test
    fun cargadorQueRevientaDaMotivoYSilencioNo() {
        val motivo = MotorOnnx.estado({ throw UnsatisfiedLinkError("libonnxruntime.so") })
        assertNotNull("un cargador que revienta tiene que dar motivo", motivo)
        assertTrue("el motivo tiene que llevar lo que faltó: %s".format(motivo),
            motivo!!.contains("libonnxruntime.so"))
        assertTrue("el motivo tiene que decir que es el motor: %s".format(motivo),
            motivo.contains("motor ONNX no disponible"))
    }

    @Test
    fun cargadorSanoDaNulo() {
        assertNull(MotorOnnx.estado({ Any() }))
    }

    @Test
    fun nadieCreaElEntornoAPeloFueraDeLaPuerta() {
        var d = File(".").absoluteFile
        while (d.parentFile != null && !File(d, "android/app/src/main/java").isDirectory) {
            d = d.parentFile
        }
        val raiz = File(d, "android/app/src/main/java/com/ceroX/app")
        assertTrue("no encontré las fuentes desde %s".format(d), raiz.isDirectory)
        val llamada = "%s%s".format("OrtEnvironment.get", "Environment(")
        val culpables = raiz.walkTopDown()
            .filter { it.isFile && it.name.endsWith(".kt") && it.name != "MotorOnnx.kt" }
            .filter { it.readText().contains(llamada) }
            .map { it.name }
            .toList()
        assertEquals("el entorno se crea sólo en MotorOnnx.kt, no en %s".format(culpables),
            emptyList<String>(), culpables)
    }
}
'''
ok(balancear(MOTOR_KT) == [], "la puerta no balancea: %s" % balancear(MOTOR_KT))
ok(balancear(TEST_KT) == [], "la prueba no balancea: %s" % balancear(TEST_KT))
print("  R16  balance con escáner                      puerta y prueba ok")

# ── R20/R21 · el flujo, tras cuatro sustituciones ───────────────────────────
probs = yaml_valido(y) + bloques_literales(y)
ok(not probs, "el flujo nuevo no se lee: %s" % probs[:1])
guion, p2 = mandato_de_paso(y, "Publicar la release")
ok(guion is not None and not p2, "no encontré el paso de publicar: %s" % p2)
probs += sintaxis_de_mandato(guion)
ok(not probs, "el paso de publicar no pasa bash -n: %s" % probs[:1])
ok('NOMBRE="app-$ABI.apk"' in guion and '"sha256sums-$ABI.txt"' in guion,
   "el paso de publicar no sube con nombre de arquitectura")
gb, p3 = mandato_de_paso(y, "Construir el APK de release, sin modelos")
ok(gb is not None and not p3 and "-PsinOnnxNative" in gb,
   "el paso de construir no añade -PsinOnnxNative para el universal")
print("  R20  YAML y shell del flujo                   válidos · assets con nombre de ABI")

# ── R5 · lo que FirmaNuevaTest exige sigue en el flujo ──────────────────────
EXIGIDOS = ["org.gradle.jvmargs", ":app:assembleRelease", "-PsinModelos", "apksigner",
            "entorno/HUELLA-CERTIFICADO.txt", "onnx", "secrets.CEROX_KEYSTORE_B64"]
fp = crudo("android/app/src/test/java/com/ceroX/app/core/engine/FirmaNuevaTest.kt", BASE)
for lit in EXIGIDOS:
    ok(lit in fp, "el censo está viejo: la prueba ya no exige %r" % lit)
    ok(lit in y, "apk.yml perdió %r, que FirmaNuevaTest exige" % lit)
ok("BEGIN PRIVATE KEY" not in y, "apk.yml ganó la clave en claro")
print("  R5   censo de FirmaNuevaTest                  %d literales preservados" % len(EXIGIDOS))

# ── R4 · lo nuevo, pasado por las prohibiciones publicadas ──────────────────
TABLA = ["filesDir", "SharedPreferences", "cacheDir", "registry.getInstance",
         "createMediaItem", "latest.release", "media3-exoplayer:+",
         "media3-exoplayer-hls:+", "TODO:"]
for nom, txt in (("MotorOnnx.kt", MOTOR_KT), ("MotorOnnxTest.kt", TEST_KT)):
    for lit in TABLA:
        toks = re.findall(r"\w+", lit)
        if all(t in txt for t in toks):
            raise SystemExit("FALLO DE COMPROBACION: %s lleva la prohibición %r" % (nom, lit))
print("  R4   lo nuevo contra las 9 prohibiciones      0 contradicciones")

# ── R8 · conteos derivados ───────────────────────────────────────────────────
n_tests = TEST_KT.count("@Test")
ok(n_tests == 3, "la prueba nueva lleva %d @Test" % n_tests)
print("  R8   pruebas                                  %d → %d" % (PRUEBAS_ANTES, PRUEBAS_ANTES + n_tests))

CAMBIOS = [(GRADLE, g), (MANIF, mf), (APK, y), (MOTOR, MOTOR_KT), (TESTN, TEST_KT)]
CAMBIOS += [(r, mods[r]) for r in ONNX_FICH]
print("\n  ficheros: %d" % len(CAMBIOS))
for ruta, texto in CAMBIOS:
    antes = crudo(ruta, BASE) if ruta not in (MOTOR, TESTN) else ""
    print("     %-44s %+6d bytes%s" % (ruta.split("/")[-1], len(texto) - len(antes),
                                       "" if antes else "  (NUEVO)"))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arbol = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": t} for r, t in CAMBIOS]})["sha"]

msg = """1.0.4-beta-dos-apks: un APK por arquitectura, y el universal sin motor ONNX

Decisión tomada en consulta, no supuesta: cada release acumula un APK por
arquitectura. El universal viaja sin los .so de ONNX y el de arm64 los
conserva. Medido sobre el APK de la 1.0.2 (33,0 MB): el 53,7 % son bibliotecas
nativas y la mitad de eso es un solo fichero, libonnxruntime.so, 15,7 MB
guardado sin comprimir, con cero modelos .onnx dentro: el motor de una IA que
hoy no tiene nada que cargar. Meterlo cuatro veces en un universal sería
pagar 63 MB de motor por una capacidad que no se ejerce.

CAMBIOS.

1. build.gradle: versionCode 9 y un bloque condicional -PsinOnnxNative que
   excluye los dos .so de ONNX del empaquetado. Las clases de onnxruntime4j se
   quedan: son kilobytes y son lo que permite detectar la ausencia.
2. AndroidManifest: extractNativeLibs=true. Hasta hoy los .so viajaban sin
   comprimir para que el sistema los mapeara directo del APK; ahora viajan
   deflate y se extraen al instalar. El APK baja bastante; el espacio
   instalado queda igual. Es el intercambio correcto para una app que se baja
   por red y no por Play.
3. apk.yml: el universal añade -PsinOnnxNative al Gradle, y cada run sube sus
   assets con nombre de arquitectura (app-<abi>.apk y su suma). El paso de
   publicar ya era idempotente —si la etiqueta existe, sube con --clobber en
   vez de crear—, pero los dos runs subían el mismo nombre de fichero y el
   segundo pisaba al primero: ésa era la pieza que faltaba para que dos APKs
   convivieran en una release.
4. core/MotorOnnx.kt: la puerta del motor. estado() da el motivo de la
   ausencia o null; entorno() lanza con ese motivo. Sin puerta, un
   UnsatisfiedLinkError —que es un Error, no un Exception— cruzaría código
   que sólo caza Exception y la variante sin motor reventaría en vez de
   explicarse. Los nueve sitios que creaban el entorno pasan por ella y los
   tres healthCheck que hay reportan el estado del motor: decir «funcionando»
   en una variante sin motor sería otra verdad vieja publicada, que es el
   vicio que el commit L vino a cerrar.
5. core/MotorOnnxTest.kt: __TESTS__ pruebas nuevas, incluida una que recorre
   las fuentes y no deja crear el entorno a pelo fuera de la puerta.

Pruebas: __PRUEBAS__ → __DESPUES__. Lo que este commit NO demuestra: cuánto
pesa cada variante. Eso lo dicen los dos dispatch que vienen detrás, con sus
bytes medidos, no una estimación."""
msg = (msg.replace("__TESTS__", str(n_tests))
          .replace("__PRUEBAS__", str(PRUEBAS_ANTES))
          .replace("__DESPUES__", str(PRUEBAS_ANTES + n_tests)))
ok("__" not in msg, "quedó un marcador sin sustituir en el mensaje")

c = api("/git/commits", "POST", {"message": msg, "tree": arbol, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
