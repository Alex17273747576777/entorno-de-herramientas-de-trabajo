# Pieza 13 — Rama Aniyomi: manga y anime en un solo lector — Aniyomi, Animetail y Tadami

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `42fa17ede33f` · ES-TG `d95698671744` · EN-Reddit `5dbd81e2f528` · EN-Discord `e75af386e9de`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 13 — Rama Aniyomi: manga y anime en un solo lector — Aniyomi, Animetail y Tadami

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌳 El árbol de esta rama
├── 🎬 Aniyomi — la rama madre
├── 🦋 Animetail — el fork que se declara oficial
├── 🌗 Tadami — el tercero en la conversación
├── 🌲 La red completa de forks (revisada el 14-sep)
├── 🧩 Las extensiones de anime: dónde viven hoy
├── ⚖️ Cuándo tiene sentido esta rama
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

El árbol Tachiyomi/Mihon tiene una rama entera dedicada al anime: lectores que hacen las dos cosas — leer manga y ver anime — desde la misma aplicación. Esta guía es el mapa de esa rama, abierta HOY, 14 de septiembre, repo por repo:

```
Aniyomi     ★7.683   v0.18.2.1 (14-sep)     push del 14-sep  la rama madre
Animetail   ★578     v0.20.4.0 (5-ago)      push 7-sep    fork respaldado
Tadami      ★260     v0.62 (12-sep)         push 13-sep   fork — viva (rectificación al pie)
```

Las tres viven. Y la noticia del día la da la madre: Aniyomi publicó DOS versiones ese mismo 14 de septiembre, después de once meses sin releases — el mismo día en que su descendiente Animiru hacía lo propio en su rama. La familia entera se movió hoy. El criterio para elegir entre ellas no cambia: el uso real y el repo vivo, como con todo el árbol.

## 🌳 El árbol de esta rama

```
Aniyomi (la rama madre: manga + anime)
   ├── Animetail     se declara «Official fork of Aniyomi»
   ├── Tadami        manga + anime + ranobe (novelas ligeras)
   └── Animiru       la versión SOLO anime
                     (tiene guía propia: siguiente pieza)
```

Un apunte de linaje que se lee en la API: Animetail y Tadami figuran como forks (campo fork = true, padre visible). Animiru también desciende de Aniyomi — pero su historia está en la pieza de su rama.

## 🎬 Aniyomi — la rama madre

https://github.com/aniyomiorg/aniyomi

```
Qué es:       «An app for manga and anime» — el lector
              del linaje Tachiyomi con reproductor de anime
              integrado (basado en mpv)
Licencia:     Apache-2.0
Versiones:    0.18.2.1 y 0.18.2.0 — publicadas el 14-sep
              (la anterior estable: 0.18.1.2, del 28-oct-2025)
Push:         14 de septiembre de 2026 (día de la verificación)
Android:      8.0+ (según su ficha de descarga)
Trackers:     MyAnimeList, AniList, Kitsu, MangaUpdates,
              Shikimori, Simkl y Bangumi (su README)
Organización: aniyomiorg — mantiene además su sitio web,
              el host de previews (aniyomi-preview)
              y la documentación de forks
```

Hasta esta mañana, su última versión estable era de octubre de 2025 — once meses de silencio de releases, con la duda flotando de si la rama madre seguía en pie. La duda quedó resuelta HOY: v0.18.2.0 y v0.18.2.1 salieron el mismo día en que su descendiente Animiru también publicaba. Los empujones de código de este mes no eran humo: eran preparación. La lección se cumple otra vez en esta colección: un repo callado no es un repo muerto — y lo único que lo dice con certeza es la página de releases, abierta el día en que se decide.

Su organización hizo además algo poco común: mantiene una página que lista los forks conocidos del proyecto — el índice donde Animiru (rama siguiente de esta serie) figura registrado. Un proyecto que cartografía a sus hijos es un proyecto con memoria.

## 🦋 Animetail — el fork que se declara oficial

https://github.com/Animetailapp/Animetail

```
Qué es:       «Official fork of Aniyomi» (su descripción)
Licencia:     Apache-2.0
Versión:      0.20.4.0 (5 de agosto de 2026)
Push:         7 de septiembre de 2026
Curiosidad:   su numeración sigue a Mihon (0.20.4),
              porque sincroniza el núcleo del lector manga
              con el tronco — su historial de cambios
              lo documenta
Host de pruebas: Animetail-preview (★75)
```

Animetail es el fork que tomó la decisión técnica más interesante de la rama: en lugar de esperar a Aniyomi, trae el núcleo actualizado del lector de manga (el de Mihon) dentro del reproductor de anime — por eso sus versiones comparten número con Mihon, y la página de forks de Aniyomi le añade una función concreta: soporte Cast. Y hay novedad de estatus verificada HOY: la organización de Aniyomi lo lista en su página de «forks respaldados», junto a Animiru. La etiqueta «Official» ya no es solo suya: la firma el original. La API confirma el linaje por su lado: fork registrado, padre aniyomiorg.

Publica checksums SHA-256 por arquitectura en sus releases — la buena práctica de siempre: el archivo y su huella, juntos.

## 🌗 Tadami — el tercero en la conversación

> **Acta (15-sep):** la casa original — andarcanum/Tadami-Aniyomi-fork — devuelve 404 desde la reverificación de HOY. Quedan su sitio oficial (tadami.qzz.io) vivo y forks huérfanos. Método de la casa: **el espejo no es el repo** — Tadami no se receta hasta que su casa diga dónde vive. Lo anotado aquí queda como historia fechada.

> **Rectificación (15-sep, noche):** el dueño constató la casa viva y el verificador re-abrió en vivo: **andarcanum/Tadami-Aniyomi-fork responde — ★260, v0.62 (12-sep), push del 13-sep. VIVA.** El 404 de la tarde fue real, pero de otra puerta: el slug `anandnet/…` que el censo arrastraba — y el error fue atribuirle la caída a esta casa. Y noticia nueva del corte: el proyecto estrenó organización propia — **tadamiorg/tadami** (★56, con carril de releases propio: v1.9.3 del 26-jul). Dos casas del mismo nombre: la palabra sobre cuál manda la tiene el dueño.

https://github.com/andarcanum/Tadami-Aniyomi-fork *(viva — rectificación arriba)*

```
Qué es:       «An app for manga, anime and ranobe» —
              el que sumó las novelas ligeras a la fórmula
Licencia:     Apache-2.0
Versión:      0.62 (12 de septiembre de 2026)
Push:         13 de septiembre de 2026
Ritmo:        tres versiones en un mes (0.60 → 0.62)
Estrellas:    258 — el más joven y el más pequeño
```

Tadami es la apuesta fresca: fork de Aniyomi que añade lectura de ranobe (novelas ligeras) y se mueve rápido — versiones del 20 de agosto, 29 de agosto y 12 de septiembre. Su tamaño pequeño es su ficha honesta: comunidad joven, desarrollo personal, cadencia alta. Para saber si va en serio, el método de siempre: abrir sus issues, mirar si el autor responde, y seguirle el rastro unas semanas. Lo que hoy es verificable: vive, empuja, y publica versiones con fecha reciente.

## 🌲 La red completa de forks (revisada el 14-sep)

Esta rama no son solo tres fichas: la red de forks de las tres casas se revisó el 14-sep, fork por fork, en la API de GitHub. El panorama, con la trastienda abierta:

```
aniyomi     1ª página de forks más nuevos: 100
            la mayoría: copias personales ★0 con la
            descripción de fábrica — sin cambios propios

Animetail   30 forks — todos «no oficiales», ★0-1
Tadami      31 forks — 6 renombrados con propósito
```

**Los que sí traen algo propio (verificado hoy):**

- **Kuro** (Zykrave/aniyomi-Kuro, ★21) — «una biblioteca multimedia y reproductor rediseñados al moderno» según su README: el fork más seguido de la red, v1.0.0 del 13 de agosto. Rebrand completo, no parches.
- **MeMedia** (FunMan1995/MeMedia, v0.21.2 del 22-ago) — la idea más curiosa de la red: lector manga de Mihon + reproductor anime de Aniyomi en una sola app, con pestañas separadas que Mihon no tiene. Su README explica el «por qué de este fork» con bibliotecas independientes por medio.
- **aniyomi-revived** (Blackyfi, ★1) — «fork actualizado para mantenerse al día»: dos releases el mismo 3 de septiembre (v0.18.1.32/33). Cumple lo que promete el nombre.
- **anteiku** (Heavenofficial) — la variante «manga, anime y películas».
- En Tadami: **mugen** (h80r, v0.72.81 del 1-sep), **Nattyflix** (anime+manga+películas) y un fork de localización que promete «arreglo de inglés y overhaul de gestos» del lector de novelas (sin releases aún). Y dato de lealtad: un fork de Tadami publicó su v0.62.0 el mismo HOY que el padre — la red sigue los releases en vivo.
- En Animetail, el único con función propia declarada: un fork que añade **Discord Rich Presence** al re-enfocar la app.

El resto de la red son copias sin funciones propias: no se anotan — el mapa es de lo que vive y aporta.

**La expedición profunda (la red entera, 649 miembros, caminada el 14-sep):** el bosque no termina en la primera página. La red completa de Aniyomi — que es la misma de Animiru, familia por API — se caminó miembro a miembro: 93 cargan nombre propio. En la capa profunda, las rarezas que valen mención: **kikuyomi**, un fork de Aniyomi para escuchar **audiolibros**; **jishoyomi**, para estudiar con el anime (herramientas de aprendizaje); **Anichibi**, el fork lúdico con versiones V2 y V3; y un árbol dentro del árbol: **Kuukiyomi**, proyecto personal con siete miembros de red propios. El resto de la capa profunda son copias con README de fábrica: fuera del mapa. Con esa vara, el mapa queda completo.

## 🧩 Las extensiones de anime: dónde viven hoy

El capítulo delicado de esta rama son sus extensiones. El mapa de hoy:

```
Yūzōnō anime            ★428 · push 13-sep
   hoy, el canal vivo de referencia:
   github.com/yuzono/anime-extensions

Yūzōnō / kohi-den       vivo, verificado el 14-sep
   el código de la casa Kohi-den continúa
   en la familia Yūzōnō:
   github.com/yuzono/kohi-den

Nuevos almacenes dedicados      push del 14-sep
   existen repos nuevos centrados en los clientes
   anime de la familia Anikku/AniZen — van en la
   pieza de esa rama, donde les toca.
```

La regla de la casa: los índices de instalación no se pegan — se leen en el README de cada almacén, el día que se usan. Lo que esta guía da es el mapa: quién vive, quién murió, con fecha.

## ⚖️ Cuándo tiene sentido esta rama

Con el criterio de la casa (uso real, unicidad, madurez, propósito propio):

```
¿Ves anime Y lees manga, y quieres una sola app?
   → El terreno natural de esta rama: las tres
     fichas cubren ese caso, con estilos distintos.

¿Solo anime?
   → Esta rama es más de lo que necesitas:
     la pieza siguiente (Animiru/Anikku) es la
     rama de anime puro.

¿Solo manga?
   → El tronco (Mihon y familia, guía propia)
     pesa menos y sobra menos.

¿Novelas ligeras además?
   → Tadami las trae de fábrica; Reikai (rama
     J2K) es la otra vía manga+novelas.
```

Ninguna de las tres fichas es «la mejor». La buena es la que cubre tu uso, con repo vivo el día que instales — y esa comprobación se hace abriendo su releases ese día.

## ❓ Preguntas frecuentes

**¿Aniyomi dejó de desarrollarse?**
La pregunta quedó respondida el 14 de septiembre: v0.18.2.0 y v0.18.2.1, publicadas el 14 de septiembre tras once meses sin releases — con el código empujándose durante el mes. La organización sigue activa. Cuando dudes de un proyecto, el reloj es su página de releases, abierta ese día.

**¿Animetail es «oficial de verdad»?**
Triple verificación: lo declara su descripción, la API confirma el parentesco directo y —desde hoy verificado— la página de forks respaldados de aniyomi.org lo lista junto a Animiru, con soporte Cast entre sus funciones. Su historial (migrar el núcleo de Mihon, releases con checksums) es de proyecto serio.

**¿Por qué las versiones de Animetail llevan el número de Mihon?**
Porque sincroniza el lector de manga con el tronco: es su propuesta de valor — anime + lector actualizado sin esperar a nadie.

**¿Tadami no es demasiado pequeño?**
Es joven. Pequeño no es inválido: es la puerta de madurez pendiente de demostrar. Con cadencia de releases de esta semana, va camino.

**¿Las extensiones del almacén viejo todavía sirven?**
Las que ya instaladas, siguen; las nuevas, salen por los almacenes vivos. El oficial paró en agosto de 2024 — la fecha manda.

**¿Animiru entra en esta guía?**
Comparte abuelo, pero su rama tiene pieza propia (la siguiente): allí vive su ficha completa, con las dos versiones que publicó el 14-sep.

## 🔗 Enlaces

- Aniyomi: https://github.com/aniyomiorg/aniyomi · https://github.com/aniyomiorg/aniyomi-preview
- Animetail: https://github.com/Animetailapp/Animetail · https://github.com/Animetailapp/Animetail-preview
- Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- Destacados de la red: https://github.com/Zykrave/aniyomi-Kuro · https://github.com/FunMan1995/MeMedia · https://github.com/Blackyfi/aniyomi-revived
- Extensiones de anime vivas: https://github.com/yuzono/anime-extensions · sucesión de Kohi-den: https://github.com/yuzono/kohi-den
- Forks respaldados por Aniyomi: https://aniyomi.org/forks/
- Archivados (historia): https://github.com/aniyomiorg/aniyomi-extensions · https://github.com/kohi-den/extensions-source

> La Bandita informa a partir de fuentes fechadas. Manga y anime en la misma mano — con el repo vivo por delante de la etiqueta.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Aniyomi ★7.683 + acta y rectificación Tadami. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Rama Aniyomi — manga y anime en una mano

- **Aniyomi** ★7.683 · v0.18.2.1 (14-sep) — DOS releases el 14 tras 11 meses de silencio · github.com/aniyomiorg/aniyomi
- **Animetail** ★577 · v0.20.4.0 (el que se declara «oficial»; pruebas: Animetail-preview ★75)
- **Tadami** ★260 · v0.62 — VIVA (404 de la tarde era otro slug; nueva org: tadamiorg, ★56)

Red de forks: Kuro ★21 («biblioteca rediseñada») · aniyomi-revived ★1 (dos releases el 3-sep). Extensiones: Yūzōnō anime ★432 (el código de Kohi-den vive en la familia).

¿Cuándo? Una app pa' las dos cosas. Anime puro: pieza 14.
*Fuente: pieza 13 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 13 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Aniyomi volvió o era rumor? —Volvió con dos versiones el mismo día. El rumor era que había muerto.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# The Aniyomi branch: manga and anime in one hand — Aniyomi came back with 2 releases the same day, Animetail and Tadami alive
**Reddit · ingles-US · fuente: pieza 13 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** Aniyomi ★7,683 (v0.18.2.1 from Sep 14) broke 11 months of silence with two releases; Animetail ★577 (v0.20.4.0) and Tadami ★260 (v0.62, alive — the 404 belonged to another slug) complete the branch that reads and watches.
## The table (counted TODAY, Sep 15)

- **Aniyomi** — ★7,683 · v0.18.2.1 (Sep 14) · push from the 14th — **the mother branch**; its two releases on the 14th broke eleven months of silence · github.com/aniyomiorg/aniyomi
- **Animetail** — ★577 · v0.20.4.0 — the fork that declares itself "official" and pulled the Mihon core inside · tests: Animetail-preview (★75)
- **Tadami** — ★260 · v0.62 (Sep 12) · push from the 13th — **ALIVE** (rectified with a record: the afternoon 404 belonged to another slug) · new organization: tadamiorg/tadami (★56)

## The fork network, what matters

Most are personal copies at ★0; the living ones with a proposal: **Kuro** (Zykrave, ★21) — "a redesigned media library" — and **aniyomi-revived** (Blackyfi, ★1) — two releases on the very same Sep 3.

**The branch's extensions:** Yūzōnō anime — ★432 · push from Sep 13; Kohi-den's code stays alive in the family. The Kohi-den host's fall (2026) left the lesson: **the house lives, the host doesn't always.**

**When does this branch make sense?** If you want ONE app for manga and anime without fighting two libraries. Pure, fine anime: piece 14 is your street.
> —Did Aniyomi come back or was it a rumor?
> —It came back with two versions the same day. The rumor was that it had died.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# The Aniyomi branch — manga and anime in one hand (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 13 (Sep 15) · **Verified:** today, September 15, 2026

The branch that does both things: read AND watch. Tonight's cutoff:

**The table (counted TODAY, Sep 15):**
- **Aniyomi** — ★7,683 · v0.18.2.1 (Sep 14) · push from the 14th — **the mother branch**; its two releases on the 14th broke eleven months of release silence · github.com/aniyomiorg/aniyomi
- **Animetail** — ★577 · v0.20.4.0 — the fork that declares itself "official" and pulled the Mihon core inside · test host: Animetail-preview (★75)
- **Tadami** — ★260 · v0.62 (Sep 12) · push from Sep 13 — **ALIVE** (rectified with a record: the afternoon 404 belonged to another slug) · and the project's new organization: tadamiorg/tadami (★56)

**The fork network, what matters:** most are personal copies at ★0; the living ones with a proposal: **Kuro** (Zykrave, ★21) — "a redesigned media library" — and **aniyomi-revived** (Blackyfi, ★1) — two releases on the very same Sep 3.

**This branch's extensions live at:** Yūzōnō anime — ★432, push from Sep 13 — and Kohi-den's code stays alive in the family (verified in its day). The Kohi-den host's fall (2026) left the lesson: the house lives, the host doesn't always.

**When does this branch make sense?** If you want ONE app for manga and anime without fighting two libraries. If you want pure, fine anime, piece 14 is your street.

The house meme:
> —Did Aniyomi come back or was it a rumor?
> —It came back with two versions on the same day. The rumor was that it had died.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
