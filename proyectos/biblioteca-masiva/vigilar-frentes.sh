#!/usr/bin/env bash
# Vigilante de los frentes externos. Nueve frentes:
#   1. PR #3   Awerkori/anime-extensoes (índice anime en protobuf)
#   2. Issue #32 Harrys-HQ/ShinKu    (feed/novedades)
#   3. Issue #33 Harrys-HQ/ShinKu    (biblioteca masiva + fusión)
#   4. Issue #94 salmanbappi/AniZen  (feed/novedades)
#   5. Issue #95 salmanbappi/AniZen  (biblioteca masiva + fusión)
#   6. PR #34  Harrys-HQ/ShinKu      (Fase 1 de #33) + el estado de su CI, que quedó
#      en action_required: sólo un mantenedor puede aprobar la ejecución desde un fork
#   7. Rama merge-groups-phase1 del fork Alex17273747576777/AniZen (Fase 1 de #95)
#   8. Rama feed-cap-per-tab del mismo fork (Fase 2 de #94)
#      Las dos publicadas como ramas porque su AGENTS.md prohíbe abrir pull requests
#   9. Rama feed-tabs-phase1 del fork Alex17273747576777/ShinKu (Fase 1 del feed, apilada
#      sobre el PR #34: su 43.sqm sigue al 42.sqm de ese PR, así que no lleva PR propio)
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
  # Frentes 7 y 8: ramas del fork de AniZen (sin abrir PR, porque su AGENTS.md lo prohíbe)
  #   merge-groups-phase1 = Fase 1 de #95 (grupos de fusión)
  #   feed-cap-per-tab    = Fase 2 de #94 (tope de 25 fuentes por pestaña)
  for rama in merge-groups-phase1 feed-cap-per-tab; do
    g "repos/Alex17273747576777/AniZen/branches/$rama" | R="$rama" H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} FORK-AniZen rama={os.environ['R']} viva={d['commit']['sha'][:10]}\")
except Exception as e: print(os.environ['H'],'FORK-AniZen',os.environ['R'],'error',e)" >> "$LOG"
  done
  # Frente 9: rama feed-tabs-phase1 del fork de ShinKu (Fase 1 del feed, sin PR propio)
  g "repos/Alex17273747576777/ShinKu/branches/feed-tabs-phase1" | H="$H" python3 -c "
import json,sys,os
try:
    d=json.load(sys.stdin); print(f\"{os.environ['H']} FORK-ShinKu rama=feed-tabs-phase1 viva={d['commit']['sha'][:10]}\")
except Exception as e: print(os.environ['H'],'FORK-ShinKu error',e)" >> "$LOG"
  sleep 600
done
