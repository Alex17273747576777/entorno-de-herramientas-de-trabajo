#!/usr/bin/env bash
set -euo pipefail

# preparar-espacio-trabajo.sh — Prepara y valida la configuracion del espacio de trabajo
# Uso:
#   bash bin/preparar-espacio-trabajo.sh [--solo-verificar] [--sincronizar DIR] [--estricto-origen]

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOLO_VERIFICAR=0
ESTRICTO_ORIGEN=0
DIR_REPOS=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --solo-verificar)
      SOLO_VERIFICAR=1
      shift
      ;;
    --estricto-origen)
      ESTRICTO_ORIGEN=1
      shift
      ;;
    --sincronizar)
      DIR_REPOS="${2:-}"
      if [[ -z "$DIR_REPOS" ]]; then
        echo "Error: --sincronizar requiere un directorio destino" >&2
        exit 2
      fi
      shift 2
      ;;
    -h|--help)
      echo "Uso: bash bin/preparar-espacio-trabajo.sh [--solo-verificar] [--sincronizar DIR] [--estricto-origen]"
      exit 0
      ;;
    *)
      echo "Argumento no reconocido: $1" >&2
      exit 2
      ;;
  esac
done

echo "== 1. Verificando herramientas base del espacio de trabajo =="
command -v python3 >/dev/null || { echo "FALTA python3" >&2; exit 1; }
command -v git >/dev/null || { echo "FALTA git" >&2; exit 1; }

python3 - << 'PY'
import sys
if sys.version_info < (3, 11):
    raise SystemExit(f"Se requiere Python >= 3.11 (actual: {sys.version.split()[0]})")
print(f"  ok  python3 {sys.version.split()[0]}")
PY
echo "  ok  $(git --version)"

for opt in make gcc g++ node curl; do
  if command -v "$opt" >/dev/null 2>&1; then
    echo "  ok  $opt disponible"
  else
    echo "  opc $opt no instalado (opcional)"
  fi
done

echo "== 2. Asegurando permisos seguros sobre credenciales locales (si existen) =="
if [[ "$SOLO_VERIFICAR" -eq 0 ]]; then
  for sec_dir in "$HOME/.cerox-keys"; do
    if [[ -d "$sec_dir" ]]; then
      chmod 700 "$sec_dir" || true
      find "$sec_dir" -type f -exec chmod 600 {} + || true
      echo "  ok  permisos 700/600 asegurados en $sec_dir"
    fi
  done
  if [[ -f "$HOME/.gh-credential" ]]; then
    chmod 600 "$HOME/.gh-credential" || true
    echo "  ok  permisos 600 asegurados en ~/.gh-credential"
  fi
fi

echo "== 3. Verificando pruebas y copias canonicas del entorno =="
python3 "$RAIZ/tests/pruebas.py" >/dev/null
echo "  ok  tests/pruebas.py (11/11)"

if [[ "$ESTRICTO_ORIGEN" -eq 1 ]]; then
  (cd "$RAIZ" && bash ./proyectos/comprobar-copias.sh --estricto-origen)
else
  (cd "$RAIZ" && bash ./proyectos/comprobar-copias.sh)
fi

if [[ -n "$DIR_REPOS" ]]; then
  echo "== 4. Sincronizando repositorios propios en $DIR_REPOS =="
  mkdir -p "$DIR_REPOS"
  for repo in ruta-programacion-sistemas la-bandita-archivo normas-de-diseno; do
    dest="$DIR_REPOS/$repo"
    url="https://github.com/Alex17273747576777/$repo.git"
    if [[ -d "$dest/.git" ]]; then
      git -C "$dest" fetch -q origin
      git -C "$dest" pull --ff-only -q
      echo "  ok  actualizado $repo ($(git -C "$dest" rev-parse --short HEAD))"
    else
      git clone --depth 5 -q "$url" "$dest"
      echo "  ok  clonado $repo ($(git -C "$dest" rev-parse --short HEAD))"
    fi
  done
fi

echo "ESPACIO_DE_TRABAJO_LISTO"
