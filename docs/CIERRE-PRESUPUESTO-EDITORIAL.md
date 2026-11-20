# Cierre del presupuesto editorial de almacenamiento

Referencia temporal de plataforma: 2026-11-10, America/Santo_Domingo. Las cifras siguientes son mediciones de esta ejecución, no una reconstrucción histórica de las marcas del host.

## Resultado

- Archivos regulares al inicio: 73.091.507 bytes en 3.305 archivos, medidos por recorrido del filesystem (no incluye metadata de directorios).
- Se retiraron 31 archivos recuperables que suman 30.514.274 bytes.
- Medición posterior con `du -sb /home/user`, el método de la guarda: **42.590.641 bytes**, antes de escribir esta nota y el helper de persistencia.
- Límite editorial: **50.000.000 bytes**. Cumplimiento demostrado en esa medición. Se vuelve a medir al entregar.
- Cuota de plataforma: 128 MB o 10.000 archivos; es independiente y también queda por debajo según el inventario local. El contador definitivo del snapshot lo determina la plataforma.

## Qué se retiró y por qué es recuperable

- Copias del overlay histórico de atestaciones dentro de EDT: cada archivo se comparó con el SHA de blob del árbol remoto de `Alex17273747576777/entorno-de-herramientas-de-trabajo` en `419db3c9e94d12942494536fa9f243c26521e604` antes de retirarlo.
- Tres WAV, el perfil baseline y las imágenes README de ShinKu: misma comparación contra `Alex17273747576777/ShinKu` en `9aa4683917016827c3208ae5cdd489b64c2916ce`.
- Ninguna versión remota se borró. La omisión local de recursos significa que este checkout reducido no está listo para compilar Android sin rehidratarlos primero; no se confundirá un fallo por archivo retirado con un fallo del código.
- Se conservaron fuentes, tests, reglas, fusiones y modificaciones locales no respaldadas. Ningún token ni backup privado se publicó.

El manifiesto detallado está en `/home/user/WORKSPACE-CLEANUP.json`, clave `editorial_budget_cleanup`: ruta, tamaño, repositorio, commit y blob. Para recuperar un recurso, descargar la ruta del commit indicado y comprobar su hash Git antes de usarlo. No ejecutar una restauración masiva de todo el repo sin volver a presupuestar el espacio.

## Criterio de cierre

La tarea cierra al verificar la publicación de esta nota en la rama de investigación y volver a medir `du -sb /home/user < 50000000`. No se cambió el límite ni se escogió una raíz menor para obtener un verde.
