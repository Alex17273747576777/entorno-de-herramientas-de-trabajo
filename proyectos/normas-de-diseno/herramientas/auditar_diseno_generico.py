#!/usr/bin/env python3
"""
Auditor de diseño GENÉRICO: aplica la ley de `REGLAS.md` a un repositorio cualquiera.

Por qué existe (incidencia #1): faltaba el procedimiento que se usa DESPUÉS de publicar. Volver a
una app seis meses más tarde y comprobar que nadie reintrodujo un violeta ni un degradado no puede
depender de acordarse, ni de releer la pantalla a ojo. `06-auditar-publicado.sh` llama a este
script; éste hace las medidas.

Dos principios que vienen de fracasos concretos, no de teoría:

1.  SE MIDE EL EFECTO, NO EL NOMBRE. La comprobación antigua de GLTools buscaba las cadenas
    `.vidrio(` y `Brush.linearGradient(`; en la 1.9.1 había 28 usos de `Cristal.vidrio` —el COLOR—
    y la ley daba verde con 30 cajas de cristal en pantalla (incidencia #7). Aquí se mide matiz en
    HSL, alfa, ARGB completo, usos de API y contraste WCAG 2.1 con la fórmula real. Renombrar no
    sirve de nada.

2.  LO QUE NO SE PUEDE MEDIR SE DECLARA, NO SE CALLA. Cada regla sabe si pudo medir o no. Si un
    repositorio no declara su paleta de forma reconocible, la regla de contraste dice
    `NO_MEDIBLE` y por qué, en vez de imprimir un verde que no significa nada. Un verde falso es
    peor que un rojo.

Cada umbral lleva escrito de dónde sale. Los que no se pudieron derivar de `REGLAS.md` ni de una
fuente medida se declaran como trinquete (no permiten empeorar) en vez de disfrazarse de ideal.

Uso:
    python3 auditar_diseno_generico.py RUTA_DEL_REPO
    python3 auditar_diseno_generico.py RUTA_DEL_REPO --estricto   # cualquier aviso corta
    python3 auditar_diseno_generico.py RUTA_DEL_REPO --json

Salida: 0 = sin incumplimientos · 1 = hay incumplimientos · 2 = no se pudo auditar.
"""
from __future__ import annotations

import argparse
import colorsys
import json
import re
import sys
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# UMBRALES. Cada uno con su procedencia.
# ─────────────────────────────────────────────────────────────────────────────

# REGLAS.md prohíbe el «violeta de plantilla (#7C4DFF, #6C5CE7, #A855F7 y parientes)». El rango de
# matiz sale de medir esos tres hex, no de elegir un número bonito: se calcula en hue_prohibido().
# La saturación mínima evita castigar un gris ligeramente frío.
SATURACION_MINIMA = 0.18

# REGLAS.md: «Cinco acentos compitiendo … UN acento, y el resto neutro», más el punto 3 de la
# superficie: verde = bien, ámbar = ojo, rojo = no se puede. O sea un acento + tres de estado = 4
# tonos saturados como máximo. Se cuentan los matices distintos con saturación >= este valor.
SATURACION_DE_ACENTO = 0.45
TOPE_ACENTOS_SATURADOS = 4

# REGLAS.md, superficie 1: «tres tonos de gris con los canales RGB casi iguales (diferencia <= 24)».
# El 24 es literal de la ley, no derivado.
DIFERENCIA_MAX_CANAL_FONDO = 24

# REGLAS.md, superficie 5: «el dato principal es grande (>= 24 sp), lo secundario pequeño
# (11-12 sp)». Ambos son literales de la ley.
SP_MIN_DATO_PRINCIPAL = 24.0
SP_MAX_SECUNDARIO = 12.0
# Una «escala» con dos pasos no es una escala. REGLAS.md prohíbe «tipografía … sin escala: títulos
# y cuerpo casi del mismo tamaño»; el mínimo de pasos distintos es la traducción medible.
PASOS_MIN_ESCALA = 4

# TRINQUETE, no ideal: en GLTools Reborn hay 22 tamaños distintos, que es un catálogo y no una
# escala. Se admite ese techo para que la regla no permita EMPEORAR y baje según se consolide.
TOPE_PASOS_TIPOGRAFICOS = 22

# REGLAS.md: «el contenido se apoya en el fondo … no cajas dentro de cajas. Una caja sólo cuando el
# contenido de verdad necesita un límite». Los topes numéricos salen de medir la app que sí cumple
# la ley (GLTools Reborn, 2026-11-17): 4 bordes, 78 cajas, 0 degradados, 2 colores translúcidos.
TOPE_BORDES_DECORATIVOS = 6
TOPE_CAJAS_REDONDEADAS = 110
TOPE_DEGRADADOS = 0
TOPE_TRANSLUCIDOS = 6
# Por encima de este alfa un fondo translúcido es vidrio (deja ver lo que hay debajo);
# por debajo es un tinte de estado. 0.5 es el punto medio: no sale de REGLAS.md, sale de
# que un fondo al 22 % no tapa nada y uno al 70 % sí.
ALFA_MIN_SUPERFICIE = 0.5
# Si el 90 % de las cajas comparten un único radio, son «tarjetas idénticas apiladas», que la ley
# prohíbe. Se mide la proporción del radio más usado.
PROPORSION_MAX_RADIO_UNICO = 0.90

# REGLAS.md: «cero movimiento: nada responde al toque, nada entra ni sale». Medible: si en toda la
# UI no hay ni una API de animación, la ley se incumple.
APIs_MOVIMIENTO = ("animate", "Animated", "spring(", "tween(", "transition", "Crossfade", "ripple")

# Contraste: WCAG 2.1. AA texto normal 4,5:1; texto grande (>= 18 sp) y componentes no textuales
# 3:1. No son negociables ni derivados: es el estándar.
CONTRASTE_MIN_TEXTO = 4.5
CONTRASTE_MIN_ACENTO = 3.0

# Distinción entre superficies vecinas. Derivado el 2026-11-17 midiendo los pasos de la paleta
# tonal OSCURA publicada por Material 3 (#1C1B1F -> #25232A -> #2B2930 -> #322F37 -> #38353D ->
# #434149): 1.103, 1.081, 1.092, 1.092 y 1.198:1. El paso más sutil que Material acepta es 1.081,
# así que ése es el suelo legítimo. Un umbral anterior mío de 1.15 estaba inventado y era exigente
# de más: habría forzado un cambio de paleta sin motivo.
DISTINCION_MIN_SUPERFICIES = 1.08

# Iconos que son caracteres de texto, prohibidos por REGLAS.md («◇ ◆ ✦ ▤ ? ↻ ✓ ×»). Se buscan
# éstos y parientes; el `?` y el `x` ASCII NO cuentan porque son prosa legítima.
ICONOS_DE_TEXTO = "◇◆◈◉●○■□▲△▼▽✦✧★☆✚✜✤➤➜↻↺⟳✓✔✕✖×⚙⚡☰☱⌂⌘⎔"

CARPETA_EXCLUIDA = {".git", "build", ".gradle", ".idea", "node_modules", "out", "dist"}


# ─────────────────────────────────────────────────────────────────────────────
# Color
# ─────────────────────────────────────────────────────────────────────────────

def hex_a_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def matiz(rgb: tuple[int, int, int]) -> tuple[float, float]:
    """(matiz en grados 0-360, saturación 0-1) en HSL."""
    h, l, s = colorsys.rgb_to_hls(*[c / 255.0 for c in rgb])
    return h * 360.0, s


def luminosidad(rgb: tuple[int, int, int]) -> float:
    """Luminosidad relativa de WCAG 2.1 (linearización sRGB, no media aritmética)."""
    def lin(c: int) -> float:
        v = c / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    la, lb = luminosidad(a), luminosidad(b)
    alto, bajo = max(la, lb), min(la, lb)
    return (alto + 0.05) / (bajo + 0.05)


def hue_prohibido() -> tuple[float, float, list[str]]:
    """Rango de matiz prohibido, DERIVADO de los tres violetas que REGLAS.md nombra."""
    nombres = ["#7C4DFF", "#6C5CE7", "#A855F7"]
    hs = [matiz(hex_a_rgb(n))[0] for n in nombres]
    return min(hs) - 1.0, max(hs) + 70.0, [f"{n}={h:.1f}°" for n, h in zip(nombres, hs)]


# ─────────────────────────────────────────────────────────────────────────────
# Lectura del repositorio
# ─────────────────────────────────────────────────────────────────────────────

def ficheros_kotlin(raiz: Path) -> list[Path]:
    out = []
    for p in sorted(raiz.rglob("*.kt")):
        if any(part in CARPETA_EXCLUIDA for part in p.parts):
            continue
        # sólo código de producto: los tests no diseñan pantallas
        if "/test/" in str(p).replace("\\", "/") or "/androidTest/" in str(p).replace("\\", "/"):
            continue
        out.append(p)
    return out


_BLOQUE = re.compile(r"/\*.*?\*/", re.S)
_LINEA = re.compile(r"//[^\n]*")


def quitar_comentarios(texto: str) -> str:
    """Texto sin comentarios, CONSERVANDO los saltos de línea (las líneas siguen cuadrando).

    Un comentario que mencione `Brush.` no es un degradado. Lo demostró una prueba de mutación: sin
    esto, documentar la ley en el propio código hacía fallar la compilación de la comprobación.
    """
    fuera = _BLOQUE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), texto)
    return _LINEA.sub(lambda m: " " * len(m.group(0)), fuera)


class Repo:
    """Lo que se pudo leer del repositorio, con las líneas reales de cada hallazgo."""

    def __init__(self, raiz: Path):
        self.raiz = raiz
        self.ficheros = ficheros_kotlin(raiz)
        self.crudo: dict[Path, list[str]] = {}
        self.limpio: dict[Path, list[str]] = {}
        for f in self.ficheros:
            t = f.read_text(encoding="utf-8", errors="replace")
            self.crudo[f] = t.splitlines()
            self.limpio[f] = quitar_comentarios(t).splitlines()
        self.paleta = self._leer_paleta()

    def rel(self, f: Path) -> str:
        try:
            return str(f.relative_to(self.raiz))
        except ValueError:
            return str(f)

    def _leer_paleta(self) -> dict[str, dict]:
        """nombre -> {argb, rgb, alfa, fichero, linea}.

        Se acepta cualquier color con nombre a la izquierda: `val x = Color(0xAARRGGBB)` y también
        `surfaceColor = Color(0xAARRGGBB)` como parámetro nombrado. Los `Color(0x…)` sin nombre, los
        `Color.Red`, `colorResource()` y `MaterialTheme.colorScheme` no se pueden clasificar por rol
        y se cuentan aparte como NO_CLASIFICABLES: una paleta que el auditor no puede leer no se
        mide, se declara.
        """
        # `val x = Color(0x…)` Y `parametro = Color(0x…)`: los dos dan un nombre al color, que es lo
        # que permite clasificarlo por rol. Un `Color(0x…)` suelto dentro de una expresión no tiene
        # nombre y se cuenta aparte, sin fingir que se puede medir.
        pat = re.compile(r"\b(\w+)\s*=\s*Color\(0x([0-9A-Fa-f]{8})\)")
        out: dict[str, dict] = {}
        for f, lineas in self.limpio.items():
            for i, ln in enumerate(lineas, 1):
                for m in pat.finditer(ln):
                    nombre, argb = m.group(1), m.group(2).upper()
                    out.setdefault(nombre, {
                        "argb": argb,
                        "rgb": hex_a_rgb(argb[2:]),
                        "alfa": int(argb[0:2], 16),
                        "fichero": self.rel(f),
                        "linea": i,
                        "sitios": [],
                    })
                    out[nombre]["sitios"].append(f"{self.rel(f)}:{i}")
        return out

    def contar(self, patron: str) -> list[str]:
        """`fichero:linea` de CADA coincidencia, no de cada línea (tres `.border(` en una línea son
        tres golpes; contar líneas subcontaba y lo cazó una prueba de mutación)."""
        r = re.compile(patron)
        hits = []
        for f, lineas in self.limpio.items():
            for i, ln in enumerate(lineas, 1):
                for _ in r.finditer(ln):
                    hits.append(f"{self.rel(f)}:{i}")
        return hits

    def lineas_con(self, patron: str) -> list[tuple[str, int, str]]:
        r = re.compile(patron)
        out = []
        for f, lineas in self.limpio.items():
            for i, ln in enumerate(lineas, 1):
                if r.search(ln):
                    out.append((self.rel(f), i, self.crudo[f][i - 1].strip()[:110]))
        return out


# ─────────────────────────────────────────────────────────────────────────────
# Clasificación de roles (necesaria para el contraste)
# ─────────────────────────────────────────────────────────────────────────────

RE_FONDO = re.compile(r"fondo|background|bg|base|canvas", re.I)
RE_SUPERFICIE = re.compile(r"superficie|surface|card|tarjeta|elevad|panel|container", re.I)
RE_TEXTO = re.compile(r"texto|text|foreground|letra|on[A-Z]|titulo|title|label|rotulo", re.I)
RE_ACENTO = re.compile(r"marca|accent|primary|principal|verde|ambar|amber|rojo|red|error|warning|"
                       r"exito|success|green|info|secundar|secondary|tertiary", re.I)


def clasificar(paleta: dict[str, dict]) -> dict[str, list[str]]:
    """Rol -> nombres. Es una heurística por nombre y SE DECLARA como tal: si el repositorio usa
    nombres que no encajan, las reglas de contraste dicen NO_MEDIBLE en vez de inventar pares."""
    roles: dict[str, list[str]] = {"fondo": [], "superficie": [], "texto": [], "acento": []}
    for nombre, v in paleta.items():
        r, g, b = v["rgb"]
        oscuro = luminosidad((r, g, b)) < 0.30
        if RE_TEXTO.search(nombre) and not oscuro:
            roles["texto"].append(nombre)
        elif RE_ACENTO.search(nombre):
            roles["acento"].append(nombre)
        elif RE_SUPERFICIE.search(nombre) and oscuro:
            roles["superficie"].append(nombre)
        elif RE_FONDO.search(nombre) and oscuro:
            roles["fondo"].append(nombre)
    return roles


# ─────────────────────────────────────────────────────────────────────────────
# Reglas
# ─────────────────────────────────────────────────────────────────────────────

def auditar(repo: Repo, estricto: bool) -> tuple[list[dict], list[dict], list[str]]:
    """(incumplimientos, avisos, no_medibles). Un aviso no corta salvo con --estricto."""
    malos: list[dict] = []
    avisos: list[dict] = []
    no_medibles: list[str] = []

    def mal(regla: str, ley: str, texto: str, sitios: list[str] | None = None) -> None:
        malos.append({"regla": regla, "ley": ley, "detalle": texto, "sitios": (sitios or [])[:8]})

    def aviso(regla: str, ley: str, texto: str, sitios: list[str] | None = None) -> None:
        avisos.append({"regla": regla, "ley": ley, "detalle": texto, "sitios": (sitios or [])[:8]})

    p = repo.paleta

    # ── R0 · integridad de la paleta ────────────────────────────────────────
    # No es una regla de REGLAS.md: es la que impide que las demás mientan. Nació de un verde falso
    # real (un `Color(0xFF)` mal escrito hizo desaparecer un color del recuento y el contraste dio
    # 36 pares en vez de 42, sin fallar).
    literales = sum(1 for f, ls in repo.limpio.items() for ln in ls
                    for _ in re.finditer(r"\bColor\(0x", ln))
    con_nombre = len([1 for v in p.values() for _ in v["sitios"]])
    malformados = repo.lineas_con(r"\bColor\(0x(?![0-9A-Fa-f]{8}\))")
    if malformados:
        mal("R0 integridad", "ninguna (meta-regla)",
            f"{len(malformados)} Color(0x…) mal escritos: el auditor no puede medirlos y tampoco "
            "compilan", [f"{f}:{i}" for f, i, _ in malformados])
    if literales - con_nombre > 0:
        no_medibles.append(
            f"R0 cobertura de la paleta: hay {literales} literales Color(0x…) y {con_nombre} tienen "
            "un nombre a la izquierda, que es lo que permite clasificarlos por rol. Los "
            f"{literales - con_nombre} restantes van sueltos dentro de una expresión (o son "
            "Color.Red / colorResource / MaterialTheme.colorScheme) y las reglas de paleta NO los "
            "cubren. No es un incumplimiento: es el alcance real de esta auditoría.")
    if not p:
        no_medibles.append(
            "R13/R14 contraste y distinción de superficies: el repositorio no declara colores con "
            "`Color(0xAARRGGBB)` en código de producto (probablemente usa MaterialTheme.colorScheme "
            "o recursos XML). Sin paleta legible no hay contraste que medir, y no se va a fingir.")

    # ── R1 · violeta de plantilla, por matiz ────────────────────────────────
    bajo, alto, evidencia = hue_prohibido()
    viol = []
    for nombre, v in p.items():
        h, s = matiz(v["rgb"])
        if bajo <= h <= alto and s > SATURACION_MINIMA:
            viol.append(f"{nombre} #{v['argb'][2:]} matiz={h:.0f}° sat={s:.2f} ({v['fichero']}:{v['linea']})")
    if viol:
        mal("R1 violeta de plantilla", "REGLAS.md · PROHIBIDO · «Violeta de plantilla (#7C4DFF, "
            "#6C5CE7, #A855F7 y parientes)»",
            f"{len(viol)} colores en el rango prohibido {bajo:.0f}-{alto:.0f}° → " + "; ".join(viol))

    # ── R2 · acentos compitiendo ────────────────────────────────────────────
    saturados: dict[int, list[str]] = {}
    for nombre, v in p.items():
        h, s = matiz(v["rgb"])
        if s >= SATURACION_DE_ACENTO:
            saturados.setdefault(round(h / 12.0), []).append(nombre)
    if len(saturados) > TOPE_ACENTOS_SATURADOS:
        mal("R2 acentos", "REGLAS.md · PROHIBIDO · «Cinco acentos compitiendo … UN acento, y el "
            "resto neutro» + superficie 3 (verde/ámbar/rojo de estado)",
            f"{len(saturados)} familias de matiz saturadas (tope {TOPE_ACENTOS_SATURADOS}) → "
            + "; ".join(f"{k*12}°: {','.join(v)}" for k, v in sorted(saturados.items())))

    # ── R3 · fondo neutro (canales RGB casi iguales) ────────────────────────
    roles = clasificar(p)
    fondos = roles["fondo"] + roles["superficie"]
    coloreados = []
    for nombre in fondos:
        r, g, b = p[nombre]["rgb"]
        d = max(r, g, b) - min(r, g, b)
        if d > DIFERENCIA_MAX_CANAL_FONDO:
            coloreados.append(f"{nombre} #{p[nombre]['argb'][2:]} diferencia={d} "
                              f"({p[nombre]['fichero']}:{p[nombre]['linea']})")
    if coloreados:
        mal("R3 fondo neutro", "REGLAS.md · superficie 1 · «tres tonos de gris con los canales RGB "
            f"casi iguales (diferencia ≤ {DIFERENCIA_MAX_CANAL_FONDO})»",
            f"{len(coloreados)} fondos/superficies con color → " + "; ".join(coloreados))
    if not fondos and p:
        no_medibles.append("R3 fondo neutro: ningún color se clasificó como fondo o superficie por "
                           "su nombre. La clasificación es heurística y se declara antes que "
                           "imprimir un verde que no significa nada.")

    # ── R4 · degradados ─────────────────────────────────────────────────────
    deg = repo.contar(r"\bBrush\.")
    if len(deg) > TOPE_DEGRADADOS:
        mal("R4 degradados", "REGLAS.md · PROHIBIDO · «Degradados por todas partes» y «Degradados "
            "decorativos, incluido el linearGradient de dos tonos»",
            f"{len(deg)} usos de Brush. (tope {TOPE_DEGRADADOS})", deg)

    # ── R5 · vidrio en el contenido ─────────────────────────────────────────
    translucidos = [n for n, v in p.items() if v["alfa"] < 0xFF]
    # Vidrio de verdad = una SUPERFICIE translúcida: `.background(color.copy(alpha = X))` con X alto,
    # o un color de la paleta declarado translúcido y usado de fondo. Lo demás —`.copy(alpha = 0f)`
    # para dejar invisible lo no seleccionado, `0.10f`-`0.25f` para teñir una ficha seleccionada,
    # `Modifier.alpha()` y `color = texto.copy(alpha = 0.6f)` para atenuar— son ESTADOS, no vidrio, y
    # la ley no los prohíbe. Medirlo todo junto daba 18 falsos positivos en una app que cumple.
    vidrio, tinte, sin_literal = [], [], []
    pat_alfa = re.compile(r"\.background\([^)]*?copy\(\s*alpha\s*=\s*([0-9.]+)f?\s*\)")
    for f, lineas in repo.limpio.items():
        for i, ln in enumerate(lineas, 1):
            for m in pat_alfa.finditer(ln):
                try:
                    a = float(m.group(1))
                except ValueError:
                    sin_literal.append(f"{repo.rel(f)}:{i}"); continue
                (vidrio if a >= ALFA_MIN_SUPERFICIE else tinte).append(f"{repo.rel(f)}:{i} (alpha={a:g})")
    for f, lineas in repo.limpio.items():
        for i, ln in enumerate(lineas, 1):
            if re.search(r"\.background\(\s*[\w.]+\s*\)", ln):
                for n in translucidos:
                    if re.search(rf"\b{n}\b", ln):
                        vidrio.append(f"{repo.rel(f)}:{i} (fondo con `{n}`, alfa {p[n]['alfa']:02X})")
    if len(vidrio) > TOPE_TRANSLUCIDOS:
        mal("R5 vidrio", "REGLAS.md · PROHIBIDO · «Cristal/glass en todo» y «Vidrio en el "
            "contenido. Si la superficie no flota sobre nada, no es vidrio: es una caja»",
            f"{len(vidrio)} superficies translúcidas (tope {TOPE_TRANSLUCIDOS})", vidrio)
    if sin_literal:
        no_medibles.append(
            f"R5 vidrio: {len(sin_literal)} fondos usan un alfa que no es un literal "
            f"({', '.join(sin_literal[:3])}…). Sin el valor no se sabe si es vidrio o un tinte de "
            "estado, y no se va a juzgar a ciegas.")
    # Un color llamado «vidrio» con alfa FF no es vidrio: es un alias. Se mide el alfa, no el nombre.
    for nombre, v in p.items():
        if re.search(r"vidrio|glass|cristal|blur", nombre, re.I) and v["alfa"] >= 0xFF:
            mal("R5 vidrio", "REGLAS.md · PROHIBIDO · «Vidrio en el contenido»",
                f"`{nombre}` se llama vidrio pero es opaco (alfa {v['alfa']:02X}): un color opaco "
                f"idéntico a una superficie no es vidrio, es un alias con nombre bonito "
                f"({v['fichero']}:{v['linea']})")

    # ── R6 · bordes decorativos ─────────────────────────────────────────────
    bordes = repo.contar(r"\.border\(")
    if len(bordes) > TOPE_BORDES_DECORATIVOS:
        mal("R6 bordes", "REGLAS.md · superficie 2 y 4 · la elevación se expresa «por tono, no por "
            "borde ni por sombra»; el contenido se apoya en el fondo, «no cajas dentro de cajas»",
            f"{len(bordes)} usos de .border( (tope {TOPE_BORDES_DECORATIVOS})", bordes)

    # ── R7 · tarjetas idénticas apiladas ────────────────────────────────────
    cajas = repo.contar(r"RoundedCornerShape\(")
    valores = []
    for f, lineas in repo.limpio.items():
        for ln in lineas:
            valores += [int(x) for x in re.findall(r"RoundedCornerShape\(\s*(\d+)", ln)]
    if len(cajas) > TOPE_CAJAS_REDONDEADAS:
        mal("R7 cajas", "REGLAS.md · PROHIBIDO · «Tarjetas idénticas apiladas sin jerarquía»",
            f"{len(cajas)} cajas redondeadas (tope {TOPE_CAJAS_REDONDEADAS})", cajas)
    if valores:
        distintos = sorted(set(valores))
        mas_usado = max(distintos, key=valores.count)
        proporcion = valores.count(mas_usado) / len(valores)
        if len(distintos) < 2 and len(valores) >= 8:
            mal("R7 cajas", "REGLAS.md · PROHIBIDO · «todo el mismo radio, la misma opacidad, el "
                "mismo peso, la misma separación»",
                f"{len(valores)} cajas con UN SOLO radio ({mas_usado} dp): no hay jerarquía de forma")
        elif proporcion >= PROPORSION_MAX_RADIO_UNICO and len(valores) >= 8:
            aviso("R7 cajas", "REGLAS.md · PROHIBIDO · «todo el mismo radio»",
                  f"{proporcion:.0%} de las {len(valores)} cajas usan el mismo radio ({mas_usado} dp); "
                  f"radios distintos: {distintos}")

    # ── R8 · jerarquía tipográfica real ─────────────────────────────────────
    pasos: dict[float, list[str]] = {}
    for f, lineas in repo.limpio.items():
        for i, ln in enumerate(lineas, 1):
            for m in re.finditer(r"fontSize\s*=\s*(\d+(?:[.,]\d+)?)\s*\.sp", ln):
                pasos.setdefault(float(m.group(1).replace(",", ".")), []).append(f"{repo.rel(f)}:{i}")
    if pasos:
        orden = sorted(pasos)
        if max(orden) < SP_MIN_DATO_PRINCIPAL:
            mal("R8 tipografía", "REGLAS.md · superficie 5 · «el dato principal es grande "
                f"(≥ {SP_MIN_DATO_PRINCIPAL:.0f} sp)»",
                f"el tamaño mayor de toda la UI es {max(orden):g} sp: no hay dato principal grande")
        if min(orden) > SP_MAX_SECUNDARIO:
            mal("R8 tipografía", "REGLAS.md · superficie 5 · «lo secundario pequeño (11-12 sp)»",
                f"el tamaño menor es {min(orden):g} sp: no hay texto secundario pequeño")
        if len(orden) < PASOS_MIN_ESCALA:
            mal("R8 tipografía", "REGLAS.md · PROHIBIDO · «Tipografía por defecto del sistema, sin "
                "escala: títulos y cuerpo casi del mismo tamaño»",
                f"{len(orden)} pasos distintos ({', '.join(f'{x:g}' for x in orden)}): "
                f"una escala necesita al menos {PASOS_MIN_ESCALA}")
        if len(orden) > TOPE_PASOS_TIPOGRAFICOS:
            mal("R8 tipografía", "trinquete: un catálogo de tamaños no es una escala",
                f"{len(orden)} tamaños distintos (tope {TOPE_PASOS_TIPOGRAFICOS}): "
                + ", ".join(f"{x:g}" for x in orden))
    else:
        no_medibles.append("R8 tipografía: no se encontró ni un `fontSize = N.sp`. O la UI no fija "
                           "tamaños (usa sólo los estilos de Material, que es legítimo) o no es "
                           "Compose. Sin medidas no se juzga.")

    # ── R9 · iconos que son caracteres de texto ─────────────────────────────
    ui = [f for f in repo.ficheros
          if "androidx.compose" in "\n".join(repo.crudo[f][:80])
          or re.search(r"@Composable", "\n".join(repo.crudo[f]))]
    no_medibles.append(
        f"R9/R10 alcance: sólo se juzgan los {len(ui)} ficheros de interfaz (importan "
        "androidx.compose o llevan @Composable). Un ⛔ o un ✓ en un informe de texto que se guarda "
        "en un fichero o se registra no es un icono de interfaz y la ley no lo prohíbe: en GLTools "
        "hay seis, en core/, y están bien donde están.")
    iconos = []
    for f, i, txt in [(f, i, t) for f, i, t in repo.lineas_con(r"Text\(\s*[\"']")
                      if any(f == repo.rel(g) for g in ui)]:
        encontrados = [c for c in txt if c in ICONOS_DE_TEXTO]
        if encontrados:
            iconos.append(f"{f}:{i} ({''.join(dict.fromkeys(encontrados))})")
    if iconos:
        mal("R9 iconos de texto", "REGLAS.md · PROHIBIDO · «Iconos que son caracteres de texto "
            "(◇ ◆ ✦ ▤ ? ↻ ✓ ×) en vez de rutas dibujadas»",
            f"{len(iconos)} sitios con caracteres usados como icono", iconos)

    # ── R10 · emojis como iconos ────────────────────────────────────────────
    emojis = []
    pat_emoji = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
    rutas_ui = {repo.rel(g) for g in ui}
    for f, i, txt in repo.lineas_con(r"[\"']"):
        if f in rutas_ui and pat_emoji.search(txt):
            emojis.append(f"{f}:{i}")
    if emojis:
        mal("R10 emojis", "REGLAS.md · PROHIBIDO · «Emojis como iconos de interfaz»",
            f"{len(emojis)} cadenas con emojis en código de producto", emojis)

    # ── R11 · estados vacíos que sólo dicen «no hay datos» ──────────────────
    vacios = repo.lineas_con(r"[\"']\s*(No hay datos|Sin datos|No data|Nothing here|Empty)\s*[\"']")
    if vacios:
        aviso("R11 estados vacíos", "REGLAS.md · PROHIBIDO · «Estados vacíos que dicen «No hay "
              "datos» y nada más»",
              f"{len(vacios)} cadenas que se agotan en anunciar la ausencia",
              [f"{f}:{i}" for f, i, _ in vacios])

    # ── R12 · cero movimiento ───────────────────────────────────────────────
    mov = []
    for api in APIs_MOVIMIENTO:
        mov += repo.contar(re.escape(api))
    if repo.ficheros and not mov:
        mal("R12 movimiento", "REGLAS.md · PROHIBIDO · «Cero movimiento: nada responde al toque, "
            "nada entra ni sale, todo aparece de golpe»",
            "ninguna API de animación en todo el código de producto")

    # ── R13 · contraste WCAG 2.1 ────────────────────────────────────────────
    textos = roles["texto"]
    superficies = roles["fondo"] + roles["superficie"]
    if textos and superficies:
        pares = 0
        fallidos = []
        for t in textos:
            for s in superficies:
                ratio = contraste(p[t]["rgb"], p[s]["rgb"])
                pares += 1
                if ratio < CONTRASTE_MIN_TEXTO:
                    fallidos.append(f"{t}/{s}={ratio:.2f}")
        if fallidos:
            mal("R13 contraste AA", "WCAG 2.1 · texto normal 4,5:1 (no es REGLAS.md: es el estándar "
                "que la ley de accesibilidad supone)",
                f"{pares} pares medidos, {len(fallidos)} por debajo de {CONTRASTE_MIN_TEXTO}:1 → "
                + "; ".join(fallidos[:10]))
        for a in roles["acento"]:
            for s in superficies:
                ratio = contraste(p[a]["rgb"], p[s]["rgb"])
                if ratio < CONTRASTE_MIN_ACENTO:
                    mal("R13 contraste acentos", "WCAG 2.1 · componentes no textuales 3:1",
                        f"el acento `{a}` sobre `{s}` da {ratio:.2f}:1, por debajo de "
                        f"{CONTRASTE_MIN_ACENTO}:1")
    elif p and not no_medibles:
        no_medibles.append("R13 contraste: la paleta se lee pero los nombres no permiten separar "
                           "texto de superficie. Sin roles no hay pares que medir.")

    # ── R14 · distinción entre superficies por tono ─────────────────────────
    supers = sorted(roles["superficie"], key=lambda n: luminosidad(p[n]["rgb"]))
    fondos_n = sorted(roles["fondo"], key=lambda n: luminosidad(p[n]["rgb"]))
    if len(supers) >= 2 or (supers and fondos_n):
        debiles, medidas = [], []
        # (a) la escalera de superficies, que es lo que la ley exige literalmente
        for a, b in zip(supers, supers[1:]):
            r = contraste(p[a]["rgb"], p[b]["rgb"])
            medidas.append(f"{a}/{b}={r:.2f}")
            if r < DISTINCION_MIN_SUPERFICIES:
                debiles.append(f"{a}/{b}={r:.2f} (escalón de superficie)")
        # (b) cada superficie contra el fondo más desfavorable. Esto NO es un incumplimiento y la
        #     primera versión lo trataba como si lo fuera: REGLAS.md, superficie 2, exige «TRES
        #     NIVELES DE SUPERFICIE que se distinguen por tono» y los nombra (superficie,
        #     superficieAlta, superficieMasAlta). El lienzo no es uno de esos niveles, y exigirle al
        #     telón el mismo paso que a la escalera es inventarse un umbral otra vez —el mismo error
        #     que el 1.15 de la primera versión—. Se mide y se AVISA, con el número y el motivo,
        #     porque hay un sitio donde importa de verdad: una hoja o un diálogo que flota con cajas
        #     dentro puede perder el límite de la caja. Comprobarlo con los ojos es incidencia #6.
        for sup in supers:
            peor = min(((contraste(p[sup]["rgb"], p[f]["rgb"]), f) for f in fondos_n), default=None)
            if peor:
                r, f = peor
                medidas.append(f"{sup}/{f}(fondo más próximo)={r:.2f}")
                if r < DISTINCION_MIN_SUPERFICIES:
                    aviso("R14b superficie sobre el lienzo",
                          "REGLAS.md · PROHIBIDO · «Tarjetas idénticas apiladas sin jerarquía» (no la "
                          "regla de los tres niveles, que sólo gobierna la escalera de superficies)",
                          f"`{sup}` sobre `{f}` se queda en {r:.2f}:1, por debajo del paso más sutil "
                          f"que Material 3 acepta entre niveles ({DISTINCION_MIN_SUPERFICIES}:1). Si "
                          f"`{f}` es el contenedor de una hoja, un diálogo o una barra que flota, las "
                          f"cajas `{sup}` de dentro pueden perder su límite. Hace falta verlo en "
                          "pantalla para saber si se pierde: incidencia #6.")
        if debiles:
            mal("R14 superficies", "REGLAS.md · superficie 2 · «tres niveles de superficie que se "
                "distinguen por tono, no por borde ni por sombra»",
                f"{len(debiles)} pares que no se distinguen (mínimo "
                f"{DISTINCION_MIN_SUPERFICIES}:1, derivado de los pasos de la paleta tonal oscura de "
                "Material 3) → " + "; ".join(debiles) + " · todo lo medido: " + ", ".join(medidas))
    elif p:
        no_medibles.append("R14 superficies: se clasificaron menos de dos superficies/fondos, así "
                           "que no hay escalones que comparar.")

    # ── R15 · dos nombres, el mismo color ───────────────────────────────────
    vistos: dict[str, list[str]] = {}
    for nombre, v in p.items():
        vistos.setdefault(v["argb"], []).append(nombre)
    duplicados = {k: v for k, v in vistos.items() if len(v) > 1}
    if duplicados:
        mal("R15 duplicados", "REGLAS.md · superficie 2 · la jerarquía se expresa por tono: dos "
            "nombres con el mismo ARGB son un alias, y un alias con nombre bonito es exactamente "
            "cómo se esquivó la ley en la 1.9.1 (incidencia #7)",
            "; ".join(f"{k[2:]} = {'/'.join(v)}" for k, v in duplicados.items()))

    # ── Lo que este auditor NO puede medir, dicho en voz alta ───────────────
    no_medibles += [
        "El tacto y el ritmo: si la interfaz se siente bien exige pantalla encendida.",
        "Si un elemento pequeño se ve de verdad (un chevrón de 14 dp, un rótulo de 9,5 sp): "
        "exige captura real, no texto.",
        "Si una fila se corta en un ancho concreto: exige medir el texto renderizado.",
        "El número exacto de cajas visibles por pantalla: aquí se cuentan usos en el texto, no la "
        "composición real. Un `if` puede no ejecutarse nunca.",
        "Si los botones primario/secundario/destructivo se distinguen: se puede medir el color, no "
        "la percepción de peso.",
    ]
    return malos, avisos, no_medibles


def main() -> int:
    ap = argparse.ArgumentParser(description="Auditor de diseño genérico (ley de REGLAS.md)")
    ap.add_argument("repo", help="ruta del repositorio a auditar")
    ap.add_argument("--estricto", action="store_true", help="los avisos también cortan")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    a = ap.parse_args()

    raiz = Path(a.repo).resolve()
    if not raiz.is_dir():
        print(f"NO EXISTE el directorio {raiz}", file=sys.stderr)
        return 2
    repo = Repo(raiz)
    if not repo.ficheros:
        print(f"NO HAY código Kotlin de producto en {raiz}: nada que auditar "
              "(este auditor mide Compose/Kotlin; para otra tecnología hace falta otro)",
              file=sys.stderr)
        return 2

    malos, avisos, no_medibles = auditar(repo, a.estricto)
    hue_bajo, hue_alto, evidencia = hue_prohibido()

    if a.json:
        print(json.dumps({
            "repo": str(raiz),
            "ficheros": len(repo.ficheros),
            "colores": {k: {"argb": v["argb"], "sitios": v["sitios"]} for k, v in repo.paleta.items()},
            "rango_matiz_prohibido": [round(hue_bajo, 1), round(hue_alto, 1)],
            "derivacion_del_rango": evidencia,
            "incumplimientos": malos,
            "avisos": avisos,
            "no_medibles": no_medibles,
        }, ensure_ascii=False, indent=1))
    else:
        print(f"AUDITORÍA DE DISEÑO · {raiz.name}")
        print(f"  {len(repo.ficheros)} ficheros Kotlin de producto · {len(repo.paleta)} colores "
              f"declarados con Color(0xAARRGGBB)")
        print(f"  rango de matiz prohibido {hue_bajo:.0f}-{hue_alto:.0f}°, derivado de "
              f"REGLAS.md: {', '.join(evidencia)}")
        print()
        if malos:
            print(f"INCUMPLIMIENTOS ({len(malos)}):")
            for m in malos:
                print(f"  ✗ {m['regla']}")
                print(f"      ley: {m['ley']}")
                print(f"      {m['detalle']}")
                for s in m["sitios"]:
                    print(f"        · {s}")
            print()
        if avisos:
            print(f"AVISOS ({len(avisos)}) — no cortan, salvo con --estricto:")
            for m in avisos:
                print(f"  ! {m['regla']}: {m['detalle']}")
                for s in m["sitios"]:
                    print(f"        · {s}")
            print()
        if no_medibles:
            print(f"NO SE PUEDE MEDIR ({len(no_medibles)}) — declarado, no escondido:")
            for n in no_medibles:
                print(f"  · {n}")
            print()
        total = len(malos) + (len(avisos) if a.estricto else 0)
        print(f"RESULTADO: {'SIN INCUMPLIMIENTOS' if not total else str(total) + ' INCUMPLIMIENTOS'}")
    return 1 if (malos or (a.estricto and avisos)) else 0


if __name__ == "__main__":
    sys.exit(main())
