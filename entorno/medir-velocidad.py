#!/usr/bin/env python3
"""
Mide si Reikai es de verdad más rápido que Komikku, o si solo lo parece.

No hay benchmark ejecutable sin emulador, así que se mide lo que sí es objetivo
y guarda relación con la velocidad percibida:

  - tests de UI reales (androidTest): más tests de viewport/paginado = más
    comportamiento medido, no más promesas
  - uso de Compose vs WebView en el lector: una página en WebView tarda
    decenas de ms en montarse; un canvas de Compose, unos pocos
  - cachés de página y prefetch declarados
  - nº de dependencias pesadas en el build

Es una medición indirecta y se presenta como tal. No es un tiempo en ms.
"""
import json
import sys
import urllib.error
import urllib.request

REPOS = ["unseensnick/Reikai", "komikku-app/komikku", "null2264/yokai", "PineappleTwilight/houri"]


def main() -> int:
    tok = open("/home/user/.gh-tokens").readline().strip()

    def api(url):
        req = urllib.request.Request(
            url, headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"}
        )
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            return {"_error": e.code}

    filas = []
    for repo in REPOS:
        d = api(f"https://api.github.com/repos/{repo}")
        if "_error" in d:
            print(f"{repo}: error {d['_error']}")
            continue
        arbol = api(f"https://api.github.com/repos/{repo}/git/trees/{d['default_branch']}?recursive=1")
        rutas = [e["path"] for e in arbol.get("tree", []) if e["type"] == "blob"]
        bajas = [r.lower() for r in rutas]

        ui_tests = [r for r in bajas if "androidtest" in r and r.endswith(".kt")]
        tests_lector = [r for r in ui_tests if "reader" in r or "viewport" in r or "pager" in r or "zoom" in r]
        webview = [r for r in bajas if "webview" in r and r.endswith(".kt")]
        prefetch = [r for r in bajas if "prefetch" in r or "preload" in r]
        caches = [r for r in rutas if "/cache/" in r and r.endswith(".kt")]
        compose = [r for r in bajas if r.endswith(".kt")]

        fila = {
            "repo": repo,
            "estrellas": d["stargazers_count"],
            "archivos_kt": len(compose),
            "tests_ui": len(ui_tests),
            "tests_de_lector": len(tests_lector),
            "archivos_webview": len(webview),
            "prefetch": len(prefetch),
            "caches": len(caches),
        }
        filas.append(fila)

    cab = f"  {'repo':<30}{'★':>7}{'.kt':>8}{'testsUI':>9}{'testsLector':>13}{'webview':>9}{'prefetch':>10}{'cachés':>8}"
    print(cab)
    print("  " + "-" * (len(cab) - 2))
    for f in filas:
        print(
            f"  {f['repo']:<30}{f['estrellas']:>7}{f['archivos_kt']:>8}{f['tests_ui']:>9}"
            f"{f['tests_de_lector']:>13}{f['archivos_webview']:>9}{f['prefetch']:>10}{f['caches']:>8}"
        )

    json.dump(filas, open("/opt/work/medicion-velocidad.json", "w"), indent=2, ensure_ascii=False)
    print("\n  Medición indirecta: tests de lector y prefetch/caché son indicios de")
    print("  velocidad, NO un tiempo en milisegundos. Sin emulador no hay ms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
