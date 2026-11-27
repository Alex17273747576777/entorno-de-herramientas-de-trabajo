# Estudio comparativo del ecosistema (`miyomi.app` y `anipirate.xyz`) — Diferenciación sin clonación

Fecha de referencia: `2026-11-26` (America/Santo_Domingo)

## 1. Catálogos explorados
- **`https://miyomi.app/`** (`miyomiorg/Miyomi`): directorio abierto con **150+ aplicaciones**, **47+ ecosistemas de extensiones** y **24+ guías** de configuración para manga, anime, novelas ligeras y herramientas locales/autoalojadas.
- **`https://anipirate.xyz/`** (`SehonYT/anipirate`, `/directory`): índice comunitario con **237 entradas verificadas** entre apps nativas, clientes Android TV, servidores autoalojados, lectores web, utilidades de descarga y trackers.

## 2. Arquetipos destacados observados (fuera de nuestros 8 repositorios base)

| Proyecto (GitHub) | Nicho y personalidad propia | Fortalezas distintivas verificadas |
| :--- | :--- | :--- |
| `yomihon/yomihon` | Lector Mihon para estudiantes de idiomas | OCR local en tiempo real en viñetas para extraer y estudiar texto |
| `akitaonrails/FrankYomik` | Traducción visual automatizada | Edición e inserción directa sobre el arte original |
| `mednasserallah/tankobon` | Biblioteca local pura por **tomos** | Cero extensiones remotas, parseo de ediciones/ómnibus, portadas por volumen |
| `Gent8/Taison` | Control fino sin sobrecarga visual | Mejoras QoL puntuales sobre Mihon con distribución F-Droid |
| `dmzz-yyhyy/LightNovelReader` | Lector Compose nativo de novelas ligeras | Exportación directa a EPUB, estilos de lectura y estantería local |
| `Anxcye/anx-reader` / `readest/readest` | Lectura profunda de libros multiplataforma | Lectura paralela, estadísticas, sincronización WebDAV y resúmenes/herramientas de lectura |
| `5rahim/seanime` | Servidor autoalojado + cliente web/escritorio | Gestión centralizada de anime/manga en red local |
| `NuvioMedia/NuvioMobile` / `gg-shub/anikentv` | Experiencia TV/escritorio/móvil sincronizada | Navegación Android TV / Leanback y biblioteca sincronizada con subtítulos y carátulas |
| `RyanYuuki/AnymeX` / `aayush2622/Dartotsu` | Clientes Flutter multi-tracker | Integración centrada en AniList, MAL y Simkl multiplataforma |
| `RockinChaos/Shiru` | Gestor en tiempo real sin esperas | Seguimiento y reproducción directa de biblioteca/torrents en escritorio |

## 3. Ideas diferenciadas por proyecto (potenciar su nicho sin copiar ni clonar)

Principio rector: en lugar de replicar exactamente las mismas funciones en los 8 proyectos, cada propuesta fortalece la **rama propia** de cada app:

1. **`Harrys-HQ/ShinKu`** *(Identidad: lector inteligente de manga con IA supervisada y diagnóstico local)*
   - **Oportunidad diferenciadora:** evolucionar su caché de glosarios (`#47`) y agrupación determinista (`#48`) hacia una **memoria contextual offline/opt-in de serie** (resúmenes locales de capítulos previos o glosario vivo de personajes antes de retomar un tomo pausado, inspirado en herramientas de lectura como `anx-reader`/`Emaki`), sin diluir su foco en manga añadiendo reproductores de TV/torrents.
2. **`unseensnick/Reikai`** *(Identidad: biblioteca unificada minimalista manga + novelas ligeras local-first)*
   - **Oportunidad diferenciadora:** reforzar su eje Manga + LN (`LnPluginHost`) con **empaquetado de volúmenes/arcos a EPUB/CBZ local** y detección estructurada de tomos/ómnibus locales (inspirado en `LightNovelReader` y `tankobon`), manteniendo la austeridad que exige su `CONTRIBUTING.md`.
3. **`PineappleTwilight/hyoukan`** *(Identidad: motor gráfico WebGPU + visión/OCR en dispositivo `yakuyomi-engine`/`llamatik`)*
   - **Oportunidad diferenciadora:** profundizar en su nicho único de procesamiento local en GPU/OCR incorporando **lookup léxico al tocar globos OCR** para lectores de idiomas (inspirado en `yomihon`) y limpieza/rotulado local no destructivo en capas (inspirado en `FrankYomik`), aprovechando su propio motor `houri-engine`.
4. **`Kototoro-app/Kototoro`** *(Identidad: puente multiplataforma KMP Android + Desktop + iOS y ecosistemas `Legado`/`TVBox`/`Cloudstream`)*
   - **Oportunidad diferenciadora:** potenciar su arquitectura KMP + `desktop-runtime` como **servidor/puente LAN + OPDS entre móvil y escritorio** (inspirado en `Seanime` / `Komga` / `Readest`) para continuar lectura y descargas locales dentro de la red del hogar sin depender de la nube.
5. **`salmanbappi/AniZen`** *(Identidad: reproductor anime Compose + shaders Anime4K + calendario de emisión y `SuggestionSection`)*
   - **Oportunidad diferenciadora:** llevar su personalidad audiovisual hacia **perfiles adaptativos para Android TV / D-pad y línea temporal interactiva de emisión multi-tracker** (inspirado en `AnikenTV`, `NyanTV` y `AnymeX`), sin convertirla en un clon lector de EPUB/cómics.
6. **`Arthurpendragon9876/DeepSync`** *(Identidad: continuidad de estado entre 3 plataformas — `Yugen` Android, `Yomi` Windows y `Shinkai` Linux)*
   - **Oportunidad diferenciadora:** centrar su evolución en **handoff instantáneo de sesión entre móvil y escritorio** (posición exacta de página/minuto, cola de reproducción y conflictos `ReplicaMerger` resueltos de forma transparente como en `Nuvio`/`Readest`).
7. **`Foxlations/Foxlations`** *(Identidad: app Flutter ligera multi-formato con soporte Nativo/FFI)*
   - **Oportunidad diferenciadora:** capitalizar Flutter para entregar **paridad ligera escritorio + móvil** y una **suite mínima automatizada `flutter test`** sobre sus parsers de migración (`.fox`/`.tachibk`/`.mangayomi`/`.lnreader`), tomando referencia de proyectos Flutter maduros como `Dartotsu` / `AnymeX`.
8. **`Noirero/Miyorare`** *(Identidad: santuario personal híbrido Kotatsu/Mihon con Notas Personales, Favoritos Privados, Source Packs curados y Predicción de Capítulos)*
   - **Oportunidad diferenciadora:** reforzar lo que ya lo distingue en `miyomi.app`: **verificación de salud/confianza de `Source Packs` desde la app** y **enriquecimiento del calendario de predicción de capítulos** vinculado a las notas privadas y etiquetas de estado personal.

## 4. Clonación, pruebas ejecutadas e Issues publicados en proyectos del ecosistema (2026-11-26/27)

Además de los 8 repositorios base (`Noirero/Miyorare`, `Harrys-HQ/ShinKu`, `unseensnick/Reikai`, `PineappleTwilight/hyoukan`, `Foxlations/Foxlations`, `Kototoro-app/Kototoro`, `Arthurpendragon9876/DeepSync`, `salmanbappi/AniZen`), se clonaron y probaron aplicaciones distintivas relevadas desde `miyomi.app` y `anipirate.xyz`:

| Repositorio | Clon y pruebas ejecutadas | Hallazgos e Issues abiertos (sin clonación) |
| :--- | :--- | :--- |
| `akitaonrails/FrankYomik` (`555be90`) | `go test ./...` **PASS** (`65.8s`); `PYTHONPATH=. pytest` (`182` unit tests): **175 passed, 7 failed** en `test_bytes_io.py` | `#7` (importación temprana de `fugashi` en `kindle/processor.py:35` rompe flujo puro `TRANSLATE`) y `#8` (glosario y lecturas por serie para el nicho *Hold-to-Peek Lens*) |
| `RockinChaos/Shiru` (`a5ac501`) | Inspección de 76 JS + reproducción en Node v20.20.2 sobre `common/modules/anime/animeresolver.js` | `#186` (`alternativeTitles()` elimina `ona`/`ova`/`oav`/`movie` sin límites de palabra, corrompiendo títulos como `Akatsuki no Yona` y `Persona 5`) |
| `dmzz-yyhyy/LightNovelReader` (`fa98bf5`) | `./gradlew :epub:test` con OpenJDK 21 y Gradle 9.5.1 | `#544` (`:epub:test` falla en Gradle 9 porque `GenerateSimpleBookTest.kt` y `XmlBuilderTest.kt` solo declaran `fun main()` sin `@Test`) |
| `yomihon/yomihon` (`c743d91`) | Auditoría de `DictionarySearchScreenModel.kt`, `OcrScanManager.kt`, `AnkiDroidRepositoryImpl.kt` | `#40` (caché de diccionario conserva `existingTermExpressions` obsoleto) y `#41` (etiquetas contextuales de manga/capítulo en exportaciones AnkiDroid) |
| `5rahim/seanime` (`main`) | `go test` en verde para `internal/continuity`, `internal/customsource`, `internal/directstream`, `internal/manga/...` y `internal/util/...` | `#1010` (extender `internal/continuity` al progreso manga página/capítulo + feed OPDS LAN opt-in de solo lectura) |
| `Gent8/Taison` (`33f3bb3`) | Auditoría de `TaisonEntryLink.kt`, `DeepLinkScreenModel.kt` y `MangaScreen.kt` | Hallazgo verificado en `shareManga()` (`publicUrl` opcional omitido si `getMangaUrl()` falla); repositorio archivado en solo lectura (`HTTP 403`) |
| `readest/readest` (`main`) | Inspección de suite `foliate-cbz-page-order.test.ts` y verificación de `test-koplugin.mjs` | Referencia multiplataforma de ordenamiento natural CBZ y continuidad entre dispositivos |

## 5. Ronda de respuestas a mantenedores y nuevos Issues sin duplicados (2026-11-27)

- **Respuestas publicadas (7 hilos):**
  - `Noirero/Miyorare#1057` (confirmada estrategia sin duplicación y entregados esquemas anonimizados de Usagi, Kototoro V1/V3 y Aniyomi `.tachibk`).
  - `Noirero/Miyorare#1058` (acordado separar descubrimiento hacia Explore, conservar agrupación visual no destructiva en Feed y priorizar `SuggestionsWorker` + carruseles diferidos).
  - `PineappleTwilight/hyoukan#104` (agradecido el aterrizaje de `PlainBookConverter` y `NovelPluginRuntime`, respaldando evitar shims parciales de cheerio/ESM).
  - `Arthurpendragon9876/DeepSync#35` (verificados todos los llamadores de `ensureChapterLoaded` en `Dispatchers.IO`/`Default`, agradecido y cerrado limpiamente) y `#42`.
  - `Harrys-HQ/ShinKu#60` (confirmada resolución de `#53`–`#57` y `#60` en `v2.8.6-preview.4`).
  - `unseensnick/Reikai#114` (agradecida la revisión de `#112`–`#119` y los parches en nightly `r5341`).
- **Segunda oleada de clones y nuevos Issues verificados sin duplicados (3):**
  - `Anxcye/anx-reader#1024` (`0c7fc1a` / `1.15.0+6358`): `AiKeyRotator.getNextKey()` puede devolver una clave vacía cuando coexiste un campo habilitado en blanco junto a otra clave válida (`lib/service/ai/ai_key_rotator.dart`).
  - `RyanYuuki/AnymeX#669` (`9274a66` / `3.2.1+43`): `getAiRecommendations()` omite `AnimeSproutOptions` en `cacheKey`, devolviendo recomendaciones cacheadas obsoletas al cambiar filtros (`lib/ai/animeo.dart`).
  - `RyanYuuki/AnymeX#670`: suite inicial `flutter_test` pura en `test/` para `GistSyncService` y mapeo multi-tracker (`AniList`/`MAL`/`Simkl`) protegida contra regresiones sin tocar extensiones.
