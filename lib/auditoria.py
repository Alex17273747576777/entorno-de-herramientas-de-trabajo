"""Auditoría de relleno — detecta párrafos repetidos literalmente.

Este módulo nació de un caso real: diez publicaciones (31 a 40) que declaraban
~46.000 caracteres y resultaron tener el mismo párrafo repetido hasta 7 veces.
Un archivo largo no es una pieza larga.
"""
from __future__ import annotations
import collections, re
from . import medicion

RELLENO_TOLERADO = 8.0   # % de caracteres repetidos que se acepta (recap legítimo)


def auditar(ruta: str, minimo_parrafo: int = 120) -> dict:
    ps = medicion.parrafos(medicion.leer(ruta), minimo=minimo_parrafo)
    total = sum(len(p) for p in ps) or 1
    cuenta = collections.Counter(ps)
    repetidos = {p: n for p, n in cuenta.items() if n > 1}
    chars_repetidos = sum(len(p) * (n - 1) for p, n in repetidos.items())
    pct = 100.0 * chars_repetidos / total
    peores = sorted(repetidos.items(), key=lambda kv: -len(kv[0]) * (kv[1] - 1))[:5]
    return {
        "ruta": ruta,
        "parrafos": len(ps),
        "bloques_repetidos": len(repetidos),
        "caracteres_repetidos": chars_repetidos,
        "pct_relleno": round(pct, 1),
        "veredicto": "LIMPIO" if pct <= RELLENO_TOLERADO else "RELLENO",
        "peores": [(n, len(p), p[:110]) for p, n in peores],
    }


def prosa_unica(ruta: str) -> int:
    """Caracteres de prosa que quedan si se eliminan las repeticiones."""
    a = auditar(ruta)
    m = medicion.medir(ruta)
    return m["caracteres_prosa"] - a["caracteres_repetidos"]


def frase_repetida(ruta: str, n: int = 6) -> str | None:
    """Detecta muletillas de plantilla: la misma frase inicial n veces o más."""
    texto = medicion.leer(ruta)
    frases = re.findall(r"^[^.\n]{60,140}\.", texto, flags=re.M)
    cuenta = collections.Counter(re.sub(r"\s+", " ", f).strip() for f in frases)
    for frase, c in cuenta.most_common(1):
        if c >= n:
            return f"{c}× · {frase[:120]}"
    return None
