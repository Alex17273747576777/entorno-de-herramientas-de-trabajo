# cerox-investigacion — estado

Última actualización: 2026-11-12, tras convertir lo aprendido en **reglas ejecutables**
(`reglas/`, 21 hoy), publicar dos de ellas como puertas de CI (`b79e3941` y `6cb3f85a`,
475 pruebas), retirar 20 comentarios que eran ruido en hilos ajenos, cerrar 3 issues que
su propio cuerpo ya mandaba cerrar, dejar línea de retirada en otras 43, publicar la
1.0.3 con la nota derivada ejecutada por fin en el corredor, respaldar el keystore fuera
de GitHub, ver la app arrancar y navegar en el V60 ThinQ 5G, y cortar la 1.0.4 en dos APKs por arquitectura: universal sin motor ONNX y arm64 con él.

## Lo que hay aquí

Los generadores de los commits publicados. Se quedan porque documentan **qué se
publicó y con qué comprobaciones**, no porque hagan falta para volver a hacerlo: el
código está en `main` y cada commit lleva su mensaje largo explicando el porqué.

| guion | commit | qué publicó |
|---|---|---|
| `h_commit.py` | `917c3f06` | reproductor media3, traducción de `#EXTVLCOPT`/`#KODIPROP`, módulo `iptv` registrado, media3 1.11.1 |
| `h_fix.py` | `c7815891` | `createMediaSource`, que `createMediaItem` no existe |
| `h_fix2.py` | `708a9904` | las fuentes al almacenamiento externo, y la prueba que defendía el fallo |
| `i_textos.py` + `i_commit.py` | `f11a1b7a` | la pantalla IPTV, 3 layouts, 22 cadenas × 15 idiomas, el destino de la barra |
| `j_commit.py` | `ff3e1404` | versión 1.0.2-beta y el título de la release derivado de su etiqueta |
| `k_commit.py` | `b79e3941` | `CoherenciaDePruebasTest`: ninguna prueba puede exigir lo que el proyecto prohíbe |
| `l_commit.py` | `1d592c6b` | 4 verdades viejas del repo + `entorno/COMPILAR-Y-FIRMAR.md`; **publicó `apk.yml` roto** |
| `l_fix.py` | `6cb3f85a` | la sangría del flujo + `FlujosValidosTest`: ningún flujo del repo puede colgar fuera de su bloque |
| `m_commit.py` | `329c7059` | 1.0.3-beta-notas: versionCode 8 y el `universal` ofrecido en el selector del flujo |
| `o_commit.py` | `56c95a28` | 1.0.4-beta-dos-apks: universal sin motor ONNX, nativos comprimidos, puerta `MotorOnnx` |
| `p_commit.py` | `d208af2f` | cierra la contradicción entre `ArranqueHonestoTest` y `MotorOnnxTest` |
| `revisar_issues.py` | — | reutilizable: recorre las issues de la cuenta y marca las que tienen comentarios sin responder |

Todos se ejecutan igual: `export GP=<token>` y `python3 -B <guion> --run`. Sin `GP`
no publican. Ojo: `h_commit.py` en modo seco lee un árbol local que ya se borró, así
que ese en concreto sólo funciona con `--run`.

## `reglas/` — las reglas ejecutables

No es documentación: es un **registro de reglas con código que las comprueba**. Cada
regla guarda cuatro cosas y sin las cuatro no entra:

- el **incidente** que la produjo (commit, fichero, línea, qué se rompió);
- el **contra**, o sea qué se hace en vez de lo que se hizo mal;
- una **función que comprueba** el contra sobre texto real;
- una **muestra mala** (la función tiene que cazarla) y una **buena** (tiene que
  dejarla pasar). Si una regla no caza su propio incidente, no es una regla: es una
  opinión.
- y su **línea de evolución**: cada vez que la regla muerde de nuevo se apunta qué se
  le añadió, con fecha. Así una regla no se congela el día que nace.

```
cd reglas && python3 -B pruebas_reglas.py [--arbol RUTA]
```

Sale verde hoy: **23 reglas · 23 temas · 7 literales prohibidos registrados en 5
temas · 56 líneas de evolución** (cifras de la última línea del propio ejecutor, no
contadas a mano). Ejecuta cuatro cosas: las muestras malas y buenas de cada regla,
una auditoría del árbol publicado (`R1`, `R5`, `R6`, `R11`, `R12`, `R13`), el
espacio de trabajo (nada re-descargable guardado) y la **autoaplicación** (que este
registro no cite lo que prohíbe, que es exactamente el fallo que lo originó).

| regla | tema | de qué incidente viene |
|---|---|---|
| R1 | La prosa describe, no cita | seis veces: un comentario que explicaba un arreglo nombraba el método inventado y la puerta disparaba contra la explicación |
| R2 | El ámbito de una puerta nueva se decide | `latest.release` en el comentario de `build.gradle`; y el modo espejo para las que imitan a una prueba publicada |
| R3 | Los nombres de API se comprueban | `createMediaItem` no existe en media3: `c7815891` tras un rojo en CI |
| R4 | Una prueba no puede exigir lo prohibido | `IptvReproductorTest` exigía el directorio interno con un mensaje que decía lo contrario de la regla |
| R5 | Censar las pruebas publicadas antes de escribir | `ReglaDeAlmacenamientoTest` llevaba semanas publicada y nadie la leyó |
| R6 | Cadenas crudas de Kotlin: mirar el valor evaluado | escapes perdidos entre dos capas de Python |
| R7 | El hilo de fondo no toca vistas ni APIs del Looper | ExoPlayer lanza desde un hilo ajeno |
| R8 | Las cuentas esperadas se derivan, no se escriben a mano | 15/4 ids de layout cuando eran 16/5 |
| R9 | Sospechar del fixture, reproducir la lógica, nunca relajar | dos fixtures mal escritos en `ecaae4f4` → 455 · 2 |
| R10 | Toda ancla se cuenta antes de sustituir | anclas que paraban pronto y empalmaban en otro ámbito |
| R11 | Los datos van a los mecanismos aprobados | `708a9904`: las fuentes al almacenamiento externo |
| R12 | Una cadena nueva son 15 entradas | 22 claves `iptv_*` × 15 idiomas, marcadores `%1$d`/`%2$s` iguales |
| R13 | Los ids de layout se cruzan en los dos sentidos | el id muerto que se borró en vez de leerse |
| R14 | Nada de «funciona» sin evidencia | el barrido de fabricación: 45 sitios que inventaban éxito |
| R15 | Nada re-descargable se guarda | `logs/` y el APK descargado: borrados tras verificar |
| R16 | Los símbolos se cuentan con un escáner | tres falsos positivos de balance en un día |
| R17 | En un hilo ajeno, o se aporta un dato o no se comenta | `komikku#892`: un cierre de cortesía en una issue cerrada en 2025, y la respuesta de un colaborador |
| R18 | Un mandato «cada uno» se censura antes de ejecutarse | la tanda de 48 respuestas se publicó informando del total, sin decir que 31 iban a hilos cerrados |
| R19 | Un guion que escribe fuera se puede volver a ejecutar | un `KeyError` reventó el lote de retiradas **después** de la primera edición publicada |
| R20 | Un flujo se valida como YAML antes de publicarlo | `1d592c6b` publicó `apk.yml` con una línea en la columna 0 dentro de un bloque: GitHub lo reportó como un run fallido **sin ningún job** |
| R21 | Un paso que la prueba no ejecuta se ejecuta en un repo de juguete | el arreglo cayó en el paso de publicar, que sólo corre con `publicar=true`, y el despacho de comprobación fue con `false` |
| R22 | Un bucle de espera distingue «todavía no» de «la llamada falló» | una ventana de 401 del token y cincuenta iteraciones mudas que no dijeron que lo caído era la credencial |
| R23 | Quien mueve un literal de sitio busca quién más lo lee | `ArranqueHonestoTest` escaneaba los módulos por el literal ONNX que O movió detrás de la puerta: main quedó en rojo y la 1.0.4 se cortó así |

## La retirada del 2026-11-12

Un colaborador de komikku contestó a un comentario de la cuenta en la issue #892,
cerrada en 2025, con un «deja de poner basura en issues viejas que no se van a
implementar». Tenía razón en el patrón, no sólo en ese hilo: de los 48 comentarios
publicados el día anterior, **31 iban a issues cerradas y 25 de ésas ya tenían
respuesta del mantenedor**.

No se contestó. Contestar a «deja de comentar» con otro comentario es hacer justo lo
que piden que se deje de hacer; se cumple en el mismo medio —silencio en el hilo— y se
cambia la conducta. Lo que se hizo fue retirar lo añadido a hilos muertos: **20
comentarios borrados en 15 repositorios**, comprobado uno a uno releyéndolos después
(los 20 dan 404) y releído el hilo del incidente (0 comentarios de la cuenta).

El criterio no fue «los cerrados», fue `merece_respuesta()`: hilo cerrado **y** ya
respondido por el mantenedor **y** nada nuestro pendiente **y** el texto sólo retirando
o agradeciendo. Los otros 28 se quedaron porque corrigen una publicación nuestra que
sigue en pie o contestan a algo dirigido a la cuenta. En los dos hilos donde quedaba un
comentario antiguo de la cuenta se leyó antes de dar por buena la retirada: en
`namida#1105` el registro ya estaba enmendado desde julio (el análisis largo se editó)
y en `yokai#288` era la respuesta original de 2024. Lo que se borró fue sólo la
adición tardía.

Los 20 textos están en `comentarios-retirados.json`. No son re-descargables —ése es
justo el motivo de guardarlos—, así que si se quiere volver a publicar alguno, se puede.

### Lo que el censo dijo después, y por eso no se editaron 113 cuerpos

Se ofreció editar las issues viejas para dejar arriba una línea de retirada, y antes de
hacerlo se censaron: **131 issues de la cuenta, 113 en repos ajenos — 36 abiertas y 77
cerradas**. El censo desmontó la oferta:

- todo el texto enorme (hasta 63.862 caracteres) está en las **77 cerradas**. Sus
  mantenedores ya las dispusieron; editarlas sería tocar 77 hilos muertos, que es
  exactamente lo que se acababa de reprochar;
- de las 36 abiertas la más larga es de 2.688 caracteres y es una de las tres peticiones
  de licencia. Los cuerpos gigantescos ya no están abiertos, y bastantes ya fueron
  reescritos en una ronda anterior a peticiones estrechas y revisables.

O sea que la acción prometida era mayormente innecesaria, y decirlo vale más que
ejecutarla. Lo que sí estaba en pie eran tres issues abiertas cuyo **propio cuerpo** ya
las mandaba cerrar, y se cerraron (comprobado releyendo: estado, motivo y línea arriba):

| issue | motivo | por qué |
|---|---|---|
| `komikku-app/komikku#1529` | `not_planned` | su cuerpo decía que un mantenedor preguntó si debía cerrarse «y la respuesta es sí» |
| `salmanbappi/AniZen#69` | `duplicate` | su cuerpo decía que estaba sustituida por #12 |
| `komikku-app/komikku#1321` | `duplicate` | mismo asunto que #1538 después del aclarado del mantenedor |

Los tres cuerpos originales están en `issues-editadas.json`, que tampoco es
re-descargable una vez editados. ### Las 77 cerradas: 43 sí, 34 no, y el censo decidió cuáles

Se ofreció dejarlas como estaban y se ofreció también editarlas. Antes de elegir se
censo por **motivo de cierre y por quién cerró**, que es lo que decide si una retirada
es verdad o es mentira:

| | cuántas | qué se hizo |
|---|---|---|
| cerradas como `completed` **por un mantenedor** | 18 | **nada.** Ahí sí se hizo algo con la petición; poner «retirada, no hace falta nada» encima sería falso |
| cuerpo pequeño (≤ 3.000 caracteres) | 29 | **nada.** Una issue corta no es una pared de texto generado |
| resto, con cuerpo grande y sin línea de retirada | **43** | **editadas**: la línea arriba, el cuerpo original intacto debajo |

Las 43 sumaban **728.171 caracteres** de texto generado por máquina todavía visibles y
buscables en repos ajenos (la mayor, `Kototoro#206`, 63.862). Se reparten en 10
repositorios; 40 líneas van en inglés y 3 en francés, que es el idioma del repo.

**Comprobado releyendo una por una, carácter a carácter:** en las 43 el cuerpo es
exactamente `línea + separador + original`, y las 43 siguen cerradas con su motivo.

El dato que ayer dije sin comprobar y ahora sí: **editar el cuerpo de una issue no
notifica a nadie** —sólo notifica crear un comentario, y añadir una *@mención nueva*
dentro de una edición—. Las líneas no llevan ninguna mención, así que fueron 43
correcciones de un registro público y 0 notificaciones. Fuentes:
[stackoverflow 38986589](https://stackoverflow.com/questions/38986589),
[ReviewNB/support#58](https://github.com/ReviewNB/support/issues/58),
[JN0V/workline#426](https://github.com/JN0V/workline/issues/426).

Los 43 cuerpos originales están en `issues-editadas.json` (821 KB). Después de editar
ya no se pueden descargar, que es el único motivo por el que se guardan.

### El flujo que se publicó roto: R20 y R21, y van 49 líneas de evolución

- **R20 nace aquí.** El commit L (`1d592c6b`) publicó `apk.yml` con la continuación de
  una sustitución de mandato en la columna 0, dentro de un bloque `run: |` que pedía
  diez espacios de sangría. GitHub no dijo nada útil: creó un run con el nombre en forma
  de ruta, `conclusion: failure` y **cero jobs**; `/jobs` devolvió `[]` y `/logs` y las
  anotaciones, 404. Al lado, las 472 pruebas salían en verde —ninguna prueba de JVM lee
  un flujo y el compilador no lo ve—, así que `main` estuvo roto para ese flujo mientras
  todo lo demás decía que estaba bien. La única manera de encontrar la línea fue bajar el
  fichero publicado y parsearlo: «línea 162, columna 1».
- Contra: `yaml_valido()` y `bloques_literales()` en `reglas/motor.py`, probadas **contra
  el fichero roto de verdad** antes de darlas por buenas —una puerta que no acusa al
  fichero que la originó es decoración—. La segunda no depende de ninguna biblioteca y
  dice la línea exacta donde algo cuelga fuera de la sangría de su bloque. Y si falta la
  biblioteca de YAML, `yaml_valido` levanta `ImportError` en vez de devolver «todo bien»:
  una comprobación que no se ejecutó no puede decir que pasó.
- **R21 nace del arreglo.** Las líneas corregidas viven en el paso «Publicar la release»,
  que sólo corre con `publicar=true`; el despacho de comprobación fue con `publicar=false`,
  así que el flujo arrancó en verde sin ejecutarlas nunca. Se sacó el guion del YAML **ya
  evaluado** y **por nombre de paso** —no por índice, que es como falló el primer
  intento—, se le pasó `bash -n` y se ejecutó en un repo de juguete con dos etiquetas: la
  lista de cambios se construyó de verdad antes de publicar. Porque un YAML válido no dice
  nada del shell que lleva dentro: una comilla sin cerrar pasa el YAML y revienta en el
  corredor.
- **Una puerta propia falló por no imitar bien a la que imita.** El pre-vuelo de L
  reproducía `PlaceholderDetectorTest` y partía el fichero por un nombre de lista que no
  existe (`formasDeExceso` en vez de `formasDeExito`), así que se quedó el fichero entero
  y puso «return true» entre las *marcas*, acusando a un `VideoModule.kt` correcto.
  Contra: imitar al cazador publicado entero —las líneas que se salta, la ventana de tres,
  la regla de *combinación* y sólo las rutas que recorre— y afirmar que el parser leyó lo
  que cree que leyó.
- **R8 mordió tres veces más, siempre del mismo lado.** Las comprobaciones de escapes de
  `l_fix.py` esperaban seis `\$` cuando el texto llevaba cinco, `(\s|$)` cuando lleva
  `(?:\s|$)`, y `"\$X"` cuando en Kotlin va `\"\$X\"`. Los tres fallos decían que el
  contenido estaba mal estando bien. La forma esperada se deriva ahora del valor evaluado
  del bloque que se va a publicar, no de un literal escrito a su lado.

### La ventana de 401: R22, y van 50 líneas de evolución

- El token fino tuvo una ventana mala de unos veinticinco minutos justo entre el commit
  N y su despacho: el `POST` del dispatch devolvió 401, y el bucle de vigilancia pedía
  los runs del commit y leía `workflow_runs` sin mirar el estado de la respuesta. Con el
  401 el cuerpo no traía la clave, el python del bucle moría en cada vuelta y el bucle
  imprimió cincuenta líneas vacías seguidas sin decir nunca que lo caído era la
  credencial y no la espera. El run de pruebas del commit terminó en verde sin que nadie
  lo viera, porque el bucle miraba otra cosa.
- Contra: `sondeo_sano(status, cuerpo, claves)` en `reglas/motor.py`. Estado distinto de
  200 es un fallo y se dice; cuerpo sin las claves esperadas es un fallo y se dice con el
  `message` que traiga. Un bucle que no distingue «todavía no» de «la llamada falló»
  convierte una credencial caída en silencio.
- Y de regalo, el primer intento de esa función diagnosticó mal su propia fixture buena:
  `motor.py` no importaba `json`, el `NameError` cayó dentro del `except` y un cuerpo
  válido salió dicho como «no es JSON». Una puerta que se equivoca de diagnóstico es peor
  que ninguna, porque se la cree uno. Los 403 anónimos por rate-limit que vinieron
  después, en las vigilancias largas, ya los atrapó esta misma distinción: el bucle los
  dijo en vez de tragárselos.

### Dos pruebas que se contradecían: R23, y van 56 líneas de evolución

- El commit O movió la creación del entorno ONNX detrás de `MotorOnnx.entorno()`, y con
  eso rompió un contrato publicado que su pre-vuelo no censó: `ArranqueHonestoTest`
  escanea los siete módulos buscando el literal y exige `by lazy` en la misma línea.
  Main quedó en 478 · 1 y la release 1.0.4 se cortó de un commit rojo. El pre-vuelo de O
  censó la prueba que lee el flujo y no las que leen los ficheros reescritos: el censo
  miraba lo famoso y no lo tocado.
- El commit P cerró la contradicción sin relajar ninguna de las dos intenciones: la
  prueba vieja ahora escanea la llamada a la puerta y sigue exigiendo el `by lazy`, y
  añade que el literal a pelo ya no está; la nueva sigue exigiendo que nadie cree el
  entorno fuera de la puerta. Y el pre-vuelo estrenó `lectores_de_literal()` (R23), que
  al primer uso encontró al lector que O no vio **y** señaló a un consumidor que no
  necesitaba nada (`ModelosEjecutadosTest`, que crea su entorno para ejercitar
  modelos): de ese mordisco salió la división entre escaneadores —literal entre
  comillas, acoplados— y consumidores —literal como código, sueltos—.

### Las dos mordeduras de la tanda de issues

- **R8 mordió en la comprobación, no en el código.** Verifiqué las 43 ediciones con una
  longitud esperada escrita a mano —«línea + 5 + original»— cuando el separador tiene 7
  caracteres. Las 43 dieron fallo siendo correctas. La constante se deriva en el código
  que escribe **y** en el que comprueba.
- **R19 nace aquí: un guion que escribe fuera se puede volver a ejecutar.** El lote de
  retiradas leía un campo de un censo guardado antes de empezar; el campo no existía y
  reventó con `KeyError` **después** de publicar la primera edición. Una issue quedó
  escrita y sin registrar, y al reejecutar se habría editado dos veces. El contra: leer
  el estado vivo antes de cada escritura y comprobar el guion idempotente, que es lo que
  hace `idempotente()` en `reglas/motor.py`.

## Lo que ya no depende de que yo me acuerde

**R4 está publicada como prueba del repo** (`b79e3941`, `CoherenciaDePruebasTest`,
4 `@Test`, run `43128193456` verde con **472 · 0 · 0 · 6**). Lleva una tabla de 9
prohibiciones, cada una con su porqué y su incidente; comprueba que ninguna está en el
**código** de su ruta, que **ninguna prueba publicada exige** su presencia, que la
propia prueba no escribe los literales que prohíbe (los compone a trozos y se comprueba
contra sí misma) y que cada prohibición está explicada. La comparación es por
**palabra**, no por subcadena: dos mecanismos aprobados —el almacén cifrado de tokens y
el método que migra las preferencias viejas— llevan dentro el nombre de lo prohibido y
por subcadena se habrían denunciado, haciendo nacer la prueba en rojo.

**R20 también** (`6cb3f85a`, `core/FlujosValidosTest`, 3 `@Test`, run `43134156604`
verde con **475 · 0 · 0 · 6**): recorre `.github/workflows/*.yml` y no deja que ninguna
línea cuelgue fuera de la sangría del bloque donde empezó, que es exactamente lo que
rompió `main` en el commit anterior. No usa ninguna biblioteca de YAML —no la hay en el
classpath de las pruebas—: reimplementa la regla de sangría en Kotlin. Y afirma primero
que encuentra al menos dos flujos, porque un recorrido que no encuentra ficheros no
encuentra culpables y daría verde en un repo vacío. La tercera prueba lleva dentro el
fallo exacto del commit L con su muestra buena al lado, así que si alguien la relaja se
ve.

## Estado publicado (verificado, no supuesto)

`main` = `d208af2fac6575cfc41d140d89addb93b3079461`. Pruebas: **478 · 0 fallos ·
0 errores · 6 saltadas** (run `43199644577`). Cadena: `6cb3f85a` (475) → `329c7059`
(475) → `56c95a28` (478 · **1 en rojo**: dos pruebas publicadas se contradecían) →
`d208af2f` (478 · 0).

Release **v1.0.3-beta-notas** (id 442417941, run `43139712170`, con el paso «Publicar
la release» en **success** por primera vez en la historia del repo): `app-release.apk`
de 33.020.136 bytes, SHA-256 `823285ea24907516e1d9ac29c35ac6bed23afea6cfd81cdfe115ef7541b14da1`,
misma huella de certificado que la 1.0.1 y la 1.0.2, o sea que actualiza en el sitio.
Su cuerpo lleva la nota derivada del historial —«Cambios desde v1.0.2-beta-iptv-eq:» y
los cuatro commits con su punto—: las líneas que `6cb3f85a` arregló se ejecutaron por
fin en el corredor y lo que produjeron es lo que se publicó.

Release **v1.0.4-beta-dos-apks** (id 442768462): un APK por arquitectura, decisión
tomada en consulta. `app-universal.apk`, **16.841.870 bytes**, cuatro ABIs
(arm64-v8a, armeabi-v7a, x86, x86_64) y **ningún .so de ONNX**; `app-arm64-v8a.apk`,
**21.487.795 bytes**, con el motor pero comprimido: los 16,03 MB de
`libonnxruntime.so` que en la 1.0.2 viajaban sin comprimir ahora viajan en 5,54.
SHA-256 del universal `c3b033732ac170a1f3ba19175458f11362773a727700f473b7a85c234cc4693b`
y del arm64 `fd558815c5055e690d3346f35b0bd8054021b58ed6ab722d72e761b5ef05fa58`, ambos
recortados de `d208af2f` después de que el primer corte, de `56c95a28`, saliera con el
suite en rojo: el cuerpo de la release lo cuenta con sus propias palabras.

El flujo `apk` se despachó sobre este `main` con `publicar=false` (run `43134550385`,
**success**): construyó y firmó el APK desde `6cb3f85a` —`BUILD SUCCESSFUL in 4m 22s`,
33.020.129 bytes, huella del certificado `6626f635…273a19` igual a la esperada, 0
modelos `.onnx` dentro, 1 firmante RSA de 4096— y el paso «Publicar la release» quedó
**skipped**, así que no hay release nueva: siguen siendo las dos de abajo. Ese run es la
prueba de que GitHub ya lee el fichero; las líneas corregidas viven en el paso que se
saltó, y ésas se probaron aparte, en un repo de juguete (R21).

Aviso nuevo y benigno en la compilación de pruebas: `FlujosValidosTest.kt:38:17 Java
type mismatch: inferred type is 'java.io.File?'` — la misma familia que el que ya daba
`CoherenciaDePruebasTest.kt:49:17`, y viene de que `File.listFiles()` es una API de Java
con tipo de plataforma. Es un `w:`, no un error: los dos ficheros compilaron y las 475
corrieron.

**En dispositivo, por fin.** El 2026-11-11 entre las 21:07 y las 21:08 (hora de Santo
Domingo) la 1.0.2 corrió en el V60 ThinQ 5G: nueve capturas muestran el panel con **37
de 38 módulos listos · 1 perezoso · 0 fallidos** leídos del gestor en el momento, la
pantalla de diseño con las tres paletas y el aviso de que el desenfoque no existe, los
modos, el booru y el catálogo vacíos **diciendo que están vacíos**, y el IPTV con su
superficie negra y «Sin reproducción» porque no hay ninguna fuente instalada. Los
diagnósticos reportan QuickJS 0.9.2 respondiendo en 3 ms, 21 sitios de almacenamiento
conformes con 3 por migrar, y ningún gestor de privilegios usable. Lo que las capturas
**no** prueban: que el ecualizador suene, que un vídeo se reproduzca o que una fuente
cargue —nada de eso se ejercitó—. Es la primera vez que la app se ve viva fuera de la
JVM, y a la vez la mejor medida de lo vacío que está el cascarón.

**Keystore respaldado fuera de GitHub.** `cerox-2026-keystore.p12` vive ahora también en
Google Drive (id `14lz25dplSQz-hKwRvyaz9xZjg1KmDhMo`), cotejado por MD5
(`b3020b3ab3f86c134c06f81e6e8e965c`, idéntico al local) y por tamaño (4.245 bytes) sin
pasar los bytes de la clave por esta conversación. El PKCS12 va protegido por su
contraseña y la contraseña **no** está en Drive: sigue sólo en `~/.cerox-keys/.pass`.
Quien tuviera el Drive sin esa contraseña no puede firmar.

**De qué pesa lo que pesa.** Medido sobre el APK de la 1.0.2 (33,0 MB): **53,7 %
bibliotecas nativas y 40,1 % DEX**; recursos, 1,2 %. Dentro de las nativas, un solo
fichero —`lib/arm64-v8a/libonnxruntime.so`, 15,7 MB guardado **sin comprimir** para que
el sistema lo mapee directo del APK— es la mitad del APK entero, con cero modelos
`.onnx` dentro: el motor de una IA que hoy no tiene modelos que cargar. El DEX lleva la
firma de `material-icons-extended`. `minifyEnabled` y `shrinkResources` ya están
activados desde hace meses: lo que queda no es grasa de configuración, es contenido.
La decisión, tomada en consulta: el universal se publica **sin** el motor y el de
arm64 **con** él, y desde la 1.0.4 cada release acumula un APK por arquitectura con su
nombre y su suma. Medido, no estimado: el universal quedó en 16,8 MB y el de arm64 en
21,5 MB, frente a los 33,0 MB de la 1.0.2.

Release `v1.0.2-beta-iptv-eq` (id 442334285), construida por el flujo `apk` en el run
`43125112241` sobre `ff3e1404`:

- `app-release.apk` — **33.020.137 bytes** (31,5 MiB)
- SHA-256 `e1a617e954f1d11d02e5c7a8e754a0b2a23c3852012e8aa37d3149cdb820cda5`
- Firmado con nuestra clave: huella del certificado extraída del propio APK
  `6626f635443cd189851b793a9cda43eb1f81ebacdf2519e48cc0ab417e273a19`, igual a la de
  `entorno/HUELLA-CERTIFICADO.txt` y a la del keystore local. Certificado
  `CN=cero-X, O=La Bandita, L=Santo Domingo, C=DO`, válido hasta 2056.
- Una sola ABI (`arm64-v8a`), 0 modelos `.onnx`, 0 ficheros `.m3u`/`.m3u8`/`.xmltv`
  dentro: ninguna lista de canales viaja en el APK.
- La 1.0.1 pesó 31.577.211 bytes y la primera build, 475.523.392.

**No probado en un dispositivo.** Ni el DSP del ecualizador ni el decodificador de
vídeo se han abierto nunca aquí: las pruebas son de JVM y no hay emulador. El banco
es el V60 ThinQ 5G y falta instalarlo y abrirlo.

## Lo que no se guarda aquí, y cómo recuperarlo

- El árbol del repo: `GET /repos/Alex17273747576777/cero-X-app/tarball/<sha>`, o por
  fichero con `raw.githubusercontent.com/.../<sha>/<ruta>` (por SHA, no por `main`:
  recién publicado, `main` sirve contenido viejo).
- Los logs de CI: `curl -sSL -H "Authorization: Bearer $GP" .../actions/jobs/<jid>/logs`
  (con `urllib` da 403). Se borraron `logs/` con log21–log26.
- El APK: asset de la release. Se baja, se comprueba y se borra; son 33 MB que no
  aportan nada guardados.
- Los índices de FMHY y appteka: los regeneran `scripts/buscar-fmhy.py` y
  `scripts/buscar-appteka.py` del propio repo, que son autosuficientes.

`/tmp` se pierde entre turnos y los tokens no están en el snapshot: lo que deba vivir
de un turno a otro va en `/home/user`, y las claves en `../.cerox-keys/` (NO BORRAR;
falta aún su copia fuera de GitHub).
