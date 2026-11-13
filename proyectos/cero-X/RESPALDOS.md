# cero-X · respaldos externos

*Corte 2026-11-13. La cabecera y la tabla de Drive reflejan el estado tras la fusión y el
empuje a `main` (HEAD `2dc023e`); el bloque marcado como histórico debajo conserva el
detalle de la divergencia previa a la fusión.*

El repo remoto es `github.com/Alex17273747576777/cero-X-app` (**público**). La
divergencia **se fusionó y se empujó a `main` el 2026-11-13**: el dueño lo autorizó
(«Fusionalo»), el PR #7 pasó de `mergeable=false`/`dirty` a `merged=True` tras un
fast-forward por push, y `main` avanzó de `52619ef` a **`2dc023e`** con el entorno de
paralelismo y caché medido. La fusión original fue en `7bbc2ae` (dos padres: `57538ab` de
la rama y `1fdad35` de `main`), con los cinco conflictos resueltos leyendo las dos
versiones y un cierre completo de 88 suites, 614 pruebas, 0 fallos y 14 omitidas más los
dos APK. El verde del HEAD empujado se confirmó por SHA en la API de Actions: corrida
`43437675315` sobre `2dc023e`, `completed`/`success`.

> **Lo que sigue debajo de esta línea es el detalle histórico de la divergencia tal como
> estaba antes de fusionarse**, conservado porque explica por qué la fusión se hizo leyendo
> las dos versiones y no con un `merge` a ciegas. Los tiempos verbales en presente («el PR
> no es fusionable», «`main` sigue sin tocarse») describen el estado de *antes* del
> 2026-11-13, no el actual. Así estaba antes de eso:

| | commit | qué es |
|---|---|---|
| remoto `main` | `1fdad3595de1378fa745f70112d6d8e65152dfec` | 4 commits que el sandbox no tenía: catálogo Nox y Kisara, asistente IA, VM Android, buscador web |
| remoto `fases-verificadas-2026-11-13` | `c7191bf76befba17937c6e75820aef88cf4bf847` | los 19 commits del sandbox, empujados el 2026-11-13 |
| remoto `icono-y-auditoria` | `85e986489fc60bc7d92691d5b772aaa10ca424b0` | rama previa, sin tocar |
| base común | `0aaad47768ef` | punto de la divergencia |

Se empujó a **rama nueva y no a `main`** a propósito: `git merge-base --is-ancestor`
dijo que `origin/main` no es ancestro del HEAD local, o sea que un force-push habría
borrado esos 4 commits remotos. De los 57 ficheros que tocan, 49 ya son idénticos en el
árbol local, 8 difieren y ninguno falta.

**Cifra corregida.** La divergencia se anotó primero como «161 ficheros, 10.411
inserciones, 1.445 borrados», que sale de `git diff origin/main HEAD`: dos puntos, o sea
que **mezcla lo que hizo la rama con lo que avanzó `main`** y subestima el trabajo de la
rama. Lo que ve un PR es la comparación desde la base común, tres puntos:

```text
git diff --stat origin/main...HEAD
  210 files changed, 12886 insertions(+), 1853 deletions(-)
```

**Y la rama no es fusionable tal cual.** Quedó como [PR #7](https://github.com/Alex17273747576777/cero-X-app/pull/7),
abierto y sin fusionar. La API responde `mergeable=false`, `mergeable_state=dirty`,
`rebaseable=false`, y `git merge-tree --write-tree origin/main HEAD` sale 1 con **cinco
conflictos**, medidos sin tocar el árbol. Dos son `add/add`: `main` y la rama crearon
esos ficheros **por separado**, cada una con su versión, o sea que no es un conflicto de
líneas sino dos implementaciones paralelas del mismo módulo. Los 8 ficheros que difieren:

```text
android/app/build.gradle                                                  +31 -11
android/app/src/main/AndroidManifest.xml                                  +15  -0
android/app/src/main/java/com/ceroX/app/core/CeroXApplication.kt          +15  -0
.../modules/extension_sandbox/InstaladorProjectNox.kt                     +21 -15
.../ui/extensiones/IntegracionesActivity.kt                               +84 -17
android/app/src/main/java/com/ceroX/app/ui/ia/PantallaIa.kt                +6  -0
android/app/src/main/java/com/ceroX/app/ui/main/MainActivity.kt          +158 -154
android/app/src/test/java/com/ceroX/app/ui/estado/NavegacionTest.kt        +7  -2
```

De esos 8, **cinco son conflicto** y tres fusionan solos (`build.gradle`,
`CeroXApplication.kt`, `PantallaIa.kt`):

| fichero | tipo de conflicto | `main` desde la base | rama desde la base |
|---|---|---|---|
| `android/app/src/main/AndroidManifest.xml` | content | +15 −2 | +30 −2 |
| `…/modules/extension_sandbox/InstaladorProjectNox.kt` | **add/add** | +65 −0 | +71 −0 |
| `…/ui/extensiones/IntegracionesActivity.kt` | **add/add** | +270 −0 | +337 −0 |
| `…/ui/main/MainActivity.kt` | content | +17 −0 | +163 −142 |
| `…/src/test/java/com/ceroX/app/ui/estado/NavegacionTest.kt` | content | +25 −0 | +30 −0 |

Fusionar no es un `merge` y ya: produce código nuevo que hay que volver a cerrar con
suite completa y los dos APK.

## El PR sí dispara CI: la nota anterior era una medición prematura

Esta sección decía que en todo el historial del repo había **0 corridas con
`event=pull_request`** y que la causa no se encontraba. Medido de nuevo con
`/actions/runs?event=pull_request`, hay dos, y las dos son posteriores a esa nota:

| corrida | commit | creada | resultado |
|---|---|---|---|
| `43415076063` | `7bbc2ae` | 11:11:39Z, unos 84 s después del push | success |
| `43418068714` | `e960c81` | 11:33:52Z, unos 19 s después del push | success |

El error fue medir un sistema asíncrono una sola vez, segundos después de provocar el
evento, y escribir la ausencia observada como propiedad permanente del repositorio: quien
leyera el doc no comprobaba el disparador por PR y se quedaba sin esa verificación. Lo que
sigue sin explicarse, y se deja dicho en vez de taparlo: el push de `57538ab` a las 10:45Z
**no** produjo corrida `pull_request` y los dos siguientes sí.

Consecuencia práctica, que no cambia: la verificación se mira explícitamente con
`/actions/runs?head_sha=<sha>` y se lanza también con `workflow_dispatch` **sobre el HEAD
del momento** — la primera corrida verde cubría `8bf0747` y no los commits de docs que
vinieron después, así que se volvió a disparar sobre `57538ab`.

**Dependabot, diagnosticado el 2026-11-13.** Las 3 alertas (alta `GHSA-5c6j-r48x-rmvq`
por RCE, moderada `GHSA-qj8w-gfj5-8c6v` por DoS, baja `GHSA-m5mm-p8h7-m29v` por XSS) son
todas de `serialize-javascript` 6.0.2 en `comun/kotlin-js-store/yarn.lock`, arrastrado por
`mocha@10.7.0` del target `js(IR) { nodejs() }`. Los tres parches exigen `>= 7.1.3`, un
salto mayor que el `^6.0.2` de mocha no permite, y forzarlo rompería el target JS sin poder
verificarlo en el sandbox (`comun/build` no existe, `yarn` no está instalado). Se midió que
no alcanza al producto: la app consume `comun/` por fuentes, el APK lleva **0 ficheros
`.js`** y ningún workflow compila el target. Sigue abierto en GitHub, con criterio de salida
en `docs/PENDIENTES-EXTERNOS.md` del repo y una guarda (`CadenaDeSuministroJsTest`) para que
la conclusión no caduque en silencio.

## Copias en Google Drive

Además del remoto Git hay tres tarballs con `work/` entero (repo con `.git`, evidencia
de `work/ci`, `work/auditoria-apks`), en la carpeta «cero-X — respaldos»
(id `1MTFiK3m6_CbBsWuklewEdW3azRAgKZpg`). Los tres con restauración probada antes de
subir y `md5Checksum` devuelto por Google coincidiendo con el local.

| fecha UTC | head | bytes | md5 | id en Drive |
|---|---|---:|---|---|
| 2026-11-13T09:52:33Z | `cd18457` | 8.963.823 | `db264bdad023132dd8fbcc8696816909` | `1fd1856Yydk-Q-AXOmsP90hMEtbu7zF79` |
| 2026-11-13T09:57:34Z | `d85c0bd` | 8.990.675 | `0a329b63af148966664f8e42f6336e1a` | `1qNAlhuCjbClSl6_otA1h0lJq1YevEf1A` |
| 2026-11-13T10:07:44Z | `7bfde2c` | 9.034.304 | `4da1e2e1a18e178b1b0c02a7a95f91aa` | `1NdZcqtIq6Mip85AJhAKHXfGkgUhp3MZ8` |

Ninguno contiene `/home/user/.cerox-keys/tokens.txt`. Con el remoto Git ya configurado
estos tarballs pasan a ser redundantes para el código y siguen valiendo para `work/ci`,
que no está en ningún repo.

## Autenticación sin escribir el token en ningún sitio

`docs/POLITICA-DE-ALMACENAMIENTO.md` describe un helper en `/home/user/.gh-credential`
que lee `/home/user/.gh-token`. En este sandbox el token vive en
`/home/user/.cerox-keys/tokens.txt` (modo 0600, cuatro claves `GP_EXPLORA_1..3` y `GP`),
así que el helper se creó leyendo de ahí en vez de duplicar el secreto a un segundo
archivo:

```sh
#!/bin/sh
case "$1" in
  get) printf 'username=x-access-token\npassword=%s\n' \
         "$(grep -E '^GP=' /home/user/.cerox-keys/tokens.txt | head -1 | cut -d= -f2- | tr -d '\r\n')" ;;
esac
```

```bash
git config credential.helper /home/user/.gh-credential   # por repo, no --global
git remote add origin https://github.com/Alex17273747576777/cero-X-app.git
git remote -v    # la URL sale limpia: ningún token embebido
```
