# REGISTRO DE CAMBIOS

Todo lo notable de este archivo, en orden inverso, con la forma de [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) y numeración [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html). Las fechas van en ISO 8601 (`AAAA-MM-DD`).

Criterio de numeración, para que no sea arbitraria: **menor** cuando cambia una pieza publicada, una herramienta o el registro de fichas; **mediano** cuando cambia la estructura del árbol o el contrato de datos; **mayor** cuando cambia la licencia o se rompe una ruta publicada sin traducción en el mapa.

---

## [3.0.0] — 2026-11-15

El retiro y la casa de reglas. Por orden del dueño se borraron todas las publicaciones:
458 ficheros de `Arena-Reimagined/01-PUBLICACIONES/`, carpeta que ya no existe. Por el
criterio de numeración de este mismo archivo, romper una ruta publicada sin traducción
en el mapa es cambio **mayor**. El contenido no se reescribió para disimular: vive en el
historial git y en las actas (Addendum 3 de `docs/ACTA-RESELLADO-2026-11-14.md` y
ADDENDUM DE RETIRO de `CORAZON-LA-BANDITA.md`).

La casa quedó en tres capas vivas —ley (CORAZON, `CIMIENTOS/`, `PROCESOS/`), medida
operativa (`REGLAS/INDICE-DE-REGLAS.md`, `docs/bandas.json`, vara G0-G17 y vara_idiomas
G20-G23) y habilidades (`SKILLS/`, `Arena-Reimagined/HABILIDADES/`,
`ENTORNO-DE-TRABAJO/`)— más el archivo medido: 70 fichas de la guía maestra, 6.838
fichas de registro y sellos encadenados.

Del mismo corte:

- `README.md` reescrito: describía la casa del 8 de noviembre y contradecía el retiro.
- `tools/autoprueba.py`: la salida de la autoprueba sintética queda etiquetada
  (FALLA-007); se leía como aviso real sobre el README vivo y no lo era.
- Registro de fallas al día con las entradas 005 a 008
  (`ENTORNO-DE-TRABAJO/FALLAS-Y-CONTRAPARCHES.md`).
- Segundo resello del día y empuje del conjunto con autorización del dueño.

---

## [2.2.0] — 2026-11-08

La deuda de las nueve piezas. Del bloque anterior quedaron nueve piezas cortas declaradas «sin
medición propia»: 24 a 29, 32, 33, 34 y —en parte— 40. En esta pasada se midieron los temas de
verdad y se reescribieron los nueve cuerpos con sus cifras.

### Añadido

- **`tools/medir_piezas_24_34.py`**: mide los repositorios de cada pieza contra la API pública de
  GitHub y escribe `docs/MEDICION-NN-2026-11-08.json` con estrellas, forks, licencia, archivado,
  fechas, última entrega, número de entregas, adjuntos totales, **adjuntos con suma** y descargas.
  Cachea cada respuesta y permite volver a medir con `--todas`. Salida medida: nueve JSON,
  **34 repositorios distintos** y **11.897 archivos** contados, de los cuales **111 llevan suma de
  comprobación** —y 102 de esos 111 son de un solo proyecto: Kototoro.
- **Nueve cuerpos reescritos** con medición propia: 24 (extensiones de anime), 25 (OCR), 26 (Usagi),
  27 (DropSauce), 28 (Mangayomi), 29 (LNReader), 32 (Tu Manga Online), 33 (apoyo a desarrolladores)
  y 34 (biblioteca de Kototoro). Entre 9.984 y 13.856 caracteres cada uno, todos dentro de banda.
- **Nueve comentarios fijados generados desde el JSON de medición**: ninguna cifra va escrita a mano;
  el generador sustituye la cifra vieja si la medición cambia.

### Cambiado

- **Las piezas cortas anteriores se retiran a `_reemplazadas-2026-11-08/`** con `git mv`, no se borran.
- **`LEEME-de-la-carpeta.md`**: la tabla dice en cada fila si la pieza está medida y qué salió; se
  añade la sección «La medición del 8 de noviembre» con las órdenes para volver a medir.
- **`README.md`**: la deuda declarada pasa a contarse como pagada, con lo que salió al medir.
- **`docs/bandas.json`**: 80 entradas recalculadas con los caracteres reales.

### Corregido

- **Un fallo del medidor**: `dias_push = 0` se interpretaba como «desconocido», así que los
  repositorios que empujaron código **hoy** no contaban como actividad de la semana. Detectado al
  comparar la prosa con los totales; corregido y regeneradas las nueve mediciones.

### Lo que sigue sin hacerse, y se declara

- La **pieza 36** sigue corta y sin medición propia: cuenta el cierre de un sitio, y eso no se mide
  con la API de repositorios. Se queda declarada.
- **No hay prueba en dispositivo**: ninguna de las nueve piezas se probó ejecutando las aplicaciones.
  Lo que se midió son repositorios, no el comportamiento de los programas en un teléfono.

---

## [2.1.0] — 2026-11-08

La pasada del cierre de la serie de Facebook: cuarenta piezas con cuerpo y comentario fijado, y la
corrección de la mentira que las estaba inflando. Es **menor** y no mediano porque no cambia la
estructura del árbol —solo se mueven ocho archivos a `_reemplazadas-2026-11-08/` y se añade una
herramienta—, pero toca piezas publicadas y por eso lleva versión propia.

### Corregido

- **El «mínimo obligatorio de 45.000 caracteres para Facebook» no existe.** Era una vara interna de la
  casa que se convirtió en relleno: `generar_piezas.py` produjo nueve cuerpos repitiendo cinco
  secciones fijas —«Resumen ejecutivo», «Contexto general», «Análisis técnico profundo», «Comparativa
  con alternativas»— con el título de cada pieza metido a la fuerza en medio, frases como «Los fichas»
  y una conclusión idéntica en las nueve. Se retiraron las ocho versiones de relleno de las piezas 32 a
  39 a `_reemplazadas-2026-11-08/` —no se borra nada— y quedó viva la original de cada número. La
  doctrina nueva está en `docs/bandas.json`: banda de **6.000 a 45.000** caracteres, sin obligación de
  acercarse al máximo.
- **Pieza 06**: se retira la voz rota que se publicó a la vista —«Eso son cinco de diecisiete, no
  cuatro: me corrijo, son cinco. Espera, contemos: …»— y queda el conteo limpio.
- **Pieza 07**: la semilla afirmaba que los cinco gigantes «no publican huella». Medido otra vez el
  8-nov contra la API de GitHub: tres no publican ningún adjunto en su última entrega, SmartTube
  publica cuatro y **ninguno de los cinco adjunta una suma**. La frase ahora dice eso, con fecha.
- **Piezas 08 a 18**: se retiran las cajas «### Datos comparados (lista jerárquica)» que metió el
  generador dentro del texto publicado.
- **Ocho piezas cortas** (32 a 39) declaraban un número de pieza que no era el suyo —la 37 decía
  «pieza 12»—; renumeradas.
- **Once comentarios fijados**: «Los fichas» → «Las fichas».

### Añadido

- **Diez comentarios fijados** que faltaban: 06, 07, 08, 09, 10, 11, 12, 13, 14 y 40, con las cifras que
  ya estaban medidas en el cuerpo de cada pieza y las seis órdenes de comprobación.
- **Pieza 40 reescrita entera**: «La lección del hash SHA-256: cómo comprobar un archivo sin root»,
  13.532 caracteres, dentro de banda. Su título anterior decía «premio de La Bandita» y no había ningún
  premio: era una etiqueta del generador. Las tres órdenes que enseña se ejecutaron en esta máquina
  antes de publicarla (`sha256sum`, `sha256sum -c` → `OK`, `apksigner`).
- **`tools/leeme_carpeta.py`**: cuadra el LEEME de la carpeta con el disco. Verifica que cada número
  01–40 tenga un cuerpo y un comentario fijado, que los caracteres de la tabla sean los reales y que no
  haya piezas sin número en la raíz. Salida medida: **40 piezas comprobadas · fallos: 0**.

### Cambiado

- **`LEEME-de-la-carpeta.md`** del canal de Facebook: reescrito con las cuarenta filas medidas, la
  doctrina de longitud corregida, las nueve cortas declaradas como *sin medición propia* y la ruta de
  las reemplazadas.
- **`README.md`**: estado al 8 de noviembre, serie de Facebook hasta la 40, y una sección nueva —«La
  corrección del 8 de noviembre»— que dice lo que se corrigió y lo que sigue sin hacerse.
- **`docs/bandas.json`**: banda rehecha pieza por pieza y fijado por fijado, 81 entradas, ninguna fuera
  de su propia banda.

### Lo que sigue sin hacerse, y se declara

- Nueve piezas cortas —24 a 29, 32, 33, 34 y 36— **no tienen medición propia**: su tema no se ha medido
  todavía contra la API. El LEEME las marca una por una en vez de contarlas como terminadas.

---

## [2.0.0] — 2026-11-03

La pasada de la poda y de la pieza 06. Se quitaron los residuos que el árbol podía reconstruir
—once archivos, 16,6 MB— y `uploads/` dejó de estar en la raíz. Se publicó la pieza de Facebook
sobre el gestor de parches Universal Patch Manager, con el código 451 de su módulo comprobado en
vivo. Es **mediano** y no **menor** porque cambia la estructura del árbol: una ruta publicada
(`uploads/`) desaparece de la raíz y se traduce en el mapa y en la tabla de mudanzas.

### Añadido

- **Pieza 06 de Facebook · «El taller: un gestor de parches con mil cuatrocientas siete estrellas, sesenta y cinco entregas y un módulo que perdió su casa»** — 44.716 caracteres, dentro de banda, VERDE en `manual_gate` y en `novedad_gate`. Mide el programa contra su fuente el mismo día: 65 entregas, 238 archivos, 122.769 descargas sumadas, 78 contribuidores, 2.355 confirmaciones, el árbol de 32 carpetas explicado y cinco pasos de uso que se pueden deshacer.
- **`docs/ACTA-PIEZA-06-2026-11-03.md`**: qué se midió, con qué orden, qué se declara como hueco y la verificación triple del envío.
- **`docs/ACTA-PODA-2026-11-03.md`** y **`ARCHIVO-HISTORICO/_podado-2026-11-03/README.md`**: el acta de la poda, con el SHA-256 de cada archivo retirado, el motivo, y el envase que se restauró antes de confirmar.
- **`docs/bandas.json`**: declarada la banda de la pieza 06 con sus 44.716 caracteres, para que la compuerta M11 la exija como a las demás.
- **`tools/referencias.py`**: la mudanza `uploads/` → `ARCHIVO-HISTORICO/subidas-2026-09/` entra en la tabla de mudanzas, con lo que G17 la vigila como cualquier otra.

### Cambiado

- **`uploads/`** → `ARCHIVO-HISTORICO/subidas-2026-09/`: 53 documentos de la carga inicial de septiembre, con sus nombres originales, movidos con `git mv` para conservar la historia del archivo.
- **`README.md`**: estado al 4 de noviembre, serie de Facebook hasta la pieza 06, la poda declarada en la sección de la disculpa y en la tabla de estado.
- **`MAPA-DEL-ARCHIVO.md`**: nueva sección «Lo que se podó el 4 de noviembre», y corregida la frase que decía que los ZIP se quedaban donde estaban.
- **`Arena-Reimagined/LEEME-ESTRUCTURA.md`**: el envase de la entrega del 29 de octubre ya no está, y el LEEME lo dice con la ruta del acta.
- **`docs/PENDIENTES.md`**: sección de cierre del 4 de noviembre, con lo terminado y, separado, lo que sigue abierto y por qué.
- **`docs/POLITICA-DUPLICADOS.md`**: la poda como cumplimiento de las reglas 1 a 3 de la propia política.
- **`Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/LEEME-de-la-carpeta.md`**: pieza 06 publicada, 07 siguiente, y el cambio de tema de la 06 declarado.
- **`tools/referencias.py`**: `uploads/` sale de los prefijos históricos porque ya no existe en la raíz.

### Retirado

- **11 archivos · 16,6 MB**, todos reconstruibles o idénticos: dos envases comprimidos cuya copia ya estaba abierta (284 y 36 entradas, cotejadas nombre por nombre), la suma de comprobación de uno de ellos, cinco vistas HTML generadas desde sus `.xhtml`, la vista HTML de 6,5 MB de la entrega completa y dos copias byte por byte de documentos del respaldo del 14 de septiembre. El hash de cada uno queda en el acta; la copia, en la historia de Git.
- **No se retiró** `ENTREGA-La-Bandita-COMPLETA.zip`: dos de sus 456 entradas son su propio manifiesto interno, y eso lo convierte en archivo. Se restauró antes de confirmar el cambio, y el acta lo explica.

---

## [1.4.0] — 2026-11-03

La pasada de la memoria y del registro. Se movieron cinco carpetas de etapas anteriores
**sin romper una sola referencia viva**, y el registro se volvió a medir contra la fuente
primaria: 4.098 fichas leídas, 278 declaradas sin objeto. De camino apareció lo que había
debajo: 4.186 fichas declaraban una fecha que ningún archivo respaldaba.

### Añadido

- **`tools/vencimiento.py`**: decide qué ficha está `vigente`, `por_vencer`, `vencida`, `sin_respaldo` o `sin_objeto`, midiendo la edad **contra la evidencia** y no contra la confianza. Escribe `docs/VENCIMIENTOS.md`, `registry/_vencimientos.json` y el bloque `frescura` de cada ficha.
- **`docs/POLITICA-FRESCURA.json`**: las ventanas en un solo sitio, cada una con su razón —actividad y estrellas 30 días, licencia y scorecard 90, ficha entera 180—. Antes eran un número suelto en la vara y una frase en el calendario de novedades.
- **`tools/referencias.py`**: la tabla de mudanzas del repositorio y el auditor que distingue una ruta vieja citada por un archivo vivo (fallo) de una citada por un acta (cita que se conserva y se traduce).
- **Compuerta G16 · fecha respaldada**: ninguna ficha puede declarar una fecha que su evidencia no sostenga, ni decir «vencida» sin motivo escrito.
- **Compuerta G17 · rutas vivas**: ninguna carpeta movida puede seguir citada por su ruta vieja desde un archivo que hoy se lee o se ejecuta.
- **`make vencer`**, **`make remedir`** y **`make referencias`**: los tres destinos nuevos del `Makefile`.
- **`docs/ACTA-REMEDICION-2026-11-03.md`**: el acta de la pasada, con sus números y con el error propio que hubo que corregir.

### Cambiado

- **`Arena-Reimagined/_versiones/`, `packs/`, `_herramientas/`, `_herramientas-casa/` y `_referencia/`** → `Arena-Reimagined/02-ARCHIVO/_etapas-anteriores/`. Cinco carpetas, 70 archivos, y las referencias corregidas en el mismo cambio.
- **`tools/censo_medir.py`**: guarda el payload crudo de cada medición en `registry/_evidencia/<id>.json` con la fecha **dentro del archivo** y su SHA-256 en la ficha; acepta `--vencidas` y `--solo` para remedir solo lo que hace falta en vez del registro entero; y fecha con `fecha_casa.hoy()` en lugar de `date.today()`.
- **`tools/registro_construir.py`**: modo `--indice`, que refresca el índice del registro desde el disco sin reconstruir las fichas —reconstruirlas desde el censo habría borrado la re-medición—.
- **`schemas/ficha.schema.json`**: se declara el bloque `frescura` (estado, días, evidencia, próxima remedición, ventana y motivo).
- **`MAPA-DEL-ARCHIVO.md`** y **`README.md`**: la deuda de estructura deja de ser deuda y pasa a ser una mudanza hecha, con su tabla de traducción de rutas.

### Corregido

- **4.186 fichas declaraban `medido_en: 2026-11-03` con una fila del censo del 15 de octubre como única evidencia.** La compuerta G2 leía `medido_en` y las contaba como recién medidas. Se remediation leyendo la API y hoy ninguna ficha declara una fecha sin respaldo.
- **194 + 84 repositorios de la lista ya no existen**: sus fichas se marcan `sin_objeto` con el motivo escrito, en vez de seguir contando como vigentes.
- **La re-medición fechó con UTC**: 4.193 fichas quedaron con el día siguiente al de la casa. Se refecharon y se recalcularon los SHA-256 de 3.999 payloads y las fechas de 3.711 licencias.
- **`Arena-Reimagined/.gitignore`**, `HABILIDADES/herramientas/chequeo-niveles.py` y `HABILIDADES/herramientas/guardar.py` apuntaban a las carpetas movidas: son consumidores reales y se corrigieron con la mudanza.

### Verificado

- Vara: **G0 a G17 en verde**, `fallos: NINGUNO`.
- Registro: **6.838 fichas · 6.560 vigentes · 278 sin objeto · 0 vencidas · 0 sin respaldo**.
- Referencias: **0 rutas vivas rotas** sobre 14.224 archivos revisados; 307 citas históricas conservadas en 47 documentos.
- Contra la fuente remota: 10 fichas al azar consultadas otra vez por REST; 7 coinciden al dato, 2 difieren solo en estrellas (+14 y +2 en media hora) y 1 declara correctamente que el repositorio no existe.

---

## [1.3.1] — 2026-11-03

La pasada de orden. Se hizo porque el archivo, que presume de verificar, tenía la raíz con 29 entradas, dos carpetas de canal con **números repetidos** y rutas que las actas citaban y ya no existían. Nada de lo aquí listado cambia una pieza ya publicada: se corrige hacia adelante.

### Añadido

- `ARQUITECTURA.md`: las tres capas, el sentido del dato en cinco pasos, seis decisiones con su contexto y su coste, y los números del corte.
- `docs/CODIGO.md`: las 31 herramientas explicadas una por una —qué recibe, qué hace, qué produce y **qué no hace**— más tres invariantes.
- `tools/tareas.py`: extrae el tablero de tareas de las piezas y los documentos, y falla si una pieza repite número o salta uno dentro de su propia serie. Salida: `docs/TAREAS.md`, 12 tareas, 0 incidencias, 2 declaradas.
- `tools/indice_docs.py`: índice de documentos con resumen largo verificado. Salida: `docs/INDICE.md`, 49 documentos en 19 familias y 31 herramientas.
- `tools/doctor.py`: cinco bloques de diagnóstico y un veredicto. Se niega a decir LISTO si falta una pieza esencial.
- `Makefile`: catorce destinos (`ayuda`, `doctor`, `verificar`, `sellar`, `compuertas`, `licencias`, `generar`, `sitio`, `tareas`, `indice`, `libro`, `medir`, `publicar`, `push`) para que el primer comando no haya que adivinarlo.
- Archivos de salud comunitaria: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `CHANGELOG.md`, plantillas de incidencia y de solicitud de cambio, y `CODEOWNERS`.

### Cambiado

- **`ARCHIVO-HISTORICO/`**: ocho carpetas de memoria (`03-PUBLICACIONES-2026-09-15`, `04-VERSIONES-MULTIIDIOMA`, `backup-previo-correccion-14-09`, `archivo`, `site-demo`, `datos-censo`, `datos-miyomi`, `datos-v25`) consolidadas en una sola, con `INDICE-2026-10.md` y `MANIFIESTO-2026-10.md`. La raíz pasa de 29 a 24 entradas.
- **El sello ahora cubre el gobierno del repositorio.** `tools/sello_reglas.py` no sellaba `Makefile`, `ARQUITECTURA.md`, los archivos de salud comunitaria, `.github/`, `LICENSES/` ni las licencias: el README podía cambiar sin que la integridad lo notara. Con la corrección, el sello pasa de 10.173 a **10.196 archivos**.
- Rutas de herramienta corregidas en `tools/duplicados.py`, `tools/idioma_mojibake.py` y `tools/sitio.py`, que seguían apuntando a las carpetas movidas. Las dos compuertas vuelven a salir con código 0.
- `README.md` y `MAPA-DEL-ARCHIVO.md` revisados: tabla de rutas anteriores traducidas, estado del corte y punto de entrada único.

### Corregido

- El resumen del índice tomaba la primera línea no vacía y devolvía fragmentos que empezaban a media frase («tras la limpieza del 2-nov, con su huella…»). Ahora une el párrafo antes de leerlo, exige que empiece en mayúscula o signo de apertura y corta en oración completa; los documentos sin primera oración con cuerpo se marcan en vez de quedar en blanco.
- `_archivo-historico/` (con guion bajo) duplicaba la función de `ARCHIVO-HISTORICO/`; se eliminó tras mover su contenido.
- El `LEEME` de la carpeta de canal llevaba un prefijo numérico `00-` que lo sacaba del filtro `startswith(("leeme","readme"))` y hacía fallar la compuerta G0 por el latido y la fecha. Renombrado a `LEEME-de-la-carpeta.md`.

### Verificado

- `vara.py`: **fallos NINGUNO** en las quince compuertas.
- `atestar.py`: **10.196 archivos**, huella encadenada en `attestations/lote-2026-11-03.json`.
- Integración continua: `success` sobre el árbol sellado.
- `envio.py --verificar`: 5 de 5 en Facebook y 5 de 5 en WhatsApp, cero fallos.

---

## [1.3.0] — 2026-11-03

### Añadido

- Pieza **05** de cada canal: «la guía maestra» en Facebook y el resumen de bolsillo en WhatsApp, con su tabla de bandas y su parte de envío.
- `docs/envios/{facebook,whatsapp}/` con los envíos medidos y verificados de las cinco piezas de cada canal.

### Cambiado

- `MAPA-DEL-ARCHIVO.md` y `README.md` con el bloque de estado del corte.

---

## [1.2.0] — 2026-11-02

### Añadido

- **Guía maestra**: 70 fichas medidas en 12 capítulos, con autor, licencia, versión, fecha de medición y límite declarado de cada aplicación; más el comando único `guia_maestra.py --compuertas --generar --estricto` (70 fichas, 12 páginas, 0 fallos).
- Créditos completos de los creadores y las licencias de cada obra citada, conforme a `LEGAL/`.

### Corregido

- Autor mal atribuido en la familia de clientes de YouTube alternativos: la atribución correcta es la del repositorio vigente, no la del espejo.

---

## [1.1.0] — 2026-10-28

### Añadido

- Ciclo vivo de canal con plan de catorce piezas: 01 la puerta y el recibo · 02 la música · 03 la caja del bolsillo · 04 la lista del permiso · 05 la guía maestra · 06 el taller · 07 la pantalla grande · 08 la red · 09 archivos y nubes propias · 10 privacidad comprobable · 11 cuando algo se rompe · 12 el oficio · 13 remisión de diciembre · 14 la lista del día uno.
- `LEEME-de-la-carpeta.md` en cada canal con el estado, el plan y la regla de convivencia con el archivo histórico.

### Cambiado

- Las piezas anteriores pasan a `_ARCHIVO-HISTORICO/<mes>/` y conservan su fecha y sus fallos.

---

## [1.0.0] — 2026-10-15

### Añadido

- Piezas 01 a 04 de Facebook y 00 a 04 de WhatsApp, con las dos compuertas en verde, el sello encadenado y la integración continua en `success`.
- Las quince compuertas de la vara, el sello `atestar.py` y las herramientas de medición sobre las que se apoya todo lo demás.
- `LICENSE`, `LICENSE-CONTENIDO`, `LICENSE-DATOS` y `NOTICE`: código, texto y datos con condiciones distintas, declaradas por archivo según las prácticas de REUSE.

---

*La Bandita informa a partir de fuentes fechadas.*
