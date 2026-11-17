# Ficha de auditoría — Miyorare

Ruta auditada: `/var/tmp/referencias/Miyorare`

## Eje 1 — manifiesto

- manifiestos: 7
- permisos distintos: 15
- componentes: 74 (21 exportados)
- sensibles (12): ACCESS_NETWORK_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, VIBRATE, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 1626
- permisos ejercidos en código: FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, RECEIVE_BOOT_COMPLETED, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): ninguno
- **usos sin permiso declarado**: READ_MEDIA_IMAGES, READ_MEDIA_VIDEO

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 56
- de su propia infraestructura: token.actions.githubusercontent.com

| host | menciones |
|---|---:|
| `myanimelist.net` | 14 |
| `kitsu.app` | 14 |
| `api.mangabaka.org` | 7 |
| `api.myanimelist.net` | 6 |
| `mangabaka.org` | 5 |
| `graphql.anilist.co` | 5 |
| `www.mangaupdates.com` | 3 |
| `anilist.co` | 3 |
| `v.recipes` | 3 |
| `www.googleapis.com` | 3 |
| `issuetracker.google.com` | 2 |
| `token.actions.githubusercontent.com` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 9
- **SDK que entran en el APK**: acra
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno

| SDK | qué es | dónde |
|---|---|---|
| `acra` | reporte de fallos abierto (ACRA) | `app/src/main/AndroidManifest.xml:1680` |
| `acra` | reporte de fallos abierto (ACRA) | `gradle/libs.versions.toml:58` |

Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
