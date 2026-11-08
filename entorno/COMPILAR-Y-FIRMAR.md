# Cómo se construyó el APK de cero-X

Todo lo de aquí se ejecutó en esta máquina. Nada es una sugerencia sin probar.

## La máquina

2 núcleos, 2 GB de RAM, sin `/dev/kvm`. Esto importa: **las tres primeras veces
el build falló por memoria, no por código.**

## Instalación desde cero

```bash
sudo apt install -y openjdk-21-jdk

# swap — SIN ESTO EL DAEMON DE GRADLE MUERE A MITAD DE COMPILACIÓN
sudo fallocate -l 2G /swapfile && sudo chmod 600 /swapfile
sudo mkswap /swapfile && sudo swapon /swapfile

# SDK y Gradle en /opt, NO en /home (limitado a 992 MB)
curl -sLO https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip
sudo mkdir -p /opt/android-sdk/cmdline-tools
sudo unzip -q commandlinetools-linux-11076708_latest.zip -d /tmp/sdkx
sudo mv /tmp/sdkx/cmdline-tools /opt/android-sdk/cmdline-tools/latest

curl -sLO https://downloads.gradle.org/distributions/gradle-8.11.1-bin.zip
sudo unzip -q gradle-8.11.1-bin.zip -d /opt

sudo chown -R $USER /opt/android-sdk /opt/gradle-8.11.1

yes | /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager --sdk_root=/opt/android-sdk \
  "platform-tools" "platforms;android-36" "build-tools;36.0.0"

# Gradle necesita su propio HOME en /opt
sudo mkdir -p /opt/gh && sudo chown $USER /opt/gh
```

## Compilar

```bash
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export ANDROID_HOME=/opt/android-sdk ANDROID_SDK_ROOT=/opt/android-sdk
export GRADLE_USER_HOME=/opt/gh
export PATH=$JAVA_HOME/bin:$PATH

cd cero-X-app/android
/opt/gradle-8.11.1/bin/gradle assembleRelease --no-daemon --console=plain --max-workers=1
```

`--no-daemon` y `--max-workers=1` no son preferencia: con daemon y 2 workers la
máquina entra en swap y el proceso acaba asesinado.

## Las tres trampas que cuestan una tarde cada una

**1. Sin swap, el daemon desaparece.**
El síntoma es `Gradle build daemon disappeared unexpectedly`. No es un bug del
código. Con 0 swap y 2 GB, R8 y el compilador de Kotlin se pelean y el OOM
killer mata al más grande.

**2. R8 necesita 2 GB de heap.**
Con `-Xmx1024m` y con `-Xmx1536m` abortaba con `java.lang.OutOfMemoryError:
Java heap space` dentro de `minifyReleaseWithR8`. Con 2048m y swap termina.
Está en `gradle.properties`.

**3. `signingConfigs` tiene que declararse ANTES de `buildTypes`.**
Al revés, la evaluación de `buildTypes` no encuentra `signingConfigs.release` y
falla con `Could not get unknown property 'release'`.

## Firmar

```bash
keytool -genkeypair -keystore /opt/keys/cerox-release.jks \
  -storepass TU_CLAVE -alias cerox -keypass TU_CLAVE \
  -dname "CN=cero-X,O=La Bandita,C=DO" -validity 10000 -keyalg RSA -keysize 4096

export CEROX_KEYSTORE=/opt/keys/cerox-release.jks
export CEROX_KEYSTORE_PASS=TU_CLAVE
export CEROX_KEY_ALIAS=cerox
export CEROX_KEY_PASS=TU_CLAVE
```

La llave NO va al repo: `build.gradle` la lee del entorno. Sin esas variables el
APK sale sin firmar, que es lo correcto.

Firma v2 basta: existe desde Android 7.0 (API 24) y cero-X pide API 26 mínimo.
No hace falta v1, aunque es fácil creer lo contrario —me pasó.

## Los modelos

No van en git: GitHub rechaza archivos de más de 100 MB y tres de los cinco los
superan. Se bajan con:

```bash
python3 scripts/bajar-modelos.py
```

Comprueba el `sha256` de cada uno contra el que se verificó ejecutándolo. Si no
coincide, borra el archivo: es preferible un build que falla a un APK con un
modelo que no es el que se probó.

Van con `noCompress 'onnx'`: el runtime los mapea desde el archivo en vez de
descomprimir cientos de MB en RAM.

## Verificar el resultado

```bash
BT=/opt/android-sdk/build-tools/36.0.0
APK=android/app/build/outputs/apk/release/app-release.apk

$BT/apksigner verify --print-certs $APK                      # firma y quién firma
$BT/aapt2 dump badging $APK | grep launchable                 # actividad de arranque
$BT/aapt2 dump resources $APK | grep -A7 'mipmap/ic_launcher'  # el icono, por config

# Desglose real por tipo, sin estimar:
python3 -c "
import zipfile
z=zipfile.ZipFile('$APK'); b={}
for i in z.infolist():
    k=('modelos' if i.filename.startswith('assets/models/') else
       'nativo' if i.filename.startswith('lib/') else
       'dex' if i.filename.startswith('classes') and i.filename.endswith('.dex') else 'otros')
    b[k]=b.get(k,0)+i.file_size
[print(f'{k:10}{v/1048576:8.2f} MiB') for k,v in b.items()]"
```

**No verifiques el icono buscando archivos `mipmap` con `unzip -l`:** aapt2
renombra los recursos dentro del APK. Hay que preguntarle a `aapt2 dump
resources`. Yo dije que el APK no tenía icono por ese error; sí lo tenía.

## Comprobar si un modelo ONNX sirve, antes de empaquetarlo

Esto evitó meter 111 MB muertos en el APK. Cargar no es lo mismo que funcionar, y
"funcionar" no se sabe sin ejecutarlo:

```bash
curl -sLO https://repo1.maven.org/maven2/com/microsoft/onnxruntime/onnxruntime/1.17.0/onnxruntime-1.17.0.jar

cat > V.java <<'JAVA'
import ai.onnxruntime.*; import java.nio.FloatBuffer; import java.util.*;
public class V { public static void main(String[] a) throws Exception {
  OrtEnvironment env=OrtEnvironment.getEnvironment();
  OrtSession s=env.createSession(a[0],new OrtSession.SessionOptions());
  System.out.println("entradas: "+s.getInputInfo());
  int C=3,H=224,W=224; float[] d=new float[C*H*W]; Arrays.fill(d,0.5f);
  OnnxTensor t=OnnxTensor.createTensor(env,FloatBuffer.wrap(d),new long[]{1,C,H,W});
  long t0=System.currentTimeMillis();
  OrtSession.Result r=s.run(Collections.singletonMap(a[1],t));
  System.out.printf("OK %d ms -> %s%n", System.currentTimeMillis()-t0,
     Arrays.toString(((OnnxTensor)r.get(0)).getInfo().getShape()));
  env.close(); } }
JAVA

javac -cp onnxruntime-1.17.0.jar V.java
java -Xmx2g -cp onnxruntime-1.17.0.jar:. V modelo.onnx nombre_de_la_entrada
```

Si dice `ORT_NOT_IMPLEMENTED` o `Type Error`, el modelo no vale por muy bien que
se descargue. Pasó con los int8 de manga-ocr (usan `ConvInteger`, que ONNX
Runtime no implementa en CPU) y con su decoder fp16.

## Lo que esta máquina NO puede hacer

- **Emulador**: sin `/dev/kvm`, con 2 GB de RAM, un AVD de API 36 no arranca. Por
  eso cero-X tiene verificación estática y no prueba de arranque. Decirlo es
  parte del trabajo.
- **Builds en paralelo**: 2 núcleos. `--max-workers=1` o muerte por swap.
