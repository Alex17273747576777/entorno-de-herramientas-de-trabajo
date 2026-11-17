# Ficha de auditoría — Tadami-Aniyomi-fork

Ruta auditada: `/var/tmp/referencias/Tadami-Aniyomi-fork`

## Eje 1 — manifiesto

- manifiestos: 13
- permisos distintos: 15
- componentes: 29 (7 exportados)
- sensibles (10): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES, WAKE_LOCK

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 3164
- permisos ejercidos en código: ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, MANAGE_EXTERNAL_STORAGE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, REQUEST_DELETE_PACKAGES, REQUEST_INSTALL_PACKAGES
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): WAKE_LOCK
- **usos sin permiso declarado**: CHANGE_WIFI_STATE, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, WRITE_EXTERNAL_STORAGE

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 104
- de su propia infraestructura: square.github.io, gist.github.com, coil-kt.github.io

| host | menciones |
|---|---:|
| `aniyomi.org` | 18 |
| `shikimori.one` | 12 |
| `issuetracker.google.com` | 10 |
| `graphql.anilist.co` | 9 |
| `www.novellist.co` | 9 |
| `api.jikan.moe` | 8 |
| `www.novelupdates.com` | 6 |
| `novel.example.com` | 5 |
| `kitsu.app` | 5 |
| `www.themoviedb.org` | 4 |
| `integrate.api.nvidia.com` | 4 |
| `ollama.com` | 4 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 31
- **SDK que entran en el APK**: ninguno
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno


Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
