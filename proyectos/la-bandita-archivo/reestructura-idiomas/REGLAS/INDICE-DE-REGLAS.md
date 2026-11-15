# INDICE DE REGLAS — La Bandita

*Corte: noche del sábado 14 de noviembre de 2026 (UTC-4). Este índice **señala** la ley viva;
no la sustituye. En conflicto de reglas manda la precedencia de `CIMIENTOS/01-PRECEDENCIA.md`.
Ninguna regla se cambia de pasada: primero se mide, luego se escribe aquí y en el fichero que
toca, con nota fechada.*

## Capa 1 · La ley

- **`CORAZON-LA-BANDITA.md`** (raíz) — ley operativa única: molde (l.1061), notas fechadas (§13),
  bandas (§14, sincronizada al corte 2026-11-14/15), protocolo de erratas (l.810), sello con
  acta (l.806).
- **`CIMIENTOS/`** — 00-INDICE · 01-PRECEDENCIA · 02-CONTRATO-DATOS · 03-LICENCIAS-Y-RAYA-LEGAL ·
  04-VOZ-Y-CIERRE · 05-METODO-DE-MEDICION · 06-PROTOCOLO-DE-ERRORES.
- **`PROCESOS/`** — 00-INDICE · 01-PIEZA · 02-LOTE · 03-PUBLICACION (**retirado el 2026-11-15**:
  se conserva como historia, ya no rige) · 04-CADENCIA · 05-FRONTEND.

## Capa 2 · La medida operativa

- **`docs/bandas.json`** — bandas por canal; manda sobre el texto del CORAZON (CORAZON:442).
  Desde el 2026-11-15 no quedan canales de publicación activos: las claves viven como historial
  y como banda lista si las publicaciones renacen (`es-dominicano`, `en-ingles`: cuerpo 6.000-45.000).
- **`Makefile`** — ritual, verificar, sellar, push. **El push exige `GHP_A`**; sin él, todo queda
  local y espejado.
- **`tools/vara.py`** (G0-G17) y **`tools/vara_idiomas.py`** (G20-G23) — las compuertas.
  Las compuertas que miden piezas (G0, G6, G8, G10, G12, G13-piezas) quedan **retiradas hasta
  nuevo aviso** desde el 2026-11-15: informan «SIN PIEZAS» y pasan; no miden aire.

## Capa 3 · Habilidades y parches

- **`SKILLS/`** — habilidades de oficio por carpeta, más `DEPRECADOS.md` y `LECCIONES.md`.
- **`Arena-Reimagined/HABILIDADES/`** — índice de habilidades, evolución y bitácora de lecciones.
- **`ENTORNO-DE-TRABAJO/`** — registro de fallas y contraparches, checkpoint, reaplicación del
  clon tras reinicios, y moldes medidos. La meta-capa: cómo sobrevive el trabajo.

## Registro fechado de cambios de reglas

- **(8-nov-2026)** se retira el «mínimo 45.000 de Facebook»: no existía en Facebook; banda de
  cuerpo 6.000-45.000 y fijado 900-4.000.
- **(14-nov-2026)** reestructura por idioma: `es-dominicano` (FB+WA+IG en un maestro adaptable)
  y `en-ingles` (Reddit+X+Discord), ambas en Telegram; G8 mide por canal y cubre 01-45; la firma
  💓 se exige también en derivados; nacen G20-G23.
- **(14/15-nov-2026)** decisión del dueño: **todas las publicaciones se borran** («son basura»).
  El repositorio pasa a ser casa de reglas y entorno de trabajo. Compuertas de pieza retiradas
  hasta nuevo aviso; `PROCESOS/03-PUBLICACION.md` queda como historia; los moldes medidos se
  conservan en `ENTORNO-DE-TRABAJO/moldes/`.

## Cómo se cambia una regla

1. Nota fechada en el CORAZON (o addendum a una nota existente).
2. Sincronización el mismo día entre `docs/bandas.json` y el CORAZON si toca bandas.
3. Acta si el cambio toca ficheros sellados (CORAZON l.806), y resello encadenado.
4. Entrada en este índice con su fecha. Sin los cuatro pasos, el cambio no existe.
