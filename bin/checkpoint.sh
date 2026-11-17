#!/usr/bin/env bash
# checkpoint.sh — contraparche de FALLA-001 (turno caído por tiempo).
# Uso:
#   bash checkpoint.sh escribir "<tarea>" "<hecho>" "<siguiente paso>"
#   bash checkpoint.sh leer
# El checkpoint vive en edt/docs/CHECKPOINT-ACTUAL.md (persistente).
# Se invoca con `bash` a propósito: los reinicios quitan el bit de ejecución.
set -eu
DOC="$(cd "$(dirname "$0")/.." && pwd)/docs/CHECKPOINT-ACTUAL.md"
cmd="${1:-leer}"
case "$cmd" in
  escribir)
    tarea="${2:?falta tarea}"; hecho="${3:?falta hecho}"; sig="${4:?falta siguiente paso}"
    ts="$(date -u +%F' '%H:%M'Z')"
    {
      echo "# CHECKPOINT ACTUAL"
      echo
      echo "- Tarea: $tarea"
      echo "- Hecho: $hecho"
      echo "- Siguiente paso: $sig"
      echo "- Escrito: $ts"
      echo
      echo "## Historial (lo más nuevo arriba)"
      if [[ -f "$DOC" ]]; then
        sed -n '/^## Historial/,$p' "$DOC" | tail -n +3 | head -40 || true
      fi
      echo "- $ts — $tarea — hecho: $hecho"
    } > "$DOC.tmp"
    mv "$DOC.tmp" "$DOC"
    echo "CHECKPOINT_OK $ts"
    ;;
  leer)
    if [[ -f "$DOC" ]]; then cat "$DOC"; else echo "SIN_CHECKPOINT (primera vez: empieza y escribe uno)"; fi
    ;;
  *) echo "uso: escribir|leer" >&2; exit 2 ;;
esac
