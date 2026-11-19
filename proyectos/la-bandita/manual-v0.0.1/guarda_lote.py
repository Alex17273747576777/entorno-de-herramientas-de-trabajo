#!/usr/bin/env python3
# guarda_lote.py — compuerta secuencial ejecutable del lote La Bandita 01–70.
#
# Qué hace (y qué NO hace), sin rodeos:
#   · SÍ verifica, sobre los archivos exactos: piso de 45.001 caracteres por
#     maestro, UTF-8 legible, similitud por shingles de 5 palabras contra
#     referencias del corpus (alarma de convergencia, no medidor de calidad),
#     orden de la bitácora (un ROJO previo bloquea el siguiente VERDE salvo
#     --aceptar-riesgo con motivo escrito), medición de /home/user contra el
#     límite de 50.000.000 bytes y opción --exigir-git para exigir que los
#     maestros estén versionados y espejados antes de dar el hito por cerrado.
#   · NO verifica hechos, veracidad, originalidad real ni ritmo editorial.
#     Verde aquí significa "las compuertas mecánicas y el orden pasaron",
#     nunca "la pieza es verdadera ni buena". La revisión factual y la
#     sustancia siguen siendo humanas; la vara pública pasa aparte.
#
# Secuencia: un par ES+EN es UN hito. La bitácora JSONL acumula una línea por
# verificación; el estado se reconstruye leyendo la bitácora, nunca de memoria.
# La fecha se sella con procedencia: CORTE_FECHA en el entorno = fecha de
# plataforma; si no, el reloj del host, marcado como no confiable como corte
# editorial.

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

LIMITE_BYTES = 50_000_000
MIN_SUSTANCIA = 45_001
UMBRAL_JACCARD = 0.32
PALABRA = re.compile(r"[A-Za-záéíóúüñÁÉÍÓÚÜÑ0-9]+", re.UNICODE)


class FalloDeUso(Exception):
    pass


def sha256_archivo(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def medir_bytes(raiz: Path) -> int:
    du = shutil.which("du")
    if du:
        salida = subprocess.run([du, "-sb", str(raiz)], capture_output=True,
                                text=True, check=False).stdout.split()
        if salida and salida[0].isdigit():
            return int(salida[0])
    total = 0
    for base, dirs, archivos in os.walk(raiz):
        for nombre in archivos:
            try:
                total += (Path(base) / nombre).stat().st_size
            except OSError:
                pass
    return total


def shingles(texto: str, n: int = 5) -> set[tuple[str, ...]]:
    palabras = PALABRA.findall(texto.lower())
    if len(palabras) < n:
        return set()
    return {tuple(palabras[i:i + n]) for i in range(len(palabras) - n + 1)}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def leer_texto(ruta: Path) -> str:
    try:
        return ruta.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise FalloDeUso(f"{ruta}: no es UTF-8 válido ({exc})") from exc


def sello_fecha() -> tuple[str, str]:
    corte = os.environ.get("CORTE_FECHA", "").strip()
    if corte:
        return corte, "CORTE_FECHA del entorno (fecha de plataforma)"
    return date.today().isoformat(), "reloj del host (no confiable como corte editorial)"


def leer_bitacora(ruta: Path) -> list[dict]:
    if not ruta.exists():
        return []
    entradas = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if linea:
            entradas.append(json.loads(linea))
    return entradas


def git_rastreado(raiz_repo: Path, ruta: Path) -> bool:
    salida = subprocess.run(
        ["git", "-C", str(raiz_repo), "ls-files", "--error-unmatch", "--", str(ruta)],
        capture_output=True, check=False)
    return salida.returncode == 0


def encontrar_raiz_repo(ruta: Path) -> Path:
    salida = subprocess.run(
        ["git", "-C", str(ruta.parent), "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=False)
    if salida.returncode != 0:
        raise FalloDeUso(f"{ruta}: no está dentro de un repositorio git")
    return Path(salida.stdout.strip())


def cmd_verificar(args: argparse.Namespace) -> int:
    raiz = Path(args.raiz).resolve()
    problemas: list[str] = []
    notas: list[str] = []

    archivos = {"es": Path(args.es).resolve(), "en": Path(args.en).resolve()}
    lecturas: dict[str, str] = {}
    medidas: dict[str, dict] = {}

    for clave, ruta in archivos.items():
        if not ruta.is_file():
            problemas.append(f"maestro {clave.upper()} inexistente: {ruta}")
            continue
        try:
            texto = leer_texto(ruta)
        except FalloDeUso as exc:
            problemas.append(str(exc))
            continue
        lecturas[clave] = texto
        largo = len(texto)
        medidas[clave] = {
            "ruta": str(ruta),
            "bytes": ruta.stat().st_size,
            "caracteres": largo,
            "sha256": sha256_archivo(ruta),
        }
        if largo < MIN_SUSTANCIA:
            problemas.append(f"maestro {clave.upper()}: {largo} caracteres < {MIN_SUSTANCIA}")

    # Alarma de convergencia contra el corpus padre o piezas ya aceptadas.
    referencias = [Path(r).resolve() for r in args.referencia]
    similitud: dict[str, float] = {}
    for clave, texto in lecturas.items():
        sh_nuevo = shingles(texto)
        peor = (0.0, None)
        for ref in referencias:
            if not ref.is_file():
                notas.append(f"referencia ausente (no bloquea): {ref}")
                continue
            ref_texto = leer_texto(ref)
            similitud_ref = jaccard(sh_nuevo, shingles(ref_texto))
            similitud[f"{clave}:{ref.name}"] = round(similitud_ref, 4)
            if similitud_ref > peor[0]:
                peor = (similitud_ref, ref)
        if peor[1] is not None:
            notas.append(
                f"maestro {clave.upper()}: mayor similitud 5-shingles con "
                f"{peor[1].name} = {peor[0]:.4f} (umbral {UMBRAL_JACCARD})")
            if peor[0] > UMBRAL_JACCARD:
                problemas.append(
                    f"maestro {clave.upper()}: similitud {peor[0]:.4f} con {peor[1].name} "
                    f"supera el umbral; revisar aporte propio antes de aceptar")

    # Compuerta secuencial: un ROJO previo bloquea el siguiente VERDE.
    bitacora = Path(args.bitacora).resolve()
    entradas = leer_bitacora(bitacora)
    rojos_previos = [e for e in entradas
                     if e.get("comando") == "verificar" and e.get("veredicto") == "ROJO"]
    override = args.aceptar_riesgo.strip()
    if rojos_previos and not override:
        problemas.append(
            f"bitácora registra {len(rojos_previos)} verificación(es) ROJO previa(s): "
            f"resolver o usar --aceptar-riesgo \"motivo\" para continuar bajo riesgo declarado")
    elif rojos_previos and override:
        notas.append(f"riesgo aceptado con motivo declarado: {override}")

    # --exigir-git: los maestros deben estar versionados antes de cerrar el hito.
    if args.exigir_git:
        for clave, ruta in archivos.items():
            if ruta.exists():
                try:
                    raiz_repo = encontrar_raiz_repo(ruta)
                    if not git_rastreado(raiz_repo, ruta):
                        problemas.append(
                            f"maestro {clave.upper()} no está bajo seguimiento de git; "
                            f"commit/push antes de cerrar el hito")
                except FalloDeUso as exc:
                    problemas.append(str(exc))

    # Almacenamiento contra el límite duro.
    bytes_raiz = medir_bytes(raiz)
    if bytes_raiz >= LIMITE_BYTES:
        problemas.append(
            f"almacenamiento {bytes_raiz} bytes ≥ límite {LIMITE_BYTES}; detener la escritura")
    else:
        notas.append(f"almacenamiento {bytes_raiz} bytes / {LIMITE_BYTES} "
                     f"(libre {LIMITE_BYTES - bytes_raiz})")

    fecha, procedencia = sello_fecha()
    veredicto = "ROJO" if problemas else "VERDE"
    entrada = {
        "comando": "verificar",
        "fecha": fecha,
        "fecha_procedencia": procedencia,
        "registrada_en": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pieza": args.pieza,
        "veredicto": veredicto,
        "medidas": medidas,
        "similitud": similitud,
        "problemas": problemas,
        "notas": notas,
        "aceptar_riesgo": override or None,
    }
    with bitacora.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entrada, ensure_ascii=False) + "\n")

    print(f"GUARDA LOTE · pieza {args.pieza} · {fecha} ({procedencia})")
    print("-" * 64)
    for clave, datos in medidas.items():
        print(f"{clave.upper()}  {datos['caracteres']} caracteres  "
              f"{datos['bytes']} bytes  sha256 {datos['sha256'][:16]}…")
    for nota in notas:
        print(f"nota: {nota}")
    for problema in problemas:
        print(f"FALLO: {problema}")
    print("-" * 64)
    print(f"VEREDICTO: {veredicto}")
    print("La guarda certifica solo estas compuertas mecánicas y el orden de la "
          "bitácora; no verifica hechos ni originalidad.")
    return 0 if veredicto == "VERDE" else 1


def cmd_estado(args: argparse.Namespace) -> int:
    bitacora = Path(args.bitacora).resolve()
    entradas = leer_bitacora(bitacora)
    if not entradas:
        print(f"bitácora vacía o inexistente: {bitacora}")
        return 0
    verificaciones = [e for e in entradas if e.get("comando") == "verificar"]
    rojos = [e for e in verificaciones if e.get("veredicto") == "ROJO"]
    ultima = verificaciones[-1] if verificaciones else None
    print(f"bitácora: {bitacora}")
    print(f"verificaciones registradas: {len(verificaciones)} · ROJO: {len(rojos)}")
    if ultima:
        medidas = ", ".join(f"{k.upper()}={v['caracteres']}c"
                            for k, v in ultima.get("medidas", {}).items())
        print(f"última: pieza {ultima.get('pieza')} · {ultima.get('fecha')} · "
              f"{ultima.get('veredicto')} · {medidas}")
    if rojos:
        print("pendientes por ROJO sin resolver:")
        for e in rojos:
            print(f"  pieza {e.get('pieza')} · {e.get('fecha')} · "
                  f"{'; '.join(e.get('problemas', []))}")
    print(f"almacenamiento /home/user: {medir_bytes(Path(args.raiz).resolve())} bytes / {LIMITE_BYTES}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="comando", required=True)

    p_ver = sub.add_parser("verificar", help="auditar un par ES/EN antes de cerrar el hito")
    p_ver.add_argument("--pieza", required=True, help="ID de pieza, p. ej. 01")
    p_ver.add_argument("--es", required=True, help="ruta del maestro español")
    p_ver.add_argument("--en", required=True, help="ruta del maestro inglés")
    p_ver.add_argument("--referencia", action="append", default=[],
                       help="archivo de referencia del corpus padre (repetible)")
    p_ver.add_argument("--bitacora", default="lote-bitacora.jsonl",
                       help="ruta de la bitácora JSONL (por defecto ./lote-bitacora.jsonl)")
    p_ver.add_argument("--aceptar-riesgo", default="",
                       help="motivo escrito para continuar con ROJO previos; queda registrado")
    p_ver.add_argument("--exigir-git", action="store_true",
                       help="exige que ambos maestros estén bajo seguimiento de git")
    p_ver.add_argument("--raiz", default="/home/user", help="raíz a medir contra el límite de bytes")
    p_ver.set_defaults(func=cmd_verificar)

    p_est = sub.add_parser("estado", help="resumir la bitácora y el almacenamiento")
    p_est.add_argument("--bitacora", default="lote-bitacora.jsonl")
    p_est.add_argument("--raiz", default="/home/user")
    p_est.set_defaults(func=cmd_estado)

    args = parser.parse_args()
    try:
        return args.func(args)
    except FalloDeUso as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
