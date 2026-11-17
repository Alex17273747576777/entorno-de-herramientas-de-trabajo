# Ficha de auditoría — >>> cero-X-app

Ruta auditada: `/home/user/work/cero-X-app/android/app/src/main`

## Eje 1 — manifiesto

- manifiestos: 1
- permisos distintos: 21
- componentes: 16 (3 exportados)
- sensibles (13): ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, FOREGROUND_SERVICE, INTERNET, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, REQUEST_INSTALL_PACKAGES, VIBRATE, WAKE_LOCK, WRITE_EXTERNAL_STORAGE

## Eje 2 — APIs usadas frente a permisos declarados

- fuentes analizadas: 244
- permisos ejercidos en código: INTERNET, REQUEST_INSTALL_PACKAGES, WRITE_EXTERNAL_STORAGE
- ejercidos sólo en recursos XML (no en código): ninguno
- **permisos huérfanos** (declarados, sin uso detectado): ACCESS_WIFI_STATE, FOREGROUND_SERVICE, POST_NOTIFICATIONS, QUERY_ALL_PACKAGES, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, WAKE_LOCK
- **usos sin permiso declarado**: REQUEST_DELETE_PACKAGES

Que no aparezca la cadena no prueba que el permiso sobre: puede ejercerlo una
dependencia o un recurso XML. Y al revés: un uso sin declarar puede venir de un
manifiesto fusionado de otra biblioteca. Ambos se confirman leyendo, no grepando.

## Eje 3 — endpoints

- hosts distintos fuera del ruido: 49
- de su propia infraestructura: anikku-app.github.io, hitarth-gg.github.io

| host | menciones |
|---|---:|
| `everythingmoe.com` | 8 |
| `anipirate.xyz` | 7 |
| `miyomi.app` | 6 |
| `justindex.cc` | 5 |
| `fmhy.net` | 4 |
| `wotaku.wiki` | 3 |
| `search.brave.com` | 3 |
| `api.openai.com` | 2 |
| `codeberg.org` | 2 |
| `duckduckgo.com` | 2 |
| `mangadex.org` | 2 |
| `nhentai.net` | 2 |

## Eje 4 — telemetría en dependencias

- ficheros de build analizados: 5
- **SDK que entran en el APK**: ninguno
- sólo declarados en el catálogo de versiones (no entran): ninguno
- aplicados dentro de un condicional (hay variante sin ellos): ninguno


Cero coincidencias **no** prueba ausencia: un SDK puede llegar transitivo sin
dejar su nombre en un fichero de build. Probarlo exige el árbol de dependencias
resuelto, que sólo existe si el proyecto compila.
