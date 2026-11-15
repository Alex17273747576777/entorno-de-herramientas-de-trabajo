#!/usr/bin/env bash
# Vigilante de los frentes externos. Siete frentes:
#   1. PR #3   Awerkori/anime-extensoes (índice anime en protobuf)
#   2. Issue #32 Harrys-HQ/ShinKu    (feed/novedades)
#   3. Issue #33 Harrys-HQ/ShinKu    (biblioteca masiva + fusión)
#   4. Issue #94 salmanbappi/AniZen  (feed/novedades)
#   5. Issue #95 salmanbappi/AniZen  (biblioteca masiva + fusión)
#   6. PR #34  Harrys-HQ/ShinKu      (Fase 1 de #33) + el estado de su CI, que quedó
#      en action_required: sólo un mantenedor puede aprobar la ejecución desde un fork
#   7. Rama merge-groups-phase1 del fork Alex17273747576777/AniZen (Fase 1 de #95,
#      publicada como rama porque su AGENTS.md prohíbe abrir pull requests)
# Vive lo que viva la sesión. Sondea cada 10 minutos y escribe una línea por frente.
set -u
TOKEN=$(grep -o 'GHP_A=[A-Za-z0-9_]*' /home/user/.cerox-keys/tokens.txt | cut -d= -f2)
LOG=/home/user/work/feed-novedades/vigilancia.log
g(){ curl -sS -m 40 -H "Authorization: Bearer $TOKEN" -H "Accept: application/vnd.github+json" -H "User-Agent: arena-agent" "https://api.github.com/$1"; }
while true; do
  H=$(date -u +%H:%M:%SZ)
  g repos/Awerkori/anime-extensoes/pulls/3 | H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} PR3 state={d['state']} merged={d['merged']} comentarios={d['comments']}+{d['review_comments']} head={d['head']['sha'][:10]}\")
except Exception as e: print(os.environ['H'],'PR3 error',e)" >> "$LOG"
  for pair in "Harrys-HQ/ShinKu 32" "Harrys-HQ/ShinKu 33" "salmanbappi/AniZen 94" "salmanbappi/AniZen 95"; do
    set -- $pair
    g "repos/$1/issues/$2" | R="$1" N="$2" H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} {os.environ['R']}#{os.environ['N']} state={d['state']} comentarios={d['comments']} actualizado={d['updated_at']}\")
except Exception as e: print(os.environ['H'],os.environ['R'],os.environ['N'],'error',e)" >> "$LOG"
  done
  # Frente 6: PR #34 y su CI
  g repos/Harrys-HQ/ShinKu/pulls/34 | H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} PR34 state={d['state']} merged={d['merged']} mergeable_state={d.get('mergeable_state')} comentarios={d['comments']}+{d['review_comments']} head={d['head']['sha'][:10]}\")
except Exception as e: print(os.environ['H'],'PR34 error',e)" >> "$LOG"
  g "repos/Harrys-HQ/ShinKu/actions/runs?branch=merge-groups-phase1&per_page=5" | H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin)
    for r in d.get('workflow_runs',[]):
        print(f\"{os.environ['H']} PR34-CI {r['name']} id={r['id']} {r['status']}/{r['conclusion']}\")
except Exception as e: print(os.environ['H'],'PR34-CI error',e)" >> "$LOG"
  # Frente 7: rama del fork de AniZen (sin abrir PR, por su AGENTS.md)
  g "repos/Alex17273747576777/AniZen/branches/merge-groups-phase1" | H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} FORK-AniZen rama=merge-groups-phase1 viva={d['commit']['sha'][:10]}\")
except Exception as e: print(os.environ['H'],'FORK-AniZen error',e)" >> "$LOG"
  sleep 600
done
