# Cotejo semántico de §9.9 y revisión factual de Pieza 01 ES

**Estado: cotejo semántico de las 70 unidades completado en esta revisión, con nueve correcciones de matriz; la aceptación del manual y de la pieza siguen pendientes.** Este documento no declara el contenido listo para publicar.

## Corte, archivos y límites

- Fecha autorizada de referencia: **2026-11-10, America/Santo_Domingo**. El dueño aclaró que **2026-11-19 era una fecha prevista**, no un corte histórico ni la fecha actual. El reloj del sandbox y las cabeceras `Date` del API de GitHub devolvieron 2026-11-19; se registra el conflicto y no se usan esos días futuros como corte local.
- Manual cotejado: `proyectos/la-bandita/manual-v0.0.1/MANUAL-v0.0.1.md`, SHA-256 actual `73f71daa13af1c776d49aaefbdf19e64ab4cff07e41675449e09221f56707f1f` (verificado idéntico en worktree, índice y HEAD). La revisión anterior lo registró por error como `c83c11fe…`; no se editó el manual en esta actualización.
- Pieza examinada: `proyectos/la-bandita/molde-vivo/pieza-01-ES.md`, SHA-256: `b63b5434b73debf9561e3243392966b540bac5f21dc6356b1b003fa493aa390b`.
- Se leyó el manual completo y la matriz de §9.9; se cotejó cada una de las 70 subsecciones numeradas con su fila, no solo los IDs o el test estructural. Se reforzaron nueve filas para cubrir pruebas que estaban ausentes o demasiado genéricas: §0.1 (compuerta real); §1.5 (vista móvil); §1.7 (caso positivo/negativo); §3.5 (cinco estados y su acción); §5.2 (prueba de materialidad antes de preguntar); §7.2 (estados, persistencia y alcance real de la guarda); §8.2 (alarma Jaccard como triage, no veredicto ni generador); §8.4 (campos del checkpoint y cifras medidas); §10.3 (todas las condiciones para declarar completa v0.0.1). La corrección no elimina el bloqueo de lecciones ni convierte el manual en aceptado.
- Comprobaciones repetidas tras esos cambios: `make prueba` — **TODO BIEN**; unittest editorial — **14/14**; `vara_bandita.py MANUAL --modo-norma` — **VERDE, 133.646 caracteres**; `vara_bandita.py pieza-01-ES.md` — **VERDE mecánico, 48.062 caracteres**; `git diff --check` — limpio. El VERDE de la pieza no confirma hechos, sustancia, orden editorial ni seguridad.

## Resultado por cada una de las 70 reglas

| ID | Resultado del cotejo sección ↔ fila de §9.9 |
|---|---|
| 0.1 | Corregida: el ejemplo ahora corresponde a la receta convertida en compuerta antes de entregar. |
| 0.2 | Alineada. |
| 0.3 | Alineada. |
| 0.4 | Alineada: conserva como declaraciones del dueño las cifras cuya medición/fuente no se ha confirmado. |
| 0.5 | Alineada. |
| 0.6 | Alineada. |
| 0.7 | Alineada. |
| 1.1 | Alineada. |
| 1.2 | Alineada como bloqueo explícito: 15 entradas en la tabla, 18 declaradas; no se rellenan ni borran. Falta la lista de 18 del dueño. |
| 1.3 | Alineada. |
| 1.4 | Alineada. |
| 1.5 | Corregida: se añadió al texto normativo la verificación de la vista móvil/destino real que ya figuraba en el criterio. |
| 1.6 | Alineada. |
| 1.7 | Corregida: el caso positivo muestra criterio, opinión y corte, y el negativo prueba una fórmula vetada. |
| 1.8 | Alineada. |
| 1.9 | Alineada. |
| 1.10 | Alineada. |
| 1.11 | Alineada. |
| 2.1 | Alineada. |
| 2.2 | Alineada. |
| 2.3 | Alineada. |
| 2.4 | Alineada. |
| 2.5 | Alineada. |
| 2.6 | Alineada. |
| 2.7 | Alineada. |
| 2.8 | Alineada. |
| 2.9 | Alineada. |
| 2.10 | Alineada. |
| 3.1 | Alineada. |
| 3.2 | Alineada. |
| 3.3 | Alineada. |
| 3.4 | Alineada. |
| 3.5 | Corregida: ahora distingue los cinco estados y explicita cuándo se excluye, se limita o se detiene la recomendación. |
| 3.6 | Alineada. |
| 4.1 | Alineada. |
| 4.2 | Alineada. |
| 4.3 | Alineada. |
| 4.4 | Alineada. |
| 4.5 | Alineada. |
| 4.6 | Alineada. |
| 4.7 | Alineada. |
| 4.8 | Alineada. |
| 5.1 | Alineada. |
| 5.2 | Corregida: incorpora resultados posibles, materialidad y la pregunta breve que separa lecturas. |
| 5.3 | Alineada. |
| 6.1 | Alineada. |
| 6.2 | Alineada. |
| 6.3 | Alineada. |
| 6.4 | Alineada. |
| 7.1 | Alineada. |
| 7.2 | Corregida: explicita compuertas/estado de la guarda, máximo dos maestros y la secuencia de estados hasta publicación comprobada. |
| 7.3 | Alineada. |
| 7.4 | Alineada. |
| 8.1 | Alineada. |
| 8.2 | Corregida: delimita Jaccard 0,32 como alarma con posibles falsos positivos/negativos, no como calidad/originalidad ni generador. |
| 8.3 | Alineada. |
| 8.4 | Corregida: enumera estado por ID/idioma, fallos, pruebas/avisos, cambios, almacenamiento y siguiente paso, con datos medidos. |
| 9.1 | Alineada. |
| 9.2 | Alineada. |
| 9.3 | Alineada. |
| 9.4 | Alineada. |
| 9.5 | Alineada. |
| 9.6 | Alineada. |
| 9.7 | Alineada. |
| 9.8 | Alineada; sigue exigiendo fecha, alcance y efecto de cada lección. |
| 9.9 | Alineada: la revisión humana se hizo; el resultado no se infiere del conteo ni del test. |
| 10.1 | Alineada. |
| 10.2 | Alineada. |
| 10.3 | Corregida: explicita todas las condiciones de aceptación completa y las cinco decisiones canónicas ratificadas. |
| 10.4 | Alineada. |

**Conclusión del cotejo:** tras la lectura humana completa, las 70 filas ahora cubren la unidad normativa comparada y sus casos/consecuencias; nueve se reforzaron como se indica. Esto acepta únicamente el cotejo semántico §9.9 de esta versión, no el manual completo: sigue bloqueado por la lista de 18 lecciones que debe aportar el dueño (la tabla conserva 15 y no se altera por conjetura), la aceptación factual/estructural de la pieza y el lote 01–70.

## Pieza 01 ES: hallazgos que impiden aceptarla

### Fechas y evidencia mutable

- La pieza se presenta como «verificada en vivo» el **19-nov-2026** en la introducción, los créditos y las notas. Esa fecha era prevista, no un corte histórico confirmado. La fecha local autorizada es 2026-11-10.
- La misma pieza menciona actividad posterior al corte: Omnify 11-nov, microG 12-nov, Appteka/SD Maid SE/Magisk 18-nov y NewPipe/AntennaPod/VLC 19-nov. Son fechas futuras respecto del corte autorizado y no pueden sostener una verificación «de hoy» al 10-nov. Las estrellas y versiones rotuladas 19-nov tampoco quedan validadas para el 10-nov; deben volver a medirse desde cada casa canónica y guardarse con commit/release y fecha de acceso.
- La API REST de GitHub devolvió `Date: Thu, 19 Nov 2026 … GMT` y ramas/ejecuciones con fechas posteriores al corte. No se tratan como si fueran un archivo histórico del 10-nov. La página de Keep Android Open presenta un contador dinámico; no se abrió una captura fechada que demostrara el número «unos 110 días» al 14-sep.
- Los enlaces a repositorios ayudan a localizar fuentes, pero no sustituyen el registro por afirmación que exige §4.2: frase concreta, ruta/release/commit, corte, evidencia y qué no demuestra. Los conteos exactos y las licencias de todos los candidatos no quedan reproducibles con solo la lista de enlaces.

### Afirmaciones técnicas que requieren corrección o acotación

1. **F-Droid y compilación reproducible — contradicción directa.** La pieza afirma que si un APK no puede reproducirse byte por byte «no se publica» y que ese estándar se aplica a toda la tienda. La [FAQ oficial de desarrolladores](https://f-droid.org/docs/FAQ_-_App_Developers/) dice que las compilaciones reproducibles **no son obligatorias**; la [documentación de F-Droid](https://f-droid.org/docs/Reproducible_Builds/) pide revisar el estado de reproducibilidad por aplicación y explica que la cobertura y los resultados varían. No presentar el estándar como garantía universal ni como condición de publicación general.
2. **Firma digital — analogía demasiado fuerte.** La documentación de Android sobre [firma de aplicaciones](https://developer.android.com/guide/topics/permissions/defining#signing) explica que el certificado puede ser autofirmado y sirve para distinguir autores/llaves en el modelo de Android. La firma protege integridad y continuidad respecto de una clave; por sí sola no demuestra la identidad civil del autor, que el código sea benigno ni que no haya recopilación de datos. Para enlazar una clave con un desarrollador hay que comparar una huella comunicada por un canal confiable. Un cambio de firma exige detenerse y verificar una migración oficial; no prueba por sí solo un ataque.
3. **Aurora Store — anonimato absoluto no demostrado.** La documentación propia [enumera datos que se envían](https://auroraoss.gitbook.io/wiki/troubleshooting-and-faqs/faqs/aurora-store): consultas y descargas, IP y, para comprobación de actualizaciones, nombres de paquetes; el inicio anónimo usa un servidor dispensador de tokens. «No usar tu cuenta personal de Google» puede ser correcto; «Google no sabe quién eres ni te perfila» va más allá de esa evidencia y debe retirarse o limitarse.
4. **Exodus Privacy — presencia no equivale a actividad.** Su [FAQ oficial](https://exodus-privacy.eu.org/en/page/faq/) describe detección estática de firmas/clases de rastreadores y advierte expresamente que encontrar uno no demuestra que esté activo; tampoco garantiza que la lista sea completa. La frase de la pieza «quién te va a espiar» presenta inferencia como hecho; cambiar a «componentes/rastreadores conocidos detectados» y conservar el límite.
5. **microG — no garantiza desconexión de Google.** La [wiki oficial de microG](https://github.com/microg/GmsCore/wiki) lo describe como reimplementación libre, incluye funciones optativas de servicios de Google y avisa que apps pueden usar bibliotecas propietarias para comunicarse con microG o con servicios reales. «Trabaja para ti y no le cuenta tus conversaciones a Google» y «sin entregarle tus datos a Google» son absolutos sin respaldo; hay que distinguir módulos, ajustes, destinos de red y aplicaciones dependientes.
6. **Obtainium y la instalación automática — evidencia oficial abierta en esta revisión.** La frase de la pieza («la descarga y la instala […] sin que muevas un dedo») convierte una capacidad opcional en comportamiento general. Abrí la [guía de desarrollo oficial fijada al commit `ef0eed86adaac91dc9b18f9fde3b045d99ad538b`](https://github.com/ImranR98/Obtainium/blob/ef0eed86adaac91dc9b18f9fde3b045d99ad538b/docs/DEVELOPER_GUIDE.md); la página identifica ese commit como el último editado el 31-oct-2026, anterior al corte de plataforma 10-nov. La guía dice que las apps pueden instalarse desde sus fuentes «optionally silently in the background»; distingue chequeos/notificaciones de la modalidad de instalación, condiciona el trabajo en background a opciones y guardas, usa `canInstallSilently(app)` y documenta que `StockInstaller` requiere `INSTALL_PACKAGES` concedido vía ADB para la vía silenciosa, con otras rutas según el instalador seleccionado (Shizuku/Sui, instalador externo o root). Esto respalda que la función puede existir bajo configuración y condiciones compatibles, no que toda detección instale silenciosamente de manera predeterminada y universal. Reescribir como capacidad condicional y distinguir seguimiento, aviso e instalación. No se probó en dispositivo la configuración de la pieza ni la instalación real; la guía de desarrollador tampoco demuestra el comportamiento de cada combinación/version de Android.
7. **Verificación de desarrolladores Android.** La [guía primaria de Android Developers](https://developer.android.com/developer-verification/guides) consultada dice que las protecciones «go live» desde el 30-sep-2026 para usuarios de Brasil, Indonesia, Singapur y Tailandia; lista siete tiendas participantes y anuncia expansión global para apps en dispositivos Android certificados en 2027. Como la guía es una página viva y no se obtuvo una captura histórica fechada al 10-nov, la pieza debe atribuir el calendario a la fuente y no decir que se comprobó el despliegue efectivo de cada territorio/tienda. La misma guía distingue distribución completa, limitada a 20 dispositivos y sideloading avanzado de apps no registradas; dice que las apps aún se pueden instalar por sideload y que la experiencia ADB permanece. No afirmar un bloqueo universal. Keep Android Open es una campaña de incidencia, no reemplazo de la política primaria de Google.
8. **Cifra de la comunidad.** El cierre atribuye «más de un millón trescientas mil personas» sin fuente ni fecha; §0.4 conserva «1,358M» como declaración no medida y de notación aún no aclarada. No convertir esa cifra en alcance probado: retirar o aportar medición primaria, unidad y corte.
9. **Permisos, mods, root, garantía y legalidad.** «Permiso de más = intención de más», «las tiendas de mods no revisan nada», las acusaciones sobre sitios nombrados, fallos de bancos/garantía por root y «legal en casi todos los países» se presentan como universales o como hechos sin evidencia específica. Un permiso es una señal para investigar, no prueba de intención; políticas de banco/garantía dependen de app, fabricante y jurisdicción; la legalidad necesita jurisdicción y fuente. Corroborar o reescribir como riesgo condicionado, sin atribuir conducta a un sitio sin prueba.
10. **Candidatos y cifras restantes.** Las descripciones de catálogos, permisos, Android mínimo, licencias, versiones, estrellas, actividad y características de cada tienda/instalador/lupa/app citada deben cotejarse, una por una, contra su casa canónica al corte válido. No se marca el conjunto completo como comprobado a partir de una revisión dirigida de algunos ejemplos.

### Orden y estado del archivo

- La cabecera lo llama **«PARTE 1 de 3»**, pero el mismo archivo contiene Créditos, meme, firma y Notas y termina ahí; no se encontraron las partes 2/3 en esta ruta. Debe aclararse si es un maestro completo o un fragmento antes de llamarlo listo.
- El archivo tiene 48.062 caracteres y pasa el mínimo mecánico, pero no se aportó la cuenta humana por sección de §2.7; el conteo bruto no demuestra 45.001 caracteres de sustancia.
- El orden real es Créditos → diálogo/meme → firma/remate → Notas. El manual exige Notas → meme → firma → remate → Créditos, con Créditos como última sección (§1.8/§2.10/§4.7). La vara no lo detectó, así que el verde es insuficiente.
- No se editó `pieza-01-ES.md` en esta ronda. El siguiente trabajo es volver a abrir fuentes válidas para el corte, corregir/retirar las afirmaciones anteriores, cerrar el orden y el registro de sustancia, y ejecutar lectura humana y vara sobre el archivo final exacto.

## Issue de ShinKu: autorización solicitada, pero no publicado

El dueño reiteró que quiere reportar el OOM al upstream [Harrys-HQ/ShinKu](https://github.com/Harrys-HQ/ShinKu), sin adjuntar el backup. Volví a verificar **solo lectura**: Issues está habilitado, pero la identidad autenticada `Alex17273747576777` recibe `permissions.push=false` y `permissions.triage=false` en ese repositorio. El conector de GitHub de Arena está `unsupported`. No hice un segundo POST ni intenté sortear el control de acceso; con esos permisos el issue no se puede crear desde esta sesión. El upstream exige en su formulario pasos, resultado esperado/real, versión de ShinKu, versión de Android y dispositivo. Esos tres datos obligatorios no aparecen en la información recibida y no se inventan.

**Título propuesto (inglés):** Large Mihon backup restore reports OutOfMemoryError during Android trim-memory callback

**Borrador ajustado al formulario oficial (sin adjuntos):**

- **ShinKu version:** missing — must be supplied by the reporter.
- **Android version:** missing — must be supplied by the reporter.
- **Device/model:** missing — must be supplied by the reporter.
- **Steps to reproduce (reported, not independently reproduced):** open ShinKu’s backup restore flow, select a large Mihon-format backup, and start restoration; the reporter says the failure happens at about 10%. The exact menu path/version must be confirmed before submission.
- **Expected behavior:** restore completes, or the app stops with a clear recoverable error instead of exhausting the process heap.
- **Actual behavior:** the reporter supplied this truncated error excerpt:

```text
java.lang.Throwable: java.lang.OutOfMemoryError: Failed to allocate a 24 byte allocation with 199056 free bytes and 194KB until OOM, target footprint 536870912, growth limit 536870912; giving up on allocation because <1% of heap free after GC.
    at android.app.ActivityThread.collectComponentCallbacks(ActivityThread.java:6025)
    at android.app.ActivityThread.handleTrimMemory(ActivityThread.java:6611)
    at android.app.ActivityThread.-$$Nest$mhandleTrimMemory(Unknown Source:0)
    at android.app.ActivityThread$ApplicationThread…
```

  The excerpt ends mid-stack at `ActivityThread$ApplicationThread`; it is not represented as a complete crash log. The OOM is reported around a large-backup restore, but this trace alone does **not** establish that backup decoding caused it. The prior investigation also noted a separate `ThrowableSerializer`/`CrashActivity` path; that trace must not be conflated with this excerpt.
- **Other details:** an earlier owner-provided report described a backup larger than 110 MB and failures at roughly 10%; the exact size, app version, RAM and reproduction environment still need confirmation. No backup file, library contents, account information or private log is attached.

**Engineering hypothesis, not a confirmed cause.** The earlier code review at [`a478592cb040e644f0e222d1fec9b20feba9ff18`](https://github.com/Harrys-HQ/ShinKu/tree/a478592cb040e644f0e222d1fec9b20feba9ff18) found whole-stream `readByteArray()` decoding in `BackupDecoder`, with validation and restoration each decoding. This makes memory pressure plausible, but the code observation is not proof of the user’s runtime path or root cause. Keep it out of the issue unless the reporter confirms that the affected release contains that code.

**Submission gate:** obtain (1) ShinKu version, (2) Android version, (3) device/model, and a write-authorized GitHub route for `Harrys-HQ/ShinKu` Issues. Do not paste a token in chat; configure an authorized, repo-scoped `issues:write` credential locally or ask the maintainer to grant access. Then submit the exact text above after rechecking duplicates and the current issue form. No issue has been created.

Siguiente paso concreto: el dueño aporta los tres datos obligatorios del formulario y habilita `issues:write` en una vía local autorizada; después se publica una sola vez el borrador sin backup ni datos de biblioteca.

## Complemento de lectura factual/editorial de Pieza 01

**Estado de esta pasada:** se releyó la pieza completa y se contrastaron los puntos de mayor riesgo contra documentación primaria. Esto completa el dictamen editorial de esta versión, no la validación de cada cifra/candidato ni la aceptación de la pieza. No se modificó `pieza-01-ES.md`: sus cifras se rotulan al 19-nov, mientras que el corte editorial autorizado es 10-nov; cambiar etiquetas o reciclar las cifras sin una fuente fechada convertiría la contradicción en una afirmación inventada.

### Conteo reproducible y resultado

- Archivo examinado: 546 líneas (`wc -l`); 49.693 bytes, 48.062 puntos de código Unicode y 8.053 elementos separados por espacios (conteos reproducibles con Python `len(read_bytes())`, `len(text)` y `len(text.split())`); SHA-256 `b63b5434b73debf9561e3243392966b540bac5f21dc6356b1b003fa493aa390b`.
- El recuento de 48.062 puntos de código confirma únicamente tamaño bruto. No demuestra las 45.001 letras de sustancia que exige el manual; sigue faltando registro humano por sección.
- No se reconstruyeron estrellas, actividad, versiones ni estados históricos al 10-nov desde respuestas que incluyen datos al 19-nov. Los valores fechados 11–19-nov quedan fuera del corte. No usar esos resultados futuros como «verificación de hoy».

### Contrastes primarios añadidos en esta pasada

1. **F-Droid:** la [FAQ oficial de desarrolladores](https://f-droid.org/docs/FAQ_-_App_Developers/) dice expresamente que los builds reproducibles no son requisito para publicar; la [guía oficial de builds reproducibles](https://f-droid.org/docs/Reproducible_Builds/) indica que el estado se consulta por aplicación. Quedan refutadas las frases «si no se puede reconstruir idéntico, no se publica» y «punto». Reescritura mínima: F-Droid fomenta y muestra comprobaciones reproducibles, pero no las exige de manera universal; revisar la ficha concreta.
2. **Firma de APK:** el [documento de Android Open Source Project](https://source.android.com/docs/security/features/apksigning) confirma que Android admite certificados autofirmados y no hace verificación de CA para esos certificados. La firma permite comprobar la clave/continuidad e integridad desde esa clave; no certifica identidad civil, seguridad del código ni intención. Las analogías «prueba quién la mandó» y «ninguna mesa de mods puede igualarlo» deben acotarse; un cambio de clave es una señal para verificar una migración, no prueba aislada de ataque.
3. **Aurora Store:** la [FAQ oficial](https://auroraoss.gitbook.io/wiki/troubleshooting-and-faqs/faqs/aurora-store) permite el inicio anónimo mediante token dispenser, pero describe solicitudes de búsqueda/descarga y el tráfico asociado al servicio; la lista de paquetes para comprobación de actualizaciones depende de esa función. Se sostiene «puedes no iniciar sesión con tu cuenta personal», no «Google no sabe quién eres ni te perfila» ni anonimato absoluto. La metáfora de «gafas y sombrero» también debe indicar qué información sigue saliendo.
4. **Exodus Privacy:** su [FAQ](https://exodus-privacy.eu.org/en/page/faq/) aclara que hace análisis estático de firmas/clases conocidas, que una coincidencia no demuestra actividad y que la lista puede estar incompleta. Refrasear «te señala quién te va a espiar» como detección de componentes conocidos, con el límite junto al resultado.
5. **Obtainium:** la guía de desarrollador oficial [fijada al commit `ef0eed86adaac91dc9b18f9fde3b045d99ad538b`](https://github.com/ImranR98/Obtainium/blob/ef0eed86adaac91dc9b18f9fde3b045d99ad538b/docs/DEVELOPER_GUIDE.md) trata la instalación silenciosa como opcional y condicionada por ajustes, guardas y el instalador/permisos disponibles. No respalda la frase de que toda versión nueva se descarga e instala «sin que muevas un dedo». Separar vigilar, avisar, descargar e instalar; no prometer ejecución silenciosa universal.
6. **microG:** la [wiki oficial sobre conexiones a Google](https://github.com/microg/GmsCore/wiki/Google-Network-Connections) documenta que registro de dispositivo, mensajería, atestación, autenticación y otras funciones pueden contactar servicios de Google, según servicios y ajustes habilitados. No respalda «no le cuenta tus conversaciones» ni «sin entregarle tus datos». Describir qué función puede conectar y condicionar a configuración; no equiparar microG con desconexión total.
7. **Verificación Android:** la [guía primaria vigente de Android Developers](https://developer.android.com/developer-verification/guides) enumera las siete tiendas participantes para la fase que comenzó el **30-sep-2026** en **Brasil, Indonesia, Singapur y Tailandia**; anuncia expansión global en 2027 para apps en dispositivos certificados. La misma página dice que las apps aún se pueden sideloadear, aunque la experiencia depende de la vía, y que el flujo ADB se mantiene. Así, «esto afecta a todo el mundo que usa Android» como situación ya desplegada es excesivo; «todo el que venda comida necesita licencia» no es una analogía suficiente para explicar alcance, excepciones o los canales. El encabezado debe distinguir la fase regional ya fechada de la expansión posterior.
8. **Licencia de App Manager:** la afirmación del borrador sobre el valor `NOASSERTION` es una respuesta del detector de metadatos de GitHub, no evidencia de que el proyecto no tenga licencia. Los registros del proyecto en [F-Droid](https://f-droid.org/packages/io.github.muntashirakon.AppManager/) y [IzzyOnDroid](https://apt.izzysoft.de/fdroid/index/apk/io.github.muntashirakon.AppManager) atribuyen GPL-3.0; antes de cerrar la ficha hay que fijar la licencia del commit/corte citado y distinguir el campo automático de GitHub del texto legal realmente presente.

### Dictamen por bloques no aceptables aún

- **Presentación y cronología (líneas iniciales, cabecera de tiendas, créditos y notas):** los sellos 19-nov contradicen el corte 10-nov; las cifras vivas carecen de registro por afirmación (URL, commit/release, fecha, evidencia y límite). La nota mezcla datos 14–15-sep con valores 19-nov. No sustituir por una fecha nueva hasta volver a medir cada casa canónica o retirar el dato.
- **Tiendas (ocho fichas):** F-Droid contiene una falsedad ya identificada; Aurora sobrepromete anonimato; Neo-Store contiene una descripción de rastreadores que requiere cotejo con el changelog del corte; Accrescent/Appteka/IzzyOnDroid y Komi Store requieren fijar documentación/commit y la política de publicación. Estrellas, última actividad, versión, mínimo Android, licencia, tamaño de catálogo y cambios recientes quedan sin verificación histórica individual. «Pasa filtros» no puede inferirse solo de estrellas, actividad o existir un repositorio.
- **Instaladores (cuatro fichas):** Obtainium universaliza una modalidad condicional; la pareja Obtainium/ObtainX y las fichas de Omnify y FFUpdater necesitan confirmar relación, estado de mantenimiento, procedencia real de cada descarga e instalación, licencia, versión y fecha desde commits/releases pre-corte. Omnify (11-nov) está explícitamente después del corte.
- **Lupas y utilidades (cuatro fichas):** Exodus presenta detección como espionaje activo; la licencia de App Manager necesita cotejo con la licencia del commit y no solo la etiqueta del API; «limpieza profunda» y residuos de SD Maid SE requieren describir capacidades y límites; el retrato de microG omite salidas de red y dependencia de ajustes.
- **Root/Magisk:** «más respetada», «más usada del mundo» y «la herramienta seria» son superlativos no medidos. Compatibilidad bancaria, Play Integrity, garantía, seguridad y consecuencias dependen de app, dispositivo, fabricante, versión y jurisdicción; el texto los formula con alcance demasiado general. La frase de que mucha gente pierde datos/cuentas por mods no trae fuente o denominador.
- **Sitios de mods nombrados:** se atribuyen modelo de negocio, falta de revisión/cadena de custodia y conducta a sitios concretos. Una pantalla anti-bot no demuestra conducta; «número uno, por definición, número uno en archivos sin revisar» no se sigue lógicamente de un eslogan. Retirar las acusaciones o aportar evidencia específica, contemporánea y atribuida; los permisos son una señal, no prueba de intención.
- **Checklist y FAQs:** permiso «de más = intención de más», cambio de firma = mudanza de dueño/ataque, urgencia, antigüedad del dominio y «sin repo = nadie responde» son heurísticas, no hechos concluyentes. La respuesta legal «en casi todos los países» carece de jurisdicción y fuente; eliminar o acotar a una jurisdicción con asesoría/fuente legal primaria. La guía tras instalar un mod confunde Exodus (no es antivirus) y App Manager (no es un escáner forense de malware) con detección de «lo que dejó atrás». La FAQ de root no distingue causas de fábrica/administración del dispositivo de una modificación maliciosa. La respuesta sobre actualizaciones F-Droid/Obtainium debe distinguir aviso, descarga e instalación.
- **Ejemplos NewPipe/AntennaPod/VLC:** fecha y estrellas son posteriores al corte; «sin que te graben», «sin publicidad» y «reproduce prácticamente todo» requieren límites explícitos (redes/servicios, anuncios incluidos en feeds o contenido y formatos no soportados). «Funciona mejor, respeta más y no te traiciona» no se desprende de licencia abierta o mantenimiento.
- **Glosario, créditos y cierre:** firma, rastreador, licencia libre y sideloading contienen simplificaciones que pueden ser materialmente engañosas; el crédito afirma verificación total que no está trazada; «más de un millón trescientas mil personas» carece de fuente, unidad y corte y contradice el dato no medido de §0.4.
- **Orden/alcance:** el archivo se titula «PARTE 1 de 3» pero termina con el cierre completo y no incorpora las otras partes; aclarar si el documento es una entrega parcial o un maestro. El orden de cierre actual incumple el orden normativo de Notas → meme → firma/remate → Créditos. No aceptar la pieza por la vara verde.

**Conclusión operativa:** la lectura editorial del archivo y el dictamen de riesgos de esta versión están completados; la verificación factual de cada candidato/cifra no lo está. La pieza sigue **NO ACEPTADA** y sin editar. Próximo trabajo factual: conservar evidencia histórica válida al 10-nov o, si no existe, retirar cada número/claim temporal; después corregir afirmaciones técnicas y editoriales con fuentes primarias por afirmación, registrar sustancia por sección y validar orden/lectura humana/vara sobre el SHA final. No iniciar el lote 01–70 hasta cerrar los bloqueos y recibir la lista auténtica de 18.