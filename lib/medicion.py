"""Medición de piezas — cuenta lo que una publicación realmente tiene.

Regla de oro: medir el CUERPO, no el archivo. Un encabezado de 200 caracteres
y siete párrafos repetidos no son una pieza de 46.000 caracteres.
"""
from __future__ import annotations
import re, unicodedata

MIN_FACEBOOK = 45_000   # mínimo declarado en CIMIENTOS
MAX_SANO     = 62_000   # por encima de esto, casi siempre es relleno


def leer(ruta: str) -> str:
    with open(ruta, encoding="utf-8", errors="replace") as f:
        return f.read()


def sin_encabezado(texto: str) -> str:
    """Quita líneas de título markdown (#) que no son prosa."""
    return re.sub(r"^#{1,6} .*$", "", texto, flags=re.M)


def parrafos(texto: str, minimo: int = 120) -> list[str]:
    """Párrafos normalizados y de prosa real (>= minimo caracteres)."""
    limpio = sin_encabezado(texto)
    trozos = re.split(r"\n\s*\n", limpio)
    salida = []
    for t in trozos:
        n = re.sub(r"\s+", " ", t).strip()
        if len(n) >= minimo and not n.startswith("|") and not n.startswith("━"):
            salida.append(n)
    return salida


def medir(ruta: str) -> dict:
    texto = leer(ruta)
    cuerpo = sin_encabezado(texto)
    ps = parrafos(texto)
    return {
        "ruta": ruta,
        "bytes": len(texto.encode("utf-8")),
        "caracteres_archivo": len(texto),
        "caracteres_cuerpo": len(cuerpo),
        "palabras": len(cuerpo.split()),
        "lineas": texto.count("\n") + 1,
        "parrafos": len(ps),
        "parrafos_unicos": len(set(ps)),
        "caracteres_prosa": sum(len(p) for p in ps),
    }


def veredicto(m: dict, minimo: int = MIN_FACEBOOK, maximo: int = MAX_SANO) -> tuple[str, list[str]]:
    notas = []
    c = m["caracteres_prosa"]
    if c < minimo:
        notas.append(f"FALTA: {minimo - c:,} caracteres de prosa para el mínimo ({c:,}/{minimo:,})")
    if c > maximo:
        notas.append(f"EXCESO: {c - maximo:,} caracteres por encima del techo sano ({c:,}/{maximo:,})")
    estado = "APTO" if not notas else "NO APTO"
    return estado, notas
