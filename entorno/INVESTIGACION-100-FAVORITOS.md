# Los 100 favoritos de GitHub: qué se midió y qué se eligió

Fecha de medición: 2026-11-08, con la API de GitHub y token. Todos los números
de este documento salen de una llamada a la API en esa fecha, no de memoria.

## Lo primero: dos premisas que no aguantaron la medición

### 1. «Houri es el reemplazo de Komikku»

No lo es.

| | Komikku | Houri |
|---|---:|---:|
| estrellas | **5 001** | 45 |
| archivos | 3 004 | 3 758 |
| último push | 2026-11-07 | 2026-11-04 |
| licencia | Apache-2.0 | Apache-2.0 |

Komikku tiene **111 veces** más estrellas y sigue publicando. Houri es un fork
pequeño de la misma cadena:

```
Tachiyomi → TachiyomiSY → Mihon → Komikku → Houri
```

Es un descendiente, no un sucesor. Se usa la cadena como referencia de
compatibilidad de extensiones, que es donde sí manda, y no se presenta a Houri
como algo que no es.

### 2. «Reikai es más rápido»

Es el único que **mide** si lo es.

| | Reikai | Komikku | Yokai | Houri |
|---|---:|---:|---:|---:|
| estrellas | 47 | 5 001 | 1 922 | 45 |
| archivos `.kt` | 2 972 | 1 365 | 883 | 1 795 |
| tests de UI | **25** | 0 | 0 | 0 |
| tests de lector | **21** | 0 | 0 | 0 |
| archivos webview | 28 | 8 | 8 | 10 |
| cachés | 6 | 3 | 2 | 4 |

Los 21 tests de lector de Reikai, con nombre:

```
PageSlideTest                 TiledPictureTest
PagedReadingTest              WebtoonResizeAfterZoomTest
TextViewportContractTest      RenderedLinesParityTest
NovelTextViewportWindowTest   WebViewSeamPositionTest
NovelTapZonesTest             RecyclerPrependPositionTest
NovelBlankLineTest            RenderedLinesParityTest
NovelImageLayoutTest          NovelImageFailureTest
ReadAloudRubyCountTest        NovelWebDocumentTest
NovelWebImagesInterceptTest   NovelWebImagesCancelTest
ForeignKeyEnforcementTest     QuickJsCreationTest
HeadlessJsIntegrationTest
```

Komikku, Yokai y Houri tienen **cero**. Eso no demuestra que Reikai sea más
rápido: demuestra que es el único de los cuatro que puede saberlo. Sin emulador
—esta máquina no tiene `/dev/kvm`— no hay milisegundos, y sin milisegundos «es
más rápido» es una opinión.

Lo que sí se tomó de Reikai: **la disciplina de probar el lector**, no el código.

## Qué hay de verdad en cada repo, por función

Conteo por segmentos de ruta exactos. La primera medición buscaba subcadenas y
contaba `ai/` dentro de `reikai/`, dando 1 681 archivos de IA a Reikai cuando
tiene **cero**. Ese error se corrigió antes de decidir nada.

| repo | feed | sugerencias | IA | sync | velocidad | lector | extensiones |
|---|---:|---:|---:|---:|---:|---:|---:|
| SalmanBappi/AniZen | 0 | 0 | **10** | 50 | 2 | 2 | 130 |
| Harrys-HQ/ShinKu | 9 | 1 | **14** | 46 | 5 | 1 399 | 174 |
| Kototoro | 14 | **35** | 0 | **138** | 15 | 392 | 206 |
| Miyorare | 8 | 26 | 0 | 47 | 6 | 144 | 102 |
| DropSauce | 8 | 25 | 0 | 40 | 4 | 105 | 53 |
| Reikai | 5 | 0 | 0 | 64 | 4 | 219 | 215 |
| Houri | 5 | 1 | 0 | 51 | 9 | 143 | 203 |
| Kisara | 8 | **33** | 5 | 67 | 9 | 278 | **390** |
| Komikku | 4 | 1 | 0 | 49 | 3 | 72 | 179 |

## Los archivos concretos que se estudiaron

**Kisara** (`ifritraen/kisara`, 2★, Apache-2.0) — los modelos y las sugerencias:
```
app/src/main/java/eu/kanade/tachiyomi/data/ai/MangaColorizeEngine.kt
app/src/main/java/eu/kanade/tachiyomi/data/ai/SuperResolutionEngine.kt
app/src/main/java/eu/kanade/tachiyomi/data/ai/AiModelManager.kt
app/src/main/java/eu/kanade/tachiyomi/data/suggestions/SuggestionsWorker.kt
app/src/main/java/eu/kanade/tachiyomi/data/suggestions/HomeFeedWorker.kt
```
Es la fuente de `colorize.onnx` y `esrgan_x4.onnx` que van dentro del APK.

**ShinKu** (`Harrys-HQ/ShinKu`, 46★, Apache-2.0) — IA sin red y cursor por fuente:
```
app/src/main/java/com/shinku/reader/data/ai/MangaEmbeddingJob.kt
app/src/main/java/com/shinku/reader/data/ai/AiClusteringJob.kt
app/src/main/java/com/shinku/reader/ui/browse/feed/SourcePageCursor.kt
app/src/main/java/com/shinku/reader/domain/source/interactor/MlKitTranslationInteractor.kt
```
Hace agrupación por similitud **en el aparato**, con embeddings propios. Es lo
más cercano a «IA de verdad» que tiene el ecosistema sin depender de una API.

**AniZen** (`salmanbappi/AniZen`, 201★, Apache-2.0) — feed y asistente:
```
app/src/main/java/eu/kanade/tachiyomi/ui/home/FeedScreen.kt
app/src/main/java/eu/kanade/tachiyomi/ui/home/FeedManageScreen.kt
app/src/main/java/eu/kanade/tachiyomi/data/ai/AiManager.kt
app/src/main/java/eu/kanade/tachiyomi/data/ai/everythingmoe/EverythingMoeScraper.kt
```
El asistente lee todoenmoe para recomendar. Idea interesante; cero-X lo sustituye
por el motor local, que no depende de que una web siga viva.

**Kototoro** (`Kototoro-app/Kototoro`, 677★, Apache-2.0) — sugerencias:
```
app/src/main/kotlin/org/skepsun/kototoro/discover/ui/DiscoverViewModel.kt
app/src/main/kotlin/org/skepsun/kototoro/tracker/domain/feed/FeedSnapshotStore.kt
```
El motor de sugerencias más grande del ecosistema, pero atado a su base de datos.

**Miyorare** (`Noirero/Miyorare`, 20★, **GPL-3.0**) — solo el concepto:
```
IncompatiblePluginException.kt     fallar con un motivo, no "error inesperado"
```
De un GPL-3.0 no se copia ni una línea: cero-X es Apache-2.0 y así se queda.

**DropSauce** (`HuzaifaKhalid1311/DropSauce`, 233★, **GPL-3.0**) — solo el
concepto de feed ligero sin base de datos pesada.

## Lo que se implementó en cero-X

| pieza | de dónde viene la idea | archivo en cero-X |
|---|---|---|
| Feed multi-entrada con cursor por fuente | AniZen + ShinKu | `modules/feed/FeedManager.kt` |
| Sugerencias sin red con TF-IDF y coseno | Kisara + Kototoro | `modules/feed/SuggestionEngine.kt` |
| Caché de páginas con tope en bytes | Reikai (disciplina) | `modules/reader/PageCache.kt` |
| Prefetch según la red | Reikai | `modules/reader/ReaderPrefetcher.kt` |
| Colorización conectada a modelo real | Kisara | `modules/kisara/KisaraColorizer.kt` |
| Reescalado con dos modelos según la página | Kisara | `modules/kisara/KisaraUpscaler.kt` |

Nada de esto es código copiado. Cuando la fuente es GPL-3.0 se tomó el concepto;
cuando es Apache-2.0 se podría haber portado, pero arrastra su base de datos y su
paquete `eu.kanade`. Se reescribió con las piezas que cero-X ya tiene.

## Los otros 90 favoritos

De los 100, estos son los que tocan el nicho y no se usaron:

- **Navegadores/lectores alternativos**: `capyreader` (RSS), `koodo-reader`,
  `IReader`, `codeless` — fuera de alcance.
- **Descargadores**: `ytdlnis` (11 018★), `Ghost-Downloader-3`,
  `ab-download-manager` — buenos, pero no son lectores.
- **Herramientas de sistema**: `Shizuku-Next`, `InstallerX-Revived`,
  `Morphe-Manager` — útiles para el usuario, no son cero-X.
- **Extensiones**: `keiyoushi/extensions-source` (4 866★) es el repositorio de
  fuentes del ecosistema Mihon. cero-X lo consume por la capa 1, no lo copia.
- **Trackers**: `AniSync`, `Animite`, `hoshi` — candidatos para la
  sincronización que falta.
- **Otros lectores**: `rokku`, `Wammy`, `Futon`, `Kotatsu-Redo`, `Usagi`,
  `Tsuki`, `chimahon` — todos forks de la misma cadena, con las mismas
  limitaciones. `Kotatsu-Redo` (1 022★) es el más vivo de los pequeños.

## Conclusión, en una línea

El ecosistema tiene **un solo** proyecto con IA propia y verificable (Kisara),
**uno** con IA sin red de verdad (ShinKu), **uno** con feed maduro (AniZen),
**uno** con motor de sugerencias grande (Kototoro) y **uno** que mide su lector
(Reikai). Ninguno es mejor que todos los demás: cada uno gana en una cosa. Por
eso cero-X toma la idea de cada uno en lugar de copiar una app entera.
