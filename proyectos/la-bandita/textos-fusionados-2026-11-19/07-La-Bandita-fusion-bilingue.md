# Pieza 07 — Usagi está viva: la cadena Kotatsu → Yukimi → Usagi y los cuatro vivos del árbol

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `84eb3537087c` · ES-TG `d114fb85ff4b` · EN-Reddit `4a8433c776cd` · EN-Discord `9d032125c5ed`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 07 — Usagi está viva: la cadena Kotatsu → Yukimi → Usagi y los cuatro vivos del árbol

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🧬 La cadena completa: Kotatsu → Yukimi → Usagi
├── 🏗️ Lo que sí se archivó (y no fue la app)
├── 📱 Ficha: UsagiApp/Usagi
├── 🌳 Los cuatro vivos del árbol Kotatsu
├── 🧩 Plugins y parsers: cómo come este árbol
├── 🍴 Los forks de Usagi
├── 🎭 Los impostores de la semana
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Corre que anda por los grupos: «Usagi fue archivada», «Usagi murió». Se verificó el 14 de septiembre, en la casa misma del proyecto (re-verificado a 15-sep: sigue viva):

```
UsagiApp/Usagi — lo que se vio hoy
✓ Sin banner de archivado en la página del repo
✓ Push verificado el 14-sep
✓ README vivo: «lector de manga libre para Android,
  inspirado en Kotatsu»
✓ Ficha activa en F-Droid: org.draken.usagi
✓ Organización con 16 repositorios
✓ Única versión estable: 1.0 (con rc2 y rc1 detrás)
```

**Usagi está viva.** Lo que murió fue otra cosa — y de ahí viene la confusión: la organización sí archivó su capa vieja de plugins (dos repos concretos), y la predecesora de Usagi, llamada Yukimi, sí fue descontinuada por su propio desarrollador. Esa historia completa va abajo, con fechas.

## 🧬 La cadena completa: Kotatsu → Yukimi → Usagi

El árbol Kotatsu tiene una genealogía de tres actos. La primera parte está verificada en GitHub; la transición del medio viene de los reportes de la comunidad (hilos de noviembre de 2025 y principios de 2026):

```
ACTO 1 — Kotatsu
KotatsuApp/Kotatsu · ★8.855
ARCHIVADO el 4 de noviembre de 2025 (confirmado el 14-sep)
El original cierra tras la presión legal de Kakao
Entertainment y, según sus propios autores, también
por la política de verificación de desarrolladores
que se venía. Última versión: 9.4.1.

ACTO 2 — Yukimi (reportes de la comunidad)
Los mismos desarrolladores anuncian una sucesora:
Yukimi. Semanas después, su autor la descontinúa
y retira su sitio. Los hilos de la época la dan
por terminada — «the project ended today».
No quedó repo vivo que verificar ese día: por eso
esta guía la cuenta como historia relatada,
no como ficha.

ACTO 3 — Usagi
La comunidad continúa por otro camino: Usagi,
con el mismo espíritu Kotatsu pero con una decisión
de diseño clave: NO trae fuentes integradas.
Las fuentes las trae el usuario. Esa decisión
es, probablemente, la razón por la que Usagi
sigue viva donde otras murieron.
```

Los reportes de la época nombraban también a Kotatsu-Redo, Kototoro y Futon como los sobrevivientes del árbol. Los cuatro viven — fichas abajo, todos abiertos hoy.

## 🏗️ Lo que sí se archivó (y no fue la app)

La organización UsagiApp tiene 16 repositorios, abiertos hoy. Dos están archivados — y son la fuente real del rumor:

```
ARCHIVADOS (la arquitectura vieja)
UsagiApp/core-parsers   «librería para el repo de plugins»
UsagiApp/core-exts      «núcleo para cargar plugins externos»

VIVOS (lo que los reemplaza)
UsagiApp/TsukiMix       el núcleo nuevo para leer y compilar
                        extensiones y parsers
UsagiApp/plugins        plugins y ejemplo para creadores
UsagiApp/syncserver     servidor de sincronización de datos
                        «para Kotatsu / Usagi»
UsagiApp/Tsuki          la librería compartida del ecosistema
```

Es el gesto de toda casa viva: demoler el andamio viejo mientras el edificio sigue abierto. Quien pasó por la organización y vio dos «archived» sin leer nombres, se llevó el rumor. Los nombres dicen otra cosa: se archivó la capa de plugins antigua — la app ni lo notó por fuera.

## 📱 Ficha: UsagiApp/Usagi

https://github.com/UsagiApp/Usagi

```
Qué es:       lector de manga libre para Android,
              inspirado en Kotatsu, SIN fuentes integradas
Licencia:     GPL-3.0
Versión:      1.0 (la única estable; rc2 el 2-sep,
              rc1 el 9-ago)
Estrellas:    257 · push del 14-sep (día de la verificación; release 1.0 del 10-sep)
Android:      5.0 en adelante (badges del README)
Casa:         github.com/UsagiApp/Usagi
Canales:      GitHub, F-Droid (org.draken.usagi),
              Obtainium y OpenAPK según su README
```

Su página de F-Droid carga hoy — la app está publicada allí, con su paquete org.draken.usagi. El Discord y el Telegram que el README exhibe no se enlazan aquí: esta familia no usa ni recomienda canales de envío, y los enlaces de comunidad los tiene el propio proyecto.

Un «1.0» es un número de nacimiento, no de madurez. La app tiene release, README, casa y comunidad pequeña pero viva. Lo que no se ha auditado: cuánto responde su autor a los reportes — se abre un par de hilos de issues antes de confiarte tu biblioteca, como con cualquier proyecto joven.

## 🌳 Los cuatro vivos del árbol Kotatsu

### Kotatsu-Redo — el que heredó el nombre

https://github.com/Kotatsu-Redo/Kotatsu-Redo

★867 · versión **9.8.3 (6 de septiembre)** · GPL-3.0 · vivo. El fork comunitario que la comunidad nombra primero desde que el original archivó. Su organización sostiene cuatro repos: la app, sus parsers (kotatsu-parsers-redo), un servidor de telemetría y otro de sincronización. Lleva el nombre «Kotatsu» adelante con versiones de la serie 9.8.x.

### Futon — el del motor propio

https://github.com/AppFuton/Futon

★427 · versión **9.8.1 (16 de agosto)** · GPL-3.0 · vivo. Su organización tiene ocho repos, entre ellos su propia librería de parsers (AppFuton/futon-parsers, archivada — congelada mientras la app avanza; señal a vigilar) y hasta su landing page. Curiosidad del árbol: los números de versión de Futon y Kotatsu-Redo se parecen — ambos heredaron la numeración del original.

Y un aviso de desvío: existe MikuX-Dev/Futon (3 estrellas, otra cosa con el mismo nombre). La ficha válida es AppFuton.

### Kototoro — el que quiso todo junto

https://github.com/Kototoro-app/Kototoro

★569 · **v2.1.2 publicada el 14-sep — y el 15 amaneció con la v2.1.3** (Publicación 02) · Apache-2.0 en su licencia declarada. Manga, novelas y vídeo en una sola app — la más movida del árbol esta semana (tres versiones en cuatro días). Tiene guía completa propia en esta familia.

### Usagi — la que no trae fuentes

La ficha de arriba. Su diferencia de diseño con los otros tres es su carta de identidad: sin fuentes integradas, el usuario trae las suyas vía plugins.

## 🧩 Plugins y parsers: cómo come este árbol

El árbol Kotatsu no usa extensiones tipo Mihon: usa librerías de parsers y plugins compilados. Las piezas del día:

**Gekkoushi/plugin** — https://github.com/Gekkoushi/plugin — los artefactos listos para Usagi y apps con estructura Tsuki. Su README (reverificado hoy) dice: «Only for the Usagi App», «No updates, 1.3k sources» — mil trescientas fuentes compiladas congeladas en su estado actual — y el plugin UMA «solo para la versión 1.0». Esa última condición encaja con la realidad de hoy: la única estable de Usagi es la 1.0.

**Gekkoushi/plugin-source** — https://github.com/Gekkoushi/plugin-source — ★90, GPL-3.0, push del 13-sep, versión 1.2.6. Aquí se contribuye y aquí se reportan las fuentes rotas.

**InvalidDavid/UMA** — https://github.com/InvalidDavid/UMA — ★69, GPL-3.0, tags del 12 y 13 de septiembre. Instalación automática o manual de plugins para Usagi y otros forks de Kotatsu.

**Tsuki y TsukiMix** — las librerías compartidas de la propia organización: Tsuki (la de la era plugins) y TsukiMix (la evolución actual). Con syncserver, la organización cubre todo el sándwich: app, capa de carga, parsers y sincronización.

La regla de siempre sobre descargas: los artefactos se nombran, no se pegan. El clic de instalación lo da cada quien en la casa del proyecto, el día que lo use.

## 🍴 Los forks de Usagi

La lista pública de forks muestra hoy 30 en su primera página, con actividad mayormente reciente — y ninguno con proyecto propio. Un fork sin identidad es una copia de seguridad con fecha: existe, no sucede. Si alguno crece, tendrá ficha el día que la merezca.

## 🎭 Los impostores de la semana

La búsqueda de esta semana trajo una camada con el mismo traje — estrellas infladas e idénticas (115–120 mil), nacimiento el 13-sep, títulos de clasificado: «usagi-nightly», «usagi-sora-vn-sources», «komikku-scans», «translation-hub-stringsets». Ninguno es fork de Usagi ni fuente verificada: son imanes de clic con nombre prestado.

```
El traje del impostor
★ idénticas entre varios repos
Título de anuncio, no de proyecto
Sin historial: nacieron esta semana
Prisa por que los enlaces «antes de que lo borren»
```

Si «el nuevo fork de Usagi» que te pasaron termina en uno de estos, ahí es exactamente donde entra el malware. La casa de Usagi es una y tiene dueño: UsagiApp.

## ❓ Preguntas frecuentes

**¿Usagi está muerta?**
No. Push de hoy, organización activa, F-Droid publicada. Lo archivado fue la capa vieja de plugins; lo descontinuado fue Yukimi, su predecesora. Cada cosa con su fecha arriba.

**¿Cuál es «el nuevo fork» entonces?**
Del árbol Kotatsu viven hoy cuatro: Kotatsu-Redo, Futon, Kototoro y Usagi. No hay sucesor de Usagi porque no ha hecho falta.

**¿Usagi o Kotatsu-Redo?**
Distintos diseños: Usagi sin fuentes integradas (las traes tú); Kotatsu-Redo hereda el modelo del original. La que cubra tu uso, con el repo que abras ese día.

**¿Futon y Kotatsu-Redo son lo mismo por los números de versión?**
Comparten herencia de numeración, no repositorio. Fichas separadas, casas separadas.

**¿Dónde están las fuentes de Usagi?**
En la capa de plugins: Gekkoushi/plugin (artefactos), plugin-source (código), UMA (instalador). Sin recetas pegadas aquí — la casa del proyecto las explica.

**¿Puedo ponerle extensiones de Mihon?**
No: otro árbol, otro protocolo. Los árboles no se injertan por descuido.

**¿Y si me pasan un APK «Usagi Plus»?**
Si no sale de UsagiApp o de F-Droid (org.draken.usagi), es un letrero. Los impostores de la semana son la razón por la que esa regla existe.

**¿Por qué F-Droid importa tanto aquí?**
Porque su publicación pasó por el proceso de la tienda: paquete identificado, compilación verificable. Es la diferencia entre «descárgalo de este enlace» y «está en una casa con proceso».

## 🔗 Enlaces

- Usagi: https://github.com/UsagiApp/Usagi · F-Droid: https://f-droid.org/en/packages/org.draken.usagi/
- Organización: https://github.com/orgs/UsagiApp/repositories
- Plugins: https://github.com/Gekkoushi/plugin · https://github.com/Gekkoushi/plugin-source · https://github.com/InvalidDavid/UMA
- Kotatsu-Redo: https://github.com/Kotatsu-Redo/Kotatsu-Redo
- Futon: https://github.com/AppFuton/Futon
- Kotatsu original (archivado): https://github.com/KotatsuApp/Kotatsu
- Kototoro: https://github.com/Kototoro-app/Kototoro

> La Bandita informa a partir de fuentes fechadas. La app vive; el andamio viejo, no. Y el rumor, ya ves, viaja más rápido que el changelog.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Usagi ★257 viva, Kotatsu ★8.855, Redo ★867, Futon ★427, Kototoro v2.1.3. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 «Usagi murió» = FALSO — la cadena Kotatsu → Yukimi → Usagi

Verificado EN LA CASA, dos veces hoy: **Usagi — ★257 · release 1.0 del 10-sep · push del 14 · VIVA.**

La cadena: **Kotatsu** ★8.855 (archivó 4-nov-2025) · **Yukimi** archivada (nov-2025) · **Usagi** sigue.

Los cuatro vivos del árbol: **Kotatsu-Redo** ★867 · **Futon** ★427 · **Kototoro** ★569 (v2.1.3 HOY) · **Usagi**.
Plugins: Gekkoushi ★90 (v1.2.6) · UMA ★69.

Impostores de la semana: estrellas idénticas de 115–120 mil, nacimiento reciente, cero casa. Sin enlace.
*Fuente: pieza 7 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 07 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —Oye, ¿Usagi murió? —Murió el rumor. La casa empujó código esta semana.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# "Usagi got archived" is false: I verified the Kotatsu → Yukimi → Usagi chain, and this is what the house says
**Reddit · ingles-US · fuente: pieza 7 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** The rumor ran through the groups. The house says the opposite: Usagi ★257 with release 1.0 from Sep 10 and a push from the 14th — ALIVE. Kotatsu archived Nov 2025 (documented), Yukimi too, and the family lives on in forks.
## The full chain

- **Kotatsu** — ★8,855 — the original; **archived Nov 4, 2025** (confirmed at its house) — and the community didn't sit still
- **Yukimi** — archived too (Nov 2025, checked): the link that passed the torch
- **Usagi** — ★257 · **release 1.0 from Sep 10** · push from Sep 14 · **ALIVE** · github.com/UsagiApp/Usagi

## The tree's four living ones

- **Kotatsu-Redo** — ★867 · 9.8.3 (Sep 6) — the original's community fork
- **Futon** — ★427 · 9.8.1 (Aug 16) — with its own parser library
- **Kototoro** — ★569 · **v2.1.3 from TODAY** — the manga+novels+video branch
- **Usagi** — the chain's living one

## Plugins and parsers

**Gekkoushi/plugin** and **plugin-source** — ★90 · GPL-3.0 · push from Sep 13 · v1.2.6 — this is where you contribute and report broken sources · **InvalidDavid/UMA** — ★69 — plugin installs with tags from Sep 12 and 13.

**The week's impostors:** a litter with inflated, identical stars (115–120 thousand), recent birth and classified-ad titles. Not a single open house. Named without linking.
> —Hey, did Usagi die?
> —The rumor died. The house pushed code this week.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Usagi is alive — the Kotatsu → Yukimi → Usagi chain (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 07 (Sep 15) · **Verified:** today, September 15, 2026

It's going around the groups: "Usagi got archived", "Usagi died". It was verified AT THE HOUSE, and re-verified today: **FALSE.** This is what the house says, with a date:

**The full chain:**
- **Kotatsu** — ★8,855 — the family's original; it **archived** on November 4, 2025 (confirmed at its home) — and the community didn't sit still
- **Yukimi** — archived too (Nov 2025, checked): the link that passed the torch
- **Usagi** — ★257 · **release 1.0 from Sep 10** · push from Sep 14 · **ALIVE** · github.com/UsagiApp/Usagi — the fork the community names first

**The tree's four living ones, counted tonight:**
- **Kotatsu-Redo** — ★867 · 9.8.3 (Sep 6) — the original's community fork
- **Futon** — ★427 · 9.8.1 (Aug 16) — with its own parser library
- **Kototoro** — ★569 · **v2.1.3 from TODAY** — the branch that joined manga+novels+video
- **Usagi** — the chain's living one

**Plugins and parsers (how this tree eats):**
- **Gekkoushi/plugin** and **plugin-source** — ★90, GPL-3.0, push from Sep 13, v1.2.6 — this is where you contribute and report broken sources
- **InvalidDavid/UMA** — ★69 — automatic or manual plugin installs, with tags from Sep 12 and 13

**The week's impostors:** a litter in the same suit — inflated and identical stars (115–120 thousand), recent birth, classified-ad titles. Not a single open house. Named without linking.

The house meme:
> —Hey, did Usagi die?
> —The rumor died. The house pushed code this week.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
