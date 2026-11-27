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
