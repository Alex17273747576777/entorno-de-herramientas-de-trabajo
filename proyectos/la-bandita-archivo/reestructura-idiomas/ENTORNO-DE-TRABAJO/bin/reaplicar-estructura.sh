#!/usr/bin/env bash
# reaplicar-estructura.sh — contraparche de FALLA-003: el reinicio borra /var/tmp.
# Reconstruye EN UN MANDO los cambios de sistema del clon a partir del espejo edt.
# Uso: bash reaplicar-estructura.sh /var/tmp/la-bandita-archivo
# Idempotente: la nota del CORAZON sólo se agrega si no está (marcador por grep).
# El espejo manda sobre bandas.json: toda edición de bandas se hace aquí y se copia al clon.
set -eu
CLON="${1:?ruta del clon}"
MIR="$(cd "$(dirname "$0")" && pwd)"
PUB="$CLON/Arena-Reimagined/01-PUBLICACIONES"
test -d "$CLON/.git" || { echo "ERROR: $CLON no es un clon" >&2; exit 1; }
mkdir -p "$PUB/es-dominicano" "$PUB/en-ingles"
cp "$MIR/LEEME-es-dominicano.md" "$PUB/es-dominicano/LEEME-de-la-carpeta.md"
cp "$MIR/LEEME-en-ingles.md"     "$PUB/en-ingles/LEEME-de-la-carpeta.md"
cp "$MIR/derivar_plataformas.py" "$CLON/tools/derivar_plataformas.py"
[ -f "$MIR/vara_idiomas.py" ] && cp "$MIR/vara_idiomas.py" "$CLON/tools/vara_idiomas.py"
cp "$MIR/bandas.json" "$CLON/docs/bandas.json"
if [ -d "$MIR/attestations-overlay" ]; then
  mkdir -p "$CLON/attestations"
  cp "$MIR"/attestations-overlay/lote-*.* "$CLON/attestations/" 2>/dev/null || true
  echo "attestations: overlay restaurado ($(ls "$MIR/attestations-overlay" | wc -l) ficheros, glob lote-*.*)"
fi
for d in ENTORNO-DE-TRABAJO REGLAS; do
  if [ -d "$MIR/$d" ]; then
    mkdir -p "$CLON/$d"
    cp -r "$MIR/$d/." "$CLON/$d/" 2>/dev/null || true
    echo "$d: restaurado desde espejo"
  fi
done
for a in "$MIR"/actas/ACTA-*.md; do [ -f "$a" ] && cp "$a" "$CLON/docs/"; done
if ! grep -q "NOTA DE REESTRUCTURA — sábado 14 de noviembre de 2026" "$CLON/CORAZON-LA-BANDITA.md"; then
  cat "$MIR/CORAZON-nota-reestructura-2026-11-14.md" >> "$CLON/CORAZON-LA-BANDITA.md"
  echo "CORAZON: nota agregada"
else
  echo "CORAZON: nota ya estaba"
fi
# parche de bandas + addendum de retiro (FALLA-003: las ediciones viven como fichero propio)
PATCH="$MIR/CORAZON-fix-bandas-y-retiro-2026-11-14.md"
if [ -f "$PATCH" ] && ! grep -q "ADDENDUM DE RETIRO" "$CLON/CORAZON-LA-BANDITA.md"; then
  python3 - "$CLON/CORAZON-LA-BANDITA.md" "$PATCH" <<'PY'
import sys, pathlib
cor, patch = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
txt = cor.read_text(encoding="utf-8")
nuevo, add = patch.read_text(encoding="utf-8").split("---ADDENDUM---")
ini = txt.find("## 14. BANDAS DE LONGITUD")
fin = txt.find("| HdP (serie corta)")
fin = txt.find("\n", fin) + 1
txt = txt[:ini] + nuevo.rstrip("\n") + txt[fin:] + "\n" + add
cor.write_text(txt, encoding="utf-8")
print("CORAZON: bandas sincronizadas + addendum de retiro")
PY
else
  echo "CORAZON: parche de bandas ya aplicado o ausente en espejo"
fi
cp "$MIR"/es-dominicano/*.md "$PUB/es-dominicano/" 2>/dev/null || true
cp "$MIR"/en-ingles/*.md     "$PUB/en-ingles/"     2>/dev/null || true
echo "REAPLICADO_OK es=$(ls "$PUB/es-dominicano" | wc -l) en=$(ls "$PUB/en-ingles" | wc -l) herramientas=$(ls "$CLON/tools/derivar_plataformas.py" "$CLON/tools/vara_idiomas.py" 2>/dev/null | wc -l)"
