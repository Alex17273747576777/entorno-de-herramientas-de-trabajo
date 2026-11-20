> **Nota de archivo histórico:** El cuerpo siguiente describe una etapa anterior y no debe interpretarse como estado actual. Posteriormente se publicó el bug https://github.com/Harrys-HQ/ShinKu/issues/40, la solicitud de compatibilidad https://github.com/Harrys-HQ/ShinKu/issues/41 y la PR de investigación https://github.com/Harrys-HQ/ShinKu/pull/42 (commit 9aa4683917016827c3208ae5cdd489b64c2916ce). La nueva traza sitúa el OOM en deserialización protobuf durante validación. Se preparó un prototipo y pasaron comprobaciones JVM aisladas; el build Android sigue sin validar. Las afirmaciones antiguas de «no se publicó/no se modificó/no se compiló» se conservan únicamente como registro de aquella etapa. No hay mejora de rendimiento medida ni solución final validada.

# ShinKu 2.8.5-preview.1 — investigación de memoria en restauración Mihon

**Referencia temporal de la investigación inicial:** 2026-11-10 (no es la fecha de cierre ni publicación).  
**Alcance:** borrador técnico listo para revisión; no se modificó ShinKu ni se ejecutó una compilación.

## Resumen ejecutivo

El reporte describe un fallo de memoria durante una restauración de backup Mihon grande, aproximadamente al 10%. El fragmento de stack disponible es incompleto: informa un `OutOfMemoryError` durante `ActivityThread.handleTrimMemory`, con límite de crecimiento del heap de 512 MiB, pero no identifica la operación de ShinKu que agotó la memoria. En la fuente de `v2.8.5-preview.1` se observó que el decoder materializa todo el contenido (descomprimido, si aplica) en un `ByteArray` antes de deserializarlo; el validador y el restaurador llaman al decoder en etapas distintas. Es una ruta de investigación fundada en código, no una causa raíz probada.

La entrega concreta de esta investigación es el borrador de issue en `docs/SHINKU-2.8.5-PREVIEW-1-OOM-ISSUE-DRAFT.md` y el plan de evolución que sigue. El issue no se publicó: faltan datos del dispositivo/versión y una identidad con permiso de escritura. No se adjunta backup.

## Evidencia y límites

| Elemento | Observación | Confianza / límite |
|---|---|---|
| Ref del prerelease | `v2.8.5-preview.1` → `a478592cb040e644f0e222d1fec9b20feba9ff18` | SHA consultado con `git ls-remote`; no hay checkout local. |
| Error aportado | `OutOfMemoryError` al no poder asignar 24 bytes; quedan 199056 bytes libres y 194 KB hasta OOM; heap target/growth limit 536870912 bytes; menos de 1% libre después del GC. Stack incluye `collectComponentCallbacks` y `handleTrimMemory`, termina truncado en `ActivityThread$ApplicationThread`. | Es evidencia suministrada por la reportante; stack incompleto, sin frame de ShinKu, no permite atribuir causa raíz. |
| Escenario descrito | Restaurar backup Mihon de más de 110 MB, con unos 6–8 años de biblioteca/historial; falla cerca de 10%. | No se verificaron tamaño exacto, compresión, pasos completos, versión afectada ni dispositivo. |
| `BackupDecoder.kt` | Detecta gzip/JSON y usa `readByteArray()` para cargar el contenido completo antes de la deserialización protobuf. | Lectura estática en el tag indicado; posible pico de memoria. No se midió consumo. |
| `BackupFileValidator.kt` / `BackupRestorer.kt` | Validación y restauración decodifican URI en llamadas distintas. El restaurador vuelve a llamar al decoder para comenzar la restauración. | Sugiere decodificación duplicada entre etapas; no prueba que objetos/bytes coexistan ni que ello cause el OOM. |
| Build local | OpenJDK 11; `ANDROID_HOME` y `ANDROID_SDK_ROOT` no definidos; `sdkmanager` no disponible. | No se ejecutó `./gradlew assembleDevRelease`; no hay resultado de compilación. |
| Publicación del issue | Intento previo POST devolvió 403; los permisos observados no incluyen `push` ni `triage`. | No reintentar con esa credencial; se requiere permiso autorizado. |

## Backlog priorizado para una evolución sustantiva

### P0 — conseguir diagnóstico reproducible

1. **Confirmar reporte mínimo:** versión exacta afectada, modelo, versión Android, RAM, espacio libre, tamaño exacto del archivo, gzip/no gzip, origen/variante del backup y secuencia exacta. Solicitar versión mediante datos de Acerca de o nombre de APK; no pedir contenido privado.
2. **Reproducir sin datos personales:** crear backups sintéticos Mihon de tamaños escalonados y con distribuciones realistas (muchos registros pequeños y entradas grandes). Comparar ZIP/gzip y entradas con historial/extensiones. Reproducir en heap limitado y en emulador/dispositivo con poca RAM.
3. **Perfil de memoria por fase:** medir heap nativo/Java y tiempo antes/después de selección, validación, parseo y aplicación de entradas; conservar traces redacted y tamaño del archivo, no biblioteca privada.

### P1 — rediseñar el flujo de importación/restauración (propuesta; validar primero con la API protobuf y el formato real)

4. **Inspección sin decodificar dos veces:** separar validación superficial del encabezado/estructura de la semántica completa; o conservar el resultado de una única decodificación, con límite de vida claro. No retener byte array y grafo de objetos simultáneamente más de lo indispensable. Verificar si el formato permite leer desde `InputStream`/`BufferedSource` con la biblioteca actual; no presuponer que protobuf puede decodificarse en streaming sin cambios de formato.
5. **Control de límites antes de inflar datos:** límites configurables/defensivos para tamaño comprimido y descomprimido, bytes leídos, número de entradas y tamaños de cadenas/payloads, con mensajes claros. Evitar una bomba gzip; no fijar límites arbitrarios sin comparar con backups legítimos grandes.
6. **Aplicación por lotes si el formato lo permite:** procesar/referenciar elementos gradualmente y liberar buffers; conservar progreso honesto. Si el esquema obliga a materializar el backup completo, diseñar alternativa incremental compatible (p. ej., migración de formato/versionado) en vez de simular streaming.
7. **Consistencia de restauración:** definir explícitamente si se restaura de forma atómica o parcial. Si hay parcialidad, reportar cuántas categorías/elementos se aplicaron y permitir reintento seguro. No prometer rollback/atomicidad sin soporte y prueba.
8. **Errores recuperables:** capturar condiciones conocidas (entrada demasiado grande, gzip corrupto/truncado, protobuf inválido, falta de espacio) y mostrar acción segura. No intentar ocultar un OOM genérico que deja la app en estado incierto.

### P2 — regresión, compatibilidad y observabilidad

9. **Pruebas de formatos:** gzip y sin comprimir; tamaños habituales y grandes; todos los campos/categorías; esquemas/versions históricas compatibles; entradas truncadas y corruptas; fuentes desconocidas; cero elementos.
10. **Pruebas de memoria:** test bajo heap acotado que valide memoria pico/ausencia de doble parseo; Android instrumentation en dispositivo de baja RAM cuando esté disponible. Evitar assertions frágiles basadas en bytes exactos de GC.
11. **Seguridad y privacidad:** no registrar URLs privadas, títulos, historial, tokens ni texto del backup. Telemetría opcional debe ser agregada y consentida; no habilitar carga de backups.
12. **Build y revisión:** seguir `CONTRIBUTING.md`: probar `./gradlew assembleDevRelease`; añadir tests pertinentes; revisar compatibilidad congelada de paquetes de fuentes/red, sin cambios fuera de alcance.

## Criterios de aceptación propuestos

- Un backup grande, gzip y no comprimido, restaura en una prueba de memoria limitada o termina con error recuperable y sin dejar un falso éxito.
- El mismo archivo no se decodifica por duplicado sin motivo documentado; el pico de memoria y el tiempo se comparan con una línea base reproducible.
- Archivos corruptos, truncados y sobredimensionados se rechazan con mensajes seguros, sin OOM intencional ni logs de datos privados.
- Casos de compatibilidad históricos se cubren con fixtures sintéticos/no personales.
- La política sobre restauración parcial/atómica queda probada y reflejada en el resultado al usuario.
- `./gradlew assembleDevRelease` y la suite relevante pasan en un entorno con Android SDK; adjuntar la versión de JDK/SDK y resultados. Hasta entonces el build se considera no verificado.

## Próximas acciones verificables

1. Obtener de la usuaria los campos de contexto faltantes y permiso/identidad de publicación autorizados, sin pedir backup ni secretos.
2. Revisar el borrador del issue, buscar duplicados en el tracker y publicar una sola vez con identidad autorizada, guardando la URL/ID y el contenido enviado.
3. En rama de trabajo de ShinKu, preparar pruebas sintéticas/benchmark y perfil de la ruta actual; no tocar los paquetes de fuentes/red congelados.
4. Elegir solución de memoria a partir de mediciones y contrato del formato; implementar, probar compatibilidad, ejecutar build y documentar comparación antes/después.
5. Entregar la rama/commit revisable y resultados. No marcar la evolución como terminada hasta superar criterios de aceptación.

## Estado de esta ronda

Se consultaron el release, `BackupDecoder.kt`, `BackupFileValidator.kt`, `BackupRestorer.kt` y `CONTRIBUTING.md` mediante fuentes públicas. No se clonó ShinKu, no se modificó código ni configuración, no se compiló, no se publicó issue y no se adjuntó material privado. Por tanto, esto es una propuesta técnica priorizada y un borrador utilizable, no una implementación ni cierre del reporte.
