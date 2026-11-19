# Pieza 14 — Rama anime puro: Animiru y Anikku — los clientes que se quitaron el manga de encima

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `ca563ebce4ad` · ES-TG `ec6673a77078` · EN-Reddit `26b9785e0f49` · EN-Discord `88ec4e6172d9`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 14 — Rama anime puro: Animiru y Anikku — los clientes que se quitaron el manga de encima

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌳 El árbol de esta rama
├── 🍥 Animiru — el anime-only que nació de Aniyomi
├── 📺 Anikku — el anime de la organización Komikku
├── 🌲 La red de forks de los dos (revisada el 14-sep)
├── 🧩 Las extensiones de estos clientes (novedad del día)
├── ⚖️ Anime puro o anime+manga: cómo decidir
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Hay una rama del árbol anime que tomó la decisión contraria a la de Aniyomi: en vez de añadir manga al reproductor, le QUITARON el manga para quedarse solo con el anime. Esta guía abrió el 14 de septiembre, las casas de esa rama:

```
Animiru   ★864    v0.20.0.1 (14-sep)   fork anime-only de Aniyomi
Anikku    ★1.028  v0.2.0 (11-sep)           anime de la organización Komikku
```

Dato del día: **Animiru publicó dos versiones esta misma mañana** (0.20.0.0 y 0.20.0.1). Y en el frente Anikku, hay almacenes de extensiones dedicados a él con actividad de hoy. La rama pequeña del árbol es, esta semana, la que más se movió.

## 🌳 El árbol de esta rama

```
Aniyomi (manga + anime)
   └── Animiru      le quitó el manga: SOLO anime
         └── AnimiruTv  variante para Android TV

Komikku (manga, con organización)
   └── Anikku       su cliente de anime
         └── anikku-preview   el canal de pruebas
```

Dos caminos distintos al mismo destino: un cliente de anime libre. Animiru salió de la rama Aniyomi; Anikku salió de la organización Komikku. No son competencia directa por nacimiento — son dos familias que llegaron al mismo mostrador.

## 🍥 Animiru — el anime-only que nació de Aniyomi

https://github.com/Quickdesh/Animiru

```
Qué es:       fork de Aniyomi que elimina la parte
              de manga para ser una app SOLO de anime
Licencia:     Apache-2.0
Versiones:    0.20.0.1 y 0.20.0.0 — publicadas el 14-sep
              (la anterior: 0.19.8.1, del 9-ago)
Android:      8.0+ (su ficha de descarga)
Reproductor:  construido sobre mpv, configurable
Trackers:     MyAnimeList, AniList, Kitsu, Shikimori,
              Simkl, Bangumi y Hikka (su README)
Estrellas:    862
```

Tres cosas hacen a Animiru especial dentro del árbol:

**Uno: el registro oficial.** Animiru figura listado en la página de forks que mantiene la propia organización de Aniyomi (aniyomi.org/forks/Animiru). No es un clon que apareció de la nada: es un fork registrado en el índice del proyecto madre — la diferencia entre la casa reconocida y la caseta sin dueño.

**Dos: la decisión de diseño.** Le quitaron el manga a propósito. Menos app, menos peso, un solo trabajo bien hecho. Para quien nunca lee manga, es exactamente la herramienta correcta — y para quien lee ambos, es la mitad de una solución.

**Tres: el ritmo de hoy.** Dos versiones publicadas la misma mañana de hoy. Sea lo que sea que está ajustando su autor, lo está haciendo ahora mismo — el repo se siente vivo desde la portada.

Su estirpe tiene ramita propia: existe AnimiruTv (fork para Android TV) y copias menores sin actividad. La ficha canónica es Quickdesh/Animiru — el que mantiene el ritmo y el registro.

## 📺 Anikku — el anime de la organización Komikku

https://github.com/komikku-app/anikku

```
Qué es:       «Free and open source anime watcher
              for Android» — el cliente de anime de
              la organización que mantiene Komikku
Licencia:     Apache-2.0
Versión:      0.2.0 (11 de septiembre de 2026)
Push:         14-sep (día de la verificación)
Canal de pruebas: anikku-preview (★112, push 10-sep)
Estrellas:    1.028 — la mayor de esta rama
```

Anikku es la apuesta institucional: no es un proyecto de una persona, es la pieza de anime de una organización que ya demuestra oficio con Komikku (uno de los lectores manga más activos del ecosistema, ★4.717). Su versión 0.2.0 de esta semana la pone en la fase joven pero patrocinada: hay org detrás, hay canal de previews, hay traducciones comunitarias.

El nombre, cuidado con el parecido: existe una familia entera de clientes con raíz «Ani-» (Aniyomi, Animetail, Animiru, Anikku, y el rebautizado AniZen, que tiene su propia guía). Cada uno con su repo y su dueño. El nombre no hereda nada; el repo sí explica todo.

## 🌲 La red de forks de los dos (revisada el 14-sep)

Lo vivo y con propuesta en las dos redes (revisado el 14-sep, fork por fork):

- **AnimiruTv** sigue siendo la variante canónica para Android TV.
- **Vidi** es la única variante de Animiru con builds propios y frescos: v0.19.12, del 4 de septiembre.
- En la red de anikku: el **puerto a macOS** sigue en obra (push de agosto) y **anikku-pineapple** teje con Houri en la rama manga — el mismo autor en las dos ramas de la casa Komikku (ver la guía SY/Komikku).

El resto de las dos redes (32 y 68 forks) son copias sin funciones propias declaradas: no se anotan. El mapa es de lo que vive y aporta — y el día que alguien aporte, entrará con fecha.

## 🧩 Las extensiones de estos clientes (novedad del día)

Un cliente de anime sin fuentes no hace nada — y esta semana la rama estrenó almacenes propios. Verificados hoy:

```
salmanbappi/extensions-repo      ★40 · push de HOY (re-verificado 15-sep)
   «Repositorio de extensiones de anime
   dedicado a Anikku» — según su descripción

salmanbappi/aniyomi-extensions   ★15 · push 12-ene
   «Extensiones para Anikku / Aniyomi & forks»
```

El detalle que conecta guías: el autor de esos almacenes es el mismo desarrollador de AniZen — el rebrand de Anikku Mod que tiene guía propia en esta colección. Hay un ecosistema pequeño construyéndose alrededor del cliente de la organización Komikku: cliente, canal de previews, y almacenes de extensiones. Eso, en pañales, es cómo nace una rama seria.

El contexto histórico, con fecha: el almacén oficial de anime de Aniyomi archivó en agosto de 2024 y el comunitario (Kohi-den) en mayo de 2026 — el que estos repos nuevos existan es la respuesta del ecosistema a esos vacíos. Los índices de instalación no se pegan aquí: se leen en el README de cada almacén, el día que se use.

## ⚖️ Anime puro o anime+manga: cómo decidir

```
¿Ves anime y NUNCA tocas el manga?
   → Animiru o Anikku: la app pesa menos,
     la interfaz no te estorba con la mitad
     que no usas.

¿Ves anime y lees manga, con distinto ánimo?
   → La rama anterior (Aniyomi/Animetail/Tadami):
     las dos cosas en una mano.

¿Anime en la tele?
   → AnimiruTv existe — con la advertencia de
     siempre: fork pequeño, verifícalo el día
     que lo pruebes.

¿Ya usas Komikku para manga?
   → Anikku tiene la lógica del mismo equipo:
     la familia se siente en la interfaz.
```

Las dos fichas de hoy pasan las puertas de la casa: uso real (comunidades activas), unicidad (anime puro es su nicho), madurez (releases de esta semana, estructura de org en un caso) y propósito propio (quitar el manga ES el propósito — no es cosmética).

## ❓ Preguntas frecuentes

**¿Animiru es «Aniyomi sin manga» nada más?**
Su base es Aniyomi y su diferencia es esa — pero suma detalles propios (el set de trackers incluye Simkl y Hikka, el reproductor mpv va afinado en cada versión). Dos versiones en una mañana dicen que el «nada más» está siendo trabajado.

**¿Por qué Anikku va por 0.2 si Komikku va por 1.14?**
Son apps distintas: el manga lleva años de ventaja. 0.2 con organización detrás es una fase normal de un proyecto joven — el canal de previews y las traducciones son señales de estructura, no de juguete.

**¿Anikku y AniZen son lo mismo?**
Familia, no gemelos: AniZen se declara rebrand de «Anikku Mod» (su guía lo cuenta con fechas). Anikku es el original de la organización. Mismo linaje declarado, casas distintas.

**¿Qué extensión le va a Animiru?**
Las del ecosistema de Aniyomi — es su herencia — con el mapa vivo de la guía anterior. Para Anikku, sus almacenes dedicados de arriba. En ambos casos: el índice se lee en la casa del almacén, no en un post.

**¿Tienen versión para TV o escritorio?**
AnimiruTv (TV, fork pequeño). Anikku: no se le conocen variantes — su org se concentra en móvil. Lo que exista mañana, dirán sus organizaciones.

**¿Cuál de las dos fichas va más rápido?**
Animiru, sin discusión: dos releases hoy. Pero la velocidad no es el criterio — el repo vivo sí, y las dos viven.

## 🔗 Enlaces

- Animiru: https://github.com/Quickdesh/Animiru · registro de forks de Aniyomi: https://aniyomi.org/forks/Animiru/
- AnimiruTv: https://github.com/Znabil/AnimiruTv
- Anikku: https://github.com/komikku-app/anikku · pruebas: https://github.com/komikku-app/anikku-preview
- Almacenes nuevos: https://github.com/salmanbappi/extensions-repo · https://github.com/salmanbappi/aniyomi-extensions
- Guía cruzada: rama Aniyomi/Animetail (pieza 13) · AniZen (pieza 11) de esta colección

> La Bandita informa a partir de fuentes fechadas. Quitar el manga también es un propósito — y esta semana lo publicó dos veces.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Animiru ★864, extensions-repo push de HOY. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Rama anime puro — Animiru y Anikku: dos escuelas

- **Animiru** ★864 · v0.20.0.1 (14-sep) — proyecto de una persona, cadencia rápida · github.com/Quickdesh/Animiru
- **Anikku** ★1.032 · v0.2.0 (11-sep) · r8932 HOY — la apuesta institucional de la org Komikku (pruebas: anikku-preview ★112)

Novedad extensiones: salmanbappi/extensions-repo ★40 (push HOY) · aniyomi-extensions ★15.

¿Elección? Manga en Mihon/Komikku + anime de vez en cuando → Anikku. Anime como servicio completo → Animiru. Ninguna es eterna: la casa decide con fechas.

Impostores: build con el nombre y otra firma = cebo.
*Fuente: pieza 14 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 14 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Cuál es mejor, Animiru o Anikku? —¿Panas solos o con organización? Ambos empujan esta semana.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# Pure anime: Animiru vs Anikku, two schools verified today (with cadence and a house)
**Reddit · ingles-US · fuente: pieza 14 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** The branch that removed the manga from the player: Animiru ★864 (v0.20.0.1, Sep 14, one dev's fast cadence) vs Anikku ★1,032 (v0.2.0 from Sep 11 + r8932 TODAY, the Komikku org's institutional bet).
## Two houses, two schools

- **Animiru** — ★864 · v0.20.0.1 (Sep 14) — the anime-only born from Aniyomi; it inherits extensions from the warehouse piece 13 details (Yūzōnō anime) · github.com/Quickdesh/Animiru
- **Anikku** — ★1,032 · v0.2.0 (Sep 11) · **r8932 in sight TODAY** — the Komikku organization's anime piece (the same one sustaining Komikku) · tests: anikku-preview (★112)

**The difference:** Animiru is a one-person project with a fast cadence; Anikku is an org with a proven trade — a monthly release, give or take. No choice is eternal: the house decides with dates.

## Today's extension news

**salmanbappi/extensions-repo** — ★40 · push from TODAY — and its partner aniyomi-extensions (★15). The anime warehouse map grows.

**Pure anime or anime+manga?** A manga library in Mihon/Komikku and occasional sports anime: Anikku fits you. If you live anime as a full service: Animiru.

**Impostors:** builds wearing the houses' names with a different signature — named without linking. An inflated version without a release at the house = bait.
> —Which is better, Animiru or Anikku?
> —Lone folks or with an organization? Both are pushing this week.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# The pure-anime branch — Animiru and Anikku (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 14 (Sep 15) · **Verified:** today, September 15, 2026

The branch that REMOVED the manga from the player to keep only the anime. Two houses, two schools:

- **Animiru** — ★864 · v0.20.0.1 (Sep 14) — the anime-only born from Aniyomi; it inherits extensions from the same warehouse (Yūzōnō anime, ★432) · github.com/Quickdesh/Animiru
- **Anikku** — ★1,032 · v0.2.0 (Sep 11) · **r8932 in sight TODAY** — the INSTITUTIONAL bet: the anime piece of the Komikku organization (the same one sustaining Komikku) · testing channel: anikku-preview (★112)

**The difference in schools:** Animiru is a one-person project with a fast cadence; Anikku is an org with a proven trade — a monthly release, give or take. No choice is eternal: the house decides with dates.

**Today's extension news:** salmanbappi/extensions-repo — ★40, push from TODAY — and its partner aniyomi-extensions (★15). The anime warehouse map grows.

**Pure anime, or anime+manga?** If your manga library lives in Mihon/Komikku and anime is an occasional sport: Anikku fits you. If you live anime as a full service: Animiru.

**Impostors:** builds wearing the houses' names with a different signature — named without linking. An inflated version number without a release at the house = bait.

The house meme:
> —Which is better, Animiru or Anikku?
> —Lone folks or with an organization? Both are pushing this week.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
