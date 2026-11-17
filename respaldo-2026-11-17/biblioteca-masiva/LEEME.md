# Biblioteca masiva + fusión de entradas — ShinKu ⇄ AniZen ⇄ Reikai

Ronda del 2026-11-15 (T0 = 16:07:52Z). Encargo: otro issue en cada repo para que soporten
bibliotecas masivas y optimicen al nivel de **Reikai**, incluyendo la fusión de entradas que éste
trae por defecto; traducir los issues anteriores al inglés; subirlos con el menor ruido posible.

## Entregables

| Qué | Dónde |
|---|---|
| Issue ShinKu #33 (biblioteca masiva + fusión) | https://github.com/Harrys-HQ/ShinKu/issues/33 |
| Issue AniZen #95 (biblioteca masiva + fusión) | https://github.com/salmanbappi/AniZen/issues/95 |
| Cuerpos publicados (espejo fiel) | `ISSUE-SHINKU-BIBLIOTECA.md` · `ISSUE-ANIZEN-BIBLIOTECA.md` |
| Issues de feed ya en inglés puro | https://github.com/Harrys-HQ/ShinKu/issues/32 · https://github.com/salmanbappi/AniZen/issues/94 (espejos en `work/feed-novedades/ISSUE-*.md`) |
| Estado de variables de la ronda | `work/edt/docs/ESTADO-VARIABLES-2026-11-15.md` |

## Procedencia (para reaplicar tras un reinicio)

```bash
git clone --depth 1 https://github.com/unseensnick/Reikai.git          # main 00206fe6ae0c6cf87e2f6114b59164ea295a6fd1
git clone --depth 1 https://github.com/Harrys-HQ/ShinKu.git            # main 043ab7d8e68e8a77752805c34969a2477195826a
git clone --depth 1 https://github.com/salmanbappi/AniZen.git          # master 95160a724d1147777dd1f7997fff4885a4cd9deb
```

Los tres Apache-2.0. Clones en `/var/tmp` (**volátiles**): `/var/tmp/reikai/reikai` (100 MB),
`/var/tmp/feed/{shinku,anizen}` (110 MB / 33 MB, árboles prístinos).

## Verificación de las citas (todo con fichero y línea, leído del código)

- **Reikai**: `merge_group.sq` (grupos persistidos, `UNIQUE(manga_id)`, FK en cascada,
  `source_priority`, `override_source_ranking`), `ReikaiLibraryPreferences.kt:161`
  (`auto_merge_same_title` por defecto **true**, «repurposed from silent auto-merge»),
  `DuplicatePrompt.kt:32` (`suggestGroupingOnAdd`), `SettingsLibraryScreen.kt:148`,
  `MergeGroupDedup.kt` (`dedupeByMergeGroup` / `onePerSeries` / `bucketByMergeGroup`),
  `dedupe_merged_ids.sq` + `MergedDuplicateCarryMigration.kt`, `LibraryAssembly.kt:100`
  (`itemsByKey.getOrPut`), `ReikaiLibraryContent.kt:238` (claves estables),
  `libraryView.sq` (el `CASE WHEN EXISTS` del join de history), módulo `baseline-profile/`,
  10 vistas SQL, índices parciales, y 7 tests del subsistema de merge.
- **ShinKu**: `mangas.sq:122-149` (`getDuplicateLibraryManga` con CTE de `chapter_counts` que
  excluye scanlators), `BrowseSourceScreen.kt:269-278`, `BrowseSourceScreenModel.kt:448`,
  `DuplicateMangaDialog.kt:81`, `merged.sq` (con `chapter_priority`, `chapter_sort_mode`,
  `info_manga`, `get_chapter_updates`, `download_chapters`, 2 FK y 2 índices),
  `ui/manga/merged/EditMergedManga*`, `BackupMergedMangaReference.kt`, `libraryView.sq`,
  índices parciales en `migrations/13.sqm:225-228`, `macrobenchmark/` **sin** `baseline-profile/`.
- **AniZen**: `merged.sq` (con `episode_priority` «the deduplication uses», `episode_sort_mode`,
  `info_anime`, `get_episode_updates`, `download_episodes`), `MergedAnimeReference.kt`
  (`EPISODE_SORT_NONE/NO_DEDUPE/PRIORITY`), `MergeAnimeSettingsUpdate.kt`,
  `ui/anime/merged/EditMergedAnime*`, `GetDuplicateLibraryAnime.kt:6-11` +
  `AnimeRepositoryImpl.kt:70-72` + `animes.sq:128` + `DuplicateAnimeDialog.kt:34` usado en
  `BrowseSourceScreen.kt:585`, `animes.parent_id` (temporadas) con índice en `:45`, 8 vistas SQL,
  `activity_log.sq` + `SourceHealthCache`, `macrobenchmark/` **sin** `baseline-profile/`.

## Dos correcciones publicadas (no silenciosas)

La primera versión de #33 decía que ShinKu no detectaba duplicados, y la de #95 describía la fusión
de AniZen como «de temporadas» y sin detección automática. **Ambas eran falsas**: los dos repos
detectan duplicados al añadir y los dos tienen la tabla `merged` del linaje SY con prioridad de
capítulos/episodios. Corregido en público con una sección «Correction (verified after posting — read
this first)» al principio de cada issue y la propuesta re-alcanceada a lo que de verdad falta
(agrupar en un toque desde el diálogo que ya existe, grupos persistidos con `UNIQUE`, memoria de
parejas rechazadas, un único helper de recuento, arrastre de estado fuera de la BD, y el paquete de
rendimiento).

---

## Publicación de la Fase 1 (2026-11-15, 17:03Z–17:10Z)

Los parches ya no son sólo locales: están publicados, cada uno por la vía que permite su repo.

| Repo | Vía | Referencia | Por qué esa vía |
|---|---|---|---|
| ShinKu | **Pull request** | https://github.com/Harrys-HQ/ShinKu/pull/34 · rama `Alex17273747576777:merge-groups-phase1` · commit `8e035e149a` · base `main` · 3 ficheros +92 | Su `CONTRIBUTING.md:10` dice «Pull requests are welcome!» y `build_check.yml` corre en cada PR |
| AniZen | **Rama pública en fork, sin PR** | https://github.com/Alex17273747576777/AniZen/tree/merge-groups-phase1 · commit `e1c6b51c195b` · 3 ficheros +93 · referenciada dentro del issue #95 con el `git fetch` + `cherry-pick` | Su `AGENTS.md` (Non-negotiables → Git) dice **«Never \| Open a pull request»**: `preview.yml` publica un release en cada run de PR y eso desincroniza el esquema de etiquetas `r<commitCount>` |

Ambos push verificados comparando `git rev-parse HEAD` con `git ls-remote` (idénticos).

### Reglas del destino respetadas (leídas antes de escribir, no después)

- **Convención SQLDelight de los dos repos:** toda tabla existe **dos veces** — en el `.sq` (de donde
  SQLDelight genera `Schema.create()`, o sea la instalación limpia) y en el `.sqm` (lo que se reproduce
  al actualizar). Comprobado contra todos los casos reales: `feed_categories.sq`+`133.sqm`,
  `activity_log.sq`+`134.sqm`, `custom_buttons.sq`+`129.sqm` (AniZen); `excluded_scanlators.sq`+`29.sqm`,
  `manga_embeddings.sq`+`41.sqm` (ShinKu). **La primera versión de estos parches declaraba la tabla sólo
  en la migración**, lo que habría dejado sin ella a toda instalación nueva. Corregido antes de publicar.
- **Marcadores de procedencia de AniZen** (`AGENTS.md` → Provenance markers): el Kotlin nuevo va envuelto
  en `// ANZ -->` … `// ANZ <--`, y además lleva un `// ANZ` **al final de una línea de código**, porque
  `scripts/check-provenance.sh` (regla R3) descarta las líneas de sólo comentario antes de buscar el
  marcador: con los dos símbolos sueltos no lo habría visto.
- Numeración secuencial de migraciones (`ShinKu AGENTS.md §3`, `PROJECT_MEMORY.md:52`): 42 tras 41,
  147 tras 146 — re-comprobado tras `git fetch` al HEAD real, que no se había movido.
- Ningún locale ni módulo i18n congelado tocado (R1/R2 de AniZen). `max_line_length = 120` de ambos
  `.editorconfig` respetado. Sin cabecera de licencia: los ficheros de dominio de los dos repos
  empiezan directamente en `package`.

### Verificación ejecutada (reproducible con `python3 validar_sql.py`)

El DDL de **las dos rutas** (`.sq` y `.sqm`) se ejecutó contra **SQLite 3.46.1** real vía el módulo
`sqlite3` de python3, con `PRAGMA foreign_keys=ON`, más las consultas y las restricciones:
**13 aserciones por repo, 0 fallos** — `UNIQUE` impide la doble pertenencia, las dos FK rechazan filas
inexistentes, borrar la entrada elimina su pertenencia en cascada, borrar el grupo lo vacía, y
`getMembers` devuelve los ids ordenados por `source_priority, id`. `git apply --check` limpio en ambos
clones prístinos.

**Lo que NO se verificó:** nada de Kotlin/SQLDelight compilado (aquí no hay Android SDK, Gradle ni
`kotlinc`); ejecutar el SQL valida el DDL y el texto de las consultas, **no** la API generada
`DatabaseQueries`. El CI de ShinKu (`run 43739153438`, `spotlessCheck assembleDevDebug`) quedó en
**`action_required`**: es la aprobación que GitHub exige a un contribuidor nuevo desde un fork, así que
la primera compilación real sólo ocurrirá cuando un mantenedor la apruebe. En AniZen el guard de
procedencia se leyó, no se ejecutó. `MergeGroupDedup.kt` va sin prueba unitaria en esta fase.

---

## Ronda de las 21:22Z-21:44Z: de «nada compilado» a código compilado y ejecutado

Apareció utillaje real en el entorno (kotlinc, JDK 17, jars de Maven Central) y se usó para dejar de
declarar lo que antes sólo se argumentaba. Todo lo ejecutado está en `mediciones/` con su arnés.

| Fichero | Qué es |
|---|---|
| `mediciones/medida-kotlin.txt` | `dedupeByMergeGroup` (lineal) contra una réplica del escaneo por título (cuadrático), en JVM |
| `mediciones/medida-sql.txt` | SQLite 3.46.1 con 50.000 entradas y 5.000 grupos: pertenencia guardada vs el patrón real de `animes.sq:128` |
| `mediciones/medida_sql.py`, `mediciones/Medida.kt` | los dos arneses, reproducibles |
| `mediciones/Arnes.kt`, `mediciones/Log.kt`, `mediciones/evidencia-interactor.txt` | doble del repositorio + doble de `android.util.Log` y la salida real del interactor de AniZen (9 ✓) |
| `mediciones/validar_migracion.py`, `mediciones/validacion-migracion-43.txt` | equivalencia de esquema instalación-limpia vs actualización para el `43.sqm` de ShinKu (13 ✓) |
| `parches/shinku-fase1-pestanas-de-feed.patch` | Fase 1 del feed de ShinKu (pestañas), rama `feed-tabs-phase1` |

Dos hallazgos que se verificaron en vez de suponerse: `foreign_keys = ON` se activa en `onOpen`
(`AppModule.kt:100` ShinKu, `:77` AniZen), que corre **después** de las migraciones — por eso el
`133.sqm` de AniZen con `REFERENCES` + `DEFAULT 1` funciona y **no** es un fallo de producción, y por eso
mi `43.sqm` añade la columna sin `REFERENCES` (funciona en ambos estados del pragma y deja los dos
esquemas idénticos). Y `logcat` se publica como AAR, no JAR.
