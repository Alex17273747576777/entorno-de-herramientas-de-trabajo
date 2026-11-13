# entorno-de-herramientas-de-trabajo

*La caja de herramientas de La Bandita · abierta el sábado 8 de noviembre de 2026, Santo Domingo*

Esto no es un esqueleto. Son las herramientas que ya se usaron para medir, y que cualquiera puede repetir en su máquina sin instalar un solo paquete.

**Desde el 2026-11-13 esto ya no es sólo la caja de medición ni sólo un sitio de
publicación.** En [`proyectos/`](proyectos/) cada proyecto vivo tiene su directorio con
lo que no tiene casa en ningún otro repo: recetas de entorno, límites medidos de la
máquina, registro de fallas con su contraparte y registro de respaldos. El código de
cada proyecto sigue en su propio repo; aquí vive lo que se pierde cuando un contenedor
se recicla. Empieza por [`proyectos/README.md`](proyectos/README.md).

---

## 🧰 Qué hay aquí

| herramienta | para qué | estado |
|---|---|---|
| `bin/medir-pieza` | mide una publicación: prosa real, relleno, caracteres útiles, veredicto | funcionando · 11 pruebas |
| `lib/medicion.py` | el motor de medición: párrafos, palabras, cuerpo sin encabezados | funcionando |
| `lib/auditoria.py` | detecta párrafos repetidos literalmente y muletillas de plantilla | funcionando |
| `docs/INFORME-31-40.md` | la auditoría de las publicaciones 31 a 40, con las cifras | listo |
| `muestras/` | los diez archivos auditados + la pieza 01 como molde | listo |
| `tests/pruebas.py` | once pruebas, sin frameworks, salida en verde | 11/11 |

---

## ⚡ En una página

Una publicación larga no es una publicación buena. Esta caja nace de un caso concreto: diez archivos que pesaban 46.300 bytes cada uno y que, al medirlos de verdad, tenían **27.400 caracteres útiles** y el **mismo párrafo repetido siete veces**.

El error de origen es contar bytes de archivo y llamarlo contenido. Así que la herramienta hace lo obvio y lo difícil: separa el **archivo** de la **prosa**, y separa la **prosa** de la **prosa que ya se había dicho**.

Tres números, y con eso se decide:

1. **prosa** — caracteres reales, sin encabezados `#`;
2. **relleno** — caracteres que están repetidos literalmente dentro del mismo archivo;
3. **útil** — la resta. Es el único número que importa.

Si el útil está por debajo de 45.000, la pieza no llega. Si el relleno pasa del 8 %, la pieza se devuelve aunque pese lo que tenga que pesar.

---

## 🛠️ Uso

No hay nada que instalar. Python 3.9 o superior, y ya.

```bash
# una pieza, en detalle
./bin/medir-pieza muestras/p31.md

# un lote, en tabla
./bin/medir-pieza muestras/p*.md --tabla

# para encadenar con otras herramientas
./bin/medir-pieza muestras/p31.md --json
```

Salida real, sin editar:

```
📄 p31.md
   archivo           46,420 bytes ·  45,540 caracteres
   prosa (sin #)   38,029 caracteres ·  6,457 palabras · 141 párrafos
   relleno         10,532 caracteres repetidos (27.7%) en 15 bloques
   ÚTIL REAL       27,497 caracteres
   estado         NO APTO · relleno: RELLENO
   ↳ repetido ×7 (226 car.) Cada release de Kototoro v2.3.12 y el ecosistema…
```

En lote:

```
pieza                                 prosa     útil  relleno    estado
-----------------------------------------------------------------------
p31.md                               38,029   27,497    27.7%   NO APTO
p32.md                               38,015   27,935    26.5%   NO APTO
...
p40.md                               38,002   27,387    27.9%   NO APTO
```

---

## 📐 Las reglas que aplica

| constante | valor | por qué |
|---|---|---|
| `MIN_FACEBOOK` | 45.000 caracteres | el mínimo declarado en CIMIENTOS |
| `MAX_SANO` | 62.000 caracteres | por encima, casi siempre es relleno |
| `RELLENO_TOLERADO` | 8,0 % | deja pasar el repaso deliberado, corta la plantilla |
| párrafo mínimo | 120 caracteres | ignora tablas y separadores decorativos |

Las tres son constantes de módulo, en `lib/medicion.py` y `lib/auditoria.py`. Si el criterio cambia, cambia en un sitio.

---

## ✅ Pruebas

```bash
python3 tests/pruebas.py
```

```
· medicion
  ok    cuenta caracteres
  ok    detecta párrafos
  ok    palabras > 0
· auditoria
  ok    sin repetición = limpio
  ok    detecta repetición
  ok    marca relleno
  ok    cuenta lo repetido
· veredicto
  ok    corto no apto
  ok    largo no apto
  ok    en banda apto
· cli
  ok    json corre

TODO BIEN
```

---

## 🚪 Lo que esta caja NO es

- **No es un generador de publicaciones.** Detecta y mide. No escribe prosa: escribir 46.000 caracteres que valgan la pena exige medir datos reales primero, y eso no se automatiza honestamente.
- **No consulta la API de GitHub todavía.** La siguiente herramienta de la caja (`bin/medir-repo`) sí lo hará; hoy mide texto, que es donde estaba el problema.
- **No tiene dependencias.** Ni `pip`, ni `requirements.txt`, ni entorno virtual. A propósito: la caja tiene que funcionar dentro de cinco años en una máquina ajena.

---

## 🗺️ Lo que viene

1. `bin/medir-repo` — mide un repositorio de GitHub contra la API: estrellas, licencia, entrega, descargas, huella.
2. `bin/traer-piezas` — descarga un rango de publicaciones del archivo y las mide en lote.
3. `bin/comparar-piezas` — mide una pieza contra el molde de las 1 a 30 y dice qué le falta, elemento por elemento de los siete.

---

*Cero paquetes alojados aquí. Cero cuentas. Cero telemetría. Todo lo que hace, se lo hace a un archivo que ya está en tu disco.*

---

## 📁 Capa de proyectos (2026-11-13)

| ruta | qué |
|---|---|
| `proyectos/README.md` | la convención: qué entra aquí y qué no, y por qué ninguna copia de herramienta entra sin su contraparte |
| `proyectos/comprobar-copias.sh` | la contraparte de **todas** las copias: recorre los `MANIFIESTO.sha256` y sale 1 si algo derivó, 2 si no había nada que comprobar |
| `proyectos/LICENCIAS.md` | la licencia medida de cada fuente (GPL-3.0, Apache-2.0, MIT, sin declarar) y qué implica para las copias |
| `proyectos/fallas-comunes/` | 12 fallas del modo de trabajar, no de un proyecto (C1-C11, con C7b); ocho son la misma clase: el éxito que no lo es, C10 es la inversa: el rojo que no lo es, y C11 es el arreglo aplicado a medias |
| `proyectos/cero-X/herramientas/` | `latido.py`, `comprobar_entorno.py`, `preparar-entorno-android.sh`, `low-memory.gradle` |
| `proyectos/gltools-reborn/herramientas/` | censo del APK, auditoría de releases, preparación de firma, verificación de versión + 7 y 15 comprobaciones |
| `proyectos/normas-de-diseno/herramientas/` | 5 procedimientos: censar catálogo, elegir y desmontar, cerrar tramo, incidencias, auditar reglas |
| `proyectos/bandwidth-hero-proxy2/` | registro sin copias, con el motivo medido |
| `proyectos/la-bandita-archivo/` | registro sin copias: 182 herramientas archivadas por etapas |
| `proyectos/cero-X/entorno/` | límites medidos del sandbox (sin KVM, 2 CPU, 1,9 GiB de RAM, techo de Robolectric en API 36) y receta de rearme |
| `proyectos/cero-X/fallas/` | 20 fallas reales con la comprobación que las caza ahora; cinco son la misma clase: el cero silencioso, dos más (17-18) son el verde que no ejecutó nada, y las últimas dos (19-20) son la inversa: el rojo que no significaba nada |
| `proyectos/cero-X/RESPALDOS.md` | fusión de la divergencia con el remoto Git (PR #7, `merged=True`, `main` en `2dc023e`), el detalle histórico de los conflictos, y las copias en Drive con sus hashes |

---

## Licencia de este repositorio

**GPL-3.0** (ver [`LICENSE`](LICENSE)), decidida el 2026-11-13 por compatibilidad: el
repo ya contiene copias de herramientas GPL-3.0 de `cero-X-app`, y las fuentes
Apache-2.0 y MIT de las que también se copia son compatibles en esa dirección. Una
licencia permisiva no habría sido válida: no se puede relicenciar como permisivo el
código GPL-3.0 que ya está dentro. Procedencia de cada copia y razonamiento completo en
[`proyectos/LICENCIAS.md`](proyectos/LICENCIAS.md).

Los seis repos de la cuenta son **públicos por decisión del dueño**, lo que obliga a
que ninguno contenga jamás un secreto:
[`docs/POLITICA-DE-ALMACENAMIENTO.md`](docs/POLITICA-DE-ALMACENAMIENTO.md).
