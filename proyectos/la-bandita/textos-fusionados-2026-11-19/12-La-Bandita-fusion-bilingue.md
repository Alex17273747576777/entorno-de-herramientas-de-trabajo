# Pieza 12 — FMHY es una wiki de pistas, no un catálogo: discovery ≠ verificación

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `de99064891a4` · ES-TG `7a4094c6af9a` · EN-Reddit `06d33b0d4673` · EN-Discord `f11652d3d899`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 12 — FMHY es una wiki de pistas, no un catálogo: discovery ≠ verificación

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🌐 Qué es FMHY y cómo funciona
├── 🧩 Lo que su navegación revela hoy
├── 🔒 El interstitial Base64 (qué es y qué no es)
├── 📦 El repo detrás de la wiki
├── 🧭 Discovery ≠ verificación: el embudo completo
├── 🔬 Un ejemplo real, de punta a punta
├── 📌 La corrección a la «gran ola» de abril
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

FMHY — «freemediaheckyeah» — se presenta como «la mayor colección de cosas gratis de internet». Es una wiki comunitaria enorme, viva hoy, y con un papel preciso en el mapa del conocimiento: **es un descubridor de primer nivel y un verificador de nada.**

La diferencia importa porque abril lo demostró con daño: alguien vació una porción de la wiki en un hilo de 340 mil caracteres y lo vendió como catálogo verificado. No lo era. Cada pista de FMHY es un primer eslabón — abrir la casa del proyecto, leer su licencia, comprobar su versión y su dueño es el trabajo que nadie puede hacer por ti, ni esta wiki ni esta guía.

Estado de hoy, 14 de septiembre: el sitio responde con su post mensual de septiembre activo, su guía de principiantes carga, y el repo que la genera suma ★14.592 — con la particularidad de que su código git no empuja desde mayo, y la wiki no por eso está muerta. Ambas cosas, contadas abajo.

## 🌐 Qué es FMHY y cómo funciona

https://fmhy.net

FMHY es una wiki mantenida por su comunidad: miles de entradas de herramientas, sitios y recursos organizados por categorías — privacy, AI, video, audio, gaming, reading, downloading, torrenting, educational, mobile, linux-macos, non-english, misc, entre otras. Su mecánica:

- La comunidad propone y curada entradas continuamente.
- Un changelog registra qué cambió — y su ritmo es visible: la wiki publica **posts mensuales de novedades** (el de septiembre de 2026 está en línea hoy).
- Hay variante SFW (sin contenido adulto) para quien la prefiera.
- La cultura del proyecto es la de un índice: describe, enlaza, no garantiza.

Su tamaño es su virtud y su límite: cubre todo, no audita nada. Es la biblioteca más grande del mundo en su género — y como toda biblioteca grande, el valor no está en tenerla toda: está en saber usar el catálogo.

## 🧩 Lo que su navegación revela hoy

La barra del sitio, abierta hoy, es una lección de lo que la wiki piensa de sí misma:

```
📑 Changelog    qué cambió y cuándo
📖 Glossary     el diccionario de sus términos
💾 Backups      cómo obtener la wiki entera
🌱 Ecosystem    las variantes y proyectos hermanos
❓ FAQs          las preguntas del proyecto
✅ SafeGuard    su capítulo de seguridad
🚀 Startpage    su propuesta de página de inicio
🔎 SearXNG      búsqueda propia
😇 SFW FMHY     la versión sin adulto
🏠 Selfhosting  cómone la montas en tu servidor
```

Fíjate en lo que esa barra dice sin decirlo: un proyecto que publica su changelog, mantiene glosario, ofrece backups de sí misma y tiene capítulo de seguridad se toma en serio como infraestructura. Sigue siendo un índice de pistas — pero de los organizados.

## 🔒 El interstitial Base64 (qué es y qué no es)

Al entrar, FMHY a veces muestra un aviso sobre enlaces codificados en Base64. Qué hay detrás, sin vueltas:

```
Es:    una medida de diseño. Algunos enlaces de la
       wiki se publican codificados para que los
       rastreadores automáticos no los indexen.
       El propio sitio ofrece un decodificador en página.

No es: un sistema de seguridad, ni un rito obligatorio,
       ni una instrucción de esta guía. El usuario
       decide si usa esa vía; el decodificador es
       del sitio y corre en tu navegador.

Y no es: motivo para copiar enlaces codificados en
       un post. Aquí van enlaces en claro o no van.
```

La wiki hace su ingeniería para sobrevivir a los indexadores; esta familia de guías hace la suya para no pegar recetas. Cada cual protege lo suyo.

## 📦 El repo detrás de la wiki

https://github.com/fmhy/FMHY

★14.592 · último push del 13 de mayo de 2026 · licencia: sin clasificar en su página (se dice tal cual — la wiki define su propia política de contenido en su sitio).

La curiosidad que enseña algo: el git lleva meses quieto y la wiki está viva — re-verificado HOY, 15-sep: carga con su post de septiembre. ¿Cómo? La wiki se sirve por vías propias (su web y sus despliegues) y el repo público no refleja cada movimiento. La lección general que ya viste en esta familia: **git quieto ≠ proyecto muerto; proyecto vivo ≠ todo verificado.** Un repo es una capa, no el proyecto entero.

## 🧭 Discovery ≠ verificación: el embudo completo

La regla de la casa cabe en una línea — encontrar no es verificar. Desplegado, el embudo que convierte una pista en algo citable:

```
1. DESCUBRIMIENTO
   FMHY (o un grupo, o un amigo) dice:
   «esta app es buena».
   ── esto vale exactamente cero como verificación.

2. APERTURA
   Se abre la casa del proyecto — su repo o sitio —
   ESE DÍA. No el recorte del grupo: la casa.

3. LECTURA
   ¿Quién es el dueño? ¿Desde cuándo existe?
   ¿Qué licencia declara? ¿Cuándo fue su última
   versión y su último push? ¿Está archivado?

4. CONTRASTE
   ¿Lo nombran otras fuentes independientes?
   ¿Su comunidad responde issues?
   ¿Su firma/checksums son públicos?

5. USO REAL
   ¿Alguien de carne y hueso lo usa y puede
   contar cómo le va? El uso real es la última
   puerta — y la única que nadie puede abrir por ti.

6. FICHA
   Recién entonces: una ficha con fecha, en una
   guía como esta. Y con fecha de caducidad.
```

Cualquier atajo que se salte pasos — «está en FMHY, punto», «lo recomiendan en Telegram, punto» — es el gesto exacto que hizo del hilo de abril un estorbo de 340 mil caracteres.

## 🔬 Un ejemplo real, de punta a punta

Para que el embudo no quede en teoría, el recorrido que ya hizo esta familia con una entrada real:

```
1. La wiki (y medio internet) menciona «Mihon»
   como lector de manga.

2. Se abre la casa: github.com/mihonapp/mihon

3. Se lee: 23.575 estrellas · Apache-2.0 ·
   versión 0.20.4 de agosto · push de HOY ·
   organización mihonapp con historial desde 2024.

4. Se contrasta: Keiyoushi (el almacén de
   extensiones) lo lista primero entre las apps
   soportadas; sus issues tienen actividad; la
   comunidad del ecosistema lo nombra como el
   sucesor de hecho de Tachiyomi.

5. Uso real: la gente de la banda que lo usa,
   con su opinión.

6. Ficha: hoy Mihon tiene guía propia dentro de
   esta familia (la de forks de lectores), con su
   fecha de corte.
```

Seis pasos. Todo lo que hace falta para que «Mihon» pase de pista a información. Y todo lo que NO pasó el día que alguien pegó una wiki entera en un hilo.

## 📌 La corrección a la «gran ola» de abril

```
Lo que hizo abril                Lo que hace esta familia
Vaciar FMHY en un post           Abrir la casa de cada pista
Vender la wiki como verificación Presentar la wiki como descubrimiento
340 mil caracteres sin dueño     Fichas cortas, fechadas, con casa
Índices de instalación pegados   El índice se lee en la casa del
                                 proyecto, nunca en un post
«Todo gratis, todo seguro»       Cada ficha con su límite y su fecha
```

La wiki no era el problema. El problema era el gesto: presentar acumulación como verificación. Ese gesto es lo que esta familia de guías existe para no repetir.

## ❓ Preguntas frecuentes

**¿Puedo usar FMHY?**
Puedes leerla: es pública y su papel como índice es legítimo. Lo que esta guía no hace es mandarte a sus destinos ni vaciarla aquí. Cada clic dentro de ella es un descubrimiento — el verificación va aparte, con el embudo de arriba.

**¿Es más segura que googlear?**
No se afirma. Es otra lista, curada por otra gente, con otros incentivos. Los buscadores te mandan a anuncios pagados; las wikis, a lo que la comunidad anotó. Ninguna de las dos puertas verifica por ti.

**¿Su sección de Android reemplaza la guía de tiendas de esta familia?**
No. La guía de tiendas abrió cada proyecto el día del corte; una sección de wiki es una lista con otra fecha y otro criterio.

**¿Y su sección de música?**
Misma respuesta: la familia tiene guía de música con las fichas verificadas. La wiki puede apuntar a lo mismo — o a cosas que nadie abrió todavía.

**¿El repo dice mayo pero la wiki está viva, cuál es la verdad?**
Las dos: la wiki se sirve por despliegues propios y el repo no refleja cada cambio. Git quieto no es proyecto muerto — ya lo decía la lección del repo.

**¿Base64 es piratería?**
Es codificación de texto — la misma técnica que tu teléfono usa para mandar imágenes por correo. El uso que cada quien le dé a los enlaces es su asunto y su ley. Aquí no se decodifica nada para nadie.

**¿Entonces para qué sirve FMHY, al final?**
Para lo que dijo su definición: el índice más grande del ecosistema. Como mapa de qué EXISTE, no tiene rival. Como prueba de qué funciona y es seguro, no vale nada — y no pretende valerla.

## 🔗 Enlaces

- La wiki: https://fmhy.net
- Guía de principiantes: https://fmhy.net/beginners-guide
- Post de septiembre: https://fmhy.net/posts/sept-2026
- El repo: https://github.com/fmhy/FMHY

> La Bandita informa a partir de fuentes fechadas. La wiki de pistas no es un catálogo — y el que descubre, todavía no verificó.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: wiki re-verificada viva a HOY. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 FMHY es una wiki de pistas, no un catálogo

Viva HOY (post mensual de septiembre en portada). Repo: github.com/fmhy/FMHY — ★14.613 · push del 13-mayo (el repo es el archivo).

**Discovery ≠ verificación:** la wiki te dice dónde hay puerta; la casa dice si la puerta sirve. Pista → casa abierta → estrellas y fecha → ficha.

**El Base64:** enlaces codificados pa' no ser indexados — decodificar = abrir tú el paquete. No es sello de calidad.

La «gran ola» de abril cayó sola al abrir las casas: la wiki no miente; los que copian sin verificar, sí.
*Fuente: pieza 12 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 12 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —FMHY dijo que era bueno. —FMHY dice que existe. Que sea bueno lo decidimos abriéndolo.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# FMHY is a leads wiki, not a catalog: what that means and how to use it without biting bait
**Reddit · ingles-US · fuente: pieza 12 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** FMHY (freemediaheckyeah) is discovery, never verification. The wiki is alive (September's monthly post on the front page); the repo backing it: ★14,613 · push from May 13.
## Tonight's state

Wiki alive — re-verified TODAY with September's monthly post on the front page · repo: github.com/fmhy/FMHY — ★14,613 · last push from May 13 (the wiki travels its own roads; the repo is the archive).

## How it works

The community edits, nobody guarantees. Its own navigation bar defines itself as "starting points" — a class in humility worth copying.

**The Base64 interstitial:** those links that arrive as weird text aren't witchcraft — the wiki encodes them so link hunters can't index them. Decoding = you open the package yourself. It's not a quality seal.

## Discovery ≠ verification

The wiki tells you where a door is; the house tells you whether the door works. Wiki lead + house date = an honest listing. April's "great wave" (an inflated list) fell on its own once the houses got opened — the wiki doesn't lie: those who copy without verifying do.
> —FMHY said it was good.
> —FMHY says it exists. Whether it's good, we decide by opening it.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# FMHY is a leads wiki, not a catalog (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 12 (Sep 15) · **Verified:** today, September 15, 2026

"So what's good on FMHY?" — trick question. FMHY (freemediaheckyeah) introduces itself as the internet's largest collection of free things: **discovery yes; verification, never.**

**Tonight's state:** the wiki is alive — re-verified TODAY with its September monthly post on the front page · the repo backing it: github.com/fmhy/FMHY — ★14,613 · last push from May 13 (the wiki travels its own roads; the repo is the archive).

**How it works:** the community edits, nobody guarantees. Its navigation bar is a class in humility: they define themselves as "starting points".

**The Base64 interstitial:** those links that arrive as weird text aren't witchcraft — the wiki encodes them so link hunters can't index them. Decoding = you open the package yourself. It's not a quality seal.

**Discovery ≠ verification, the full funnel:** the wiki tells you where a door is; the house tells you whether the door works. La Bandita takes the lead, opens the house, counts stars and date — and only then lists it.

**The correction to April's "great wave":** that month's inflated list fell on its own once the houses got opened. The wiki doesn't lie: those who copy without verifying do.

The house meme:
> —FMHY said it was good.
> —FMHY says it exists. Whether it's good, we decide by opening it.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
