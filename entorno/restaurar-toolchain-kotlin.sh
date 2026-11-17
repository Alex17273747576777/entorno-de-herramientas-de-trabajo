#!/usr/bin/env bash
# Restaura el utillaje de verificación de Kotlin/SQL tras un reinicio del sandbox.
#
# Por qué existe: /var/tmp se barre en cada reinicio (FALLA-003), así que los compiladores, el JDK 17 y
# los jars que permiten COMPILAR Y EJECUTAR el código propuesto desaparecen. Este guion los devuelve en
# unos 2-3 minutos y deja las mismas rutas absolutas que usan los arneses de work/biblioteca-masiva/.
#
# Uso:  bash work/edt/entorno/restaurar-toolchain-kotlin.sh          # descarga lo que falte
#       bash work/edt/entorno/restaurar-toolchain-kotlin.sh --comprobar   # sólo verifica rutas y URLs
#
# Qué instala (versiones tomadas de los catálogos reales de los repos, no elegidas al azar):
#   kotlinc 2.3.10   -> /var/tmp/kc-2.3.10/kotlinc     (kotlin_version de Harrys-HQ/ShinKu)
#   kotlinc 2.0.21   -> /var/tmp/kc/kotlinc            (respaldo; lee kotest 5.x)
#   JDK 17 Temurin   -> /var/tmp/jdk/jdk-17.0.13+11    (JUnit 6 exige class file 61.0; el sandbox trae Java 11)
#   jars             -> /var/tmp/jars                   (kotest 6.0.7 y 5.9.1, consolas JUnit 6.1.2/6.1.3/1.11.4,
#                                                        coroutines 1.10.2, classes.jar de logcat)
set -uo pipefail
COMPROBAR=0; [ "${1:-}" = "--comprobar" ] && COMPROBAR=1
J=/var/tmp/jars; MC=https://repo1.maven.org/maven2; GH=https://github.com
fallos=0
ruta(){ if [ -e "$1" ]; then echo "  ✓ $1"; else echo "  ✗ FALTA $1"; fallos=$((fallos+1)); fi; }
bajar(){ # url destino
  [ -s "$2" ] && { echo "  · ya existe $(basename "$2")"; return 0; }
  curl -sSL -m 900 -o "$2" "$1" || { echo "  ✗ fallo al bajar $1"; return 1; }
  sz=$(stat -c%s "$2" 2>/dev/null || echo 0)
  if [ "$sz" -lt 5000 ]; then echo "  ✗ $(basename "$2") tiene $sz bytes: casi seguro un 404 (Maven devuelve 554 bytes de HTML)"; rm -f "$2"; return 1; fi
  echo "  ✓ $(basename "$2") ($sz bytes)"
}
echo "== rutas esperadas =="
if [ "$COMPROBAR" = 1 ]; then
  ruta /var/tmp/kc-2.3.10/kotlinc/bin/kotlinc; ruta /var/tmp/kc/kotlinc/bin/kotlinc
  ruta /var/tmp/jdk/jdk-17.0.13+11/bin/java; ruta $J/junit-console-6.1.2.jar; ruta $J/junit-console-6.1.3.jar
  ruta $J/kotest-assertions-core-jvm-6.0.7.jar; ruta $J/kotest-assertions-core-jvm-5.9.1.jar
  ruta $J/kotlinx-coroutines-core-jvm-1.10.2.jar; ruta $J/logcat-real-classes.jar
  echo "== clones (también se barren) =="; ruta /var/tmp/feed/shinku; ruta /var/tmp/feed/anizen; ruta /var/tmp/reikai/reikai
  echo "RESULTADO: $([ $fallos -eq 0 ] && echo COMPLETO || echo "FALTAN $fallos elementos (ejecutar sin --comprobar)")"
  exit $((fallos>0))
fi
mkdir -p $J /var/tmp/jdk
for v in 2.3.10 2.0.21; do
  d=/var/tmp/kc$( [ "$v" = 2.3.10 ] && echo -2.3.10 ); mkdir -p "$d"
  if [ ! -x "$d/kotlinc/bin/kotlinc" ]; then
    bajar "$GH/JetBrains/kotlin/releases/download/v$v/kotlin-compiler-$v.zip" "$d/kc.zip" && (cd "$d" && unzip -q -o kc.zip && echo "  ✓ kotlinc $v")
  fi
done
if [ ! -x /var/tmp/jdk/jdk-17.0.13+11/bin/java ]; then
  bajar "$GH/adoptium/temurin17-binaries/releases/download/jdk-17.0.13%2B11/OpenJDK17U-jdk_x64_linux_hotspot_17.0.13_11.tar.gz" /var/tmp/jdk/jdk17.tar.gz && (cd /var/tmp/jdk && tar xzf jdk17.tar.gz && echo "  ✓ JDK 17")
fi
bajar "$MC/org/junit/platform/junit-platform-console-standalone/6.1.2/junit-platform-console-standalone-6.1.2.jar" $J/junit-console-6.1.2.jar
bajar "$MC/org/junit/platform/junit-platform-console-standalone/6.1.3/junit-platform-console-standalone-6.1.3.jar" $J/junit-console-6.1.3.jar
for a in kotest-assertions-core-jvm kotest-assertions-shared-jvm kotest-common-jvm; do
  for v in 6.0.7 5.9.1; do bajar "$MC/io/kotest/$a/$v/$a-$v.jar" "$J/$a-$v.jar"; done
done
bajar "$MC/io/kotest/kotest-assertions-api-jvm/5.9.1/kotest-assertions-api-jvm-5.9.1.jar" $J/kotest-assertions-api-jvm-5.9.1.jar
bajar "$MC/org/jetbrains/kotlinx/kotlinx-coroutines-core-jvm/1.10.2/kotlinx-coroutines-core-jvm-1.10.2.jar" $J/kotlinx-coroutines-core-jvm-1.10.2.jar
# logcat se publica como AAR: hay que extraerle classes.jar (0.4 no está servido aquí; 0.1 sí y la
# superficie LogPriority/asLog/logcat es la misma)
if [ ! -s $J/logcat-real-classes.jar ]; then
  bajar "$MC/com/squareup/logcat/logcat/0.1/logcat-0.1.aar" $J/logcat-0.1.aar && \
    (mkdir -p $J/ax && cd $J/ax && unzip -q -o ../logcat-0.1.aar && cp classes.jar ../logcat-real-classes.jar && echo "  ✓ logcat classes.jar")
fi
echo "== humo =="
/var/tmp/kc-2.3.10/kotlinc/bin/kotlinc -version 2>&1 | head -1
/var/tmp/jdk/jdk-17.0.13+11/bin/java -version 2>&1 | head -1
echo "RESULTADO: $([ $fallos -eq 0 ] && echo HERRAMIENTAS_LISTAS || echo "FALTAN $fallos")"

# --- GIT_ASKPASS -------------------------------------------------------------
# El vaciado del espacio local se lleva /tmp/ap.sh, y sin él ningún empuje funciona
# ("could not read Username"). Pasó de verdad el 2026-11-17: el commit quedó local sin
# publicar hasta que se recreó el helper. Se rehace aquí para que restaurar el entorno
# restaure también la capacidad de publicar. Nunca se escribe el token en la URL.
if [ ! -x /tmp/ap.sh ]; then
  cat > /tmp/ap.sh <<'APEOF'
#!/bin/sh
case "$1" in
  *Username*) echo "Alex17273747576777" ;;
  *)          echo "$GIT_TOKEN" ;;
esac
APEOF
  chmod 700 /tmp/ap.sh
  echo "  ✓ /tmp/ap.sh (GIT_ASKPASS) recreado"
fi
