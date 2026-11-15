#!/usr/bin/env python3
# vara_idiomas.py — compuertas de las banditas por idioma (es-dominicano / en-ingles).
# G20 banda del maestro · G21 derivados completos · G22 formato por canal · G23 misión.
# Uso: python3 tools/vara_idiomas.py [ruta-a-01-PUBLICACIONES]
# Sale 1 si hay algún rojo. No toca ficheros: sólo mide.
import re, sys, pathlib

RAIZ = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(
    "Arena-Reimagined/01-PUBLICACIONES")
CANALES = {"es-dominicano": ("Facebook", "WhatsApp", "Instagram", "Telegram"),
           "en-ingles": ("Reddit", "X", "Discord", "Telegram")}
SPDX = re.compile(r"\b(MIT|Apache-2\.0|GPL-[23]\.0|AGPL-3\.0|MPL-2\.0|BSD-[23]-Clause|NOASSERTION)\b")

def g20(texto):
    n = len(texto)
    return (6000 <= n <= 45000, f"cuerpo {n} car.")

def g21(carpeta, base, plats):
    faltan = []
    for p in plats:
        hits = list(carpeta.glob(f"{base}-{p}-*.md"))
        if not hits or hits[0].stat().st_size == 0:
            faltan.append(p)
    return (not faltan, f"derivados {len(plats)-len(faltan)}/{len(plats)}" + (f" faltan {faltan}" if faltan else ""))

def g22(carpeta, base, canal):
    probs = []
    for p in CANALES[canal]:
        hit = list(carpeta.glob(f"{base}-{p}-*.md"))
        if not hit:
            continue
        t = hit[0].read_text(encoding="utf-8")
        if canal == "es-dominicano" and p == "Facebook":
            if re.search(r"^\.?\|.*\|$", t, re.M):
                probs.append("Facebook con tabla")
            if "```" in t:
                probs.append("Facebook con vallas")
        if canal == "es-dominicano" and p == "Instagram":
            cap = t.split("#LaBandita")[0]
            if len(cap) > 2200:
                probs.append(f"Instagram epígrafe {len(cap)}>2200")
        if canal == "en-ingles" and p == "X":
            largos = [l for l in t.splitlines() if re.match(r"\d+/\d+", l) and len(l) > 280]
            if largos:
                probs.append(f"X con {len(largos)} tweets >280")
        if canal == "en-ingles" and p == "Discord":
            chunks = re.split(r"― mensaje \d+/\d+ ―", t)[1:]
            if chunks and max(len(c) for c in chunks) > 2000:
                probs.append("Discord con mensaje >2000")
    return (not probs, "formatos limpios" if not probs else "; ".join(probs))

def g23(texto):
    stars = texto.count("★") + texto.lower().count("estrellas") + texto.lower().count("stars")
    urls = texto.count("github.com")
    repos = len(re.findall(r"\brepositorios?\b|\brepos?\b|\brepositories\b", texto, re.I))
    lic = len(SPDX.findall(texto))
    ok = stars >= 3 or urls >= 1 or repos >= 3 or lic >= 2
    return (ok, f"★/{stars} urls/{urls} repos/{repos} lic/{lic}")

def main():
    rojos = 0
    for canal, plats in CANALES.items():
        carpeta = RAIZ / canal
        if not carpeta.is_dir():
            print(f"{canal}: SIN CARPETA"); rojos += 1; continue
        for m in sorted(carpeta.glob("*MAESTRO-*.md")) + sorted(carpeta.glob("*MASTER-*.md")):
            texto = m.read_text(encoding="utf-8")
            base = m.name.split("-MAESTRO-")[0].split("-MASTER-")[0]
            # base termina en -es-dominicano o -en-ingles: los derivados se buscan con ese tag
            filas = [("G20", g20(texto)), ("G21", g21(carpeta, base, plats)),
                     ("G22", g22(carpeta, base, canal)), ("G23", g23(texto))]
            for g, (ok, det) in filas:
                if not ok:
                    rojos += 1
                print(f"  {canal} {m.name[:2]}… {g} {'OK  ' if ok else 'ROJO'} · {det}")
    print(f"vara_idiomas: {'NINGUN ROJO' if rojos == 0 else str(rojos) + ' ROJOS'}")
    sys.exit(1 if rojos else 0)

if __name__ == "__main__":
    main()
