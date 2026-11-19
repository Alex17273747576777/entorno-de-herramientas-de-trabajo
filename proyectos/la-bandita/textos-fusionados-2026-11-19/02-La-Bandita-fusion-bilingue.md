# Pieza 02 — Kototoro: manga, novelas y vídeo en una sola biblioteca — v2.1.3 salió hoy (re-verificada 15-sep)

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `f3b489d59bba` · ES-TG `ee177457bf3e` · EN-Reddit `bcbef253bb2d` · EN-Discord `cb4c451197ca`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 02 — Kototoro: manga, novelas y vídeo en una sola biblioteca — v2.1.3 salió hoy (re-verificada 15-sep)

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── ℹ️ Qué es Kototoro
├── 🧭 Estado del proyecto (verificado hoy)
├── 📦 La versión de hoy: v2.1.3
├── 🏗️ Cómo está construido
├── 🔌 Fuentes y extensiones: qué se conecta
├── 📖 Novelas y lectura por JSON
├── 🌳 El vecindario: Mihon, Aniyomi, Komikku y Tadami
├── ♿ Comodidad de lectura y accesibilidad
├── 🛠️ Solución de problemas
├── 🔒 Seguridad y cadena de suministro
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Kototoro es una aplicación Android de código abierto que reúne tres bibliotecas en una: manga, novelas y vídeo. Historial, favoritos y sincronización viven en un mismo flujo, y encima trae traducción por OCR en el propio teléfono, con modelos descargables.

La razón de esta edición: la versión **v2.1.3** salió HOY mismo, 15 de septiembre — un día después de la 2.1.2 — y ya son cuatro en cinco días. Re-verificado en la mañana del 15: el proyecto amaneció con release nueva. El proyecto se mueve a ritmo casi diario, así que esta guía trae los números de hoy y te enseña el único reloj que manda: su página de versiones.

La idea en una imagen: una estantería de tres cajones donde antes tenías tres muebles separados. Unificar ahorra saltos — y multiplica dependencias. Esta guía mira qué junta y qué te pide a cambio.

## ℹ️ Qué es Kototoro

https://github.com/Kototoro-app/Kototoro

Kototoro viene del linaje de los lectores tipo «fuente»: la aplicación no traida contenido dentro, sino que habla con fuentes que el usuario añade. Sobre esa base, le suma dos cosas que la distinguen: las novelas (lectura larga por JSON, al estilo de los lectores chinos de fuentes) y el vídeo, en la misma app.

```
Kototoro en una caja
Repositorio:   github.com/Kototoro-app/Kototoro
Licencia:      Apache-2.0
Paquete:       org.skepsun.kototoro
Android:       8.0 en adelante (builds recientes)
Docs:          kototoro-app.github.io/Kototoro
Origen:        linaje skepsun (kototoro-parsers)
Estrellas:     569 · actividad: hoy mismo
```

Su sitio de documentación está vivo y se leyó hoy: describe el lector todo-en-uno (manga, novelas, vídeo, historial, favoritos y sincronización), la traducción local por OCR con descarga de modelos, los flujos de sincronización y la referencia de integración de fuentes.

## 🧭 Estado del proyecto (verificado hoy)

La API del repositorio, abierta el 14 y re-abierta HOY, 15 de septiembre (re-verificación de mudanza):

```
Estrellas:        569
Último push:      14-sep · release de HOY (15-sep): v2.1.3
Rama de trabajo:  devel (al corte del 13-sep: 8 ramas,
                  196 tags, ~6.950 commits)
Versiones:        v2.1.3 (HOY, 15-sep) · v2.1.2 (14-sep) · v2.1.1 (13-sep) · v2.1.0 (11-sep)
Nightly:          repo Kototoro-Nightly, build N20260914 (14-sep)
```

Cuatro versiones en cinco días. El Nightly — versión de pruebas diaria — también está vivo, con build del 14-sep (última constada a HOY). ¿Qué significa para ti? Que cualquier número de esta guía (o de otra) envejece rápido: la única referencia de versión vigente es la página de versiones del proyecto, abierta el día que instales.

## 📦 La versión de hoy: v2.1.3

Publicada HOY, 15 de septiembre. Sus paquetes, según la API (ninguno se descargó para esta guía):

```
arm64-v8a      125.446.780 bytes    119 descargas al mediodía
armeabi-v7a    117.554.684 bytes      5
universal      312.997.668 bytes     14
x86            140.010.036 bytes      1
x86_64         147.078.128 bytes      2
```

Para casi todos los teléfonos modernos el archivo correcto es el arm64-v8a. El universal pesa más del doble porque trae todo — se usa en casos especiales.

Las notas de la versión (leídas hoy) traen cambio concreto:

- Personalización del fondo de portada (artwork).
- Distancia de desplazamiento por tecla de volumen en lectura webtoon.
- Gestión y búsqueda mejorada de categorías en favoritos.
- Ajustes del lector en pantallas anchas y recuperación del desplazamiento de márgenes al reanudar.

Lo que una versión así NO prueba: que episodios antiguos de respaldos (la serie 1.4–1.7) estén cerrados. Si vienes con una biblioteca grande, la regla no cambia: respaldo manual y prueba en vacío antes de migrar nada.

**Cachés y espejos van con retraso.** La v2.1.3 salió hace horas: si una página te muestra versiones de julio o la serie 1.x, no es fraude — es retraso. La única referencia viva es Releases.

## 🏗️ Cómo está construido

Kototoro hereda la arquitectura de su linaje: la aplicación en Kotlin consumía una librería de parsers propia — hoy independiente — llamada kototoro-parsers (github.com/skepsun/kototoro-parsers, versión 1.8, con actividad del 10 de septiembre). Esa separación app/parsers es el patrón del ecosistema: la casa (app) y las calles (fuentes) se mantienen por separado.

Dentro de la app, cada pestaña (Manga / Novelas / Vídeo) habla con su tipo de fuente:

- Manga: fuentes tipo lector (extensiones compatibles con el ecosistema Mihon).
- Novelas: fuentes JSON al estilo Legado — libros de reglas que dicen dónde está cada cosa.
- Vídeo: fuentes de streaming por JSON, incluidos perfiles tipo TVBox.

Esa mezcla es su promesa y su riesgo: tres tipos de fuente, tres tipos de fallo posible. La sección de solución de problemas de abajo existe por eso.

## 🔌 Fuentes y extensiones: qué se conecta

Las extensiones de manga de Kototoro son compatibles con el formato del ecosistema Mihon. Los almacenes de ese ecosistema, con su estado verificado hoy:

```
Keiyoushi          ★14.980  push 14-sep      el hub principal
   https://github.com/keiyoushi/extensions
   (código: keiyoushi/extensions-source, ★4.678, vivo a 15-sep)
Yūzōnō anime       ★432     push 13-sep
   https://github.com/yuzono/anime-extensions
manga-repo         ★445     push 14-sep      para Komikku/Mihon
   https://github.com/cuong-tran/manga-repo
Copymanga (CN)     ★2.753   v1.4.85 (8-sep)
   https://github.com/LittleSurvival/copymanga-copy20
```

La regla de esta familia de guías sobre almacenes: se nombra el proyecto y su página oficial; la receta de instalación (el índice que se pega en la app) cada quien la lee en el README del proyecto, el día que la use. No se copia aquí.

## 📖 Novelas y lectura por JSON

Aquí Kototoro habla el idioma de los lectores chinos de fuentes:

**Legado 3.0** — github.com/gedoor/legado — ★47.074, el gigante del modelo «libro de fuentes»: cada fuente es un JSON que dice cómo buscar, dónde está el texto y cómo paginar.

**Yuedu (阅读)** — github.com/XIU2/Yuedu — ★12.268, colección comunitaria de fuentes de lectura.

Kototoro importa esos flujos JSON y les suma su capa de traducción: OCR sobre la imagen, con modelos descargables que corren en el teléfono, o vía API si prefieres un servicio externo. Para el vídeo, importa además perfiles estilo TVBox — listas JSON que apuntan a medios, con distintos niveles de complejidad (enlaces directos, listas de reproducción, CMS simples, y perfiles que dependen de JavaScript o componentes remotos, en ese orden de prueba).

## 🌳 El vecindario: Mihon, Aniyomi, Komikku y Tadami

Kototoro no está sola. Los lectores del ecosistema libre, con sus números de hoy:

```
Mihon        ★23.601  v0.20.4 (5-ago)   push HOY (15-sep)      manga
Aniyomi      ★7.683   push 14-sep                      manga+anime
Komikku      ★4.721   v1.14.1 (17-jul)  push 11-sep   manga
Tadami       ★260     v0.62 (12-sep)    push 13-sep · viva     manga+anime+ranobe
Kototoro     ★569     v2.1.3 (HOY)      push HOY      manga+novelas+vídeo
```

Mihon es el tronco del árbol manga (el sucesor de hecho de Tachiyomi, cerrado en 2024). Aniyomi y Tadami suman anime. Komikku es el fork con vida propia. Kototoro es la rama que quiso todo junto. Ninguna es «la mejor» en abstracto: la buena es la que cubre lo que lees, con repo vivo.

Y ojo con la tentación de mezclar: las extensiones de un árbol no sirven en el otro. Kotatsu, Usagi y sus parientes usan parsers propios (otra familia de guías cubre ese árbol).

## ♿ Comodidad de lectura y accesibilidad

Lo que la app trae de fábrica para el ojo y la mano:

- Lectores por modo: página, continuo y webtoon, con ajuste de desplazamiento (ahora también por volumen, según la v2.1.2 del 14-sep).
- OCR de traducción en dos niveles (básico y avanzado) con modelos locales descargables — útil para manga sin traducción oficial.
- Historial, favoritos y categorías unificados (la v2.1.2 del 14-sep mejoró justamente la gestión de categorías).
- Sincronización del propio flujo de lectura entre sesiones.

El consejo de siempre para la vista: brillo alto en páginas de márgenes blancos, modo noche para webtoon, y descargar antes de leer en viaje — los tres lectores del ecosistema lo permiten.

## 🛠️ Solución de problemas

**Las fuentes no aparecen.**
Revisa en orden: ¿la extensión está instalada? ¿el repositorio fue agregado y sincronizado? ¿estás en la pestaña correcta (Manga / Novelas / Vídeo)? ¿refrescaste la pantalla de extensiones? La cura clásica: reinstalar la extensión y refrescar.

**Un JSON de novelas no importa.**
Primero: ¿es una fuente Legado o un perfil TVBox? Son formatos distintos y se importan por menús distintos. Segundo: ¿el JSON es válido? ¿la URL responde? Tercero: prueba primero importando desde archivo local — elimina la mitad de las variables.

**Un perfil TVBox importa pero no carga.**
La escalera de prueba, de lo simple a lo complejo: medios directos → listas de reproducción → CMS simples → perfiles que dependen de JavaScript → perfiles con componentes remotos. Un JSON puede importar perfecto y aun así fallar porque una dependencia externa cambió o murió. Eso no es culpa de la app.

**La traducción no arranca.**
Lista corta: modo local o solo-API según lo que quieras usar; idiomas origen/destino correctos; nivel de OCR (básico/avanzado); modelos efectivamente descargados; y si usas API, endpoint, clave y modelo bien escritos. El 80% de los casos es un modelo que nunca se descargó.

**La app consume espacio.**
Es grande por diseño: parsers de tres medios + modelos de OCR. Si el teléfono es justo, empieza sin descargar modelos avanzados y sin modo universal.

## 🔒 Seguridad y cadena de suministro

Lo que el proyecto declara: sus desarrolladores no tienen afiliación con proveedores de contenido ni gobiernan repositorios de extensiones — las fuentes las pone el usuario. La app es un instrumento; el contenido es tu decisión y tu responsabilidad legal.

Al corte de la semana pasada, el repo no publicaba política de seguridad ni código de conducta (sí guía de contribución y licencia). No implica inseguridad — pero en una aplicación que carga runtimes y fuentes de terceros, es una señal a vigilar. Build concretos distribuidos por tiendas alternativas pasaron escaneos (ClamAV, APKiD, Quark-Engine) sin amenazas: eso vale para ese archivo exacto, no para la cadena completa.

La regla de la casa: no confíes en una fuente solo porque esté en una lista de internet. Repo, commit, etiqueta y firma se miran antes de instalar. Y las estrellas no instalan nada.

## ❓ Preguntas frecuentes

**¿Cuál es la versión buena hoy?**
La que diga Releases el día que instales — hoy es la v2.1.2, publicada esta misma mañana. Mañana puede ser otra; tres releases en cuatro días lo dicen todo.

**¿Puedo tener manga, novelas y vídeo en la misma app?**
Sí, es su punto. El precio: tres tipos de fuente con tres tipos de fallo. Respaldo por separado y paciencia con la escalera de diagnóstico.

**¿Es compatible con las extensiones de Mihon?**
El formato de extensiones de manga, sí. Las de anime/novelas tienen su propio camino (JSON). Lo que no: las fuentes de Kotatsu/Usagi son otro árbol, no entran.

**¿Vengo de la serie 1.x, cómo migro?**
Con respaldo manual y prueba en vacío. El episodio de respaldos 1.4–1.7 está documentado en la comunidad; que la serie 2.x vaya rápida no prueba por sí sola que ese capítulo esté cerrado.

**¿La traducción OCR necesita internet?**
El modo local no: corre en el teléfono con modelos descargables. El modo API sí, y depende del servicio que tú configures.

**¿Y TVBox, eso qué es?**
Listas JSON que apuntan a medios de vídeo. Importar es fácil; que carguen depende de que las cosas a las que apuntan sigan vivas. Empieza siempre por lo simple de la escalera.

**¿Cuánto pesa?**
El paquete arm64 de v2.1.2 ronda los 125 MB, y el universal pasa de 300 MB. A eso súmale modelos de OCR si los descargas.

**¿Las 569 estrellas significan algo?**
Comunidad pequeña pero en pleno crecimiento, con un ritmo de desarrollo que pocas apps del mapa igualan hoy. Las estrellas no instalan: miden fama, no calidad.

## 🔗 Enlaces

- Repositorio: https://github.com/Kototoro-app/Kototoro
- Versiones: https://github.com/Kototoro-app/Kototoro/releases
- Nightly: https://github.com/Kototoro-app/Kototoro-Nightly
- Documentación: https://kototoro-app.github.io/Kototoro/
- Parsers del origen: https://github.com/skepsun/kototoro-parsers
- Keiyoushi: https://github.com/keiyoushi/extensions · https://keiyoushi.github.io
- Yūzōnō anime: https://github.com/yuzono/anime-extensions
- manga-repo: https://github.com/cuong-tran/manga-repo
- Copymanga: https://github.com/LittleSurvival/copymanga-copy20
- Legado: https://github.com/gedoor/legado · Yuedu: https://github.com/XIU2/Yuedu
- Mihon: https://github.com/mihonapp/mihon · Aniyomi: https://github.com/aniyomiorg/aniyomi
- Komikku: https://github.com/komikku-app/komikku · Tadami: https://github.com/andarcanum/Tadami-Aniyomi-fork

> La Bandita informa a partir de fuentes fechadas. La estantería es libre; lo que pones en ella, también es tu decisión.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: Kototoro re-verificado (v2.1.3 de HOY), Mihon ★23.601, Keiyoushi ★14.980, Yūzōnō ★432, manga-repo ★445. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

**Nota de la verificación final (15-sep, noche):** la documentación propia (kototoro-app.github.io/Kototoro) devuelve 404 a esta hora, constado en vivo; la casa GitHub sigue viva (★569, v2.1.3 de HOY). El sitio puede estar en mudanza; el enlace se reabre el día que se use.

### ▸ Telegram *(adaptación de canal)*

📌 Kototoro: 4 versiones en 5 días — v2.1.3 salió esta madrugada

★569 · Apache-2.0 · github.com/Kototoro-app/Kototoro

v2.1.0 (11-sep) → 2.1.1 (13) → 2.1.2 (14) → **2.1.3 HOY**. Manga + novelas + vídeo, linaje Mihon con parsers propios. Cachés con retraso ≠ fraude: la referencia es su casa.

**Almacenes que come:** Keiyoushi ★14.980 · Yūzōnō anime ★432 · manga-repo ★445
**Vecindario:** Mihon ★23.601 (push HOY) · Aniyomi ★7.683 · Komikku ★4.721
*Fuente: pieza 2 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 02 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —¿Cada cuánto saca versión Kototoro? —Pregunta mejor qué día NO sacó.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# Kototoro shipped 4 releases in 5 days: today's verified state of the multi reader (manga, novels, video)
**Reddit · ingles-US · fuente: pieza 2 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** Kototoro (★569 · Apache-2.0) published v2.1.3 THIS very day: v2.1.0 on the 11th → v2.1.1 on the 13th → v2.1.2 on the 14th → v2.1.3 on the 15th. Manga + light novels + video in one app, Mihon lineage with its own parsers.
## The state, verified TODAY

- **Kototoro** — ★569 · **v2.1.3 from TODAY** · Apache-2.0 · github.com/Kototoro-app/Kototoro
- Own parsers: skepsun/kototoro-parsers (★14)
- A Nightly glued to the day: build N20260914 · github.com/Kototoro-app/Kototoro-Nightly (★9)

**What v2.1.2/v2.1.3 brought:** volume-key reading, better category management, unified history and favorites. Caches and mirrors run late: if a page shows you the 1.x series, that's lag, not fraud.

## The warehouses it eats from

- **Keiyoushi** — ★14,980 · push from Sep 14 — the main hub (code: extensions-source, ★4,678)
- **Yūzōnō anime** — ★432 · push from Sep 13 · **manga-repo** — ★445 · push from Sep 14
- **Copymanga CN** — ★2,753 · v1.4.85 (Sep 8)

## The neighborhood, counted tonight

Mihon ★23,601 (push TODAY) · Aniyomi ★7,683 (push 14th) · Komikku ★4,721 · Tadami ★260 v0.62 (alive, rectified with a record) · Legado ★47,074 · Yuedu ★12,268.
**House edit (Sep 15):** its own documentation (kototoro-app.github.io/Kototoro) 404s, checked live — the GitHub house lives and pushes. The site may be between homes.

> —How often does Kototoro ship a version?
> —Ask a better question: which day did it NOT ship one.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Kototoro — manga, novels and video in one library (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 02 (Sep 15) · **Verified:** today, September 15, 2026

The busiest tree this week, and no joke: **four releases in five days** — and today's shipped this very morning.

**The state, verified TODAY (Sep 15):**
- **Kototoro** — ★569 · **v2.1.3 from TODAY** (v2.1.0 on Sep 11 → v2.1.1 on the 13th → v2.1.2 on the 14th → v2.1.3 on the 15th) · Apache-2.0 · github.com/Kototoro-app/Kototoro
- Manga + light novels + video in a single app — Mihon lineage, with its own parsers (skepsun/kototoro-parsers, ★14)
- The Nightly tracks the day: build N20260914 · github.com/Kototoro-app/Kototoro-Nightly (★9)

**What v2.1.2/v2.1.3 brought:** volume-key reading, better category management, unified history and favorites. Caches and mirrors run late: if a page shows you the 1.x series, that's lag, not fraud — the living reference is its home.

**The warehouses it eats from:**
- Keiyoushi — ★14,980, push from Sep 14 — the main hub (code: extensions-source, ★4,678)
- Yūzōnō anime — ★432, push from Sep 13
- manga-repo — ★445, push from Sep 14 (for Komikku/Mihon)
- Copymanga CN — ★2,753 · v1.4.85 (Sep 8)

**The neighborhood, counted tonight:**
- Mihon — ★23,601 · v0.20.4 · push from TODAY
- Aniyomi — ★7,683 · push from Sep 14
- Komikku — ★4,721 · v1.14.1
- Tadami — ★260 · v0.62 · alive (rectified with a record: the afternoon 404 belonged to a different slug)
- Legado 3.0 — ★47,074 — the giant of the "book of sources" model · Yuedu — ★12,268

**Anti-finding:** its own documentation (kototoro-app.github.io/Kototoro) returns 404 tonight, checked live — the GitHub house keeps living and pushing. The site may be between homes; the link gets reopened the day it's used.

The house meme:
> —How often does Kototoro ship a version?
> —Ask a better question: which day did it NOT ship one.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
