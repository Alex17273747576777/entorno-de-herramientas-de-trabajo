Build de release en commit `1fdad3595de1378fa745f70112d6d8e65152dfec`.

## Incremento real

- Índices Project Nox fijados por commit: 1.618 extensiones de manga y 273 de anime.
- Explorador Kotatsu multi-parsers: 3.662 entradas, 1.113 marcadas rotas; NSFW y rotas ocultos por defecto.
- Resolución de GitHub Releases bajo demanda, caché externa, límite de descarga, SHA-256 y certificado Project Nox antes de abrir el instalador de Android.
- Biblioteca Kisara local: búsqueda AND/comillas/exclusiones/campos, favoritos individuales y por lote, fusión sin sumar capítulos duplicados.
- Auditoría y licencias documentadas en `docs/AUDITORIA-FUENTES-Y-KISARA.md`.

## Verificación

- 526 pruebas JVM: 0 fallos, 0 errores, 8 saltadas.
- CI `43255661160`: success. Builds ARM64 `43256585847` y universal `43256591698`: success.
- MangaDex 1.6.5 real: 103.438 bytes, hash y firma APK v2 Project Nox coincidentes.
- Índices reales: 1.618 manga / 273 anime / 3.662 Kotatsu parseados correctamente.

| APK | Bytes | SHA-256 |
|---|---:|---|
| `app-arm64-v8a.apk` | 21.570.286 | `2a643ba30a0d0025ff961dc5bedc8f3ab69ffa537a2adcec13bf213b22f0750c` |
| `app-universal.apk` | 16.924.359 | `c7889415479d010af75a39f2d623f9544a0e453c320143983c1f6bd3e94e71f4` |

## Límites explícitos

La instalación Nox se etiqueta **para Mihon/Aniyomi**. El contrato antiguo de cero-X no equivale a `extensions-lib 1.6`: esta release NO demuestra ejecutar esos APK dentro del lector. Los JAR Kotatsu se exploran como metadatos, no se ejecutan. Un hash/firma prueba integridad y firmante, no seguridad o disponibilidad del sitio. No se instaló esta build en el LG V60 ni se validó visualmente; tampoco se verificó una respuesta de contenido de MangaDex ni una conversación con credenciales IA reales.
