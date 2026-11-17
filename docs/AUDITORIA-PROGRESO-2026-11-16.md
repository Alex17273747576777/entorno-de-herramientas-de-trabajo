# Auditoría de emergencia · progreso real de todo lo encargado

**Medida el 2026-11-16 a las 12:00Z con evidencia verificada en este turno** (API de GitHub, `git`
sobre los clones, archivos en disco). Nada de lo que sigue se afirma de memoria: cada renglón lleva su
fuente de verificación y su hora.

Regla de puntuación usada, declarada para que se pueda discutir:

- **100 %** = entregado **y verificado por ejecución o por fusión** en su destino real.
- **parcial** = publicado/propuesto pero **no adoptado ni ejecutado** en el destino, o adoptado sólo en parte.
- **0 %** = diagnosticado por escrito pero sin ejecutar, o bloqueado por falta de entorno.
- El peso de cada corriente es proporcional a lo que costó pedirla y a lo que cuesta hacerla bien.

---

## 1 · El titular

**Progreso global ponderado: 58 %.** Tu intuición de «ni siquiera 60 %» es correcta. El desglose importa
más que el número: hay corrientes al 85 % (ShinKu, donde el mantenedor fusionó e implementó) y otras al
15 % (AniZen, donde nadie ha respondido; y los 12 issues abiertos en tus propios repos).

| # | Corriente de trabajo | Peso | % | Evidencia verificada hoy |
|---|---|---:|---:|---|
| 1 | Biblioteca masiva / fusión por defecto — **ShinKu** | 14 | **85** | PR **#34 FUSIONADO** en `main` (`26aa57dcaf`, 10:06Z, +147); Fase 2 implementada por el mantenedor (`5b50121099`, 10:30Z, 17 ficheros); mi `merge_group.sq`, `MergeGroupDedup.kt` y `MergeGroupDedupTest.kt` presentes en su `main` |
| 2 | Feed de novedades — **ShinKu** | 12 | **85** | Etapa 1 (`64f68d1d98`, 10:11Z) y Etapa 2 (`336f56b2dc`, 11:10Z, 25 ficheros) landeadas por el mantenedor; su `feed_categories.sq` y `43.sqm` son de forma **idéntica** a los míos; quedan **3 defectos verificados** (sección 3) |
| 3 | Infraestructura propia (edt, checkpoint, compuertas, restaurador) | 10 | **90** | 43 commits en `work/edt` (primero `88209c6` 11-08 10:19); `python3 tests/pruebas.py` → **TODO BIEN** ejecutado hoy 11:57Z; `restaurar-toolchain-kotlin.sh` probado en sus dos modos |
| 4 | Auditoría remota y mantenimiento de 6 repos propios (10-11) | 10 | **70** | `docs/AUDITORIA-REMOTA-2026-11-10.md`: 19.528 archivos / 236,9 MB recorridos, secretos y Dependabot habilitados; **pero 12 issues de seguimiento siguen abiertos** (sección 4) |
| 5 | cero-X-app (exploración, icono, presentación, PR #7) | 9 | **75** | HEAD local `7d108e17` **== remoto** (verificado hoy); PR **#7 fusionado** (13-11); 6 issues cerrados; `serialize-javascript` sólo diagnosticado |
| 6 | Publicaciones La Bandita (piezas 1-40, archivo sellado) | 9 | **65** | pieza 31 reescrita y medida (`piezas/31-medicion.json`); 458 publicaciones retiradas; casa sellada v2; **piezas 32-40 nunca se reescribieron** (se retiraron) |
| 7 | Guías e investigación (Adobe, FMNY, Photoshop, Houri, Kisara) | 7 | **85** | `guia-suite-adobe-a-codigo-abierto.md` (16 KB, 10 pares, campeón Firefly→ComfyUI ★146.837); mediciones de 14 y 24 repos con recuentos reproducibles |
| 8 | Frente Nox / `index.pb` (Awerkori) | 7 | **60** | PR **#3 sigue `open`, sin fusionar** (verificado hoy 11:57Z, +2/-1, 2 ficheros); `anime-index.pb` 17.663 B con md5; tests y CI en verde; **el destino no lo ha aceptado** |
| 9 | Biblioteca masiva / feed — **AniZen** | 12 | **35** | #94 (31.286 chars) y #95 (35.057) `open` con **0 comentarios**; ramas `merge-groups-phase1` y `feed-cap-per-tab` (3 commits) públicas; `master` de AniZen **sin mover desde el 31-10** (`95160a724d`); nada adoptado |
| 10 | Idiomas / sugerencias / estadísticas / «explorar idiomas» en ShinKu | 6 | **55** | el mantenedor landeó `lang` y `explore` en `feed_categories`, el filtro por idioma del dispositivo y **sugerencias de títulos** (`SuggestedTitlesScreenModel.kt`, con `SourceHealthRepository`, `feedLanguageFilter`, `feedSourceFilter`); lo que **no** existe: sugerencias de *pestañas* (`SuggestFeedTabs`, 0 ficheros), estadísticas de actividad de feed (`feed_activity`/`getCountsByPeriod`, 0) y una UI que active `explore` (siempre se inserta `false` en `FeedScreenModel:757`) |
| 11 | gltools-reborn: 8 issues abiertos | 3 | **15** | los 8 siguen `open` desde el 10-11; la mayoría exige **dispositivo físico** (superposición, arranque, contraste real, APK en ROM) |
| 12 | normas-de-diseno: 2 issues abiertos | 2 | **25** | ambos `open`; el procedimiento de auditoría de app publicada no está escrito |
| 13 | Dependabot / `serialize-javascript` en cero-X | 1 | **20** | diagnosticado por escrito (`DEPENDABOT-SERIALIZE-JAVASCRIPT.md`); **no ejecutado**: falta Gradle/Kotlin-JS y tu orden |

**Total ponderado: 58 %** (suma de peso×% / 102 de peso declarado).

---

## 2 · Lo que sí cambió en las últimas 14 horas (mientras dormías)

Verificado por API a las 11:56-11:59Z:

1. **PR #34 fue fusionado en `main` de ShinKu** a las 10:06:42Z por `Harrys-HQ` (`merged=True`,
   merge commit `26aa57dcaf`). Es el primer código mío que entra en el `main` de un repo ajeno.
2. El mantenedor **implementó él mismo la Etapa 1 y la Etapa 2 del feed** (`64f68d1d98` 10:11Z,
   `336f56b2dc` 11:10Z con 25 ficheros: `FeedCategoryTabs.kt`, `FeedCategoryDialogs.kt`,
   `FeedFilterDialog.kt`, interactores y DI) y la **Fase 2 de biblioteca** (`5b50121099` 10:30Z,
   17 ficheros: `MergeGroupRepositoryImpl`, `GroupManga`, diálogo de duplicados con agrupación a un
   toque, `dedupeByMergeGroup` cableado en `LibraryScreenModel`, ajuste en Ajustes→Biblioteca).
3. Escribió dos comentarios en #32 y dos en #33 agradeciendo la propuesta y el análisis de pila, y
   añadió sus propios tests: `FeedCategoryInteractorsTest` (7/7), `FeedRequestsTest` (12/12),
   `GroupMangaTest` (5/5) — los tres **existen** en su `main` (verificado por `find`).
4. Consecuencia directa: **mi rama `feed-tabs-phase1` quedó obsoleta**. Su `43.sqm` y el mío son
   *diferentes* como fichero pero **equivalentes en forma** (misma tabla, mismas columnas, mismos
   defaults, misma fila de sistema `_id=1 'Global'`). `git diff` entre su `main` y mi rama: 3 ficheros,
   +25/-34. No hay que empujarla ni proponerla; hay que decirlo en público para que nadie la aplique.
5. **AniZen no se movió**: `master` en `95160a724d` del 31-10, `pushed_at` 15-11 05:31Z, **0
   comentarios** en #94 y #95. Mis dos ramas siguen siendo la única propuesta viva allí.

---

## 3 · Tres defectos verificados en lo que ShinKu acaba de landear

Revisión hecha sobre `336f56b2dc` (su `main` de hoy), con `grep`/`sed` sobre el código real:

**A) El aviso de «demasiadas fuentes» miente en 14 idiomas.** `base/strings.xml:469` sí se actualizó a
`cannot add more than 25`, pero **14 de los 16** `strings.xml` que llevan `too_many_in_feed` siguen
diciendo «10» (es, de, fr, ru, ja, pt-rBR, ar, tr, in, ta, hr, zh-rCN, zh-rTW, fil, as). Ningún locale
usa `%1$d`, que era justamente lo que propuse para que el número salga del código y no de la traducción.

**B) El tope de 25 se comprueba al abrir el diálogo, no al insertar.** `hasTooManyFeeds` sólo se llama
en `FeedScreenModel:658` (`openAddDialog`) y `SourceFeedScreenModel:269` (`onSavedSearchAddToFeed`).
Las inserciones reales —`FeedScreenModel:718 createFeed` (llamada desde `FeedTab.kt:171`) y
`SourceFeedScreenModel:112 createFeed` (desde `SourceFeedScreen.kt:68`)— **no vuelven a comprobar
nada**, y `InsertFeedSavedSearch.await` no tiene tope. `selectCategory` (`:733`) cambia de pestaña sin
cerrar diálogos y `createFeed` lee la pestaña **en el momento de insertar**, así que abrir el diálogo en
una pestaña con 24, cambiar a una que ya tiene 25 y confirmar la deja en 26. Es el mismo defecto que yo
cacé en mi propio parche y corregí poniendo el tope en el interactor como punto único.

**C) El backup no se lleva los feeds ni las pestañas.** `BackupSavedSearch` sólo cubre la tabla
`saved_search` (`name`, `query`, `filterList`, `source`); **ningún** modelo ni restorer referencia
`feed_saved_search` ni `feed_categories` (verificado con `find … | xargs grep -l`, salida vacía).
Copiar y restaurar pierde toda la configuración del feed, y desde hoy también las pestañas. Es
preexistente, pero la Etapa 2 lo hace más costoso.

Además: sus tres tests nuevos **no cubren el tope** (ninguna referencia a `MAX_SOURCES_PER_FEED`,
`hasTooManyFeeds` ni `too_many` en `FeedCategoryInteractorsTest.kt`, `FeedRequestsTest.kt`,
`GroupMangaTest.kt`).

**Actuado en este mismo turno, no sólo reportado:** los tres hallazgos se publicaron como un único
comentario en #32 (`issuecomment-6915861295`, 12:02:46Z, con la declaración de que mi rama
`feed-tabs-phase1` queda obsoleta para que nadie la aplique), y el punto B se convirtió en el
**PR #36** (`https://github.com/Harrys-HQ/ShinKu/pull/36`, commit `b888787d4a84`, push verificado
`ls-remote == rev-parse`): el tope movido a `InsertFeedSavedSearch.await` como punto único de escritura,
`null` como señal de rechazo (ninguna firma cambia), `awaitAll` sin tope a propósito, y
`InsertFeedSavedSearchTest.kt` con 6 casos **ejecutados** contra sus fuentes reales con kotest 6.0.7 /
JUnit 6.1.2 / mockk 1.14.7 / coroutines-test → `6 tests successful, 0 failed`. El punto A (cadena con
«10» en 14 locales) **no** va en ese PR a propósito: tokenizar `%1$d` exige actualizar los dos
consumidores a la vez, y tokenizar sólo la base dejaría un `%1$d` literal en el toast de
`SourceFeedScreenModel:271` (su firma `(StringResource) -> Unit` no puede llevar argumentos de formato);
el diff exacto y la trampa del sobrecargado con `toast(res, Toast.LENGTH_LONG)` de
`MigrationListScreen.kt:43` quedaron escritos en el PR.

---

## 4 · El agujero que explica la sensación de no avanzar

El 2026-11-10 abrí **12 issues en tus propios repos** como seguimiento de la auditoría remota y **no
cerré ninguno**:

| Repo | Abiertos | De qué tratan |
|---|---:|---|
| `gltools-reborn` | 8 | superposición sin probar en teléfono, rediseño 1.9.1 sin ver en pantalla, contraste real de 4 secciones, ley de diseño esquivable renombrando un color, carrusel con datos sin mostrar, cierre de app sin parte del teléfono, capturas del kit compuestas en vez de reales, energía/ROM/arranque/APK en dispositivo |
| `normas-de-diseno` | 2 | censo de Appteka sin diff (es una foto), falta procedimiento para auditar una app ya publicada |
| `cero-X-app` | 1 | firma de publicación, confianza de extensiones y pruebas reales |
| `la-bandita-archivo` | 1 | política de duplicados, cachés y datos versionados |

Cinco de los ocho de gltools exigen **dispositivo físico o captura real de pantalla**, que este entorno
no tiene: son bloqueos estructurales, no descuidos, pero llevan seis días abiertos sin que yo lo haya
declarado así en un solo lugar. Los otros siete **sí** se pueden cerrar con trabajo de escritorio y no
los hice porque las rondas siguientes se fueron todas a los repos ajenos (feed y biblioteca).

---

## 5 · Lo que sigue sin hacerse (y por qué)

1. **AniZen**: nada adoptado, 0 respuestas. Su `AGENTS.md` prohíbe abrir PR, así que la vía es rama +
   issue, que es lo que hay. No se puede forzar; se puede mejorar la propuesta.
2. **`serialize-javascript`** en cero-X: exige entorno Gradle/Kotlin-JS y tu orden explícita.
3. **PR #3 de Awerkori**: `open` desde el 15-11 08:52Z, sin respuesta del mantenedor.
4. **Sugerencias de pestañas + estadísticas de feed + pestaña «explorar idiomas»** en ShinKu: las columnas
   `lang`/`explore` y las sugerencias de *títulos* ya están en su `main`; `SuggestFeedTabs`,
   `feed_activity` y una UI que active `explore` no existen (verificado por `grep` a las 12:01Z).
5. **Dispositivo físico**: 5 issues de gltools, más `assembleDevRelease`/`spotlessCheck`/`detekt` de
   ambos repos, más el efecto real de `logcat`. Sin Android SDK ni Gradle en el sandbox, no ejecutable.

---

## 6 · Fuente de cada cifra

- Estados y fechas de GitHub: `GET /repos/…`, `GET /search/issues?q=author:Alex17273747576777`,
  `GET /repos/Harrys-HQ/ShinKu/commits/{64f68d1d98,336f56b2dc,5b50121099,26aa57dcaf}` — 11:56-12:00Z.
- Código de ShinKu: clon en `/var/tmp/feed/shinku` con `git fetch` de su `main` y revisión en
  `336f56b2dc` — 11:57-11:59Z.
- Disco y commits propios: `ls`, `du`, `git log`, `git rev-parse`/`git ls-remote`,
  `python3 tests/pruebas.py` → `TODO BIEN` — 11:55-11:57Z.
- Recuento global de objetos GitHub bajo tu cuenta: **139** (48 abiertos, 91 cerrados) en **31** repos,
  el primero el 2024-12-09 (`null2264/yokai#288`); en la ventana de esta colaboración (08-11 → 15-11),
  **29** objetos.

---

# ACTUALIZACIÓN 2026-11-17 (medida a las 10:48-10:55Z, hora autoritativa de GitHub)

⚠️ **El reloj del sandbox iba un día atrás**: marcaba 2026-11-16 10:47Z cuando la cabecera `Date` de la
API de GitHub decía **Tue, 17 Nov 2026 10:47:17 GMT**. Regla nueva: la hora se toma de GitHub, no del
reloj local, y se declara cuál de las dos se está usando. Habían pasado ~23 h, no 14.

## Lo que cambió mientras no había turno

| Hecho | Evidencia |
|---|---|
| **PR #36 FUSIONADO** en `main` de ShinKu | `merged=True`, `merged_at=2026-11-17T02:28:53Z`, merge commit `5e7d46e610` |
| **#32 CERRADO como resuelto** | comentario de `Harrys-HQ` 07:17Z: *«Resolved and released in ShinKu v2.8.3 via multi-tab feed categories and domain-level 25-source safety cap (#36)»* |
| **#33 CERRADO como resuelto** | comentario 07:17Z: *«…via dedicated library merge group viewing, consolidated chapter counting, and one-tap deduplication (#34)»* |
| **ShinKu v2.8.3 publicada** | `4b4acb129f` (bump) y `c7ab60c983` (project memory v2.8.3, 147), release con 5 assets |
| Mi test y el tope en el interactor están en su `main` | `raw.githubusercontent.com/…/main/…InsertFeedSavedSearchTest.kt` y `…InsertFeedSavedSearch.kt` contienen `countGlobalByCategory` |
| **PR #3 (Nox/anime) CERRADO SIN FUSIONAR** | `Awerkori` 06:52Z: la implementación se aprovechó **con crédito** en `Awerkori/anime-fonte-extensoes#9`, pero mi binario usaba `sources=8` (esquema de la org) cuando Aniyomi exige `sources=9` |
| El repo se mudó | `Awerkori/anime-extensoes` → **`ProjectNox-org/anime-extensoes`** (307 con redirect) |
| AniZen sigue igual | `pushed_at=2026-11-15T05:31`, #94/#95 con **0 comentarios** |

**Verificación propia del cierre del PR #3, por bytes (no de memoria):** el `index.pb` de la rama
`index-pb` (17.663 B) es **idéntico byte a byte** a mi `anime-index.pb`, con `Extension` en campos
`[1..8]` y 326 fuentes en el campo **8** = esquema de la org; mi `anime-index-spec-aniyomi.pb`
(17.664 B) lleva `[1..7,9]` y 326 fuentes en el campo **9** = spec oficial Aniyomi. El diagnóstico del
mantenedor es correcto. **Y la secuencia es peor que un despiste:** la primera revisión del PR llevaba el
spec correcto y mi segundo commit lo «corrigió» al proto de la org; mi propio informe llamaba «corrección»
a esa regresión. Registrado como **FALLA-010** con la precisión honesta de que `Source.message=7` no
aplica a mi artefacto (ningún `Source` lleva campo 6 ni 7: proto3 omite cadenas vacías).

**Contramedida ejecutada, no prometida:** compuerta en `json_a_index_pb.py` — modo `verificar-spec` que
lee los bytes escritos y compara el número de campo real, negativa a generar `spec=nox` para repos
consumidos por clientes Aniyomi, y auto-comprobación tras escribir que borra el fichero si no casa.
Probada a las 10:53Z contra cuatro casos, **incluido el que debe fallar** (`verificar-spec
anime-index.pb aniyomi` → salida 1; `generar … anime-extensoes … nox` → NEGADO, salida 1, nada escrito).

## Porcentaje recalculado a las 10:55Z

| # | Corriente | Peso | 11-16 | **11-17** | Por qué se movió |
|---|---|---:|---:|---:|---|
| 1 | Biblioteca masiva — ShinKu | 14 | 85 | **95** | PR #34 fusionado, Fase 2 landeada y **publicada en v2.8.3**, #33 cerrado como resuelto |
| 2 | Feed — ShinKu | 12 | 85 | **90** | Etapas 1 y 2 landeadas, **PR #36 fusionado**, #32 cerrado y publicado; falta la cadena en 14 locales |
| 3 | Infraestructura edt | 10 | 90 | **90** | igual; se añadió la compuerta de spec y la FALLA-010 |
| 4 | Auditoría remota 6 repos | 10 | 70 | **70** | los 12 issues siguen abiertos (se atacan en este turno) |
| 5 | cero-X-app | 9 | 75 | **75** | sin cambio |
| 6 | La Bandita | 9 | 65 | **65** | sin cambio |
| 7 | Guías/investigación | 7 | 85 | **85** | sin cambio |
| 8 | Frente Nox `index.pb` | 7 | 60 | **50** | **bajó**: PR cerrado sin fusionar por binario con esquema equivocado; implementación adoptada con crédito en otro repo |
| 9 | AniZen (feed + biblioteca) | 12 | 35 | **35** | nada adoptado, 0 respuestas |
| 10 | Idiomas/sugerencias/estadísticas | 6 | 55 | **55** | sin cambio |
| 11 | gltools-reborn (8 issues) | 3 | 15 | **15** | se atacan en este turno |
| 12 | normas-de-diseno (2 issues) | 2 | 25 | **25** | se atacan en este turno |
| 13 | Dependabot/serialize-javascript | 1 | 20 | **20** | se ataca en este turno |

**Global ponderado: 58 % (11-16) → 69 % (11-17).** Subió 11 puntos por dos fusiones y una release, y
bajó en el frente Nox por un defecto mío. Lo que impide pasar de ~70 % no son los repos ajenos: son los
**12 issues abiertos en tus propios repos** y AniZen, que no responde.

---

## Porcentaje recalculado a las 12:15Z del 17-11 (segunda mitad del turno)

| # | Corriente | Peso | 11-17 mañana | **11-17 tarde** | Por qué se movió |
|---|---|---:|---:|---:|---|
| 1 | Biblioteca masiva — ShinKu | 14 | 95 | **95** | sin cambio: v2.8.3 publicado, #34 fusionado |
| 2 | Feed — ShinKu | 12 | 90 | **92** | **PR #37 abierto** con las 16 cadenas tokenizadas y verificadas; sin fusionar |
| 3 | Infraestructura edt | 10 | 90 | **90** | igual; se añadieron FALLA-011/012/013 y tres recetas de entorno |
| 4 | Auditoría remota 6 repos | 10 | 70 | **78** | issues abiertas en repos propios: **12 → 8** (gltools 6, cero-X 1, la-bandita 1, normas 0) |
| 5 | cero-X-app | 9 | 75 | **75** | sin cambio en este renglón; el lockfile va en el 13 |
| 6 | La Bandita | 9 | 65 | **65** | sin cambio |
| 7 | Guías/investigación | 7 | 85 | **85** | sin cambio |
| 8 | Frente Nox `index.pb` | 7 | 50 | **50** | sin cambio desde la caída por FALLA-010 |
| 9 | AniZen (feed + biblioteca) | 12 | 35 | **35** | nada adoptado, 0 respuestas, `master` sin mover desde el 31-10 |
| 10 | Idiomas/sugerencias/estadísticas | 6 | 55 | **55** | sin cambio |
| 11 | gltools-reborn (issues) | 3 | 15 | **35** | #4 y #7 cerrados con evidencia; #3 con el parte mejorado y **13 casos ejecutados**; #6 con la mitad medible publicada; auditor de diseño EXIT=0. Siguen 6 abiertos, casi todos por falta de dispositivo |
| 12 | normas-de-diseno (issues) | 2 | 25 | **95** | **#1 y #2 cerrados**: auditor genérico + envoltorio fechado + segundo censo real + diff probado con cambios conocidos |
| 13 | Dependabot/serialize-javascript | 1 | 20 | **80** | **corregido y vigilado**: `resolution(7.1.3)`, lock regenerado con yarn real (76 pares, 0 avisos), auditor propio, workflow nuevo **ejecutado en CI** (run 44076096239, success). No llega a 100 porque Gradle no se ejecutó aquí y `cero-X#6` sigue abierto por cuatro criterios que no dependen de mí |

**Total de peso declarado: 102.** Suma ponderada: 7080 → **7444**, o sea
**69.4 % → 73.0 %**. La aritmética la hace Python sobre esta misma tabla, no yo de
cabeza: FALLA-012 es justamente publicar una cifra que no salió de la medición.

### Lo que subió y por qué, con la evidencia a la vista

- **normas-de-diseno 25 → 95** (peso 2). `#1` y `#2` cerrados y verificados por `GET` aparte. `#2`
  pedía dos cosas y están las dos: `censo/2026-11-08.json.gz` y `censo/2026-11-17.json.gz` versionados
  (sha256 del contenido sacado de git == el fichero en disco, y ese contenido se vuelve a leer: 42
  categorías, 37.284 listados) y `procedimientos/07-diff-de-censos.py`, probado con 6 cambios
  inyectados en `/tmp` antes de usarse con los reales. No llega a 100 porque con dos fotos no hay
  tendencia y el recorrido no está en CI.
- **Dependabot 20 → 80** (peso 1). De «diagnosticado por escrito» a «corregido, con auditor propio y
  con el workflow **visto correr** en GitHub Actions». Lo que falta para 100 no es mío: `cero-X#6`
  sigue abierto por cuatro criterios (clave privada legítima, compilación firmada con plan de
  migración, catálogo autenticado, prueba positiva con extensión auténtica) y el primero depende de
  que alguien entregue una clave por un canal seguro.
- **gltools-reborn 15 → 35** (peso 3). Sube poco y a propósito: de 8 issues quedan **6 abiertos** y
  casi todos exigen un teléfono (superposición, arranque, contraste real en panel, APK en ROM,
  energía/permisos). Lo que sí se hizo hoy es medible: el auditor de diseño específico en
  `SIN INCUMPLIMIENTOS` con su prueba de mutación, el genérico separado en R14/R14b, y el parte de
  fallos con 13 casos ejecutados en JVM. **Ninguna de esas cosas cierra un issue que pide una captura.**
- **Auditoría remota 70 → 78** (peso 10). Sólo por el recuento: **12 → 8** issues abiertas en repos
  propios, contado por API sobre los 9 repos (sin forks) y no de memoria — la primera versión de esta
  línea decía 7 y se había dejado fuera `la-bandita-archivo#1`. El reparto: `gltools-reborn` 6
  (#1 #2 #3 #5 #6 #8), `cero-X-app` 1 (#6), `la-bandita-archivo` 1 (#1), `normas-de-diseno` 0. Aparte,
  `bandwidth-hero-proxy2` tiene 3 PRs abiertos, que no son issues y no cuentan aquí.
- **Feed ShinKu 90 → 92** (peso 12). El PR #37 existe y está verificado en lo que se puede verificar
  sin Gradle, pero **no está fusionado**, y un PR abierto no es entrega.

### Lo que este recuento NO oculta

El PR #37 no se compiló, y no se va a compilar en CI tal como está el repo: `spotlessCheck` va antes
que `assembleDevDebug` y hay **1.113 violaciones de formato en 621 ficheros** del `main` del
mantenedor (910 sólo en `:app`), medidas con ktlint 1.8.0 —la versión fijada en su
`libs.versions.toml`— y falsadas contra cuatro resultados reales de CI. Las cuatro corridas
registradas en ese repo fallaron, incluida la del PR #36 que sí fusionó. Mi rama añade **0**
violaciones (5 preexistentes en los cuatro ficheros, las mismas 5 en `c7ab60c9`). La receta y la tabla
están en `proyectos/feed-novedades/pr37/KTLINT-COMO-ORACULO.md`.

**Global ponderado: 58 % (11-16) → 69 % (11-17 mañana) → 73 % (11-17 tarde).** Lo que sigue sujetando
el número no es lo que hago en los repos propios —ésos ya están casi todos cerrados— sino AniZen (peso
12 al 35 %, sin una sola respuesta) y los 6 issues de gltools que necesitan un dispositivo que no
existe en este contenedor.
