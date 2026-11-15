# ACTA DE RESELLADO — 2026-11-14

*Acta exigida por CORAZON l.806 («prohibido sellar sin acta»). Documento por qué se re-sella
el árbol, qué cambió y qué NO se hizo.*

## Motivo

Reestructura por idioma de las publicaciones (decisión del dueño, 2026-11-14) y rehacer la
pieza 01 desde cero como modelo. Ambos cambios tocan ficheros del árbol sellado, así que el
lote anterior queda roto y hay que sellar uno nuevo para que `make verificar` vuelva a ser
suelo verde y no techo falso.

## Qué cambió desde el lote 2026-11-10

Editados (rompen sello previo):

1. `CORAZON-LA-BANDITA.md` — nota fechada de reestructura agregada al final (no deroga molde ni bandas).
2. `docs/bandas.json` — claves nuevas `es-dominicano` y `en-ingles` con sus bandas y la pieza 01.

Nuevos (sin sello):

3. `Arena-Reimagined/01-PUBLICACIONES/es-dominicano/` — LEEME + maestro 01 + 4 derivados (Facebook, WhatsApp, Instagram, Telegram).
4. `Arena-Reimagined/01-PUBLICACIONES/en-ingles/` — LEEME + master 01 + 4 derivados (Reddit, X, Discord, Telegram).
5. `tools/derivar_plataformas.py` — generador de recortes por plataforma.
6. `tools/vara_idiomas.py` — compuerta G20-G23 de las banditas por idioma (si existe al sellar).
7. `docs/ACTA-RESELLADO-2026-11-14.md` — esta acta.

## Qué NO se hizo

- **Ningún push.** El ritual de empuje exige `GHP_A` y no está en este entorno; todo queda local y espejado en `edt/proyectos/la-bandita-archivo/reestructura-idiomas/`.
- Ninguna pieza publicada anterior fue renombrada ni retocada: las carpetas por red quedan congeladas como historial hasta decisión del dueño sobre su archivo.
- Ninguna cifra de esta acta fue escrita de memoria: la lista sale de `make verificar` (sello roto: 2 alterados, 12 sin sellar) corrido el 2026-11-14 tras reaplicar la estructura.

## Alcance del sello nuevo

El lote nuevo cubre el árbol completo con su huella encadenada al lote anterior, como siempre.
El sello prueba que los ficheros no cambiaron después de sellarse; **no prueba que la medición
sea correcta** (nota vigente de los lotes). La corrección de las mediciones se defiende aparte:
`medicion-01-2026-11-14.json` en el espejo, con hora y endpoints.

— La Bandita · acta local, sin empuje.

### Addendum · segundo resello del mismo día

- `tools/vara.py` G8: medía el pool global de piezas bajo cada canal y su `range(1,41)`
  dejaba sin medir las piezas 41-45. Ahora mide los ficheros propios de cada canal y
  cubre 01-45. Defecto latente del repo, no introducido por la reestructura.
- Maestros 01 (es y en): agregada la firma literal de la casa
  «💓 La Bandita informa. Lo que no se midió, aquí no se escribe.» (G0 la exige).
- Derivados de la 01 regenerados con `tools/derivar_plataformas.py` tras la firma.
- `tools/vara_idiomas.py`: corregido el glob de derivados (G21/G22 pasaban vacuos).

### Addendum 2 · tercer resello del mismo día

- `tools/derivar_plataformas.py`: los derivados Instagram y X ahora llevan la firma
  literal 💓 (G0 exige firma en toda pieza viva; los recortes también son piezas).
- `tools/vara_idiomas.py`: sincronizado al clon (el fix de G21/G22 estaba en el espejo
  y no se copió en la corrida anterior; error del agente, no del repo).

### Addendum 3 · retiro de publicaciones y casa de reglas

- Decisión del dueño (2026-11-15 UTC): borradas todas las publicaciones
  (`Arena-Reimagined/01-PUBLICACIONES/`, 458 ficheros rastreables + no rastreables).
- Nuevos: `REGLAS/INDICE-DE-REGLAS.md`, `ENTORNO-DE-TRABAJO/` (LEEME, registro de fallas,
  bin/checkpoint.sh, bin/reaplicar-estructura.sh, moldes/ con maestra 01 es y master 01 en).
- `CORAZON-LA-BANDITA.md`: tabla §14 sincronizada con bandas.json + ADDENDUM DE RETIRO.
- Compuertas de pieza: se retiran hasta nuevo aviso (editarán vara.py tras diagnosticar).
- Sin push: falta GHP_A. Todo queda local + espejo edt.

### Addendum 4 · README al día, autoprueba etiquetada y empuje

- `README.md` (material sellado): reescrito completo. Describía la casa del 8 de
  noviembre —series vivas, tabla citando `Arena-Reimagined/01-PUBLICACIONES/`— y
  contradecía al Addendum 3. Ahora cuenta el presente: casa de reglas y entorno,
  retiro fechado, capas, compuertas vigentes (G0-G17 en `tools/vara.py`, G20-G23 en
  `tools/vara_idiomas.py`) y puertas de entrada. Las rutas citadas se verificaron
  vivas una por una antes de escribirse; la ruta retirada se cita con la fórmula
  «ya no existe» (cita histórica para `tools/referencias.py`).
- `CHANGELOG.md`: entrada [3.0.0] — 2026-11-15. Por el criterio de numeración de la
  casa, romper una ruta publicada sin traducción en el mapa es cambio mayor.
- `tools/autoprueba.py` (FALLA-007): el eco de la salida sintética queda etiquetado;
  una línea del árbol falso ya no suplanta un aviso de la casa real.
- `ENTORNO-DE-TRABAJO/FALLAS-Y-CONTRAPARCHES.md`: sincronizado con las entradas
  005-008 (005 present_file, 006 llaves, 007 eco sintético, 008 awk END).
- Segundo resello del 2026-11-15 (`make sellar`): el lote cubre el árbol corregido,
  con su huella encadenada a la anterior; `make verificar` tras el sello, en el mismo
  turno: EXIT=0, `fallos: NINGUNO`.
- **Push ejecutado** (autorización del dueño, 2026-11-15): lo que el Addendum 3 dejó
  pendiente («Sin push: falta GHP_A») queda hecho; se empujan el retiro, la
  reestructura y este ajuste, y se verifica la cabeza remota contra la local.
