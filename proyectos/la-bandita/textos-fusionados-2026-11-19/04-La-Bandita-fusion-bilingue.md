# Pieza 04 — Extensiones de los tres árboles: hubs vivos y la camada de impostores

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `8a00dac61b22` · ES-TG `99be2bd601dd` · EN-Reddit `eb8e3539fded` · EN-Discord `a8be7f2bd01c`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 04 — Extensiones de los tres árboles: hubs vivos y la camada de impostores

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🧩 Qué es una extensión (las tres capas)
├── 📗 Keiyoushi: el hub principal
├── 📘 Yūzōnō: anime y el estante «cursed»
├── 📙 Los demás almacenes vivos
├── 🧬 La convención KeiSource 1.6 (y el PR que la salvó)
├── 🗂️ Miyomi: el directorio de todo esto
├── 🎭 La camada de impostores
├── 🧭 Cómo leer un almacén sin tragarse nada
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Las extensiones son la capa que conecta un lector libre con las fuentes. No viven dentro de la app: viven en almacenes con dueño, y el estado de cada almacén cambia semana a semana. Esta guía revisó hoy — 14 de septiembre — todos los almacenes vivos del ecosistema, los que murieron con fecha, la convención técnica que mantiene todo funcionando, y una camada de repos impostores que apareció esta semana.

El estado de la mañana:

```
VIVOS (todos con actividad reciente)
Keiyoushi extensions        ★14.980   push 14-sep     el principal
Keiyoushi extensions-source ★4.678    vivo a 15-sep     el código
Yūzōnō anime                ★432      push 13-sep
Yūzōnō cursed               ★185      push 9-sep
cuong-tran/manga-repo       ★445      push 14-sep
mojuru/cursed-manga-repo    ★160      push 3-ago
Suwayomi/tachiyomi-extension ★327     push 12-sep  (para servidor)
Copymanga (comunidad CN)    ★2.753    v1.4.85
ZGQ-inc/source (CN)         ★1.268    megacolección

tachiyomiorg/extensions       ★546    ene-2024
stevenyomi/copymanga        ★1.918    feb-2024
```

## 🧩 Qué es una extensión (las tres capas)

```
La app         el lector (Mihon, Komikku, Tadami...)
El almacén     el lugar donde viven las extensiones
               (esta guía)
El índice      la receta que la app usa para leer
               el almacén — un archivo de instalación
```

La regla de esta familia de guías sobre la tercera capa: el índice no se pega. No porque sea secreto — está en el README de cada proyecto — sino porque pegar recetas de instalación en un post es exactamente el gesto que convierte una guía en un anzuelo. Quien quiera el índice, que lo lea en la casa del proyecto, el día que lo use.

## 📗 Keiyoushi: el hub principal

https://github.com/keiyoushi/extensions
Código: https://github.com/keiyoushi/extensions-source
Sitio: https://keiyoushi.github.io

El almacén de referencia del ecosistema Mihon: más de mil fuentes, bot que actualiza el índice a diario (los «Repository Update» del 12, 13 y 14 de septiembre se ven en su historial), y una comunidad de traductores que empuja el código cada día.

Su sitio web, abierto hoy, trae el aviso que resuelve media duda del mundo: si tu lista de extensiones sale vacía, o todas figuran «obsoletas», con el mensaje «Outdated app» — tu aplicación ya no es compatible con el almacén. Soportan Mihon, TachiyomiSY y Komikku. La solución no es buscar un espejo: es actualizar la app desde su repo.

Un detalle de transparencia: el almacén de binarios no declara licencia en su página (el código sí: Apache-2.0). Se dice tal cual — sin licencia visible, no inventada.

## 📘 Yūzōnō: anime y el estante «cursed»

Anime: https://github.com/yuzono/anime-extensions
Código sucesor: https://github.com/yuzono/kohi-den
Sitio: https://yuzono.github.io

El canal vivo de referencia para extensiones de anime en el árbol Tachiyomi — y junto a él, el código de la casa Kohi-den continúa vivo en la familia Yūzōnō (verificado el 14-sep). Y la regla que manda en esta familia: el mapa se anota con lo vivo — cada enlace se reabre el día que se usa.

Tercera pieza que pocos nombran: yuzono/cursed-manga-extensions — el estante de contenido adulto (NSFW), con actividad del 9 de septiembre. Se nombra porque existe y se actualiza; no se pega su índice ni se recomienda su contenido. Lo que cada quien lee es tema suyo y de su jurisdicción.

## 📙 Los demás almacenes vivos

**cuong-tran/manga-repo** — ★445, push del 14-sep. Extensiones para Komikku/Mihon y forks. De los almacenes independientes, el más activo.

**mojuru/cursed-manga-repo** — ★160, push del 3 de agosto. El segundo estante «cursed» del ecosistema. Mismo tratamiento: nombre sí, índice no.

**Copymanga-copy20** (LittleSurvival) — ★2.753, versión 1.4.85 del 8 de septiembre y «vomic» 1.4.4 del 4-sep. La comunidad china de fuentes para Mihon/Tachiyomi: su README enlaza sus grupos de comunidad. Fuentes centradas en copymanga y recursos chinos.

**ZGQ-inc/source** — ★1.268. Megacolección china que junta libros, imágenes, reglas y hasta fuentes de streaming. Se nombra como mapa del ecosistema chino; lo que hay dentro no se receta.

**Suwayomi/tachiyomi-extension** — ★327, push del 12 de septiembre. Caso aparte: no es para el teléfono, es la extensión para Suwayomi — el servidor de escritorio del ecosistema Tachiyomi (tu biblioteca corriendo en la PC, leída desde el navegador). Otra capa más: servidor.

**uchiyomi** — ★37, MPL-2.0, y dos versiones publicadas el 14-sep (v0.32.0 y v0.33.0). El recién llegado de esta capa: un lector self-hosted que corre como PWA en el navegador — webtoon-first, pensado para pantallas OLED — y que come las MISMAS extensiones de Mihon/Tachiyomi. Tu biblioteca en tu servidor, leída desde cualquier navegador, con el ecosistema de extensiones entero detrás. La capa servidor acaba de estrenar segunda casa — seguimiento abierto.

## 🧬 La convención KeiSource 1.6 (y el PR que la salvó)

Las extensiones no son archivos sueltos: siguen una convención técnica del ecosistema. La vigente se llama KeiSource, versión de librería 1.6. El documento de contribución del ecosistema (abierto hoy, 1.813 líneas) lo dice claro: las fuentes nuevas extienden KeiSource con libVersion 1.6, y la base antigua (HttpSource, 1.4) queda legado.

¿Por qué importa para quien solo lee? Porque cuando una app «no ve» las extensiones nuevas, casi siempre es esto: la app es vieja para la convención. Es la otra cara del aviso «Outdated app» de Keiyoushi.

El caso que confirmó la transición: el PR #448 de Animetail — «resolve 1.6+ extension loading» — abrió hoy y figura fusionado. Los lectores que no migran a tiempo se quedan fuera de los almacenes que adoptan la convención.

## 🗂️ Miyomi: el directorio de todo esto

https://miyomi.app
Código del sitio: https://github.com/miyomiorg/Miyomi

Un directorio comunitario que cataloga apps, almacenes de extensiones y guías del ecosistema entero — la portada se lee hoy, y su front-end es una aplicación web viva (sus recuentos internos no se pudieron re-contar hoy por esa misma razón: el catálogo vive en la sesión del navegador, no en un JSON público).

Su repo: ★189, licencia AGPL-3.0, con su propio código abierto. El proyecto declara que no aloja contenido y que no garantiza seguridad ni legalidad de terceros — un índice de índices, con la honestidad de quien sabe que catalogar no es auditar.

«Aprobado» en Miyomi significa «está en su catálogo hoy». No significa aval de nadie.

## 🎭 La camada de impostores

La búsqueda de esta semana detectó repos con el mismo traje: estrellas idénticas entre sí (115–120 en varios casos), actividad del mismo día, y títulos de anuncio clasificado — «Best Manga Reader App 2026», «Top Komikku Open Source Alternative», «Ultimate Multilanguage Hub for Usagi».

```
El traje del impostor
★ idénticas entre sí (115–120 en varios casos)
Título de propaganda, no de proyecto
Sin historial propio: nacieron el 13-sep
Nombre de proyecto conocido + palabra de venta
```

No son almacenes ni forks ni fuentes: son imanes de clics — y, razonablemente sospechar, de instalaciones envenenadas. La regla práctica que no falla: si el título suena a anuncio y las estrellas no cuadran con la historia del proyecto, no se abre, no se enlaza, no se instala.

## 🧭 Cómo leer un almacén sin tragarse nada

```
1. ¿Quién lo mantiene?
   Un bot de un org con historial > una cuenta
   sin cara que nació este mes.

2. ¿Desde cuándo empuja?
   Historial de commits de meses/años > actividad
   de una sola semana.

3. ¿El código está a la vista?
   extensions-source publicado > solo binarios.

4. ¿Su sitio avisa lo que no sabe?
   Keiyoushi avisa qué apps ya no soporta.
   El que confiesa límites merece más confianza
   que el que promete infinito.

5. ¿La instalación sale de la casa?
   El índice se lee en el README del proyecto,
   nunca en un post de terceros. Ni en este.
```

## ❓ Preguntas frecuentes

**¿Qué almacén uso con Mihon?**
Keiyoushi: lo declara su propio sitio (Mihon, TachiyomiSY, Komikku). Si tu lista sale vacía con «Outdated app», el problema es la versión de tu app.

**¿Y para anime?**
Yūzōnō anime-extensions es el canal vivo de referencia; el oficial de Aniyomi archivó en agosto de 2024 y Kohi-den en mayo de 2026.

**¿Los estantes «cursed» son peligrosos?**
Su riesgo no está en el mecanismo sino en el contenido y tu jurisdicción. Se nombran para completar el mapa; el índice de instalación no se pega en esta familia de guías, para ninguno.

**¿Sirven las extensiones de Keiyoushi en Usagi o Kotatsu?**
No: otro árbol, otro protocolo de parsers. Esos viven en sus propias casas y tienen guía propia.

**¿Un almacén «approved» en Miyomi es confiable?**
Es catalogado, no auditado. La diferencia es exactamente la del teléfono en la guía de contacto: está en la lista, no pasó el examen.

**¿Cada cuánto reviso que mi almacén siga vivo?**
Cada vez que algo deje de actualizarse. Por eso esta guía solo anota lo vivo — y cada enlace se reabre el día que se usa.

**¿Dónde reporto una extensión rota?**
En el repo del código de la extensión (para Keiyoushi: extensions-source), con versión de app, fuente y pasos. Los mantenedores responden mejor a pasos que a quejas.

## 🔗 Enlaces

- Keiyoushi: https://github.com/keiyoushi/extensions · https://github.com/keiyoushi/extensions-source · https://keiyoushi.github.io
- Yūzōnō: https://github.com/yuzono/tachiyomi-extensions · https://github.com/yuzono/anime-extensions · https://github.com/yuzono/cursed-manga-extensions · https://yuzono.github.io
- Almacenes: https://github.com/cuong-tran/manga-repo · https://github.com/mojuru/cursed-manga-repo
- Ecosistema chino: https://github.com/LittleSurvival/copymanga-copy20 · https://github.com/ZGQ-inc/source
- Servidor de escritorio: https://github.com/Suwayomi/tachiyomi-extension
- Miyomi: https://miyomi.app · https://github.com/miyomiorg/Miyomi

> La Bandita informa a partir de fuentes fechadas. El mapa va con lo vivo.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: 7 almacenes re-contados a HOY (Keiyoushi ★14.980, Yūzōnō ★432, manga-repo ★445). Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Extensiones de lectura — los tres árboles y sus hubs vivos

La app · el almacén · el índice. (El índice NO se pega: método sí, receta en su casa.)

- **Keiyoushi/extensions** — ★14.980 · push del 14 — EL hub Mihon (código: extensions-source ★4.678)
- **Yūzōnō anime** ★432 · cursed ★185 · **manga-repo** ★445 · cursed-manga-repo ★160
- **Copymanga-copy20** ★2.753 · **ZGQ-inc/source** ★1.268 · **Suwayomi/tachiyomi-extension** ★327

**Muertos con fecha:** tachiyomiorg/extensions (ene-2024) · stevenyomi (feb-2024).
**Nuevo:** uchiyomi ★37 — PWA self-hosted, dos releases el 14.
*Fuente: pieza 4 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 04 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Este almacén es confiable? —¿Tiene dueño, tiene push y tiene historia? Tres síes, adelante.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# Free reader extensions: today's living warehouses, the dated dead, and how to spot impostors
**Reddit · ingles-US · fuente: pieza 4 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** Extensions live in warehouses with an owner. Alive TODAY: Keiyoushi ★14,980 (push Sep 14), Yūzōnō anime ★432, manga-repo ★445, Copymanga ★2,753, ZGQ ★1,268. Frozen: tachiyomiorg (Jan 2024), stevenyomi (Feb 2024).
## The three layers (learned once)

The app (Mihon, Kototoro…) · the extension warehouse · the index the app downloads. **The index doesn't get pasted in posts: the method gets told; the recipe lives at each house.**

## The living warehouses, counted TODAY

- **Keiyoushi/extensions** — ★14,980 · push from Sep 14 — THE hub of the Mihon ecosystem (code: extensions-source, ★4,678)
- **Yūzōnō anime-extensions** — ★432 · push from Sep 13 · **cursed-manga-extensions** — ★185 · push from Sep 9
- **cuong-tran/manga-repo** — ★445 · push from Sep 14 · **mojuru/cursed-manga-repo** — ★160
- **Copymanga-copy20** — ★2,753 · v1.4.85 (Sep 8) · **ZGQ-inc/source** — ★1,268 (ecosystem map, not a recipe)
- **Suwayomi/tachiyomi-extension** — ★327 — its own case: it's for the server
- New: **uchiyomi** — ★37 · MPL-2.0 — a self-hosted reader as a PWA, two releases on Sep 14
- **Miyomi** (miyomi.app) — ★189 · AGPL-3.0 — the directory of all this

## The dead, with dates

tachiyomiorg/extensions — frozen Jan 2024 · stevenyomi/copymanga — Feb 2024. The map doesn't list them as alive.

**The technical convention:** KeiSource 1.6 — extensions follow a common packaging format; that's why one house serves many readers.

**Impostors:** newborn repos wearing serious projects' names. Named without linking — the real project doesn't staple a year onto its name.
> —Is this warehouse trustworthy?
> —Owner, push, history? Three yeses, go ahead.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Extensions — the three trees and their living hubs (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 04 (Sep 15) · **Verified:** today, September 15, 2026

Extensions are the layer that connects your free reader to the sources. They don't live in the app: they live in warehouses with an owner — and each warehouse's state changes week to week. This is the Sep 15 cutoff.

**The three layers (learn this once):** the app (Mihon, Kototoro…) · the extension warehouse · the index the app downloads. The index does NOT get pasted here — we tell the method; the recipe lives at each home.

**The living warehouses, counted TODAY:**
- **Keiyoushi/extensions** — ★14,980, push from Sep 14 — THE hub of the Mihon ecosystem (a bot updates the index daily) · code: keiyoushi/extensions-source, ★4,678
- **Yūzōnō anime-extensions** — ★432, push from Sep 13 — the living anime channel (and Kohi-den's code stays alive in the family)
- **Yūzōnō cursed-manga-extensions** — ★185, push from Sep 9
- **cuong-tran/manga-repo** — ★445, push from Sep 14 — the most active independent (Komikku/Mihon)
- **mojuru/cursed-manga-repo** — ★160, push from Aug 3 — the second "cursed" shelf
- **Copymanga-copy20** — ★2,753 · v1.4.85 (Sep 8) — the Chinese sources community
- **ZGQ-inc/source** — ★1,268 — Chinese mega-collection (ecosystem map, not a recipe)
- **Suwayomi/tachiyomi-extension** — ★327 — its own case: it's for the server, not the phone

**The dead, with dates (so nobody installs them):** tachiyomiorg/extensions — frozen Jan 2024 · stevenyomi/copymanga — Feb 2024. The map doesn't list them as alive; the Register does count them.

**What's new:** uchiyomi — ★37, MPL-2.0 — a self-hosted reader that runs as a PWA, with two releases on Sep 14 (v0.32.0 and v0.33.0).

**The technical convention (KeiSource 1.6):** extensions follow a common packaging format — that's why one house can serve many readers. The PR that saved it is in the repo's history.

**Miyomi** (miyomi.app) — ★189, AGPL-3.0 — the directory of all this; its repo open, its catalog live in the browser.

**This cutoff's impostors:** newborn repos wearing serious projects' names. Named without linking: it's SEO to farm downloads. The real project doesn't need to staple a year onto its name.

The house meme:
> —Is this warehouse trustworthy?
> —Does it have an owner, a push and a history? Three yeses, go ahead.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
