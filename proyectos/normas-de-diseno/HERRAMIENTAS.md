# normas-de-diseno · herramientas

Fuente canónica: [`normas-de-diseno`](https://github.com/Alex17273747576777/normas-de-diseno)
rama `main` @ `b3e224218f34` (medido el 2026-11-13; 41 ficheros, **sin licencia
declarada**, 1.561 KB). Copiadas de `procedimientos/`. Ver `proyectos/LICENCIAS.md`.

Son procedimientos, no librerías: cada uno es un tramo de trabajo completo con su porqué
en la cabecera. Sirven para cualquier proyecto Android que publique APK.

| fichero | bytes | sha256 | qué hace |
|---|---:|---|---|
| `01-censar-catalogo-appteka.py` | 5,532 | `50568d575c9e3cc0` | censa el catálogo de Appteka categoría por categoría por su API interna `/api/proxy/list`. Leer el HTML da una foto falsa: sólo trae la primera página y lo más reciente |
| `02-elegir-y-desmontar.sh` | 2,731 | `e071f24b3a73fb78` | elegir apps de las que aprender y desmontarlas. Mirar capturas no basta: el diseño vive en Compose, no en `res/`, así que `aapt2` solo no lo cuenta |
| `03-cerrar-tramo.sh` | 10,074 | `51d13ea22f5f2327` | cerrar un tramo: probar, firmar, publicar, dejar constancia. Son 18 pasos y siempre se olvida uno; la vez que se olvidó el `versionCode` el APK se instaló encima del anterior sin actualizarse |
| `04-incidencias.sh` | 3,734 | `d84c568f25217e16` | crear incidencias por API sin temporales ni interpolación de títulos en código |
| `06-auditar-reglas.sh` | 4,318 | `217d42d3ebd30b06` | auditar las reglas: si están todas, si se numeran sin saltos y si el disco coincide con el repo. Nació de un `git status` con cuatro permisos cambiados, sin remoto y cuatro commits sin subir |

Comprobación de deriva: `./proyectos/comprobar-copias.sh`.

## Lo que deliberadamente NO se copió

Los tres tests de la fuente (`tests/test_procedimientos.py`, `test_habilidades.py`,
`test_kit_diseno.py`) **no están aquí**, y se probó antes de decidirlo:

```text
$ python3 -B test_procedimientos.py     # copiado solo a /tmp/prueba-nd
Ran 7 tests in 0.062s
FAILED (failures=1, errors=5)
```

Resuelven `ROOT = Path(__file__).resolve().parents[1]` y recorren `ROOT/"procedimientos"`,
o sea que esperan la forma del repo entero. Copiados sueltos no prueban nada: serían un
cascarón que parece cobertura. Sus comprobaciones siguen corriendo en el CI de
`normas-de-diseno`, que es donde tienen sentido.

Los cinco procedimientos sí son autocontenidos: `01` habla con la API de Appteka, `04`
con la de GitHub y `06` con `normas/` de su repo, pero ninguno importa un módulo hermano.
