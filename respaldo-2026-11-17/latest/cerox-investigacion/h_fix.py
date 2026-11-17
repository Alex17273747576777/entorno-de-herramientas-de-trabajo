#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Commit H2: createMediaItem no existe en media3; el metodo es createMediaSource.

Un error de compilacion, y solo uno: el resto de las llamadas a media3 resolvieron,
que es lo que dice el log (ni un segundo `e: file://`).
"""
import base64, datetime, json, os, sys, time, urllib.request, urllib.error

TOK = os.environ.get("GP")
API = "https://api.github.com/repos/Alex17273747576777/cero-X-app"
P = "android/app/src/main/java/com/ceroX/app/modules/iptv/ReproductorIptv.kt"
PRUEBA = "android/app/src/test/java/com/ceroX/app/modules/iptv/IptvReproductorTest.kt"
BASE_ESPERADO = "917c3f06196499a5f29281af5180dd87fb1778fc"
EJECUTAR = "--run" in sys.argv


def ok(c, m):
    if not c:
        raise SystemExit("FALLO: " + m)


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


def leer(p):
    return base64.b64decode(api("/contents/%s?ref=%s" % (p, BASE))["content"]).decode()


BASE = api("/git/ref/heads/main")["object"]["sha"]
ok(BASE == BASE_ESPERADO, "main se movio: " + BASE)
t = leer(P)

viejo = """            val elemento = MediaItem.fromUri(solicitud.url)
            p.setMediaSource(DefaultMediaSourceFactory(fabrica).createMediaItem(elemento))"""
nuevo = """            val elemento = MediaItem.fromUri(solicitud.url)
            // La fábrica se llama por lo que devuelve: una fuente, no un elemento.
            // Este comentario describe el método en vez de escribir su nombre, porque
            // la comprobación de abajo busca el nombre equivocado en todo el fichero.
            p.setMediaSource(DefaultMediaSourceFactory(fabrica).createMediaSource(elemento))"""
ok(t.count(viejo) == 1, "anclaje: %d" % t.count(viejo))
t = t.replace(viejo, nuevo)
ok("createMediaItem" not in t, "quedaba alguna llamada al metodo que no existe")
ok("createMediaSource(elemento)" in t, "no quedo la llamada buena")

# Los literales que la prueba publicada exige de este fichero siguen ahí.
for lit in ["@OptIn(UnstableApi::class)", "ExoPlayer.Builder", "onPlayerError", "errorCodeName",
            "release()", "setDefaultRequestProperties", "setUserAgent",
            "fun ultimoMotivo(): String?"]:
    ok(lit in t, "la prueba exige %r y ya no esta" % lit)
ok("!!" not in t and '?: ""' not in t, "prohibidos")
for m in ["Placeholder", "placeholder", "Simular", "simulado", "TODO:", "FIXME", "dummy",
          "hardcodeado", "sin implementar"]:
    ok(m not in t, "marca " + m)
ok(t.count("{") == t.count("}") + t.count("${"), "llaves raras")
print("ReproductorIptv.kt: %d B -> %d B · literales de la prueba intactos" % (len(leer(P).encode()), len(t.encode())))

if not EJECUTAR:
    print("DRY-RUN"); raise SystemExit(0)

arb = api("/git/trees", "POST", {"base_tree": BASE, "tree": [
    {"path": P, "mode": "100644", "type": "blob", "content": t}]})["sha"]
ahora = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
iden = {"name": "La Bandita", "email": "reborn@labandita.dev", "date": ahora}
msg = """IPTV: createMediaSource, que createMediaItem no existe

Un error de compilacion en el commit anterior, y solo uno:

  e: ReproductorIptv.kt:93:65 Unresolved reference 'createMediaItem'.

Me invente el nombre del metodo. `DefaultMediaSourceFactory` implementa
`MediaSourceFactory`, cuya unica funcion de creacion es `createMediaSource(MediaItem)`
y devuelve un `MediaSource`, que es lo que `Player.setMediaSource` acepta. No hay
ningun `createMediaItem` en media3.

Que el log traiga un solo error dice algo util: el resto de las llamadas a media3 —el
opt-in de UnstableApi, la fabrica de datos con sus cabeceras, el oyente de errores con
su codigo, la superficie de video, la liberacion— resolvieron todas contra la 1.11.1.

Esta clase de fallo no la caza ninguna prueba: crear un MediaSource necesita el
framework, y las pruebas del reproductor comprueban el cableado, no la ejecucion. Lo
que si se puede hacer, y se hizo aqui, es comprobar antes de publicar que los literales
que la prueba exige del fichero siguen en su sitio despues del arreglo."""
c = api("/git/commits", "POST", {"message": msg, "tree": arb, "parents": [BASE],
                                 "author": iden, "committer": iden})
api("/git/refs/heads/main", "PATCH", {"sha": c["sha"], "force": False})
print("COMMIT:", c["sha"]); time.sleep(5)
print("main:", api("/git/ref/heads/main")["object"]["sha"])
