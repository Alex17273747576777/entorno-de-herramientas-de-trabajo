#!/usr/bin/env python3
"""
Mide los repositorios candidatos con la API de GitHub.

Mide estrellas, licencia, número de archivos, último push y releases. No
interpreta ni recomienda: solo saca los números para decidir con datos en vez
de con la memoria de nadie.
"""
import json
import sys
import urllib.error
import urllib.request

REPOS = [
    "komikku-app/komikku",
    "PineappleTwilight/houri",
    "unseensnick/Reikai",
    "null2264/yokai",
    "salmanbappi/AniZen",
    "Harrys-HQ/ShinKu",
    "HuzaifaKhalid1311/DropSauce",
    "Noirero/Miyorare",
    "Kototoro-app/Kototoro",
    "ivucicev/DropSync",
    "Arthurpendragon9876/DeepSync",
    "ifritraen/kisara",
    "Kotatsu-Redo/Kotatsu-Redo",
    "rokku-app/rokku",
    "Wammy-app/Wammy",
    "AppFuton/Futon",
    "mihonapp/mihon",
]


def main() -> int:
    tok = open("/home/user/.gh-tokens").readline().strip()

    def api(url):
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {tok}",
                "Accept": "application/vnd.github+json",
            },
        )
        try:
            return json.load(urllib.request.urlopen(req, timeout=40))
        except urllib.error.HTTPError as e:
            return {"_error": e.code}

    print(f"  {'repo':<34}{'estrellas':>10} {'licencia':<14}{'archivos':>9} {'push':<12}{'rel':>5}")
    print("  " + "-" * 86)
    filas = []
    for r in REPOS:
        d = api(f"https://api.github.com/repos/{r}")
        if "_error" in d:
            print(f"  {r:<34}{'—':>10}  error {d['_error']}")
            continue
        arbol = api(f"https://api.github.com/repos/{r}/git/trees/{d['default_branch']}?recursive=1")
        n = len(arbol.get("tree", []))
        rel = api(f"https://api.github.com/repos/{r}/releases?per_page=1")
        nrel = len(rel) if isinstance(rel, list) else 0
        lic = (d.get("license") or {}).get("spdx_id") or "—"
        fila = {
            "repo": r,
            "estrellas": d["stargazers_count"],
            "licencia": lic,
            "archivos": n,
            "push": d["pushed_at"][:10],
            "releases": nrel,
            "lenguaje": d.get("language"),
        }
        filas.append(fila)
        print(f"  {r:<34}{fila['estrellas']:>10} {lic:<14}{n:>9} {fila['push']:<12}{nrel:>5}")

    json.dump(filas, open("/opt/work/medicion-candidatos.json", "w"), indent=2, ensure_ascii=False)
    print(f"\n  guardado en /opt/work/medicion-candidatos.json ({len(filas)} repos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
