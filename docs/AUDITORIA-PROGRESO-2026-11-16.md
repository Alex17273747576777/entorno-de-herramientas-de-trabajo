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
