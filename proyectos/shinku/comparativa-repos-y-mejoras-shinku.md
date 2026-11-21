# Comparativa de repositorios y análisis de mejoras para ShinKu

Fecha de análisis: 2026-11-21  
Repositorios clonados de forma completa (`--depth` sin recortar, `is-shallow-repository = false`) en `/tmp/repos-compare/`:

| # | Repositorio | Rama / HEAD | Commits totales | Últimos 30d / 90d | Último commit | Tamaño clon | Licencia | Base / Stack |
|---|---|---|---|---|---|---|---|---|
| 1 | `PineappleTwilight/hyoukan` | `master` (`42ea727d8`) | 12.008 | 137 / 1.194 | 2026-11-20 | 153 MB | Apache-2.0 | Kotlin / Android (25 módulos + 2 `includeBuild`), base Komikku/SY |
| 2 | `Suwayomi/Suwayomi-Tsumiru` | `main` (`c01ad256`) | 1.246 | 114 / 321 | 2026-11-07 | 85 MB | MPL-2.0 | Dart / Flutter (`v1.6.5`), cliente para Suwayomi-Server |
| 3 | `unseensnick/Reikai` | `main` (`00206fe6a`) | 3.891 | 153 / 2.338 | 2026-11-11 | 312 MB | Apache-2.0 | Kotlin / Android (16 módulos), base Mihon + novelas |
| 4 | `Harrys-HQ/ShinKu` | `main` (`58a3d14a66`) | 9.766 | 51 / 98 | 2026-11-21 | 228 MB | Apache-2.0 | Kotlin / Android (7 módulos), base TachiyomiSY/Mihon (`v2.8.5` / 151) |

*(Referencia del workspace restaurado desde Drive: `work/shinku` está en código equivalente a `v2.8.4` / 148, y el fork `Alex17273747576777/ShinKu` apunta a `043ab7d8e6`, anterior a los PRs `#32`–`#40` de `Harrys-HQ/ShinKu`.)*

---

## 1. Comparativa técnica: #1 Hyoukan vs #3 Reikai vs #4 ShinKu

### 1.1 Arquitectura y modularidad
- **#1 Hyoukan (`PineappleTwilight/hyoukan`)**: es el más modular y experimental en capacidades de lectura. Divide el proyecto en 25 módulos Gradle (`:core:concurrency`, `:core:metro`, `:core:navigation`, `:core:viewmodel`, `:yakuyomi`, `:mtl-spine`, `:upscale`, `:llamatik-native`, `:telemetry`) más dos builds externos (`external/yakuyomi-engine`, `external/webgpuviewer-houri`). Usa DI con Metro + Navigation3 (`LocalBackStack`).
- **#3 Reikai (`unseensnick/Reikai`)**: 16 módulos Gradle sobre Mihon moderno (`gradle/build-logic`, `:core:metro`, `:core:archive`, `:icons:material-symbols`, `:telemetry`), con una capa propia muy ordenada bajo el paquete `reikai.*` que separa dominio de fusión (`reikai/domain/merge/*`), novelas (`reikai/domain/novel/*`), selección unificada (`reikai/presentation/selection/*`) y extensiones (`reikai/presentation/browse/extension/*`).
- **#4 ShinKu (`Harrys-HQ/ShinKu`)**: 7 módulos Gradle (`:app`, `:core-metadata`, `:core:common`, `:data`, `:domain`, `:i18n`, `:i18n-sy`). Mantiene Voyager + Injekt heredados de SY, con mayor concentración de lógica dentro de `:app` (`com.shinku.reader.*`). Destaca en identidad visual ("Sanctuary", dock flotante con Haze, Jump-Back Deck), Feed Discover con caché/cuotas (`FeedRequests.kt`, `SourcePageCursor.kt`), IA con Gemini/embeddings locales y Journey/estadísticas.

### 1.2 Diferencias clave por área funcional

| Capacidad | #1 Hyoukan | #3 Reikai | #4 ShinKu (`v2.8.5`) |
|---|---|---|---|
| **Selección múltiple en Exploración (Browse / Global Search / Feed)** | **Completa**: `BulkFavoriteViewModel` + `BulkSelectionToolbar` (`SelectAll`, `Invert`, `Add to library`) conectado en `BrowseSourceScreen`, `GlobalSearchScreen`, `SourceFeedScreen`, `FeedTab`, `MigrateSearchScreen`, `RecommendsScreen` y `RelatedMangasScreen`. | **Completa y multi-tipo**: `EntryBulkFavoriteViewModel<T>` + `MixedBulkSelection` (`BulkSelectionSupport.kt`) que permite seleccionar manga y novelas en un mismo lote en búsqueda global/feed con prompts separados de categoría. | **Ausente**: en `BrowseSourceScreen.kt` (L275) el long-press sólo agrega/quita un manga individual; en `GlobalSearchScreen.kt` (L93) sólo abre `MangaScreen`; en `FeedScreen.kt` no hay `onLongClickManga`. |
| **Selección múltiple en Biblioteca** | Extraída a `LibrarySelectionController` (`cleanTitles`, `resetInfo`, acciones de lote fuera del ViewModel). | `SelectionStore<T>` con mutex (`synchronized(lock)`) para que limpiezas/refrescos en segundo plano no pisen toques del usuario. | Implementada en `LibraryTab.kt` + `LibraryToolbar.kt` (`LibrarySelectionToolbar`) + `LibraryBottomActionMenu` (`Download`, `Category`, `Mark read`, `More`). |
| **Gestión de entradas duplicadas y fusión (Merge)** | Pantalla dedicada **`DuplicateMangaScreen`** + `MergeMangaBySmartSearch` + `EditMergedMangaAdapter`. | Sistema completo en `reikai/domain/merge/*`: **`ManageMergeSourcesDialog`** (reordenar fuentes, anular prioridad, separar o eliminar miembros en lote), `EntryMergeManager`, fusión de categorías/capítulos/trackers y listas de errores de actualización. | En `v2.8.3`–`v2.8.5` añadió `MergeGroupRepositoryImpl`, `GroupManga` y `dedupeByMergeGroup` (`#33`/`#34`), pero **sin pantalla dedicada de duplicados** ni diálogo avanzado para gestionar/reordenar grupos existentes como Reikai. |
| **Gestión de extensiones** | Multi-repo persistente (`7ca14c9fa`), `ExtensionsTab` + `ExtensionDetailsScreen`, instalador estándar/Shizuku. | **`ReikaiExtensionsTab.kt`** unificada para extensiones Mihon + plugins de novelas (QuickJS/Tsundoku/IReader), badges de tipo, estado de carga/fallo claro y gestión de repositorios (`RepositoriesScreen`). | `ExtensionsTab.kt` + `ExtensionsScreen.kt` (745 líneas) + `ExtensionDetailsScreen` + `ExtensionReposScreen`; funcional, pero acciones clave como **Filtro** y **Repositorios** quedan escondidas en el menú overflow (`AppBar.OverflowAction`), y las fuentes/extensiones de manga carecen de vista unificada de salud/diagnóstico en Browse. |
| **Lector y renderizado** | WebGPU (Vulkan) con HDR/LUT/ArtCNN upscaling + lector nativo completo de EPUB/novelas + búsqueda intra-capítulo. | Lector Mihon + lector de novelas nativo/WebView + auto-webtoon + bypass Cloudflare vía Solverr/FlareSolverr. | Lector SY/Mihon + OCR de área (`PixelCopy` + MLKit) + traducción con caché en disco + audio ambiental CC0 + soporte AVIF animado (`#30`). |

*(Nota sobre #2 `Suwayomi-Tsumiru`: al ser un cliente Flutter de `Suwayomi-Server`, la biblioteca, extensiones y descargas residen en el servidor remoto; aporta ideas útiles de UX multiplataforma como filtros/orden por categoría compartidos y lectura offline automática sin conexión, pero su modelo de datos no es comparable directamente con los forks Android locales.)*

---

## 2. Evaluación de las mejoras propuestas para ShinKu

### 2.1 Botones de selección múltiple en Exploración y navegación de la Biblioteca
**Diagnóstico verificado en código (`Harrys-HQ/ShinKu`)**:
1. **En Exploración (`Browse`) falta por completo**:
   - `BrowseSourceScreen.kt` (L275–287) sólo ejecuta una acción unitaria en `onMangaLongClick` (`addFavorite` o diálogo individual).
   - `GlobalSearchScreen.kt` (L93) abre `MangaScreen` en `onLongClickItem`; no permite marcar múltiples resultados.
   - `FeedScreen.kt` / `FeedTab.kt` no exponen `onLongClickManga`.
   - Tampoco existe un `BulkFavoriteViewModel` ni un `BulkSelectionToolbar` reutilizable (a diferencia de Hyoukan y Reikai).
2. **En Biblioteca (`Library`) sí existe barra de selección, pero con fricciones de navegación**:
   - `LibraryTab.kt` (L148–218) usa `LibrarySelectionToolbar` (arriba: contador, *Seleccionar todo*, *Invertir*, cancelar) y `LibraryBottomActionMenu` (abajo: *Descargar*, *Categoría*, *Marcar leído*, *Más*).
   - **Problema real detectado**: cuando `state.selectionMode` pasa a `true`, `HomeScreen.kt` (L134–141) oculta el dock inferior flotante (`HomeScreen.showBottomNav(!state.selectionMode)`), pero `LibraryContent.kt` mantiene `dockBottomPadding = 84.dp` fijos en `LibraryTab.kt` (L256–262), mientras `LibraryBottomActionMenu` entra en `Scaffold.bottomBar`. Además, no existe un botón explícito en la barra normal para entrar en modo selección sin depender del gesto *long-press*, y la lógica de selección en `LibraryScreenModel.kt` (L1281–1346) carece de bloqueo tipo `SelectionStore` (Reikai) si `getFavoritesFlow()` emite mientras el usuario selecciona.

**Recomendación concreta**:
- Adoptar el patrón **`BulkFavoriteViewModel` + `BulkSelectionToolbar`** de Hyoukan (más el `SelectionStore<T>` con lock de Reikai) y conectarlo en `BrowseSourceScreen`, `GlobalSearchScreen`, `FeedScreen` y `SuggestedTitlesScreen`, incluyendo manejo de duplicados en lote y asignación de categorías antes de añadir.
- En Biblioteca, añadir botón de acceso rápido al modo selección en el menú/barra superior (útil en accesibilidad y una mano) y ajustar el padding inferior dinámicamente cuando `state.selectionMode` oculta el dock flotante.

### 2.2 Apartados específicos para gestión de entradas de mangas y extensiones
**Diagnóstico verificado**:
1. **Gestión de entradas de mangas**:
   - Aunque `#33` y `#34` añadieron `MergeGroupRepositoryImpl` y `dedupeByMergeGroup`, el usuario no tiene un **centro de gestión** para revisar entradas duplicadas, inspeccionar qué series están agrupadas o separar/reordenar fuentes de un grupo (como **`DuplicateMangaScreen`** en Hyoukan o **`ManageMergeSourcesDialog`** en Reikai).
   - `EditMangaDialog.kt` existe para editar metadatos manualmente, pero sin autocompletado desde trackers (`Fill from tracker` de Reikai) ni vista consolidada de **errores de actualización de biblioteca** (`Library update errors` de Reikai).
2. **Gestión de extensiones**:
   - En `ExtensionsTab.kt` (L41–50), tanto *Filtrar* como *Repositorios de extensiones* están relegados a `AppBar.OverflowAction` (ocultos tras los 3 puntos) en lugar de ser accesos directos visibles.
   - Falta una vista/pestaña clara que unifique: repositorios activos + estado de confianza/firma + diagnóstico de fuentes fallidas (que hoy vive disperso entre `FeedSourceFailures`, `ExtensionReposScreen` y `ExtensionDetailsScreen`).

**Recomendación concreta**:
- Crear un apartado dedicado en Biblioteca/Más o en el menú de Biblioteca para **Gestión de entradas** (Duplicados detectados + Grupos de fusión + Entradas con error de actualización + limpieza/reset en lote estilo `LibrarySelectionController` de Hyoukan).
- Promover **Repositorios** y **Filtros** a acciones primarias o chips rápidos en `ExtensionsTab`, añadir selección múltiple para instalar/actualizar/desinstalar extensiones en lote y mostrar estado de confianza/firma sin tener que entrar ficha por ficha.

### 2.3 Pequeños detalles optimizables detectados en el código
1. **Preferencia muerta en `BrowseTab.kt` (L75)**: `val feedTabInFront by remember { Injekt.get<UiPreferences>().feedTabInFront().asState(scope) }` se lee pero **no se usa** para reordenar `tabs` (en Hyoukan `BrowseTab.kt` L63–90 sí ordena `feedTab` vs `sourcesTab` y calcula dinámicamente `extensionsIndex`).
2. **Consultas bloqueantes y carga excesiva en `LibraryScreenModel.kt` y `FeedScreenModel.kt`** (confirmado también en `docs/code-optimization-follow-up.md`):
   - `LibraryScreenModel.kt` L760 ejecuta consultas por cada manga fusionado dentro de `getFavoritesFlow()`, y L1408 bloquea al obtener trackers en vez de reutilizar el flujo ya suscrito.
   - `FeedScreenModel.kt` L597 llama a `GetReadingStats.await()` completo en cada refresh sólo para calcular `bestGenres`.
3. **Caché de traducción en disco (`TranslationDiskCache.kt`)**: `retranslateCurrentPage()` limpia memoria pero no fuerza invalidación en disco; `putPage()` reescribe el JSON completo sin bloqueo por capítulo ni escritura atómica (`AtomicFile`).
4. **Trabajo redundante en `MangaEmbeddingJob.kt`**: re-embebe toda la biblioteca sin filtrar por `lastMetadataUpdate` ni descargar el modelo de forma atómica a archivo temporal antes de renombrar.
5. **Paginación de `SuggestedTitlesScreenModel.kt`**: mezcla errores de red con páginas vacías o duplicadas al calcular `hasMore`, en lugar de usar un cursor por fuente como ya hace `SourcePageCursor.kt` en el Feed principal.

---

## 3. Próximo paso recomendado (orden de ejecución)

1. **Sincronizar base**: decidir si trabajar sobre `Harrys-HQ/ShinKu` (`v2.8.5`, donde ya están `#32`–`#40`) o mergear `v2.8.5` hacia `Alex17273747576777/ShinKu`.
2. **Sprint 1 — Selección múltiple en Exploración + fix `BrowseTab`**: portar `BulkFavoriteViewModel` + `BulkSelectionToolbar` (inspirado en Hyoukan) con `SelectionStore` (Reikai) a `BrowseSourceScreen`, `GlobalSearchScreen` y `FeedScreen`, y activar `feedTabInFront` en `BrowseTab.kt`.
3. **Sprint 2 — Apartados de Gestión de Entradas y Extensiones**: añadir `DuplicateMangaScreen` + gestión visual de grupos de fusión (`ManageMergeSourcesDialog`) y promover filtros/repos/acciones en lote en `ExtensionsTab`.
4. **Sprint 3 — Optimizaciones de rendimiento**: corregir `feedScreenModel` (`bestGenres` ligero), eliminar bloqueos en `LibraryScreenModel`, hacer atómica la caché de traducción e incremental `MangaEmbeddingJob`.
