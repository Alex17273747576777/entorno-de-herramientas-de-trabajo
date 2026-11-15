## 14. BANDAS DE LONGITUD (operativas, al corte 2026-11-14, sincronizadas con `docs/bandas.json`)

| Canal | Banda | Comprobación |
|---|---|---|
| es-dominicano (cuerpo maestro) | **6.000 – 45.000** caracteres | `docs/bandas.json` + M11 |
| en-ingles (cuerpo maestro) | **6.000 – 45.000** caracteres | `docs/bandas.json` + M11 |
| Derivados por plataforma | no se bandean: son cortes del maestro; el generador anota su longitud al pie | `tools/derivar_plataformas.py` |
| Facebook / WhatsApp / HdP | **retiradas el 2026-11-15 con las publicaciones**; las bandas 40.000–45.000, 63.000–63.099 y 1.800–3.200 quedan como historial | addendum de retiro (al final de esta ley) |
---ADDENDUM---

## ADDENDUM DE RETIRO — noche del sábado 14 de noviembre de 2026 (UTC-4)

Decisión del dueño: **todas las publicaciones se borran** («olvidate de las publicaciones, las
borraras todas, son basura»). Ejecutado en este corte: `Arena-Reimagined/01-PUBLICACIONES/`
eliminado (458 ficheros rastreables más los no rastreables de la reestructura por idioma).
El repositorio pasa a ser **casa de reglas y entorno de trabajo**: `REGLAS/INDICE-DE-REGLAS.md`
indexa la ley viva; `ENTORNO-DE-TRABAJO/` guarda el registro de fallas, el checkpoint, la
reaplicación del clon y los moldes medidos. Las compuertas que miden piezas quedan retiradas
hasta nuevo aviso (informan «SIN PIEZAS» y pasan, no miden aire); `PROCESOS/03-PUBLICACION.md`
queda como historia. Los moldes (maestra 01 es-dominicano y master 01 en-ingles, medidos en
vivo contra la API de GitHub y con firma 💓) se conservan en `ENTORNO-DE-TRABAJO/moldes/` como
ejemplo de pieza buena. Este addendum no deroga el molde ni el método de medición: los
conserva intactos para cuando las publicaciones renazcan.
