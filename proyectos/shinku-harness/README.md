# Comprobación JVM aislada de grupos protobuf

Ejecuta `python3 run.py /ruta/a/BackupStreamDecoder.kt` con Java, Python y acceso a Maven Central. Sin argumento busca el checkout reducido de ShinKu vecino a EDT. Descarga las dependencias a un directorio temporal fuera del repositorio, verifica los SHA-256 registrados y lo elimina al terminar. Los hashes fijan bytes de esta prueba; **no** acreditan independientemente la identidad del proveedor ni son una auditoría de dependencias.

`Models.kt` define modelos sintéticos mínimos con los mismos campos raíz necesarios para compilar el decoder; no representa las clases ni datos completos de producción. `Test.kt` usa el archivo real pasado por ruta y prueba roundtrip con un registro sintético, grupos con profundidad 64 y 65, cierre distinto, grupo truncado, número de campo inválido por fuera y dentro, y cierre inesperado. La prueba de 64 fija el límite actual, no demuestra que sea un valor óptimo o compatible con todos los backups legítimos.

No ejecuta JUnit del proyecto, compilación Android, validador, restaurador, base de datos, muestras reales ni benchmark/memoria del dispositivo. El prototipo conserva listas completas y no tiene memoria constante. Está disponible para reproducir una comprobación acotada, no para declarar cerrada la PR.
