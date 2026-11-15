# LEEME de la carpeta — La Bandita **en-ingles**

*Corte: 2026-11-14. Segunda bandita por idioma: piezas en inglés para **Reddit, X (Twitter)
y Discord**, compartidas también en **Telegram**. No es traducción automática del maestro
español: es **un texto propio por idioma** (decisión del dueño), medido contra las mismas
fuentes el mismo día.*

## Cómo funciona

1. Cada pieza existe como **un solo texto maestro** en inglés:
   `NN-Title-no-accents-en-ingles-MASTER-AAAA-MM-DD.md`.
2. Los recortes por plataforma los deriva `tools/derivar_plataformas.py`:
   - `…-Reddit-….md` → markdown completo (tablas y enlaces sí renderizan).
   - `…-X-….md` → hilo de tweets ≤ 280 caracteres numerados 1/N, sacados de los puntos
     duros del maestro (cifras, tesis, enlaces).
   - `…-Discord-….md` → mensajes ≤ 2.000 caracteres con markdown de Discord.
   - `…-Telegram-….md` → markdown completo con nota de corte en 4.096 caracteres.
3. Mismas reglas que `es-dominicano`: el generador se ajusta, no el texto publicado;
  `docs/ERRATA-<fecha>.md` si un canal rompe formato.

## Banda y molde

- Banda del maestro: cuerpo **6.000–45.000** (`docs/bandas.json`, clave `en-ingles`).
- Molde idéntico al de la casa (CORAZON l.1061), en inglés: map → one-page ⚡ → cards
  (8 fields) → questions → table → glossary → links → meme → timed measurement →
  license → signature + closing → dated notes.
- Cifras medidas en vivo contra la API de GitHub el día del corte; los números son los
  mismos en ambos idiomas porque la fuente es la misma; la prosa no.

## Reglas de sustitución

- Pieza publicada no se renombra ni se retoca: se rehace; la anterior va a
  `_ARCHIVO-HISTORICO/_reemplazadas/`.
- No publicar sin compuertas verdes y «fallos: NINGUNO».
- Espejar en `edt/proyectos/la-bandita-archivo/reestructura-idiomas/` el mismo turno.
