# Pieza 16 — Rama SY/Komikku: el fork clásico y el rehijo con organización — TachiyomiSY y Komikku

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `5cf5722c88bc` · ES-TG `f3087d0eb72c` · EN-Reddit `1ac6d0a8c9a5` · EN-Discord `0986040fa6e8`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 16 — Rama SY/Komikku: el fork clásico y el rehijo con organización — TachiyomiSY y Komikku

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌳 El árbol de esta rama
├── 📗 TachiyomiSY — el clásico que sigue
├── 📘 Komikku — el rehijo con org
├── 🔀 Las dos escuelas de fork (y el contraejemplo)
├── 🧩 Las extensiones de esta rama
├── 🌲 La red completa de forks (revisada el 14-sep)
├── 🏗️ La infraestructura: previews y sync
├── ⚖️ SY o Komikku: cómo decidir con criterio
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Esta es la rama del estilo clásico: TachiyomiSY — el fork que añadió las funciones extra al Tachiyomi original, el clásico «SY» de la vieja guardia — y Komikku, el proyecto que nació de ese linaje y creció hasta tener organización propia. Verificado HOY, 14 de septiembre:

```
TachiyomiSY       ★4.143   1.13.2 (13-jul)   push 13-sep   el clásico
TachiyomiSYPreview ★484    host de previews  push 25-ago
Komikku           ★4.717   v1.14.1 (17-jul)  push 11-sep   el rehijo
komikku-preview   ★248     canal de pruebas  push 10-sep
```

Son los dos grandes vivos del estilo SY del ecosistema — y la comparación entre ellos es la lección sobre cómo un fork se convierte en proyecto con vida propia.

## 🌳 El árbol de esta rama

```
TachiyomiSY (jobobby04)      el clásico vivo
   ├── TachiyomiSYPreview     host de builds de prueba
   └── Komikku (komikku-app)  repo nuevo que hereda el
               ├── komikku-preview  código y creció con org
               ├── Anikku           su cliente de anime
               └── (su rama tiene pieza propia en esta colección)
```

Detalle técnico que se lee en la API: Komikku NO figura como fork (es un repo nuevo); su linaje lo declara su propia documentación. Es la diferencia entre el grafo de GitHub y la realidad — por eso se leen los dos.

## 📗 TachiyomiSY — el clásico que sigue

https://github.com/jobobby04/TachiyomiSY

```
★4.143 · Apache-2.0
Versión:      1.13.2 (13 de julio de 2026)
Push:         13 de septiembre — código de AYER
Qué es:       el fork clásico: el lector del tronco
              con las funciones extra del estilo SY
              (más fuentes por defecto, más ajustes
              de lectura, la experiencia "completa")
```

SY es el fork con más historia continua del ecosistema: existía antes del cierre del original, sobrevivió a enero de 2024 y sigue empujando código — lo hizo el 13-sep, constancia de su verificación. Su ritmo no es el de releases mensuales: su última estable es de julio y su código se mueve desde entonces. El patrón del veterano: menos ruido de versiones, más mantenimiento silencioso.

Su aviso de identidad: **el SY vivo es jobobby04** — el día que busques SY, instala desde su repo, el que empuja código de ayer. El nombre no basta; el dueño sí.

Su host de builds de prueba: jobobby04/TachiyomiSYPreview (★484) — versiones experimentales para curiosos y reporteros de bugs, no la vía del día a día.

## 📘 Komikku — el rehijo con organización

https://github.com/komikku-app/komikku

```
★4.717 · Apache-2.0
Versión:      1.14.1 (17 de julio de 2026)
Push:         11 de septiembre
Qué es:       lector manga del linaje SY que nació
              como repo nuevo y creció hasta
              organización completa:
              - komikku-preview (★248): canal de pruebas
              - Anikku (★1.028): su cliente de anime
              - traducciones comunitarias propias
```

Komikku es el caso de estudio de cómo un fork se vuelve institución: heredó el código del linaje, nació con casa propia, y construyó estructura — org, canal de previews, proyecto hermano de anime, comunidad de traducción. Sus versiones van por cadencia regular (1.14.1 en julio, con rama de desarrollo empujando desde entonces).

En estrellas ya supera al SY clásico (4.717 vs 4.143). Eso no es veredicto de calidad — es un dato de comunidad. Lo que sí es veredicto verificable: su taller se mueve (push del 11-sep) y su infraestructura es la más completa de esta rama.

## 🔀 Las dos escuelas de fork (y el contraejemplo)

Esta rama tiene los tres arquetipos del ecosistema, viviendo en la misma casa:

```
ESCUELA 1 — mantener el apellido
TachiyomiSY: continúa el fork clásico, conserva
el nombre y el estilo, evoluciona con cuidado.
Su valor: continuidad. Su usuario: el que quiere
lo de siempre, vivo.

ESCUELA 2 — crecer con casa nueva
Komikku: hereda el código, bautiza su nombre,
construye organización y hasta rama de anime.
Su valor: evolución con estructura. Su usuario:
el que quiere el proyecto que más se mueve
en estructura.
```

## 🌲 La red completa de forks (revisada el 14-sep)

Se abrieron el 14-sep, fork por fork, las redes de SY (238 forks, tres páginas, dos órdenes) y de Komikku (200 forks). Es la red más rica del ecosistema — y la que mejor muestra la diferencia entre copiar y aportar:

**En la red de SY:**

```
Chai (Smol-Ame)          ★12 · push 22-ago
   el fork vivo más seguido: filtro «lewd» para
   ocultar lo picante de la biblioteca, búsqueda
   por estado de tracking y edición de info del
   manga — sin releases todavía (solo código)

SY con Discord RPC (jeryjs)  ★10 · preview-43 (23-jul)
   presence de Discord mientras lees

Faxyomi                  ★4 · v9 (29-ago)
   «para tener DOS SY en el mismo teléfono» —
   el caso de uso más honesto del ecosistema

Shinyomi ★5 (1.0.0, may-25) · Mizu ★2 · Dyomi
(build 8-sep) · Fukuro (push 4-sep) · variante
desktop en obras · el fork del equipo SyncYomi
(push 10-sep)
```

**En la red de Komikku:**

```
Houri (PineappleTwilight)  ★10 · v1.22.1 (HOY 15-sep) *(la v1.22.0 salió el 14 — dos días seguidos: la cadencia sigue)*
   el fork con propuesta propia más activo:
   soporte de RELECTURA con trackers conectados
   (rereads por manga), Discord RPC mejorado que
   respeta subcategorías, filtros por defecto por
   fuente y un feed mejorado opt-in

komikku_img_upscale · r10647 (13-sep)
   upscale de imágenes de páginas — más tres
   forks más del mismo tema (upscaling/scaling)

mikku (Syncthing integrado) · komikku con
marcadores de página · kokomikku (KOReader) ·
un fork con tracker propio · komikku2 (13-sep)
```

El dato fino: el autor de Houri mantiene también un fork de Anikku (anikku-pineapple) — un solo dev tejiendo entre las dos ramas de la casa Komikku.

**La capa que el grafo esconde (cinco casas verificadas el 14-sep a petición de los grupos)**

Estos cinco NO aparecen en la red de forks directa de SY ni de Komikku: son forks rebasados con casa nueva, o nietos — invisibles para el grafo del padre. Se abrieron uno a uno, con sus opciones propias leídas de sus README:

```
ShinKu (Harrys-HQ)         ★31 · v2.6.9 (13-sep)
   «fork modernizado y rebautizado de
   TachiyomiSY/Mihon» — cadencia semanal.
   Lo suyo: búsqueda en lenguaje natural con
   descubrimiento asistido («Vibe Search» y
   «For You»), tarjeta de estadísticas de
   lectura, audio ambiental que casa con el
   género, interfaz que muda de color con la
   portada, categorizador automático, escáner
   de fuentes muertas para migrar tu manga, y
   menú para migrar las actualizaciones
   fallidas.

MihonSY (ruzhe85)          ★13 · v1.0.7 (22-ago)
   fork chino de SY (su README viene en chino).
   Lo suyo: scroll por toque en webtoon con
   distancia ajustable (½, ¾ o pantalla
   completa) y animación regulable, detección
   automática de webtoon por resolución de la
   imagen, progreso Komga sincronizado capítulo
   a capítulo (no por lotes), mejora de imagen
   Lanczos3 ligera —sin modelos pesados— y
   resolución nativa 1:1.

Pokomi (pokedo0)           ★11 · v1.0.9 (16-ago)
   fork de Komikku con una idea propia clara:
   «Author Following» — suscribirse para
   seguir a tus autores. Hereda las funciones
   únicas de Komikku.

NEXUS (the-nexus-app)      ★3 · v1.2.1 (8-sep)
   fork de Komikku: sugerencias que leen las
   recomendaciones del propio sitio de la
   fuente, categorías ocultas CON
   autenticación para abrirlas o borrarlas, y
   marcadores de capítulos y páginas al
   vuelo.

bchan (geograms)           ★5 · v1.12.1 (19-jun)
   «fork simplificado de TachiyomiSY/Mihon»:
   extensiones Keiyoushi listas de fábrica,
   lectura webtoon por defecto, descargas que
   pausan y reanudan solas entre redes, y
   nombres de archivo planos y predecibles.
```

Y la segunda generación también dio lo suyo: **Yomiko** (petalya, ★8, push del 12-sep), hija del fork de Discord-RPC — la cadena no se corta.

La lección de método queda en el texto: la lista de forks del padre no muestra a los rebasados ni a los nietos. Mapear el árbol es caminar las cadenas y leer los créditos de cada README — y cuando alguien nombra una casa que no salió en el barrido, el enlace manda.

**La expedición profunda (SY: más de 1.000 miembros · Komikku: 244 · anikku: 71 — todo caminado el 14-sep):** la segunda generación ya compila: **leassapie/houri**, hijo de Houri, con versión propia v1.21.0 (30 de agosto) — la cadena Houri → su hijo, viva. **Yomiko**, la nieta del fork de Discord-RPC — matiz fechado (corregido el 15-sep por auditoría de la casa): la casa mostraba empuje, pero su versión estable (v.1.8.1 — corrección fechada 15-sep por REST y git: release del 25-sep-2025, no ago-2026; y genealogía CERTIFICADA por fork: Yomiko ← SY-Discord-RPC ← TachiyomiSY — línea SY, no J2K). Que la fecha diga lo que la fecha dice. ShinKu, NEXUS, MihonSY, Pokomi y bchan son por ahora hojas: cuando echen raíces, se anotan con fecha.

## 🧩 Las extensiones de esta rama

La rama SY/Komikku es la que más almacenes viven atendiendo. El mapa de la hornada del 14 (su guía completa tiene pieza propia en esta colección):

```
Keiyoushi              el hub principal
   el almacén más usado del ecosistema: declara
   soporte para Mihon, TachiyomiSY y Komikku
   (guía completa: pieza 04 de esta colección)

Yūzōnō manga           ★890 · ESPEJO de Keiyoushi
   espejo automático, sin aportes propios —
   descontinuado (no archivado): el «push de
   hoy» es el espejo sincronizando, no vida
   propia. Para manga, la casa es Keiyoushi

cuong-tran/manga-repo  ★445 · push del 14-sep
   «Extensions for Komikku / Mihon & forks»
   (su descripción)

Estantes "cursed"      ★185/★158  nombre sí, índice no
```

El aviso de Keiyoushi sigue siendo la llave del ecosistema: si tu lista de extensiones sale vacía con «Outdated app», tu app ya no es compatible — actualízala desde su repo. Y la convención técnica del momento (KeiSource 1.6) se cuenta en la guía de extensiones: es la razón por la que las apps viejas dejan de ver extensiones nuevas.

## 🏗️ La infraestructura: previews y sync

Dos piezas que esta rama comparte con el ecosistema y que conviene conocer:

- **Los hosts de previews** (SYPreview, komikku-preview) son el canal de pruebas de cada proyecto: builds experimentales para quien reporta bugs. Instalarlos es una decisión de tester, no de usuario diario.
- **tracker-extensions** (komikku-app, ★14): las extensiones de trackers de la casa Komikku — los trackers se sirven aparte del núcleo, como extensiones (verificado el 14-sep). 
- **SyncYomi** es la sincronización de bibliotecas entre dispositivos y entre forks de la familia — útil exactamente para el gesto de esta guía: si pruebas SY y Komikku, tu progreso puede acompañarte entre ambos. Su ficha completa, en la colección de herramientas de esta serie.

## ⚖️ SY o Komikku: cómo decidir con criterio

Las cuatro puertas de la casa, aplicadas sin «mejores»:

```
Continuidad          si venías del SY de toda la vida,
                     jobobby04 es la misma casa con
                     las luces encendidas.

Estructura           si valoras org, canal de previews,
                     proyecto hermano de anime y
                     cadencia de releases: Komikku.

Compatibilidad       los dos leen los mismos almacenes
                     principales (Keiyoushi lo declara
                     para ambos). El criterio de desempate
                     no está en las fuentes: está en el
                     uso que le vayas a dar.

Madurez              los dos empujaron esta semana.
                     Ninguno pasa la puerta con las
                     manos en los bolsillos.
```

El resto es gusto personal — y el uso real: quien lo usa y lo comprueba. Las estrellas (4.717 vs 4.143) son el dato de fama del día, no una recomendación.

## ❓ Preguntas frecuentes

**¿SY y Komikku son el mismo código?**
Comparten linaje, no repo ni dueño. La API no declara a Komikku como fork; su propia documentación cuenta de dónde viene. Parentela declarada, casas separadas.

**¿Cuál tiene más fuentes?**
Las fuentes viven en los almacenes (Keiyoushi, Yūzōnō…), no en la app — y los almacenes principales declaran soporte para ambos. El desempate real está en la app que mejor te quepa en la mano.

**¿Y los repos con el mismo letrero que ya no se mueven?**
No se anotan: el mapa es de lo vivo. La regla práctica: instala SY desde el repo de jobobby04 — y nadie más.

**¿Y los repos que se anuncian como «el lector de 2026»?**
En el escaneo del 14-sep apareció otra camada del patrón ya conocido: repos nuevos con nombres de proyectos serios — un «komikku-scans», un «Neko-Manga-Pearl» que toma prestado el nombre del fork real de MangaDex, un «kumo-surreal» que se dice Mihon optimizado — creados los tres el mismo día, con estrellas casi idénticas entre sí y el año «2026» en la descripción. La camada crece mientras tanto: un «weeb-index» («Best Otaku Directory 2026») y un «manga-zen-reader» («Best Alternatives 2026») repiten el traje con las mismas estrellas de mentira. Se nombran sin enlazar: es SEO para cosechar descargas de quien busca rápido. El proyecto real no necesita ponerle el año al nombre.

**¿Y forks con nombres que suenan japonés que menciona la gente (tipo «ShinKu»)?**
Fichados arriba, con fecha: ShinKu existe (★31, v2.6.9 con cadencia semanal, del linaje SY/Mihon) — en el repaso anterior no apareció porque los forks rebasados y los nietos no salen en la red de forks del padre. Dos reglas quedan para el lector: un nombre sin enlace no se verifica ni se descarta — y el enlace, siempre, cierra el caso.

**¿Komikku salió de SY o de Tachiyomi?**
Su documentación declara el linaje del ecosistema; el grafo de GitHub lo muestra como repo nuevo. Ambas cosas son ciertas: herencia declarada, casa propia.

**¿Puedo tener los dos instalados?**
Técnicamente sí (paquetes distintos). La pregunta útil es la de siempre: ¿qué aporta el segundo que el primero no cubra? Si la respuesta es «nada», un lector basta.

**¿Y Anikku?**
Es el cliente de anime de la organización Komikku — tiene su propia guía en esta colección (rama anime puro). La familia se extiende: manga (Komikku), anime (Anikku), y el rebautizado AniZen en su rama aparte.

**¿Cuál sacó versión más reciente?**
Ninguna de las dos en septiembre: SY 1.13.2 y Komikku 1.14.1 son de julio — con código de ambas moviéndose este mes. El push no retaguea: el release se abre el día que se instala.

## 🔗 Enlaces

- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY · https://github.com/jobobby04/TachiyomiSYPreview
- Komikku: https://github.com/komikku-app/komikku · https://github.com/komikku-app/komikku-preview
- Destacados de la red: https://github.com/PineappleTwilight/houri · https://github.com/Smol-Ame/Chai · https://github.com/jeryjs/TachiyomiSY-with-discord-RPC · https://github.com/Viel0320/komikku_img_upscale · https://github.com/nas3ts/mikku
- La capa que el grafo esconde: https://github.com/Harrys-HQ/ShinKu · https://github.com/ruzhe85/MihonSY · https://github.com/pokedo0/Pokomi · https://github.com/the-nexus-app/NEXUS · https://github.com/geograms/bchan
- Almacenes de la rama: https://github.com/keiyoushi/extensions · https://github.com/yuzono/tachiyomi-extensions · https://github.com/cuong-tran/manga-repo
- Sincronización: https://github.com/syncyomi/syncyomi
- Guías hermanas: extensiones (pieza 04) · forks del tronco (pieza 06) · anime puro (pieza 14) de esta colección

> La Bandita informa a partir de fuentes fechadas. Dos escuelas, un mismo linaje — y el letrero, ya sabes, no instala nada.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Houri v1.22.1 de HOY, manga-repo ★445, SY/Komikku re-contados. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Rama SY/Komikku — el clásico y el rehijo

- **TachiyomiSY** ★4.146 · 1.13.2 · push del 13 — existía ANTES del cierre y sobrevivió (el vivo: jobobby04)
- **Komikku** ★4.721 · v1.14.1 · push del 11 — repo nuevo con organización propia, previews ★249, trackers como extensiones, y Anikku como su pieza anime

Camada nueva con fecha: **Houri** ★10 · v1.22.1 HOY · **ShinKu** ★31 · v2.6.9 (13-sep) · MihonSY ★13 · Pokomi ★11 · Chai ★12 · NEXUS ★3 · bchan ★5 · Yomiko ★8.

Nota de repaso: ShinKu no salió en el repaso anterior — el mapa aprende.
Extensiones: Yūzōnō manga ★892 (ESPEJO de Keiyoushi) · manga-repo ★445.
*Fuente: pieza 16 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 16 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿SY o Komikku? —El clásico sabe a hogar; el rehijo organiza la casa. Tu biblioteca decide.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# The SY/Komikku branch: the classic that survived the closure and the re-child with its own organization (verified today)
**Reddit · ingles-US · fuente: pieza 16 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** TachiyomiSY ★4,146 (1.13.2, push from Sep 13 — the living one is jobobby04) existed BEFORE the original closed; Komikku ★4,721 (v1.14.1) was born with an organized house, previews and trackers as separate extensions.
## The ecosystem's richest network

- **TachiyomiSY** — ★4,146 · 1.13.2 (Jul 13) · push from Sep 13 — THE CLASSIC: it existed before the closure and survived. The living one is **jobobby04** — the name isn't enough; the owner is · test host: SYPreview (★483)
- **Komikku** — ★4,721 · v1.14.1 (Jul 17) · push from the 11th — THE RE-CHILD: a new repo (the API doesn't declare it a fork) with its own organization, previews (★249), trackers as separate extensions, and Anikku (★1,032) as its anime piece

**The two schools:** SY inherited the code and walked the classic's road; Komikku was born with an organized house. The counterexample that explains it all: **Mihon** — it doesn't even compete for the name: it earned its own.

## The new litter, with dates

**Houri** — ★10 · **v1.22.1 from TODAY** (two releases two days in a row) · **ShinKu** — ★31 · v2.6.9 (Sep 13), weekly cadence · MihonSY ★13 · Pokomi ★11 · Chai ★12 · NEXUS ★3 · bchan ★5 · Yomiko ★8 (daughter of the fork with Discord-RPC — the chain doesn't break).

**Review note:** ShinKu exists — listed with a house, a date and a cadence. It didn't show up in the previous review: the map learns.

**The branch's extensions:** Yūzōnō manga — ★892 (a MIRROR of Keiyoushi) · cuong-tran/manga-repo — ★445 · "cursed" shelves: the name yes, the index no.
> —SY or Komikku?
> —The classic tastes like home; the re-child organizes the house. Your library decides.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# The SY/Komikku branch — the classic and the re-child (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 16 (Sep 15) · **Verified:** today, September 15, 2026

The ecosystem's richest network, tonight's cutoff:

- **TachiyomiSY** — ★4,146 · 1.13.2 (Jul 13) · push from Sep 13 — THE CLASSIC: it existed before the original closed and survived. The living one is **jobobby04** — the name isn't enough; the owner is · test host: SYPreview (★483)
- **Komikku** — ★4,721 · v1.14.1 (Jul 17) · push from Sep 11 — THE RE-CHILD: new repo (the API doesn't declare it a fork) with its own organization, previews (★249), trackers as separate extensions, and Anikku (★1,032) as its anime piece

**The two fork schools:** SY inherited the code and walked the classic's road; Komikku was born with an organized house. And the counterexample that explains it all: Mihon — which doesn't even compete for the name: it earned its own.

**The new litter, with dates:** Houri — ★10, **v1.22.1 from TODAY** (two releases two days in a row) · ShinKu — ★31 · v2.6.9 (Sep 13), weekly cadence · MihonSY ★13 · Pokomi ★11 · Chai ★12 · NEXUS ★3 · bchan ★5 · Yomiko ★8 (daughter of the fork with Discord-RPC — the chain doesn't break).

**Review note:** ShinKu exists — listed with a house, a date and a cadence. It didn't show up in the previous review: the map learns.

**This branch's extensions:** Yūzōnō manga — ★892 (a MIRROR of Keiyoushi) · cuong-tran/manga-repo — ★445 · "cursed" shelves: the name yes, the index no.

The house meme:
> —SY or Komikku?
> —The classic tastes like home; the re-child organizes the house. Your library decides.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
