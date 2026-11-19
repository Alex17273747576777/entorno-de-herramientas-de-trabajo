# Pieza 01 — Tiendas de APK: la tienda legal, el letrero de mods y el reloj de 2027

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `428c83d0029d` · ES-TG `45274e8029b7` · EN-Reddit `40c34c3640a0` · EN-Discord `557d4dde075d`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 01 — Tiendas de APK: la tienda legal, el letrero de mods y el reloj de 2027

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🏪 Las tiendas que sí (ficha por ficha)
├── 🧰 Los instaladores que traen las tiendas a ti
├── ⚠️ Los letreros de mods (se nombran, no se recetan)
├── 🕐 El reloj de 2027 y la puerta chica
├── 🧭 Qué mirar antes de instalar cualquier APK
├── 🚩 Señales de cebo
├── ❓ Preguntas frecuentes
├── 📚 Palabras clave de esta guía
└── 🔗 Enlaces

## ⚡ En una página

Una tienda de APK es un lugar con dueño conocido que te deja instalar aplicaciones fuera de la tienda oficial del teléfono. Hay de dos clases: las que revisan, firman y se hacen responsables de lo que publican — y las que viven de tráfico de mods, donde el «premium gratis» llega con regalo sorpresa dentro del archivo.

Esta guía recorre las tiendas legítimas de ecosistema libre, una por una, con su estado real a 15 de septiembre de 2026: cuál está bajo amenaza, cuál estrenó versión ayer, cuál cambió de casa hace días. Y termina con el reloj: la política de verificación de desarrolladores de Google ya tiene cuenta regresiva pública.

Si vienes por «Spotify premium gratis» o «juegos con todo desbloqueado», esta guía no te va a acompañar: eso no es una tienda, es un anzuelo con cartera.

## 🏪 Las tiendas que sí (ficha por ficha)

### F-Droid — la casa madre

https://f-droid.org

La tienda histórica del software libre en Android. Todo lo que publica pasa por compilación reproducible: el archivo que descargas se puede reconstruir desde el código público, y si no coincide, no sale. Esa es la promesa de fondo, y es la que ninguna tienda de mods puede igualar.

Lo visto el 14-sep: el sitio mantiene su banner de campaña — «F-Droid is under threat» — en el marco del programa de verificación de desarrolladores de Google que esta misma guía cronometra más abajo. El instalador de la propia tienda se descarga directo de su sitio.

Si solo vas a elegir una tienda de esta lista, elige esta. Es la más vieja, la más revisada y la que tiene el estándar de publicación más exigente del ecosistema libre.

```
F-Droid en una caja
Qué es:      tienda y repositorio de apps libres
Promesa:     compilación reproducible, sin rastreadores declarados
Estado a su día (14-sep):  viva, con campaña activa «under threat»
Para quién:  todo el mundo; es el punto de entrada natural
```

### IzzyOnDroid — el anexo respetado

https://apt.izzysoft.de/fdroid

El repositorio complementario más conocido del ecosistema F-Droid: muchas apps que aún no entran al canal principal se publican primero aquí. Es un almacén de confianza dentro de la comunidad, mantenido desde hace años.

Lo visto el 14-sep: el sitio responde; su carga depende de JavaScript, así que el navegador lo monta a su ritmo. Nada alarmante: es el mismo sitio de siempre.

### Droid-ify — el cliente F-Droid moderno

Repositorio canónico: https://codeberg.org/droidify/client
Espejo en GitHub: https://github.com/Droid-ify/client

Un cliente para consumir catálogos tipo F-Droid con interfaz moderna. La versión 0.7.8 salió el 12 de septiembre: trae corrección del repositorio tras importarlo, importar por código QR, instalador para quien tiene root, y tema adaptativo Material You.

Detalle que importa: el proyecto declara que su casa oficial es Codeberg y que su página de GitHub es solo espejo. Cuando un proyecto nombra canónico a otro dominio, ese es el enlace que manda — la regla de esta guía es simple: lo canónico primero.

```
Droid-ify en una caja
Qué es:      cliente de repositorios F-Droid
Última:      0.7.8 — 12 de septiembre de 2026
Casa:        codeberg.org/droidify/client (GitHub es espejo)
Extras:      QR, instalador root, tema dinámico
```

### Neo-Store — el cliente con brújula de rastreadores

https://github.com/NeoApplications/Neo-Store

Otro cliente del ecosistema F-Droid, con detalles de usabilidad que su comunidad cuida. Su movimiento más reciente (commit del 13 de septiembre) es una joya de diseño: está reemplazando el bloque estático de rastreadores de cada ficha por acciones de control — y te da un atajo a Exodus Privacy para auditar cualquier app instalada.

Eso es una idea de tienda madura: no solo dejarte instalar, sino darte el instrumento para saber qué instala. La versión estable es la 1.2.6.

### Komi Store — la que cambió de casa (y lo dice a gritos)

https://github.com/komi-store/komi-store
Sitio: https://komistore.app

Esta ficha existe porque el cambio de casa confunde. Komi Store antes se llamaba «GitHub Store» y vivía en otra organización; migró a la organización komi-store, estrenó dominio propio (komistore.app) y va por la versión 1.9.3 (código 22). El movimiento está declarado por el propio proyecto en su repositorio — 18.500 estrellas y actividad de principios de septiembre.

La diferencia entre «migró» y «lo clonaron» es esta: la migración la anuncia el dueño, en el repo, con historial. El clon aparece de la nada, con el nombre de otro y prisa de que instales. Komi hizo lo primero.

### Aurora Store — la puerta a otro catálogo

https://gitlab.com/AuroraOSS/AuroraStore

El cliente libre que consulta el catálogo de la tienda de Google sin rendir tu cuenta: sesiones anónimas, búsquedas y actualizaciones, sin exponer tu identidad principal. Es de las piezas más instaladas del ecosistema libre y tiene infraestructura seria detrás.

Lo visto el 14-sep: la versión etiquetada más reciente es la 4.8.4, con actividad de repositorio de las últimas semanas. Y un detalle que dice mucho del proyecto: su commit más reciente de documentación es exactamente esto — «declarar el uso de IA en el desarrollo». Transparencia declarada de forma voluntaria. Eso, en una tienda de mods, no existe ni va a existir.

### Accrescent — la joven con estándares altos

https://accrescent.app

La tienda más joven de la lista, en fase alpha, con Android 10 como mínimo. No es «una F-Droid más»: su apuesta es seguridad de entrada — verificación estricta de firmas (key pinning), metadatos firmados, actualizaciones automáticas sin privilegios adicionales en Android 12 o superior, soporte de APK divididos y cero cuentas.

También se encuentra dentro de la tienda de GrapheneOS, que es un buen termómetro de a quién le hace caso la comunidad paranoica por buenas razones.

```
Accrescent en una caja
Qué es:      tienda centrada en seguridad, en alpha
Mínimo:      Android 10
Firma:       key pinning + metadatos firmados
Cuentas:     ninguna
Vía:         sitio propio y tienda de GrapheneOS
```

### Appteka — el mercado de comunidad (con lupa)

https://appteka.store
Código del cliente: https://github.com/solkin/appteka-android

Un mercado gestionado por comunidad con catálogo grande (declara 320.000 aplicaciones) y cliente propio: la versión oficial del cliente es la 23.0, pesa menos de 4 MB y pide Android 6 en adelante. El sitio vive y responde.

Va en la lista de «sí» pero con lupa: al ser catálogo de comunidad, el estándar de publicación no es el de F-Droid. Sirve, y a cambio pide lo que toda esta guía repite: mirar el dueño del archivo antes de instalar.

Dentro de Appteka viven fichas de apps concretas que esta guía cita como ejemplo de estado — por ejemplo, las páginas de los dos proyectos Rebuild, abiertas hoy con la versión 23.0 del cliente visible en los títulos. Se citan como ejemplo de vida del mercado, no como recomendación de esas apps concretas.

## 🧰 Los instaladores que traen las tiendas a ti

Los últimos años trajeron una figura nueva: herramientas que no son tiendas con escaparate, sino instaladores que construyen tu propia tienda a medida, siguiendo los repositorios que tú les señalas.

### Obtainium — la app que vigila los repositorios por ti

https://github.com/ImranR98/Obtainium

La más popular de su especie: le dices qué repositorios te importan y ella vigila sus lanzamientos, descargando e instalando las versiones nuevas apenas salen. A HOY 15-sep suma cerca de 19.700 estrellas y commits de ayer — de los proyectos más vivos de todo este mapa.

Su propio README acredita a ObtainX como el instalador externo del ecosistema. Eso también es señal de madurez: saber nombrar a los vecinos.

### ObtainX — el brazo instalador

https://github.com/bikram-agarwal/ObtainX

Vivo (constado el 14-sep). Complemento de instalación del ecosistema Obtainium: el eslabón entre «detecté una versión nueva» y «queda instalada en el teléfono».

### Omnify — el cliente F-Droid sin ruido

https://github.com/Victor-root/Omnify
Sitio: https://victor-root.github.io/Omnify/

Vivo a su día (14-sep), con su landing cargando: se presenta como «un cliente F-Droid sin desorden que instala aplicaciones desde cualquier parte». De las apuestas nuevas por hacer el consumo de catálogos libres más amable.

```
Los tres en una frase
Obtainium:  vigila releases y te avisa
ObtainX:    ejecuta la instalación
Omnify:     cliente F-Droid ligero
Ninguna de las tres te pide salir de la vía legal.
```

## ⚠️ Los letreros de mods (se nombran, no se recetan)

Estos nombres existen para que los reconozcas, no para que los visites:

- **Espacio APK** — sitio vivo (constado el 14-sep), catálogo de «apps y juegos populares». Su producto real: mods con promesas premium.
- **HappyMod** — respondió el 14-sep sin título legible (escudo anti-bot). Su modelo de negocio: subir mods subidos por cualquiera, sin cadena de custodia seria.
- **Liteapks** — vivo (constado el 14-sep), se anuncia como «#1 en MOD APK». El número uno en mods es, por definición, el número uno en archivos sin revisión.

El patrón común: te prometen lo de pago gratis, te piden permisos que la app original no pide, y si algo sale mal no hay ni repo ni dueño al que reclamar. El «mod» muchas veces ni siquiera es la app original: es otra app disfrazada con su icono.

Aquí no van enlaces. El nombre ya cumple su función: si te aparece en un grupo con «descárgalo de aquí», ya sabes qué es.

## 🕐 El reloj de 2027 y la puerta chica

El marco que cambia todo esto tiene fecha y reloj público.

El plan de Google — «verificación de desarrolladores de Android» — exige que las apps de dispositivos certificados estén registradas por desarrolladores verificados. El 30 de septiembre de 2026 toca el primer hito: cuatro países (Brasil, Indonesia, Singapur, Tailandia), siete tiendas (Google Play, HONOR, OPPO, Galaxy Store, Palm Store, V-Appstore y GetApps), Android 7 en adelante.

En 2027 el filtro llega a todas las apps de dispositivos certificados. La campaña Keep Android Open mantiene hoy su contador público: 110 días — y su FAQ ya sitúa el bloqueo alrededor de enero de 2027. Dos calendarios, el mismo mensaje: el tiempo del sideloading tal como lo conocemos está contado.

La puerta chica que Google abrió este mes: las cuentas de distribución limitada. Para estudiantes, docentes y aficionados — hasta 20 dispositivos, sin identificación gubernamental y sin tarifa. Es un alivio pequeño con techo duro: veinte aparatos no sostienen un proyecto comunitario.

```
El reloj, en dos líneas
30-sep-2026: 4 países, 7 tiendas, Android 7+
2027:        todas las apps, dispositivos certificados
Contador de la campaña (al 14-sep): 110 días
```

Lo que esto significa para el ecosistema libre: F-Droid con su banner de amenaza, Accrescent construyendo seguridad desde hoy, y cada tienda de esta guía sabiendo que su modelo se juega el futuro en los próximos meses. Nadie de esta lista se queda quieto — y esa es, quizá, la mejor señal de todas.

## 🧭 Qué mirar antes de instalar cualquier APK

```
1. ¿De dónde sale?
   Repo o sitio con historial > enlace de un grupo.

2. ¿Quién firma?
   El proyecto declara su firma; si el archivo no
   coincide con esa firma, es otra cosa.

3. ¿Qué pide?
   Permisos que la app original no piden = motivo.

4. ¿Está en más de una tienda seria?
   F-Droid + repo propio + IzzyOnDroid = triple vía.
   Solo en un sitio de mods = ninguna vía.

5. ¿Qué dicen los audita-dores?
   Exodus (rastreadores), VirusTotal (multiples motores),
   el repo del proyecto (issues reales de usuarios).

6. ¿Hay prisa?
   «Últimas 24 horas con este link» es la gramática
   del cebo. Lo bueno sigue ahí mañana.
```

## 🚩 Señales de cebo

- El anuncio de arriba del buscador «descarga X» paga más caro que el resultado legítimo. El que paga el anuncio no es el proyecto.
- «Versión modificada», «premium desbloqueado», «todo ilimitado»: modificó alguien algo — lo que no te dice es qué más metió dentro.
- La página te pide desactivar la protección del teléfono para «completar la instalación». Ninguna tienda seria necesita que te bajes los pantalones de seguridad.
- Comentarios clonados en varias páginas con las mismas frases.
- El candado del navegador: solo dice que la conexión está cifrada. El banco lo tiene, y el phishing también.

## ❓ Preguntas frecuentes

**¿Con cuál empiezo si vengo de cero?**
F-Droid. Es la puerta con más historia, más revisión y más comunidad. De ahí cuelga el resto: IzzyOnDroid como anexo, y el cliente que prefieras (Droid-ify o Neo-Store) para manejar el catálogo con comodidad.

**¿Las apps de F-Droid son 100% seguras?**
Ninguna tienda promete eso. F-Droid promete transparencia: compilación reproducible y política declarada. Es el estándar más alto del ecosistema libre, no una varita.

**¿Por qué hay dos casas para Droid-ify (Codeberg y GitHub)?**
Porque el proyecto lo declara así: Codeberg es canónico, GitHub espejo. Cuando un proyecto declara su casa, la casa manda. Es la misma lógica de «el repo vivo sí» que esta familia de guías repite.

**¿Komi Store y «GitHub Store» son la misma?**
Sí — migró de organización y lo documenta en su repo, con dominio propio. La migración la cuenta el dueño; el clon no tiene dueño que cuente.

**¿Aurora Store es «la tienda de Google ilegal»?**
No. Es un cliente libre que consulta ese catálogo sin tu cuenta. El proyecto lo declara y lo mantiene con actividad reciente — hasta declara en su documentación cuándo usa IA en el desarrollo.

**¿Las cuentas de distribución limitada me sirven para «distribuir» mi app al grupo?**
Veinte dispositivos es un circuito cerrado: pruebas, clase, casa. Para algo más ancho, la vía es otra (y cada vía exige lo suyo).

**¿Y los mods? ¿Nunca?**
Esta guía no los receta ni los enlaza. Si alguien insiste, que sea con la firma revisada y el riesgo firmado por quien insiste — que nunca es quien va a perder los datos.

**¿El 30 de septiembre me bloquea el teléfono?**
No. Ese hito toca tiendas participantes en cuatro países. Tu cambio llega con el despliegue global de 2027. Reabre esta guía el día que decidas algo: el mapa se mueve.

## 📚 Palabras clave de esta guía

```
APK         el paquete instalable de una app Android
Sideload    instalar fuera de la tienda del sistema
Reproducible  el archivo sale igual recompilado desde el código
Key pinning   la firma del proyecto está atada de antemano
Split APKs  el paquete viene en partes por arquitectura
Exodus      auditoría pública de rastreadores en apps
Repo        repositorio: la casa del código (y de la verdad)
```

## 🔗 Enlaces

- F-Droid: https://f-droid.org
- IzzyOnDroid: https://apt.izzysoft.de/fdroid
- Droid-ify (canónico): https://codeberg.org/droidify/client · espejo: https://github.com/Droid-ify/client
- Neo-Store: https://github.com/NeoApplications/Neo-Store
- Komi Store: https://github.com/komi-store/komi-store · https://komistore.app
- Aurora Store: https://gitlab.com/AuroraOSS/AuroraStore
- Accrescent: https://accrescent.app
- Appteka: https://appteka.store · cliente: https://github.com/solkin/appteka-android
- Obtainium: https://github.com/ImranR98/Obtainium · ObtainX: https://github.com/bikram-agarwal/ObtainX
- Omnify: https://github.com/Victor-root/Omnify · https://victor-root.github.io/Omnify/
- Verificación de desarrolladores: https://developer.android.com/developer-verification
- Campaña: https://keepandroidopen.org

> La Bandita informa a partir de fuentes fechadas. La tienda legal te da algo que el mod nunca: un dueño al que exigirle.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: fecha de estado. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

**Nota de la verificación final (15-sep, noche):** el sitio propio de Omnify (victor-root.github.io/Omnify) devuelve 404 a esta hora, constado en vivo; la casa GitHub sigue viva (★20, v1.0.5-beta.6 del 4-sep). Los enlaces se reabren el día que se usan — regla de la casa.

### ▸ Telegram *(adaptación de canal)*

📌 Tiendas de APK legales — y el reloj de 2027

¿Dónde bajar sin regalo sorpresa? Tiendas con dueño y repos legibles:

- **F-Droid** — la madre (banner «under threat» por el programa de Google)
- **Appteka** — ★1.173 · v23.0 (ficha ANTES de fiarse)
- **Neo-Store** ★5.009 · **Droid-ify** ★7.420 · **Aurora Store**
- **Obtainium** — ★19.702 — te instala las versiones nuevas apenas salen

⚠️ Mods: Espacio APK, HappyMod, Liteapks — se nombran, NO se enlazan.
🕐 30-sep: piloto 4 países/7 tiendas · 2027: todo certificado. KAO: 110 días.
*Fuente: pieza 1 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 01 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Qué tienda es mejor? —La que te deja leer de dónde viene el APK antes de instalarlo.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# Legal APK stores and the 2027 clock: what to use, what to avoid, and the bait signs (verified today)
**Reddit · ingles-US · fuente: pieza 1 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** Stores with a known owner and readable repos: F-Droid, Appteka (★1,173 · v23.0), Neo-Store ★5,009, Droid-ify ★7,420, Aurora Store; Obtainium ★19,702 brings you versions straight from the repo. The mod storefronts get named, not prescribed.
## The stores that yes

- **F-Droid** — the free ecosystem's mother; today it keeps its "under threat" banner under Google's verification program
- **Appteka** (appteka.store) — community catalog; its repo stands at ★1,173 · v23.0 — read the listing BEFORE trusting it
- **Neo-Store** — ★5,009 — the no-clutter F-Droid client · github.com/NeoApplications/Neo-Store
- **Droid-ify** — ★7,420 — the material client, straight · github.com/Droid-ify/client
- **Aurora Store** — the door to Play without the Play account
- **Obtainium** — ★19,702 · commit from Sep 13 — tell it which repos you care about and it installs the new versions · github.com/ImranR98/Obtainium

## The mod storefronts (named, NOT prescribed)

Space APK ("popular apps" = promised premium mods) · HappyMod (anti-bot shield against probing) · Liteapks ("#1 in MOD APK"). Identical model in all three: upload whatever and let the ads pay.

## The 2027 clock

- Sep 30, 2026: first milestone — Brazil, Indonesia, Singapore and Thailand; 7 stores in the filter
- 2027: all apps on certified devices
- Keep Android Open campaign: 110 days as of the Sep 14 cutoff (checked on the front page)

**Bait signs:** an inflated version nobody else has · permissions the function doesn't paint · a "premium mod" of an app that's already free · a signature that changes between versions.

**Today's anti-finding:** Omnify's site (victor-root.github.io/Omnify) 404s tonight, checked live — its GitHub house lives (★20 · v1.0.5-beta.6 from Sep 4).
**House edit (Sep 15):** Omnify's own site returns 404, checked live; its GitHub house lives. The link gets reopened the day it's used.

> —Which store is better?
> —The one that lets you read where the APK comes from before installing it.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Legal APK stores — the listings and the 2027 clock (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 01 (Sep 15) · **Verified:** today, September 15, 2026

The channel's evergreen question: "where do I download without catching a surprise gift?" Short answer: stores with a known owner and repos you can read. Long answer below — with the 2027 clock running.

**The stores that yes:**
- **F-Droid** — the mother of the free ecosystem; today it keeps its "under threat" campaign banner under Google's verification program
- **Appteka** (appteka.store) — community catalog; its GitHub repo stands at ★1,173 · v23.0 — heads up: read the listing BEFORE trusting it (house rule)
- **Neo-Store** — ★5,009 — the no-clutter F-Droid client · github.com/NeoApplications/Neo-Store
- **Droid-ify** — ★7,420 — the material client, straight, no smoke · github.com/Droid-ify/client
- **Aurora Store** — the door to Play without the Play account

**The installers that bring the stores to you:**
- **Obtainium** — ★19,702, commit from Sep 13 — you tell it which repos you care about and it installs new versions as they ship · github.com/ImranR98/Obtainium

**⚠️ The mod storefronts (named, NOT prescribed):**
Space APK ("popular apps and games" = promised premium mods) · HappyMod (answered with an anti-bot shield) · Liteapks ("#1 in MOD APK"). The model is the same in all three: upload whatever and let the ads pay. None of them get in here.

**🕐 The 2027 clock:**
- Sep 30, 2026: first milestone — 4 countries (Brazil, Indonesia, Singapore, Thailand) and 7 stores in the filter
- 2027: all apps on certified devices
- Keep Android Open campaign counter: 110 days as of the Sep 14 cutoff (checked on their front page)

**Bait signs, the quick guide:** an inflated version nobody else has · permissions the function doesn't paint · a "premium mod" of an app that's already free · signature changes between versions.

**Today's anti-finding:** Omnify's own site (victor-root.github.io/Omnify) returns 404 tonight, checked live — its GitHub house is alive (★20, v1.0.5-beta.6 from Sep 4). The link gets reopened the day it's used.

The house meme:
> —Which store is better?
> —The one that lets you read where the APK comes from before installing it.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
