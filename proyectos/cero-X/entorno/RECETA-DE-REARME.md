# cero-X · receta de rearme tras un reinicio

En este orden. Saltarse el paso 1 es la causa de casi todos los falsos fallos: sin
toolchain nada compila, y un rojo de entorno se lee como un rojo de código.

```bash
cd /home/user/work/cero-X-app
python3 tools/comprobar_entorno.py          # ENTORNO_OK, o dice qué falta
bash scripts/preparar-entorno-android.sh    # JDK 21, SDK, build-tools, swap
chmod +x android/gradlew scripts/*.sh tools/*.py apk/como-verificar.sh
git config user.name  'Arena Agent'         # .git/config no persiste
git config user.email 'arena-agent@localhost'
source entorno/local.sh                     # JAVA_HOME, ANDROID_HOME, GRADLE_USER_HOME, CEROX_M2_REPO
python3 tools/latido.py --entorno           # HEARTBEAT_OK
```

Y antes de escribir código nuevo, **reproducir la línea base del último commit**: suite
completa y hashes de los dos APK. Si la línea base no da los mismos números, el problema
es del entorno y no de la fase siguiente.

## Dos trampas del rearme

- `swapon` vive en `/usr/sbin` y no está en el PATH del shell: da exit 127. Para
  comprobar el swap, `cat /proc/swaps`, `free -m` y `df -h /`.
- Las cachés de Gradle y Maven van fuera del workspace (`GRADLE_USER_HOME=/opt/cerox/gradle`,
  `CEROX_M2_REPO=/opt/cerox/m2`). Dentro se comen el presupuesto de snapshot: un log de
  Gradle llegó a 49,9 MB y los jars `android-all-instrumented` de Robolectric pesan
  150-213 MB cada uno.

## Al terminar la sesión

```bash
cd android && ./gradlew --stop; cd ..
adb kill-server 2>/dev/null
rm -rf android/.gradle android/app/build android/build
grep -vE '^\s+at ' /tmp/cierre.log | gzip -9 > /home/user/work/ci/<nombre>.log.gz && rm -f /tmp/cierre.log
python3 tools/comprobar_entorno.py && python3 tools/latido.py --entorno
```

Antes de comprimir o renombrar un log, comprobar qué nombres citan `docs/*.md` y
`AGENTS.md`: un barrido ancho con `find … -name '*.log' | gzip` rompió cinco rutas
documentadas que iban sin `.gz`.
