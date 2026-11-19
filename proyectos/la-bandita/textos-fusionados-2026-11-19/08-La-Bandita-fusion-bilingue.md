# Pieza 08 — Música FOSS: clientes con repo y fecha de pulso — Spotify crackeado no entra

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `cb9004aebc40` · ES-TG `10b2b8e267c7` · EN-Reddit `71097e7760ef` · EN-Discord `5b1285493641`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 08 — Música FOSS: clientes con repo y fecha de pulso — Spotify crackeado no entra

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── ⚖️ Qué no es esta guía
├── 🧬 La genealogía: de ViMusic a la familia actual
├── 🎧 Los clientes de streaming, ficha por ficha
├── 📻 NewPipe: la especie aparte
├── 📂 Auxio: tu música, tus archivos
├── 🎙️ AntennaPod: los podcasts
├── 🆕 Los que faltaban: N-Zik y Gabi
├── 🚫 Lo que no se pega
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Guía de clientes de música de código abierto, con el pulso de cada proyecto medido el 14 de septiembre y re-verificado al mudar (15-sep). La semana trajo movimiento de verdad en esta familia: OuterTune estrenó versión este mes, Metrolist sigue en racha de lanzamientos, y el linaje completo quedó documentado.

```
STREAMING (YouTube Music como fondo)
SimpMusic      ★11.257   2.1.0 (7-sep)     push 11-sep   vivo
OuterTune      ★5.390    v0.11.1 (6-sep)   push 6-sep    vivo
Metrolist      ★12.789   13.7.0 (7-sep) · Nightly del 14 a la vista    vivo          ← la más activa
InnerTune      ★6.088    push nov-2025                   dormido
Harmony-Music  ★3.081    v1.12.2 (dic-25)  multiplataforma
music-you      ★220      vivo              minimalista
InterTune      ★12       fork fijo, nicho

STREAMING (front-end general)
NewPipe        ★39.682   v0.29.1 (15-ago)  push 31-ago

ARCHIVOS LOCALES
Auxio          ★4.274    v4.1.5 (4-ago)    push 8-sep

PODCASTS
AntennaPod     ★8.153    3.12.1 (5-sep)    push 12-sep

ViMusic        ★9.480    el ancestro
```

## ⚖️ Qué no es esta guía

YouTube y YouTube Music tienen sus términos de servicio. Un cliente libre que consulta esos servidores puede chocar con ellos — esta guía no es un bufete: no dice «es legal» ni «no lo es». Dice repo, licencia (GPL en todas las fichas de hoy, verificadas en su página), versión y último push. La decisión de qué usas es tuya, con sus consecuencias.

Y la frase de siempre: aquí no hay APK de «Spotify premium gratis» ni mods de nada. Esa puerta tiene guía propia — la de tiendas — y termina siempre igual.

## 🧬 La genealogía: de ViMusic a la familia actual

Esta familia tiene árbol genealógico documentado, y conocerlo aclara media docena de nombres:

```
   la app que inventó el modelo: streaming de
   YouTube Music con cola, sin la app oficial.
   Hoy archivada — pero su idea parió todo esto.
   │
   ├── InnerTune (z-huang)
   │      el heredero directo: Material 3, biblioteca
   │      con cuenta, letras sincronizadas. Su último
   │      push fue en noviembre de 2025 — el creador
   │      se movió a otros proyectos y el repo duerme.
   │      │
   │      ├── OuterTune (su fork vivo más sólido)
   │      │      le añadió soporte de ARCHIVOS LOCALES
   │      │      junto al streaming. Versión 0.11.1
   │      │      el 6 de septiembre — el mes pasado
   │      │      todavía mostraba un tag de diciembre;
   │      │      el 14-sep la fila quedó corregida.
   │      │
   │      └── Metrolist (★12.789)
   │             la más instalada de la segunda
   │             generación: versión 13.7.0 del 7-sep
   │             con nightly propio. De las vivas,
   │             la de cadencia más regular.
   │
   └── SimpMusic (proyecto paralelo, mismo fondo)
          multiplataforma, con una línea de desarrollo
          muy activa: 2.0.0 el 28 de agosto y 2.1.0
          el 7 de septiembre.
```

Los parientes menores completan la foto: Harmony-Music (★3.081, multiplataforma de escritorio y móvil, con su última estable de diciembre de 2025), music-you (★220, la minimalista) y el caso curioso de InterTune (★12): un fork que se quedó anclado a la versión 0.10.1 de OuterTune «por su pantalla de reproducción», mantenido por su autor para uso propio y de quien lo encuentre útil. Su README recomienda, para quien busque mantenimiento activo, a Metrolist y a otro proyecto llamado ArchiveTune — de ese último, no se abrió repo en esta revisión.

## 🎧 Los clientes de streaming, ficha por ficha

### Metrolist — la de cadencia regular

https://github.com/mostafaalagamy/Metrolist

★12.789 · versión **13.7.0 (7 de septiembre)** · GPL · vivo. La segunda generación más estable del linaje InnerTune: versiones mensuales, nightly propio, y una base de usuarios que la puso entre las recomendaciones fijas de las comunidades del tema. Si vienes de InnerTune dormido, esta es la casa natural. Pulso de hoy: además de la 13.7.0, el repo publica **Nightly** — compilación diaria vista HOY, 14 de septiembre. *Mudanza certificada el 15-sep: la casa ahora es la organización MetrolistGroup (los enlaces viejos redirigen) — la dinastía completa en la Publicación 27.*

### OuterTune — la que une streaming y archivos

https://github.com/OuterTune/OuterTune

★5.390 · versión **0.11.1 (6 de septiembre)** · GPL · vivo. El fork que le agregó a la línea InnerTune la lectura de archivos locales: tu música descargada y el catálogo de streaming en el mismo reproductor. Material 3, tema dinámico. El mes pasado su último tag era de diciembre — esta guía lo registraba así; el 6-sep corrigió la foto. Así de rápido caduca un número.

### SimpMusic — la multiplataforma incansable

https://github.com/maxrave-dev/SimpMusic

★11.257 · **2.1.0 (7-sep)** y 2.0.0 (28-ago) · GPL · vivo. Dos versiones mayores en diez días. Su apuesta: el mismo fondo de YouTube Music con funciones extra — letras sincronizadas, audio sin pérdida declarado en su ficha, multiplataforma. La de desarrollo más inquieto de la familia.

### InnerTune — el ancestro que descansa

https://github.com/z-huang/InnerTune

★6.088 · push del 13 de noviembre de 2025 · GPL · sin archivar pero dormido: casi diez meses sin código nuevo, releases de 2024. Su lugar en la historia está garantizado — es la fuente de la que bebe media familia. Para instalar hoy, sus herederos hacen el trabajo.

### Harmony-Music y music-you — las alternativas

https://github.com/anandnet/Harmony-Music — ★3.081 · v1.12.2 (7-dic-2025) · multiplataforma (Android y escritorio), GPL. Ritmo lento pero proyecto serio.

https://github.com/DanielSevillano/music-you — ★220 · GPL · la opción minimalista de la familia, para quien quiere lo justo.

### InterTune — el caso de nicho

https://github.com/ItzSkyeYT/InterTune — ★12 · GPL · vivo por decisión de su autor: anclado a la versión 0.10.1 de OuterTune para conservar una pantalla de reproducción concreta. «Lo uso a diario y lo dejo público porque a unos pocos les sirvió», dice su README. La honestidad también es un rasgo de proyecto sano — y su recomendación de alternativas activas (Metrolist) lo confirma.

## 📻 NewPipe: la especie aparte

https://github.com/TeamNewPipe/NewPipe

★39.682 · v0.29.1 (15 de agosto) · push del 31-ago · GPL · vivo. NewPipe no es un cliente de YouTube Music: es un front-end libre de TODO el universo YouTube — vídeos, música, suscripciones, sin cuenta y sin publicidad. En música pide menos comodidad de biblioteca que los clientes de arriba; a cambio, cubre todo lo demás. Es de los proyectos más veteranos y respetados del software libre Android. Su canal histórico de distribución es F-Droid — la ficha de la tienda de esa familia aplica.

## 📂 Auxio: tu música, tus archivos

https://github.com/OxygenCobalt/Auxio

★4.274 · v4.1.5 (4 de agosto) · push del 8-sep · GPL · vivo. Para la música que YA tienes: reproductor local, racional, sin conectarse a ningún catálogo ni a ninguna nube. Si tu biblioteca vive en el teléfono (copiada con las herramientas de la guía de archivos de esta familia), esta es la ficha. Sin cuenta, sin streaming, sin sustos.

## 🎙️ AntennaPod: los podcasts

https://github.com/AntennaPod/AntennaPod

★8.153 · 3.12.1 (5-sep) · push del 12-sep · GPL · vivo. Gestor de podcasts completo: feeds RSS, descargas automáticas, velocidad variable, capítulos. No compite con ninguno de arriba: otra categoría que los hilos viejos mezclaban con la música en mil caracteres de ruido. Aquí, cada cosa en su cajón.

## 🆕 Los que faltaban (adición del 14 de septiembre)

### N-Zik — el hijo multilingüe de Kreate

https://github.com/N-Zik-Group/N-Zik · v7.5.1-f (1 de septiembre; a HOY 15-sep su releases baila con un dev v8.0.0) · tienda: https://appteka.store/app/4abr315772

Bifurcación multilingüe de Kreate declarada en su propio README: transmite y guarda en caché música de YouTube Music, con descargas sin conexión, letras sincronizadas palabra por palabra, visualizador, Discord Rich Presence, widgets y soporte Android Auto/TV/Automotive. Alterna la interfaz moderna N-Zik con la clásica de ViMusic — la genealogía viva de esta guía. Calidad Premium opcional entrando con cuenta de YouTube Music. Actualizaciones OTA. Honestidad del autor, incluida: desarrolla asistido por IA con revisión humana, lo declara, y recomienda alternativas más maduras (Metrolist, VIVI Music, RiPlay) si prefieres estabilidad probada. Ese aviso es señal de oficio, no debilidad. Pulso de cierre (14-sep, noche): el repo ya cocina la **v8.0.0-dev de HOY** — la estable de la tienda sigue siendo la 7.5.1-f.

### Gabi — el descargador de mil sitios

https://github.com/Hotaro26/gabi · v4.6.1 «YouTube 403 Fix» (1 de septiembre) · tienda: https://appteka.store/app/b4cr315682

Descargador de medios en Material 3 y Jetpack Compose que corre yt-dlp y gallery-dl: vídeos, audio y galerías de más de 1.000 sitios — YouTube, TikTok, Instagram, Twitter/X, Reddit, SoundCloud, Pixiv y la lista sigue. Descarga desde el portapapeles con un toque (botón Instant), comparte el enlace desde cualquier app y Gabi lo recoge, calidad hasta 1080p/máxima, extracción a MP3, vista previa con título y peso estimado, y temas con colores dinámicos Material You. El complemento natural de esta guía: para escuchar, los clientes de arriba; para llevar, Gabi.

Ambas se consiguen en Appteka — la tienda de la Publicación 01. El APK directo no se pega: la casa de cada app es su repo.

## 🚫 Lo que no se pega

APK de mods «premium» de cualquier app · listas copiadas de wikis de descarga · invitaciones de grupos · recetas de URLs. Cada quien abre el README del proyecto el día que lo usa — la casa de cada ficha está en los enlaces de abajo.

## ❓ Preguntas frecuentes

**¿Cuál instalo para empezar?**
Si tu música es catálogo: Metrolist (la de cadencia más regular) u OuterTune (si además tienes archivos locales). Si tu música es tu colección: Auxio. Si quieres todo YouTube sin cuenta: NewPipe. Si vives de podcasts: AntennaPod.

**¿Estas apps son legales?**
Esta guía no es un bufete y no dice eso. Dice qué proyecto existe, con qué licencia, y en qué estado. Los términos de cada servicio se leen en su casa.

**¿Por qué InnerTune sigue en las listas si está dormido?**
Porque es el ancestro vivo de media familia — y porque sus herederos (OuterTune, Metrolist) llevan su código adelante. Se ficha por historia y por quien lo use igual.

**¿Metrolist u OuterTune?**
Ambas vivas y activas este mes. Metrolist: cadencia mensual probada. OuterTune: archivos locales integrados. La que cubra tu uso — y las dos se abren el día que instalas, porque los números caducan.

**¿Y qué pasó con RiMusic?**
Archivada en julio de 2025. El hilo de 340 mil caracteres de abril la trataba como viva: inflar no verifica. Su ficha dice: historia.

**¿Estas apps consumen mucha batería?**
Lo que esta guía puede decir sin laboratorio: son reproductores, no juegos; el consumo depende del uso (descarga vs streaming). Lo que NO puede decir: números de batería — no se midieron aquí, y no se inventan.

**¿Hay versión para iPhone?**
De esta familia: Harmony-Music declara multiplataforma (escritorio y móvil). El resto de las fichas son Android. El ecosistema iOS libre de música es otro mapa.

**¿Discord o grupo para soporte?**
Cada proyecto tiene su casa de comunidad en su README — se abre ahí, no se pega aquí. Esta familia no usa canales de envío.

## 🔗 Enlaces

- Metrolist: https://github.com/mostafaalagamy/Metrolist
- OuterTune: https://github.com/OuterTune/OuterTune
- SimpMusic: https://github.com/maxrave-dev/SimpMusic
- InnerTune: https://github.com/z-huang/InnerTune
- Harmony-Music: https://github.com/anandnet/Harmony-Music · music-you: https://github.com/DanielSevillano/music-you · InterTune: https://github.com/ItzSkyeYT/InterTune
- NewPipe: https://github.com/TeamNewPipe/NewPipe
- Auxio: https://github.com/OxygenCobalt/Auxio
- AntennaPod: https://github.com/AntennaPod/AntennaPod
- N-Zik: https://github.com/N-Zik-Group/N-Zik · tienda: https://appteka.store/app/4abr315772
- Gabi: https://github.com/Hotaro26/gabi · tienda: https://appteka.store/app/b4cr315682
- Archivados: https://github.com/vfsfitvnm/ViMusic · https://github.com/fast4x/RiMusic

> La Bandita informa a partir de fuentes fechadas. El linaje también se verifica: los ancestros explican a los vivos.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: SimpMusic ★11.257, Metrolist ★12.789 (+Nightly), OuterTune ★5.390, InnerTune ★6.088, dev N-Zik v8.0.0. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Música FOSS — la tabla con pulso del 15-sep

(Cliente libre de YouTube = revisa términos; Spotify crackeado NO entra.)

- **Metrolist** ★12.789 · 13.7.0 — la más activa · **SimpMusic** ★11.257 · 2.1.0
- **InnerTune** ★6.088 (dormida) · **OuterTune** ★5.390 · v0.11.1
- **Harmony-Music** ★3.081 · **N-Zik** ★217 — HOY soltó su primer dev v8.0.0

**Especies aparte:** NewPipe ★39.699 (TODO YouTube) · Auxio ★4.274 (local) · AntennaPod ★8.153 (podcasts) · ViMusic ★9.480 (el ancestro).
*Fuente: pieza 8 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 08 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Cuál es mejor pa' YouTube Music? —El que tenga push esta semana. Hoy es Metrolist; por eso llevamos fechas.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# I verified free YouTube Music clients today: Metrolist leads on cadence (everyone's numbers)
**Reddit · ingles-US · fuente: pieza 8 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** Metrolist ★12,789 (13.7.0, Sep 7 + a Nightly from the 14th) is the most active; SimpMusic ★11,257, OuterTune ★5,390, Harmony-Music ★3,081, N-Zik ★217 (today it dropped its first dev v8.0.0). NewPipe ★39,699 and AntennaPod ★8,153 in the separate species.
## Tonight's table (Sep 15)

- **Metrolist** — ★12,789 · 13.7.0 (Sep 7) · Nightly from the 14th — **the most active** · github.com/mostafaalagamy/Metrolist
- **SimpMusic** — ★11,257 · 2.1.0 (Sep 7) — two major versions in ten days
- **InnerTune** — ★6,088 · push Nov 2025 — the living but sleeping ancestor
- **OuterTune** — ★5,390 · v0.11.1 (Sep 6) — it added local files to the line
- **Harmony-Music** — ★3,081 · v1.12.2 — mobile and desktop
- **music-you** — ★220 · **InterTune** — ★12 (a fixed fork for one niche)
- **N-Zik** — ★217 · v7.5.1-f (Sep 1) — **TODAY it dropped its first dev v8.0.0**

## The separate species

- **NewPipe** — ★39,699 · v0.29.1 — the free front-end to ALL of YouTube (not just Music)
- **Auxio** — ★4,274 · v4.1.5 — for music you ALREADY own: local, no catalog
- **AntennaPod** — ★8,153 · 3.12.1 (Sep 5) — podcasts: feeds, downloads, variable speed
- **ViMusic** — ★9,480 — the archived ancestor; half of today's family branched off it

**House notice:** a free client against Google's servers can run into their terms — here goes repo, version and date; the decision is each person's. Cracked Spotify doesn't get in: that's not free software.
> —Which is better for YouTube Music?
> —The one with a push this week. Today it's Metrolist; tomorrow, who knows — that's why we carry dates.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# FOSS music — clients with a repo and a pulse date (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 08 (Sep 15) · **Verified:** today, September 15, 2026

First things first, so nobody gets offended by free: YouTube and YouTube Music have their terms. A free client that talks to those servers can run into them — this guide isn't a law office: it states repo, version and date. The decision and its consequences are yours. And second: **cracked Spotify doesn't get in** — that's not free software, it's somebody else's gift wrap.

**Tonight's table (Sep 15):**
- **Metrolist** — ★12,789 · 13.7.0 (Sep 7) · Nightly from the 14th in sight — **the most active** · github.com/mostafaalagamy/Metrolist
- **SimpMusic** — ★11,257 · 2.1.0 (Sep 7) — two major versions in ten days · github.com/maxrave-dev/SimpMusic
- **InnerTune** — ★6,088 · push Nov 2025 — the living but sleeping ancestor (z-huang)
- **OuterTune** — ★5,390 · v0.11.1 (Sep 6) — the one that added local files to the line · github.com/OuterTune/OuterTune
- **Harmony-Music** — ★3,081 · v1.12.2 — cross-platform (mobile and desktop) · github.com/anandnet/Harmony-Music
- **music-you** — ★220 — the minimalist option · **InterTune** — ★12 — a fixed fork for one niche
- **N-Zik** — ★217 · v7.5.1-f (Sep 1) — Kreate's multilingual son; **TODAY it dropped its first dev v8.0.0** · github.com/N-Zik-Group/N-Zik

**The separate species:**
- **NewPipe** — ★39,699 · v0.29.1 — not a Music client: it's the free front-end to ALL of YouTube · github.com/TeamNewPipe/NewPipe
- **Auxio** — ★4,274 · v4.1.5 — for music you ALREADY own: local, rational, no catalog
- **AntennaPod** — ★8,153 · 3.12.1 (Sep 5) — podcasts: feeds, automatic downloads, variable speed
- **ViMusic** — ★9,480 — the ancestor; archived long ago, but half of today's family branched off it (full genealogy in the source piece)

**What doesn't get pasted here:** shared logins, APKs from Telegram channels and that kind of "shortcut". The house gives dated sources, not shortcuts with surprises.

The house meme:
> —Which one is better for YouTube Music?
> —The one with a push this week. Today the most active is Metrolist; tomorrow, who knows — that's why we carry dates.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
