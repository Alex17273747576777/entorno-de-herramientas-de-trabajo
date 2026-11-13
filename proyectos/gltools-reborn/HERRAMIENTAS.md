# gltools-reborn · herramientas

Fuente canónica: [`gltools-reborn`](https://github.com/Alex17273747576777/gltools-reborn)
rama `main` @ `4389482dd4e7` (medido el 2026-11-13; 173 ficheros, Kotlin, **Apache-2.0**,
9.942 KB). Copiadas de `.github/scripts/`. Ver `proyectos/LICENCIAS.md`.

## Cómo se comprueba que no derivaron

```bash
./proyectos/comprobar-copias.sh    # COPIAS_OK · COPIAS_DERIVADAS (sale 1) · COPIAS_SIN_MANIFIESTO (sale 2)
```

Los hashes viven en `herramientas/MANIFIESTO.sha256` y los genera `sha256sum`, no se
transcriben a mano.

| fichero | bytes | sha256 | qué hace |
|---|---:|---|---|
| `LICENSE-de-origen.txt` | 11,358 | `cfc7749b96f63bd3` | Apache-2.0 de la fuente, conservado porque Apache-2.0 pide atribución |
| `auditar_releases.py` | 6,820 | `ac78f15cefcfb3a3` | auditoría de APK publicados, sólo en Actions: descarga a temporales del runner, verifica con `apksigner` oficial, sha256 y compara sumas publicadas. Nunca escribe tokens ni los pone en URLs |
| `censo_apk.py` | 4,223 | `1495dad819d07db7` | censo del APK: qué arquitecturas lleva dentro y cómo va empaquetado. Nació de una promesa («universal, todo comprimido») que medida sobre la 1.16.0 publicada no era cierta |
| `preparar_firma.py` | 4,770 | `f897bc6c2fb378d9` | lee un JSON o cuatro secrets y prepara el keystore. Nunca registra valores ni genera claves |
| `test_censo_apk.py` | 4,229 | `b396f2536b6175a2` | las comprobaciones de `censo_apk.py`. 7 comprobaciones |
| `test_preparar_firma.py` | 2,866 | `25d58b738e6c9969` | las comprobaciones de `preparar_firma.py`. 15 tests |
| `verificar_version.py` | 5,037 | `c442e0cfd6658b36` | verificación fail-closed en Actions: la versión se lee de `build.gradle`, no se escribe a mano; el certificado esperado va fijado por sha256 |

## Cómo se ejecutan sus tests (y la trampa)

```bash
python3 -B proyectos/gltools-reborn/herramientas/test_censo_apk.py       # 7 comprobaciones, todas en verde
python3 -B proyectos/gltools-reborn/herramientas/test_preparar_firma.py  # Ran 15 tests … OK
```

**No con `pytest`.** `pytest -q test_censo_apk.py` da «no tests ran» y exit 5, porque el
fichero no tiene funciones `test_*`: es un script de asertos. Parece un fallo y no lo es.
Así lo invoca su CI original, en `version.yml:32-34`.

## Lo que estas herramientas necesitan del entorno

Leen del entorno, no de ficheros: `GITHUB_TOKEN`, `GITHUB_REPOSITORY`, `GITHUB_SHA`,
`GITHUB_ENV`, `GITHUB_OUTPUT`, `GITHUB_STEP_SUMMARY`, `ANDROID_HOME` o
`ANDROID_SDK_ROOT`, y para la firma `REBORN_KEYSTORE_BASE64`, `REBORN_STORE_PASS`,
`REBORN_KEY_ALIAS`, `REBORN_KEY_PASS`, más `FIRMADO` y `PUBLICAR`.

Las copias **no contienen ningún valor** de ésos (barrido antes de subir: 0 coincidencias
de `github_pat_`, `ghp_`, `AKIA` y clave privada PEM en todo `proyectos/`). Aun así: no
ejecutarlas con secrets reales en un entorno que registre la salida, y nunca pasar el
token por una URL.
