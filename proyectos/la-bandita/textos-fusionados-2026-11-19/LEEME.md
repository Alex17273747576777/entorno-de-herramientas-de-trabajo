# Léeme — Textos fusionados de La Bandita

**Qué es.** Las 70 piezas (01–70) del corpus de La Bandita, reunidas **un archivo por número**, bilingües.

**Cómo se hizo (2026-11-19).** Se descargaron los cuerpos reales desde el repositorio
`Alex17273747576777/la-bandita-archivo`, rama `main`, carpeta
`ARCHIVO-HISTORICO/04-VERSIONES-MULTIIDIOMA/<plataforma>/<variante>/`. Cada cuerpo se copió
**textual, sin reescritura**; la fusión es puro ensamblaje. La trazabilidad (ruta + sha del blob en
GitHub) va en la cabecera de cada archivo para poder auditar byte a byte.

**Decisiones del dueño aplicadas.**
- Español = Facebook·WhatsApp + Telegram. Se comprobó en las 80 piezas que Facebook y WhatsApp son
  **byte-idénticos** (mismo sha); por eso aparecen como un único bloque «Facebook·WhatsApp», no duplicados.
  Telegram sí es una adaptación genuina (post corto de canal) y va aparte.
- Inglés = Reddit + Discord. La variante **X / Twitter nunca existió** en la matriz multiplataforma
  (los canales presentes son discord, facebook, instagram, reddit, rethubs, telegram, whatsapp, xda),
  así que se entrega Reddit + Discord y se anota X como pendiente.

**Cobertura medida.** 280/280 cuerpos descargados sin fallos; cada pieza 01–70 tiene los cuatro bloques.

**Archivos.** `INDICE.md` (tabla con tamaños), este `LEEME.md`, y `01-…` a `70-La-Bandita-fusion-bilingue.md`.
