# Pieza 15 — Rama J2K: el abuelo volvió — tachiyomiJ2K, Yōkai, Rokku, Reikai y el fantasma Hayai apareció

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `2a4a38ed56c8` · ES-TG `d76fbac2f951` · EN-Reddit `f0cf0d9d8ae9` · EN-Discord `bc2806d16435`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 15 — Rama J2K: el abuelo volvió — tachiyomiJ2K, Yōkai, Rokku, Reikai y el fantasma Hayai apareció

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌳 El árbol de esta rama
├── ⚡ tachiyomiJ2K — el abuelo despertó
├── 👻 Yōkai — el tronco en pausa activa
├── 🪇 Rokku — el fork de mantenimiento práctico
├── ⛩️ Reikai — manga y novelas en una biblioteca
├── 🐇 Hayai — el fantasma tiene casa (y se puede abrir)
├── 🌲 La red completa de forks (revisada el 14-sep)
├── 🧬 Los primos menores de la rama
├── 📜 La historia que explica esta rama
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Esta es la rama del interfaz querido: la que nació de tachiyomiJ2K — el fork que rediseñó Tachiyomi — y parió una familia entera. Lo primero que hay que decir es la noticia grande: **tachiyomiJ2K volvió a publicar versiones en agosto de 2026 después de dos años y medio de silencio.** Y la segunda: **Hayai — el proyecto que durante meses fue un fantasma sin repo accesible — hoy tiene casa pública y se puede abrir.**

```
tachiyomiJ2K  ★5.383  v1.8.1 (15-ago-2026)  el abuelo, de vuelta
Yōkai         ★1.883  v1.10.1 (4-sep)     push de ayer (14-sep) — el tronco
Rokku         ★51     v1.7.1 (29-ago)     el de mantenimiento
Reikai        ★27     v0.3.2 (4-sep)      manga + novelas unificadas
Hayai         ★41     v1.13.0 (10-abr)    el que ya no es fantasma
```

Todas las fichas se abrieron y verificaron HOY, 14 de septiembre. Donde la vida personal de los mantenedores explica los ritmos del proyecto, se cuenta como ellos la contaron: citada, fechada y sin chisme.

## 🌳 El árbol de esta rama

```
tachiyomiJ2K (el interfaz rediseñado)
         │   v1.7.4 (ene-2024) → dos años de silencio
         │   → v1.8.0 y v1.8.1 (agosto 2026): VOLVIÓ
         │
         ├── Yōkai        el fork personal de null2264
         │     ├── Rokku    fork de Yōkai: mantenimiento
         │     ├── Reikai   empezó en Yōkai, rebasado en Mihon
         │     └── Hayai    J2K-based, manga + novelas
         │
         ├── yomu         J2K-based, pequeño
         └── TachiyomiDNP variante pequeña, activa en agosto
```

## ⚡ tachiyomiJ2K — el abuelo despertó

https://github.com/Jays2Kings/tachiyomiJ2K

```
★5.383 · Apache-2.0
v1.7.4 → enero de 2024 (el cierre de la era vieja)
v1.8.0 → 9 de agosto de 2026 «Warning: Funny numbers ahead»
v1.8.1 → 15 de agosto de 2026 «Wait, there's more?»
```

Su historia en dos actos: fue EL fork de la era dorada — el que inventó el rediseño visual que media familia heredó — y luego calló durante dos años y medio, hasta agosto de 2026, cuando soltó dos versiones en una semana con su humor de siempre en los títulos. La comunidad lo considera el padre de la migración masiva de bibliotecas: fue el primero en mover bibliotecas completas entre lectores.

Su retorno no lo revive como candidato diario — dos versiones no son un ritmo — pero sí lo devuelve al mapa como historia viva: el abuelo no murió, estaba de viaje. Quien quiera la experiencia J2K «pura», su casa está de nuevo abierta y con versiones de este año.

## 👻 Yōkai — el tronco en pausa activa

https://github.com/null2264/yokai

```
★1.883 · Apache-2.0 · push de ayer (14-sep)
v1.10.0 y v1.10.1 (ambas el 4 de septiembre)
Soporte: extension-lib 1.6 · Android 8+ (su nota de versión)
```

Yōkai es el fork personal de null2264: tomó el interfaz J2K y lo sostiene solo. Su propio mantenedor lo explicó en la nota de la versión de septiembre, con una honestidad que vale citar: dio un paso atrás de sus proyectos por burnout, con la tesis y el trabajo encima, con la esperanza de volver «antes de año nuevo» y revisando contribuciones de vez en cuando. Llamó a su propia versión «bastante poco pulida». Y la misma nota abre con una advertencia en mayúsculas que conviene respetar: «BACKUP YOUR DATA» — copia tus datos antes de actualizar.

Lo que decía el dato del 14: la rama no está abandonada — el repo empujó ayer (14-sep). Lo que también dice: es un proyecto de una persona con una vida encima, y su ritmo lo marcará esa vida. La lección de la rama entera sale de aquí: los mantenedores son personas; el burnout es real; y la honestidad de un changelog vale más que un roadmap falso.

## 🪇 Rokku — el fork de mantenimiento práctico

https://github.com/rokku-app/rokku

```
★51 · Apache-2.0
v1.6.1 (15-ago) · v1.7.0 (23-ago) · v1.7.1 (29-ago)
— tres versiones en dos semanas: cadencia firme
Nace de: Yōkai, para mantenerlo al día con el
ecosistema de extensiones y dependencias
```

Rokku existe por la razón más práctica del mundo: cuando Yōkai se pausó, alguien decidió mantener la experiencia viva y al día — extensiones modernas, correcciones de rendimiento, el trabajo sucio y necesario. Sus notas de agosto se concentran en exactamente eso: ajustes de rendimiento y de descargas, compatibilidad con la librería de extensiones moderna y cuidados heredados del interfaz — el trabajo que no sale en capturas pero mantiene una app viva.

Es la ficha más pequeña en estrellas de la rama y la que más se mueve en arreglos. El estrellar mide fama; la cadencia mide taller. Y hay más señal de taller vivo: Rokku tiene canal nocturno propio (rokku-nightly) con builds casi diarios — el último visto era del día de ayer. *(Reverificado el 15-sep: el último nightly es el r7091, del 13-sep — la cadencia sigue; la fecha, actualizada.)* Cuando una casa compila de noche, trabaja de día.

## ⛩️ Reikai — manga y novelas en una biblioteca

https://github.com/unseensnick/Reikai · Sitio: https://reikai.app

```
★28 · Apache-2.0 · push del 14-sep (día de la verificación) · v0.3.2 (4-sep)
v0.3.2 (4-sep) · v0.3.1 (9-ago) · v0.3.0 (16-jul)
Nace de:     empezó como fork de Yōkai — el grafo de
             GitHub aún lo anota así — y su proyecto
             cuenta que el código fue rebasado después
             sobre Mihon
Tiene: versión FOSS aparte (sin reportes de crash ni
analítica) — reikai-foss en sus releases
```

Reikai es la idea más diferenciada de la rama: UNA biblioteca donde la misma serie de manga y de novela ligera viven juntas. Sus funciones declaradas: agrupación multi-fuente (pliega la misma serie de distintos sitios en una entrada), fusión manual cuando los títulos no coinciden, lectura fusionada con lista de capítulos unificada, sincronización de trackers compartida en el grupo, y biblioteca de novelas de primer nivel con soporte del lector de LNReader.

Su filosofía, dicha por su autor: construido primero para su uso diario — el desarrollo es esporádico y las funciones siguen sus gustos. Esa honestidad define lo que es: un proyecto personal muy bien documentado (su sitio web completo lo confirma), no un producto con promesas de equipo.

## 🐇 Hayai — el fantasma tiene casa (y se puede abrir)

https://github.com/HayaiApp/hayai

```
★41 · Apache-2.0
v1.13.0 (10 de abril de 2026) · push del 6-sep
Qué es: «Hayai es un lector Android basado en
TachiyomiJ2K con manga y novelas ligeras»
(según su propia descripción)
```

Aquí está la sorpresa de esta rama: durante meses, Hayai fue el proyecto fantasma — mencionado en listas y en changelogs ajenos, con su repo inaccesible, imposible de evaluar. Hoy el repo abre, se puede leer, y dice lo que es: J2K-based, manga y novelas ligeras, con versión de abril y actividad del mes pasado.

Lo que hoy es verificable: la casa existe, la licencia está declarada, hay release etiquetada. Y su README —leído entero HOY— precisa la receta con una honestidad rara: arquitectura J2K declarada como base y fuente de verdad, soporte de fuentes adult reconstruido sobre los contratos de TachiyomiSY, plugins de novelas al estilo LNReader, e «importación defensiva» de la base de datos del Hayai viejo — el archivo de la era fantasma sigue cuidando a quien lo usó. Lo que todavía no: si su desarrollo es sostenido — su última versión tiene cinco meses, aunque su repo se movió la semana pasada. Ficha nueva, seguimiento abierto: el fantasma se le da un mes de vida pública antes de cualquier veredicto. Es la regla de la casa — el rumor se comprueba en la casa del proyecto, y a veces la casa aparece.

**Y la familia Hayai creció por el lado que nadie miraba:** el mismo org publicó **HayaiTTS** (★39) — un motor de texto-a-voz neuronal OFFLINE para Android: se registra en el sistema entero y trae 186 voces (Piper y Kokoro, vía sherpa-onnx). Última versión: 2.5.1, del 15 de junio. La pieza que faltaba del rompecabezas: leer la novela… o escucharla. Para quien lee novelas ligeras en el bus, esto es el cierre del círculo.

## 🌲 La red completa de forks (revisada el 14-sep)

Las redes de los cinco proyectos se abrieron fork por fork hoy en la API de GitHub — incluida la de J2K, que esconde al pariente rico que casi nadie nombra:

**En la red de J2K:**

- **TachiyomiS97** (Saud-97, ★125) — el príncipe de esta rama y su fork más seguido: «una versión más rápida de Tachiyomi». Sus funciones propias, de su README: actualizaciones globales hasta 5× más rápidas, descargas hasta 3× más rápidas, progreso multi-dispositivo vía trackers (experimental), auto-descarga del siguiente capítulo mientras lees, y búsqueda por URL en el global search. Y la historia se repite: v1.7.5 del 1 de agosto de 2026 tras callar desde enero de 2024 — la pareja del abuelo: ambos despertaron este año.

**En la red de Yōkai (100+ forks):**

- **yurei** (NotBlankyu, v1.10.1 del 21-ago) — la variante con ambición: manga + webnovels, modo texto que renderiza el capítulo como texto en vez de imágenes, filtro NSFW heredado de SY, y lectura local que ahora lee ComicInfo.xml por capítulo.
- **yokai-T** (KakarottoCake, v1.0.2 del 4-jul) — streaming y descarga por torrent, su apuesta propia.
- Un fork con **carpetas personalizadas** (colecciones multi-seria con orden y backup) empujó el 14-sep (constancia del día) — sin releases todavía.
- Red completa con nombres propios: kagura, Mekuri (local-first), Miko, Karasu, y una variante Komga+galería. Más las copias ★0 de fábrica, que son la mayoría.

**Y las redes chicas:** Rokku tiene 3 forks (todos ★0, uno empujó el 14-sep — red recién nacida); Reikai tiene 5, con **Nekoumy** (Zykrave, el mismo autor de Kuro: «una biblioteca para manga y novelas», push del 12-sep); Hayai tiene 4, todas copias ★0. Cuanto más joven es la casa, más pequeña es su estela — por ahora.

**La expedición profunda (J2K: 999 miembros · Yōkai: 125 — caminadas el 14-sep hasta las hojas):** en la capa honda de estas redes, lo vivo con propuesta propia: **yurei** tiene ya un hijo activo — el fork para usuarios **MIUI/HyperOS**, que corrige lo que la optimización de fábrica de Xiaomi estorba, y va por v1.11.0. En la línea Yōkai, hojas con nombre y pulso: **Miko**, **Karasu**, **kagura**, **Mekuri** (local-first), **shuo** (novelas) y **MiruKan** (con versión propia, v1.0.1 de mayo). Y el taller Hayai se completa: canal nocturno con builds de esta semana (hayai-nightly) *(reverificado el 15-sep: el último build fechado del canal es el r6674, del 6-sep)* al lado del **HayaiTTS** fichado arriba. El resto de la capa profunda son copias sin aportes: fuera del mapa.

## 🧬 Los primos menores de la rama

Para completar el mapa, los repos pequeños que la búsqueda de hoy trajo — nombrados con su tamaño real:

```
yomu (HugoFMiranda)          ★3   J2K-based, push jul-2026
TachiyomiDNP                 ★4   variante, push 16-ago
Hiirbaf/yokai                ★3   fork de Yōkai, push del 13-sep
```

Ninguno alcanza la puerta de madurez para recomendarse como alternativa diaria — pero se nombran porque existir también es información, y porque cualquiera de ellos puede ser el próximo Rokku (que hace seis meses era igual de pequeño). Las copias sin dueño activo, ni eso: copias con reloj.

## 📜 La historia que explica esta rama

Esta rama es la mejor clase de historia del ecosistema: la de la herencia que se reparte.

```
2019–2023   tachiyomiJ2K define el interfaz moderno
            del lector manga libre. La migración
            masiva de bibliotecas nace aquí.

ene-2024    Tachiyomi original cierra (presión legal).
            J2K calla. Los usuarios del interfaz J2K
            quedan huérfanos.

2024–2025   Yōkai recoge la herencia del interfaz.

2026        La familia se ramifica por necesidad:
            Rokku mantiene, Reikai une formatos,
            Hayai sale de la sombra, y el abuelo
            mismo vuelve en agosto.
```

Cinco proyectos vivos donde había uno callado. La lección de la rama: cuando un taller cierre, no es el fin del oficio — es el reparto de las herramientas.

## ❓ Preguntas frecuentes

**¿tachiyomiJ2K «volvió» de verdad o fue una cosa puntual?**
Dos versiones en una semana de agosto, con etiquetas y notas — es un regreso real de actividad. Si habrá cadencia, lo dirá el otoño; su releases page es el reloj.

**¿Yōkai o Rokku si venía del interfaz J2K?**
Yōkai es el tronco con el mantenedor original en pausa activa; Rokku es la rama de mantenimiento con cadencia de agosto. La diferencia práctica está en su ritmo — y ambas se abren el día que se decide.

**¿Reikai reemplaza a mi lector de manga normal?**
No viene a reemplazar: trae la función que casi nadie tiene — manga y novelas en UNA biblioteca, con la misma serie agrupada aunque venga de fuentes distintas. Si no lees novelas, es más app de la que necesitas.

**¿Hayai era un mito entonces?**
Era un proyecto real sin puerta. Hoy la puerta existe, la licencia está declarada y hay versión etiquetada. El mito quedó en historia — y esta corrección es exactamente por lo que las guías llevan fecha.

**¿Cuál tiene la versión más fresca de la rama?**
Yōkai y Reikai: 4 de septiembre. Rokku: 29 de agosto. Hayai: 10 de abril. J2K: 15 de agosto. Los números caducan — la página de releases de cada uno no.

**¿Y el fork «más rápido» (TachiyomiS97)?**
Es el fork más seguido de la red de J2K (★125) y sus promesas están escritas en su README: revive en agosto de 2026 con optimizaciones de actualizaciones y descargas. La regla no cambia: los números de rendimiento de cualquier fork se comprueban en uso propio — y su página de releases, abierta el día que se decide.

**¿Los primos menores (yomu, DNP)?**
Se nombran, se miden, no se recomiendan: no pasan aún la puerta de madurez. Mañana puede ser otro cuento — con fecha, se dirá.

**¿Por qué tanto «su propio mantenedor dice» en esta guía?**
Porque en una rama de proyectos personales, la palabra del mantenedor ES la fuente primaria: Yōkai explicó su pausa, Reikai explica su filosofía, J2K firma con humor sus regresos. Citarlos con fecha es verificarlos.

## 🔗 Enlaces

- tachiyomiJ2K: https://github.com/Jays2Kings/tachiyomiJ2K
- Yōkai: https://github.com/null2264/yokai
- Rokku: https://github.com/rokku-app/rokku
- Reikai: https://github.com/unseensnick/Reikai · https://reikai.app
- Hayai: https://github.com/HayaiApp/hayai
- Destacados de la red: https://github.com/Saud-97/TachiyomiS97 · https://github.com/NotBlankyu/yurei · https://github.com/KakarottoCake/yokai-T · https://github.com/Zykrave/Nekoumy
- Primos: https://github.com/HugoFMiranda/yomu · https://github.com/theordinaryguy23/TachiyomiDNP · https://github.com/cuong-tran/tachiyomiJ2K

> La Bandita informa a partir de fuentes fechadas. El abuelo volvió, el fantasma tiene casa — y la rama entera se verificó hoy.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Yōkai ★1.883 (push del 14), Reikai ★28 (v0.3.2 del 4-sep), redes chicas re-fechadas. El J2K y sus 999 miembros de red, constados a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Rama J2K — el abuelo volvió

- **tachiyomiJ2K** ★5.384 · **v1.8.1 (15-ago-2026)** — versiones de nuevo tras el silencio · github.com/Jays2Kings/tachiyomiJ2K
- **Yōkai** ★1.883 · v1.10.1 · push del 14 (pausa activa de una persona)
- **Rokku** ★51 · **Reikai** ★28 (sitio: reikai.app) · **Hayai** ★42 + **HayaiTTS** ★39 (voz neuronal OFFLINE pa' novelas)

Primos: TachiyomiS97 ★125 (revivió en agosto) · yomu ★3 · TachiyomiDNP ★4.

La historia: J2K fue EL lector de la era dorada; el original cerró ene-2024, la rama quedó en coma — y el fork más seguido volvió a compilar. Los mapas que lo dieron por muerto: desactualizados.
*Fuente: pieza 15 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 15 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿J2K no estaba muerto? —Estaba dormido. El push reciente despertó a todo el linaje.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# The grandfather came back: tachiyomiJ2K shipped v1.8.1 in August and its family (Yōkai, Rokku, Reikai, Hayai) has dates
**Reddit · ingles-US · fuente: pieza 15 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** tachiyomiJ2K ★5,384 published v1.8.1 (Aug 15, 2026) after years of silence. The family: Yōkai ★1,883 (push Sep 14), Rokku ★51, Reikai ★28, Hayai ★42 (+HayaiTTS ★39, offline neural voice).
## The classic's lineage

- **tachiyomiJ2K** — ★5,384 · **v1.8.1 (Aug 15, 2026)** — THE GRANDFATHER WOKE UP: versions again after the silence · github.com/Jays2Kings/tachiyomiJ2K
- **Yōkai** — ★1,883 · v1.10.1 (Sep 4) · push from the 14th — a trunk in active pause (a one-person project; their life sets the rhythm, and that's how we tell it)
- **Rokku** — ★51 · v1.7.1 (Aug 29) — the practical-maintenance fork
- **Reikai** — ★28 · v0.3.2 (Sep 4) · push from the 14th — manga + novels unified · own site: reikai.app
- **Hayai** — ★42 · v1.13.0 — no longer a ghost: a Yōkai fork with novels, and it grew where nobody looked: **HayaiTTS** (★39), OFFLINE neural voice for reading novels

## The network's prince and the cousins

**TachiyomiS97** (Saud-97, ★125) — "a faster version of Tachiyomi", revived in August. Younger cousins with a date: yomu ★3 · TachiyomiDNP ★4 · Hiirbaf/yokai ★3.

## The history that explains this

J2K was THE reader of the golden era; when the original closed (Jan 2024), its branch went into a coma — until the most-followed fork compiled again. **The maps that declared it dead: outdated.** Small networks, a sign of life: Rokku has 3 forks (one pushed on the 14th); Reikai 5, with Nekoumy (Zykrave, the same author as Kuro).
> —Wasn't J2K dead?
> —It was asleep. The recent push woke the whole lineage.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# The J2K branch — the grandfather came back (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 15 (Sep 15) · **Verified:** today, September 15, 2026

The lineage of the classic tachiyomiJ2K, counted tonight:

- **tachiyomiJ2K** — ★5,384 · **v1.8.1 (Aug 15, 2026)** — THE GRANDFATHER WOKE UP: versions again after the silence · github.com/Jays2Kings/tachiyomiJ2K
- **Yōkai** — ★1,883 · v1.10.1 (Sep 4) · push from the 14th — the trunk in active pause (a one-person project; their life sets the rhythm, and that's how we tell it)
- **Rokku** — ★51 · v1.7.1 (Aug 29) — the practical-maintenance fork
- **Reikai** — ★28 · v0.3.2 (Sep 4) · push from the 14th — manga + novels unified; own site: reikai.app
- **Hayai** — ★42 · v1.13.0 — the one that's no longer a ghost: a Yōkai fork with novels, and the family grew where nobody was looking: **HayaiTTS** (★39), OFFLINE neural voice for reading novels

**The network's prince:** TachiyomiS97 (Saud-97, ★125) — "a faster version of Tachiyomi", revived in August. And the younger cousins with their date: yomu ★3 · TachiyomiDNP ★4 · Hiirbaf/yokai ★3.

**The history that explains this:** J2K was THE reader of the golden era; when the original closed (Jan 2024), its branch went into a coma — until the most-followed fork compiled again. The maps that declared it dead: outdated.

**Small networks, sign of life:** Rokku has 3 forks (one pushed on the 14th); Reikai 5, with Nekoumy (Zykrave, the same author as Kuro).

The house meme:
> —Wasn't J2K dead?
> —It was asleep. The recent push woke the whole lineage.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
