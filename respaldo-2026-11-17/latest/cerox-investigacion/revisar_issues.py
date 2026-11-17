#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorre las issues creadas por la cuenta y dice cuáles merecen un comentario.

Antes sólo marcaba «sin responder». Eso fue lo que produjo la tanda del 2026-11-11:
48 comentarios publicados porque 48 hilos estaban «sin responder», y 31 de esos hilos
estaban cerrados con el mantenedor ya contestado. Responder ahí no aportaba nada a
nadie y le costaba una notificación a quien lo recibía.

Ahora aplica las dos reglas que salieron de aquello (R17 y R18 de `reglas/`):

  · R17 — para cada hilo decide si un comentario aportaría algo. Un hilo cerrado, ya
    respondido por el mantenedor y sin nada nuestro pendiente no merece cortesía.
  · R18 — antes de informar del total, informa de la **composición**. Si la categoría
    muerta pasa de la mitad, el guion lo dice y manda parar a preguntar.

El campo `pendiente` se decide con dos hechos del hilo: que la petición sea nuestra y
siga abierta, o que el último comentario ajeno se dirigiera a la cuenta. El segundo es
una heurística —un regex no sabe si alguien te está hablando a ti—, así que el listado
la marca y hay que confirmarla leyendo antes de publicar nada.

El detalle se vuelca en /tmp y no en el espacio de trabajo: es re-descargable con
volver a ejecutar este guion, y guardar aquí lo que se puede volver a obtener fue el
motivo de que el workspace llegara a 475 MB (R15).
"""
import io, json, os, re, sys, time, urllib.request, urllib.error

sys.path.insert(0, "/home/user/cerox-investigacion/reglas")
from motor import censar_acciones, merece_respuesta  # noqa: E402

TOK = os.environ["GP"]
YO = "Alex17273747576777"
H = {"Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json",
     "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "cx-revisa"}

MANTENEDOR = ("COLLABORATOR", "MEMBER", "OWNER")
# Señales de que el comentario ajeno se dirigía a la cuenta: la nombra, le pregunta o
# le reprocha algo. Es una aproximación y el listado lo advierte.
DIRIGIDO = re.compile(
    r"Alex17273747576777|\bslop\b|\bspam\b|\bAI[- ]generated\b|why don't you|"
    r"you should|are you|can you|could you|\byou\b[^.]{0,60}\?", re.I)


def get(url):
    for intento in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=90) as x:
                return json.loads(x.read() or b"null")
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and intento < 3:
                espera = e.headers.get("Retry-After")
                time.sleep(int(espera) if espera else 20 * (intento + 1))
                continue
            return {"__error__": "HTTP %s: %s" % (e.code, e.read().decode()[:150])}
        except Exception as e:
            if intento < 3:
                time.sleep(5); continue
            return {"__error__": str(e)}


items = []
for pagina in (1, 2):
    d = get("https://api.github.com/search/issues?q=author:%s+type:issue&per_page=100"
            "&sort=created&order=desc&page=%d" % (YO, pagina))
    if "__error__" in d:
        print("error de busqueda:", d["__error__"]); break
    items += d.get("items", [])
    print("pagina %d: %d issues (total declarado %s)"
          % (pagina, len(d.get("items", [])), d.get("total_count")))
    time.sleep(3)

print("\nrecorriendo las que tienen comentarios…")
pendientes = []
for it in items:
    if it.get("comments", 0) == 0:
        continue
    repo = it["repository_url"].split("/repos/")[-1]
    coms = get(it["comments_url"] + "?per_page=100")
    if isinstance(coms, dict):
        print("  %s#%s -> %s" % (repo, it["number"], coms.get("__error__"))); continue
    ajenos = [c for c in coms if c["user"]["login"].lower() != YO.lower()]
    if not ajenos:
        continue
    ultimo_ajeno = max(c["created_at"] for c in ajenos)
    mios_despues = [c for c in coms if c["user"]["login"].lower() == YO.lower()
                    and c["created_at"] > ultimo_ajeno]
    ajenos_antes = sorted([c for c in ajenos if c["created_at"] <= ultimo_ajeno],
                          key=lambda c: c["created_at"])
    hilo = {
        "state": it["state"],
        "locked": it.get("locked", False),
        "respondio_mantenedor": any(c.get("author_association") in MANTENEDOR for c in ajenos),
        # Dos hechos, no intuición: petición nuestra todavía abierta, o el último
        # comentario ajeno dirigido a la cuenta.
        "pendiente": (it["state"] == "open" and (it.get("user") or {}).get("login") == YO)
                     or bool(DIRIGIDO.search((ajenos_antes[-1].get("body") or ""))),
    }
    veredicto, motivo = merece_respuesta(hilo, "")
    pendientes.append({
        "repo": repo, "numero": it["number"], "estado": it["state"],
        "bloqueada": hilo["locked"], "cerrada": (it.get("closed_at") or "")[:10],
        "titulo": it["title"], "url": it["html_url"],
        "sin_responder": len(mios_despues) == 0,
        "hilo": hilo, "veredicto": veredicto, "motivo": motivo,
        "comentarios_ajenos": [{"autor": c["user"]["login"], "fecha": c["created_at"],
                                "asociacion": c.get("author_association"),
                                "cuerpo": c["body"]} for c in ajenos],
    })
    print("  %-36s #%-6s %-6s %-8s %s" % (
        repo[:36], it["number"], it["state"],
        ("SIN RESP." if not mios_despues else "respond."),
        ("MERECERÍA" if veredicto == "responder" else "callar")))

# ═══ R18: la composición antes que el total ═══
sin_responder = [p for p in pendientes if p["sin_responder"]]
merecen = [p for p in sin_responder if p["veredicto"] == "responder"]
ruido = [p for p in sin_responder if p["veredicto"] == "callar"]

print("\n%s" % ("═" * 74))
print("CENSO (R18: de qué está hecho el «todas», antes de ejecutarlo)")
print("═" * 74)
lineas, alarma = censar_acciones(
    pendientes,
    lambda p: ("viva" if p["veredicto"] == "responder" else "muerta") if p["sin_responder"]
              else "ya_respondida",
    categoria_muerta="muerta")
for l in lineas:
    print("   ", l)
print("\n    issues con comentarios ajenos : %d" % len(pendientes))
print("    sin responder                 : %d" % len(sin_responder))
print("    de ésas, merecen comentario   : %d" % len(merecen))
print("    de ésas, serían ruido         : %d" % len(ruido))
print("    alarma de composición         : %s" % alarma)
if alarma:
    print("\n    → MÁS DE LA MITAD serían ruido. R18 manda parar aquí y preguntar")
    print("      antes de publicar nada, no ejecutar el mandato y dar el total.")

if ruido:
    print("\n%s" % ("─" * 74))
    print("HILOS QUE LA REGLA MANDA DEJAR EN PAZ (R17)")
    print("─" * 74)
    for p in sorted(ruido, key=lambda x: x["cerrada"] or ""):
        print("  %-34s #%-6s cerrada %-10s %s" % (p["repo"][:34], p["numero"],
                                                   p["cerrada"] or "—", p["motivo"][:60]))
    print("\n  En estos hilos un comentario sólo añadiría una notificación. Si se")
    print("  quiere publicar algo ahí, tiene que aportar un dato de verdad: un")
    print("  enlace, una versión, un fichero, un fallo concreto o una corrección de")
    print("  algo nuestro que siga en pie.")

SALIDA = "/tmp/issues_pendientes.json"
with io.open(SALIDA, "w", encoding="utf-8") as f:
    json.dump(pendientes, f, ensure_ascii=False, indent=1)
print("\ndetalle en %s (re-descargable, por eso no se guarda en el workspace)" % SALIDA)
