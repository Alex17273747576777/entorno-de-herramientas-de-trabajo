# Auditoría viva del perfil y los nueve repositorios

**Estado: parcial; no es una auditoría integral de seguridad ni una lectura línea por línea de todos los árboles.** Se fija la revisión a hashes de ramas obtenidos de GitHub REST, no a una clonación antigua. La tarea sólo se dará por terminada después de revisar los hallazgos aún abiertos y completar el examen de contenido que falta.

## Corte, alcance y límites

- Se consultaron el perfil y el inventario de repositorios del API de GitHub; para los repositorios relevantes se leyeron ramas, árboles recursivos, README, issues/comentarios, PR/revisiones, runs de Actions, releases y metadatos de sus assets. Se descargaron por API algunos ficheros de texto y pequeños manifiestos de verificación para cotejarlos; no se descargaron APK grandes.
- La plataforma fija **2026-11-10** como fecha local; varias respuestas vivas del API llevan marcas `updated_at`/`created_at` hasta **2026-11-19**. Se conservan los hashes y las marcas tal como llegaron, pero no se presenta el reloj del host ni esas marcas futuras como fecha local de corte.
- Las pruebas verdes no equivalen a aceptación funcional. No hubo dispositivo Android conectado, emulador ni validación física; no se comprobó criptográficamente el certificado de los APK descargando y analizando los APK. No se revisaron todas las ~3.000 entradas de AniZen/ShinKu ni todos los ~19.000 elementos de La Bandita. La revisión de código fue dirigida a riesgos y hallazgos concretos.
- El árbol local de `/home/user/work/edt` se actualizó con `git fetch --prune origin`; `HEAD`, `origin/main` y `origin/HEAD` coincidían en `ade1b8ec0d732db102db81a258dffed411bfe76e` y no había cambios previos.

## Perfil e inventario

El API devolvió **9 repositorios públicos propios**, **0 gists**, **5 seguidores** y **194 seguidos**. No existe un repositorio público `Alex17273747576777/Alex17273747576777` para README de perfil. No se reproduce aquí la bio personal. Hay tres forks (`anime-extensoes`, `AniZen`, `ShinKu`) y seis repositorios propios no-fork.

| Repositorio | Rama predeterminada | HEAD del fork/propio | Entradas del árbol remoto* | Estado de issues/Actions/release |
|---|---|---|---:|---|
| [anime-extensoes](https://github.com/Alex17273747576777/anime-extensoes) | `repo` | `51bb0521189d2a1bc678bf16d522e6a09d814f83` | 553 | Issues deshabilitados; sin Actions ni releases en el fork |
| [AniZen](https://github.com/Alex17273747576777/AniZen) | `master` | `95160a724d1147777dd1f7997fff4885a4cd9deb` | 3.054 | Issues deshabilitados; sin Actions ni releases en el fork |
| [ShinKu](https://github.com/Alex17273747576777/ShinKu) | `main` | `043ab7d8e68e8a77752805c34969a2477195826a` | 2.936 | Issues deshabilitados; sin Actions ni releases en el fork |
| [normas-de-diseno](https://github.com/Alex17273747576777/normas-de-diseno) | `main` | `bd9af9a47913d027bbdc2cc2316fc3544398e37e` | 63 | 3 issues cerrados; Actions reciente verde; `v1.0.0` |
| [entorno-de-herramientas-de-trabajo](https://github.com/Alex17273747576777/entorno-de-herramientas-de-trabajo) | `main` | `ade1b8ec0d732db102db81a258dffed411bfe76e` | 323 | Sin issues/PR/release; Actions reciente verde |
| [cero-X-app](https://github.com/Alex17273747576777/cero-X-app) | `main` | `855547210c65dca1de00c2669396c8f1c84380d0` | 804 | Issue genuino #6 abierto; PR #7 fusionado; releases beta |
| [gltools-reborn](https://github.com/Alex17273747576777/gltools-reborn) | `main` | `feb464873253df55789d46cc55d5c8825e92e4dc` | 212 | #1/#2/#3/#5/#6/#8 abiertos; #4/#7 cerrados; `v1.16.1` |
| [la-bandita-archivo](https://github.com/Alex17273747576777/la-bandita-archivo) | `main` | `ac259ae55255e20a02ba38689ddd2b947aded29f` | 19.005 | #2/#3 abiertos; Actions reciente verde |
| [bandwidth-hero-proxy2](https://github.com/Alex17273747576777/bandwidth-hero-proxy2) | `main` | `a391df66ba4b9e6219e782b82ac2332afc9645ed` | 26 | PRs de Dependabot #1/#3/#4 abiertos; sin issues de producto |

\* El conteo del árbol incluye directorios, además de archivos; no es un recuento de ficheros fuente.

## Diferencias vivas entre los forks y sus upstreams

| Fork | Upstream consultado | Comparación de rama predeterminada | Diferencia útil para decidir; no se sincronizó automáticamente |
|---|---|---|---|
| `anime-extensoes/repo` | [`ProjectNox-org/anime-extensoes`](https://github.com/ProjectNox-org/anime-extensoes) `repo` = `ff1868d951de5e7cfa5aedc9d0b2f89b854dff7d` | Fork **15 commits detrás, 0 delante** | El fork tiene 272 APK e iconos y `repo.json` sin `index_v2`; el upstream tiene 273 de cada uno, anuncia `index_v2` y versiona `index.pb` (17.857 B). El fork no debe presentarse como espejo actual del catálogo. No se decodificó aquí el esquema del `index.pb` actual del upstream. |
| `AniZen/master` | [`salmanbappi/AniZen`](https://github.com/salmanbappi/AniZen) `master` = `95160a724d1147777dd1f7997fff4885a4cd9deb` | **Idénticos** | Las ramas propias `feed-cap-per-tab` y `merge-groups-phase1` tienen 2 commits cada una sobre `master`; no hay PR ni CI en el fork. Son trabajo parcial relacionado con #94/#95, no código ya integrado. |
| `ShinKu/main` | [`Harrys-HQ/ShinKu`](https://github.com/Harrys-HQ/ShinKu) `main` = `a478592cb040e644f0e222d1fec9b20feba9ff18` | Fork **14 commits detrás, 0 delante** | Las ramas `merge-groups-phase1`, `feed-cap-at-insert` y `feed-cap-i18n` están superadas por los PR #34/#36/#37 fusionados upstream. El default del fork todavía no recibe los cambios más recientes ni los APK de upstream. |

### Anime: cierre correcto de la propuesta incompatible

El PR del fork [ProjectNox #3](https://github.com/ProjectNox-org/anime-extensoes/pull/3) está **cerrado sin fusionar**, con la explicación documentada: su `index.pb` final usaba `Extension.sources=8` y `Source.message=7`; el esquema oficial Aniyomi requiere `sources=9` y `Source.message=6`. Por eso el cliente habría interpretado incorrectamente las fuentes. El mantenedor de Awerkori integró una versión corregida en [anime-fonte-extensoes #9](https://github.com/Awerkori/anime-fonte-extensoes/pull/9), que declara el esquema oficial y pruebas de catálogo. El `index.pb` vivo de ProjectNox existe ahora, pero este barrido no confirma que su esquema sea intercambiable con el oficial de Aniyomi. No reutilizar el binario rechazado ni afirmar paridad sin decodificarlo.

### AniZen: upstream y propuestas abiertas

- Las incidencias de producto propuestas por Alex en [#12](https://github.com/salmanbappi/AniZen/issues/12), [#94](https://github.com/salmanbappi/AniZen/issues/94) y [#95](https://github.com/salmanbappi/AniZen/issues/95) siguen abiertas, sin comentarios de respuesta. #94 describe feed y límite de fuentes; el branch `feed-cap-per-tab` sólo trae el límite y pruebas, no todo el rediseño planteado. #95 describe grupos deduplicados/perfilado; `merge-groups-phase1` sólo entrega tablas, migración y helper de deduplicación. Ambas ramas carecen de evidencia de CI y no se abrió PR.
- El upstream conserva abierta [#78, “[CRITICAL] Critical leaks & UI freezes”](https://github.com/salmanbappi/AniZen/issues/78), con 0 comentarios y una lista amplia de riesgos. Un cotejo puntual en `master` encontró al menos dos afirmaciones que ya no coinciden con el código actual: `ExtensionInstaller` cierra la respuesta con `execute().use`, y `SettingsDiscordScreen` no contiene `runBlocking`. `DownloadStore` sí conserva un `runBlocking`. No se auditó cada punto: la incidencia debe volver a comprobarse por archivo/commit antes de tratar toda la lista como vigente o cerrada.
- El upstream tiene PRs abiertos de terceros #88/#89/#90: #88 se declara presentación visual “no need to merge”; #89 y #90 están en conflicto (`mergeable=false/dirty`), sin revisiones ni check-runs visibles. No se recomienda tratar ninguno como listo para integrar.
- Pendiente de divulgación coordinada: se detectó una posible exposición de material de firma de release en el upstream. Los detalles no se copian a este registro público y no se abre un issue público; hace falta notificar privadamente al mantenedor y confirmar si es clave de producción. No se extrajo ni publicó el material.
- El último release estable observado es `v0.5.220` (5 APK para arquitecturas). Los últimos runs de `Preview Build` y `Apply Spotless` que devolvió el API fueron exitosos en la rama `preview`, no prueban los PRs abiertos.

### ShinKu: avances integrados y evidencia de build

- [#34](https://github.com/Harrys-HQ/ShinKu/pull/34) añadió el esquema inicial de grupos persistentes/deduplicación; la conversación de [#33](https://github.com/Harrys-HQ/ShinKu/issues/33) dice que las fases posteriores se implementaron y cerró con `v2.8.3`.
- [#36](https://github.com/Harrys-HQ/ShinKu/pull/36) aplicó el límite de 25 en la escritura y añadió pruebas. [#37](https://github.com/Harrys-HQ/ShinKu/pull/37) parametrizó la cifra en 16 locales para que 15 traducciones no siguieran diciendo 10. Los tres PR de Alex (#34/#36/#37) figuran fusionados.
- Importante: el check **Build app** falló en los runs de los tres PR; las etiquetas/controles secundarios que aparecen verdes no vuelven verde el build. Los logs detallados devolvieron HTTP 401 desde el endpoint de Actions, así que no se atribuye una causa. El mantenedor fusionó los cambios; el API muestra `v2.8.4` estable después de #37, pero no se afirma que los check-runs fallidos hayan pasado.
- La única issue abierta observada en el upstream es [#39](https://github.com/Harrys-HQ/ShinKu/issues/39) sobre chips de búsquedas guardadas. El mantenedor publicó `v2.8.5-preview.1`; quien reportó confirmó que el preview funciona, y la issue sigue abierta hasta la versión estable. El fork no incluye ese avance por sus 14 commits de desfase.

## Hallazgos abiertos en repositorios propios

### `cero-X-app`

- La [issue #6](https://github.com/Alex17273747576777/cero-X-app/issues/6) sigue abierta. Se mantienen pendientes la clave de publicación legítima/canal seguro, migración de usuarios, catálogo autenticado y consentimiento de certificados, prueba positiva con extensión auténtica, pruebas de manipulación, instalación/lector/navegación/IA en dispositivos, revisión de módulos incompletos y cualquier promesa de aislamiento por proceso/UID. La corrección de `serialize-javascript` sí está ejecutada en `855547210c`; el run `dependencias-js` de ese SHA fue exitoso. Ese CI no cierra los criterios de firma ni los de dispositivo.
- El release que el API devuelve como “latest” es `v1.0.8-beta-fuentes-verificadas`, con dos APK y dos ficheros de sumas. Aunque el nombre incluye `beta`, GitHub informa `prerelease=false`; revisar si esa etiqueta de distribución es intencional. Las líneas de SHA-256 y los digests de GitHub para esos assets coinciden, pero eso no identifica por sí solo el certificado de firma.
- El tag `v1.0.8-beta-fuentes-verificadas` está **53 commits** detrás de `main` (`8555472…`). No atribuir al APK público cada cambio que hoy está en la rama.

### `gltools-reborn`

- Siguen abiertas #1 (superposición sobre un juego y que deje pasar toques), #2 (revisión táctil de cinco pantallas), #3 (un parte de cierre real), #5 (seis capturas reales en vez de compuestas), #6 (capturas de Configurar/Rendimiento/Pantalla/Datos) y #8 (ROM, Shizuku, restauración y firma en dispositivo). #6 ya tiene contraste tonal medido y corrección del texto tenue, pero no sus capturas de cierre; #8 acumula compilación/pruebas y releases, no prueba física.
- El último run de pruebas en `main` (`44201498448`, commit `feb4648…`) es verde; hubo cuatro fallos anteriores en commits de esa misma ronda. La release pública `v1.16.1` apunta a `4389482…`, **5 commits** detrás del `main` actual.
- Se descargaron sólo `SHA256SUMS.txt` y `verificacion.json`: sus digests coinciden con GitHub y las sumas listadas coinciden con los digests de los APK. El JSON declara `firmado=true` y commit `4389482…`; no descargué ni inspeccioné los APK, por lo que esto verifica coherencia del manifiesto/sumas, no el certificado de los binarios. La aceptación física sigue bloqueada.

### `la-bandita-archivo`

- [#2](https://github.com/Alex17273747576777/la-bandita-archivo/issues/2) se confirma en el `main` vivo: `registry/registro.db` pesa **7.348.224 bytes** y no aparece en el manifiesto SHA-256 de 14.364 líneas. El run verde de `vara` verifica lo que el sello incluye; no prueba el contenido de esa base de datos ni sustituye el hash del volcado propuesto en el issue.
- [#3](https://github.com/Alex17273747576777/la-bandita-archivo/issues/3) también se confirma: `tools/medir_piezas_24_34.py` promete en el docstring dejar el SHA-256 del payload en el JSON, pero el cache guarda URL/código/cuerpo y el hash del fichero final se imprime; no se añade al documento de medición. La issue deja elegir corregir el docstring o cambiar sólo las mediciones futuras, preservando las ya selladas.

### `normas-de-diseno` y `entorno-de-herramientas-de-trabajo`

- `normas-de-diseno`: las tres issues están cerradas (#3 duplicada); la última ejecución `procedimientos` fue exitosa, tras varios fallos anteriores de esa serie; `v1.0.0` contiene un asset de censo gzip. Esto no completa la aceptación semántica de §9.9 del manual en `/home/user/work/edt`.
- `entorno-de-herramientas-de-trabajo`: el run más reciente visible en `ade1b8e` fue exitoso. No se encontraron issues/PR/releases. La búsqueda textual de “40 minutos” en el árbol local sólo encontró la bitácora de ronda, no una regla normativa fuente; localizar la regla exacta sigue abierto.

### `bandwidth-hero-proxy2`: PRs de Dependabot revisados

- El `main` vivo usa Node `>=22`, `node-fetch@2.7.0`, `sharp@0.35.5` y `jest@30.5.2`; tests/CodeQL recientes en `main` están verdes. El código `functions/index.js` es CommonJS y hace `require("node-fetch")`. El test sustituye `node-fetch` por una función simulada.
- #1 propone `sharp@0.34.5` y #3 `jest@30.3.0`; ambos están `mergeable=false/dirty` y son versiones menores que las ya fijadas en `main`. #2 de Jest está cerrado como reemplazado por #3.
- #4 propone `node-fetch@3.3.2`; en el check-run aparecen Tests y CodeQL exitosos y el PR está limpio. Aun así, se comprobó el comportamiento real en Node **v22.23.5**: `require("node-fetch")` devuelve un objeto namespace (`default` es la función), y llamarlo como hace el endpoint produce `TypeError: fetch is not a function`. El mock del test explica el falso verde para esa frontera de carga.
- Se dejó un comentario técnico reproducible en [PR #4](https://github.com/Alex17273747576777/bandwidth-hero-proxy2/pull/4#issuecomment-7021954302), recomendando no fusionar hasta mantener una versión CommonJS compatible o migrar la importación y agregar una prueba sin mock. **No se fusionó ningún PR.** El código actual sí muestra controles útiles que se revisaron: allowlist exacta de hosts, DNS no unicast rechazado, redirecciones manuales, autenticación, límite de respuesta y pruebas de SSRF.

## Acciones y pendientes de esta auditoría

1. No sincronizar las tres ramas por reflejo. Revisar antes el upstream, el esquema Protobuf correcto y las migraciones; el fork AniZen ya coincide, los otros dos tienen desfase cuantificado.
2. Esperar respuesta o corrección a la nota de PR #4; verificar el test contra el módulo real antes de considerar ese bump.
3. Volver a revisar por UI los logs fallidos de `Build app` de ShinKu #34/#36/#37; no se obtuvo evidencia suficiente por API para explicar el fallo.
4. Resolver con criterios explícitos las issues #6 de cero-X, #1/#2/#3/#5/#6/#8 de GLTools y #2/#3 de La Bandita. No cerrarlas por CI verde.
5. Tratar privadamente el hallazgo de firma de AniZen; no publicar un issue con detalle sensible antes de notificar al mantenedor.
6. Completar lectura dirigida de código/workflows y de los assets pendientes en los repos grandes. Este informe no declara finalizada la auditoría total.
7. Mantener las tareas editoriales independientes: cotejo semántico completo de §9.9; revisión factual de `pieza-01-ES.md`; producción y revisión secuencial de maestros ES/EN 01–70; hallar una fuente exacta para la regla de 40 minutos; esperar la lista del dueño para resolver 15/18 sin inventar lecciones. No se reintentará el issue de ShinKu en el fork con Issues deshabilitados (403 previo).

## Fuentes y crédito

Fuentes primarias: [perfil y repositorios de Alex](https://github.com/Alex17273747576777), API REST de GitHub (refs, trees, issues, pulls, checks, releases y assets), [node-fetch 3.3.2](https://github.com/node-fetch/node-fetch/tree/v3.3.2), y los issues/PR/release enlazados arriba. Se reconoce el trabajo de Alex (autor de los PR de ShinKu y propuestas de AniZen); de ProjectNox-org, salmanbappi y Harrys-HQ como mantenedores de upstream; de Awerkori y contribuidores de `anime-fonte-extensoes` por la integración corregida del índice; de Reikai como referencia citada en la propuesta de grupos; de AzamSaja por el reporte de ShinKu #39; de Dependabot y los autores de cada PR revisado; y de las comunidades de AniZen, Aniyomi y ShinKu. Revisión preparada por un agente de Arena.ai a solicitud del dueño; no suplanta la confirmación de los mantenedores ni de las pruebas en dispositivo.
