#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit J: versión 1.0.2-beta y una release cuyo título no miente.

Dos cosas, y las dos existen por lo mismo: el flujo `apk` tenía el título de la
release escrito a mano («cero-X 1.0.1-beta - arranque honesto»), así que publicar
otra versión con otra etiqueta habría sacado una release etiquetada v1.0.2 y
titulada 1.0.1. Y sobrescribir la etiqueta vieja con un APK distinto habría roto la
trazabilidad de una huella que ya está publicada.
"""
import base64, datetime, json, os, re, sys, time, urllib.request, urllib.error

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
P_GRADLE = "android/app/build.gradle"
P_APK = ".github/workflows/apk.yml"
BASE_ESPERADO = "f11a1b7a418dfceed4f865c426285e4c52647522"
VERSION = "1.0.2-beta-iptv-eq"
EJECUTAR = "--run" in sys.argv


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
print("MODO: %s · base %s" % ("PUBLICACION" if EJECUTAR else "DRY-RUN", BASE[:8]))


def leer(p):
    return base64.b64decode(api("/contents/%s?ref=%s" % (p, BASE))["content"]).decode()


gradle = leer(P_GRADLE)
apk = leer(P_APK)
cambios = {}

# ── 1 · la versión ─────────────────────────────────────────────────────────

viejo_code = re.search(r"^        versionCode (\d+)$", gradle, re.M)
viejo_name = re.search(r'^        versionName "([^"]+)"$', gradle, re.M)
ok(viejo_code and viejo_name, "no encuentro versionCode/versionName")
anterior_code = int(viejo_code.group(1))
anterior_name = viejo_name.group(1)
print("  version actual            %d · %s" % (anterior_code, anterior_name))

gradle2 = gradle.replace("        versionCode %d\n" % anterior_code,
                         "        versionCode %d\n" % (anterior_code + 1), 1)
gradle2 = gradle2.replace('        versionName "%s"\n' % anterior_name,
                          '        versionName "%s"\n' % VERSION, 1)
ok(gradle2 != gradle, "no se ha cambiado nada en build.gradle")
cambios[P_GRADLE] = gradle2

# ── 2 · el título de la release, derivado de la etiqueta ──────────────────

viejo_titulo = '''            gh release create "$ETIQUETA" "$APK" sha256sums.txt \\
              --target main --title "cero-X 1.0.1-beta - arranque honesto ($ABI, sin modelos)" \\
              --notes-file notas.md'''
nuevo_titulo = '''            # El título sale de la etiqueta y no está escrito a mano: con la
            # versión anterior aquí ponía «1.0.1-beta» y cualquier etiqueta nueva
            # habría publicado una release que se contradice con su propio nombre.
            gh release create "$ETIQUETA" "$APK" sha256sums.txt \\
              --target main --title "cero-X ${ETIQUETA#v} ($ABI, sin modelos)" \\
              --notes-file notas.md'''
ok(apk.count(viejo_titulo) == 1, "anclaje del titulo: %d" % apk.count(viejo_titulo))
apk2 = apk.replace(viejo_titulo, nuevo_titulo)

viejo_tam = '''          · Tamaño: $TAM bytes ($MIB MiB). La build anterior pesaba 475.523.392
            bytes porque llevaba 378 MiB de modelos y cuatro arquitecturas.'''
nuevo_tam = '''          · Tamaño: $TAM bytes ($MIB MiB). La 1.0.1 pesó 31.577.211 bytes, y la
            primera build pesó 475.523.392 porque llevaba 378 MiB de modelos ONNX
            y cuatro arquitecturas dentro.'''
ok(apk2.count(viejo_tam) == 1, "anclaje del tamano: %d" % apk2.count(viejo_tam))
apk2 = apk2.replace(viejo_tam, nuevo_tam)

viejo_no = '''          Lo que esta build NO demuestra: que la app funcione en un teléfono. El
          flujo compila, firma y comprueba bytes; no hay emulador aquí. El arreglo
          del arranque (1.0.1) está razonado sobre el código y cubierto por
          pruebas de JVM, y queda por confirmarse instalándolo en el V60.'''
nuevo_no = '''          Qué trae esta build respecto a la 1.0.1: el ecualizador (módulo 37, con
          sus diez curvas ISO y los pasos de volumen del sistema) y el IPTV neutro
          (módulo 38: las fuentes las instala el usuario, listas M3U, guía XMLTV y
          reproductor media3), con su pantalla y su destino en la barra inferior.
          No trae ninguna lista de canales ni ninguna fuente dentro del APK.

          Lo que esta build NO demuestra: que la app funcione en un teléfono. El
          flujo compila, firma y comprueba bytes; no hay emulador aquí. Ni el
          ecualizador ni la reproducción se han probado en un dispositivo: las
          pruebas que los cubren son de JVM, y una prueba de JVM no abre un DSP ni
          un decodificador de vídeo. Queda por confirmarse instalándolo en el V60.'''
ok(apk2.count(viejo_no) == 1, "anclaje del no-demuestra: %d" % apk2.count(viejo_no))
apk2 = apk2.replace(viejo_no, nuevo_no)
cambios[P_APK] = apk2

# ── COMPROBACIONES ─────────────────────────────────────────────────────────

ok("versionCode %d" % (anterior_code + 1) in cambios[P_GRADLE], "no quedo el versionCode nuevo")
ok('versionName "%s"' % VERSION in cambios[P_GRADLE], "no quedo el versionName nuevo")
ok("1.0.1-beta-arranque-honesto" not in cambios[P_GRADLE], "queda la version vieja")
# Lo que IptvReproductorTest exige de build.gradle tiene que seguir ahí.
for lit in ["androidx.media3:media3-exoplayer:1.11.1", "androidx.media3:media3-exoplayer-hls:1.11.1"]:
    ok(lit in cambios[P_GRADLE], "se ha perdido " + lit)
ok("media3-exoplayer:+" not in cambios[P_GRADLE] and "latest.release" not in cambios[P_GRADLE],
   "version dinamica en media3")

ok("cero-X 1.0.1-beta" not in cambios[P_APK], "el titulo viejo sigue escrito a mano")
ok('--title "cero-X ${ETIQUETA#v} ($ABI, sin modelos)"' in cambios[P_APK], "no quedo el titulo derivado")
# El heredoc se expande: un $ o un backtick nuevo ejecutaría algo en el runner.
heredoc = cambios[P_APK].split("cat > notas.md <<NOTAS")[1].split("\n          NOTAS")[0]
sospechosos = [l.strip() for l in heredoc.split("\n")
               if "`" in l or re.search(r"\$\((?!(TAM|MIB|ABI))", l)]
ok(not sospechosos, "el heredoc ejecutaría algo: %s" % sospechosos[:2])
ok("31.577.211" in heredoc and "475.523.392" in heredoc, "los tamaños no están los dos")
ok("módulo 37" in heredoc and "módulo 38" in heredoc, "no se dice qué trae la build")
ok("NO demuestra" in heredoc, "se ha perdido lo que la build no demuestra")
try:
    import yaml
    yaml.safe_load(cambios[P_APK])
    print("  YAML                      apk.yml parsea")
except ImportError:
    print("  YAML                      sin PyYAML, no se comprueba el parseo")

# Los anclajes de los pasos anteriores siguen intactos: el flujo tiene que poder
# construir y firmar igual que antes.
for lit in ["-PsoloAbi=$ABI", "-Xmx6g", ":app:assembleRelease", "apksigner",
            "HUELLA-CERTIFICADO.txt", "gh release upload \"$ETIQUETA\" \"$APK\" sha256sums.txt --clobber"]:
    ok(lit in cambios[P_APK], "se ha perdido un paso del flujo: " + lit)

print("  versionCode               %d -> %d" % (anterior_code, anterior_code + 1))
print("  versionName               %s -> %s" % (anterior_name, VERSION))
for p in sorted(cambios):
    print("  %7d B · %s" % (len(cambios[p].encode()), p))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": p, "mode": "100644", "type": "blob", "content": cambios[p]}
    for p in sorted(cambios)]})["sha"]
msg = """1.0.2-beta: versión nueva y una release cuyo título sale de su etiqueta

Dos cambios pequeños que existen para poder publicar el APK con el ecualizador y el
IPTV dentro sin decir una mentira por el camino.

  · `versionCode` 6 → 7 y `versionName` 1.0.2-beta-iptv-eq. Subir el código es lo
    que permite actualizar una instalación de la 1.0.1 en vez de tener que
    desinstalarla: el certificado ya es el mismo desde el arreglo de la firma.
  · El flujo `apk` tenía el título de la release escrito a mano, con «1.0.1-beta»
    dentro. Publicar con otra etiqueta habría creado una release llamada v1.0.2 y
    titulada 1.0.1, que es exactamente la clase de cosa que este repo se pasó una
    limpieza entera quitando. Ahora el título sale de la etiqueta.

Y las notas de la release dejan de hablar sólo del arranque: dicen qué trae esta
build respecto a la anterior (el ecualizador y el IPTV neutro, y que no trae ninguna
lista de canales dentro), corrigen el tamaño de referencia —la build anterior ya no
es la de 475 MB, es la 1.0.1 de 31.577.211 bytes— y mantienen la frase que importa:
esto NO demuestra que la app funcione en un teléfono. Ni el DSP del ecualizador ni
el decodificador de vídeo se han abierto nunca aquí; las pruebas que los cubren son
de JVM. Eso sólo lo confirma el V60.

No se sobrescribe la etiqueta v1.0.1-beta-arranque-honesto: su APK y su SHA-256 ya
están publicados y citados, y cambiar los bytes debajo de un nombre que alguien
pudo anotar es perder la trazabilidad. La build nueva sale con su propia etiqueta."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
