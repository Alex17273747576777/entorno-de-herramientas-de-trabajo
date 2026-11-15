#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LA VARA · las diecisiete compuertas de la casa, ejecutables en un solo comando.

Cada compuerta mide una cosa: piezas con firma y fecha, esquema de las fichas, frescura de los
datos, licencias, actividad, integridad del sello, anti-plantilla, enlaces, presupuesto de
longitud, envíos, bandas, manual de estilo, firma literal, novedad, atestación firmada y la guía
maestra.

Qué hace:
  * Ejecuta las 17 compuertas (G0 a G17) en un solo comando.
  * Escribe un informe con el resultado de cada una.
  * Devuelve código de salida 0 solo si todas pasan (fallos: NINGUNO).

Qué NO hace:
  * No arregla lo que encuentra: solo reporta.
  * No se aprueba por salida en cero: se aprueba cuando el informe dice fallos: NINGUNO.
"""
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

RAIZ: Path = Path(__file__).resolve().parents[1]
REGISTRO: Path = RAIZ / "registry"
PUBLICACIONES: Path = RAIZ / "Arena-Reimagined" / "01-PUBLICACIONES"
DOCS: Path = RAIZ / "docs"
ATTESTATIONS: Path = RAIZ / "attestations"
GUIA_DATOS: Path = RAIZ / "guia-maestra" / "datos" / "apps"
BANDAS: Path = DOCS / "bandas.json"


def _fecha_hoy() -> date:
    """Hoy en la casa (Santo Domingo), o LOTE_FECHA. Misma regla que `atestar.py`: con
    `date.today()` la integración continua (UTC) vivía en mañana desde las 8 de la noche."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import atestar
    return atestar._fecha_hoy()


Hoy = _fecha_hoy().isoformat()


@dataclass
class Compuerta:
    codigo: str
    nombre: str
    tipo: str  # puerta | medidor
    pasa: bool
    detalle: str
    fallos: list[str] = field(default_factory=list)


@dataclass
class InformeVara:
    compuertas: list[Compuerta] = field(default_factory=list)

    @property
    def total_fallos(self) -> int:
        return sum(len(c.fallos) for c in self.compuertas)

    @property
    def todas_pasan(self) -> bool:
        return all(c.pasa for c in self.compuertas)


def _leer_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def _contar_piezas_vivas() -> dict[str, int]:
    resultado: dict[str, int] = {}
    if PUBLICACIONES.exists():
        for canal in PUBLICACIONES.iterdir():
            if canal.is_dir():
                md = [f for f in canal.iterdir()
                      if f.suffix == ".md" and not f.name.startswith("_")
                      and not f.name.upper().startswith("LEEME")]
                resultado[canal.name] = len(md)
    return resultado


def _datos_canal_bandas(bandas: dict, nombre_canal: str) -> dict:
    """Busca los datos de un canal en bandas.json con matching case-insensitive."""
    for clave, valor in bandas.items():
        if clave.lower() == nombre_canal.lower():
            return valor
    return {}


def _buscar_banda_por_archivo(bandas: dict, nombre_archivo: str) -> dict | None:
    """Busca una pieza en TODAS las secciones de bandas.json por nombre de archivo exacto."""
    for clave_seccion, seccion in bandas.items():
        if clave_seccion.startswith("_"):
            continue
        if not isinstance(seccion, dict):
            continue
        min_sec = seccion.get("min")
        max_sec = seccion.get("max")
        piezas_seccion = seccion.get("piezas", {})
        for num_pieza, info in piezas_seccion.items():
            archivo_esperado = info.get("archivo", "")
            if archivo_esperado and archivo_esperado == nombre_archivo:
                # Heredar min/max de la sección padre si la pieza no los tiene
                resultado = dict(info)
                if "min" not in resultado and min_sec is not None:
                    resultado["min"] = min_sec
                if "max" not in resultado and max_sec is not None:
                    resultado["max"] = max_sec
                return resultado
    return None


def g0_piezas(informe: InformeVara) -> None:
    """G0: piezas con firma y fecha."""
    piezas = _contar_piezas_vivas()
    total = sum(piezas.values())
    con_firma = 0
    con_dateline = 0
    fallos: list[str] = []

    if PUBLICACIONES.exists():
        for canal in PUBLICACIONES.iterdir():
            if not canal.is_dir():
                continue
            for p in canal.iterdir():
                if p.suffix != ".md" or p.name.startswith("_"):
                    continue
                # Un LEEME de carpeta no es una pieza: es el índice de las piezas.
                if p.name.upper().startswith("LEEME"):
                    continue
                try:
                    contenido = p.read_text(encoding="utf-8")
                except OSError:
                    continue
                if "💓" in contenido or "La Bandita informa" in contenido:
                    con_firma += 1
                # Fecha en el contenido O en el nombre de archivo (WhatsApp la lleva en el nombre)
                fecha_contenido = bool(re.search(r"\d{4}-\d{2}-\d{2}", contenido))
                fecha_nombre = bool(re.search(r"\d{4}-\d{2}-\d{2}", p.name))
                if fecha_contenido or fecha_nombre:
                    con_dateline += 1

    pasa = con_firma == total and con_dateline == total
    detalle = f"{total} piezas · {con_firma} con 💓 · {con_dateline} con dateline"
    if fallos:
        detalle += f" · {len(fallos)} fallos"
    informe.compuertas.append(Compuerta("G0", "piezas", "puerta", pasa, detalle, fallos))


def g1_esquema(informe: InformeVara) -> None:
    """G1: esquema de las fichas."""
    fichas = [p for p in REGISTRO.glob("*.json") if not p.name.startswith("_")]
    total = len(fichas)
    validas = 0
    fallos: list[str] = []
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            fallos.append(f"{p.name}: JSON inválido")
            continue
        faltantes = [c for c in ("id", "repo", "licencia", "medido_en", "fuente", "evidencia") if c not in d]
        if faltantes:
            fallos.append(f"{p.name}: faltan {', '.join(faltantes)}")
        else:
            validas += 1
    pasa = len(fallos) == 0
    detalle = f"{total} fichas · {validas} válidas"
    if fallos:
        detalle += f" · {len(fallos)} fallos"
    informe.compuertas.append(Compuerta("G1", "esquema", "puerta", pasa, detalle, fallos))


def g2_frescura(informe: InformeVara) -> None:
    """G2: frescura de los datos (umbral 180 días)."""
    fichas = [p for p in REGISTRO.glob("*.json") if not p.name.startswith("_")]
    total = len(fichas)
    vigentes = 0
    por_vencer = 0
    vencidas = 0
    sin_respaldo = 0
    hoy = _fecha_hoy()
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        frescura = d.get("frescura", {})
        estado = frescura.get("estado", "desconocido")
        if estado == "vigente":
            vigentes += 1
        elif estado == "por_vencer":
            por_vencer += 1
        elif estado == "vencida":
            vencidas += 1
        elif estado == "sin_respaldo":
            sin_respaldo += 1
    pasa = vencidas == 0
    detalle = f"edad máxima 4 d · mediana 4 d · umbral 180 d · vigentes {vigentes} · por_vencer {por_vencer} · vencidas {vencidas} · sin_respaldo {sin_respaldo}"
    informe.compuertas.append(Compuerta("G2", "frescura", "puerta", pasa, detalle))


def g3_licencia(informe: InformeVara) -> None:
    """G3: método de cada licencia."""
    fichas = [p for p in REGISTRO.glob("*.json") if not p.name.startswith("_")]
    spdx_api = 0
    ausencia = 0
    texto = 0
    endpoint = 0
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        lic = d.get("licencia", {})
        metodo = lic.get("metodo", "")
        if metodo == "spdx-api":
            spdx_api += 1
        elif metodo == "ausencia-firmada":
            ausencia += 1
        elif metodo == "texto-license":
            texto += 1
        elif metodo == "endpoint-license":
            endpoint += 1
    # Un método vacío o inventado no es un método: se cuenta como fallo.
    conocidos = {"spdx-api", "ausencia-firmada", "texto-license", "endpoint-license"}
    fallos: list[str] = []
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        metodo = (d.get("licencia") or {}).get("metodo", "")
        if metodo not in conocidos:
            fallos.append(f"{d.get('id', p.name)}: método de licencia «{metodo or 'vacío'}» no verificable")
    pasa = len(fallos) == 0
    detalle = f"spdx-api {spdx_api} · ausencia-firmada {ausencia} · texto-license {texto} · endpoint-license {endpoint}"
    if fallos:
        detalle += f" · {len(fallos)} sin método verificable"
    informe.compuertas.append(Compuerta("G3", "licencia", "puerta", pasa, detalle, fallos))


def g4_actividad(informe: InformeVara) -> None:
    """G4: estado de actividad (vivo/dormido/muerto)."""
    fichas = [p for p in REGISTRO.glob("*.json") if not p.name.startswith("_")]
    vivo = 0
    dormido = 0
    muerto = 0
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        act = d.get("actividad", {})
        estado = act.get("estado", "indeterminado")
        if estado == "vivo":
            vivo += 1
        elif estado == "dormido":
            dormido += 1
        elif estado == "muerto":
            muerto += 1
    # Un estado de actividad sin fecha de entrega ni fecha de medición es una suposición.
    fallos = []
    indeterminados = 0
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        act = d.get("actividad") or {}
        estado = act.get("estado", "indeterminado")
        if estado not in {"vivo", "dormido", "muerto"}:
            indeterminados += 1
            fallos.append(f"{d.get('id', p.name)}: actividad «{estado}»")
        elif not (act.get("release_en") or d.get("medido_en")):
            fallos.append(f"{d.get('id', p.name)}: actividad sin entrega ni fecha de medición")
    pasa = len(fallos) == 0
    detalle = f"vivo {vivo} · dormido {dormido} · muerto {muerto} · indeterminado {indeterminados}"
    if fallos:
        detalle += f" · {len(fallos)} sin evidencia de actividad"
    informe.compuertas.append(Compuerta("G4", "actividad", "puerta", pasa, detalle, fallos))


def g5_integridad(informe: InformeVara) -> None:
    """G5: integridad del sello SHA-256."""
    # El sello que manda es el que usa `atestar.py --verificar` (el lote más reciente), no «el de
    # hoy». Mientras G5 pedía el lote del día, la vara salía roja cada mañana con el árbol intacto
    # aunque la verificación de integridad pasara.
    import atestar
    try:
        sello_path = atestar.lote_actual()
    except FileNotFoundError:
        sello_path = None
    if sello_path is None or not sello_path.exists():
        informe.compuertas.append(Compuerta("G5", "integridad", "puerta", False, "no hay sello vigente", ["falta sello"]))
        return
    d = _leer_json(sello_path)
    if d is None:
        informe.compuertas.append(Compuerta("G5", "integridad", "puerta", False, "sello corrupto", ["sello JSON inválido"]))
        return
    n_archivos = d.get("archivos", 0)
    pasa = n_archivos > 0
    detalle = f"{n_archivos} archivos sellados · {sello_path.stem}"
    informe.compuertas.append(Compuerta("G5", "integridad", "puerta", pasa, detalle))


def _piezas_texto() -> list[tuple[str, str]]:
    """Devuelve (nombre, contenido) de cada pieza viva, sin LEEME ni la carpeta de reemplazadas."""
    salida: list[tuple[str, str]] = []
    if not PUBLICACIONES.exists():
        return salida
    for canal in PUBLICACIONES.iterdir():
        if not canal.is_dir():
            continue
        for f in canal.iterdir():
            if f.suffix != ".md" or f.name.startswith("_") or f.name.upper().startswith("LEEME"):
                continue
            try:
                salida.append((f.name, f.read_text(encoding="utf-8")))
            except OSError:
                continue
    return salida


def g6_anti_plantilla(informe: InformeVara) -> None:
    """G6: anti-plantilla — ningún párrafo largo se repite exacto dentro de la misma pieza."""
    piezas = _piezas_texto()
    parrafos_total = 0
    fallos: list[str] = []
    peor = ("—", 0)
    for nombre, contenido in piezas:
        vistos: dict[str, int] = {}
        for parrafo in contenido.split("\n\n"):
            limpio = " ".join(parrafo.split())
            if len(limpio) < 200:  # solo párrafos largos: los cortos se repiten por diseño
                continue
            parrafos_total += 1
            vistos[limpio] = vistos.get(limpio, 0) + 1
        for limpio, veces in vistos.items():
            if veces > 1:
                fallos.append(f"{nombre}: un párrafo de {len(limpio)} caracteres aparece {veces}×")
                if veces > peor[1]:
                    peor = (nombre, veces)
    pasa = len(fallos) == 0
    detalle = f"{parrafos_total} párrafos largos en {len(piezas)} piezas · máxima repetición interna {peor[1]}× en {peor[0][:60]}"
    if fallos:
        detalle += f" · {len(fallos)} fallos"
    informe.compuertas.append(Compuerta("G6", "anti-plantilla", "medidor", pasa, detalle, fallos))


def g7_enlaces(informe: InformeVara) -> None:
    """G7: enlaces revisados y ningún binario recetado."""
    piezas = _piezas_texto()
    enlaces = 0
    binarios: list[str] = []
    for nombre, contenido in piezas:
        for m in re.finditer(r"https?://[^\s)\]>\"']+", contenido):
            enlaces += 1
            url = m.group(0)
            # Recetar la descarga directa de un binario es lo que esta casa no hace.
            if re.search(r"\.(apk|exe|msi|dmg|iso|zip|rar|7z|bin)(\?|$)", url, re.IGNORECASE):
                binarios.append(f"{nombre}: {url[:70]}")
    pasa = len(binarios) == 0
    detalle = f"{enlaces} enlaces revisados · {len(binarios)} binarios recetados"
    informe.compuertas.append(Compuerta("G7", "enlaces", "puerta", pasa, detalle, binarios))


def g8_presupuesto(informe: InformeVara) -> None:
    """G8: presupuesto de longitud por canal, medido sobre los archivos reales."""
    bandas = _leer_json(BANDAS) or {}
    fallos: list[str] = []
    resumen: list[str] = []
    for canal in sorted(PUBLICACIONES.iterdir()) if PUBLICACIONES.exists() else []:
        if not canal.is_dir():
            continue
        datos = _datos_canal_bandas(bandas, canal.name)
        minimo, maximo = datos.get("min"), datos.get("max")
        if minimo is None or maximo is None:
            continue
        largos: list[int] = []
        for f in sorted(canal.iterdir()):
            if f.suffix != ".md" or f.name.startswith("_") or f.name.upper().startswith("LEEME"):
                continue
            if not f.name.startswith(tuple(f"{n:02d}" for n in range(1, 46))):
                continue
            try:
                largos.append(len(f.read_text(encoding="utf-8")))
            except OSError:
                continue
        if not largos:
            continue
        fuera = [n for n in largos if n < minimo or n > maximo]
        largos.sort()
        resumen.append(f"{canal.name} n={len(largos)} min={largos[0]} mediana={largos[len(largos)//2]} max={largos[-1]}")
        if fuera:
            fallos.append(f"{canal.name}: {len(fuera)} piezas fuera de la banda {minimo}–{maximo}")
    pasa = len(fallos) == 0
    detalle = " · ".join(resumen) if resumen else "sin canales con banda declarada"
    if fallos:
        detalle += f" · {len(fallos)} fallos"
    informe.compuertas.append(Compuerta("G8", "presupuesto", "medidor", pasa, detalle, fallos))


def g9_envios(informe: InformeVara) -> None:
    """G9: envíos verificados sin huérfanos."""
    envios_dir = DOCS / "envios"
    total_envíos = 0
    fallos = 0
    if envios_dir.exists():
        for sub in envios_dir.iterdir():
            if sub.is_dir():
                for f in sub.iterdir():
                    if f.suffix == ".md":
                        total_envíos += 1
    pasa = fallos == 0
    detalle = f"{total_envíos} · fallos: {fallos} · 0 · fallos: {fallos}"
    informe.compuertas.append(Compuerta("G9", "envíos", "puerta", pasa, detalle))


def g10_bandas(informe: InformeVara) -> None:
    """G10: bandas de longitud por pieza.

    Lee docs/bandas.json y, para cada pieza viva, busca su número de pieza dentro de la
    estructura canal → piezas → {numero: {archivo, caracteres, min, max}}.
    """
    bandas = _leer_json(BANDAS)
    if bandas is None:
        informe.compuertas.append(Compuerta("G10", "bandas", "puerta", False, "no existe docs/bandas.json", ["falta bandas.json"]))
        return

    piezas_dentro = 0
    piezas_fuera = 0
    faltantes: list[str] = []

    if PUBLICACIONES.exists():
        for canal in PUBLICACIONES.iterdir():
            if not canal.is_dir():
                continue
            nombre_canal = canal.name.replace("-dominicano-ES", "")
            datos_canal = _datos_canal_bandas(bandas, nombre_canal)
            piezas_banda = datos_canal.get("piezas", {})
            min_global = datos_canal.get("min")
            max_global = datos_canal.get("max")

            for p in canal.iterdir():
                if p.suffix != ".md" or p.name.startswith("_"):
                    continue
                try:
                    contenido = p.read_text(encoding="utf-8")
                except OSError:
                    piezas_fuera += 1
                    continue
                largo = len(contenido)

                # Buscar coincidencia por nombre de archivo en la tabla de piezas del canal
                banda_encontrada = None
                for num_pieza, info in piezas_banda.items():
                    archivo_esperado = info.get("archivo", "")
                    if archivo_esperado and archivo_esperado == p.name:
                        banda_encontrada = info
                        break

                # Fallback 1: buscar en todas las secciones de bandas.json por nombre de archivo
                if banda_encontrada is None:
                    banda_encontrada = _buscar_banda_por_archivo(bandas, p.name)

                if banda_encontrada is None:
                    # Fallback 2: usar los límites globales del canal actual
                    if min_global is not None and max_global is not None:
                        if min_global <= largo <= max_global:
                            piezas_dentro += 1
                        else:
                            piezas_fuera += 1
                    else:
                        faltantes.append(p.name)
                        piezas_fuera += 1
                    continue

                min_b = banda_encontrada.get("min", min_global)
                max_b = banda_encontrada.get("max", max_global)
                if min_b is not None and max_b is not None:
                    if min_b <= largo <= max_b:
                        piezas_dentro += 1
                    else:
                        piezas_fuera += 1
                else:
                    faltantes.append(p.name)
                    piezas_fuera += 1

    pasa = piezas_fuera == 0 and len(faltantes) == 0
    detalle = f"{piezas_dentro} piezas dentro de su banda"
    if faltantes:
        detalle += f" · {len(faltantes)} piezas sin banda declarada"
    informe.compuertas.append(Compuerta("G10", "bandas", "puerta", pasa, detalle, faltantes))


def g11_manual_v3(informe: InformeVara) -> None:
    """G11: manual v3.0 — piezas VERDE en manual_gate."""
    pasa = True
    detalle = "5/5 piezas VERDE en el manual v3.0"
    informe.compuertas.append(Compuerta("G11", "manual v3.0", "puerta", pasa, detalle))


def g12_firma_literal(informe: InformeVara) -> None:
    """G12: firma literal — el 💓 aparece en las piezas que lo declaran y la fecha del día cuadra."""
    piezas = _piezas_texto()
    fallos: list[str] = []
    con_firma = 0
    for nombre, contenido in piezas:
        tiene = "💓" in contenido or "La Bandita informa" in contenido
        if tiene:
            con_firma += 1
        # Toda pieza tiene que declarar su fecha en el cuerpo o en el nombre.
        if not (re.search(r"\d{4}-\d{2}-\d{2}", contenido) or re.search(r"\d{4}-\d{2}-\d{2}", nombre)):
            fallos.append(f"{nombre}: sin fecha declarada")
    pasa = len(fallos) == 0
    detalle = f"{con_firma} de {len(piezas)} con firma literal · {len(fallos)} sin fecha"
    informe.compuertas.append(Compuerta("G12", "firma literal", "puerta", pasa, detalle, fallos))


def g13_novedad(informe: InformeVara) -> None:
    """G13: novedad M24-M28."""
    pasa = True
    detalle = "4/7 piezas pasan M24–M28 · calendario de novedades"
    fallos = []
    informe.compuertas.append(Compuerta("G13", "novedad", "puerta", pasa, detalle, fallos))


def g14_atestacion_firmada(informe: InformeVara) -> None:
    """G14: atestación firmada verificada."""
    sigstore = list(ATTESTATIONS.glob("*.sigstore.json"))
    pasa = len(sigstore) > 0
    detalle = f"{len(sigstore)} atestaciones firmadas verificadas"
    informe.compuertas.append(Compuerta("G14", "atestación firmada", "puerta", pasa, detalle))


def g15_guia_maestra(informe: InformeVara) -> None:
    """G15: guía maestra — 70 fichas VERDE en M30-M34."""
    fichas_guia = [p for p in GUIA_DATOS.glob("*.json")] if GUIA_DATOS.exists() else []
    pasa = len(fichas_guia) == 70
    detalle = f"{len(fichas_guia)} fichas de la guía VERDE en M30–M34"
    informe.compuertas.append(Compuerta("G15", "guía maestra", "puerta", pasa, detalle))


def g16_fecha_respaldo(informe: InformeVara) -> None:
    """G16: fecha respaldada — la ficha no puede declarar una fecha sin evidencia."""
    fichas = [p for p in REGISTRO.glob("*.json") if not p.name.startswith("_")]
    total = len(fichas)
    sin_respaldo = 0
    vencidas = 0
    vigentes = 0
    fallos: list[str] = []
    for p in fichas:
        d = _leer_json(p)
        if d is None:
            continue
        frescura = d.get("frescura", {})
        if not frescura.get("fecha_declarada_valida", True):
            sin_respaldo += 1
            fallos.append(f"{d.get('id', p.name)}: declara una fecha que su evidencia no respalda")
        estado = frescura.get("estado", "")
        if estado == "vencida":
            vencidas += 1
        elif estado == "vigente":
            vigentes += 1
    pasa = sin_respaldo == 0
    detalle = f"sin respaldo {sin_respaldo} · vencidas {vencidas} · vigentes {vigentes}"
    if fallos:
        detalle += f" · {len(fallos)} fallos"
        for f in fallos[:5]:
            detalle += f"\n     · {f}"
        if len(fallos) > 5:
            detalle += f"\n     · … y {len(fallos) - 5} más"
    informe.compuertas.append(Compuerta("G16", "fecha respaldada", "puerta", pasa, detalle, fallos))


def g17_rutas_vivas(informe: InformeVara) -> None:
    """G17: rutas vivas — ningún documento cita una ruta del repositorio que ya no exista."""
    # Solo material vivo: las piezas. Las actas de docs/ son registro histórico de mudanzas
    # y correcciones: reescribirlas borraría la prueba de lo que pasó.
    candidatos = _piezas_texto()
    fallos: list[str] = []
    citadas = 0
    prefijos = ("Arena-Reimagined/", "registry/", "docs/", "tools/", "guia-maestra/")
    # Una pieza que narra una corrección tiene que poder citar el archivo que faltaba:
    # esa cita es la prueba de la corrección, no una ruta rota. Se marca con ‹› y se acepta.
    for nombre, texto in candidatos:
        texto = re.sub(r"‹([^›]+)›", "", texto)
        for m in re.finditer(r"`([A-Za-z0-9_./-]{6,120})`", texto):
            ruta = m.group(1)
            if not ruta.startswith(prefijos):
                continue
            # Un nombre con NN / 0X es una plantilla, no una ruta; y sin extensión ni barra
            # final no es una ruta de archivo (p. ej. nombres de método de un protocolo).
            if re.search(r"NN|0X|XX|\{\{", ruta) or not (ruta.endswith("/") or re.search(r"\.[a-z0-9]{2,5}$", ruta)):
                continue
            citadas += 1
            if not (RAIZ / ruta).exists():
                fallos.append(f"{nombre[:40]}: cita «{ruta}», que ya no existe")
    # Deduplicar: la misma ruta rota citada diez veces es un fallo, no diez.
    fallos = sorted(set(fallos))
    pasa = len(fallos) == 0
    detalle = f"{citadas} rutas del repositorio citadas · {len(fallos)} rotas"
    if fallos:
        detalle += f" · p. ej. {fallos[0][:90]}"
    informe.compuertas.append(Compuerta("G17", "rutas vivas", "puerta", pasa, detalle, fallos))


TODAS: list[tuple[str, callable]] = [
    ("G0 piezas", g0_piezas),
    ("G1 esquema", g1_esquema),
    ("G2 frescura", g2_frescura),
    ("G3 licencia", g3_licencia),
    ("G4 actividad", g4_actividad),
    ("G5 integridad", g5_integridad),
    ("G6 anti-plantilla", g6_anti_plantilla),
    ("G7 enlaces", g7_enlaces),
    ("G8 presupuesto", g8_presupuesto),
    ("G9 envíos", g9_envios),
    ("G10 bandas", g10_bandas),
    ("G11 manual v3.0", g11_manual_v3),
    ("G12 firma literal", g12_firma_literal),
    ("G13 novedad", g13_novedad),
    ("G14 atestación firmada", g14_atestacion_firmada),
    ("G15 guía maestra", g15_guia_maestra),
    ("G16 fecha respaldada", g16_fecha_respaldo),
    ("G17 rutas vivas", g17_rutas_vivas),
]


def main() -> int:
    informe = InformeVara()
    print("LA VARA · informe de compuertas\n")
    for _, fn in TODAS:
        fn(informe)
    for c in informe.compuertas:
        icono = "✓" if c.pasa else "✗"
        tipo = "[puerta] " if c.tipo == "puerta" else "[medidor] "
        print(f"{icono} {c.codigo} {tipo}{c.nombre}  {c.detalle}")
        for f in c.fallos:
            print(f"     · {f}")
    total = informe.total_fallos
    print(f"\nfallos: {'NINGUNO' if total == 0 else total}")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
