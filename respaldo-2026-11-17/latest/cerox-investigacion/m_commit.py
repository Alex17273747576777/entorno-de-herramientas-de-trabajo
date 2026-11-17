#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit N · 1.0.3-beta-notas: cierra el pendiente de la nota de release.

Dos cambios y ninguno toca código de la app:

1. `android/app/build.gradle`: versionCode 7 → 8 y versionName
   `1.0.3-beta-notas`. De ese nombre sale la etiqueta de la release cuando el
   despacho no lleva una, así que el nombre dice lo que la release cierra.
2. `.github/workflows/apk.yml`: el selector de arquitectura del despacho ofrece
   `universal`. El guion ya lo conocía —compara el valor por nombre y, si es
   `universal`, no añade `-PsoloAbi`— pero la lista de opciones no lo ofrecía:
   se podía pedir un universal sólo a mano, nunca desde el formulario.

Por qué no se hace aquí el universal de verdad: el APK de 1.0.2 pesa 33,0 MB y
la mitad larga son bibliotecas nativas (53,7 %), de las que una sola —el
motor ONNX, 15,7 MB guardado sin comprimir— es la mitad. Un universal mete ese
motor por cada arquitectura. Antes de ofrecerlo hay que decidir qué pasa con
ese motor, y eso se pregunta, no se supone.

Uso: export GP=<token fino> && python3 -B m_commit.py [--run]
"""
import datetime, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import bloques_literales, mandato_de_paso, yaml_valido  # noqa: E402

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
RAW = "https://raw.githubusercontent.com/Alex17273747576777/cero-X-app"
GRADLE = "android/app/build.gradle"
APK = ".github/workflows/apk.yml"
# Cifra con la evidencia al lado (R14): run 43134156604, línea «475 pruebas · 0
# fallos · 0 errores · 6 saltadas». Este commit no toca pruebas, así que no
# sube: se afirma igual y no más.
PRUEBAS = 475
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO DE COMPROBACION: " + m)


def api(p, m="GET", b=None):
    d = json.dumps(b).encode() if b is not None else None
    r = urllib.request.Request(API + p, data=d, method=m, headers={
        "Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cxcommitN"})
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

g_antes = crudo(GRADLE, BASE)
y_antes = crudo(APK, BASE)

# ── R10 · cada anclaje se cuenta antes de sustituir ─────────────────────────
ANCLAJE_V = '        versionCode 7\n        versionName "1.0.2-beta-iptv-eq"'
ok(g_antes.count(ANCLAJE_V) == 1,
   "el anclaje de versión aparece %d veces" % g_antes.count(ANCLAJE_V))
vc_viejo = int(re.search(r"^\s*versionCode (\d+)$", g_antes, re.M).group(1))
ok(vc_viejo == 7, "el versionCode publicado es %d, se esperaba 7" % vc_viejo)
VC_NUEVO = vc_viejo + 1          # derivado, no escrito a mano (R8)
VN_NUEVO = "1.0.3-beta-notas"

ANCLAJE_O = 'options: ["arm64-v8a", "armeabi-v7a", "x86_64", "x86"]'
ok(y_antes.count(ANCLAJE_O) == 1,
   "el anclaje de opciones aparece %d veces" % y_antes.count(ANCLAJE_O))
ok('"universal"' not in y_antes.split("abi:")[1].split("publicar:")[0],
   "el selector ya ofrecía universal: este commit no tendría objeto")

g_desp = g_antes.replace(
    ANCLAJE_V,
    '        versionCode %d\n        versionName "%s"' % (VC_NUEVO, VN_NUEVO))
y_desp = y_antes.replace(
    ANCLAJE_O,
    'options: ["universal", "arm64-v8a", "armeabi-v7a", "x86_64", "x86"]')
ok(g_desp != g_antes and y_desp != y_antes, "alguna sustitución no ocurrió")

# ── R20 · el flujo sigue siendo YAML válido después del cambio ──────────────
probs = yaml_valido(y_desp) + bloques_literales(y_desp)
ok(not probs, "el flujo nuevo no se lee: %s" % probs[:1])
doc = __import__("yaml").safe_load(y_desp)
entr = (doc[True] if True in doc else doc.get("on"))["workflow_dispatch"]["inputs"]["abi"]
ok("universal" in entr["options"], "el universal no quedó en las opciones")
ok(entr["default"] == "arm64-v8a", "el universal se coló como opción por omisión")
print("  R20  YAML del flujo tras el cambio           válido · universal en opciones · "
      "por omisión sigue arm64-v8a")

# ── R21 · la opción nueva tiene que tener detrás el guion que la entiende ───
guion, probs2 = mandato_de_paso(y_desp, "Construir el APK de release, sin modelos")
ok(guion is not None, "no encontré el paso de construir: %s" % probs2)
ok(not probs2, probs2[:1] if probs2 else "")
ok('$ABI" != "universal"' in guion or '!= "universal"' in guion,
   "el selector ofrece universal pero el paso de construir no lo conoce por nombre")
ok("-PsoloAbi=$ABI" in guion, "el paso ya no añade -PsoloAbi para las arquitecturas sueltas")
print("  R21  el paso de construir conoce la opción    compara $ABI con universal por nombre")

# ── lo que el commit NO toca: ni una prueba ─────────────────────────────────
ok("@Test" not in g_desp and "@Test" not in y_desp, "apareció una prueba donde no debía")
print("  R8   versión y pruebas                        versionCode %d · pruebas %d, sin cambio"
      % (VC_NUEVO, PRUEBAS))

CAMBIOS = [(GRADLE, g_desp), (APK, y_desp)]
print("\n  ficheros: %d" % len(CAMBIOS))
for ruta, texto in CAMBIOS:
    antes = g_antes if ruta == GRADLE else y_antes
    print("     %-40s %+5d bytes" % (ruta, len(texto) - len(antes)))

if not EJECUTAR:
    print("\nDRY-RUN: nada publicado")
    raise SystemExit(0)

ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
arbol = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": r, "mode": "100644", "type": "blob", "content": t} for r, t in CAMBIOS]})["sha"]

msg = """1.0.3-beta-notas: cierra el pendiente de la nota de release

Dos cambios, y ninguno toca código de la app.

LA VERSION. versionCode 7 → 8. El versionName deriva la etiqueta de la release
cuando el despacho no lleva una (entrada `etiqueta` vacía), así que el nombre
dice lo que esta release cierra: el pendiente del ciclo de 1.0.2, o sea el
flujo que se publicó roto, su arreglo y su prueba.

EL UNIVERSAL. El flujo `apk` ya sabía construir sin `-PsoloAbi` —es decir,
universal—: el paso de construir compara la arquitectura por nombre y sólo
añade `-PsoloAbi` cuando no es `universal`. Lo que faltaba era ofrecerlo en el
selector del despacho, que listaba las cuatro arquitecturas y no listaba
`universal`. Desde este commit está en la lista.

Lo que NO se hace aquí es publicar un universal: el APK de 1.0.2 pesa 33,0 MB
de los que el 53,7 % son bibliotecas nativas, y la mitad de eso es un solo
fichero —el motor ONNX, 15,7 MB guardado sin comprimir para que el sistema lo
mapee directo— con cero modelos dentro. Un universal mete ese motor una vez
por arquitectura. Antes de ofrecerlo como release hay que decidir qué pasa con
ese motor, y esa decisión se pregunta, no se supone.

Sin cambio funcional: es el código de 6cb3f85a, donde las __PRUEBAS__ pruebas salieron
en verde (run 43134156604) y cuya versión anterior, la 1.0.2, es la que un V60
ThinQ 5G arrancó y navegó sin cuelgues. Esta release existe para que el paso
de la nota de cambios —arreglado en el commit anterior pero que sólo corre con
publicar=true— se ejecute por primera vez en el corredor, que es donde aún no
se había probado nunca."""
msg = msg.replace("__PRUEBAS__", str(PRUEBAS))
ok("__PRUEBAS__" not in msg and str(PRUEBAS) in msg,
   "el marcador de pruebas no se sustituyó en el mensaje")

c = api("/git/commits", "POST", {"message": msg, "tree": arbol, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("\nCOMMIT:", c["sha"])
time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
