# Cotejo semántico de §9.9 y revisión factual de Pieza 01 ES

**Estado: cotejo semántico de las 70 unidades completado en esta revisión, con nueve correcciones de matriz; la aceptación del manual y de la pieza siguen pendientes.** Este documento no declara el contenido listo para publicar.

## Corte, archivos y límites

- Fecha autorizada de referencia: **2026-11-10, America/Santo_Domingo**. El dueño aclaró que **2026-11-19 era una fecha prevista**, no un corte histórico ni la fecha actual. El reloj del sandbox y las cabeceras `Date` del API de GitHub devolvieron 2026-11-19; se registra el conflicto y no se usan esos días futuros como corte local.
- Manual cotejado y corregido: `proyectos/la-bandita/manual-v0.0.1/MANUAL-v0.0.1.md`, SHA-256 final de esta ronda: `c83c11fe98bff4049f32f572226d52ba31d8e12856ba134367f1923f2e7e9bbc`.
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

## Issue de ShinKu: borrador no publicado

El upstream [Harrys-HQ/ShinKu](https://github.com/Harrys-HQ/ShinKu) tiene Issues habilitadas. El POST autorizado para crear el reporte falló con **HTTP 403: `Resource not accessible by personal access token`**; no se creó issue. No se reintentará con ese token. El borrador no incluye ni adjunta el backup privado.

**Título propuesto (inglés):** Large Mihon backup restore fails early; possible high memory use during decode

> I’m reporting a restoration failure with a large backup created by Mihon. The reported file is over 110 MB and contains about six to eight years of library and reading-history data. The user reports default settings and a failure at roughly 10% of restore. Some reported backups of 36–45 MB also fail; this does not establish a fixed size limit.
>
> Code observations at `a478592cb040e644f0e222d1fec9b20feba9ff18`: `BackupDecoder.decode()` reads the entire (possibly gzip-decompressed) input with `readByteArray()` and then decodes it in memory; no explicit size limit was found in this path. `BackupFileValidator.validate()` decodes the file, and `BackupRestorer.restoreFromFile()` decodes it again during restoration. This makes high memory pressure plausible, but it does **not** establish the root cause of the reported failure or prove that the restoration route caused the OOM.
>
> The separately reported trace mentions a 512 MiB heap and `GlobalExceptionHandler$ThrowableSerializer.deserialize` → `CrashActivity.onCreate`. In the inspected code, that serializer decodes a stringified exception for the crash screen; this trace is not proof that backup decoding caused the crash. No device reproduction or memory profile was performed. Mihon is the format reported by the user; Komikku and Yōkai compatibility were not independently tested.
>
> Could the maintainers assess whether the validation/restore flow can avoid decoding the full backup twice, use a bounded/streaming strategy, and add regression tests with synthetic large backups under constrained memory? Please advise what non-private diagnostics (app version, Android/device/RAM, exact file size, steps, or a redacted log) would help. No personal backup is attached.

**Rutas de código citables:** [`BackupDecoder.kt`](https://github.com/Harrys-HQ/ShinKu/blob/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/data/backup/BackupDecoder.kt), [`BackupFileValidator.kt`](https://github.com/Harrys-HQ/ShinKu/blob/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/data/backup/BackupFileValidator.kt), [`BackupRestorer.kt`](https://github.com/Harrys-HQ/ShinKu/blob/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/data/backup/restore/BackupRestorer.kt), [`GlobalExceptionHandler.kt`](https://github.com/Harrys-HQ/ShinKu/blob/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/crash/GlobalExceptionHandler.kt), [`CrashActivity.kt`](https://github.com/Harrys-HQ/ShinKu/blob/a478592cb040e644f0e222d1fec9b20feba9ff18/app/src/main/java/com/shinku/reader/crash/CrashActivity.kt).

Siguiente paso concreto: cuando exista una vía con permiso de escritura para el upstream, pegar este borrador sin adjuntos; antes, esperar la lista auténtica de 18 lecciones y corregir la pieza 01 tras abrir fuentes con un corte temporal compatible.