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
