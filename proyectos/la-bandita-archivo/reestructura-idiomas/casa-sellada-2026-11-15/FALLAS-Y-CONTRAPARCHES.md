# FALLAS Y CONTRAPARCHES — registro canónico de La Bandita

*Corte: noche del sábado 14 de noviembre de 2026 (UTC-4). Copia canónica en el repositorio;
copia de supervivencia en `edt/docs/FALLAS-Y-CONTRAPARCHES.md` (el espejo sobrevive reinicios;
el remoto, cuando haya push, será la fuente). Cada falla que tumbe trabajo se registra aquí
con su contraparche u habilidad solucionadora **antes** de proseguir.*

Formato: síntoma → causa → contraparche/habilidad → estado.

---

## FALLA-001 · Turno caído por tiempo («The AI took too long to respond»)

- **Síntoma:** el turno murió a mitad de faena; el dueño vio `The AI took too long to respond.
  Please try again.` con id `01a1da29-208d-70f4-b9a4-bb9d34ea4bb6` (2026-11-14). Lo no guardado
  a fichero se perdió con el turno.
- **Causa:** un solo turno intentó el paquete completo (decenas de piezas de 40-63 k) sin
  persistir estados intermedios.
- **Contraparche / habilidad:** `SKILL-TURNO-CON-CHECKPOINT` + `bin/checkpoint.sh`:
  leer checkpoint al abrir, escribir en cada hito, tope de 2 maestras por turno (enmienda
  3-bis: turno combinado permitido sólo con checkpoint+espejo entre hitos), espejar todo en
  `edt/`, invocar con `bash`, y un reenvío tras timeout no es instrucción nueva: se retoma.
- **Estado:** CONTRAPARCHADA.

## FALLA-002 · Detector G19 cazaba slugs pelados y dejaba pasar cultura pop

- **Síntoma:** 44 falsos positivos por regex de slug `owner/repo`; luego `EntityData/Q193835.json`
  (Wikidata) contó como repo.
- **Causa:** medir por forma en vez de por vocabulario de medición.
- **Contraparche:** G19 por vocabulario (`★|estrellas`, URLs github, `repositorio|repos`,
  SPDX) con `en_mision = ★>=3 or urls>=1 or repos>=3 or licencias>=2`, validado pieza por pieza
  (45/45). Lección: todo detector se valida contra un positivo y un negativo conocidos.
- **Estado:** CONTRAPARCHADA y validada.

## FALLA-003 · El reinicio se llevó el clon y con él las EDICIONES no espejadas

- **Síntoma:** reinicios entre turnos borraron `/var/tmp/la-bandita-archivo`; el espejo tenía
  los ficheros nuevos pero no las ediciones (nota del CORAZON, bandas, estructura).
- **Causa:** la SKILL mandaba espejar contenido nuevo, no **ediciones** a ficheros existentes.
- **Contraparche:** `bin/reaplicar-estructura.sh` (reconstruye en un mando, idempotente por
  marcador) + regla: toda edición vive además como fichero propio en el espejo; bandas.json se
  edita en el espejo y se copia al clon, nunca al revés.
- **Estado:** CONTRAPARCHADA.

## FALLA-004 · Overlay de sellos por nombre y lista de herramientas a mano

- **Síntoma:** tras un reinicio, `atestar --verificar` rojo («tabla TSV no corresponde al lote»)
  porque el overlay sólo copió `lote-2026-11-14.json` y no su `.tsv`; y G8 rojo otra vez porque
  `reaplicar` no copiaba el `vara.py` corregido: el clon revivió con el bug original.
- **Causa:** overlay por nombre exacto (un fichero) y lista de herramientas escrita a mano en
  el script: todo lo no listado renacía roto o faltante.
- **Contraparche:** overlay con glob `lote-2026-11-14.*` (json, tsv y lo que el lote produzca)
  y `reaplicar` copia **toda** herramienta espejada bajo `tools/` (vara.py,
  derivar_plataformas.py, vara_idiomas.py). Comprobación: tras reaplicar, atestar y vara
  verdes sin resellar.
- **Estado:** CONTRAPARCHADA (corte de la retirada de publicaciones).

---

## FALLA-005 · present_file entrega el entregable roto al dueño

- **Síntoma:** el visor de entregables llega disfuncional al dueño (iframe aislado, sin
  red: sin estilos, sin imágenes, sin nada que cargue de fuera).
- **Causa:** limitación de la plataforma, no del archivo; presentar ahí es entregar roto.
- **Contraparche / habilidad solucionadora:** prohibido `present_file` para entregables;
  la ruta se da en el chat y el archivo vive en el espejo persistente.
- **Estado:** CONTRAPARCHADA (2026-11-15).

## FALLA-006 · Llaves pegadas en el chat y llavero relajado tras reinicio

- **Síntoma:** cuatro llaves de GitHub viajaron en texto plano por el chat; tras un
  reinicio el llavero `tokens.txt` amaneció en 0644.
- **Causa:** el chat no es una bóveda y los reinicios relajan permisos (pariente de
  FALLA-003).
- **Contraparche / habilidad solucionadora:** llavero en 0600 con las llaves nombradas;
  nunca imprimirlas ni citarlas. La ROTACIÓN sigue pendiente: sólo el dueño puede crear
  llaves nuevas (GitHub no expone API para crear PATs).
- **Estado:** CONTRAPARCHADA A MEDIAS (la rotación depende del dueño).

## FALLA-007 · La salida sintética de la autoprueba se leía como aviso real

- **Síntoma:** `make verificar` imprimía «⚠ rutas vivas rotas: README.md:1 · cita a
  carpeta-vieja/» y no había tal cita en el README real; de ahí nació una nota de
  «aviso abierto» falsa que costó un turno de diagnóstico.
- **Causa:** `tools/autoprueba.py` hace eco de las primeras tres líneas de cada compuerta
  corriendo contra el ÁRBOL FALSO sin decir de dónde salen; el README del árbol falso
  cita `carpeta-vieja/` en su línea 1 a propósito.
- **Contraparche / habilidad solucionadora:** eco etiquetado («salida del árbol
  sintético — no es la casa») y cada línea prefijada con `|`. La autoprueba sigue
  detectando el fallo sintético; ya no suplanta a la casa.
- **Estado:** CONTRAPARCHADA (2026-11-15).

## FALLA-008 · `exit 0` dentro de una regla awk cae al END y voltea el veredicto

- **Síntoma:** una comprobación por lotes («¿está este archivo sellado?») declaró NO
  sellados a todos, incluido `README.md`, que el grep directo sí encontraba en el
  manifiesto.
- **Causa:** `awk '$1==p{exit 0} END{exit 1}'` — en awk, `exit` salta al bloque END, y
  el `exit 1` del END pisa al 0 de la regla.
- **Contraparche / habilidad solucionadora:** comprobación con bandera
  (`$1==p{f=1} END{exit !f}`) o `grep -q "^ruta<TAB>"`; desconfiar de todo `exit` dentro
  de regla si hay bloque END.
- **Estado:** CONTRAPARCHADA (2026-11-15).

---

## Plantilla de entrada nueva

```
## FALLA-NNN · <título>
- **Síntoma:** …
- **Causa:** …
- **Contraparche / habilidad solucionadora:** …
- **Estado:** ACTIVA | CONTRAPARCHADA
```
