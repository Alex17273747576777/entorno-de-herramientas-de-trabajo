# Resultado de la VM Android

Fecha de los intentos: 12 de noviembre de 2026 (UTC).

## Instalación comprobada

- AVD `cerox_api31_x86_64`: Android 12, API 31, Google APIs, x86_64.
- QEMU 10.0.13, emulador 37.2.13.0, ADB 34.0.5, JDK 21.0.13.
- Swap: 3 GiB. Instalador repetible: `work/vm/setup-vm.sh`.

## Intento 1: SwiftShader, TCG, 2048 MiB

ADB llegó a `device`; `getprop` confirmó Android 12/API 31/x86_64 y `pm` listó
paquetes. Captura PNG negra. `sys.boot_completed` no apareció. QEMU detectó
hilos colgados y terminó con 139 (segfault). Evidencia: `android-responde.txt`,
`vm-android.png`, `logcat-arranque.txt` y log del proceso.

## Intento 2: GPU guest, TCG, 1536 MiB

Se cambió `hw.ramSize=1536`, `hw.gpu.mode=guest` y heap de 256 MiB. ADB confirmó
Android 12/API 31/x86_64; `bootanim=running` y `sys.boot_completed` vacío. La
captura no entregó bytes tras más de tres minutos y se canceló. Host: 1982 MiB
RAM, 1918 usados y 1351 MiB de swap; QEMU ocupaba unos 1610 MiB RSS. Se detuvo
para no saturar el entorno. Evidencia: `arranque-intento2.log`,
`intento2-propiedades.txt`, `intento2-android-responde.txt`,
`screencap-intento2-error.txt`.

## Conclusión

La instalación y el acceso ADB mediante TCG son reales. Un arranque gráfico
completo y estable no está demostrado. No se instaló ni se probó el APK, ni se
validó WebView en esta VM. Esto no prueba que TCG sea imposible en general.
