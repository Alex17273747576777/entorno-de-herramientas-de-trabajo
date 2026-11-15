# Estado de variables — ronda 2026-11-15 16:07:52Z (no perder nada)

Fijado al abrir la ronda y verificado contra la realidad en ese momento.

| Variable | Valor verificado | Fuente de la verificación |
|---|---|---|
| T0 de la ronda | `1794758872` = **16:07:52Z** · fin **16:47:52Z** (`T0+2400`) | `date -u +%s` en la llamada de apertura; copia en `/var/tmp/T0-nueva-ronda.txt` (volátil) |
| Cuenta GitHub | `Alex17273747576777` (id 191147158) | `GET /user` con el token del llavero |
| Llavero | `/home/user/.cerox-keys/tokens.txt` · 638 B · modo 0600 · claves `GP_EXPLORA_1/2/3`, `GP`, `GHP_A/B/C`, `GP2` | `ls -la`; los tokens **no se revocan** (decisión del dueño, FALLA-006 cerrada) |
| cero-X | `/home/user/work/cero-X-app` · HEAD `7d108e17e6a2a7e8f37e3fae8219eb37896b18d6` == remoto · árbol limpio · CI 43718120579 y 43719391526 success (628/0/0/15) | `git rev-parse` + `git ls-remote` + logs de CI |
| edt | `/home/user/work/edt` · HEAD `16c351d5122730efe5ecc4374b324e822b2ecc85` · remoto vacío | `git rev-parse` |
| Frente Nox | PR #3 `open`, 0 comentarios, head `6711284aa49d7289a1cefe2e3f271ba5bd8e434f`; canónico `/home/user/work/nox-index-pb/anime-index.pb` 17.663 B, blob `17b50912…` | última línea de `vigilancia.log` (15:30:16Z) + API |
| Vigilante | `vigilante-pr-3-issues-32-94-08e70660` → `work/feed-novedades/vigilancia.log` · **última línea 15:30:16Z** ⇒ no sondeó a las 15:40/15:50/16:00: **el proceso no sobrevivió al cambio de turno**; hay que re-arrancarlo (hecho en esta ronda) | `tail` del log + ausencia de líneas nuevas |
| Clones feed | `/var/tmp/feed/shinku` 110 MB @ `043ab7d8e68e8a77752805c34969a2477195826a` (main) · `/var/tmp/feed/anizen` 33 MB @ `95160a724d1147777dd1f7997fff4885a4cd9deb` (master) · **árboles prístinos (0 cambios)** tras generar los parches | `du -sh` + `git status --porcelain` |
| Clon Reikai (nuevo) | `/var/tmp/reikai/reikai` 100 MB @ `00206fe6ae0c6cf87e2f6114b59164ea295a6fd1` (main, Apache-2.0, ★48) | `git rev-parse` + API |
| Clones Nox | `/var/tmp/nox/{manga-extensoes,anime-extensoes,nox-extension-developer}` siguen presentes | `ls -d` |
| Issues feed | ShinKu **#32** (31.291 chars) · AniZen **#94** (29.954 chars), ambos `open`, con parches verificados `git apply --check` | `GET` tras cada PATCH (15:30:11Z / 15:30:12Z) |
| Parches | `work/feed-novedades/parches/{shinku-fase2-tope25-e-idioma.patch (4.499 B), anizen-fase2-tope25-por-pestana.patch (3.877 B)}` | `ls -la` |
| Herramientas ausentes | `kotlinc`/`kotlin`, Android SDK y Gradle ⇒ **nada de Kotlin se puede compilar aquí**; `bc`, `column`, `xxd` ausentes | `which` |
| Escribible fuera de `/home/user` | sólo `/var/tmp` y `/usr/local/src` | experiencia de la sesión |

Reglas activas que dependen de estas variables: rondas de 40 min exactos con cada acción
registrada y verificada; cero push directo en repos ajenos (sólo issue/PR); tokens nunca
impresos ni citados; cero `present_file` (las rutas van en el chat); espejar ficheros y
ediciones el mismo turno; horas de bitácora tomadas del reloj/mtime/API, nunca de memoria
(FALLA-009).

---

## Actualización de las 21:44Z (ronda post-apagón, T0=1794777722)

### Utillaje NUEVO que existe ahora (y cómo recuperarlo tras un reinicio)

Todo vive en `/var/tmp`, o sea **se barre en cada reinicio**. El restaurador está en la casa:

```bash
bash /home/user/work/edt/entorno/restaurar-toolchain-kotlin.sh            # descarga lo que falte (~2-3 min)
bash /home/user/work/edt/entorno/restaurar-toolchain-kotlin.sh --comprobar  # sólo verifica rutas
```

| Herramienta | Ruta | Por qué esa versión |
|---|---|---|
| kotlinc 2.3.10 | `/var/tmp/kc-2.3.10/kotlinc/bin/kotlinc` | es el `kotlin_version` de ShinKu (`gradle/libs.versions.toml:7`) |
| kotlinc 2.0.21 | `/var/tmp/kc/kotlinc/bin/kotlinc` | respaldo; **no** lee los metadatos de kotest 6 |
| JDK 17 Temurin | `/var/tmp/jdk/jdk-17.0.13+11/bin/java` | JUnit 6 exige class file 61.0 y el sandbox trae Java 11 |
| jars | `/var/tmp/jars/` | kotest 6.0.7 (ShinKu) y 5.9.1 (AniZen), consolas JUnit 6.1.2/6.1.3, coroutines 1.10.2, `logcat-real-classes.jar` |

Trampas registradas: Maven devuelve **554-730 bytes de HTML** en un 404 y `curl -sSL` lo guarda como si
nada (el restaurador lleva guarda `<5000`); `com.squareup.logcat` se publica como **AAR**, hay que
extraerle `classes.jar`; y su versión `0.4` no está servida a esta máquina (se usó la 0.1, declarándolo).

### Frentes externos a las 21:44Z

| Frente | Estado | Commit / tamaño |
|---|---|---|
| ShinKu PR **#34** (Fase 1 biblioteca) | open, CI en `action_required` (espera aprobación de mantenedor por ser fork) | 2 commits, 4 ficheros, +147 · head `306cfeecce3e` |
| ShinKu rama `feed-tabs-phase1` (Fase 1 feed) | pública en el fork, **sin PR** porque se apila sobre #34 (43 sigue a 42) | `0b157a0669a4`, 3 ficheros, +68 |
| AniZen rama `merge-groups-phase1` (Fase 1 biblioteca) | pública en el fork + diff dentro de #95 (su `AGENTS.md` prohíbe PR) | `b435e3fa3b5c` |
| AniZen rama `feed-cap-per-tab` (Fase 2 feed) | pública en el fork + diff dentro de #94 | `f5f1bdd824a4` |
| Issues | #32 (35.408) · #33 (26.474) · #94 (29.906) · #95 (35.057) · todos `open`, 0 comentarios | — |
| Awerkori PR #3 (índice pb) | open, 0 comentarios | head `6711284aa4` |

Vigilante: **nueve frentes**, guion en `work/nox-index-pb/vigilar-frentes.sh`, log en
`work/feed-novedades/vigilancia.log`.

### Evidencia ejecutada (reproducible desde la casa)

| Qué | Dónde | Resultado |
|---|---|---|
| Tests de `dedupeByMergeGroup` (7 casos, estilo de cada repo) | ramas publicadas | `7 tests successful / 0 failed` en ambos |
| Interactor real `InsertFeedSavedSearch.await` + doble de repositorio | `work/biblioteca-masiva/mediciones/Arnes.kt` | `SIN FALLOS`, 9 ✓ (frontera 24/25, por pestaña, `awaitAll` sin tope) |
| Mediciones lineal vs cuadrático | `mediciones/medida-kotlin.txt`, `medida-sql.txt` | 27,50 ms (50k entradas) frente a 14,30 ms **por entrada** del escaneo; 330× |
| Migración `43.sqm`: limpia vs actualización | `mediciones/validar_migracion.py` | `SIN FALLOS`, 13 ✓ (`PRAGMA table_info` idéntico, 11 consultas) |
| Guard de procedencia de AniZen | `scripts/check-provenance.sh` del propio repo | `0 violation(s), 0 warning(s)` → `✓ ok` |
