# cero-X · límites medidos de la máquina

Todo medido el 2026-11-13 en el sandbox de Arena, no deducido. Sirve para no volver a
prometer lo que aquí no cabe.

| qué | medida | consecuencia |
|---|---|---|
| virtualización por hardware | `/dev/kvm` no existe; `/proc/cpuinfo` tiene **0** flags `vmx`/`svm` | no arranca ningún AVD, ni una imagen GSI, ni Cuttlefish |
| CPU | 2 | los cierres Gradle tardan minutos, no segundos |
| RAM | 1.982 MB | hace falta swap; R8 mata el demonio sin él |
| disco `/` | 25 GB, ~21 GB libres al rearmar | acota el tamaño de swap posible |
| `adb devices` | vacío | ninguna prueba instrumentada se ejecuta; se compilan y se empaquetan |
| `sudo` | uid 1000 con sudo sin contraseña | pero `sudo modprobe` **no existe**: no se pueden cargar módulos del kernel |
| zram | sin `/sys/block/zram*`, sin `zramctl` | imposible; swap en archivo es la única palanca |
| swap activo | `/swapfile-cerox` 12 GiB (`/proc/swaps` 12.582.908 KB) | receta versionada: el mayor tamaño de 10-15 GiB que deje 9 GiB libres, con respaldo de 5 GiB |
| plataforma Android 17 beta 3 | `platforms/android-37.2-beta3` instalada, `ApiLevel=37.1`, `CodeName=DEV` | sirve para **compilar**, no para probar |
| techo de Robolectric | 4.16.1 emula API 34, 35 y **36**; API 37 da `API level 37 is not available` (`UnknownSdk.java:45`) | las pruebas corren en Android 16; Android 17 no es alcanzable en JVM |
| presupuesto de snapshot del workspace | 128 MiB / 10.000 archivos de tope, margen operativo 110 MiB; el repo sano pesa **30,20 MiB y 1.994 archivos** | cualquier caché que una herramienta escriba dentro de `/home/user` se lo come de golpe. Medido el 2026-11-13: una corrida de Gradle **sin** `source entorno/local.sh` usó su `GRADLE_USER_HOME` por defecto y dejó `~/.gradle` con **659 MiB y 4.600 archivos**, 22 veces el repo. El canónico es `/opt/cerox/gradle` (2,1 GB, fuera del workspace) |
| escáneres de APK | `clamscan`, `apktool`, `jadx`, `androguard`, `dexdump` ausentes; VirusTotal exige clave | no se puede presentar como escaneado lo que no se escaneó |

## Lo que la compilación no certifica

Robolectric no ejecuta DEX. Que la suite pase en JVM no valida Coil, gestos reales,
foco físico, contraste renderizado, lector de pantalla ni el efecto real de detener un
módulo en el aparato. Esos recorridos están escritos, compilados y empaquetados dentro
del APK `androidTest` —verificados en su `classes4.dex`— y **nunca ejecutados**.

## Lo que se pierde en cada reinicio

JDK, Android SDK, `/opt/cerox` (Gradle y m2), el swap, la identidad Git local y **los
bits de ejecución de los archivos versionados**. El síntoma de esto último es
`git status` mostrando `mode change 100755 => 100644` con `git diff --stat` en 0: no es
ruido, es el árbol sucio. Se rearma con `entorno/RECETA-DE-REARME.md`.
