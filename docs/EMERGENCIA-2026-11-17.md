# Chequeo y autodiagnóstico de emergencia · 2026-11-17 16:04Z

*Orden del dueño: diagnosticar el progreso de lo pedido y vaciar el espacio local conservando sólo
`work/cero-X-app`, `work/edt` y el llavero. Esto es el diagnóstico, fechado y con la fuente de cada
cifra. La hora es la de GitHub (`Date:` de `api.github.com`), no la del reloj del sandbox.*

## 1 · Estado de lo pedido, frente por frente

| frente | estado real | verificado por | qué falta |
|---|---|---|---|
| **ShinKu · i18n del tope** | PR **#37 abierto**, `mergeable=True`, 2 commits, +53/−22, 21 ficheros, 2 comentarios míos | API `pulls/37` | que el mantenedor lo revise. **No está compilado**: `spotlessCheck` falla antes por 1.113 violaciones preexistentes en 621 ficheros de su `main` |
| **ShinKu · #32 #33 #34 #36** | **cerrados**; #34 y #36 fusionados y publicados en v2.8.3 | API `issues/N` | nada |
| **normas-de-diseno · #1 #2** | **cerrados** los dos (auditor publicado + segundo censo real y su diff) | API + `GET` de verificación aparte | nada; la tendencia exigiría un tercer censo |
| **la-bandita-archivo · #1** | **cerrado** (`bfaa811b`: 545 duplicados clasificados, 0 para borrar; caché declarada evidencia sellada; política de `registro.db`/`.tmp`) | API + `make verificar` EXIT=0 | — |
| **la-bandita-archivo · #2 #3** | **abiertas**, creadas por mí hoy con criterio de cierre | API | #2 huella de contenido del registro; #3 el sha256 que el docstring promete y el JSON no lleva |
| **gltools-reborn · #3** | **abierto** a propósito: el criterio es un parte real de teléfono. El código del parte mejoró en `d9c743f` (13 casos ejecutados) | API + arnés Kotlin en JVM | un dispositivo. Sin él no se cierra |
| **gltools-reborn · #1 #2 #5 #6 #8** | **abiertos** (6 en total con #3) | API | todos exigen pantalla, superposición, ROM o batería reales |
| **cero-X-app · #6** | **abierto**; el lockfile sí está corregido y vigilado (`855547210c`, workflow `dependencias-js` visto correr en verde, run 44076096239) | API + `actions/runs` | 4 criterios, y el primero (clave privada legítima por canal seguro) **no depende de mí** |
| **AniZen · #94 #95** | **abiertos, 0 comentarios**, `master` sin mover desde 2026-11-15 | API | respuesta del mantenedor. Frente bloqueado |
| **Frente Nox** | PR #3 cerrado **sin fusionar** (FALLA-010); la implementación fue adoptada con crédito en `anime-fonte-extensoes#9` | registro de la FALLA | nada que hacer sin el binario correcto del otro lado |

**Progreso global ponderado: 73,4 %** (7.489 / 102 de peso; aritmética de Python sobre la tabla de
`docs/AUDITORIA-PROGRESO-2026-11-16.md`, no de cabeza).

## 2 · Lo que sujetaba el número, dicho sin adornos

No son los repos ajenos. Son tres cosas:
1. **Seis issues de gltools que exigen un dispositivo** que este contenedor no tiene (ni `/dev/kvm`).
2. **AniZen, que no responde** (peso 12 al 35 %).
3. **El CI de ShinKu no compila nada** porque `build_check.yml` sólo corre `on: [pull_request]` y su
   `main` acumula 1.113 violaciones de formato sin que nadie las vea. Ofrecido el barrido como PR
   aparte; sin esa decisión, ningún PR mío ahí se puede verificar compilando.

## 3 · Verificación previa al borrado (lo que hizo seguro borrar)

`local == remoto` en los seis frentes, comprobado por API y no por confianza:

| repo | HEAD local | HEAD remoto |
|---|---|---|
| cero-X-app | `855547210c` | `855547210c` ✓ |
| normas-de-diseno | `fe45074d35` | `fe45074d35` ✓ |
| gltools-reborn | `d9c743fcb2` | `d9c743fcb2` ✓ |
| la-bandita-archivo | `bfaa811b40` | `bfaa811b40` ✓ |
| edt | `3aac7d3055` | `3aac7d3055` ✓ |
| ShinKu (fork, rama `feed-cap-i18n`) | `34cf4048ca` | `34cf4048ca` ✓ (cabeza del PR #37) |

El único «DIVERGE» que salió en el barrido era falso: comparaba la rama del PR contra `Harrys-HQ/ShinKu`,
donde no existe; vive en mi fork, y la cabeza del PR #37 coincide.

## 4 · Seguridad

- **Llavero en `644` otra vez** tras un reinicio — el patrón exacto de FALLA-006. Corregido a
  **`600`** (y el directorio a `700`) en esta ronda. Contenido intacto: las ocho claves
  (`GP_EXPLORA_1/2/3`, `GP`, `GHP_A/B/C`, `GP2`) con las mismas longitudes y huellas.
- **Los tokens se pegaron en el chat** al dar la orden, así que están en el registro de la
  conversación. Recomendación: **revocar y regenerar** los cuatro distintos (`GHP_A/B/C` y `GP`); desde
  aquí no se puede.
- **Ningún token se publicó**: `grep -rlE "ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"` dio
  **0 coincidencias** sobre el respaldo nuevo, sobre los diez directorios originales y sobre los
  `.git/config` de lo conservado. Los empujes se hacen con `GIT_ASKPASS`, nunca con el token en la URL.

## 5 · Qué se conservó y qué se borró

**Conservado (por orden):** `work/cero-X-app`, `work/edt` (con su remoto configurado y al día) y
`/home/user/.cerox-keys/tokens.txt`.

**Respaldado dentro de edt antes de borrar** — `respaldo-2026-11-17/`, 524 ficheros, 8.049.466 B, con
manifiesto y huella por directorio: los diez directorios de trabajo que **no eran repos git ni tenían
copia** (`ai-107-respaldo`, `auditoria-apks`, `biblioteca-masiva`, `ci`, `feed-novedades`, `gltools`,
`latest`, `nox-index-pb`, `referencias`, `vm`) y las dos guías de la raíz.

**Borrado:** el resto de `/home/user` (incluidos `google_drive` y los originales ya respaldados), todo
`/var/tmp` (1,7 GB: JDK 499 MB, kotlinc 436 MB, los clones, `reikai` 100 MB) y `/tmp` salvo
`arena-workspace` (ktlint 69 MB, los proyectos A/B de yarn, censos sintéticos).

**Reconstruible:** `bash entorno/restaurar-toolchain-kotlin.sh` devuelve JDK 17, kotlinc 2.3.10 y
2.0.21 y los jars; ktlint y yarn tienen receta en `proyectos/feed-novedades/pr37/KTLINT-COMO-ORACULO.md`
y `proyectos/cero-X/HERRAMIENTAS.md`. Los clones se re-clonan; `/tmp/ap.sh` (`GIT_ASKPASS`) se recrea
con dos líneas y está dicho en `proyectos/cero-X/HERRAMIENTAS.md`.

**Se paró el vigilante** (`vigilar-frentes.sh`, pid 12308) antes de borrar el directorio desde el que
corría; su guion va en el respaldo.
