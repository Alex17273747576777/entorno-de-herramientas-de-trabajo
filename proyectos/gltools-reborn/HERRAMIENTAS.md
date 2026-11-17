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

## Cómo se prueba el parte de fallos sin emulador (2026-11-17)

`RegistroFallos` toca Android por dos sitios: `Context.filesDir` para escribir y `android.os.Build`
para las cabeceras. Con el `android-stub.jar` **no se puede instanciar `Context`**: el constructor
lanza `RuntimeException: Stub!`, y da igual implementar sus 75 miembros abstractos (se pueden generar
con `javap -p -cp android-stub.jar android.content.Context`, cortando la cláusula `throws` y
cambiando `Outer$Inner` por `Outer.Inner`). El arnés se muere en `Ctx.<init>`.

La salida no es un mock: es **hacer pura la parte que se quiere probar**. `componerParte()` recibe
fecha, contexto, versión, API, modelo, clase, mensaje, pila y `sinMemoria` por parámetro, y no toca ni
el reloj ni el disco ni `android.os.Build`. `guardar()` se queda con lo que sólo se puede hacer en un
teléfono.

```bash
export JAVA_HOME=/var/tmp/jdk/jdk-17.0.13+11; export PATH=$JAVA_HOME/bin:$PATH
/var/tmp/kc-2.1.20/kotlinc/bin/kotlinc -nowarn -cp /var/tmp/jars/android-stub.jar -d /tmp/out \
    app/src/main/java/io/github/labandita/glreborn/RegistroFallos.kt <stub-RegistroErrores> <arnés>
java -Dstdout.encoding=UTF-8 -cp "/tmp/out:<kotlin-stdlib.jar>:/var/tmp/jars/android-stub.jar" ArnesKt
```

Se compila el `RegistroFallos.kt **del repo**, no una copia; el arnés está en
`herramientas/ArnesRegistroFallos.kt`. 13 casos, todos en verde: fotograma correcto en stack mixto,
cabecera que no se cuela cuando la excepción es clase nuestra, `null` con stack sólo de Android y con
pila vacía, `Caused by:` que también cuenta, línea `APP` antes del stack, cabeceras intactas, fallo
normal que no habla de memoria, `OutOfMemoryError` que produce `MEMORIA`+`CONSEJO`, y pila de 9.000
caracteres cortada a 6.000.

Dos trampas medidas al hacerlo:

- El stub de `RegistroErrores` **hay que pasarlo en la misma compilación**. Si se olvida, kotlinc da
  `unresolved reference 'core'` en la línea del `anotar` y, de rebote, `cannot infer type for this
  parameter` en el `runCatching` de dos líneas más arriba: el segundo error es cascada del primero y
  hace mirar en el sitio equivocado.
- `-Dstdout.encoding=UTF-8` (o `-Dfile.encoding`) hace falta para imprimir el parte: sin él, las
  cabeceras `CUÁNDO`/`EXCEPCIÓN` salen mojadas y no se puede comparar texto. Y `javac` sobre un fuente
  con acentos exige `-encoding UTF-8`, que por defecto usa US-ASCII y falla con `unmappable character`.

**Lo que este arnés no cubre, dicho explícitamente:** `guardar()` —la escritura en `filesDir` y la
llamada a `RegistroErrores.anotar`— no se ejecuta en ninguna parte de esta máquina. Se comprueba por
lectura. Y no existe ningún parte real de un teléfono, que es lo que pide la incidencia #3.
