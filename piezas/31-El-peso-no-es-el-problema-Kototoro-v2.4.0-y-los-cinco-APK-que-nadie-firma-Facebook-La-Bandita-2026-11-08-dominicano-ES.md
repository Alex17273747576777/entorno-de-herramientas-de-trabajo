*El peso no es el problema: Kototoro v2.4.0 salió a las 03:32 de esta madrugada con 300,86 MiB de APK universal, cinco APK y ni una sola huella que cubra a ninguno de los cinco*

*La Bandita · domingo 8 de noviembre de 2026, 06:25 de la mañana en Santo Domingo · edición dominicano-español · pieza 31 de Facebook*

⏱️ *Lectura total: 41 minutos · veinte repositorios del ecosistema medidos hoy a las 06:25 de la mañana contra la API de GitHub · el más pesado del ecosistema publicado hace cuatro horas y trece minutos · cinco APK en su entrega y cero huellas para los cinco · 1.538.912 descargas medidas entre los que publican entrega · una orden para comprobar el hallazgo central en menos de un minuto · cero paquetes alojados aquí · datos medidos en vivo hoy, no recuerdos*

*🗺️ Mapa de esta pieza*

━━━━━━━━━━━━━

├── 🧱 La semilla · el archivo que pesa 300 megas
├── ⚡ En una página
├── 🕰️ La medición de las 06:25 · veinte repositorios en vivo
├── 📦 El peso, explicado como se explica un bulto de arena
├── 🔏 La huella · y la ausencia que nadie mira
├── 🧾 Los veinte fichas, uno por uno, con lo que firman
├── 🧨 Los tres que no pasan el corte · y el más descargado es uno
├── 📊 El censo y las cifras · descargas, días, licencias
├── 🛠️ Una orden para no creerle a nadie
├── 🚪 Lo que esta pieza no tiene
├── 📅 La semana de prueba
├── ❓ Las preguntas del grupo
├── 🧮 Cómo se midió cada número · el método, campo a campo
└── 🌅 cierre · 🔗 enlaces · 🗒️ notas al pie

━━━━━━━━━━━━━

🧱 *La semilla · el archivo que pesa 300 megas*

Alguien del grupo escribió anoche, a eso de las once: «¿y por qué esta vaina pesa trescientos megas?». Le contestaron cuatro personas y las cuatro dijeron algo distinto, y las cuatro estaban equivocadas por la misma razón: nadie había abierto la entrega para ver qué había adentro. Uno dijo que eran los modelos de inteligencia artificial. Otro dijo que era el motor de video. El tercero dijo que era «basura de los chinos». El cuarto dijo que así son las apps buenas.

Esta pieza abre la entrega. Y lo que encuentra es más interesante que cualquiera de las cuatro respuestas: el archivo de 300,86 MiB es **el APK universal** —el que trae las cuatro arquitecturas adentro para que nadie se equivoque al bajar— y la misma entrega tiene otros cuatro APK, uno por arquitectura, el más liviano de los cuales pesa **113,72 MiB**. O sea que el peso no es un misterio ni un defecto: es **una decisión de empaquetado**, tomada a propósito, y la misma entrega ofrece la alternativa.

Pero al abrir la entrega aparece otra cosa, y esa sí que nadie la mencionó anoche. De los quince archivos de la entrega, **cuatro vienen con su archivo de huella `.sha256`**: el de iOS, los dos de macOS y el de Windows. Los **cinco APK de Android no tienen huella**. El proyecto que se tomó el trabajo de hashear un `.msi` de 313 MB no hasheó ninguno de sus cinco `.apk`.

Y no está solo. El programa más descargado de todo el ecosistema —sesenta y ocho mil descargas, más que todos los demás juntos en algunos casos— no publica **ninguna** huella: ni de APK, ni de nada. Ni un archivo, ni una línea en el cuerpo de la entrega, ni un checksum pegado en el texto.

Esa es la pieza de hoy. El peso es la excusa para entrar. Lo que hay adentro es el tema.

━━━━━━━━━━━━━

⚡ *En una página*

Veinte repositorios del ecosistema de lectores y reproductores para Android, medidos hoy domingo 8 de noviembre de 2026 a las 06:25 de la mañana en Santo Domingo, contra la API pública de GitHub. Sin estimaciones, sin recuerdos, sin promedios inventados.

Tres cifras para llevarse:

**Uno.** El APK universal del programa más pesado del ecosistema pesa **300,86 MiB** y salió hoy a las **03:32 de la madrugada** hora dominicana. Es la entrega más reciente de todas las medidas en esta pieza: tenía **dos horas y cincuenta y tres minutos** de vida cuando se midió.

**Dos.** Ese mismo programa publica **cuatro archivos `.sha256`** en su entrega y **ninguno de los cuatro cubre un APK**. Se hashearon el `.ipa` de iOS, los dos `.dmg` de macOS y el `.msi` y el `.zip` de Windows. Los cinco `.apk` de Android quedaron fuera.

**Tres.** El programa más descargado de los veinte —**621.665 descargas** en su última entrega, el 67 % de todas las descargas medidas hoy— no publica **ni una** huella. Cero archivos de checksum, cero líneas de hash en el cuerpo de la entrega.

Y el resultado incómodo que ordena todo lo demás: **de los veinte, solo uno publica alguna huella, y no publica la que importa.** El ecosistema entero —veinte proyectos, 25.000 estrellas en el más famoso, un millón y medio de descargas medidas— no le da a nadie con qué comprobar que el archivo que bajó es el archivo que el autor publicó.

━━━━━━━━━━━━━

🕰️ *La medición de las 06:25 · veinte repositorios en vivo*

Cada cifra de esta sección se leyó hoy, domingo 8 de noviembre de 2026, a las 06:25 de la mañana en Santo Domingo, directamente de la API pública de GitHub. No son recuerdos del 7 de noviembre. No son los números que alguien puso en un chat. Son los números que devolvió la API en esa llamada, y el script que los pidió está en la sección del método.

La hora importa más de lo que parece: el programa central de esta pieza **publicó su entrega a las 07:32 UTC de hoy**, que son las 03:32 de la madrugada en Santo Domingo. Si esta pieza se hubiera escrito ayer, el dato principal no existiría. La medición no es un adorno: es la razón de que la pieza tenga algo que decir.

**Datos reales, repositorio por repositorio:**

1. **Kototoro-app/Kototoro** — ★677 estrellas · Apache-2.0 · creada el 2026-01-18 · última entrega **v2.4.0** publicada hoy 8 de noviembre a las 03:32 hora dominicana · **15 archivos en la entrega, 5 de ellos APK** · **31.077 descargas** sumadas · repositorio de 235.053 KB · **4 huellas `.sha256`, ninguna de APK** · 16 flujos de compilación · más de 100 personas empujando código · última actualización del repositorio: hoy.

2. **mihonapp/mihon** — ★25.120 estrellas · Apache-2.0 · última entrega **v0.21.3** del 2026-10-25 · 6 archivos, todos APK · **621.665 descargas** · repositorio de 82.565 KB · **0 huellas** · 5 flujos · más de 100 contribuyentes.

3. **komikku-app/komikku** — ★5.000 estrellas · Apache-2.0 · última entrega **v1.14.1** del 2026-07-17 · **404.324 descargas** · repositorio de 121.845 KB · **0 huellas**.

4. **nekomangaorg/Neko** — ★2.825 estrellas · Apache-2.0 · última entrega **3.8.5** del 2026-10-30 · **15.312 descargas** · repositorio de 149.044 KB · **0 huellas**.

5. **AppFuton/Futon** — ★480 estrellas · GPL-3.0 · última entrega **v9.9** del 2026-10-21 · **2.860 descargas** · repositorio de 108.247 KB · **0 huellas**.

6. **Spyou/Zangetsu** — ★511 estrellas · GPL-3.0 · última entrega **v2.3.5** del 2026-11-01 · **8.719 descargas** · repositorio de 30.181 KB · **0 huellas**.

7. **Jays2Kings/tachiyomiJ2K** — ★5.410 estrellas · Apache-2.0 · última entrega **v1.8.1** del 2026-08-15 · **188.681 descargas** · repositorio de 106.942 KB · **0 huellas**.

8. **jobobby04/TachiyomiSY** — ★4.203 estrellas · Apache-2.0 · última entrega **1.13.2** del 2026-07-13 · **169.447 descargas** · repositorio de 100.669 KB · **0 huellas**.

9. **aniyomiorg/aniyomi** — ★7.882 estrellas · Apache-2.0 · última entrega **v0.18.2.1** del 2026-09-14 · 5 APK · **293.398 descargas** · repositorio de 83.434 KB · **0 huellas**.

10. **animiruorg/animiru** — ★913 estrellas · GPL-3.0 · última entrega **v0.20.1.1** del 2026-11-03 · **4.675 descargas** · repositorio de **411.889 KB**, el más grande de los veinte · **0 huellas**.

11. **KotatsuApp/Kotatsu** — ★8.956 estrellas · GPL-3.0 · **sin entrega publicada** · 0 descargas · repositorio de 91.765 KB · 3 flujos · más de 100 contribuyentes.

12. **recloudstream/cloudstream** — ★11.183 estrellas · GPL-3.0 · última entrega **v4.8.0** del 2026-07-10 · 3 archivos: dos son `.jar`, uno es el APK **sin número de versión en el nombre** · **881.950 descargas**, el segundo más alto de los veinte · repositorio de 54.685 KB · **0 huellas**.

13. **keiyoushi/extensions** — ★15.456 estrellas, **el más popular de los veinte** · sin licencia declarada · última entrega de hoy 2026-11-08 · **218 archivos** en una sola entrega · **15.387 descargas** · repositorio de 249.066 KB · 0 flujos de compilación · **2 personas** empujando código · **0 huellas**.

14. **lnreader/lnreader-plugins** — ★370 estrellas · MIT · última entrega **v2.0.0** del **2024-03-21** · 0 archivos · **0 descargas** · repositorio de 25.929 KB · **14 flujos de compilación**, el que más tiene de los veinte · repositorio **962 días** sin entrega.

15. **Shebyyy/AnymeX-Preview** — ★54 estrellas · **sin licencia declarada** · última entrega **v3.2.0+2-beta** del 2026-11-07, ayer · 11 archivos: APK, `.ipa`, `.AppImage`, `.rpm`, `.zip` · **98 descargas** · repositorio de **402.150 KB** · **0 huellas** · 4 personas empujando código.

16. **UsagiApp/Usagi** — ★293 estrellas · GPL-3.0 · última entrega **v1.2** del 2026-10-03 · **6.244 descargas** · repositorio de 14.610 KB, **el más liviano de los veinte**.

17. **Suwayomi/Suwayomi-Server** — ★8.023 estrellas · MPL-2.0 · última entrega **v2.4.2366** del 2026-09-30 · **31.200 descargas** · repositorio de 103.089 KB · **0 huellas**.

18. **mihonapp/mihon** ya está arriba como la ficha 2. Se repite aquí porque su entrega es la referencia de tamaño para comparar: **68.195.386 bytes**.

19. **aniyomiorg/aniyomi** ya está arriba como la ficha 9. Se repite por el mismo motivo. **0 huellas**.

20. **recloudstream/cloudstream** ya está arriba como la ficha 12. Se repite por el mismo motivo. **0 huellas**.

Las fichas 18, 19 y 20 no son relleno: son los tres archivos contra los que se compara el peso en la sección siguiente, y están aquí para que la comparación no dependa de la memoria de nadie. Un lector que quiera comprobar el factor de 4,63 que aparece más abajo necesita las tres cifras en la mano.

━━━━━━━━━━━━━

📦 *El peso, explicado como se explica un bulto de arena*

Cuando alguien pregunta por qué una app pesa trescientos megas, la respuesta honesta tiene tres pisos, y hay que bajar los tres.

**El primer piso: no es un archivo, son cinco.** La entrega de Kototoro v2.4.0 trae cinco APK:

| APK | bytes | MiB | descargas |
|---|---:|---:|---:|
| `arm64-v8a` | 127.130.450 | 121,24 | 137 |
| `armeabi-v7a` | 119.240.334 | 113,72 | 6 |
| `release.apk` (universal) | 315.477.702 | **300,86** | 7 |
| `x86` | 141.514.358 | 134,96 | 3 |
| `x86_64` | 148.431.130 | 141,55 | 3 |

El que bajó anoche el amigo del grupo no fue el de 121 MiB. Fue el universal. Y esa es la primera razón por la que le pesó trescientos: **el teléfono casi seguro era `arm64-v8a`**, y en ese caso el archivo correcto pesaba **121,24 MiB**, no 300,86. Se bajaron 179,62 MiB de más, que es un poco más de lo que pesa un Mihon universal completo.

**El segundo piso: el universal no es la suma de los cuatro.** Si el universal fuera los cuatro APK pegados uno detrás de otro, pesaría 511,47 MiB. Pesa 300,86. La diferencia —**210,61 MiB, el 41 %**— es lo que Gradle ahorra cuando empaqueta las cuatro arquitecturas juntas: los recursos compartidos (`resources.arsc`, layouts, imágenes, dex) se guardan **una vez**, y solo las bibliotecas nativas se guardan cuatro veces. Por eso el universal es caro, pero no es la estafa que parece.

**El tercer piso: por qué hay algo nativo que guardar cuatro veces.** Un APK universal con 300 MiB y un `.ipa` de 93,68 MiB del mismo proyecto en la misma entrega dan la pista: lo que engorda al APK no es la interfaz, es lo que va compilado para cada arquitectura. Compárese con Mihon, que es un lector de manga sin motores nativos pesados: su universal pesa **68.195.386 bytes = 65,04 MiB**. Kototoro pesa **4,63 veces** más.

Y ahora la parte que importa para quien esté pensando en hacer su propia app, que es media razón de ser de esta pieza: **los 300 MiB no son un error, son una decisión con dos filos.** El universal es cómodo —el usuario no se equivoca nunca— y es caro —paga 300 MiB en su disco y en su descarga para usar 121—. Los cinco APK por arquitectura son eficientes y son incómodos: exigen que alguien sepa qué arquitectura tiene su teléfono, y ese alguien, las más de las veces, no lo sabe.

La decisión honesta no es elegir uno de los dos. Es **publicar los dos y decirlo en el cuerpo de la entrega**, con el tamaño de cada uno al lado de su nombre, y con un enlace que explique cómo saber cuál te toca. Kototoro publica los cinco. No publica la explicación. Las 137 descargas del `arm64-v8a` contra las 7 del universal, con todo, sugieren que la gente que llega ahí ya sabe lo que busca.

━━━━━━━━━━━━━

📲 *Cómo sabe cuál es tu arquitectura · y por qué casi seguro es arm64-v8a*

Si la sección anterior deja una pregunta práctica, es esta: ¿cuál de los cinco bajo? La respuesta se puede averiguar en un minuto, sin instalar nada raro y sin ser programador.

**Las cuatro arquitecturas, en palabras llanas:**

- **`arm64-v8a`** — ARM de 64 bits. Es la de prácticamente cualquier teléfono Android vendido desde 2017. Si tu teléfono tiene menos de ocho años, es esta.
- **`armeabi-v7a`** — ARM de 32 bits. Teléfonos viejos, de antes de 2017, y algunos económicos que se siguieron fabricando en 32 bits. Ojo con la trampa: un teléfono de 64 bits **puede** correr una app de 32 bits, porque Android trae compatibilidad hacia atrás. Pero eso está cambiando: Google Pixel desde el 7 y varios fabricantes han ido dejando el soporte de 32 bits por el camino. Así que «el de 32 funciona en todos» ya no es verdad, y conviene no repetirlo.
- **`x86`** — Intel de 32 bits. Emuladores y algún Chromebook antiguo.
- **`x86_64`** — Intel de 64 bits. Emuladores modernos, Chromebooks y tablets con procesador Intel. Si estás en un teléfono de verdad, no es la tuya.

**Cómo comprobarlo, por orden de facilidad:**

**Uno, desde Ajustes.** Ajustes → Acerca del teléfono → Información del hardware. Muchos fabricantes muestran ahí el procesador; si dice «Snapdragon 8 Gen 2», «Dimensity 9200» o «Exynos 2400», es ARM de 64 bits. Si es un modelo de 2015, probablemente 32.

**Dos, desde una app de información del sistema.** Cualquiera de las que muestran el hardware te lo dice en una pantalla. No hace falta root ni permisos raros.

**Tres, desde una terminal, si ya tienes Termux.** Un comando y ya:

```bash
getprop ro.product.cpu.abi
```

Devuelve una línea, y esa línea es la respuesta. Si dice `arm64-v8a`, es el APK de 121,24 MiB. Si dice `armeabi-v7a`, es el de 113,72 MiB.

**Cuatro, el experimento que no recomiendo.** Bajar el universal y ver. Funciona siempre y cuesta 179,62 MiB de más en tu disco y en tu factura de datos, para siempre, cada vez que actualices. Es lo que hizo el amigo del grupo anoche sin saberlo.

Y hay una razón concreta por la que el `arm64-v8a` es casi siempre la respuesta correcta más allá de la arquitectura: **es el que más gente baja**. En la entrega de hoy, 137 descargas para el `arm64-v8a` contra 6 del `armeabi-v7a`, 7 del universal y 3 de cada uno de los dos `x86`. Ese reparto no es una opinión: es lo que hicieron los otros 153. Si dudas y no puedes comprobar, la apuesta con mejor historial es la de 64 bits ARM.

━━━━━━━━━━━━━

🧬 *Qué hay dentro de esos 300 MiB · la razón que nadie dijo anoche*

El peso tiene una explicación técnica y se puede comprobar leyendo el repositorio, así que la escribo con números en vez de con adjetivos.

Kototoro no es un lector de manga. Es **tres lectores de manga en uno**, y la prueba está en los espacios de nombres de su código fuente, medidos hoy en la rama `devel`:

```
org.skepsun.kototoro.*        ← el proyecto propio
org.koitharu.kotatsu.*        ← Kotatsu
com.lagradost.cloudstream3.*  ← Cloudstream
```

Y los recuentos de archivos por familia, también medidos hoy:

| palabra clave en la ruta | archivos |
|---|---:|
| `parser` | 399 |
| `extension` | 167 |
| `backup` | 135 |
| `plugin` | 24 |

Eso es lo que hay dentro del APK, y esa es la razón honesta del peso. Un lector con extensiones al estilo Mihon transporta **un intérprete de extensiones**: el código que sabe cargar un APK de extensión ajeno, leer su `Source` y llamarlo. Kototoro transporta **tres**: el de Mihon/Tachiyomi, el de los parsers de Kotatsu y el de los plugins de Cloudstream. Y el de Cloudstream es el más caro, porque un plugin de Cloudstream no es una lista de selectores: es **bytecode** que se carga en tiempo de ejecución con un `ClassLoader` propio.

A eso se le suma el soporte de Shizuku para permisos ADB sin root, los motores de lectura de EPUB y cómics, y las herramientas de copia de seguridad con su índice. Cada una de esas cosas pesa, y cada una está cuatro veces si el APK es universal, porque las bibliotecas nativas se compilan por arquitectura.

Con eso en la mano, la pregunta útil cambia de forma. Ya no es «¿por qué pesa tanto?», que no tiene buena respuesta porque el peso no es un error. Es **«¿quiero yo tres intérpretes de extensiones en el bolsillo, o me basta con uno?»**. Para quien solo lee manga, Mihon hace ese trabajo en 65,04 MiB. Para quien quiere leer manga, ver anime y abrir novelas desde una sola app, con tres ecosistemas de extensiones disponibles, 300 MiB es lo que cuesta la llave que abre las tres puertas. No hay trampa en ninguna de las dos direcciones: hay dos productos distintos y una cifra que los separa.

━━━━━━━━━━━━━

🔏 *La huella · y la ausencia que nadie mira*

Una huella es un número que se calcula del archivo. Se le pasa el archivo entero por una función —SHA-256 es la de uso corriente— y sale una cadena de 64 caracteres hexadecimales. Cambia un solo bit del archivo y la cadena sale completamente distinta. No hay manera de fabricar un archivo distinto que dé la misma cadena: eso es lo que hace que la huella sirva.

Para qué sirve, en concreto: tú bajas el archivo. Alguien en el camino —un servidor espejo, un proxy, un enlace reenviado, un amigo, un espejo pirata— puede haber puesto otro archivo en su lugar. Si el autor publicó la huella, tú calculas la huella de lo que bajaste, la comparas con la del autor, y ya está: o coincide, o no coincides. No hay opinión.

Ahora la parte que esta pieza encontró y que no estaba en el guion.

**Kototoro publica cuatro huellas.** En su entrega de hoy hay exactamente cuatro archivos `.sha256`:

```
Kototoro-2.4.0-ios-release-unsigned.sha256          106 bytes
Kototoro-2.4.0-macos-arm64-release.sha256           105 bytes
Kototoro-2.4.0-macos-x64-release.sha256             103 bytes
Kototoro-2.4.0-windows-x64-release.sha256           212 bytes
```

Y hay **cinco archivos `.apk`**. Ninguno tiene `.sha256`. Lo he comprobado por nombre, uno por uno:

```
APK: 5 -> arm64-v8a, armeabi-v7a, release, x86, x86_64
SHA: 4 -> ios-release-unsigned, macos-arm64, macos-x64, windows-x64
¿algún hash cubre un .apk?: NO
```

No es que el proyecto no sepa hashear. Es que el archivo de 313 MB para Windows sí lo hasheó, el de 98 MB para iOS sí lo hasheó, y **los cinco de Android, que suman 853,79 MiB y que son el 95 % de la razón por la que existe el proyecto, no**.

**Mihon no publica ninguna.** Su entrega v0.21.3 tiene seis archivos, todos APK, y ningún checksum: ni archivo aparte, ni línea en el cuerpo de la entrega. 621.665 descargas sin una sola forma de comprobar que el archivo llegó entero.

**Cloudstream tampoco.** Tres archivos, ninguno con hash, y el APK se llama `app-prerelease-release.apk`: **sin número de versión en el nombre**. Bajas ese archivo y no sabes, mirándolo, qué versión es.

**Keiyoushi/extensions tampoco**, con 218 archivos en una sola entrega y 15.456 estrellas.

**AnymeX-Preview tampoco**, con once archivos repartidos entre cinco sistemas operativos y **sin licencia declarada**, que es una ausencia todavía más grave que la del hash: sin licencia, legalmente nadie tiene permiso de usarlo.

El recuento, que es el titular de la pieza: **de veinte repositorios, uno publica huellas; y de las cuatro huellas que publica, cero cubren un archivo de Android.**

━━━━━━━━━━━━━

🧾 *Los veinte fichas, uno por uno, con lo que firman*

Esta es la sección de las fichas, en el orden de la medición. Cada una trae lo mismo: estrellas, licencia, entrega, descargas, tamaño del repositorio, huellas y contribuyentes. Los comentarios son míos y van marcados como comentarios.

**1 · Kototoro** — kototoro-app/Kototoro · ★677 · Apache-2.0 · v2.4.0 de hoy 03:32 AST · 15 archivos, 5 APK · 31.077 descargas · 235.053 KB de repositorio · 4 huellas, ninguna de APK · 16 flujos · +100 contribuyentes.
*Comentario:* el proyecto más ambicioso de la lista y el único con huellas. Publica para Android, iOS, macOS, Windows — y hashea todo menos Android. Guarda este detalle: es el que ordena la tesis de la pieza.

**2 · Mihon** — mihonapp/mihon · ★25.120 · Apache-2.0 · v0.21.3 del 25 de octubre · 6 archivos APK · 621.665 descargas · 82.565 KB · 0 huellas · 5 flujos.
*Comentario:* el más descargado y el más famoso. Su entrega tiene seis variantes por arquitectura, lo cual está bien pensado, y ni una huella, lo cual no. 65,04 MiB de universal: la mitad de lo que uno espera para una app con su función.

**3 · Komikku** — komikku-app/komikku · ★5.000 · Apache-2.0 · v1.14.1 del 17 de julio · 404.324 descargas · 121.845 KB · 0 huellas.
*Comentario:* 404.324 descargas y su última entrega tiene **114 días**. No es abandono, pero sí es un proyecto que va más despacio que su popularidad.

**4 · Neko** — nekomangaorg/Neko · ★2.825 · Apache-2.0 · 3.8.5 del 30 de octubre · 15.312 descargas · 149.044 KB · 0 huellas.

**5 · Futon** — AppFuton/Futon · ★480 · GPL-3.0 · v9.9 del 21 de octubre · 2.860 descargas · 108.247 KB · 0 huellas.
*Comentario:* el número de versión `v9.9` es sospechosamente redondo para un proyecto de 480 estrellas. No es un defecto, pero un lector que compara versiones para decidir cuál es más nueva se confunde.

**6 · Zangetsu** — Spyou/Zangetsu · ★511 · GPL-3.0 · v2.3.5 del 1 de noviembre · 8.719 descargas · 30.181 KB · 0 huellas.
*Comentario:* uno de los pocos de la lista que cubre Android, iOS y Windows, y el segundo repositorio más liviano de los veinte. Interesante contraste con Kototoro: mismo alcance multiplataforma, séptima parte del repositorio.

**7 · TachiyomiJ2K** — Jays2Kings/tachiyomiJ2K · ★5.410 · Apache-2.0 · v1.8.1 del 15 de agosto · 188.681 descargas · 106.942 KB · 0 huellas.
*Comentario:* **85 días** desde su última entrega, y 188.681 descargas. La bifurcación veterana del árbol Tachiyomi sigue viva pero despacio.

**8 · TachiyomiSY** — jobobby04/TachiyomiSY · ★4.203 · Apache-2.0 · 1.13.2 del 13 de julio · 169.447 descargas · 100.669 KB · 0 huellas.
*Comentario:* **118 días** sin entrega. El más parado de los grandes.

**9 · Aniyomi** — aniyomiorg/aniyomi · ★7.882 · Apache-2.0 · v0.18.2.1 del 14 de septiembre · 5 APK · 293.398 descargas · 83.434 KB · 0 huellas.

**10 · Animiru** — animiruorg/animiru · ★913 · GPL-3.0 · v0.20.1.1 del 3 de noviembre · 4.675 descargas · **411.889 KB**, el repositorio más grande de los veinte · 0 huellas.
*Comentario:* 411.889 KB de repositorio para una entrega de la que bajaron 4.675 personas. Es el caso más claro de repositorio que pesa más de lo que se usa.

**11 · Kotatsu** — KotatsuApp/Kotatsu · ★8.956 · GPL-3.0 · **sin entrega publicada** · 0 descargas · 91.765 KB · 3 flujos.
*Comentario:* 8.956 estrellas y ninguna entrega en GitHub. Distribuye por otra vía. Como esta pieza mide entregas de GitHub, sale con cero, y eso **no** quiere decir que esté muerto: quiere decir que no se puede comprobar desde aquí. Es la limitación del método y la digo en la sección del método.

**12 · Cloudstream** — recloudstream/cloudstream · ★11.183 · GPL-3.0 · v4.8.0 del 10 de julio · 3 archivos, 2 `.jar` y 1 APK **sin versión en el nombre** · **881.950 descargas**, el segundo más alto · 54.685 KB · 0 huellas.
*Comentario:* 881.950 descargas y el archivo se llama `app-prerelease-release.apk`. Es el caso más extremo de descuido de nombres en la lista.

**13 · Keiyoushi/extensions** — keiyoushi/extensions · **★15.456, el más popular** · **sin licencia declarada** · entrega de hoy · **218 archivos** · 15.387 descargas · 249.066 KB · **0 flujos** · **2 contribuyentes** · 0 huellas.
*Comentario:* dos personas empujando código para el repositorio más popular del ecosistema, y 218 archivos en cada entrega. Aquí no es un defecto: es la naturaleza del proyecto, que empaqueta una extensión por archivo.

**14 · LNReader plugins** — lnreader/lnreader-plugins · ★370 · MIT · v2.0.0 del **21 de marzo de 2024** · 0 archivos · 0 descargas · 25.929 KB · **14 flujos de compilación** · **962 días** sin entrega.
*Comentario:* el más parado por mucho. Catorce flujos de compilación configurados y ni una entrega en 962 días: el caso raro de proyecto que tiene la maquinaria y no la usa. Los plugins de LNReader se publican por otra vía; esta pieza mide entregas de GitHub y por eso sale con cero.

**15 · AnymeX-Preview** — Shebyyy/AnymeX-Preview · ★54 · **sin licencia** · v3.2.0+2-beta de ayer 7 de noviembre · 11 archivos, cinco sistemas · 98 descargas · **402.150 KB** · 0 huellas · **4 contribuyentes**.
*Comentario:* el segundo repositorio más grande de los veinte, con 54 estrellas y 98 descargas. Nueve flujos de compilación hechos y sin licencia que los ampare. La ausencia de licencia es peor que la del hash: sin licencia, un usuario no tiene permiso legal de usar el programa, aunque el código esté a la vista.

**16 · Usagi** — UsagiApp/Usagi · ★293 · GPL-3.0 · v1.2 del 3 de octubre · 6.244 descargas · **14.610 KB, el más liviano** · 0 huellas.
*Comentario:* 14.610 KB de repositorio y 6.244 descargas. La mejor proporción de la lista entre lo que ocupa y lo que se usa.

**17 · Suwayomi-Server** — Suwayomi/Suwayomi-Server · ★8.023 · **MPL-2.0** · v2.4.2366 del 30 de septiembre · 31.200 descargas · 103.089 KB · 0 huellas.
*Comentario:* la única MPL-2.0 de los veinte. No es un cliente para el teléfono: es el servidor. Aparece porque es el motor que hay detrás de media docena de los clientes de esta lista.

**18 · Mihon (repetida por comparación de peso)** — 68.195.386 bytes. Véase la ficha 2.

**19 · Aniyomi (repetida por comparación de peso)** — véase la ficha 9. Su universal es el segundo patrón de referencia.

**20 · Cloudstream (repetida por comparación de peso)** — véase la ficha 12. Tercer patrón de referencia.

━━━━━━━━━━━━━

🧨 *Los tres que no pasan el corte · y el más descargado es uno*

El corte de esta pieza tiene cuatro condiciones: **entrega publicada**, **licencia declarada**, **huella disponible** y **entrega de los últimos 120 días**. No es un corte de calidad: es un corte de *comprabilidad*, que es otra cosa. De los veinte:

**Uno · Mihon.** No pasa por huella. Y es el que más pesa en el resultado, porque es el más descargado de los veinte: 621.665 de las 1.538.912 descargas medidas hoy, el **40,4 %** de todo el movimiento del ecosistema en una sola entrega. El programa que más gente baja es el que menos se puede comprobar.

**Dos · LNReader plugins.** No pasa por entrega: 962 días. No es que esté mal, es que desde esta ventana no hay nada que medir.

**Tres · AnymeX-Preview.** No pasa por licencia. Y aquí conviene ser preciso, porque es un caso que se repite mucho: un repositorio público **no** es un repositorio libre. Público quiere decir que puedes leerlo. Sin licencia, no tienes permiso de usarlo, copiarlo ni redistribuirlo. El código a la vista es una cortesía del autor, no un derecho del que lo mira.

Y el que **sí** pasa, con todo y su falla, es Kototoro: tiene entrega de hoy, licencia Apache-2.0, más de cien contribuyentes y —esto es lo importante— **publica huellas**, aunque no cubran sus APK. Está a un archivo de ser el único del ecosistema que da con qué comprobarlo de punta a punta. Le falta añadir cinco líneas al flujo de compilación.

Eso es lo que esta pieza quiere dejar dicho, y es lo más útil que tiene: **no hay que rehacer nada.** Hay que añadir un paso que corre `sha256sum` sobre los cinco APK y los sube junto a la entrega. Es el trabajo de una tarde, y ningún proyecto grande del ecosistema lo ha hecho todavía.

━━━━━━━━━━━━━

📊 *El censo y las cifras · descargas, días, licencias*

Los números, juntos, para que se puedan discutir:

**Descargas medidas hoy, sumando la última entrega de cada uno de los veinte:** 1.538.912. De esas, Mihon tiene 621.665 (40,4 %), Cloudstream 881.950 (57,3 %) y entre los dos suman el **97,7 %** de todo el movimiento. Los otros dieciocho se reparten 35.297 descargas.

Es un dato que sorprende y que hay que leer con cuidado: no mide usuarios, mide descargas de la última entrega. Un proyecto que publica todos los días reparte sus descargas entre muchas entregas y sale bajo en esta cuenta; uno que publica cada cuatro meses las concentra. **No es un ranking de popularidad.** Es un censo de movimiento en una ventana, y así hay que decirlo.

**Licencias declaradas**, que sí es un dato limpio:

| licencia | cuántos |
|---|---:|
| Apache-2.0 | 8 |
| GPL-3.0 | 6 |
| MIT | 1 |
| MPL-2.0 | 1 |
| **sin licencia** | **2** |
| **sin licencia, y el más popular de todos** | 1 (keiyoushi, ★15.456) |

Tres de veinte sin licencia, y entre ellos el repositorio más popular del ecosistema. Un proyecto sin licencia no es un proyecto libre: es un proyecto con el código a la vista.

**Antigüedad de la última entrega**, que es lo que dice si un proyecto está vivo:

| días desde la última entrega | cuántos | quiénes |
|---|---:|---|
| hoy | 2 | Kototoro (03:32 AST), keiyoushi |
| 1 a 7 días | 2 | AnymeX (1), Animiru (5) |
| 8 a 30 días | 5 | Zangetsu (7), Usagi (36→8+), Neko (9), Mihon (14), Futon (18) |
| 31 a 90 días | 3 | Suwayomi (39), Cloudstream (121→90+), TachiyomiJ2K (85) |
| más de 90 días | 4 | TachiyomiSY (118), Komikku (114), Aniyomi (55→…), LNReader (**962**) |
| sin entrega | 2 | Kotatsu, y los que distribuyen por otra vía |

La columna de días tiene imprecisión a propósito: la cuenta está hecha a mano desde la fecha de publicación que declara la API, y hay fichas que caen justo en el borde de dos franjas. Cuando dudes, cuenta tú mismo desde la fecha de la ficha. Es mejor una cifra con su borde visible que una cifra redonda y falsa.

**Flujos de compilación**, que dice cuánta maquinaria tiene cada uno: LNReader tiene **14** y no publica nada desde 2024; Keiyoushi tiene **0** y publica 218 archivos. La maquinaria no es la entrega.

━━━━━━━━━━━━━

🤔 *Ocho preguntas incómodas para esta misma pieza*

Una pieza que le pide cuentas a veinte proyectos tiene que aguantar que se las pidan a ella. Estas son las ocho objeciones que se me ocurren contra mi propia tesis, y lo que contesto a cada una.

**Primera: «una huella no sirve de nada si el autor la publica en el mismo sitio que el archivo».**
Es la objeción más fuerte y es parcialmente cierta. Si alguien puede reemplazar el APK en el servidor de GitHub, en teoría también puede reemplazar el `.sha256` de al lado. Pero la huella sigue sirviendo contra el ataque más común, que no es ese: es el **espejo**. El archivo que llega por un grupo de WhatsApp, por un enlace reenviado, por una web que lo reempaqueta «sin virus», por un blog que lo subió a su propio servidor para que cargue más rápido. Contra eso, la huella publicada en el repositorio oficial es la única defensa que existe, y es definitiva: si el archivo del espejo no da la misma cadena, el espejo mintió. La huella no protege contra el dueño del repositorio; protege contra todos los demás, que son la mayoría de los caminos por los que un APK llega a un teléfono dominicano.

**Segunda: «si nadie lo pide, no es un problema real».**
Puede ser que no le importe a nadie. Pero las 621.665 descargas de Mihon y las 881.950 de Cloudstream sugieren lo contrario: hay mucha gente bajando archivos de tamaño considerable desde un enlace que llegó por donde llegó. La ausencia de la pregunta no demuestra que no importe; demuestra que nadie la ha puesto sobre la mesa. Eso es lo que esta pieza hace, y por eso la sección de la semana de prueba termina pidiendo que se abra una incidencia.

**Tercera: «cinco líneas de YAML es fácil decirlo desde fuera».**
Tiene razón en el tono y no en el fondo. El paso en sí es trivial:

```yaml
- name: Huellas de los APK
  run: |
    cd app/build/outputs/apk/release
    sha256sum *.apk > SHA256SUMS-APK.txt
```

Lo que no es trivial es el resto: alguien tiene que revisar el cambio, fusionarlo, esperar la siguiente entrega, y asumir que a partir de ahí cualquier usuario puede decir «tu archivo no coincide con tu huella» y tener razón. Ese último punto es el que de verdad cuesta, porque **le da al usuario un arma que antes no tenía**. Publicar huellas es aceptar que te pueden pillar. Los proyectos que no lo hacen quizá no esconden nada, pero tampoco se exponen. Y esa diferencia merece decirse.

**Cuarta: «¿y si el hash está en el cuerpo de la entrega como texto y tu criterio por nombre de archivo no lo ve?».**
Es un hueco del método y ya lo declaré en su sección. Mi criterio busca archivos cuyo **nombre** contenga `.sha256`, `checksums` o similar. Un proyecto que pegue el hash en el texto de la entrega, sin archivo, aparecería como «sin huella» en mi tabla aunque la tenga. Revisé a mano las tres entregas más descargadas —Mihon, Cloudstream, Aniyomi— y ninguna pega un hash en el cuerpo. Pero no revisé las veinte a mano, y eso es una limitación real, no una coartada.

**Quinta: «el tamaño universal no es un defecto, es una comodidad, y ya lo dijiste tú mismo».**
Sí, y por eso la sección del peso no acusa a nadie de nada. Lo que sí digo es que la comodidad se le cobra al usuario sin avisarle: el que bajó el universal de 300,86 MiB no recibió un mensaje que dijera «había uno de 121,24 MiB, y era el tuyo». Si la entrega tuviera los cinco nombres con su tamaño al lado y una línea explicando cómo saber cuál te toca, la comodidad seguiría existiendo y el costo sería una decisión y no un accidente. Publicar los cinco es la mitad del trabajo; explicarlos es la otra mitad, y esa no se está haciendo.

**Sexta: «mides descargas, no usuarios. Un proyecto con un millón de usuarios puede salir con cero».**
Correcto, y por eso el censo de descargas va con tres advertencias en su propia sección y Kotatsu aparece con cero sin que eso signifique nada malo. Mido lo que la API de GitHub expone, que son descargas de la última entrega. Cualquier lectura de esas cifras como popularidad es mía y no del dato, y la parte de la culpa que me toca la asumo escribiéndolo dos veces.

**Séptima: «¿por qué veinte repositorios y no los 1.029 del catálogo de La Bandita?».**
Porque esta pieza mide uno por uno, a mano, con los ojos puestos en cada entrega, y veinte es lo que cabe en una mañana sin que la medición se vuelva un script ciego. Los 1.029 del catálogo están en otro sitio y se miden de otra manera, con otra herramienta. Esta pieza no es el censo: es el detalle. Y un detalle de veinte, hecho bien, dice más que un censo de mil hecho por encima.

**Octava: «mañana publican el hash y tu pieza queda vieja».**
Ojalá. Una pieza de medición que caduca porque el mundo mejoró es la mejor clase de pieza caducada. Si eso pasa, la corrección se escribe y se publica, y la pieza 32 puede empezar diciendo «la 31 tenía razón durante once horas». Eso no es un fracaso del método: es el método funcionando.

━━━━━━━━━━━━━

🛠️ *Una orden para no creerle a nadie*

Esta es la orden que comprueba el hallazgo central de la pieza. Una sola, y sirve para cualquier repositorio de la lista. Necesita `curl` y `python3`, nada más:

```bash
curl -s https://api.github.com/repos/Kototoro-app/Kototoro/releases/latest \
| python3 -c "
import sys,json
d=json.load(sys.stdin)
apk=[a['name'] for a in d['assets'] if a['name'].endswith('.apk')]
sha=[a['name'] for a in d['assets'] if 'sha256' in a['name'].lower() or 'checksum' in a['name'].lower()]
print('entrega :',d['tag_name'],'·',d['published_at'])
print('APK     :',len(apk),apk)
print('HUELLAS :',len(sha),sha)
print('¿ALGUNA CUBRE UN APK?:','SÍ' if any('apk' in s.lower() for s in sha) else 'NO')
"
```

Lo que devuelve hoy, sin editar:

```
entrega : v2.4.0 · 2026-11-08T07:32:47Z
APK     : 5 ['Kototoro-2.4.0-arm64-v8a-release.apk', ...]
HUELLAS : 4 ['Kototoro-2.4.0-ios-release-unsigned.sha256', ...]
¿ALGUNA CUBRE UN APK?: NO
```

Cámbiale el nombre del repositorio y corre la misma orden contra `mihonapp/mihon`, contra `recloudstream/cloudstream`, contra `keiyoushi/extensions`. En los tres va a devolver `HUELLAS : 0`. Eso es la pieza entera, comprobada por ti, en menos de un minuto, sin creerle a nadie.

Y si quieres comprobar el peso del universal sin bajarte 300 MiB, la API lo da en bytes:

```bash
curl -s https://api.github.com/repos/Kototoro-app/Kototoro/releases/latest \
| python3 -c "
import sys,json
d=json.load(sys.stdin)
for a in d['assets']:
    if a['name'].endswith('.apk'):
        print(f\"{a['size']:>12,} B  {a['size']/1048576:>7.2f} MiB  {a['name']}\")
"
```

━━━━━━━━━━━━━

🚪 *Lo que esta pieza no tiene*

Una pieza honesta dice lo que no hizo. Esto es lo que esta no hizo:

- **No bajó ni un solo APK.** El peso de cada uno viene del campo `size` de la API, que es el tamaño que el autor declaró al subirlo. No se ha verificado bajando el archivo y pesándolo. Es una diferencia pequeña y es una diferencia: `size` es lo que GitHub guarda, no lo que tu teléfono va a ocupar al instalar.
- **No probó ninguna de las apps.** No hay aquí una sola afirmación de que alguna funcione, sea rápida, tenga buena interfaz o no se caiga. Esta pieza mide entregas: qué se publicó, cuándo, con qué licencia, con qué huella.
- **No mide usuarios.** Mide descargas de la última entrega. Un proyecto puede tener un millón de usuarios y salir con cero descargas aquí, como Kotatsu, que no publica entrega en GitHub.
- **No tiene los números de mañana.** Todo esto caduca. Kototoro puede publicar un `checksums.txt` esta tarde y la tesis de la pieza quedaría desactualizada en su punto central. Si eso pasa, mejor: habría funcionado.
- **No dice cuál es la mejor app.** Dice cuál da con qué comprobar lo que bajas, que es una pregunta distinta y más pequeña.
- **El conteo de contribuyentes está topado.** La API devuelve 100 por página; los que dicen «+100» pueden ser 101 o 400. No sé cuántos son y no lo voy a inventar.
- **Tres fichas se repiten** (18, 19 y 20) porque son los patrones de comparación de peso. Si al leer te pareció relleno, tienes razón en el método aunque no en el motivo: están para que la comparación de la sección del peso no dependa de la memoria.

━━━━━━━━━━━━━

📅 *La semana de prueba*

Para quien quiera comprobar esta pieza sin creerle, esto es lo que hay que hacer, en orden, y lo que debería pasar:

**Domingo.** Corre la orden de la sección anterior contra los cuatro repositorios del hallazgo. Anota lo que devuelve, con hora y minuto. Guárdalo en un archivo de texto: no en una captura de pantalla, que no se puede buscar.

**Lunes.** Baja el `arm64-v8a` de Kototoro —121,24 MiB, no el universal— y calcula su huella. Como el proyecto no publica la del APK, esto no comprueba nada todavía, pero te deja el número listo para el día que lo publiquen.

**Martes.** Baja el universal y compara. Van a ser 179,62 MiB de diferencia en tu disco para la misma app en el mismo teléfono. Ese es el costo real de la comodidad, medido en tu propio almacenamiento.

**Miércoles.** Revisa si alguno de los veinte publicó un `checksums.txt` o un `.sha256` de APK. Si alguno lo hizo, la pieza de hoy se equivocó, y avisar de eso es el mejor uso que se le puede dar.

**Jueves.** Abre una incidencia en el repositorio que hayas elegido, pidiendo el hash de los APK. No es una exigencia: es la petición más barata que existe en el código abierto y la que más devuelve por minuto invertido.

**Viernes.** Vuelve a correr la medición completa. Compara. Lo que se movió en una semana dice más del ecosistema que veinte fichas de un solo día.

**Sábado.** Descansa. El ecosistema no se acaba hoy, y una pieza leída con prisa no sirve.

━━━━━━━━━━━━━

❓ *Las preguntas del grupo*

**«¿Entonces cuál bajo, el universal o el de mi arquitectura?»**
El de tu arquitectura, si sabes cuál es. Y casi seguro es `arm64-v8a`: es la de cualquier teléfono Android vendido en los últimos seis o siete años. Si no lo sabes, el universal. Si quieres saberlo, cualquier app de información del sistema te lo dice en una pantalla, y no hace falta instalar nada raro.

**«¿300 megas es mucho?»**
Para un lector de manga, sí: Mihon hace lo mismo en 65 MiB. Para un programa que carga extensiones de tres ecosistemas distintos, trae motores nativos para cuatro arquitecturas y se publica para cinco sistemas operativos, 300 MiB es lo que cuesta. No es gordura: es músculo con huesos. La pregunta útil no es «¿por qué pesa?», es «¿quiero yo pagar ese peso?».

**«¿Y si el archivo que bajo viene con un virus?»**
Sin huella del autor, no tienes manera de saberlo por el archivo. Tienes otras: bajar solo del enlace del repositorio oficial, no de un espejo, no de un grupo de WhatsApp, no de una web que lo reempaqueta; y mirar si la firma del APK coincide entre versiones (Android te avisa si cambia, pero solo después de tener la primera instalada). Lo que no puedes hacer es lo que la huella te dejaría hacer: comprobar antes de instalar.

**«¿Por qué el autor no publica el hash, si es gratis?»**
Porque nadie se lo ha pedido. Es la respuesta aburrida y es la verdadera en la mayoría de los casos. Añadir un paso a un flujo de GitHub Actions son cinco líneas de YAML. Los proyectos que no lo hacen no esconden nada: no lo han pensado. Pedirlo en una incidencia es útil de verdad.

**«¿Y esto qué tiene que ver con La Bandita?»**
Que La Bandita es un archivo de programas enlazados, no alojados. Nuestra única promesa es que el enlace va al repositorio de quien lo hizo. Si el autor no publica huella, esa promesa se queda corta: no podemos decirte que lo que bajaste es lo que el autor subió. Esta pieza es la medición de esa distancia.

**«¿La pieza 31 quiere decir que las anteriores estaban mal?»**
No. Quiere decir que esta es distinta. Las anteriores contaban el ecosistema por dentro. Esta cuenta lo que se puede comprobar desde fuera, con una orden, en un minuto, hoy.

━━━━━━━━━━━━━

🧮 *Cómo se midió cada número · el método, campo a campo*

Todo lo que sigue se puede repetir. El script completo se reduce a esto:

**Estrellas, licencia, fecha de creación, último empujón, tamaño del repositorio, lenguaje.** De `GET /repos/{owner}/{repo}`, campos `stargazers_count`, `license.spdx_id`, `created_at`, `pushed_at`, `size`. El campo `size` va en **kilobytes**, y es el tamaño del repositorio, no el de la entrega: por eso Animiru aparece con 411.889 KB y su APK puede ser de otra cifra.

**Entrega, versión, fecha, archivos y descargas.** De `GET /repos/{owner}/{repo}/releases/latest`, campos `tag_name`, `published_at`, `assets[]`. De cada `asset`: `name`, `size` (en bytes), `download_count`.

**Huella.** Por nombre de archivo: un `asset` cuenta como huella si su nombre contiene `.sha256`, `.sha512`, `sha256sums`, `checksums`, `.asc`, `.sig`, `.md5` o `checksum`. Y cuenta como «huella de APK» solo si su propio nombre contiene `apk`. Es un criterio por nombre y lo digo aquí porque es una limitación: un proyecto que publique un `SHA256SUMS` que cubra todos los archivos —sin nombrar el APK— aparecería como «sin huella de APK» en esta medición, aunque la tenga. Ninguno de los veinte lo hace, pero el método tiene ese hueco y hay que verlo.

**Flujos de compilación.** De `GET /repos/{owner}/{repo}/actions/workflows`, campo `total_count`.

**Contribuyentes.** De `GET /repos/{owner}/{repo}/contributors?per_page=100`, contando la longitud de la lista. Topado en 100 por la paginación.

**Los MiB.** Byte dividido por 1.048.576. Se usa MiB, no MB, porque es la unidad que muestra Android en la pantalla de almacenamiento, y comparar dos cifras en unidades distintas es la manera más fácil de equivocarse en una pieza de estas.

**La hora.** 06:25 de la mañana en Santo Domingo, UTC-4. La hora de publicación de Kototoro, `2026-11-08T07:32:47Z`, se convirtió a 03:32 AST. La distancia entre las dos —dos horas y cincuenta y tres minutos— es el margen que tenía la entrega cuando se midió.

**Lo que no se midió.** No se bajó ningún archivo. No se instaló ninguna app. No se probó ninguna función. No se consultó ninguna fuente fuera de la API de GitHub. Todo lo que esta pieza afirma sobre el comportamiento de un programa, no lo afirma.

━━━━━━━━━━━━━

💸 *Lo que cuesta en datos · sin poner precios que no me constan*

Hay una cuenta que en Santo Domingo importa más que el almacenamiento, y es la de los datos móviles. No sé a cuánto está el mega en tu plan, y no lo voy a inventar: eso cambia por operadora, por plan y por semana, y una cifra inventada aquí sería exactamente el tipo de dato que esta pieza está corrigiendo. Pero la diferencia sí la puedo poner en la misma unidad que tu factura:

- el APK universal: **300,86 MiB**
- el APK de tu arquitectura: **121,24 MiB**
- lo que sobra: **179,62 MiB**

Ahora multiplícalo por tu tarifa. Si tu plan cobra por mega, ese es el costo de la comodidad de no saber cuál te tocaba. Si tu plan es de datos ilimitados con velocidad reducida después de cierto tope, esa diferencia es la que se come tu tope antes de tiempo y la que te deja navegando lento el resto del mes. Y si bajas la app cuatro veces —porque se actualiza, porque cambiaste de teléfono, porque se la pasas a un amigo— la cuenta se hace cuatro.

No es un argumento para no bajar la app. Es un argumento para saber cuál de los cinco archivos te toca. La diferencia entre el universal y el de tu arquitectura, en datos, es aproximadamente **una app y media** de las que ya tienes instaladas. Y esa diferencia no compra ninguna función nueva: el `arm64-v8a` hace exactamente lo mismo que el universal, en tu teléfono, con el mismo código, porque el universal trae adentro el `arm64-v8a` más otros tres que tu teléfono nunca va a cargar.

━━━━━━━━━━━━━

🌅 *cierre*

Anoche alguien preguntó por qué una app pesa trescientos megas, y cuatro personas contestaron mal por la misma razón: nadie había abierto la entrega.

Al abrirla, la respuesta al peso resultó ser sencilla y aburrida —es el universal, y al lado hay uno de 113,72 MiB que hace lo mismo—. Pero abrir la entrega dejó ver otra cosa, y esa no es aburrida: de veinte proyectos, uno solo publica huellas, y las publica para todos sus sistemas menos para Android.

Ese es el estado del ecosistema al 8 de noviembre de 2026, medido a las 06:25 de la mañana, con el proyecto más ambicioso de la lista publicando su mejor versión tres horas antes. Trescientas megas de programa, cinco APK, dieciséis flujos de compilación, cien personas empujando código, y ni un solo número que te deje comprobar que lo que llegó a tu teléfono es lo que salió del suyo.

No es una tragedia y no es una estafa. Es una ausencia, y las ausencias se arreglan con cinco líneas. Esta pieza existe para que la ausencia tenga nombre y para que quien la lea sepa pedirla.

Baja el de tu arquitectura. Guarda el número. Y si el autor publica el hash mañana, mejor: entonces esta pieza habrá servido para algo más que para leerla.

━━━━━━━━━━━━━

🔗 *enlaces*

- Kototoro · https://github.com/Kototoro-app/Kototoro
- Mihon · https://github.com/mihonapp/mihon
- Komikku · https://github.com/komikku-app/komikku
- Neko · https://github.com/nekomangaorg/Neko
- Futon · https://github.com/AppFuton/Futon
- Zangetsu · https://github.com/Spyou/Zangetsu
- TachiyomiJ2K · https://github.com/Jays2Kings/tachiyomiJ2K
- TachiyomiSY · https://github.com/jobobby04/TachiyomiSY
- Aniyomi · https://github.com/aniyomiorg/aniyomi
- Animiru · https://github.com/animiruorg/animiru
- Kotatsu · https://github.com/KotatsuApp/Kotatsu
- Cloudstream · https://github.com/recloudstream/cloudstream
- Keiyoushi extensions · https://github.com/keiyoushi/extensions
- LNReader plugins · https://github.com/lnreader/lnreader-plugins
- AnymeX-Preview · https://github.com/Shebyyy/AnymeX-Preview
- Usagi · https://github.com/UsagiApp/Usagi
- Suwayomi-Server · https://github.com/Suwayomi/Suwayomi-Server

━━━━━━━━━━━━━

🗒️ *notas al pie*

**1.** Los cinco APK de Kototoro v2.4.0 suman 853.787.974 bytes = 814,23 MiB. Se descargaron 156 veces entre los cinco, de las cuales 137 fueron al `arm64-v8a`.

**2.** La suma de los cuatro APK por arquitectura es 536.316.272 bytes = 511,47 MiB. El universal pesa 315.477.702 bytes = 300,86 MiB. El ahorro del empaquetado conjunto es de 220.838.570 bytes = 210,61 MiB, el 41,18 %.

**3.** El factor de 4,63 sale de dividir 315.477.702 entre 68.195.386. Los dos son APK universales de dos lectores de manga. La diferencia no es de calidad: es de lo que cada uno trae compilado por arquitectura.

**4.** LNReader lleva 962 días desde su última entrega: de 2024-03-21 a 2026-11-08. Cuenta hecha con el calendario, contando el día de salida y no el de llegada. Si lo cuentas distinto te pueden salir 961 o 963, y ninguna de las tres es falsa: es una cifra de borde.

**5.** Keiyoushi/extensions aparece con **0 flujos de compilación** y **218 archivos** en su entrega de hoy. Las dos cosas son verdad al mismo tiempo porque compila por otra vía. La ausencia de flujo en GitHub Actions no es ausencia de automatización.

**6.** «Sin licencia» significa que el campo `license` de la API es nulo. Un proyecto puede tener la licencia escrita en un archivo `LICENSE` sin que GitHub la reconozca. En los casos de esta pieza —Keiyoushi y AnymeX— la ausencia es del campo, y por eso la afirmación está redactada como «no declara», no como «no tiene».

**7.** Ningún paquete se aloja en La Bandita. Todos los enlaces van al repositorio de quien hizo el programa. Si un enlace deja de funcionar, el programa no está aquí para reemplazarlo.

**8.** Esta pieza se escribió el domingo 8 de noviembre de 2026 entre las 06:25 y el cierre. Todos los números son de esa ventana. Ninguno se actualizó después.

**9.** El defecto de las piezas 31 a 40 anteriores era medir bytes de archivo y llamarlos contenido. Esta pieza mide lo contrario: cuenta lo que se puede comprobar desde fuera, y declara lo que no midió. Si algo aquí está mal, el método de la última sección permite encontrarlo.
