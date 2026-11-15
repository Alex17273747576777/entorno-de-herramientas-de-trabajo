# Auditoría integral · la-bandita-archivo · 2026-11-14

*Mega censo + autodiagnóstico + crítica + arreglo de «todo lo anterior» del repositorio
`Alex17273747576777/la-bandita-archivo` (rama `main`, cabeza `4d257e9c`, clonado y medido hoy).
Hecho con las herramientas de la casa (`make doctor`, `make verificar`, `tools/vara.py`) y con
censo propio. Cada cifra es medida, no recordada.*

---

## 0 · El hallazgo que ordena todo lo demás

`make verificar` —el autodiagnóstico completo de la casa: registro, sello, vara y autoprueba—
terminó en **«fallos: NINGUNO»**. Las diecisiete compuertas (G0-G17) están verdes. La integridad
reporta **14.819 archivos sellados, 0 alterados**. Y sin embargo el dueño dice que el paquete
«fue de lo peor».

**Esa brecha es el diagnóstico.** Lo dice el propio CORAZON (línea 865):

> «La máquina comprueba forma, coherencia, integridad y presencia. **No comprueba verdad, ni
> criterio, ni novedad.** Una pieza puede pasar las trece compuertas y estar recomendando un
> proyecto muerto… **La compuerta es el suelo, no el techo.**»

El repositorio aprueba su propio examen y suspende en lo que el examen no mide. Lo que sigue es
el censo de eso: lo que está roto **por debajo del suelo verde**.

---

## 1 · Mega censo (medido hoy)

**Repo.** 18.909 ficheros · árbol 257 MB + `.git` 183 MB. Por tipo: 13.918 `.json`, 3.965 `.md`,
557 `.html`, 175 `.py`, 163 `.txt`, 47 `.png`, 30 `.tsv`. Por carpeta: `registry/` 13.466 ·
`ARCHIVO-HISTORICO/` 2.122 · `Arena-Reimagined/` 1.457 · `docs/` 656 · `site/` 526 ·
`catalogo/` 303 · `guia-maestra/` 171 · `tools/` 77 · `corpus-la-bandita/` 29 · `SKILLS/` 22 ·
`attestations/` 15.

**Publicaciones (G0).** 97 piezas con 💓 y dateline: Facebook 45 de cuerpo + 45 comentarios
fijados, WhatsApp 5, POSTS-COMUNIDAD 2.

**Registro (G1/G2/G4).** 6.838 fichas válidas contra el esquema · frescura edad máxima 4 días,
vigentes 6.560, vencidas 0 · actividad: 4.168 vivos, 2.392 dormidos, 278 muertos.

**Integridad (G5/G14).** 14.819 archivos sellados, lote 2026-11-10 · 1 atestación firmada
verificada (Sigstore).

**Compuertas (G0-G17).** Todas verdes. La autoprueba confirma que cada compuerta detecta fallos
sintéticos («la vara es una vara, no un adorno»). En particular **G6 anti-plantilla: repetición
interna máxima 0×** en 97 piezas —el relleno de las 31-40 (27 %) ya no está.

Hasta aquí, la casa se ve impecable. Lo que sigue es lo que la casa no se mira.

---

## 2 · Autodiagnóstico · lo que está roto bajo el suelo verde

### 2.1 Formato: escrito en Markdown, publicado en Facebook (que no lo renderiza)

Medido sobre las 45 piezas de cuerpo de Facebook:

| defecto | piezas | qué pasa en Facebook |
|---|---:|---|
| vallas de código ` ``` ` | **45 / 45** | Facebook no renderiza código: muestra los backticks literales |
| tablas Markdown `\| … \|` | **35 / 45** | Facebook no renderiza tablas: muestra las barras y guiones crudos |

El mapa de la pieza (el árbol `├── └──` dentro de una valla de código) se ve como texto crudo con
backticks. Los encabezados en `*cursiva*` salen con asteriscos. **Las piezas están formateadas
para un renderer Markdown, no para el canal donde se publican.**

Y la casa **ya lo sabe y lo prohíbe**: CORAZON:312 —«tablas pequeñas (**solo WhatsApp: Facebook no
soporta tablas Markdown**)»— y CORAZON:810 —«si el canal rompe formato, se anota en
`docs/ERRATA-<fecha>.md` y **se ajusta el generador, no el texto publicado**». Ninguna de las 45
piezas de Facebook cumple su propia regla de formato. Ninguna compuerta lo detecta, porque no hay
compuerta de «¿esto se renderiza bien en el canal destino?».

### 2.2 Deriva de misión: de código abierto a cultura pop

La doctrina fundacional (Parte 0-BIS, la razón de la v4.0) cita al dueño:

> «el grupo se centra en **la novedad y la complejidad de las aplicaciones de código abierto, no en
> lo popular, lo de moda o lo fácil**.»

Censo de los 45 temas de Facebook, validado pieza por pieza con la compuerta nueva
(`edt/bin/compuerta-canal-y-mision.py`, G19) y contrastado a mano contra las señales crudas
(★, URLs de repo, «repositorio», licencias SPDX) —coinciden en las 45:

- **01-34 · en misión (34 piezas).** Miden software de código abierto: huellas/firmas, reproductores
  de audio, cajas fuertes de contraseñas, listas de permisos, tiendas de extensiones, lectores de
  libros/manga/cómic, descargadores, torrent, teclados, radio, módulos sin root, lanzadores,
  Mangayomi, LNReader, Cloudstream, índices de extensiones. Cada una con repos, ★ y licencia.
- **41, 42, 45 · en misión pese al título.** 41 y 42 miden índices de extensiones (1.554 y 37.188★);
  45 «The Chosen» mide las apps de código abierto con que la gente ve la serie y baja la Biblia
  (20★, 7 repos). No son cultura pop: miden repos.
- **35, 36, 37, 38, 39, 40, 43, 44 · FUERA de misión (8 piezas).** 35 «La Ballenita vuelve al mar»
  (historia personal), 36 «Tu Manga Online» (mide dominios, no repos), 37 «Carta a la manada azul ·
  Chuckie Facundo Cabral», **38 Kung Fu Panda**, **39 Canserbero**, 40 «La lección del sha256»
  (concepto técnico, ningún repo), **43 El Quijote**, **44 Avatar: la leyenda de Aang**. Todas con
  **0 ★, 0 URLs de repo, 0 «repositorio», 0 licencias**.

Evidencia dura —pieza 38 «Kung Fu Panda»:

```
★: 0   URLs github.com: 0   «repositorio»: 0   licencias SPDX: 0
```

Es una pieza sobre tres películas y sus fechas (con `EntityData/Q….json` de Wikidata, que es como
la casa midió la cultura pop), sin un solo recurso de código abierto. Es exactamente «lo popular y
lo de moda» que la Parte 0-BIS prohíbe, y tiene hasta una sección titulada «Por qué esto no es una
reseña». **8 de las últimas 11 piezas abandonaron la misión**, y ninguna compuerta de la casa lo
detecta: G13 (novedad) sólo mira 7 piezas, no las 97, y no hay compuerta de misión.

**Por qué pasó (la causa, no el síntoma).** El 8-nov se derogó el mínimo de 45.000 caracteres
(`bandas.json`: «produjo nueve cuerpos de relleno hechos con `generar_piezas.py`»). Al bajar la
banda a 6.000 y quitar la obligación de medir mucho, el paquete se hinchó de 34 a 45 piezas y el
hueco se llenó con contenido pop corto que **no exige medición**. Se mató el relleno bajando la
vara, y por ese hueco entró la deriva.

### 2.3 Novedad: la doctrina existe, la infraestructura está vacía

La novedad es la razón de ser de la casa (Parte 0-BIS nació del error del 2-nov: proponer Shizuku,
viejo y famoso, en vez del fork nuevo). Lo que se mide hoy:

- `docs/CALENDARIO-DE-NOVEDADES.json` —el registro obligatorio de hallazgos— tiene **~2 entradas
  reales** (más `_nota` y `_regla`). Sin entrada ahí, «un hallazgo no es nuevo: es una opinión» (G13).
- **G13 novedad: sólo 4/7 piezas pasan M24-M28.** Y sólo **7** piezas están sujetas a la compuerta,
  de 97. Las 90 restantes no se examinan por novedad.
- `tools/baseline.json` congela la deuda de la oleada 01: sus piezas no tienen **ningún recurso por
  debajo de ★1.683**, así que M24 las marcaría para siempre. Deuda declarada, no corregida.

Veredicto: la doctrina que justifica la v4.0 está ejercida en ~2 hallazgos y 4 de 7 piezas. La
casa legisló sobre la novedad y casi no la practica.

### 2.4 Contradicción de banda: el CORAZON está viejo contra su propio bandas.json

- **CORAZON v4.1** (corte 3-nov-2026), línea 523: Facebook **40.000-45.000** caracteres.
- **`docs/bandas.json`** (vaciado y rehecho 8-nov-2026): Facebook **6.000-45.000**; el mínimo de
  45.000 «no existe en Facebook —era una vara interna— y produjo nueve cuerpos de relleno».

El propio CORAZON:442 resuelve el conflicto de antemano: «Toda banda vive en `docs/bandas.json`…
**si difieren, manda el JSON y este documento se corrige el mismo día**». El JSON cambió el 8-nov;
el CORAZON sigue en 3-nov con la banda vieja. **La «ley única de la casa» está desincronizada de la
banda que realmente aplica**, en violación de su propia regla de corrección misma-día.

### 2.5 Lo que sí se arregló (para no repetir el error)

G6 anti-plantilla da repetición interna 0× en las 97 piezas: el relleno literal de las 31-40
(27 %, el mismo párrafo siete veces, «Los fichas», «EstaValidación») **ya no está**. Eso se hizo
bien. El problema es que se consiguió **bajando la vara** (45k→6k) en vez de **subiendo la calidad**,
y la vara baja abrió la puerta a la deriva de 2.2. Arreglar un defecto creando otro es el patrón.

---

## 3 · Crítica (honesta, sin adornos)

El paquete está **técnicamente sellado y verde en sus diecisiete compuertas, y editorialmente a la
deriva**. Optimizó pasar su propio examen (forma, presencia, integridad) mientras abandonaba su
misión (verdad, criterio, novedad, código abierto). Escribe en Markdown para una plataforma que
renderiza texto plano. Relajó el largo para matar el relleno y llenó el hueco con listas de cultura
pop que no requieren medir nada. La doctrina de novedad —la razón de la v4.0— se ejerce en dos
hallazgos y cuatro de siete piezas. Y el CORAZON, la «ley única», está viejo contra su propio
`bandas.json`. Nada de esto dispara una compuerta, porque las compuertas miden presencia, no valor.
Por eso es «de lo peor» a pesar de «fallos: NINGUNO»: **la casa se construyó un suelo que no se
moja, y confundió no-mojarse con estar bien.**

La raíz es una: **no hay compuerta de misión ni de canal.** Hay 17 compuertas de forma y cero que
pregunten «¿esta pieza es de código abierto como manda la doctrina?» o «¿este texto se renderiza en
el canal donde se publica?». Lo que no se comprueba, se degrada en silencio —exactamente la familia
de fallas C5/C7/C14 del registro común: el verde que no midió lo que importaba.

---

## 4 · Arreglo (ordenado y consciente de los sellos)

**Orden:** primero lo que evita que se repita (generador + compuertas), luego el contenido, al
final la reestructura por idioma. Reestructurar basura sólo la cambia de sitio.

**A · Formato (mecánico, alta prioridad).** Ajustar `generar_piezas.py` para que la salida de
Facebook sea texto plano + emoji: sin vallas ` ``` `, sin tablas `|` (convertirlas a listas o a
imagen), mapa sin backticks. Es lo que CORAZON:810 ya manda («se ajusta el generador»). Levantar
`docs/ERRATA-2026-11-14.md` por las 45 piezas que rompieron formato en el canal.

**B · Nueva compuerta de canal (la que falta) — HECHA.** `edt/bin/compuerta-canal-y-mision.py`
implementa G18 «formato de canal»: rechaza vallas de código y tablas Markdown en piezas de Facebook.
Resultado sobre el repo: **45/45 piezas de Facebook rompen el renderizado de su canal**. Falta
integrarla en `tools/vara.py` de la casa (toca el repo sellado → ver §5).

**C · Nueva compuerta de misión (la que falta) — HECHA.** La misma herramienta implementa G19
«misión»: toda pieza del ciclo debe medir código abierto (★, URLs de repo, «repositorio» o licencias
SPDX). Validada pieza por pieza contra las señales crudas (coinciden en las 45). Resultado: **8 piezas
fuera de misión** (35, 36, 37, 38, 39, 40, 43, 44). La vara de la casa da «fallos: NINGUNO»; ésta da
ROJO. Sin estas dos compuertas el defecto vuelve en cuanto alguien genere otra pieza.

**D · Misión de las 35-45 (decisión del dueño).** Tres opciones, y es editorial: (i) declararlas
«fuera de misión» y congelarlas como deuda (igual que `baseline.json` hace con novedad); (ii)
moverlas a `POSTS-COMUNIDAD` (que no es serie); (iii) rehacerlas sobre un tema de código abierto.
**No** dejarlas en el ciclo vivo fingiendo que cumplen la doctrina.

**E · Banda (corregir la contradicción).** Actualizar el CORAZON a la banda del `bandas.json`
(6.000-45.000), fechado, como manda CORAZON:442. Decisión del dueño: ¿se queda la banda ancha
(6-45k) o se fija un mínimo real por calidad (no por relleno)?

**F · Novedad (ejercer la doctrina).** Extender G13 a las 97 piezas (no 7). Poblar
`CALENDARIO-DE-NOVEDADES.json` con hallazgos medidos. Exigir banda de descubrimiento por pieza.

**G · Reestructura por idioma (la meta original, al final).** Sólo después de A-F:
`es-dominicano/` (un texto adaptable que sirva a Facebook *texto plano*, WhatsApp *tablas ok* e
Instagram *imagen+epígrafe*) y `En-ingles/` (un texto adaptable para Reddit *largo*, X *hilo*,
Discord *mensaje*), ambas compartidas en Telegram. El generador debe **derivar el formato por
plataforma desde un mismo cuerpo**, no soltar el mismo Markdown en todas. Esto exige rehacer
`bandas.json` (claves `facebook`/`whatsapp` → `es-dominicano`/`En-ingles`), el CORAZON (canales),
`envio.py`, `fijados.py`, `bandas.py` y `make verificar`.

---

## 5 · Lo que NO puedo cerrar yo solo (y por qué)

- **Los sellos.** El repo tiene 14.819 archivos sellados (lote 2026-11-10) y 1 atestación firmada.
  **Toda edición de contenido rompe el sello** y exige re-sellar (`make sellar` / `make ritual`) y
  re-atestar (`tools/atestar.py`) antes de empujar, o `make verificar` y el CI (`vara.yml`) salen rojos.
- **La bóveda.** `make push` exige `GHP_A` (el token de la bóveda, «nunca se imprime»), que no
  tengo. Tengo el PAT del dueño (`GP`) y podría empujar con el helper como en cero-X/edt, pero eso
  salta el ritual de push de la casa. **Empujar cambios a `la-bandita-archivo` necesita la bóveda o
  autorización explícita del dueño para empujar con `GP` + re-sellar.**
- **Las decisiones editoriales** (D y E: qué hacer con las piezas pop y con la banda) son del dueño,
  no mías: se presentan, no se ejecutan.

Por eso este turno entrega el **censo + diagnóstico + crítica + plan de arreglo** (este informe),
medido y con evidencia. La ejecución de A-G va cuando el dueño autorice el push/re-sellado y tome
las decisiones D y E.

---

## 6 · Reproducir esta auditoría

```bash
git clone --branch main https://github.com/Alex17273747576777/la-bandita-archivo.git
cd la-bandita-archivo
make doctor          # VEREDICTO LISTO · integridad 14819 OK
make verificar       # G0-G17 · «fallos: NINGUNO»  ← el suelo verde
# el censo que la vara NO hace:
PUB=Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES
for f in "$PUB"/[0-9][0-9]-*.md; do case "$f" in *fijado*) continue;; esac
  grep -qF '```' "$f" && echo "valla: $f"; grep -qE '^\|' "$f" && echo "tabla: $f"; done
grep -c github.com "$PUB"/38-Kung-Fu-Panda*.md   # 0 → deriva de misión
```

*Medido el 2026-11-14 contra `la-bandita-archivo` @ `4d257e9c`. Las cifras de forma son de
`make verificar`; las de formato y misión, del censo propio de arriba.*
