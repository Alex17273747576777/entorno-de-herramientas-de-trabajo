# Auditoría remota y mantenimiento — 2026-11-10

## Alcance comprobado

Se enumeraron por API los seis repositorios propios accesibles y el repositorio ajeno AniZen se dejó fuera. Se recorrieron íntegramente por streaming 19.528 archivos, 236.902.990 bytes, en snapshots fijados por commit, sin clonar ni guardar archivos en el espacio de trabajo de Arena.

| Repositorio | Snapshot del barrido | Archivos | Bytes |
|---|---|---:|---:|
| cero-X-app | 6facb361a824f5466f6fabea64e98c76aaa8e4b7 | 386 | 4.224.684 |
| normas-de-diseno | 11b5718944f7e35a03de3fd229dd7ac85ba1fc23 | 32 | 1.610.241 |
| gltools-reborn | 8f6e840aa74e181619ecb28d644e970d516a9053 | 143 | 16.127.557 |
| entorno-de-herramientas-de-trabajo | 950bc4b0930e82b231a68e3ba4271dc199aab437 | 41 | 1.529.208 |
| bandwidth-hero-proxy2 | a391df66ba4b9e6219e782b82ac2332afc9645ed | 20 | 197.185 |
| la-bandita-archivo | 8bef36307d6c19661a6b4cbf0db8cf3b50702b08 | 18.906 | 213.214.115 |

El barrido de esos bytes no encontró coincidencias con los patrones buscados de tokens GitHub, claves privadas PEM y claves AWS. Esto no prueba ausencia universal de secretos, no sustituye una revisión semántica línea por línea y no es un barrido independiente de todo el historial y de todas las ramas. Se habilitaron escaneo de secretos/protección de pushes donde faltaban y alertas/actualizaciones de seguridad de Dependabot en los seis repositorios; en la consulta realizada no había alertas abiertas de secretos.

## Cambios aplicados

- **cero-X:** clave debug retirada del árbol actual; APK de idiomas y APK debug movidos a cuarentena privada en una release en borrador. La copia del segundo se comprobó por SHA-256 antes de retirar el original público. Se corrigieron exclusiones de backup/transferencia, wrapper, validación criptográfica y confianza explícita de extensiones. El cargador verifica una copia privada de sólo lectura, y la inspección de contrato no ejecuta DEX. Sin certificados aprobados se rechaza la carga, de forma deliberada. También se corrigió un requisito inválido de pip (`sqlite3` es stdlib), la descripción minSdk/targetSdk y el recuento de pruebas.
- **normas:** notas de publicación comprobadas antes de mutar/publicar; incidencias sin temporales globales ni interpolación de títulos, con etiquetas opcionales y paginación; scripts ejecutables y regresiones en CI. Se respetaron cambios concurrentes del propietario, incluido el arreglo de los errores de red del censo. El kit ya no impone paleta violeta/degradados.
- **GLTools:** procedimiento de publicación sincronizado, permiso INTERNET retirado del código actual, alias de colores/degradados artificiales eliminados, CI de compilación y núcleo. Notas de 1.10, 1.11 y 1.12 reconstruidas con los commits y diferencias reales entre etiquetas, sin cambiar los APK.
- **medición:** el veredicto estricto usa prosa única y la CLI sale con 1 cuando falla, también en JSON y tabla. Pruebas con relleno repetido en verde.
- **proxy:** autenticación y dominios permitidos obligatorios; destinos DNS privados/reservados bloqueados; no se siguen redirecciones ni se reenvían cookies/autorización del cliente. Límites de tamaño, tiempo y píxeles; errores de origen tratados sin acceder a datos inexistentes. Dependencias actualizadas y fijadas, lockfile generado/probado en Actions, npm ci y CodeQL en main. La clave pública de despliegue de Netlify se recreó con la misma clave, pero sólo lectura. No se cambiaron secretos ni variables del despliegue.
- **La Bandita:** manifiesto canónico sincronizado con el lote, sin autorreferencia; verificación independiente del cambio de día; fecha de la casa; cosign y acción instaladora fijados, comprobación oficial de confianza/identidad. La validación final detectó que `vencimiento --peor` alteraba dos archivos sellados: se corrigió para que sea sólo lectura y se añadió una regresión. Se eliminaron únicamente ramas demostrablemente fusionadas, no contenido histórico.

Se validaron de forma independiente las 14.819 huellas del lote nuevo contra el snapshot revisado. Las modificaciones posteriores de archivos cubiertos se acompañaron de sus huellas, TSV e índice; no se deshabilitó la compuerta de integridad. Los commits concurrentes se respetaron sin pushes forzados.

## Comprobaciones con evidencia

- [Cero-X Android: 393 pruebas descubiertas, 387 ejecutadas, 6 omitidas; 0 fallos/errores](https://github.com/Alex17273747576777/cero-X-app/actions/runs/42867247425).
- [Metadatos Python corregidos](https://github.com/Alex17273747576777/cero-X-app/actions/runs/42868363742).
- [Auditoría criptográfica de 40 APK públicos GLTools: 40 firmas válidas y 40 SHA-256 coincidentes](https://github.com/Alex17273747576777/gltools-reborn/actions/runs/42869155754).
- [Auditoría criptográfica del APK público de cero-X: firma y SHA-256 válidos](https://github.com/Alex17273747576777/cero-X-app/actions/runs/42869160420).
- Los dos APK de cero-X puestos en borrador se descargaron por streaming para recalcular sus hashes y extraer sus certificados; el workflow con GITHUB_TOKEN de sólo lectura sólo enumeró el APK público, no esos borradores. No se presenta como verificación criptográfica de los tres.
- Los resultados JSON de las auditorías están en los artefactos `auditoria-publicaciones` de sus respectivas corridas, no en Arena.
- El hash publicado del APK release antiguo de cero-X ya coincidía con el recalculado; ese punto del informe anterior no se confirmó.

### Hashes independientes de cero-X

| Artefacto | SHA-256 | Estado |
|---|---|---|
| idiomas, 488.710.587 bytes | a8d86ebb66aa7d54412161009f532bb1d57a8b31c967ba8c025598ace7f18461 | borrador/cuarentena; certificado público 726314d8… |
| debug, 87.401.796 bytes | 80621e692f487cae5d7a47d951cfe6236f8f7f067e4d260e46f0f7aa1df87948 | borrador/cuarentena; mismo certificado público |
| release, 475.572.663 bytes | 086876ac89431f30458572f3ede508c5a76dca223180e42e1134f3596f41a8bb | público; certificado f03505ce… |

## Pendientes que no se declaran terminados

1. **Claves de publicación:** no había secretos de Actions configurados en ninguna de las dos apps. Búsquedas acotadas por nombres/extensiones de claves en Drive y Dropbox no dieron coincidencias; esto no demuestra ausencia en todos los respaldos posibles. El custodio debe configurar las claves legítimas por un canal seguro. No se publicaron APK nuevos con las correcciones, ni se generó una firma incompatible para aparentar una actualización.
2. **Tokens expuestos:** necesitan rotación/revocación y sustitución por credenciales con mínimo permiso. No se guardaron ni incluyeron en repositorios, informes o URLs. No se revocaron automáticamente sin asegurar continuidad de acceso y reemplazo seguro.
3. **Extensiones y módulos incompletos:** falta catálogo autenticado/consentimiento, prueba positiva con una extensión aprobada y revisión funcional de módulos. Un ClassLoader no es aislamiento de permisos. [Seguimiento y criterios de cierre](https://github.com/Alex17273747576777/cero-X-app/issues/6).
4. **Pruebas en dispositivos:** no se afirma que apps, superposición, contraste, instalación o migración hayan sido comprobados en un teléfono. Compilar y aprobar tests JVM no lo demuestra. El issue de diseño GLTools #7 sigue abierto porque su criterio es más amplio que quitar alias.
5. **Archivo histórico:** se detectaron 742 copias adicionales idénticas (12.691.251 bytes). No se borraron evidencia, cachés o bases de datos indiscriminadamente. [Clasificación pendiente](https://github.com/Alex17273747576777/la-bandita-archivo/issues/1).
6. **Privacidad del historial:** existen metadatos personales históricos. Además, por un error del agente, los primeros commits de este mantenimiento heredaron el nombre/correo personal predeterminados de la cuenta; los siguientes se crearon con alias/noreply. No se ocultó el error ni se publican aquí los valores. Retirar metadatos ya publicados exige reescritura coordinada y tratamiento de refs/cachés; no se hizo un push forzado sin autorización específica.
7. **Despliegue del proxy:** hay que configurar un secreto nuevo `PROXY_TOKEN`, `ALLOWED_HOSTS` y clientes compatibles en el proveedor de despliegue. El código rechaza tráfico sin esa configuración. El despliegue en vivo no se declaró verificado.

La auditoría queda abierta para estos bloqueos. Un verde de CI no se usa para darles cierre ficticio.
