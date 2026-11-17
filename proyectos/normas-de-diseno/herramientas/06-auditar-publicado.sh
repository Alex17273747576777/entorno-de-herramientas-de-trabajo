#!/usr/bin/env bash
#
# 06-auditar-publicado.sh · auditar el diseño de una app YA PUBLICADA
#
# Por qué existe (incidencia #1): los procedimientos 01-05 cubren el ciclo de ELEGIR una app,
# desmontarla, imitar su estructura y cerrar el tramo. Falta el que se usa DESPUÉS de publicar:
# volver a una app seis meses más tarde y comprobar que sigue cumpliendo la ley de diseño, que nadie
# reintrodujo un violeta de plantilla ni un degradado decorativo.
#
# La diferencia con 06-auditar-reglas.sh: aquél audita si las REGLAS están declaradas y cerradas en
# un repo; éste audita el DISEÑO medido sobre el código. Los dos se llaman 06 porque son dos
# auditorías distintas que se hacen en el mismo momento (al publicar y al volver), no porque uno
# sustituya al otro.
#
# Uso:
#   ./06-auditar-publicado.sh RUTA_DEL_REPO
#   ./06-auditar-publicado.sh RUTA_DEL_REPO --estricto      # los avisos también cortan
#   ./06-auditar-publicado.sh RUTA_DEL_REPO --json          # salida máquina
#   ./06-auditar-publicado.sh RUTA_DEL_REPO --sin-informe   # no escribe el informe fechado
#
# Salida: 0 = cumple · 1 = hay incumplimientos · 2 = no se pudo auditar.
#
# Lo que hace además de medir: escribe `informes/AAAA-MM-DD-<repo>-<sha7>.md` con el commit exacto
# que se auditó. Sin eso, un informe de diseño no dice nada seis meses después: no se puede saber si
# lo que se midió es lo que hay ahora. La fecha y la hora se toman de `date -u`, no de una estimación.
#
# Lo que NO hace, dicho por adelantado: no mira la pantalla. Ni el tacto, ni si un elemento pequeño
# se ve de verdad, ni si una fila se corta en un ancho concreto. Eso exige un dispositivo y está
# declarado al final de cada informe, no escondido.

set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUDITOR="$AQUI/auditar_diseno_generico.py"
RAIZ_NORMAS="$(cd "$AQUI/.." && pwd)"

if [ "$#" -lt 1 ]; then
  echo "uso: $(basename "$0") RUTA_DEL_REPO [--estricto] [--json] [--sin-informe]" >&2
  exit 2
fi

REPO="$1"; shift || true
ESTRICTO="" ; JSON="" ; INFORME=1
for a in "$@"; do
  case "$a" in
    --estricto)    ESTRICTO="--estricto" ;;
    --json)        JSON="--json" ;;
    --sin-informe) INFORME=0 ;;
    *) echo "opción desconocida: $a" >&2; exit 2 ;;
  esac
done

if [ ! -d "$REPO" ]; then
  echo "NO EXISTE el directorio: $REPO" >&2
  exit 2
fi
REPO="$(cd "$REPO" && pwd)"

if [ ! -f "$AUDITOR" ]; then
  echo "falta el auditor: $AUDITOR" >&2
  exit 2
fi

# ── Qué se está auditando exactamente ────────────────────────────────────────
NOMBRE="$(basename "$REPO")"
FECHA="$(date -u +%Y-%m-%d)"
HORA="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
if [ -d "$REPO/.git" ]; then
  SHA="$(git -C "$REPO" rev-parse HEAD 2>/dev/null || echo SIN-COMMIT)"
  RAMA="$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
  SUCIO="$(git -C "$REPO" status --porcelain 2>/dev/null | wc -l | tr -d ' ')"
  REMOTO="$(git -C "$REPO" config --get remote.origin.url 2>/dev/null || echo '(sin remoto)')"
else
  SHA="SIN-GIT"; RAMA="?"; SUCIO="?"; REMOTO="(no es un repositorio git)"
fi
VERSION_AUDITOR="$(sha256sum "$AUDITOR" 2>/dev/null | cut -c1-16 || echo '?')"

echo "AUDITORÍA DE DISEÑO PUBLICADO"
echo "  repo:            $REPO"
echo "  remoto:          $REMOTO"
echo "  rama / commit:   $RAMA / ${SHA:0:12}"
# Con `set -e`, un `A && B && echo` aborta el script cuando A es falsa. Va en un `if`.
if [ "$SUCIO" != "0" ] && [ "$SUCIO" != "?" ]; then
  echo "  ¡OJO!            el árbol tiene $SUCIO cambios sin commitear: se audita lo que hay en"
  echo "                   disco, no lo publicado. El informe lo anota igual."
fi
echo "  fecha (UTC):     $HORA"
echo "  auditor:         auditar_diseno_generico.py sha256:${VERSION_AUDITOR}"
echo

# ── Medir ────────────────────────────────────────────────────────────────────
SALIDA="$(mktemp)"
set +e
# shellcheck disable=SC2086
python3 -B "$AUDITOR" "$REPO" $ESTRICTO $JSON > "$SALIDA" 2>&1
CODIGO=$?
set -e
cat "$SALIDA"
echo

# ── Informe fechado, para poder volver ──────────────────────────────────────
if [ "$INFORME" = "1" ] && [ -z "$JSON" ]; then
  DIR_INFORMES="$RAIZ_NORMAS/informes"
  mkdir -p "$DIR_INFORMES"
  DESTINO="$DIR_INFORMES/$FECHA-$NOMBRE-${SHA:0:7}.md"
  {
    echo "# Auditoría de diseño · $NOMBRE"
    echo
    echo "| | |"
    echo "|---|---|"
    echo "| Fecha (UTC) | \`$HORA\` |"
    echo "| Repositorio | \`$REPO\` |"
    echo "| Remoto | \`$REMOTO\` |"
    echo "| Rama | \`$RAMA\` |"
    echo "| Commit auditado | \`${SHA}\` |"
    echo "| Cambios sin commitear | \`$SUCIO\` |"
    echo "| Auditor | \`auditar_diseno_generico.py\` sha256:\`$VERSION_AUDITOR\` |"
    echo "| Modo | \`$([ -n "$ESTRICTO" ] && echo estricto || echo normal)\` |"
    echo "| Código de salida | \`$CODIGO\` |"
    echo
    echo "## Salida íntegra del auditor"
    echo
    echo '```'
    cat "$SALIDA"
    echo '```'
    echo
    echo "## Cómo repetir esta auditoría"
    echo
    echo '```bash'
    echo "git -C \"$REPO\" checkout ${SHA}"
    echo "python3 procedimientos/auditar_diseno_generico.py \"$REPO\""
    echo '```'
    echo
    echo "Si el commit ya no está (reescritura de historia, clon superficial), este informe no se puede"
    echo "reproducir: ésa es la razón de anotar el SHA y no sólo la fecha."
  } > "$DESTINO"
  echo "informe escrito: ${DESTINO#$RAIZ_NORMAS/}"
fi
rm -f "$SALIDA"

if [ "$CODIGO" = "2" ]; then
  echo "NO SE PUDO AUDITAR (código 2): o no hay código Kotlin de producto, o el auditor no entiende esta UI." >&2
fi
exit "$CODIGO"
