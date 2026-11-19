# Pieza 17 — La capa de inmersión: los lectores que enseñan japonés mientras lees — y el cliente Komga que faltaba

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `a1340d0151d9` · ES-TG `5a2d1d0a63f5` · EN-Reddit `758b80f3440a` · EN-Discord `87a873268de5`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 17 — La capa de inmersión: los lectores que enseñan japonés mientras lees — y el cliente Komga que faltaba

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🦋 Chimahon — el fork de Mihon que mina Anki
├── 📚 Hoshi Reader — el EPUB japonés con mil herramientas
├── 🎐 Yomikai — OCR, voces y el mini-player flotante
├── 🌗 Yomi Reader — el triple anime/manga/novela
├── 🏛️ Koharia — tu servidor Komga, en tu bolsillo
├── 🧩 Los talleres detrás (diccionarios compartidos y más)
├── ⚖️ ¿Para quién es esta capa?
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Hay una capa del ecosistema que los mapas grandes casi no ven: la de quien lee en japonés APRENDIÉNDOLO — diccionarios al toque, tarjetas de Anki al vuelo, texto vertical, manga Mokuro, voz encima de la página. Esta guía ficha los cinco proyectos vivos de esa capa, todos verificados HOY, 14 de septiembre — **dos publicaron versión hoy mismo**:

```
Hoshi Reader   ★378   v1.3.3 (13-ago)   EPUB japonés + Yomitan + Anki + e-ink
Chimahon       ★198   v2.4.2 (HOY, 15-sep)   fork de Mihon: diccionario, Mokuro, Anki
Koharia        ★148   v0.5.0 (14-sep)      cliente Android para servidores Komga
Yomi Reader    ★10    v0.1.7 (6-sep)    anime + manga + novela, compat. Tadami
Yomikai        ★0     v1.9.84 (HOY, 15-sep)  OCR + voces + mini-player flotante
```

Estrellas chicas, talleres grandes: aquí los números de fama no cuentan la historia — la cadencia y las funciones sí.

## 🦋 Chimahon — el fork de Mihon que mina Anki

https://github.com/Chimahon/chimahon

```
★198 · GPL-3.0
v2.4.2 (HOY, 15-sep) · v2.4.1 · v2.4.0 (11-sep) — tres en cuatro días
Qué es: «fork de inmersión de Mihon» (su descripción):
diccionario nativo (Yomitan), manga Mokuro y anime,
lector de novelas EPUB, y minado instantáneo a Anki
```

Es Mihon con aula dentro: lees tu manga de siempre y, al tocar una palabra, el diccionario abre ahí mismo; lo que quieras guardar, vuela a tu mazo de Anki sin salir del capítulo. Su taller mantiene además los componentes: Chimahon-ffmpeg y Chimahon-local-models (procesamiento local), y usa los diccionarios de Hoshi — la capa se teje entre sí.

## 📚 Hoshi Reader — el EPUB japonés con mil herramientas

https://github.com/HuangAntimony/Hoshi-Reader-Android

```
★378 · GPL-3.0
v1.3.3 (13-ago) — la mayor de la capa
Qué es: lector de EPUB japonés con búsqueda
Yomitan, minado a Anki, lectura acompañada de
audiolibro y soporte de tinta electrónica
```

Su README (leído el 14-sep) lista lo suyo: EPUB individuales o por lotes con progreso visible, estanterías propias, texto vertical u horizontal con paginación o scroll continuo, diccionarios Yomitan que se importan y actualizan desde la app, búsqueda recursiva (tocas una palabra dentro de una definición y sigue), modo enfoque inmersivo, paso de página con las teclas de volumen y opciones específicas para lectores e-ink. Y es la punta de un taller completo: su autor mantiene los diccionarios (hoshidicts), una gramática japonesa de referencia, herramientas para novelas web (narou-py) y contribuye a Yomitan y mpvacious. La capa de inmersión tiene centro de gravedad, y se llama HuangAntimony.

## 🎐 Yomikai — OCR, voces y el mini-player flotante

https://github.com/sj0404-collab/yomikai
(el «yomihon-custom» que circula: https://github.com/sj0404-collab/yomihon-custom)

```
Apache-2.0
v1.9.84 (HOY, 15-sep) · v1.9.83 (madrugada del 15) · v1.9.79 (14-sep) · v1.9.78/76 (13-sep)
— cadencia diaria de verdad
Qué es: lector de manga con OCR y ovoz
(roles y voces), diccionarios, y un
mini-player flotante sobre todas las apps
```

Su descripción (del ruso original) lo dice entero: manga con OCR de texto, ovoz por roles, diccionarios y un reproductor mini que flota sobre cualquier aplicación — escuchas la voz del capítulo mientras lees en otro lado. Dos apuntes de mapa: el proyecto raíz es **Yomihon** (yomihon/yomihon, ★125, «ahora con OCR», v0.4.0 del 30-jul) — el nombre del repo «yomihon-custom» viene de ahí — y la casa activa es Yomikai, con hermana web (yomikai-pwa, React+TSX, con navegador y chat IA dentro). Que no tenga estrellas no significa nada: publica versiones todos los días.

## 🌗 Yomi Reader — el triple anime/manga/novela

https://github.com/codegeasse1/yomi-reader

```
★10 · Apache-2.0
v0.1.7 (6-sep) — joven, en 0.1
Qué es: «lector de código abierto de anime,
manga y novelas para Android (compatible
Tadami/Aniyomi)» — su descripción
```

La apuesta del triple en el linaje de Aniyomi: las tresmedias en una app, comiendo extensiones compatibles con Tadami. Va por 0.1 — edad honesta — y su taller trae más: Nekoread (lector de manga, v2.2.5 del 10-sep) e hikari (streaming universal con addons de Stremio y plugins CloudStream, v0.3.67 del 13-sep). Un constructor con cinco hierros en el fuego — seguimiento abierto para todos.

## 🏛️ Koharia — tu servidor Komga, en tu bolsillo

https://github.com/Mister-album/Koharia

```
★147 · Apache-2.0
v0.5.0 (14-sep) · v0.4.5 (6-sep)
Qué es: «lector Android independiente de
terceros para navegar y leer contenido de
servidores Komga» — su descripción (del chino)
```

Komga es el servidor de biblioteca que los grandes lectores ya sincronizan; Koharia es la app dedicada a él: tu servidor, tu app, con el lector puesto a medida. v0.5.0 publicada el 14-sep. Del mismo autor: la web del proyecto y su propio fork del servidor komga — quien construye el cliente entiende el servidor, y al revés.

**La otra mitad de la capa, verificada esta noche por exploración libre:** **Komga** (gotson/komga, ★6.659, MIT, 1.26.3 del 12 de agosto) — servidor de comics, mangas y eBooks con API, OPDS y sincronización Kobo y KOReader; y **Kavita** (Kareadita/Kavita, ★11.677, GPL-3.0, v0.9.1.4 del 2-sep), el servidor de lectura multiplataforma. Koharia vive porque estos viven — y viceversa: el servidor sin clientes es un archivo, el cliente sin servidor es una cáscara.

## 🧩 Los talleres detrás (diccionarios compartidos y más)

La capa se sostiene en infraestructura compartida que conviene nombrar: los **diccionarios hoshidicts** los usa también Chimahon; **Yomitan** (el diccionario-pop-up del navegador, referencia absoluta del nicho) conecta con todos; y en la observación de esta semana quedó un compañero chico pero vivo: **android-koreader-companion** (★9, MIT, versión del 14-sep) — muestra lo que lees en KOReader y Mihon, el progreso entre los dos mundos.

## ⚖️ ¿Para quién es esta capa?

```
¿Lees manga en japonés y estudias?
   → Chimahon (si vienes de Mihon) o
     Yomikai (si quieres voz y OCR).

¿Lees novelas ligeras en EPUB japonés?
   → Hoshi Reader: es SU terreno, con
     e-ink incluido para el lector de tinta.

¿Anime + manga + novela en una sola app
(y el japonés no es tu foco)?
   → Yomi Reader — y mira Tadami (pieza 13),
     el triple del linaje Aniyomi con años encima.

¿Tienes un servidor Komga?
   → Koharia, la app dedicada.
```

Ninguna ficha pasa por fama: pasa por cadencia, funciones propias y repo abierto — y las cinco viven, re-verificadas a HOY 15-sep.

## ❓ Preguntas frecuentes

**¿Estos reemplazan a Mihon/Komikku/Aniyomi?**
No: son capas encima o al lado. Chimahon ES un fork de Mihon (tu biblioteca migra con las reglas de siempre); Koharia necesita un servidor Komga; Hoshi es para EPUB japonés; Yomikai y Yomi Reader son casas aparte. Cada uno cubre lo que el tronco no.

**¿Y las extensiones? ¿Sirven las de siempre?**
Yomi Reader declara compatibilidad Tadami/Aniyomi; Chimahon, al ser fork de Mihon, hereda el ecosistema Mihon. Hoshi (EPUB) y Koharia (Komga) no comen extensiones: comen libros y servidores. Yomikai construye sus fuentes propias — su README manda el día que la uses.

**¿Por qué estrellas tan chicas si son tan activos?**
Porque el nicho es nicho: quien estudia japonés con manga son miles, no millones. La vara de la casa nunca fue la fama — es la cadencia y el aporte propio, y aquí sobran.

**¿Funcionan sin saber japonés?**
Chimahon, Hoshi y Yomikai EXISTEN para aprenderlo — el diccionario y la voz son el punto. Para lectura en español/inglés, los troncos de las piezas 13–16 siguen siendo la casa.

## 🔗 Enlaces

- Chimahon: https://github.com/Chimahon/chimahon
- Hoshi Reader: https://github.com/HuangAntimony/Hoshi-Reader-Android
- Yomikai: https://github.com/sj0404-collab/yomikai · gemela web: https://github.com/sj0404-collab/yomikai-pwa · raíz del nombre: https://github.com/yomihon/yomihon
- Yomi Reader: https://github.com/codegeasse1/yomi-reader · hermanos: https://github.com/codegeasse1/Nekoread
- Koharia: https://github.com/Mister-album/Koharia
- Compañero de progreso: https://github.com/woxakv/android-koreader-companion
- Los servidores: https://github.com/gotson/komga · https://github.com/Kareadita/Kavita

> La Bandita informa a partir de fuentes fechadas. Leer con diccionario en la mano — ahora, en el mismo dedo.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Chimahon v2.4.2, Yomikai 1.9.84, Koharia ★148 (todas de HOY). Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 La capa de inmersión — lectores que te enseñan japonés

Cinco vivos, verificados HOY:

- **Chimahon** ★198 · v2.4.2 HOY — Mihon + diccionario + Mokuro + Anki · github.com/Chimahon/chimahon
- **Hoshi Reader** ★379 · v1.3.3 — EPUB japonés + Yomitan + e-ink
- **Yomikai** ★0 · 1.9.84 HOY — OCR, voces por roles, mini-player
- **Yomi Reader** ★10 · v0.1.7 — el triple con compatibilidad Tadami
- **Koharia** ★148 · v0.5.0 — tu Komga en el bolsillo (Komga ★6.662 detrás)

Dos releases el mismo día (Chimahon + Yomikai): la capa está más viva que nunca. Pa' el que abre un manga en japonés y no se rinde con la primera página.
*Fuente: pieza 17 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 17 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Esto pa' qué sirve si no sé japonés? —Pa' dejar de no saberlo, mientras lees.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# Readers that teach you Japanese while you read: Chimahon, Hoshi, Yomikai, Yomi and Koharia (the immersion layer)
**Reddit · ingles-US · fuente: pieza 17 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** The layer the big maps don't even see: a dictionary on tap, Anki on the fly, vertical text. Today: Chimahon ★198 (v2.4.2 from TODAY), Hoshi ★379, Yomikai (1.9.84 from TODAY), Yomi ★10, Koharia ★148.
## Five living ones, verified TODAY

- **Chimahon** — ★198 · **v2.4.2 from TODAY** — a Mihon fork with a built-in dictionary, Mokuro (OCR-able manga) and Anki export · github.com/Chimahon/chimahon
- **Hoshi Reader** — ★379 · v1.3.3 (Aug 13) — Japanese EPUB with Yomitan, Anki and e-ink support
- **Yomikai** — ★0 · **1.9.84 from TODAY** — manga with OCR, role voices and a floating mini-player; day-by-day cadence
- **Yomi Reader** — ★10 · v0.1.7 — the anime/manga/novel triple, declared Tadami compatibility
- **Koharia** — ★148 · v0.5.0 (Sep 14) — your Komga server in your pocket · behind it: **Komga** — ★6,662 · MIT · 1.26.3

## The shared infra

The hoshidicts dictionaries are used by Chimahon and Hoshi; Yomitan feeds several. **The layer is a small town: everybody knows everybody.**

**Who is this for?** For whoever opens a manga in Japanese and doesn't give up on the first page. Everybody else: pieces 06 and 16 are your street.

**Two releases the same day (Chimahon + Yomikai):** the layer is more alive than ever — the cutoff documents it.
> —What's this for if I don't know Japanese?
> —For stopping not knowing it, while you read.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# The immersion layer — readers that teach you Japanese (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 17 (Sep 15) · **Verified:** today, September 15, 2026

The layer the big maps don't even see: the one for people who read Japanese while LEARNING it — dictionaries on tap, Anki cards on the fly, vertical text. Five living ones, verified TODAY:

- **Chimahon** — ★198 · **v2.4.2 from TODAY** — a Mihon fork with built-in dictionary, Mokuro (OCR-able manga) and Anki export · github.com/Chimahon/chimahon
- **Hoshi Reader** — ★379 · v1.3.3 (Aug 13) — Japanese EPUB with Yomitan, Anki and e-ink support · github.com/HuangAntimony/Hoshi-Reader-Android
- **Yomikai** — ★0 · **1.9.84 from TODAY** — manga with OCR, role voices and a floating mini-player; day-by-day cadence · github.com/sj0404-collab/yomikai
- **Yomi Reader** — ★10 · v0.1.7 — the anime/manga/novel triple, with declared Tadami compatibility
- **Koharia** — ★148 · v0.5.0 (Sep 14) — your Komga server in your pocket · and the server behind it: **Komga** — ★6,662, MIT, 1.26.3

**The shared infra:** the hoshidicts dictionaries are used by Chimahon and Hoshi; Yomitan feeds several. The layer is a small town: everybody knows everybody.

**Who is this for?** For whoever opens a manga in Japanese and doesn't give up on the first page. Everybody else: pieces 06 and 16 are your street.

**Two releases on the same day (Chimahon + Yomikai):** the layer is more alive than ever — and tonight's cutoff documents it.

The house meme:
> —What's this for if I don't know Japanese?
> —For stopping not knowing it, while you read.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
