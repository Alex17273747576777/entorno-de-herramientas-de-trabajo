#!/usr/bin/env python3
"""
Segunda pasada del buscador, con segmentos de ruta exactos.

La primera versión buscaba subcadenas y contaba "ai/" dentro de "reikai/", lo
que infló el conteo de Reikai a 1681 archivos de IA cuando en realidad tiene
cero. Aquí se compara por segmentos completos: /ai/ solo casa con un directorio
llamado exactamente "ai".

Esto no es un detalle de estilo: la primera medición habría hecho elegir una
arquitectura por un número falso.
"""
import json
import sys
import urllib.error
import urllib.request

# (etiqueta, segmentos exactos que deben aparecer en la ruta)
OBJETIVOS = {
    "feed": (["feed", "feeds"], []),
    "sugerencias": (["suggest", "suggestion", "suggestions", "recommend", "recommendations", "similar", "discover"], []),
    "IA": (["ai", "llm", "embeddings", "onnx", "inference"], [".onnx", "tensor"]),
    "sync": (["sync", "backup", "backups", "restore", "webdav"], []),
    "velocidad": (["cache", "caching", "prefetch", "performance", "benchmark"], []),
    "lector": (["reader", "viewer", "pager"], []),
    "extensiones": (["extension", "extensions", "source", "sources"], []),
}

REPOS = [
    "salmanbappi/AniZen",
    "Harrys-HQ/ShinKu",
    "Kototoro-app/Kototoro",
    "Noirero/Miyorare",
    "HuzaifaKhalid1311/DropSauce",
    "unseensnick/Reikai",
    "PineappleTwilight/houri",
    "ifritraen/kisara",
    "komikku-app/komikku",
]


def main() -> int:
    tok = open("/home/user/.gh-tokens").readline().strip()

    def api(url):
        req = urllib.request.Request(
            url,
            headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"},
        )
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            return {"_error": e.code}

    resumen = {}
    for repo in REPOS:
        d = api(f"https://api.github.com/repos/{repo}")
        if "_error" in d:
            print(f"{repo}: error {d['_error']}")
            continue
        arbol = api(f"https://api.github.com/repos/{repo}/git/trees/{d['default_branch']}?recursive=1")
        rutas = [e["path"] for e in arbol.get("tree", []) if e["type"] == "blob"]

        # separar en segmentos: "app/src/main/java/reikai/novel/X.kt" -> [app, src, ..., reikai, ...]
        segmentos = [(r, set(r.lower().split("/"))) for r in rutas]

        conteo = {}
        muestras = {}
        for etiqueta, (exactos, sufijos) in OBJETIVOS.items():
            hits = [
                r
                for r, segs in segmentos
                if any(e in segs for e in exactos) or any(r.lower().endswith(s) for s in sufijos)
            ]
            # fuera tests y fuera assets de imagen
            hits = [h for h in hits if "/test" not in h.lower() and not h.lower().endswith((".webp", ".png", ".jpg"))]
            conteo[etiqueta] = len(hits)
            muestras[etiqueta] = [h for h in hits if h.endswith(".kt")][:5]

        resumen[repo] = {"conteo": conteo, "muestras": muestras}
        print(f"\n=== {repo} ===")
        for k, v in conteo.items():
            print(f"  {k:<14}{v:>5}")
        for m in muestras["IA"]:
            print(f"      IA · {m}")

    json.dump(resumen, open("/opt/work/funciones-v2.json", "w"), indent=2, ensure_ascii=False)

    print(f"\n  {'repo':<32}" + "".join(f"{k:>13}" for k in OBJETIVOS))
    print("  " + "-" * (32 + 13 * len(OBJETIVOS)))
    for r, v in resumen.items():
        print(f"  {r:<32}" + "".join(f"{v['conteo'][k]:>13}" for k in OBJETIVOS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
