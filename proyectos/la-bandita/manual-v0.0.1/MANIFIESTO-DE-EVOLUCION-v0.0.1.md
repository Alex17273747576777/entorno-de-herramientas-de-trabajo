# Manual de Estilo y Operaciones — La Bandita · v0.0.1

## MANIFIESTO DE EVOLUCIÓN (entrega fundacional)

> **Versión:** 0.0.1 — numeración reiniciada por mandato expreso del dueño.
> **Fecha prevista:** el dueño aclara que 2026-11-19 era una fecha prevista para el reinicio/edición, no la fecha histórica del mandato ni la fecha actual. La fecha de plataforma para esta sesión es 2026-11-10 (America/Santo_Domingo); el reloj del workspace marca 2026-11-19 UTC y está nueve días adelantado, una diferencia que no se explica por zona horaria. No usar el reloj del workspace para cortes; hasta nueva evidencia, la fecha de plataforma gobierna.
> **Naturaleza:** este documento ARRANCA la v0.0.1. No resume el pasado: define hacia dónde muta la norma.
> **Estado:** el cuerpo operativo de las Partes 0–X ya está redactado; la aceptación final sigue pendiente y no se declara completo mientras haya incoherencias abiertas.
> **Relación con lo anterior:** la v0.0.1 REEMPLAZA al «Manual de Campo v4.0» como norma vigente;
> el v4.0 pasa a antecedente histórico archivado, decisión ratificada por el dueño (§5, decisión 3).
> **Autocontrol mecánico:** en la última pasada de esta sesión, la suite histórica de 10 pruebas y `py_compile` pasaron (no es el recuento actual de pruebas); `--modo-norma` dio VERDE al manual y a este manifiesto. El resultado no prueba coherencia semántica completa, preservación de las 18 lecciones ni veracidad de los hechos históricos.

---

## §0 — Por qué una evolución y no un parche

El dueño lo dijo claro: las reglas corrían el riesgo de volverse **decoración** — bellas en el papel, ausentes en la práctica. Una regla que nadie verifica es una regla que nadie cumple. Y una regla que nadie cumple es peor que no tenerla, porque finge protección donde no la hay.

Tres hechos volvieron necesaria la evolución, no el remiendo:

1. **La operación debe diseñarse para una audiencia declarada diversa, sin convertir el brief en estadística verificada.** El dueño declara literalmente «1,358M usuarios», más de 200 cuentas, presencia en varias plataformas y un público objetivo de 30–40 años. La notación y su fuente no se han cotejado; no se publican como alcance medido hasta aclarar la unidad y abrir evidencia con fecha. Los cuatro perfiles lectores del manual son arquetipos de diseño, no segmentos medidos. Una norma pensada para cuarenta amigos puede quedar chica; se conserva la honestidad de fondo («sin soporte oficial, sin promesas») sin inflar ni inventar el alcance.

2. **El modelo de publicación se simplificó y se hizo más exigente a la vez.** Antes: versiones separadas por plataforma, con gemelas idénticas byte a byte para Facebook y WhatsApp. Ahora: **una pieza maestra por idioma**, con listas agrupadas por idioma: ES Facebook·WhatsApp como pareja y Telegram aparte; EN Reddit·Discord; X/Twitter excluida. Cada destino puede requerir presentación o fragmentación propia, sin crear otro maestro ni alterar hechos, riesgos o veredictos. Meta: **más de 45.000 caracteres de sustancia verificada en cada idioma**; si el tema no da, se amplía con evidencia pertinente o se detiene, nunca con cadáveres, bombas de tiempo o relleno.

3. **La pedagogía se volvió obligatoria.** El método Feynman deja de ser un consejo simpático y pasa a ser norma de redacción: cada concepto se explica con palabras de la calle y comparaciones cotidianas, como si el lector no supiera nada. Lo que no se entiende solo, está mal escrito y se rehace.

«Evolucionar» significa aquí una cosa concreta: **seleccionar lo que sirve, llevarlo a su máximo potencial y volverlo cumplible de verdad**. No borrar la historia: depurarla. No inflar el reglamento: hacerlo ejecutable.

---

## §1 — Lo que se CONSERVA intacto (porque es oro)

Esto funcionaba y define el alma de la casa. Se hereda sin cambios de fondo:

- **El método Feynman** como obligación de claridad en toda regla y pieza: se dice qué exige, por qué existe, cómo se reconoce en la práctica y qué pasa si falla; al enseñar un concepto técnico se usa la progresión de §2.6 (nombre sencillo, analogía específica, precisión, comprobación y consecuencia). No se fuerza una analogía donde reste claridad.
- **Los cuatro pilares del oficio:** verificación, trazabilidad, legibilidad, honestidad. (En la v0.0.1 se convierten además en compuertas — ver §2b.)
- **La prueba única antes de publicar:** *«¿Qué ayuda esto a decidir mejor y qué le evita perder a quien lee?»* Si la respuesta no sale, no se publica. Sigue siendo la regla madre.
- **La voz editorial:** cálida, curiosa, directa, humana. Como hablarle a un amigo, no a un cliente. Ni solemnidad, ni propaganda, ni tecnicismo gratuito.
- **La lista de frases prohibidas sin excepción** (superlativos comerciales, autoridad vacía, llamadas a instalar sin leer, metáforas gastadas). Se hereda y se amplía ligeramente en §3b.
- **La ficha rigurosa** de cada recurso: nombre con grafía respetada, URL completa y abierta, estrellas al corte, versión con fecha, push, licencia textual sin traducir, descripción citada del repo entre comillas (o declaración de su ausencia), y notas de la casa.
- **La taxonomía de fallos por familias** (A veracidad, B calibración, C alcance, D seguridad/privacidad, F interacción/rol). Se hereda entera y se le añade una familia nueva (§3b).
- **El meme del corte + el remate propio + la firma** como cierre ritual de toda pieza.
- **Las notas al pie fechadas** (mudanza, verificación final, corte, corrección, pendiente). Sin fecha, no existen.
- **El checklist final** previo a la entrega.
- **Las 18 lecciones que el manifiesto declara del dueño**, fechadas del 11 al 15 de septiembre, son doctrina viva y sus citas deben preservarse sin alteración. **Pendiente de integridad:** §1.2 del manual solo muestra 15 entradas y la búsqueda local y búsquedas dirigidas por título/frase en Google Drive y Dropbox no localizaron la nómina fuente completa; eso no prueba que no exista en otro lugar. No afirmar que las 18 están preservadas hasta cotejar el corpus o recibir confirmación expresa del dueño. Se añade mecanismo para integrar lecciones nuevas (§3e).
- **El protocolo anti-prisa y de hornadas:** una hornada buena vale más que cinco apuradas; corregir una pieza vale más que publicar dos nuevas.

Razón de conservar todo esto: cada elemento es memoria pagada con errores reales. Descartarlo sería repetirlos.

---

## §2 — Lo que se RENOVA (misma alma, mejor cuerpo)

### §2a — Modelo de publicación: de «por plataforma con gemelas» a «por idioma, multiplataforma»

- **Antes:** una versión por red; Facebook y WhatsApp idénticos byte a byte; topes creativos por red.
- **Ahora:** UNA pieza maestra por idioma, con listas agrupadas por idioma: ES trata Facebook·WhatsApp como pareja y Telegram por separado; EN agrupa Reddit·Discord. X/Twitter queda excluida. Cada destino puede exigir presentación o segmentación propia, pero no crea otro maestro ni autoriza cambios de hechos, riesgos o veredictos. Meta de sustentación: más de 45.000 caracteres de sustancia verificada en cada idioma.
- **Topes sanitarios:** los límites duros por red (p. ej. lo que un mensaje de WhatsApp o un post soportan) NO limitan la creación; sirven únicamente como guía de **despliegue fragmentado** (cómo partir la pieza al publicarla en una red corta). Se crea en grande y se despliega con criterio.

### §2b — De pilares-valores a pilares-compuerta

Cada pilar se vuelve verificable, idealmente por máquina:

| Pilar | Antes (valor) | Ahora (compuerta humana/mecánica y alcance real) |
|---|---|---|
| Verificación | «hay que verificar» | cada dato decisivo se vincula a fuente abierta y fecha mediante registro humano; la vara no abre ni certifica fuentes |
| Trazabilidad | «hay que poder rastrear» | URL/ruta + SHA o cita atribuida; la persona comprueba el vínculo. La vara no valida enlaces, hashes ni autoría |
| Legibilidad | «hay que ser claro» | método Feynman + mapa visual de emojis-índice + lectura humana; la vara cuenta caracteres y revisa patrones, no comprensión ni estructura |
| Honestidad | «hay que ser honesto» | límites declarados, correcciones fechadas y sin promesas incumplibles; la vara solo detecta una lista cerrada, no juzga promesas rotas ni fechas |

El mecanismo que materializa esto es la **vara ejecutable** (§3a).

### §2c — Firma canónica: se zanja la colisión heredada

El sistema arrastraba DOS fórmulas de cierre en documentos distintos:
- Manual v4.0: *«La Bandita informa a partir de fuentes fechadas.»*
- Versionado multiidioma: *«La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.»*

Dos firmas vivas generan deriva. **Decisión ratificada por el dueño («procede»):**
- **Firma textual normativa** (obligatoria, invariable): **«La Bandita informa a partir de fuentes fechadas.»**
- **Lema identitario / remate recurrente** (con alma, flexible): **«Las estrellas adornan; las fechas mandan.»** usado como remate propio, no como firma.

Ninguna fórmula se pierde; se reparten los papeles. La pieza 01 rehecha aplica esta decisión ratificada.

### §2d — La métrica madre, puesta a la escala real

«Crecer sin que la confianza se diluya» se mantiene como norte. El brief declara «1,358M» y edades objetivo 30–40, pero la cifra no se presenta aquí como medida independiente hasta aclarar su notación y fuente. Consecuencia editorial: cada pieza debe servir a varios modos de lectura — aprender (Feynman), ir al grano (enlaces y veredictos), resolver dudas (advertencias claras) y leer como adulto (sin paternalismo). Son criterios de diseño, no resultados de una encuesta. Corolario: 5 piezas verificadas valen más que 20 apuradas; una corrección a tiempo vale más que dos piezas nuevas.

### §2e — Créditos obligatorios como sección normativa

Toda pieza incluye una sección de créditos jerarquizada y al final:
1. A los creadores de cada recurso/herramienta/app citado (autor o mantenedor + enlace a su casa).
2. Al diseño y la metodología (de qué prácticas de cada plataforma se tomó prestado).
3. A la información y la verificación (fecha y método del corte).
4. **Cierre fijo:** a **Arena AI** (asistencia en la construcción) y a **Alex17273747576777** (creador de La Bandita), en ese orden, al final.

Compatibilidad con P10: se acredita a autores PÚBLICOS de software (usuarios/repositorios publicados), lo cual es buena práctica de atribución; NO se reproducen datos personales de terceros colaboradores/amigos/receptores, que siguen protegidos.

---

## §3 — Lo que se AÑADE (máximo potencial)

### §3a — La vara ejecutable: reglas convertidas en compuertas

Se incorpora `vara_bandita.py` como órgano permanente de cumplimiento. Principios:

- **La vara muerde primero a quien la sostiene:** se auto-testea contra las piezas del propio operador antes de confiar en ella (el fallo operativo histórico #12, «no auto-testear la vara», se eleva aquí a norma permanente).
- **Sin vara en verde, no hay publicación.** El veredicto VERDE / VENTANA / ROJO es parte obligatoria de toda entrega al dueño.
- **Checks actuales:** frases prohibidas; superlativos absolutos para revisión; autoridad vacía; meta-comentarios; promesas incumplibles; firma, meme, notas al pie y banda de longitud. La ejecución y los códigos de salida se documentan en Parte IV.
- **Límite de automatización:** la vara informa sobre reglas mecánicas; no redacta, no reescribe ni decide qué creer. VERDE no certifica veracidad, valor editorial ni originalidad: siguen siendo responsabilidad de quien investiga y revisa.
- **Auditoría normativa:** `--modo-norma` omite únicamente los fragmentos didácticos delimitados por `<!-- VARA:MENCION:INICIO -->` y `<!-- VARA:MENCION:FIN -->`. La pieza pública se audita en modo estricto, sin exenciones por cita. Marcadores desbalanceados o anidados bloquean la norma.
- **Hoja de ruta de checks futuros:** auditoría estructural completa (mapa, en-una-página, fichas con campos obligatorios); detección de URLs citadas sin nota de apertura; contraste de citas contra el repositorio cuando haya acceso; conteo y firma por idioma.

### §3b — Nueva familia de fallos: Familia E (Evolución y Cumplimiento)

Institucionaliza el aprendizaje de esta jornada. Se suma a A/B/C/D/F:

- **E01 — Regla-decoración:** regla que se escribe pero nunca se verifica ni se cumple. Antídoto: toda regla nace con su check en la vara, o no nace.
- **E02 — Vara no auto-testeada:** confiar en la compuerta sin pasarla por una pieza conocida. Antídoto: auto-test obligatorio.
- **E03 — Superlativo absoluto comercial:** <!-- VARA:MENCION:INICIO -->«la mejor», «imprescindible», metáforas gastadas como «la navaja suiza de…»<!-- VARA:MENCION:FIN -->. Antídoto: criterio declarado («a juicio de esta ficha…», «según su repo…»).
- **E04 — Firma cambiante / colisión de fórmulas:** dos documentos mandan cierres distintos. Antídoto: firma canónica única (§2c).
- **E05 — Expansión con chatarra:** engrosar una lista con cadáveres o bombas de tiempo para llegar a la meta. Antídoto: curaduría estricta; si no hay recurso bueno, se declara el hueco.
- **E06 — Promesa de completitud falsa:** presentar una entrega parcial como si fuera el total (refuerzo del C01). Antídoto: declarar alcance en números y listar pendientes con fecha.
- **E07 — Riesgo de convergencia por aprobación:** una aprobación local se generaliza sin permiso. Es prevención documentada, no se afirma que el incidente haya ocurrido. Antídoto: registrar alcance y exigir autorización expresa para extenderlo.
- **E08 — Auditoría parcial descrita como total:** se prueba una copia temporal recortada y se reporta como resultado del archivo íntegro. Antídoto: correr el modo normativo sobre el archivo completo, con menciones delimitadas y ruta/SHA.
- **E09 — Conteo bruto confundido con sustancia:** el contador supera el umbral sin demostrar contenido útil. Antídoto: mantener cuenta humana por sección y separar ese resultado del piso mecánico.

### §3c — Casos vivos: los fallos REALES de esta jornada, como primera jurisprudencia

Igual que el v4.0 traía sus doce fallos operativos históricos, la v0.0.1 nace con los suyos documentados (cometidos por el operador al construir la pieza 01, y atrapados por la vara):

| Caso | Fallo | Cómo se corrigió | Lección |
|---|---|---|---|
| Dos usos de la metáfora de herramienta multiuso vetada | frase prohibida (E03) | reformulado con criterio declarado | la metáfora gastada está prohibida aunque suene bien |
| Firma histórica distinta a la del manual | colisión de fórmulas (E04) | firma textual del manual + lema como remate | dos firmas = deriva; se zanja y se declara |
| Ausencia de sección «Notas al pie» | deuda de estructura | sección añadida con notas fechadas | la trazabilidad fechada no se negocia |
| Falso positivo de la vara ante «mejores prácticas» | herramienta sin afinar (E02) | allowlist con/sin tilde | la vara también se revisa; no es infalible |

Estos casos se citarán en el cuerpo del manual como ejemplos negativos con nombre y apellido. La evolución aprende de lo que pasó de verdad.

### §3d — Identidad: separación interno / público

- **Documento normativo interno:** conserva el nombre doctrinal del dueño, Alexis Placencia, y sus lecciones fechadas (coherente con §1 del corpus).
- **Piezas públicas:** acreditan al dueño por su handle, **Alex17273747576777**, junto a Arena AI, según lo ordenado.
- Razón: el rigor doctrinal interno no exige exponer identidad personal en cada pieza pública.

### §3e — Mecanismo de integración de lecciones nuevas

Cuando el dueño dicta una lección nueva (entre sesiones o durante una), se registra fechada y se evalúa si modifica una regla. Si la modifica, se actualiza la v0.0.x con nota de cambio y se recalibra la vara si aplica. Las lecciones no se pierden: entran al canon con fecha.

### §3f — Ejecución secuencial y anti-convergencia por aprobación

Se añade a la v0.0.1 tras la corrección del dueño: el trabajo debe dejar pasos, evidencias y condiciones de salida; «aprobado» significa aceptación local del artefacto y alcance indicados, no permiso tácito para imitarlo en futuras respuestas. La innovación se sustenta en una necesidad y evidencia propias; si no hay aporte nuevo, se declara actualización/corrección o se detiene la repetición. Los prompts genéricos no sustituyen investigar, y la vara no genera ni reescribe contenido. El procedimiento con puertas G0–G7 y ejemplos auditables queda en el cuerpo normativo, §0.6–0.7.

Esa norma ya no es solo prosa: `manual-v0.0.1/guarda_lote.py` la ejecuta. Tiene dos subcomandos: `verificar` (piso mecánico por maestro, similitud por shingles con umbral 0,32 contra referencias, orden de la bitácora con override `--aceptar-riesgo` siempre motivado y registrado, medición de /home/user contra 50.000.000 bytes y `--exigir-git` para exigir seguimiento de git) y `estado` (lee la bitácora JSONL y reporta verificaciones, ROJOs pendientes y almacenamiento sin confiar en la memoria). Sus pruebas están en `test_guarda_lote.py`. Lo que no puede demostrar —veracidad, originalidad, sustancia— lo declara en su salida y sigue siendo responsabilidad humana por archivo.

---

## §4 — Lo que se DESCARTA / archiva (obsoleto por la nueva realidad)

- **La división rígida por plataforma** con gemelas byte-a-byte Facebook/WhatsApp. Pasa al archivo histórico. La unidad de trabajo es ahora la pieza por idioma.
- **Los topes por red como techo creativo** (WA ≤ 63k, FB ≤ 40k usados para limitar la creación). Sobreviven solo como guía de despliegue fragmentado (§2a).
- **La autodescripción pública de «proyecto pequeño entre panas».** Se conserva la honestidad de «sin soporte oficial, sin promesas» y se deja de tratar esa frase como una regla vigente. La escala está declarada por el dueño como «1,358M» y más de 200 cuentas, pero no se ha verificado ni interpretado; no se presenta como alcance real comprobado hasta aclarar unidad, fuente y fecha.
- **El v4.0 como norma vigente.** Pasa a antecedente archivado; nada de su contenido útil se pierde: lo bueno vive dentro de la v0.0.1, lo superado queda citado como historia.

---

## §5 — Decisiones canónicas ratificadas

El «procede» del dueño ratifica estas cinco decisiones y autoriza continuar la redacción por hornadas. El alcance de esa aprobación es esta lista; no convierte por sí solo cada formulación, pieza futura o preferencia no expresada en regla permanente:

1. **Firma y lema** según §2c (firma textual del manual como obligatoria; lema histórico como remate).
2. **Modelo de publicación** por idioma, pieza maestra única y >45.000 caracteres de sustancia en cada edición; ES Facebook·WhatsApp juntas y Telegram aparte; EN Reddit·Discord; X/Twitter excluida (§2a).
3. **Alcance:** la v0.0.1 REEMPLAZA al v4.0 y reinicia la numeración; el v4.0 se archiva como antecedente.
4. **Identidad:** nombre interno en la norma; handle Alex17273747576777 + Arena AI en piezas públicas (§3d).
5. **Vara ejecutable** como compuerta obligatoria antes de toda publicación (§3a).

---

## §6 — Mapa del manual v0.0.1 y estado de entregas

El manifiesto fija las decisiones ratificadas; el cuerpo de Partes 0–X ya está redactado en el archivo operativo. El cotejo cruzado de 70/70 unidades tiene informe en `docs/REVISION-EDITORIAL-2026-11-10.md`; esta continuación leyó íntegros cuerpo y manifiesto y corrigió la incoherencia de polaridad de §3.6/§9.9, sin dar por cerrado el control de lecciones. La aplicación factual y de sustancia en piezas reales sigue pendiente; no se declara el manual terminado.

| Parte | Contenido | Estado |
|---|---|---|
| -1 | Manifiesto de evolución y decisiones canónicas | 🔶 decisiones ratificadas; el registro se actualiza junto al cierre de aceptación |
| 0 | Fundamentos como compuerta, prueba única, pilares y secuencia G0–G7 | 🔶 texto redactado; 70/70 encabezados tienen fila en la matriz; cotejo de cobertura semántica documentado; falta cerrar la integridad de lecciones y la aceptación final; la fecha 19-nov quedó rotulada como prevista, no como corte |
| I | Dueño, voz, estilo, humor, actitud y límites | 🔶 texto redactado; el conteo de lecciones está en conflicto (15 visibles/18 declaradas); aceptación pendiente de cotejo |
| II | Anatomía de pieza por idioma, mapa, fichas, despliegue, notas y créditos | 🔶 hornada 2 redactada; ES agrupa Facebook·WhatsApp y separa Telegram; EN agrupa Reddit·Discord; X/Twitter excluida; aplicación en piezas pendiente |
| III | Matriz permitida, condicional y prohibida | 🔶 hornada 2 redactada; aplicar y revisar consistencia |
| IV | Evidencia, auditoría, vara y pruebas | 🔶 protocolo escrito; 8 pruebas originales de vara + 2 de cobertura estructural, ampliadas con 10 de cierre y 5 de guarda; la revisión factual y de sustancia sigue siendo humana aunque la suite pase |
| V | Ambigüedades y regla de desempate | 🔶 hornada 3 redactada; revisar cobertura contra casos reales |
| VI | Taxonomía A–F y familia E | 🔶 E07–E09 ya se clasifican en §6.3 (riesgo, incidente y brecha); su cierre probatorio depende de repetir auditoría íntegra y validar la cuenta de sustancia en piezas reales |
| VII | Flujo de producción y checkpoint | 🔶 hornada 4 redactada; validar con la producción del lote 01–70 |
| VIII | Métricas, auditoría y deriva | 🔶 hornada 4 redactada; validar denominadores y evidencias en los lotes reales |
| IX | Registros, anexos y glosario | 🔶 hornada 5 redactada; revisar que sean registros, no prompts de contenido |
| X | Promesas, límites y cierre | 🔶 hornada 5 redactada; falta verificación final de coherencia |

Principio de honestidad de la entrega: Partes 0–X escritas no equivale a aceptación final. Lo que aparece como 🔶 requiere la revisión señalada; hasta resolverla, el manual está redactado pero no completo.

---

## §7 — La última regla, renovada

La Bandita no gana por tener el tratado más grande. Gana cuando una regla puede entenderse, cumplirse, verificarse, discutirse, corregirse — y dejar una huella que otra persona pueda seguir. La vara existe para eso: para que ninguna regla vuelva a ser decoración.

> La Bandita informa a partir de fuentes fechadas. Las estrellas adornan; las fechas mandan.

---

## §8 — Orden de cierre indicado por el dueño

El dueño ordenó **terminar primero las tareas pendientes y revisar GitHub al final**. Este orden prevalece; la inspección de perfil, repositorios e interacciones externas no empieza mientras siga abierto cualquiera de los hitos anteriores.

**Regla de persistencia:** todo avance comprobado se publica en GitHub sin esperar una autorización adicional. La instrucción posterior registrada en `docs/CHECKPOINT-ACTUAL.md` exige una rama revisable y no empujar directamente a `main`; esa instrucción sustituye aquí el destino histórico `origin/main`. Publicar progreso no significa desplegar en redes ni aprobar contenido. El respaldo comprimido y toda la documentación se suben igual. Lo único que jamás se sube son las credenciales: tokens y llaves permanecen solo en local y están bloqueados por `.gitignore`. Perder trabajo por no espejarlo es una falla grave; clonar para "recuperar" no sirve porque queda desactualizado.

1. **Aceptar el manual v0.0.1:** cotejar las 70 filas de §9.9 con las reglas reales, ejecutar las pruebas estructurales y revisar coherencia; resolver la discrepancia 15/18 lecciones. El dueño aclaró que 2026-11-19 era una fecha prevista, no histórica ni de corte; conservar esa etiqueta y usar la fecha de plataforma para el trabajo actual. Después correr la vara sobre ambos archivos íntegros y actualizar este manifiesto. «Redactado» no se renombra como «completo» antes de cerrar la revisión y el cotejo.
2. **Rehacer el lote 01–70 por idioma:** usar las 70 fusiones antiguas como referencia e inventario, no como texto final; investigar de nuevo lo mutable; producir una pieza ES y una EN por número; superar 45.000 caracteres de sustancia en cada idioma; cumplir créditos, fuentes, diversidad real y compuertas. Avanzar por checkpoints pequeños, sin derivadores genéricos ni reescritura automática por aprobación.
3. **Comprobar almacenamiento:** se sustituyó el árbol sin comprimir `respaldo-2026-11-17/` por `respaldo-2026-11-17.tar.xz`, con sidecar SHA-256 e instrucciones de restauración; se cotejaron 525 SHA-256 y los modos de todos los elementos. Última medición: 46.607.046 bytes (tras añadir la guarda y sus pruebas) de un máximo de 50.000.000; la verificación posterior al commit vuelve a medir. El lote exige 140 maestros (70 ES + 70 EN) y, al piso de 45.001 caracteres cada uno, suma al menos 6.300.140 caracteres; el texto UTF-8 real puede ocupar más bytes que caracteres y excedería el espacio libre si se guarda todo sin comprimir. Por eso: auditar por pares en espacio temporal, guardar hash y recuento de cada maestro, comprimir el par final y probar la extracción/comparación de hashes antes de retirar copias de trabajo. Mantener los textos fusionados de referencia y el respaldo candidato; no borrarlos. `guarda_lote.py` mide el espacio en cada `verificar` y `estado`; detener la escritura antes de superar 50.000.000 bytes.
4. **Como última tarea, revisar GitHub:** perfil público de `Alex17273747576777` y los ocho repositorios que el dueño enlazó: `anime-extensoes`, `AniZen`, `cero-X-app`, `normas-de-diseno`, `gltools-reborn`, `entorno-de-herramientas-de-trabajo`, `la-bandita-archivo` y `ShinKu`. Revisar el estado visible y reciente de cada repositorio y, además, respuestas/comentarios de issues y pull requests, revisiones, releases, workflows/CI y notificaciones relacionadas; separar lo que un comentario dice de lo que un merge, cierre, release o ejecución realmente confirma. Reportar fuentes y horas comprobadas; no inventar recepción ni estado. La auditoría pendiente de `ShinKu` PR #37 va dentro de esta última etapa.

Hasta acabar los pasos 1–3, no se consulta el perfil ni se llama a APIs de GitHub para esa revisión final.

---

*Documento de evolución v0.0.1 · estado y orden de trabajo revisados; la aceptación final del manual sigue pendiente.*

## Actualización operativa de reglas y formato

Fecha de referencia: 2026-11-10, America/Santo_Domingo; sin convertir nombres de carpetas o marcas del host en fechas de verificación. Guía de aplicación en `FORMATO-Y-CONTROL-DE-PUBLICACIONES.md`. La aprobación del usuario de trabajar con lo conservado permite continuar esta revisión, no declarar recuperado todo el chat ni ratificadas las tres lecciones ausentes.

Se corrigen: polaridad de aceptación (§3.6), ficha documental, cierre ejecutable y separación entre seguimiento local y respaldo remoto. Las pruebas de guarda miden fixtures temporales y prueban además el rechazo de sobrepresupuesto; no certifican el almacenamiento de producción. El límite editorial de 50.000.000 bytes permanece; la cuota de plataforma de 128 MB es distinta.
