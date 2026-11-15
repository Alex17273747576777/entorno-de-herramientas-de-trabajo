#!/usr/bin/env python3
# derivar_plataformas.py — deriva los recortes por plataforma desde el texto maestro.
# Uso:  python3 tools/derivar_plataformas.py <maestro.md> [--solo PLAT]
# Regla de la casa (CORAZON l.810): si un canal rompe formato se ajusta ESTE generador,
# nunca el texto publicado. Defecto G18 que corrige: vallas y tablas que Facebook no
# renderiza (45/45 piezas viejas las llevaban).
import re, sys, datetime, pathlib

FECHA = datetime.date.today().isoformat()
FIRMA = "*💓 La Bandita informa. Lo que no se midió, aquí no se escribe.*"

ES = {"Facebook", "WhatsApp", "Instagram", "Telegram"}
EN = {"Reddit", "X", "Discord", "Telegram"}

def tablas_a_listas(txt):
    out = []
    for ln in txt.splitlines():
        s = ln.strip()
        if s.startswith("|") and s.endswith("|"):
            celdas = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in celdas if c):
                continue
            out.append("• " + " · ".join(c for c in celdas if c))
        else:
            out.append(ln)
    return "\n".join(out)

def sin_vallas(txt):
    return txt.replace("```", "")

def sin_bold(txt):
    return txt.replace("**", "").replace("__", "")

def recorta(texto, n):
    if len(texto) <= n:
        return texto
    corte = texto[:n].rsplit(" ", 1)[0]
    return corte.rstrip() + " …"

def seccion(txt, marcador, hasta=None):
    lineas = txt.splitlines()
    ini = next((i for i, l in enumerate(lineas) if marcador in l), None)
    if ini is None:
        return ""
    fin = len(lineas)
    for j in range(ini + 1, len(lineas)):
        if lineas[j].startswith("## ") or (hasta and hasta in lineas[j]):
            fin = j
            break
    return "\n".join(lineas[ini:fin]).strip()

def derivar_es(txt):
    titulo = next((l for l in txt.splitlines() if l.startswith("# ")), "").lstrip("# ").strip()
    d = {}
    d["Facebook"] = sin_bold(sin_vallas(tablas_a_listas(txt)))
    d["WhatsApp"] = txt
    cap = f"{titulo}\n\n" + seccion(txt, "⚡")
    cap = sin_bold(tablas_a_listas(cap))
    cap = recorta(cap, 2000)
    d["Instagram"] = (cap + "\n\n#LaBandita #CodigoAbierto #esdominicano #OpenSource\n\n"
        "IMAGEN SUGERIDA (no va en el epígrafe): tarjeta 1080x1350 con el título, la cifra de\n"
        "estrellas totales y el conteo con-huella/sin-huella sobre fondo oscuro; epígrafe arriba."
        "\n\n" + FIRMA)
    d["Telegram"] = txt + "\n\n✂️ Telegram corta solo en 4.096 caracteres por mensaje: publicar en 2-3 envíos si excede."
    return d

def derivar_en(txt):
    titulo = next((l for l in txt.splitlines() if l.startswith("# ")), "").lstrip("# ").strip()
    d = {}
    d["Reddit"] = txt
    tweets = []
    med = next((l for l in txt.splitlines() if l.startswith("⏱️")), "")
    tweets.append(recorta(f"{titulo} {med}".strip(), 275))
    for l in seccion(txt, "🗺️").splitlines():
        if l.startswith("- "):
            tweets.append(recorta(l[2:].strip(), 275))
    tesis = seccion(txt, "⚡").splitlines()
    if tesis:
        tweets.append(recorta("Thesis: " + tesis[0].lstrip("*").strip(), 275))
    for l in seccion(txt, "🔗").splitlines():
        if l.startswith("- ") and len(tweets) < 14:
            tweets.append(recorta(l[2:].strip(), 275))
    tweets.append(recorta(FIRMA, 275))
    n = len(tweets)
    d["X"] = "\n\n".join(f"{i+1}/{n} {t}" for i, t in enumerate(tweets))
    msgs, cur = [], ""
    for par in txt.split("\n\n"):
        if len(cur) + len(par) + 2 > 1990:
            msgs.append(cur.strip()); cur = par
        else:
            cur = cur + "\n\n" + par
    if cur.strip():
        msgs.append(cur.strip())
    d["Discord"] = "\n\n― mensaje {k}/{m} ―\n".replace("{m}", str(len(msgs))).join(
        ["― mensaje 1/{} ―".format(len(msgs))] + msgs[1:]) if msgs else ""
    d["Discord"] = "\n\n".join(f"― mensaje {i+1}/{len(msgs)} ―\n{m}" for i, m in enumerate(msgs))
    d["Telegram"] = txt + "\n\n✂️ Telegram splits at 4,096 characters per message: post in 2-3 sends if longer."
    return d

def main():
    ruta = pathlib.Path(sys.argv[1])
    txt = ruta.read_text(encoding="utf-8")
    solo = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--solo" else None
    nombre = ruta.name
    if "-es-dominicano-" in nombre:
        plats, der = ES, derivar_es(txt)
        tag = "es-dominicano"
    elif "-en-ingles-" in nombre:
        plats, der = EN, derivar_en(txt)
        tag = "en-ingles"
    else:
        sys.exit("el fichero no parece maestro: falta -es-dominicano- o -en-ingles- en el nombre")
    base = nombre.replace("-MAESTRO-", "-").replace("-MASTER-", "-")
    cuerpo = len(txt)
    ok = "OK" if 6000 <= cuerpo <= 45000 else "FUERA DE BANDA"
    print(f"maestro: {nombre} · cuerpo {cuerpo} car. · banda 6.000-45.000: {ok}")
    for p in sorted(plats):
        if solo and p != solo:
            continue
        out = ruta.with_name(base.replace(f"-{tag}-", f"-{tag}-{p}-", 1))
        contenido = der[p] + (f"\n\n*Derivado de {nombre} por tools/derivar_plataformas.py el {FECHA} "
                              f"· longitud {len(der[p])} car. · maestro en banda: {ok} ({cuerpo} car.)*\n")
        out.write_text(contenido, encoding="utf-8")
        print(f"  -> {out.name}  ({len(contenido)} car.)")

if __name__ == "__main__":
    main()
