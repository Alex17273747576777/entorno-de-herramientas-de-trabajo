# Pieza 06 — Forks de lectores: el mapa vivo de Mihon, Aniyomi y sus segundas generaciones

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `6755c7f1909c` · ES-TG `4b878161720f` · EN-Reddit `9fad998c787b` · EN-Discord `789f6b13248f`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 06 — Forks de lectores: el mapa vivo de Mihon, Aniyomi y sus segundas generaciones

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── ⚖️ La regla: fork no es criterio
├── 🌳 El árbol completo de hoy
├── 📱 Las fichas de los vivos
├── 🧬 Qué es un «fork de verdad» (y qué es un rehijo)
├── 🏗️ La infraestructura que nadie ve
├── 📜 Licencias, dicho sin bufete
├── 🚩 Señales de impostor
├── 🔍 Cómo leer un repo en diez minutos
├── 🔄 Backups y mudanzas de biblioteca
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Tachiyomi — el lector de manga libre que marcó una época — cerró su núcleo en enero de 2024. Lo que quedó no es «Tachiyomi con otro nombre»: es una familia de proyectos distintos, con dueños, ritmos y licencias propias. Este mapa se leyó HOY, 14 de septiembre, repo por repo:

```
━━ El tronco manga ━━
Mihon              ★23.601   v0.20.4 (5-ago)    push HOY (15-sep)
TachiyomiSY        ★4.146    1.13.2 (13-jul)    push 13-sep    fork
TachiyomiSYPreview ★483      host de previews   push 25-ago
Komikku            ★4.721    v1.14.1 (17-jul)   push 11-sep  rehijo
Neko               ★2.792    lector MangaDex    push 14-sep     especialista

━━ La rama anime (manga + anime) ━━
Aniyomi            ★7.683    push 14-sep         rama madre
Anikku             ★1.032    v0.2.0 (11-sep)    anime, org Komikku
Aniyomi-preview    ★641      host de previews   push 14-sep
Animetail          ★579      v0.20.4.0 (5-ago)  push 7-sep   fork
Tadami             ★260      v0.62 (12-sep)     push 13-sep  fork (viva)

```

Ninguna estrella instala nada. Ningún parentesco garantiza nada. La regla va primero.

## ⚖️ La regla: fork no es criterio

Que algo sea fork, variante o rebautizo de un proyecto querido no es, por sí solo, razón para usarlo. Las cuatro puertas que sí cuentan:

```
Uso real          alguien de carne y hueso lo usa
                  y puede contar qué tal
Unicidad          ¿hace algo que lo que ya tienes
                  no cubre? «Es fork de X» no es
                  una función
Madurez pública   docs, versiones firmadas, un autor
                  que responde. Último push de 2024
                  no pasa esta puerta sin marca
Propósito propio  un icono nuevo no es un propósito;
                  un cambio de motor, sí
```

Esta guía nombra repos con URL, licencia, versión y último push — leídos el 14 y re-leídos al mudar (15-sep). «El mejor» no aparece: no existe en abstracto. Existe el que cubre lo que lees, con taller abierto.

## 🌳 El árbol completo de hoy

```
Mihon (el tronco vivo del ecosistema)
   ├── Mihon            el sucesor de hecho (el más grande)
   ├── TachiyomiSY      el fork clásico que sigue vivo
   ├── Komikku          rehijo con vida propia (repo nuevo)
   ├── Neko             el especialista en MangaDex
   └── (decenas de forks sin proyecto propio:
        no se listan por ser forks)

Aniyomi (manga + anime, del mismo linaje)
   ├── Animetail        se declara «Official fork»
   ├── Tadami           manga + anime + ranobe (el más joven)
   └── Anikku           el anime-client de la org Komikku

Kotatsu: OTRO árbol (GPL, parsers propios)
   → Kotatsu-Redo, Futon, Kototoro, Usagi
   → tienen guía propia en esta familia
```

## 📱 Las fichas de los vivos

### Mihon — el tronco

https://github.com/mihonapp/mihon

★23.601 · versión 0.20.4 (5 de agosto) · push de HOY (re-verificado 15-sep) · Apache-2.0. Es el lector manga libre más grande del mapa, y el sucesor de hecho de Tachiyomi. Su comunidad de traducciones empuja código a diario; sus versiones salen cuando salen — la de agosto es la vigente, y el push de hoy no significa APK nuevo.

Keiyoushi (la guía de extensiones de esta familia) lo nombra primero en su lista de apps compatibles.

### TachiyomiSY — el vivo con el nombre viejo

https://github.com/jobobby04/TachiyomiSY

★4.146 · versión 1.13.2 (13 de julio) · push del 13-sep · Apache-2.0. El fork clásico — fuentes extra, ajustes de lectura — que sigue abierto. Y el aviso que vale su entrada: el SY vivo es este — el nombre no basta; el dueño sí.

Su proyecto madre mantiene además un host de builds de prueba: TachiyomiSYPreview (★483) — versiones experimentales para curiosos, no la vía del día a día.

### Komikku — el rehijo con taller propio

https://github.com/komikku-app/komikku

★4.721 · versión 1.14.1 (17 de julio) · push del 11-sep · Apache-2.0. La API de GitHub no lo declara fork (es un repo nuevo); su README cuenta el linaje. Son los «rehijos»: proyectos que heredan el código y nacen con su propia casa. Su organización también mantiene Anikku (abajo).

### Neko — el especialista

https://github.com/nekomangaorg/Neko

★2.792 · push de ayer (14-sep) · «Unofficial MangaDex Reader for Android 8+». Un lector entero dedicado a una sola fuente: MangaDex. Es del linaje de los forks de Tachiyomi, pero su propósito propio es clarísimo: hacer una cosa bien. Para quien vive en MangaDex, es ficha aparte; para el resto, es un martillo con forma de destornillador.

### Aniyomi y sus herederos

https://github.com/aniyomiorg/aniyomi

★7.683 · push del 14-sep · Apache-2.0. La rama madre del manga+anime. Casi un año sin versión nueva pero con código moviéndose este mes: rama madura, no cadáver. Su host de previews: aniyomiorg/aniyomi-preview (★641).

**Anikku** — https://github.com/komikku-app/anikku — ★1.032 · versión 0.2.0 publicada el 11 de septiembre · release r8932 a la vista HOY 15-sep · «anime watcher» de la organización Komikku. La más activa de la rama anime este mes.

**Animetail** — https://github.com/Animetailapp/Animetail — ★579 · v0.20.4.0 · push del 7-sep · Apache-2.0. Se declara «Official fork of Aniyomi» en su descripción. La etiqueta la pone él — no se vio sello de aniyomiorg ratificándolo; se dice tal cual.

**Tadami** — https://github.com/andarcanum/Tadami-Aniyomi-fork — ★260 · versión 0.62 (12 de septiembre) · push del 13-sep · Apache-2.0. **Rectificación (15-sep, noche): VIVA — ★260, push del 13-sep; el acta de la tarde se equivocó de casa (detalle en la Publicación 13).** El más joven de la rama: tres versiones en un mes (0.60 → 0.62), manga + anime + novelas ligeras (ranobe). De los forks declarados, el que más rápido evoluciona.

## 🈁 La capa de inmersión (guía propia en la pieza 17)

El mapa de hoy estrena territorio: dos proyectos vivos de la capa japonesa del ecosistema. **Chimahon** (★198, GPL-3.0, v2.4.2 de HOY 15-sep) es un fork de Mihon para estudiar leyendo: diccionario nativo Yomitan, manga Mokuro, novelas EPUB y minado instantáneo a Anki. **Yomi Reader** (★10, Apache-2.0, v0.1.7 del 6-sep) es el triple joven — anime, manga y novela — compatible con extensiones Tadami/Aniyomi. Las fichas completas, con Hoshi Reader, Yomikai y el cliente Komga «Koharia», viven en la pieza 17.

## 🧬 Qué es un «fork de verdad» (y qué es un rehijo)

El grafo de GitHub y la realidad no siempre coinciden:

```
Fork declarado   la API lo dice: campo fork = true,
                 con padre visible. Animetail, Tadami. No se discute.

Rehijo           repo NUEVO que hereda el código y declara
                 el linaje en su README. Mihon, Komikku,
                 Anikku. El grafo dice «no es fork»;
                 el README dice de dónde viene. Ambos
                 son verdad: por eso se leen los dos.

Host de builds   no es una app: es un aparato de lanzamiento
                 de versiones de prueba del proyecto madre.
                 SYPreview, aniyomi-preview.

Fork de fork     lo que monta el contraejemplo: copia de
                 una copia sin taller propio. Suele morir
                 sin anunciarlo.
```

Cuando alguien te recomiende «un fork», la pregunta útil no es ¿de quién es hijo? sino ¿quién empuja código esta semana?

## 🏗️ La infraestructura que nadie ve

Dos piezas del ecosistema no son lectores pero sostienen a todos:

**SyncYomi** — https://github.com/syncyomi/syncyomi — ★710, push de ayer (14-sep) · v1.5.4 (10-sep). Sincronización de bibliotecas entre dispositivos y entre forks del linaje Tachiyomi: tu progreso te sigue si cambias de lector de la familia. Un servidor ligero y el cliente en el teléfono.

**Suwayomi** — el servidor de escritorio del ecosistema (tu biblioteca corriendo en la PC, leída desde el navegador). Su extensión se revisó en la guía de extensiones de esta familia; el proyecto vive con actividad de este mes.

Nombrarlos aquí es evitar el error clásico: confundir la app con la capa que la acompaña.

## 📜 Licencias, dicho sin bufete

Lo que la página de cada repo declaró el día de la verificación (14-sep):

- **Apache-2.0** — Mihon, TachiyomiSY, Komikku, Aniyomi, Animetail, Tadami. En términos generales: usar, modificar y redistribuir conservando los avisos y la nota de cambios.
- **GPL-3.0** — el árbol Kotatsu (Kotatsu-Redo, Futon, Usagi, Kototoro en su licencia declarada). Quien redistribuye modificaciones, las distribuye con la misma licencia.

Esto no es asesoría legal: es el campo de licencia de cada página, leído hoy. Si alguien va a redistribuir un APK con modificaciones, que abra el texto completo de la licencia ese día. Y un aviso que vale oro: un APK «SY mod premium» en una tienda de mods NO hereda la confianza de Apache-2.0 del repo — hereda la de la tienda.

## 🚩 Señales de impostor

- Estrellas altas, último commit de 2024, README que promete «active development».
- Mismo nombre, otro dueño — y los impostores de SEO de esta semana (títulos de anuncio, estrellas clónicas).
- APK en Telegram «más actualizado que GitHub». Lo actualizado vive en Releases, con tag y fecha.
- «Nightly» sin CI, sin tag, sin registro de compilación.
- Fork de un proyecto archivado que no declara su parentaje.
- Pide pegar un índice de extensiones en el primer pantallazo.

Ninguna señal sola basta. Varias juntas, paras.

## 🔍 Cómo leer un repo en diez minutos

```
1. Abre el HTML del repo, no un recorte de un grupo.
2. ¿Dice Archived? Los muertos se leyen igual de rápido.
3. Licencia: el campo de la página (o el archivo LICENSE).
4. Releases: tag y fecha de la última versión.
   El push de hoy no es una versión nueva.
5. pushed_at ≠ release: un repo puede empujar
   traducciones todo el mes sin sacar APK.
6. ¿Es fork? El campo fork de la página/la API lo dice;
   si es rehijo, el README lo cuenta.
7. ¿El autor responde issues? Míralo en dos hilos al azar
   antes de fiarte tu biblioteca.
```

## 🔄 Backups y mudanzas de biblioteca

Lo que se puede decir sin recetar nada:

- Cada lector de la familia tiene su formato de respaldo; los formatos se parecen, no se garantiza que sean iguales entre versiones ni entre primos.
- Un respaldo de 2024 no está verificado contra la versión de agosto de 2026 — de ningún lector.
- «Exportas y listo» es una promesa de publicidad, no de ingeniería: prueba SIEMPRE en copia, nunca sobre tu única biblioteca.
- Si tu progreso te importa, SyncYomi (arriba) existe para eso — y también respalda al respaldar: exportación manual periódica.
- El episodio de respaldos de Kototoro (serie 1.4–1.7) está documentado en su propia guía; vale como recordatorio de que las migraciones grandes se ensayan en vacío.

## ❓ Preguntas frecuentes

**¿Cuál instalo?**
El que uses y verifiques. Manga en general: Mihon es el tronco con más comunidad. Estilo clásico SY con extras: TachiyomiSY de jobobby04. MangaDex exclusivamente: Neko. Anime además del manga: Aniyomi o sus herederos (Anikku es la que más se movió este mes). Ninguna recomendación sustituye abrir el release el día que instalas.

**¿Mihon es Tachiyomi?**
No. Tachiyomi cerró. Mihon es otro repo, vivo hoy, que heredó el modelo.

**¿Komikku o TachiyomiSY?**
Dos vivos con estilo distinto. Hoy Komikku tiene más estrellas (4.721 vs 4.146); SY empujó el 13-sep y Komikku el 11 — constancias del 14, ambos vivos a 15. Ningún número elige por ti.

**¿Anikku es AniZen?**
No — pero es familia. AniZen se declara rebrand de «Anikku Mod» (tiene guía propia en esta familia). Anikku es la app de la organización Komikku, con versión 0.2.0 del 11 de septiembre. Parentela declarada, repos distintos.

**¿Neko sirve para todo?**
Para MangaDex, de maravilla. Para el resto del universo manga, usa un lector general.

**¿Los hosts de «preview» son para instalar?**
Son para probar y reportar. Para el día a día, la versión estable del repo madre.

**¿Y los 200 forks que no listaste?**
Ser fork no puntúa. Los que tienen proyecto propio están arriba; los que no, son copias con reloj.

**¿Discord?**
Esta familia no tiene canal de envío por Discord. Sus guías viven aquí.

## 🔗 Enlaces

- Mihon: https://github.com/mihonapp/mihon
- TachiyomiSY: https://github.com/jobobby04/TachiyomiSY · previews: https://github.com/jobobby04/TachiyomiSYPreview
- Komikku: https://github.com/komikku-app/komikku · Anikku: https://github.com/komikku-app/anikku
- Neko: https://github.com/nekomangaorg/Neko
- Aniyomi: https://github.com/aniyomiorg/aniyomi · previews: https://github.com/aniyomiorg/aniyomi-preview
- Animetail: https://github.com/Animetailapp/Animetail · Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork
- SyncYomi: https://github.com/syncyomi/syncyomi
- Extensiones del ecosistema: guía 04 de esta familia · Árbol Kotatsu: guía 07

> La Bandita informa a partir de fuentes fechadas. Un fork no es una razón. El repo vivo sí. Y el dueño, más.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: 8 fichas re-contadas (Mihon ★23.601, Komikku ★4.721, SY ★4.146, Neko ★2.792, Anikku ★1.032 + r8932) y rectificación Tadami (viva). Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Forks de lectores — las segundas generaciones, contadas HOY

Fork no es criterio: cuenta la casa, la cadencia y la propuesta.

- **Mihon** ★23.601 · v0.20.4 · push HOY · **TachiyomiSY** ★4.146 (el vivo: jobobby04)
- **Komikku** ★4.721 · v1.14.1 · **Neko** ★2.792 · **Aniyomi** ★7.683 (2 releases el 14 tras 11 meses callada)
- **Anikku** ★1.032 · r8932 HOY · **Animetail** ★579 · **Tadami** ★260 (viva, acta de rectificación)
- **SyncYomi** ★710 — tu biblioteca te sigue entre forks

**Repo en 10 min:** pushes · releases etiquetadas · README honesto · issues vivos.
*Fuente: pieza 6 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 06 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Cuál fork es el bueno? —El que tenga push de esta semana y cuente su genealogía sin vergüenza.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# I verified the Tachiyomi forks today: Mihon, SY, Komikku, Aniyomi and the rest of the family with their numbers
**Reddit · ingles-US · fuente: pieza 6 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** The rule: fork is not a criterion — the house, the cadence and the proposal count. Today: Mihon ★23,601 (push TODAY), SY ★4,146, Komikku ★4,721, Neko ★2,792, Aniyomi ★7,683, Anikku ★1,032, Animetail ★579, Tadami ★260 (alive, rectified).
## Tonight's table (all counted TODAY, Sep 15)

- **Mihon** — ★23,601 · v0.20.4 (Aug 5) · **push from TODAY** — the de facto successor · github.com/mihonapp/mihon
- **TachiyomiSY** — ★4,146 · 1.13.2 (Jul 13) · push from the 13th — the classic "SY"; the living one is **jobobby04** · **SYPreview** — ★483 (test builds)
- **Komikku** — ★4,721 · v1.14.1 (Jul 17) — the re-child with its own organization · github.com/komikku-app/komikku
- **Neko** — ★2,792 · push from the 14th — the MangaDex specialist
- **Aniyomi** — ★7,683 · push from the 14th — two releases on the 14th broke 11 months of silence
- **Anikku** — ★1,032 · v0.2.0 (Sep 11) · r8932 in sight TODAY — anime-only from the Komikku org
- **Animetail** — ★579 · v0.20.4.0 — the fork that pulled the Mihon core inside
- **Tadami** — ★260 · v0.62 (Sep 12) · push from the 13th — **alive**: the afternoon 404 belonged to ANOTHER slug; it premiered an organization (tadamiorg, ★56)

## The infra nobody sees

**SyncYomi** — ★710 · v1.5.4 (Sep 10) — syncs your library across the lineage's devices and forks.

**Licenses:** Apache-2.0 across almost the whole family (use, modify, redistribute keeping notices). **Impostors:** named without linking. **A repo in 10 minutes:** recent pushes · tagged releases · an honest README · living issues.
> —Which fork is the good one?
> —The one with a push this week that tells its genealogy without shame.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Reader forks — the second generations, counted TODAY (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 06 (Sep 15) · **Verified:** today, September 15, 2026

Tachiyomi closed its core in January 2024. What remained isn't "Tachiyomi with another name": it's a family with different trades. **The channel's rule: fork is not a criterion** — for good or bad; what counts is the house, the cadence and the proposal.

**Tonight's table (all counted TODAY, Sep 15):**
- **Mihon** — ★23,601 · v0.20.4 (Aug 5) · **push from TODAY** — the de facto successor · github.com/mihonapp/mihon
- **TachiyomiSY** — ★4,146 · 1.13.2 (Jul 13) · push from Sep 13 — the classic "SY" · the living one is **jobobby04** (the name isn't enough: the owner is)
- **TachiyomiSYPreview** — ★483 — test builds, not the daily road
- **Komikku** — ★4,721 · v1.14.1 (Jul 17) — the re-child with its own organization · github.com/komikku-app/komikku
- **Neko** — ★2,792 · push from Sep 14 — the MangaDex specialist · github.com/nekomangaorg/Neko
- **Aniyomi** — ★7,683 · push from Sep 14 — the mother branch manga+anime; its two releases on the 14th broke an 11-month release silence
- **Anikku** — ★1,032 · v0.2.0 (Sep 11) · **r8932 in sight TODAY** — anime-only from the Komikku org
- **Animetail** — ★579 · v0.20.4.0 — the fork that pulled the Mihon core inside
- **Tadami** — ★260 · v0.62 (Sep 12) · push from Sep 13 — **alive**: the afternoon 404 belonged to ANOTHER slug; the project also premiered its organization (tadamiorg, ★56)

**The immersion layer (in piece 17):** Chimahon — ★198, v2.4.2 from TODAY — the Mihon fork for learning Japanese while you read.

**The infra nobody sees:** **SyncYomi** — ★710 · v1.5.4 (Sep 10) — syncs your library across devices and across the lineage's forks. Your progress follows you.

**Licenses, said without a law office:** Apache-2.0 across almost the whole family (Mihon, SY, Komikku, Aniyomi, Animetail, Tadami): use, modify and redistribute keeping the notices.

**The impostors:** repos with serious projects' names and fake stars. Named without linking.

**How to read a repo in 10 minutes:** recent pushes · tagged releases · a README that says where it comes from · living issues. Four yeses and there's a home.

The house meme:
> —Which fork is the good one?
> —The one with a push this week that tells its genealogy without shame.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
