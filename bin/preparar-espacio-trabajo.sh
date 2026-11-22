#!/usr/bin/env bash
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOLO_VERIFICAR=0 ESTRICTO_ORIGEN=0 CONFIGURAR_GIT=0
DIR_REPOS="" PERFIL="completo" REPORTE_JSON=""
uso() { echo "Uso: $0 [--solo-verificar] [--sincronizar DIR] [--estricto-origen] [--perfil base|archivo|web|android|completo] [--configurar-git] [--reporte-json ARCHIVO]"; }
while [[ $# -gt 0 ]]; do
  case "$1" in
    --solo-verificar) SOLO_VERIFICAR=1; shift ;;
    --estricto-origen) ESTRICTO_ORIGEN=1; shift ;;
    --configurar-git) CONFIGURAR_GIT=1; shift ;;
    --sincronizar) [[ $# -ge 2 && -n "$2" ]] || { echo "Error: --sincronizar requiere DIR" >&2; exit 2; }; DIR_REPOS="$2"; shift 2 ;;
    --perfil) [[ $# -ge 2 ]] || { echo "Error: --perfil requiere un valor" >&2; exit 2; }; PERFIL="$2"; shift 2 ;;
    --reporte-json) [[ $# -ge 2 && -n "$2" ]] || { echo "Error: --reporte-json requiere ARCHIVO" >&2; exit 2; }; REPORTE_JSON="$2"; shift 2 ;;
    -h|--help) uso; exit 0 ;;
    *) echo "Argumento no reconocido: $1" >&2; uso >&2; exit 2 ;;
  esac
done
case "$PERFIL" in base|archivo|web|android|completo) ;; *) echo "Perfil inválido: $PERFIL" >&2; exit 2 ;; esac

FALTANTES=() DISPONIBLES=()
chequear() { local nombre="$1" obligatorio="${2:-no}"; if command -v "$nombre" >/dev/null 2>&1; then DISPONIBLES+=("$nombre"); echo "  ok  $nombre disponible"; else echo "  opc $nombre no instalado"; if [[ "$obligatorio" == si ]]; then FALTANTES+=("$nombre"); fi; fi; }
echo "== 1. Perfil $PERFIL: herramientas =="
chequear python3 si; chequear git si
python3 - <<'PY'
import sys
if sys.version_info < (3, 11): raise SystemExit(f"Se requiere Python >= 3.11 (actual: {sys.version.split()[0]})")
print(f"  ok  Python {sys.version.split()[0]}")
PY
for opt in make gcc g++ node curl ruff shellcheck java; do chequear "$opt"; done
if [[ "$CONFIGURAR_GIT" -eq 1 ]]; then
  git config --global user.name "Alex17273747576777"
  git config --global user.email "Alex17273747576777@users.noreply.github.com"
  echo "  ok  identidad Git global configurada"
fi
if [[ "$SOLO_VERIFICAR" -eq 0 ]]; then
  for sec_dir in "$HOME/.cerox-keys"; do
    if [[ -d "$sec_dir" ]]; then chmod 700 "$sec_dir" || true; find "$sec_dir" -type f -exec chmod 600 {} + || true; echo "  ok  permisos 700/600 asegurados en $sec_dir"; fi
  done
  if [[ -f "$HOME/.gh-credential" ]]; then chmod 600 "$HOME/.gh-credential" || true; echo "  ok  permisos 600 asegurados en ~/.gh-credential"; fi
fi
if [[ ${#FALTANTES[@]} -gt 0 ]]; then printf 'Faltan herramientas requeridas: %s\n' "${FALTANTES[*]}" >&2; exit 1; fi

echo "== 2. Pruebas y copias canónicas =="
python3 "$RAIZ/tests/pruebas.py" >/dev/null
echo "  ok  tests/pruebas.py"
if [[ "$ESTRICTO_ORIGEN" -eq 1 ]]; then (cd "$RAIZ" && bash ./proyectos/comprobar-copias.sh --estricto-origen); else (cd "$RAIZ" && bash ./proyectos/comprobar-copias.sh); fi

if [[ -n "$DIR_REPOS" ]]; then
  echo "== 3. Sincronizando perfil $PERFIL en $DIR_REPOS =="
  mkdir -p "$DIR_REPOS"
  python3 - "$RAIZ/entorno/repositorios.json" "$PERFIL" <<'PY' > "${TMPDIR:-/tmp}/preparar-repos.$$"
import json,sys
cfg=json.load(open(sys.argv[1],encoding='utf-8'))
for r in cfg['repositorios']:
    if sys.argv[2] in r['perfil']: print(r['nombre']+'\t'+r['url'])
PY
  while IFS=$'\t' read -r repo url; do
    [[ -n "$repo" ]] || continue
    dest="$DIR_REPOS/$repo"
    if [[ -d "$dest/.git" ]]; then git -C "$dest" fetch -q origin; git -C "$dest" pull --ff-only -q; echo "  ok  actualizado $repo ($(git -C "$dest" rev-parse --short HEAD))";
    else git clone --depth 5 -q "$url" "$dest"; echo "  ok  clonado $repo ($(git -C "$dest" rev-parse --short HEAD))"; fi
  done < "${TMPDIR:-/tmp}/preparar-repos.$$"
  rm -f "${TMPDIR:-/tmp}/preparar-repos.$$"
fi
if [[ -n "$REPORTE_JSON" ]]; then
  python3 - "$REPORTE_JSON" "$PERFIL" "${DISPONIBLES[*]}" <<'PY'
import json,sys,datetime,pathlib
p=pathlib.Path(sys.argv[1]); p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps({'perfil':sys.argv[2],'generado_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'herramientas_disponibles':sys.argv[3].split()},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
PY
  echo "  ok  reporte JSON: $REPORTE_JSON"
fi
echo "ESPACIO_DE_TRABAJO_LISTO"
