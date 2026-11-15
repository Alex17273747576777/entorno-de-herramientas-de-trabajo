#!/usr/bin/env python3
"""compuerta-canal-y-mision — las dos compuertas que a la vara de la-bandita-archivo le faltan.

La casa tiene 17 compuertas (G0-G17) que dan «fallos: NINGUNO» y aun así el paquete está roto,
porque miden forma/presencia/integridad pero NO:
  · G18 CANAL  — ¿el texto se renderiza en la plataforma donde se publica? (Facebook no renderiza
                 vallas de código ``` ni tablas Markdown |; el CORAZON:312 ya lo prohíbe y ninguna
                 compuerta lo comprueba.)
  · G19 MISIÓN — ¿la pieza es de código abierto como manda la Parte 0-BIS, o derivó a cultura pop?
                 («el grupo se centra en la novedad y la complejidad de las aplicaciones de código
                 abierto, no en lo popular, lo de moda o lo fácil».)

Uso:
    compuerta-canal-y-mision.py RUTA_PUBLICACIONES [--json]
Sale 1 si alguna pieza falla G18 o G19 (es una vara, no un adorno).
"""
import argparse, json, pathlib, re, sys

# Una pieza de misión mide repositorios de código abierto. La señal robusta NO es el slug pelado
# owner/repo (que caza ruido: EntityData/Q193835.json de Wikidata y docs/MEDICION-P37.json internos,
# y dejaba pasar la cultura pop) sino el VOCABULARIO DE MEDICIÓN que toda ficha de repo lleva y que
# una pieza de cultura pop (Kung Fu Panda, Canserbero, El Quijote) no tiene nunca.
RE_REPO_URL = re.compile(r"github\.com/[\w.-]+/[\w.-]+")
RE_ESTRELLA = re.compile(r"★|\bestrellas\b")
RE_REPO_PALABRA = re.compile(r"\brepositorios?\b|\brepos\b")
RE_LICENCIA = re.compile(r"\b(Apache-2\.0|GPL-[23]\.0|AGPL-[3.]+|MIT|MPL-2\.0|BSD-[23]-Clause|UPL|NOASSERTION)\b")


def piezas_carpetas(raiz: pathlib.Path):
    """Devuelve (canal, lista de ficheros de cuerpo) por carpeta de canal."""
    canales = {}
    for carpeta in sorted(p for p in raiz.iterdir() if p.is_dir()):
        nombre = carpeta.name
        if nombre.startswith("_"):
            continue
        cuerpo = []
        for f in sorted(carpeta.glob("*.md")):
            n = f.name
            if "Comentario-fijado" in n or n.startswith("LEEME"):
                continue
            cuerpo.append(f)
        if cuerpo:
            canales[nombre] = cuerpo
    return canales


def chequear_canal(canal: str, texto: str):
    """G18: qué rompe el renderizado en este canal."""
    fallos = []
    es_facebook = "facebook" in canal.lower()
    if es_facebook:
        if "```" in texto:
            fallos.append("valla de código ``` (Facebook muestra los backticks literales)")
        if re.search(r"^\|.+\|", texto, re.MULTILINE):
            n = len(re.findall(r"^\|.+\|", texto, re.MULTILINE))
            fallos.append(f"tabla Markdown | ({n} filas) (Facebook no renderiza tablas; CORAZON:312)")
    return fallos


def chequear_mision(nombre_canal: str, texto: str):
    """G19: ¿es pieza de código abierto o derivó a cultura pop?

    La misión (Parte 0-BIS) es «novedad y complejidad de las aplicaciones de código abierto». Una
    pieza en misión mide repos: cita slugs owner/repo y estrellas (★). Una pieza de cultura pop
    (Kung Fu Panda, Canserbero, El Quijote) no mide ningún repo: 0 ★ y 0 slugs. Ése es el discriminador.
    """
    # Sólo el ciclo vivo numerado (Facebook/WhatsApp dominicano-ES) debe misión de código abierto.
    if not re.search(r"dominicano-ES", nombre_canal):
        return None  # POSTS-COMUNIDAD y otros no son serie de misión
    estrellas = len(RE_ESTRELLA.findall(texto))
    urls = len(set(RE_REPO_URL.findall(texto)))
    repos = len(RE_REPO_PALABRA.findall(texto))
    licencias = len(set(RE_LICENCIA.findall(texto)))
    # En misión si mide repos: estrellas, o URLs de repo, o la palabra «repositorio», o licencias SPDX.
    en_mision = estrellas >= 3 or urls >= 1 or repos >= 3 or licencias >= 2
    if not en_mision:
        return (f"MISIÓN: {estrellas} ★, {urls} URLs de repo, {repos} «repositorio», {licencias} licencias "
                f"→ no mide código abierto; fuera de la misión (Parte 0-BIS: «no lo popular, lo de moda o lo fácil»)")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("ruta", help="carpeta 01-PUBLICACIONES del repo")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raiz = pathlib.Path(args.ruta)
    if not raiz.is_dir():
        print(f"ERROR no existe la carpeta: {raiz}", file=sys.stderr)
        return 2

    canales = piezas_carpetas(raiz)
    rojas = []
    total = 0
    for canal, ficheros in canales.items():
        for f in ficheros:
            total += 1
            texto = f.read_text(encoding="utf-8", errors="replace")
            fallos = chequear_canal(canal, texto)
            mision = chequear_mision(canal, texto)
            if mision:
                fallos.append(mision)
            if fallos:
                rojas.append({"canal": canal, "pieza": f.name, "fallos": fallos})

    resumen = {
        "piezas_examinadas": total,
        "piezas_en_rojo": len(rojas),
        "g18_formato_canal": sum(1 for r in rojas if any("valla" in x or "tabla" in x for x in r["fallos"])),
        "g19_mision": sum(1 for r in rojas if any(x.startswith("MISIÓN") for x in r["fallos"])),
    }

    if args.json:
        print(json.dumps({"resumen": resumen, "rojas": rojas}, ensure_ascii=False, indent=2))
    else:
        print("COMPUERTA CANAL (G18) + MISIÓN (G19) · las dos que le faltan a la vara")
        print(f"  piezas examinadas : {resumen['piezas_examinadas']}")
        print(f"  piezas en rojo    : {resumen['piezas_en_rojo']}")
        print(f"  → G18 formato/canal: {resumen['g18_formato_canal']} piezas rompen el renderizado de su canal")
        print(f"  → G19 misión        : {resumen['g19_mision']} piezas fuera de la misión de código abierto")
        print()
        for r in rojas:
            print(f"  ✗ [{r['canal']}] {r['pieza'][:70]}")
            for x in r["fallos"]:
                print(f"      · {x}")
        print()
        if rojas:
            print(f"VEREDICTO: ROJO · {len(rojas)} piezas fallan G18/G19 (la vara de la casa da NINGUNO; ésta no)")
        else:
            print("VEREDICTO: VERDE · ninguna pieza falla G18/G19")
    return 1 if rojas else 0


if __name__ == "__main__":
    raise SystemExit(main())
