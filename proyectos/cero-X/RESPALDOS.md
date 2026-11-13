# cero-X · respaldos externos

El repo remoto es `github.com/Alex17273747576777/cero-X-app` (**público**). El
historial local del sandbox **diverge** del remoto y no se ha fusionado:

| | commit | qué es |
|---|---|---|
| remoto `main` | `1fdad3595de1378fa745f70112d6d8e65152dfec` | 4 commits que el sandbox no tenía: catálogo Nox y Kisara, asistente IA, VM Android, buscador web |
| remoto `fases-verificadas-2026-11-13` | `c7191bf76befba17937c6e75820aef88cf4bf847` | los 19 commits del sandbox, empujados el 2026-11-13 |
| remoto `icono-y-auditoria` | `85e986489fc60bc7d92691d5b772aaa10ca424b0` | rama previa, sin tocar |
| base común | `0aaad47768ef` | punto de la divergencia |

Se empujó a **rama nueva y no a `main`** a propósito: `git merge-base --is-ancestor`
dijo que `origin/main` no es ancestro del HEAD local, o sea que un force-push habría
borrado esos 4 commits remotos. De los 57 ficheros que tocan, 49 ya son idénticos en el
árbol local, 8 difieren y ninguno falta; la divergencia total son 161 ficheros, 10.411
inserciones y 1.445 borrados. Los 8 que hay que mirar al fusionar:

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

Fusionar no es un `merge` y ya: produce código nuevo que hay que volver a cerrar con
suite completa y los dos APK, y tres de esos ficheros los tocó el proyecto entero
(`MainActivity.kt` son 312 líneas de diferencia).

GitHub reportó al empujar: **3 vulnerabilidades de Dependabot en la rama por defecto,
1 alta, 1 moderada y 1 baja** → `/security/dependabot`.

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
