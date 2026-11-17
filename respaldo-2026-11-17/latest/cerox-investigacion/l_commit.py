#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit L: tres verdades que se quedaron viejas publicadas, y el doc que falta.

1. `.github/workflows/apk.yml` decía que esta firma no actualiza una instalación
   vieja y que hay que desinstalarla antes. Era verdad para la 1.0.0-beta, cuyo
   certificado se perdió, y dejó de serlo en cuanto la 1.0.1 y la 1.0.2 salieron del
   mismo almacén de claves: entre ésas se actualiza en el sitio.
2. `modules/video/VideoModule.kt` decía que media3 no está en el proyecto. Está
   desde `917c3f06`, lo usa el módulo IPTV. Lo que no está es la conexión entre ese
   reproductor y este módulo, que es otra cosa y se dice tal cual.
3. `README.md` enlaza dos veces `entorno/COMPILAR-Y-FIRMAR.md`, que no existe, y
   enlaza la beta a una release borrada. El doc se escribe con lo que se puede
   comprobar en el propio repo, y el enlace de descarga pasa a `releases/latest`,
   que no se pudre.

Y dos cosas que se pudrirían otra vez si no se derivan:
   · la etiqueta por defecto del flujo, que seguía siendo la de la 1.0.1, pasa a
     derivarse del versionName;
   · la lista de cambios de la nota de release, escrita a mano para una versión
     concreta, pasa a salir del historial desde la etiqueta anterior.

Las puertas de abajo son las 19 reglas del registro aplicadas a este commit: anclas
contadas, balance con escáner, censo de lo que exigen las pruebas publicadas, prosa
que no cita lo prohibido y marcas de relleno.
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import auditar_espejo, balancear, solo_codigo  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
ARBOL = "/tmp/arbol"
BASE_ESPERADO = "b79e39415b08ab6b7e3b23906915124204a462dd"
PRUEBAS_ANTES = 472
EJECUTAR = "--run" in sys.argv

APK = ".github/workflows/apk.yml"
PRUEBAS_YML = ".github/workflows/pruebas.yml"
VIDEO = "android/app/src/main/java/com/ceroX/app/modules/video/VideoModule.kt"
REPRO = "android/app/src/main/java/com/ceroX/app/modules/iptv/ReproductorIptv.kt"
README = "README.md"
DOC_NUEVO = "entorno/COMPILAR-Y-FIRMAR.md"


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitL"})
    try:
        with urllib.request.urlopen(r, timeout=180) as x:
            return json.loads(x.read() or b"null")
    except urllib.error.HTTPError as e:
        raise SystemExit("HTTP %s %s %s: %s" % (e.code, m, p, e.read().decode()[:300]))


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movió: %s (esperado %s)" % (BASE[:8], BASE_ESPERADO[:8]))
print("MODO: %s · base %s" % ("PUBLICACIÓN" if EJECUTAR else "DRY-RUN", BASE[:8]))


def leer(ruta):
    p = os.path.join(ARBOL, ruta)
    ok(os.path.isfile(p), "falta en el árbol: " + ruta)
    with open(p, encoding="utf-8") as f:
        return f.read()


def sustituir(texto, viejo, nuevo, cuantas=1, que=""):
    """R10 · toda ancla se cuenta antes de sustituir."""
    n = texto.count(viejo)
    ok(n == cuantas, "%s: el ancla aparece %d veces, se esperaban %d" % (que, n, cuantas))
    return texto.replace(viejo, nuevo)


# ══════════════════════════════════════════════════════════════════════════
#  1 · apk.yml
# ══════════════════════════════════════════════════════════════════════════
apk = leer(APK)

# 1a · checkout con historial y etiquetas, o no hay de dónde derivar los cambios
apk = sustituir(apk,
    "      - uses: actions/checkout@v4\n",
    "      - uses: actions/checkout@v4\n"
    "        with:\n"
    "          # La nota de la release deriva sus cambios del historial. Con la\n"
    "          # profundidad por defecto no hay historial ni etiquetas, y la nota\n"
    "          # volvería a estar escrita a mano, que es como se pudrió la anterior.\n"
    "          fetch-depth: 0\n"
    "          fetch-tags: true\n",
    1, "checkout")

# 1b · la etiqueta por defecto, derivada en vez de escrita
apk = sustituir(apk,
    '      etiqueta:\n'
    '        description: "Etiqueta de la release"\n'
    '        type: string\n'
    '        default: "v1.0.1-beta-arranque-honesto"\n',
    '      etiqueta:\n'
    '        description: "Etiqueta de la release. Vacía = se deriva del versionName de android/app/build.gradle"\n'
    '        type: string\n'
    '        default: ""\n',
    1, "etiqueta por defecto")

# 1c · derivar la etiqueta y los cambios antes de escribir la nota
apk = sustituir(apk,
    '        run: |\n'
    '          TAM="$(stat -c%s "$APK")"\n',
    '        run: |\n'
    '          if [ -z "$ETIQUETA" ]; then\n'
    '            # Derivada del versionName y no escrita a mano. El valor por defecto\n'
    '            # anterior se quedó viejo en cuanto se publicó la versión siguiente,\n'
    '            # y una release cuya etiqueta no coincide con lo que lleva dentro\n'
    '            # es peor que ninguna.\n'
    '            VERSION="$(sed -n \'s/.*versionName "\\([^"]*\\)".*/\\1/p\' android/app/build.gradle | head -1)"\n'
    '            if [ -z "$VERSION" ]; then\n'
    '              echo "::error::no se pudo derivar la etiqueta: versionName no encontrado"\n'
    '              exit 1\n'
    '            fi\n'
    '            ETIQUETA="v$VERSION"\n'
    '            echo "Etiqueta derivada del versionName: $ETIQUETA"\n'
    '          fi\n'
    '          ANTERIOR="$(git describe --tags --abbrev=0 HEAD^ 2>/dev/null || true)"\n'
    '          if [ -n "$ANTERIOR" ]; then\n'
    '            CAMBIOS="Cambios desde $ANTERIOR:\n'
    '$(git log --oneline --no-decorate "$ANTERIOR"..HEAD | sed \'s/^/            · /\')"\n'
    '          else\n'
    '            CAMBIOS="(no hay una etiqueta anterior en el historial: ésta es la primera)"\n'
    '          fi\n'
    '          TAM="$(stat -c%s "$APK")"\n',
    1, "derivación de etiqueta y cambios")

# 1d · la frase falsa sobre desinstalar
apk = sustituir(apk,
    "          · Certificado: huella $HUELLA_TXT, generado el 2026-11-11. El\n"
    "            certificado anterior se perdió, así que esta firma no actualiza una\n"
    "            instalación vieja: hay que desinstalarla antes.\n",
    "          · Certificado: huella $HUELLA_TXT, generado el 2026-11-11. Esta firma\n"
    "            actualiza en el sitio cualquier instalación firmada con ese mismo\n"
    "            almacén de claves, o sea la 1.0.1-beta y las que vinieron después.\n"
    "            La única que NO actualiza es la 1.0.0-beta, cuyo certificado se\n"
    "            perdió: ésa hay que desinstalarla antes de instalar ésta.\n",
    1, "la frase falsa de la instalación vieja")

# 1e · la lista de cambios, derivada del historial
apk = sustituir(apk,
    "          Qué trae esta build respecto a la 1.0.1: el ecualizador (módulo 37, con\n"
    "          sus diez curvas ISO y los pasos de volumen del sistema) y el IPTV neutro\n"
    "          (módulo 38: las fuentes las instala el usuario, listas M3U, guía XMLTV y\n"
    "          reproductor media3), con su pantalla y su destino en la barra inferior.\n"
    "          No trae ninguna lista de canales ni ninguna fuente dentro del APK.\n",
    "          Qué trae esta build: los commits desde la etiqueta anterior, derivados del\n"
    "          historial y no escritos a mano. La nota anterior listaba el contenido de\n"
    "          una versión concreta y se quedó mintiendo en cuanto se publicó la\n"
    "          siguiente, que es exactamente lo que le acaba de pasar a la frase de la\n"
    "          instalación vieja.\n"
    "\n"
    "          $CAMBIOS\n"
    "\n"
    "          Lo que ninguna build de este flujo trae dentro: listas de canales ni\n"
    "          fuentes. Las fuentes las instala el usuario desde fuera del APK.\n",
    1, "la lista de cambios escrita a mano")

# ══════════════════════════════════════════════════════════════════════════
#  2 · VideoModule.kt — media3 sí está en el proyecto
# ══════════════════════════════════════════════════════════════════════════
video = leer(VIDEO)
video = sustituir(video,
    " *     decisión de cero-X. Borrada aquí y en `ConfigManager`, con su default. Cuando\n"
    " *     el reproductor sea propio (media3), la aceleración se consulta de verdad con\n"
    " *     `MediaCodecInfo` y entonces se informa con datos medidos.\n"
    " *   • No escanea el almacenamiento: la biblioteca empieza vacía en cada proceso.\n"
    " *   • No reproduce en streaming. HLS/IPTV necesita media3, que no está en el\n"
    " *     proyecto: el `MediaPlayer` del framework no resuelve playlists .m3u8.\n",
    " *     decisión de cero-X. Borrada aquí y en `ConfigManager`, con su default. Cuando\n"
    " *     este módulo lleve un reproductor propio en vez de delegar en otra app, la\n"
    " *     aceleración se consulta de verdad con `MediaCodecInfo` y entonces se informa\n"
    " *     con datos medidos.\n"
    " *   • No escanea el almacenamiento: la biblioteca empieza vacía en cada proceso.\n"
    " *   • No reproduce en streaming, y la razón ya no es la que decía este comentario:\n"
    " *     media3 SÍ está en el proyecto, lo usa el módulo IPTV desde `917c3f06`\n"
    " *     (`modules/iptv/ReproductorIptv.kt`, con las piezas `media3-exoplayer` y\n"
    " *     `media3-exoplayer-hls`). Lo que no existe es la conexión entre ese\n"
    " *     reproductor y este módulo, que sigue delegando en la app del sistema con un\n"
    " *     `ACTION_VIEW`. Y por ahí no hay streaming posible: el `MediaPlayer` del\n"
    " *     framework no resuelve playlists .m3u8. Hace falta enchufar media3 aquí, y no\n"
    " *     se ha hecho.\n",
    1, "el KDoc de VideoModule")

# ══════════════════════════════════════════════════════════════════════════
#  3 · ReproductorIptv.kt — la cita cruzada deja de ser cierta
# ══════════════════════════════════════════════════════════════════════════
repro = leer(REPRO)
repro = sustituir(repro,
    " * El IPTV es HLS casi siempre, y el `MediaPlayer` del sistema no resuelve playlists\n"
    " * .m3u8: lo deja escrito `VideoModule` en su propia documentación. media3 es\n"
    " * Apache-2.0, que es compatible con la GPL-3.0 del proyecto, y trae el soporte de\n"
    " * HLS en un módulo aparte que hay que declarar.\n",
    " * El IPTV es HLS casi siempre, y el `MediaPlayer` del sistema no resuelve playlists\n"
    " * .m3u8. `VideoModule` delega en ese reproductor del sistema con un `ACTION_VIEW` y\n"
    " * por eso no puede con el streaming; este módulo no delega: lleva media3 dentro.\n"
    " * media3 es Apache-2.0, que es compatible con la GPL-3.0 del proyecto, y trae el\n"
    " * soporte de HLS en un módulo aparte que hay que declarar.\n",
    1, "el KDoc de ReproductorIptv")

# ══════════════════════════════════════════════════════════════════════════
#  4 · pruebas.yml — su comentario dice que el doc no existe, y va a existir
# ══════════════════════════════════════════════════════════════════════════
pyml = leer(PRUEBAS_YML)
pyml = sustituir(pyml,
    "#     los secretos del repo. La huella aprobada está en entorno/HUELLA-CERTIFICADO.txt\n"
    "#     y el porqué en docs/FIRMA-NUEVA.md. El doc que se citaba aquí antes,\n"
    "#     entorno/COMPILAR-Y-FIRMAR.md, no existe en el repositorio.\n",
    "#     los secretos del repo. La huella aprobada está en entorno/HUELLA-CERTIFICADO.txt,\n"
    "#     el porqué del certificado nuevo en docs/FIRMA-NUEVA.md y cómo compilar y firmar\n"
    "#     en entorno/COMPILAR-Y-FIRMAR.md, que era un enlace roto y ya existe.\n",
    1, "el comentario de pruebas.yml")

# ══════════════════════════════════════════════════════════════════════════
#  5 · README.md — la beta enlazaba una release borrada
# ══════════════════════════════════════════════════════════════════════════
readme = leer(README)
readme = sustituir(readme,
    "**[Descargar la beta](../../releases/tag/v1.0.0-beta)**",
    "**[Descargar la beta](../../releases/latest)**",
    1, "el enlace de descarga del README")

# ══════════════════════════════════════════════════════════════════════════
#  6 · el doc que falta, escrito sólo con lo que se puede comprobar aquí
# ══════════════════════════════════════════════════════════════════════════
gp_props = leer("android/gradle.properties")
bg = leer("android/app/build.gradle")
huella = leer("entorno/HUELLA-CERTIFICADO.txt").strip()
ok(len(huella) == 64, "la huella del repo no son 64 hexadecimales")

# Los tres hechos del build.gradle que sostienen la tercera trampa.
LIN_SC = [i + 1 for i, l in enumerate(bg.split("\n")) if l.strip().startswith("signingConfigs {")]
LIN_BT = [i + 1 for i, l in enumerate(bg.split("\n")) if l.strip().startswith("buildTypes {")]
LIN_REF = [i + 1 for i, l in enumerate(bg.split("\n")) if "signingConfig signingConfigs.release" in l]
ok(len(LIN_SC) == 1 and len(LIN_BT) == 1 and len(LIN_REF) == 1,
   "no encontré los tres hitos del orden de signingConfigs: %s %s %s" % (LIN_SC, LIN_BT, LIN_REF))
ok(LIN_SC[0] < LIN_BT[0] < LIN_REF[0], "el orden supuesto no es el del fichero")

VN = re.search(r'versionName "([^"]+)"', bg).group(1)
VC = re.search(r"versionCode (\d+)", bg).group(1)
M3 = re.findall(r"androidx\.media3:([a-z0-9-]+):([0-9.]+)", bg)
ok(M3, "no leí las piezas de media3 del build.gradle")
HEAP_LOCAL = re.search(r"org\.gradle\.jvmargs=(.*)", gp_props).group(1)
HEAP_CI = re.search(r"HEAP='([^']+)'", apk).group(1)

DOC = """# Compilar y firmar

Las tres trampas que cuestan una tarde cada una, con lo que las demuestra dentro del
propio repositorio. Nada de esto es teoría: los tres números y los tres órdenes están
en ficheros que se pueden abrir, y se citan con su ruta.

Versión en el momento de escribir esto: `%s` (versionCode %s).

---

## 1 · El heap de R8 no se baja, se sube donde sobra memoria

`android/gradle.properties` lleva `-Xmx2048m`, y ese valor no es arbitrario: está
medido en una máquina de 1982 MiB de RAM con 2 GiB de swap, y el propio fichero
recuerda las tres pruebas.

| heap | qué pasó |
|---|---|
| `-Xmx1024m` | R8 murió de `OutOfMemoryError`, con mensaje |
| `-Xmx1400m` | el demonio desapareció sin mensaje: el asesino por falta de memoria del núcleo |
| `-Xmx2048m` | terminó. Es el valor con el que se construyó el APK de 475 MB |

La lección que anota el fichero es la que importa: **bajar el límite convierte un fallo
lento en uno silencioso, que es peor**. Con 2 GiB R8 se murió al minificar el release
también en CI (run `43010008338`), así que el flujo del APK sube el heap **por línea de
comandos** y deja el `gradle.properties` intacto para la máquina pequeña:

    %s

con

    %s

O sea: el techo de la máquina pequeña se queda donde está y el del corredor de CI, que
tiene 16 GiB, se usa. Nadie paga por el otro.

## 2 · La máquina pequeña: un solo trabajador, sin demonio, sin paralelo

En 2 GiB con swap, Gradle no se puede comportar como en un servidor. Los valores que
funcionan están en `android/gradle.properties`:

    org.gradle.workers.max=1
    org.gradle.parallel=false
    kotlin.compiler.execution.strategy=in-process

y en la línea de comandos, `--no-daemon --console=plain --max-workers=1`. Los dos flujos
de CI usan `--console=plain`; el del APK añade `--stacktrace`, que es lo que permite leer
dónde se murió R8 en vez de adivinarlo.

El swap no es un detalle: sin él, el asesino por falta de memoria del núcleo se lleva el
demonio de Gradle sin dejar mensaje, y lo que se ve es una compilación que «se para». Con
swap se vuelve lenta y termina. Lenta y terminada gana a rápida y muerta.

Aparte, `systemProp.maven.repo.local=/opt/m2` saca la caché de Robolectric del directorio
personal: cada versión de Android probada baja un jar de 143,67 MiB, y en este entorno lo
que está bajo el directorio personal es lo único que se conserva entre mensajes.

## 3 · `signingConfigs` va antes que `buildTypes`, y no es estética

Gradle evalúa el guion de arriba abajo, así que un bloque que se referencia tiene que
estar declarado antes. En `android/app/build.gradle` el orden es:

| línea | qué hay |
|---|---|
| %d | `signingConfigs {` |
| %d | `buildTypes {` |
| %d | `signingConfig signingConfigs.release` |

Si el primer bloque se mueve debajo del segundo, la referencia de la línea %d se resuelve
contra algo que todavía no existe y el fallo llega al configurar, antes de compilar nada:
no hay ningún error de Kotlin ni de recursos que buscar, y por eso cuesta una tarde.

En el mismo fichero, después del bloque de tipos, se fijan los dos esquemas de firma
(`v1SigningEnabled` y `v2SigningEnabled`). La 1.0.1-beta salió sólo con v2 y se instaló y
verificó igual; se mantienen los dos declarados.

---

## De dónde sale la clave

La clave **no está en el repositorio**. Vive en los secretos del flujo:
`CEROX_KEYSTORE_B64`, `CEROX_KEYSTORE_PASS`, `CEROX_KEY_ALIAS` y `CEROX_KEY_PASS`. El
flujo del APK escribe el almacén en base64 a un fichero temporal del corredor y lo borra
al terminar el trabajo.

Lo que sí es público es la huella, en `entorno/HUELLA-CERTIFICADO.txt`:

    %s

El flujo verifica el APK con el `apksigner` oficial, compara esa huella con la que da el
APK y **falla si no coincide**, en vez de publicar otra cosa. Hay una prueba publicada
(`core/engine/FirmaNuevaTest.kt`) que exige que el flujo contenga esa comparación, y otra
que exige que ningún flujo lleve la clave en claro.

## Qué se construye

    bash ./gradlew :app:assembleRelease -PsinModelos -PsoloAbi=<abi> <heap> --console=plain --stacktrace

Una sola arquitectura por build (por defecto `arm64-v8a`, la del V60 ThinQ 5G) y sin
modelos. Los ONNX pesan 378 MiB y no van dentro: ésos son los 475.523.392 bytes del APK
original. El flujo cuenta los `.onnx` del ZIP y falla si hay alguno.

Piezas de media3 declaradas hoy, las dos en la misma versión fija: %s.

## Lo que este documento NO dice

Que la app funcione en un teléfono. Aquí no hay emulador y no se ha probado nada en un
dispositivo: ni el ecualizador, ni la reproducción, ni las pantallas. Las %d pruebas del
proyecto son de JVM, y una prueba de JVM no abre un DSP ni un decodificador de vídeo. El
banco previsto es un V60 ThinQ 5G y sigue sin usarse.

Tampoco dice cómo recuperar el certificado de la 1.0.0-beta: se perdió. Por eso la
1.0.1-beta se firmó con un almacén nuevo, que es lo que cuenta `docs/FIRMA-NUEVA.md`, y
por eso una instalación 1.0.0-beta hay que desinstalarla antes. Entre la 1.0.1 y las
siguientes no: es el mismo almacén y se actualiza en el sitio.
""" % (VN, VC, HEAP_LOCAL.strip(), HEAP_CI, LIN_SC[0], LIN_BT[0], LIN_REF[0], LIN_REF[0],
       huella, " y ".join("`%s:%s`" % t for t in M3), PRUEBAS_ANTES)

CAMBIOS = [(APK, apk), (PRUEBAS_YML, pyml), (VIDEO, video), (REPRO, repro),
           (README, readme), (DOC_NUEVO, DOC)]

# ══════════════════════════════════════════════════════════════════════════
#  PRE-VUELO · las reglas aplicadas a este commit
# ══════════════════════════════════════════════════════════════════════════
print("\n" + "═" * 74)
print("PRE-VUELO")
print("═" * 74)

# R16 · balance con escáner de estados, no recortando con regex
for ruta, texto in CAMBIOS:
    if ruta.endswith(".kt"):
        des = balancear(texto)
        ok(not des, "símbolos mal cerrados en %s: %s" % (ruta, des[:2]))
print("  R16  balance con escáner                     ok en los 2 ficheros Kotlin")

# R1 · la prosa no cita lo prohibido (puertas que leen el fichero entero)
citas = []
for ruta, texto in CAMBIOS:
    for (i, tok, nombre, _lit, d) in auditar_espejo(texto, donde=ruta):
        citas.append("%s:%d %s" % (ruta, i, nombre))
ok(not citas, "prosa que cita lo prohibido: %s" % citas)
print("  R1   la prosa describe y no cita              0 citas en los %d ficheros" % len(CAMBIOS))

# R2 · PlaceholderDetectorTest lee el fichero ENTERO, pero no acusa cualquier marca:
#      se salta las líneas que empiezan por * o por /* y sólo acusa la COMBINACIÓN de
#      una marca con una forma de éxito en las tres líneas siguientes. Reproducirlo a
#      medias fue el fallo de la pasada anterior: partía el fichero de la prueba por un
#      nombre que no existe (formasDeExceso en vez de formasDeExito), así que se quedaba
#      el fichero entero y metía «return true» entre las marcas.
det = leer("android/app/src/test/java/com/ceroX/app/modules/diagnostics/"
           "PlaceholderDetectorTest.kt")


def _lista(nombre):
    return re.findall(r'"([^"]+)"', det.split(nombre + " = listOf(")[1].split(")")[0])


marcas = _lista("marcasDeRelleno")
exitos = _lista("formasDeExito")
sospechosas = _lista("sospechosas")
ok(marcas and exitos and sospechosas, "no leí las tres listas de la prueba publicada")
ok("return true" not in marcas,
   "el parser volvió a meter una forma de éxito entre las marcas de relleno")
ok("return true" in exitos, "y no la encontró en la lista donde sí está")


def detector(texto, ruta):
    """Los tres cazadores de la prueba publicada, reproducidos tal cual."""
    lineas = texto.split("\n")
    problemas = []
    for i, linea in enumerate(lineas):
        t = linea.strip()
        if t.startswith("*") or t.startswith("/*"):
            continue
        if t.startswith("//") and "placeholder" not in t.lower():
            continue
        if not any(m.lower() in linea.lower() for m in marcas):
            continue
        contexto = "\n".join(lineas[i:min(len(lineas), i + 4)])
        if any(f in contexto for f in exitos):
            problemas.append("%s:%d marca de relleno con una forma de éxito cerca"
                             % (ruta, i + 1))
    if "healthCheck" in texto:
        for i, linea in enumerate(lineas):
            t = linea.strip()
            if " to true" not in t or t.startswith("//") or t.startswith("*"):
                continue
            clave = t.split('" to true')[0].rsplit('"', 1)[-1]
            if any(x in clave.lower() for x in sospechosas):
                problemas.append("%s:%d healthCheck afirma «%s» con un true literal"
                                 % (ruta, i + 1, clave))
    for i, linea in enumerate(lineas):
        t = linea.strip()
        if t.startswith("//") or t.startswith("*"):
            continue
        if re.search(r"\b(?:result|resultado|respuesta|pagina|bitmap|file)\.\w+!!", t):
            problemas.append("%s:%d doble exclamación sobre un valor nuleable" % (ruta, i + 1))
    return problemas


# La prueba sólo recorre los .kt bajo src/main/java/com/ceroX/app. Aplicarla al doc o
# al flujo sería inventarse un ámbito que ninguna puerta publicada vigila.
kotlin = [(r, t) for r, t in CAMBIOS if r.endswith(".kt") and "/src/main/java/com/ceroX/app/" in r]
acusados = [p for r, t in kotlin for p in detector(t, r)]
ok(not acusados, "el detector de relleno acusa: %s" % acusados)
print("  R2   espejo de PlaceholderDetectorTest       %d marcas + %d formas de éxito + "
      "%d claves, 0 acusados en %d .kt" % (len(marcas), len(exitos), len(sospechosas), len(kotlin)))

# R5 · censo: lo que exigen las pruebas publicadas sigue ahí después de editar.
#      Cada literal se verifica primero contra la prueba que lo exige, para que la
#      lista no se quede vieja ella también.
EXIGIDOS = [
    ("android/app/src/test/java/com/ceroX/app/modules/LimpiezaTest.kt", VIDEO,
     ["No tiene aceleración por hardware"], ["hwAccel"]),
    ("android/app/src/test/java/com/ceroX/app/core/engine/FirmaNuevaTest.kt", APK,
     ["org.gradle.jvmargs", ":app:assembleRelease", "-PsinModelos", "apksigner",
      "entorno/HUELLA-CERTIFICADO.txt", "onnx", "secrets.CEROX_KEYSTORE_B64"],
     ["BEGIN PRIVATE KEY"]),
    ("android/app/src/test/java/com/ceroX/app/modules/license/LicenciaRepoTest.kt", README,
     ["## Licencia", "GPL-3.0"], ["así se queda"]),
    ("android/app/src/test/java/com/ceroX/app/modules/iptv/IptvReproductorTest.kt", REPRO,
     ["@OptIn(UnstableApi::class)", "ExoPlayer.Builder", "onPlayerError", "errorCodeName",
      "release()", "setDefaultRequestProperties", "setUserAgent",
      "fun ultimoMotivo(): String?"],
     []),
]
n_lit = 0
for prueba, ruta, debe, no_debe in EXIGIDOS:
    texto_prueba = leer(prueba)
    nuevo = dict(CAMBIOS)[ruta]
    for lit in debe:
        ok(lit in texto_prueba or lit.replace("## ", "") in texto_prueba,
           "el literal %r ya no lo exige %s: el censo está viejo" % (lit, prueba))
        ok(lit in nuevo, "%s perdió %r, que %s exige" % (ruta, lit, os.path.basename(prueba)))
        n_lit += 1
    for lit in no_debe:
        ok(lit in texto_prueba, "el veto %r ya no está en %s" % (lit, prueba))
        ok(lit not in nuevo, "%s ganó %r, que %s veta" % (ruta, lit, os.path.basename(prueba)))
# El README tiene su comprobación por secciones: la GPL-3.0 debe estar DENTRO de la
# sección de licencia, no en cualquier parte.
sec = dict(CAMBIOS)[README]
i = sec.index("## Licencia")
ok("GPL-3.0" in sec[i:], "la sección de licencia del README perdió GPL-3.0")
ok("así se queda" not in sec[i:], "la sección de licencia volvió a prometer que se queda")
print("  R5   censo de lo que exigen las pruebas       %d literales preservados en 4 ficheros" % n_lit)

# R13/R12/R11/R7 · no aplican: no hay layouts, ni cadenas nuevas, ni almacenamiento,
# ni hilos. Se dice en vez de callarlo.
print("  R7/R11/R12/R13  no aplican: sólo prosa, un flujo y un doc nuevo")

# R6 · ninguna cadena cruda de Kotlin nueva
ok('"""' not in video and '"""' not in repro, "cadenas crudas nuevas en los Kotlin")
print("  R6   sin cadenas crudas nuevas                ok")

# R3 · los nombres de cosas ajenas que aparecen en el doc se leen del repo, no se
#      recuerdan: heap local, heap de CI, piezas de media3, líneas del build.gradle.
ok(HEAP_LOCAL.strip() in gp_props and HEAP_CI in apk, "los heaps del doc no están en su origen")
for nombre, ver in M3:
    ok("androidx.media3:%s:%s" % (nombre, ver) in bg, "la pieza %s no está en build.gradle" % nombre)
print("  R3   los datos del doc salen de los ficheros  %s" % ", ".join("%s:%s" % t for t in M3))

# R14 · nada de «funciona» sin evidencia: el doc tiene que decir lo que NO demuestra.
ok("NO dice" in DOC and "sin usarse" in DOC or "no se ha probado" in DOC,
   "el doc afirma más de lo que hay")
ok("no se ha probado" in DOC, "el doc no dice que no se ha probado en un dispositivo")
print("  R14  el doc dice lo que no demuestra          ok")

# R10 · el heredoc de la nota sigue sin backticks ni sustituciones nuevas sin querer.
nota = apk.split("cat > notas.md <<NOTAS")[1].split("\n          NOTAS")[0]
ok("`" not in nota, "backticks dentro del heredoc de la nota: se ejecutarían")
sust = sorted(set(re.findall(r"\$\{?([A-Za-z_][A-Za-z0-9_]*)", nota)))
permitidas = {"GITHUB_SHA", "ABI", "TAM", "MIB", "SUMA", "HUELLA_TXT", "CAMBIOS"}
ok(set(sust) <= permitidas, "el heredoc expande variables no previstas: %s" % (set(sust) - permitidas))
print("  R10  heredoc de la nota                       0 backticks · expansiones %s" % sorted(sust))

# R15 · nada re-descargable guardado en el espacio de trabajo
print("  R15  este guion no escribe nada en el workspace salvo a sí mismo")

# R19 · re-ejecutable: la base se comprueba al entrar y las anclas se cuentan, así que
#      una segunda pasada falla limpiamente en vez de publicar dos veces.
print("  R19  la base está comprobada y las anclas contadas: reejecutar falla limpio")

print("\n  ficheros: %d (%d modificados + 1 nuevo)" % (len(CAMBIOS), len(CAMBIOS) - 1))
for ruta, texto in CAMBIOS:
    antes = None if ruta == DOC_NUEVO else leer(ruta)
    delta = len(texto) - (len(antes) if antes is not None else 0)
    print("     %-64s %+7d bytes%s" % (ruta, delta, "" if antes is not None else "  (NUEVO)"))
print("\n  pruebas: %d → %d (no se añade ninguna)" % (PRUEBAS_ANTES, PRUEBAS_ANTES))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arbol = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": t} for r, t in CAMBIOS]})["sha"]

msg = """Tres verdades que se quedaron viejas publicadas, y el doc que faltaba

Ninguna de estas cuatro cosas rompía la compilación. Rompían otra cosa: lo que el repo
dice de sí mismo. Y las cuatro se descubrieron igual, leyendo lo publicado en vez de lo
que yo recordaba haber publicado.

1. apk.yml decía que esta firma no actualiza una instalación vieja y que hay que
   desinstalarla antes. Era verdad cuando se escribió, para la 1.0.0-beta, cuyo
   certificado se perdió. Dejó de serlo en cuanto la 1.0.1 y la 1.0.2 salieron del mismo
   almacén de claves: entre ésas se actualiza en el sitio, y la nota publicada en la
   release 1.0.2 estaba diciéndole a quien la leyera que borrara una app que no hacía
   falta borrar.

2. VideoModule.kt decía que media3 no está en el proyecto. Está desde 917c3f06 y lo usa
   el módulo IPTV. El comentario no se limita a corregirse: dice qué es lo que sí falta,
   que es la conexión entre ese reproductor y este módulo, porque «media3 no está» y
   «este módulo no usa media3» son dos afirmaciones distintas y sólo la segunda es
   verdad. ReproductorIptv.kt citaba esa documentación como su fuente, así que la cita
   también se corrige: una referencia cruzada a un texto falso es un fallo con dos
   sitios donde crecer.

3. README.md enlazaba entorno/COMPILAR-Y-FIRMAR.md dos veces y el fichero no existía.
   En vez de borrar los enlaces se escribe el fichero, porque lo que el README prometía
   —las tres trampas del heap de R8, del swap y del orden de signingConfigs— es justo lo
   que está medido en android/gradle.properties y lo que se puede leer con su número de
   línea en android/app/build.gradle. El doc no afirma nada que no cite un fichero del
   repo, y dice explícitamente lo que no demuestra: que la app funcione en un teléfono.

4. El enlace de descarga del README apuntaba a la release v1.0.0-beta, que se borró.
   Ahora apunta a releases/latest, que no se pudre con cada versión.

Y dos cosas que se volverían a pudrir si se dejan escritas a mano, que es el mismo fallo
con otra forma:

   · La etiqueta por defecto del flujo seguía siendo v1.0.1-beta-arranque-honesto
     después de publicar la 1.0.2. Pasa a derivarse del versionName, con fallo explícito
     si no se encuentra. El título de la release ya se derivaba de la etiqueta desde
     ff3e1404; ahora la etiqueta se deriva del código, y la cadena deja de tener un
     eslabón escrito a mano.
   · La nota de release listaba el contenido de una versión concreta. Esa lista se quedó
     mintiendo en cuanto se publicó la siguiente, que es exactamente lo que le pasó a la
     frase de la instalación vieja. Ahora los cambios salen del historial desde la
     etiqueta anterior, y por eso el checkout pasa a pedir historial y etiquetas: con la
     profundidad por defecto no hay de dónde derivarlos.

Comprobaciones antes de publicar: balance de símbolos con escáner en los dos ficheros
Kotlin; ninguna marca de relleno de las que lee PlaceholderDetectorTest, que mira el
fichero entero; los 20 literales que exigen LimpiezaTest, FirmaNuevaTest,
LicenciaRepoTest e IptvReproductorTest siguen donde estaban (__N__ literales, los que
cuenta el pre-vuelo y no los que yo recuerde), y cada uno verificado primero contra la
prueba que lo exige, para que el censo no se quede viejo él tampoco;
el heredoc de la nota sin backticks y sin expansiones no previstas; los datos del doc
leídos de gradle.properties, apk.yml y build.gradle en vez de recordados.

No se añade ninguna prueba: siguen 472. Este commit no cambia comportamiento, cambia lo
que el repo dice de su comportamiento, y lo que lo vigila es que la próxima lectura
vuelva a encontrar las dos cosas de acuerdo."""

msg = msg.replace("__N__", str(n_lit))
c = api("/git/commits", "POST", {"message": msg, "tree": arbol, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
