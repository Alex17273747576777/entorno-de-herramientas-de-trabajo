# Ficha de auditoría — AniZen

Ruta auditada: `/var/tmp/referencias/AniZen`

## Eje 1 — manifiesto

- manifiestos: 15
- permisos distintos: 21
- componentes: 25 (5 exportados)
- sensibles (13): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, SCHEDULE_EXACT_ALARM, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 1284
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, SCHEDULE_EXACT_ALARM, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): RECEIVE_BOOT_COMPLETED, WAKE_LOCK
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, USE_EXACT_ALARM

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 84
- de su propia infraestructura: square.github.io, gist.github.com, coil-kt.github.io, gitlab, gitlab.com

| host | menciones |
|---|---:|
| `aniyomi.org` | 11 |
| `issuetracker.google.com` | 9 |
| `www.themoviedb.org` | 9 |
| `trakt.tv` | 6 |
| `graphql.anilist.co` | 4 |
| `kitsu.app` | 4 |
| `anilist.co` | 4 |
| `myanimelist.net` | 4 |
| `mysite.com` | 3 |
| `api.deepseek.com` | 3 |
| `opencode.ai` | 3 |
| `api.literouter.com` | 3 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 34
- **SDK que entran en el APK**: firebase-analytics, firebase-crashlytics, google-services
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): firebase-analytics, firebase-crashlytics, google-services

| SDK | qué es | dónde |
|---|---|---|
| `firebase-analytics` | analítica de Google | `gradle/libs.versions.toml:85` |
| `firebase-analytics` | analítica de Google | `telemetry/build.gradle.kts:26` |
| `firebase-crashlytics` | reporte de fallos de Google | `app/build.gradle.kts:20` |
| `firebase-crashlytics` | reporte de fallos de Google | `build.gradle.kts:11` |
| `firebase-crashlytics` | reporte de fallos de Google | `gradle/libs.versions.toml:86` |
| `firebase-crashlytics` | reporte de fallos de Google | `telemetry/build.gradle.kts:27` |
| `google-services` | plugin que cablea los servicios de Google | `app/build.gradle.kts:17` |
| `google-services` | plugin que cablea los servicios de Google | `gradle/libs.versions.toml:120` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
