#!/usr/bin/env bash
# pr3-vigilar.sh — vigila el PR #3 de Awerkori mientras viva esta sesión.
# Bitácora: pr3-watch.log (una línea por cambio de estado; termina si el PR cierra/fusiona).
LOG=/home/user/work/nox-index-pb/pr3-watch.log
TK=$(grep -o 'GHP_A=.*' ~/.cerox-keys/tokens.txt | cut -d= -f2)
ULT=""
while true; do
  S=$(curl -s -H "Authorization: Bearer $TK" https://api.github.com/repos/Awerkori/anime-extensoes/pulls/3 | python3 -c "
import json,sys
d=json.load(sys.stdin)
print(d.get('state'), 'fusionado' if d.get('merged_at') else 'sin-fusionar', 'comentarios', d.get('comments',0)+d.get('review_comments',0), d.get('updated_at'))" 2>/dev/null)
  if [ -n "$S" ] && [ "$S" != "$ULT" ]; then
    echo "$(date -u +%F' '%H:%M'Z') PR3: $S" >> "$LOG"
    ULT="$S"
  fi
  case "$S" in closed*) echo "$(date -u +%F' '%H:%M'Z') vigilancia terminada (PR cerrado/fusionado)" >> "$LOG"; exit 0;; esac
  sleep 300
done
