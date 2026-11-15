# LEEME de la carpeta — La Bandita **es-dominicano**

*Corte: 2026-11-14. Esta carpeta sustituye la división por red (Facebook-dominicano-ES /
WhatsApp-dominicano-ES) por una división por **idioma**. Decisión del dueño: una bandita
`es-dominicano` que combine lo mejor del formato de Facebook, WhatsApp e Instagram, y una
bandita `en-ingles` (Reddit, X, Discord). **Ambas se comparten en Telegram.***

## Cómo funciona

1. Cada pieza existe como **un solo texto maestro** en español dominicano:
   `NN-Titulo-sin-acentos-es-dominicano-MAESTRO-AAAA-MM-DD.md`.
2. Los recortes por plataforma **no se escriben a mano**: los deriva
   `tools/derivar_plataformas.py` desde el maestro:
   - `…-Facebook-….md` → prosa plana sin tablas ni vallas (Facebook no las renderiza;
     CORAZON:312 y el defecto G18 medido: 45/45 piezas con vallas que nadie ve).
   - `…-WhatsApp-….md` → conserva tablas y monoespaciado (único canal que sí las renderiza).
   - `…-Instagram-….md` → epígrafe ≤ 2.200 caracteres + hashtags + especificación de imagen
     (Instagram no existía en el archivo hasta este corte; entra como derivado del maestro).
   - `…-Telegram-….md` → markdown completo con nota de corte automático en 4.096 caracteres.
3. El maestro manda: si una plataforma rompe formato, se ajusta el **generador**, no el
   texto publicado (CORAZON l.810), y se levanta `docs/ERRATA-<fecha>.md`.

## Banda y molde

- Banda del maestro: cuerpo **6.000–45.000** caracteres y fijado/epígrafe 900–4.000
  (`docs/bandas.json`, clave `es-dominicano`). Los derivados no se bandeán aparte: son
  recortes; el generador anota al pie de cada uno su longitud medida.
- Molde del maestro (CORAZON l.1061): mapa (5-12) → ⚡ en una página → fichas (8 campos) →
  preguntas (6-12) → tabla → glosario → enlaces → meme → medición con hora → licencia →
  firma + remate → notas fechadas. **Lo nuevo primero.**
- Toda cifra de repositorio se mide en vivo contra la API de GitHub el día del corte;
  nada de memoria ni de descripción de directorio.

## Reglas de sustitución

- Pieza publicada **no se renombra ni se retoca**: se rehace y la anterior va a
  `_ARCHIVO-HISTORICO/_reemplazadas/`.
- No publicar sin compuertas verdes y «fallos: NINGUNO».
- Lo que vive sólo en el clon (`/var/tmp`) no existe: espejar en
  `edt/proyectos/la-bandita-archivo/reestructura-idiomas/` el mismo turno (FALLA-001).
