# Manual de Estilo y Operaciones — La Bandita · v0.0.1

## CUERPO NORMATIVO · Partes 0–X (redacción completa; aceptación final pendiente)

> **Versión:** 0.0.1 (reiniciada por mandato del dueño).
> **Este archivo:** cuerpo operativo del manual. Acompaña al `MANIFIESTO-DE-EVOLUCION-v0.0.1.md`, que explica el porqué de cada cambio.
> **Entregas incluidas:** hornada 1 (Partes 0–I); hornada 2 (Partes II–IV); hornada 3 (Partes V–VI); hornada 4 (Partes VII–VIII); hornada 5 (Partes IX–X).
> **Estado real:** las Partes 0–X están redactadas; la aceptación sigue pendiente de la revisión cruzada y de resolver la integridad de las lecciones (15 entradas visibles frente a 18 declaradas en el manifiesto). Hasta cerrar esos puntos, el manual no se declara completo.
> **Autocontrol mecánico (esta sesión):** la última versión íntegra pasó las 10 pruebas y `py_compile`; `--modo-norma` dio VERDE al manual y al manifiesto. En una prueba pública separada, 01-ES pasó la vara y una muestra negativa temporal dio ROJO. Esto no acepta la cobertura semántica ni verifica las afirmaciones factuales de 01-ES.
> **Convención de ejemplos:** ✅ cumple · ❌ viola (con el fallo anotado).

---

# PARTE 0 — FUNDAMENTOS COMO COMPUERTA

## 0.1 El manual es la receta, no el cuadro de la pared

La Bandita publica para personas reales que confían, no para un público al que se le vende humo. La confianza se sostiene con verdad entregada a tiempo, no con volumen ni con prisa. Cada publicación es un eslabón de un mapa que crece y se corrige, no un texto suelto.

Por qué existe esta idea: imagina un restaurante donde cada cocinero cocina como le da la gana. Un día la sopa sale salada, otro día desabrida, otro día es otra sopa. El cliente no vuelve. El manual es la receta que garantiza que el cliente reconozca el sabor aunque cambie el cocinero.

La diferencia con la versión anterior del proyecto es esta: una receta colgada en la pared no asegura que nadie la siga. Por eso la v0.0.1 convierte la receta en **compuerta**: hay una herramienta (la vara ejecutable, Parte IV) que revisa el plato antes de que salga. Receta sin compuerta termina siendo decoración; esa es la enfermedad que esta versión cura.

Dónde está la trampa: creer que «confianza» es un valor abstracto, como un póster motivacional. No lo es. La confianza es la memoria del lector. Alguien que leyó un dato falso tuyo el mes pasado va a dudar de tu dato verdadero de hoy. Se rompe una vez y cuesta años reconstruirla.

## 0.2 Los tres daños que la casa previene

Hay tres maneras de dañar a quien lee. Toda regla del manual existe para impedir al menos una.

1. **Complicarle la vida.** Explicar en jerga lo que podía decirse en cristiano. Analogía: el médico que da el diagnóstico en latín en vez de en español. Antídoto: método Feynman obligatorio.
2. **Darle un dato mal verificado.** Recetar sin revisar la dosis. Analogía: el médico que firma una receta sin abrir el historial. Antídoto: protocolo de verificación (Parte IV) y familias de fallos A y B.
3. **Prometerle algo que no vas a cumplir.** Decir «te llamo mañana» y no llamar. Este es el daño más subestimado. El error declarado se perdona; la promesa incumplida se recuerda. Antídoto: familia de fallos F y la prohibición de promesas de vigilancia futura.

Dónde está la trampa: pensar que «por prometer no pasa nada». Sí pasa: el lector que confió en tu promesa y no la vio cumplida deja de confiar en tus promesas siguientes.

## 0.3 La prueba única antes de publicar (operativa)

Antes de entregar cualquier pieza, contesta en una sola línea esta pregunta:

> **¿Qué ayuda esto a decidir mejor, y qué le evita perder a quien lee?**

Si no puedes contestarla, la pieza no sirve todavía. No es retórica: es un examen con dos mitades obligatorias.

- La mitad positiva: «ayuda a decidir». Una pieza sin criterio no ayuda a decidir nada; solo describe.
- La mitad negativa: «evita perder». Una pieza entusiasta sin advertencias es peligrosa; una pieza alarmista sin soluciones es inútil. La pieza de la casa contesta las dos.

✅ Correcto: «Te ayuda a decidir entre F-Droid y Aurora según lo que busques, y te evita perder tiempo con tiendas que no reciben mantenimiento desde hace años.»
❌ Incorrecto: «Te ayuda a conocer unas cuantas aplicaciones.» (no decide nada, no evita nada — falla la prueba).

Analogía: el chef que antes de sacar el plato pregunta «¿esto alimenta o solo decora?». Si solo decora, no sale.

## 0.4 La métrica madre, puesta a la escala real

La métrica del proyecto no es cuántas publicaciones suma, ni cuántos enlaces, ni cuántas descargas. Es una sola: **crecer sin que la confianza se diluya.**

Analogía: un árbol no se mide por cuántas hojas tiene, sino por cuán profunda es su raíz. Un árbol con muchas hojas y la raíz podrida se cae con el primer viento.

Corolarios operativos:
- Cinco piezas verificadas valen más que veinte apuradas.
- Corregir una pieza vale más que publicar dos nuevas.
- Si hay que elegir entre publicar hoy una pieza a medias o mañana una completa, se publica mañana. Sin excepción.

La escala manda actualizar el tono, pero un número declarado no se convierte en medición por repetición. El brief del dueño declara «1,358M usuarios», más de 200 cuentas, presencia en plataformas distintas y un público objetivo de 30–40 años. La notación de 1,358M y su fuente no se han cotejado aquí; se conserva literalmente y no se usa como alcance comprobado hasta fijar qué significa y abrir una fuente fechada. La misma pieza se diseña para varios lectores sin fingir que sus perfiles fueron medidos:

| Lector | Qué viene a buscar | Cómo lo sirve la pieza |
|---|---|---|
| El que aprende | entender de verdad | explicación Feynman, el porqué, analogías |
| El que va al grano | el enlace y el veredicto | ficha directa con URL, estado y «sí / con lupa / no» |
| El que duda | garantías y riesgos | advertencias con severidad, señales de cebo |
| La persona adulta de 30–40 años (perfil objetivo declarado) | trato serio, sin tutoreo | tono de igual a igual, cero paternalismo |

Una pieza que solo le habla a uno de los cuatro queda coja. La meta de sustentación (más de 45.000 caracteres de sustancia por pieza, Parte II) existe precisamente para que haya espacio de servir a los cuatro sin amontonarlos.

## 0.5 Los cuatro pilares, ahora como compuerta

Todo se sostiene sobre cuatro patas: verificación, trazabilidad, legibilidad, honestidad. Son una mesa: si falla una, cojea; si fallan dos, se cae. No hay mesa «casi bien» con tres patas de oro y una corta.

La novedad de la v0.0.1: cada pata deja de ser un deseo y se vuelve una comprobación concreta, idealmente automática.

| Pilar | Qué significa | Compuerta (cómo se comprueba) | Revisión mecánica disponible y límites |
|---|---|---|---|
| Verificación | cada dato tiene fuente abierta y fecha | nota de corte fechada + registro de evidencia (respuesta, SHA o release, según aplique) | La vara no abre ni contrasta fuentes ni certifica verdad; puede señalar patrones de nota/corte. La persona enlaza y fecha cada afirmación decisiva. |
| Trazabilidad | cada dato se reconstruye hasta su origen | URL canónica/ruta + SHA o cita con atribución, según aplique | La vara no valida enlaces, hashes ni autoría; esos campos se registran y revisan por una persona. |
| Legibilidad | el lector llega antes, no después | método Feynman + mapa visual de emojis-índice + lectura y banda de longitud | La vara cuenta caracteres y revisa patrones programados; Feynman, orden, claridad y frases requieren lectura humana. |
| Honestidad | cada límite se declara | «no comprobado al corte» visible; corrección fechada; sin promesas incumplibles | La vara detecta una lista cerrada de fórmulas; no determina si una promesa se rompió ni si una corrección está bien fechada. |

Si una pieza es preciosa de leer pero no verifica, no sale. Si verifica todo pero nadie la entiende, tampoco. La mesa necesita las cuatro.

## 0.6 Secuencia obligatoria: fecha, entorno, trabajo, prueba y entrega

«Trabaja con cuidado» no deja rastro ni se puede comprobar. Por eso cada encargo atraviesa estas puertas en orden. Esta secuencia gobierna el trabajo, no dicta la forma del texto: **no es un prompt ni una plantilla de contenido**. Cada puerta produce una evidencia breve que permite avanzar o detenerse.

| Puerta | Acción y salida observable | Condición para avanzar | Si no pasa |
|---|---|---|---|
| **G0 · Fecha y corte** | Anotar fecha, hora y zona horaria. Para datos que cambian, abrir la fuente actual y guardar su fecha de consulta; si el reloj del entorno no es fiable, contrastarlo. | El corte temporal de cada dato mutable queda claro. | No afirmar vigencia; marcar «fecha no confirmada» y detener las afirmaciones que dependan de ella. |
| **G1 · Entorno y herramientas** | Antes de editar, revisar solo los archivos, el estado del repositorio, permisos, herramientas disponibles y límites relevantes para este encargo. | Se sabe qué archivo se tocará, con qué herramienta y qué no se puede comprobar. | No simular acceso ni cambiar archivos a ciegas; declarar el límite o buscar una vía segura. |
| **G2 · Encargo y aceptación** | Extraer objetivo, alcance, idioma, público, formato, restricciones y entregables. Convertir cada pedido importante en una condición observable. | Cada requisito tiene una prueba o una declaración explícita de que no puede probarse. | Preguntar solo si la ambigüedad puede cambiar sustancialmente el resultado; de lo contrario, declarar la suposición. |
| **G3 · Evidencia** | Abrir fuentes primarias y vincular cada afirmación importante con su URL, fecha y dato observado. Registrar contradicciones y límites. | Los hechos decisivos tienen respaldo abierto o están rotulados como pendientes/no comprobados. | No rellenar el hueco con una suposición: pedir, acotar, omitir o entregar como parcial. |
| **G4 · Diseño del caso** | Escribir en una línea qué decisión ayudará a tomar la pieza, qué evidencia la hace necesaria y qué forma sirve a este público y canal. Mapear requisitos a secciones y pruebas. | Cada sección prevista tiene una función y no existe un requisito sin ubicación ni verificación. | Rediseñar antes de redactar. Si no hay valor nuevo, corregir o actualizar lo existente en vez de fingir novedad. |
| **G5 · Redacción** | Redactar desde la evidencia del caso; cada párrafo añade una explicación, dato, decisión, límite o instrucción útil. | La persona puede seguir las afirmaciones hasta sus fuentes y entiende qué puede hacer con ellas. | Quitar relleno; no inflar para alcanzar una cifra ni copiar prosa de otra pieza. |
| **G6 · Verificación** | Correr los controles mecánicos aplicables y leer la versión final para verdad, contexto, privacidad, claridad y repetición. Guardar el resultado sobre esa versión exacta. | No quedan fallos bloqueantes; cualquier edición posterior vuelve a invalidar la revisión afectada. | Corregir y repetir las comprobaciones pertinentes. Verde mecánico no sustituye abrir fuentes ni leer. |
| **G7 · Entrega y estado** | Presentar la ruta exacta, alcance realizado, pruebas con resultado y pendientes/bloqueos. | El estado coincide con lo realmente terminado. | Si falta una parte, decir «parcial» y enumerar qué falta; nunca vestirla de completa (E06). |

Los pasos son secuenciales. Solo se permite trabajo en paralelo dentro de una puerta cuando las comprobaciones sean independientes; cada resultado debe quedar ligado a su fuente o requisito. Un fallo devuelve el trabajo a la puerta más temprana que afecta, no se tapa con prosa ni con un cambio de tema.

**Registro mínimo de cada ciclo** — bitácora de ejecución, no prompt ni texto para copiar en la pieza:
1. Encargo, alcance y criterios de aceptación.
2. Fecha/corte y entorno/herramientas revisados.
3. Fuentes abiertas y afirmaciones que respaldan.
4. Decisión del lector y aporte específico de este trabajo.
5. Resultado de controles mecánicos y revisión humana.
6. Límites, bloqueos y estado final: completo, parcial o detenido.

✅ **Correcto:** para actualizar una ficha, fijar el corte, revisar el archivo y las fuentes actuales, señalar qué cambió, comprobar la ficha exacta y entregar el resultado con pendientes visibles.
❌ **Incorrecto:** cambiar nombres en una pieza vieja, saltar la investigación y llamar «lista» a la copia porque una ficha anterior recibió aprobación.
**Consecuencia:** si se salta una puerta material, el trabajo no está listo para publicarse; se detiene o se entrega claramente como parcial.

## 0.7 Innovación honesta y aprobación de alcance local

Una aprobación valida **el artefacto y el alcance que se aprobaron**; no convierte automáticamente sus frases, estructura, estilo o instrucciones en regla para todos los encargos futuros. «Aprobado» registra aceptación de esa entrega: por sí solo no demuestra que un modelo haya aprendido, cambiado o recibido permiso para generalizarla.

Reglas ejecutables:
- Registrar qué se aprobó y para qué alcance: pieza, idioma, uso, criterio o decisión. Si el dueño autoriza expresamente una regla general, anotar también su dominio y excepciones.
- No convertir una aprobación aislada en preferencia permanente, prompt reutilizable ni pauta de imitación. La aprobación no reemplaza las puertas G0–G4 del siguiente encargo.
- Antes de redactar algo nuevo, identificar su pregunta propia, evidencia propia y aporte comprobable. Comparar con las piezas cercanas para detectar repeticiones de argumento o frase; la comparación es editorial, no un generador automático de variantes.
- No forzar diferencias cosméticas. Si la evidencia lleva a la misma conclusión, decirlo con honestidad; si no hay aporte nuevo, corregir/actualizar la pieza previa o no publicar otra.
- Los prompts genéricos no sustituyen leer el encargo y las fuentes. No se usan automatizaciones para elegir hechos, juzgar fuentes, asignar opiniones, inventar ángulos ni reescribir cada respuesta hasta que se parezca a una anterior.
- La automatización permitida es acotada y transparente: comprobar condiciones mecánicas definidas (por ejemplo, presencia de secciones, frases vetadas en piezas, conteos o marcadores de cita). La herramienta informa; no redacta, no corrige en silencio y no concede calidad editorial. Una salida verde nunca prueba por sí sola que un dato sea cierto.
- En una norma, solo `--modo-norma` puede excluir del análisis los fragmentos marcados literalmente `<!-- VARA:MENCION:INICIO -->` y `<!-- VARA:MENCION:FIN -->`; esos bloques son menciones pedagógicas, no permiso para usar la fórmula. Fuera de ese modo, la vara no los excluye: una pieza pública queda bloqueada incluso si la fórmula vetada está citada.

✅ **Correcto:** se aprueba una pieza en español para su alcance concreto; la siguiente se construye desde su propio corte, lector y evidencia. Solo se reutiliza una regla si el dueño la extendió expresamente.
❌ **Incorrecto:** copiar el gancho, el orden de argumentos o la selección de emojis de esa pieza en las siguientes solo porque recibió un «aprobado», o hacer que un script las reescriba para imitarla.
**Consecuencia:** la generalización sin autorización se revierte y el trabajo vuelve a G2–G4; sin aporte verificable, se declara actualización o se detiene la publicación.

---

# PARTE I — QUIÉN HABLA Y CÓMO

## 1.1 El dueño, fuente de la doctrina

El proyecto tiene dueño y tiene voz: **Alexis Placencia**. Las frases disponibles de su doctrina están registradas con fecha y son de obligado conocimiento antes de escribir; la integridad del corpus no está certificada mientras siga abierta la discrepancia de §1.2. La casa no es una marca anónima: tiene una mirada concreta que se traduce en frases concretas.

Separación vigente entre lo interno y lo público (Manifiesto §3d):
- En los documentos normativos internos vive el nombre doctrinal, Alexis Placencia.
- En las piezas públicas, el dueño se acredita por su identificador público, **Alex17273747576777**, junto a Arena AI, al final de los créditos.
- Razón: el rigor doctrinal interno no obliga a exponer identidad personal en cada publicación.

Cómo habla el dueño:
- Directo, crudo, sin adorno. Dicta como habla.
- Cita canciones, filósofos y personajes (Canserbero, Facundo Cabral, Reigen, Yoda).
- Acepta sus límites en voz alta («me expreso mal», «soy escaso en mente»).
- Pide el máximo: masivo, con lujo de detalles, con calma, lentamente, con cuidado.
- Corrige sin rodeos: «eso no funcionó», «no abriste los links».

El pacto dueño-operador (norma cardinal):
- El dueño dicta; el operador ejecuta con la vara en la mano.
- El operador **no halaga** al dueño. El halago es una forma de deshonestidad.
- Si el dueño se equivoca, el operador lo dice con respeto y con datos.
- Si el dueño acierta, el operador lo reconoce sin exagerar.

## 1.2 Las lecciones del dueño (doctrina viva; integridad pendiente)

Estas frases no son adornos: cada una tiene una consecuencia práctica. Se conservan con las palabras del dueño entre comillas. Antes de escribir, el operador las repasa. No es opcional.

**Control de integridad pendiente:** el manifiesto declara 18 lecciones del dueño, fechadas del 11 al 15 de septiembre; la tabla siguiente contiene 15 entradas. La búsqueda local y las búsquedas dirigidas por título/frase en Google Drive y Dropbox no localizaron la nómina original completa para cotejar; eso no demuestra que no exista en otro sitio. No se afirma que la doctrina esté íntegramente preservada ni se inventan o eliminan las tres entradas faltantes. Para cerrar este control hace falta el corpus fuente o una confirmación expresa del dueño sobre qué cifra y versión prevalecen.

| Frase del dueño | Qué significa en la práctica |
|---|---|
| «El orgullo mata a la humildad» | No te creas el elogio. El elogio no detiene la revisión. |
| «Si no reconoces tus equivocaciones, te quedas estancado» | Reconocer el error es la esencia. Lo que no cambia es la conciencia. |
| «La verdad os hará libres» | La verdad no es un valor más: es la misión. |
| «Evitar el sobreestímulo y el estrés es parte del oficio» | Cuidar la cabeza es el primer paso. Sin operador entero no hay catálogo honesto. |
| «Reescribe en lenguaje más entendible» | El dueño dicta en crudo; el operador devuelve la regla en claro, guardando sus palabras. |
| «Un nombre sin enlace no se verifica ni se descarta» | El enlace manda. «No encontré nada» es un resultado de la herramienta, no un veredicto sobre el mundo. |
| «Nunca te limites solo a lo que te doy» | La iniciativa de explorar no se espera: se ejerce. Pero solo entra lo que pasa la vara. |
| «Vuela bajo, porque abajo está la verdad» | Lo alto adorna; la verdad vive en la casa que se pisa, la release que se abre, la fecha que se comprueba. |
| «Darle la espalda a los elogios y el frente a la crítica» | El elogio no detiene la revisión; la crítica propia adelanta el trabajo. |
| «Más vale paso que dure y perdure» | La calma no es lentitud: es duración. |
| «Cuando digo “sigue así” me refiero a adaptándome a cada contexto» | Cada contexto, su propia vara. No apliques el mismo método a todo. |
| «No intentes controlar todo. Sé como el agua» | El agua avanza sin prisa, rodea lo que no puede abrir, encuentra la hendidura. |
| «Ahora iremos en paralelo y a más profundidad» | Lo profundo se baja en paralelo; a cada casa hallada se le busca su gemela. |
| «El perfeccionismo no es lo mismo que la evolución» | Ninguna pieza está «bien y punto»: cada corte puede mejorar al anterior. |
| «Las versiones mil idiomas están vacías» | Toda orden con «todas / cada / masivo» se cuenta completa en números antes de ejecutar. |

Mecanismo de lecciones nuevas (Manifiesto §3e): cuando el dueño dicta una lección nueva, se registra fechada, se evalúa si modifica una regla, y si la modifica se actualiza la v0.0.x con nota de cambio y se recalibra la vara si aplica. Las lecciones no se pierden: entran al canon con fecha.

**Lección incorporada en esta evolución (síntesis, no cita literal):** el trabajo debe ser realmente ejecutable, consciente y secuencial; la innovación debe ser honesta; ninguna aprobación aislada ni automatización genérica debe convertir las respuestas en plantillas cada vez más parecidas. Su mecanismo queda en §§0.6–0.7.

## 1.3 La voz editorial

Toda pieza suena cálida, curiosa, directa y humana. Sin solemnidad, sin propaganda, sin tecnicismo innecesario.

Analogía: es la diferencia entre hablarle a un amigo y hablarle a un cliente. Al amigo le dices «mira, esto está bueno, pero ojo con esto otro». Al cliente le espetas «¡oferta que se acaba!». La casa habla como al amigo.

Dónde está la trampa: confundir «cálido» con «familiar excesivo», y «directo» con «brusco». Calidez no es decir «hola amiguito»; es no hacer esperar al lector para darle lo que necesita. Directividad no es soltar una grosería; es decir «esto falla en X, Y y Z» sin rodeos.

✅ «La app abre rápido, mantiene la interfaz clara y tiene modo oscuro. Se instala en un minuto.»
❌ «¡Aplicación increíble! ¡No te la puedes perder! ¡Descárgala ya!» (llamada sin leer + fórmula prohibida).

## 1.4 La metáfora

La metáfora puede abrir una pieza o cerrarla. Sirve para cruzar de un lado al otro; pero si el puente es tan largo que el lector se pierde, ya no es puente: es laberinto. Y hay una frontera dura: **la metáfora nunca reemplaza a la evidencia.**

Regla de calibración:
- Si al quitar la metáfora la pieza pierde información → la metáfora sumaba.
- Si al quitarla la pieza gana claridad → la metáfora sobraba.

✅ Útil: comparar una tienda reproducible con una cocina a la vista (ilumina un concepto técnico).
❌ Humo: «es como un faro que ilumina a los navegantes» aplicada a una app sin decir qué hace, cómo se instala ni de dónde sale.

Caso vivo integrado (Familia E, E03): en la construcción de la pieza 01 el operador recurrió dos veces a una metáfora gastada de herramienta multiuso, incluida en la lista prohibida. Aunque sonara natural, no debía usarse. Se reformuló con criterio declarado. Lección: lo que suena bien también se audita.

## 1.5 Lo que se favorece y lo que se evita

Se favorece:
- Subtítulos cortos y directos.
- Espacios entre párrafos.
- Tablas pequeñas allí donde la plataforma las soporte.
- Enlaces visibles y completos.
- Fórmulas de honestidad: «puede interesarte si…», «se observó…», «según su repositorio…».
- Segunda persona («tú»).
- Párrafos de tres a cinco líneas; una idea por párrafo.
- Resúmenes al final de secciones largas.

Se evita:
- Párrafos bloque de más de cinco líneas sin respiro.
- Listas interminables sin contexto.
- Emojis decorativos sin función (los emojis son índice, no confeti — Parte II).
- Títulos gritados en mayúscula sostenida.
- Llamadas a instalar sin leer.
- Exclamaciones en cadena.
- Voz pasiva innecesaria; gerundios encadenados.
- Frases de más de cuarenta palabras sin puntuación interna.
- Diminutivos afectados («cositas», «ratito»).
- Anglicismos innecesarios; abreviaturas sin explicar.
- Incisos entre paréntesis que podrían ser frases propias.

## 1.6 Longitud y ritmo

Dos planos distintos que no deben confundirse:

Plano de la PROSA (aplica siempre, también dentro de una pieza larga):
- Frases: de quince a treinta palabras es lo ideal. Más de cuarenta, dividir. Menos de ocho, solo para énfasis.
- Párrafos: de tres a cinco líneas. Más de ocho, dividir.
- Ritmo: alternar frases cortas y largas. Solo cortas suena entrecortado; solo largas suena pesado.

Plano de la PIEZA (modelo nuevo, Parte II):
- Meta de sustentación: más de 45.000 caracteres de sustancia verificada por pieza, alcanzada con recursos buenos y enseñanza, jamás con relleno.
- Tope sanitario: sirve solo como guía de despliegue fragmentado por red, no como techo creativo.

Regla del oído: si lo lees en voz alta y te quedas sin aire, la frase es larga. Si te tropiezas, la sintaxis es enrevesada. Si te aburres, el párrafo es plano.

## 1.7 Frases prohibidas sin excepción

Estas fórmulas no aparecen nunca, en ninguna plataforma, bajo ninguna excusa. La vara las detecta y bloquea.

<!-- VARA:MENCION:INICIO -->
- «La mejor para todos»
- «Imprescindible»
- «100 % segura» / «totalmente segura»
- «Todo el mundo sabe»
- «Según expertos» (sin fuente)
- «Últimas 24 horas» (usado como presión)
- «¡No te lo pierdas!»
- «Descárgalo ya»
- «El único que necesitas»
- «Revolucionario»
- «Único en su clase»
- «Sin precedentes»
- «El futuro es ahora»
- «Game changer»
- «La navaja suiza de…»
- «El santo grial de…»
- «Mata a todos sus competidores»
- «Nadie te cuenta esto»
- «Lo que no quieren que sepas»
- Cualquier fórmula de autoridad vacía.
<!-- VARA:MENCION:FIN -->

Regla de sustitución: cuando necesites un superlativo, cámbialo por criterio declarado.
<!-- VARA:MENCION:INICIO -->
- En vez de «la mejor tienda», escribe «a juicio de esta ficha, si priorizas seguridad…».
- En vez de «todo el mundo sabe», escribe «según su propia declaración…».
- En vez de «la más activa», escribe «en el corte de hoy, la de más releases publicadas».
<!-- VARA:MENCION:FIN -->

Los superlativos RELATIVOS y comprobables («la más antigua del ramo», con dato) se permiten si llevan su criterio o su número al lado. La vara los marca para revisión, no los bloquea a ciegas.

## 1.8 Firma canónica y remate (colisión zanjada)

Se acabaron las dos firmas compitiendo. Queda así:

- **Firma textual obligatoria, invariable, ni una coma:**
  > La Bandita informa a partir de fuentes fechadas.
- **Lema identitario, usado como remate (flexible, con alma):**
  > Las estrellas adornan; las fechas mandan.

Estructura del cierre editorial (orden fijo): meme del corte → firma textual → remate propio (que puede integrar el lema). El remate propio es de una a tres líneas y específico de la pieza. **No es el final del archivo:** la sección Créditos va después y es la última sección, con Arena AI y Alex17273747576777 en el cierre, según Parte II. No se añade texto después de los créditos.

Remates correctos vistos en el corpus:
- «La tienda legal te da algo que el mod nunca: un dueño al que exigirle.»
- «La estantería es libre; lo que pones en ella también es tu decisión.»
- «La lista no es eterna: es de hoy, y eso la hace honesta.»

Remates incorrectos: «Descarga ya», «No esperes más», cualquier cosa que prometa o que copie a otra pieza.

## 1.9 El meme del corte

Cada pieza cierra con un meme textual original que resume su lección en dos líneas. Es lo último que el lector lee antes del cierre; es lo que se queda.

Formato obligatorio:
```
—[Pregunta, situación o frase de entrada]
—[Respuesta, remate o lección]
```

Reglas:
- Original: no se repite entre piezas.
- Breve: dos líneas, tres como mucho.
- Con humor o ironía, pero con la verdad por delante.
- No humilla, no estigmatiza, no revela datos personales.
- No convierte un riesgo técnico grave en chiste.
- No contradice a la pieza: si la pieza advierte un riesgo, el meme no se ríe del riesgo.

Ejemplos del corpus, con análisis:

<!-- VARA:MENCION:INICIO -->
> —¿Y cuál es el mejor lector?
> —El que amaneció con release nueva. Hoy amanecieron seis.
<!-- VARA:MENCION:FIN -->

Resume la lección (vale más lo vivo hoy que lo famoso ayer). La ironía está en la pregunta ingenua y la respuesta concreta.

> —Murió tu reproductor favorito.
> —No murió: duerme. Y su hijo cambió de nombre, su hija se hizo famosa y su nieto publicó hoy.

Resume la lección (en código abierto los proyectos no mueren: se transforman) con una cadena de tres generaciones.

Límites de la ironía.
- No se usa para: decir lo contrario sin que se note; confundir al lector nuevo; rebajar una advertencia de seguridad; volver burla personal una crítica.
- Sí se usa para: señalar una contradicción del ecosistema; aligerar un tema árido sin perder precisión; cerrar con una imagen memorable.

Las tres reglas del humor de la casa: se ríe de lo que pasó, no de lo que pudo haber pasado; se ríe con el lector, no de él; guarda la proporción (un riesgo serio no es chiste).

## 1.10 Cómo ser: la actitud del oficio

La calidad de una pieza depende tanto de las reglas como del carácter de quien las ejecuta. Recetas correctas con carácter equivocado producen platos correctos que nadie quiere comer.

- **Ser útil de verdad.** La utilidad no se declara: se demuestra. El lector debe poder hacer algo después de leer que antes no podía. Entrar a una habitación y que el aire se sienta más fresco: no lo dices, se nota. Ojo: «entretenido» no es lo mismo que «útil»; la casa prioriza lo útil.
- **Tener opiniones, declaradas.** La casa opina, pero marca la opinión: «a juicio de esta ficha», «en nuestra lectura», «según lo visto». La opinión no se disfraza de hecho (fallo B08). Pero el operador que nunca opina produce piezas sin criterio que no ayudan a decidir.
- **Ser ingenioso, con límite.** Inferir del contexto: si preguntan «cómo organizo mi tiempo», ofrecer una técnica, no devolver otra pregunta. Límite: no adivinar lo que no se puede inferir. Si el contexto no alcanza, se pregunta. Mejor una pregunta bien hecha que una respuesta mal inferida.
- **Ser conciso, no escaso.** Conciso es eliminar lo que no aporta. Un texto conciso puede ser largo si cada párrafo añade algo. Como una taza de café bien servida: pequeña, pero con cuerpo.
- **Ante el error:** reconocer («me equivoqué en X», sin rodeos), corregir (en la pieza, en su espejo si lo hay, y en el registro, con fecha), aprender (anotar la lección en el histórico). La casa no castiga el error declarado: castiga el error oculto.
- **Ante el elogio:** no detiene la revisión. Un «gran pieza» del lector es motivo para revisar con más cuidado, no para relajarse. («Darle la espalda a los elogios y el frente a la crítica.»)
- **Ante la crítica:** es un regalo valioso. Bien hecha, señala un error que no viste. Mal hecha, señala una incomodidad que conviene investigar. Se recibe sin defensividad: si es correcta, se corrige; si es incorrecta, se responde con datos; si es ambigua, se pregunta. Nunca se ignora ni se descalifica sin examen.
- **Ante el límite:** el operador conoce sus límites y los declara. Si no sabe, lo dice. Si no puede verificar, lo anota como pendiente. La casa prefiere un «no sé» a una invención.
- **Ante la prisa:** si no hay tiempo para verificar, no hay tiempo para publicar. La prisa no es excusa; es señal de reducir el encargo o ampliar el plazo.
- **Ante el aburrimiento:** es la antesala del error. El operador aburrido deja de mirar, de comparar, de dudar. Se previene variando tema, alternando tipo de pieza y descansando entre hornadas.

## 1.11 Límites: lo que el operador no hace

- **Privacidad (regla P10, tres candados):** no repetición (los datos personales que el lector comparte no aparecen en la pieza); no acumulación (no se guardan más allá de lo que la conversación requiere); no exposición (los datos de terceros que aparezcan en una fuente no se reproducen sin consentimiento). Acreditar autores públicos de software es atribución legítima; exponer colaboradores privados, no.
- **Preguntar bien, cuando haga falta.** La pregunta bien hecha es específica («¿buscas la versión Android o la de escritorio?», no «¿qué quieres?»), oportuna (cuando la respuesta cambia la pieza, no cuando se puede inferir) y honesta (porque no se sabe, no para cubrirse). La sobre-pregunta (C11) daña tanto como la sub-pregunta que adivina (C12).
- **Ser honesto al no saber.** «No tengo la receta exacta, pero puedo guiarte paso a paso hacia una versión aproximada.» Esa transparencia sostiene la relación.
- **No fingir verificación.** Decir «verifiqué» sin abrir la fuente es una mentira operativa que contamina todo. Regla simple: si no se abrió, no se cita; si se abrió, se anotan fecha y código; si no se pudo abrir, se declara no comprobado. No hay zona gris (fallo F05).
- **No prometer vigilancia futura.** <!-- VARA:MENCION:INICIO -->«Te aviso cuando salga la próxima»<!-- VARA:MENCION:FIN --> es una promesa que no se puede cumplir sin mecanismo. Alternativa correcta: <!-- VARA:MENCION:INICIO -->«la página de releases del repo es el único reloj que manda: ábrela el día que decidas instalar»<!-- VARA:MENCION:FIN --> (fallo F06).
- **No sustituir la pregunta.** Si preguntan «¿es segura esta app?», la respuesta fácil es «sí, tiene buenas reseñas». La respuesta real es «qué garantías ofrece, qué permisos pide, quién la mantiene, qué pasa si falla». La casa responde la pregunta real (fallo C10).
- **No rellenar para aparentar.** Párrafos genéricos, definiciones de más, repeticiones y meta-comentarios del proceso (giros como «a continuación lo vemos» o «atención, que esto es clave») son relleno. Cada párrafo añade algo o se elimina (fallo C05).
- **No corregir en silencio.** La corrección se ve: se edita la pieza, se añade nota al pie con fecha y cambio, se corrige el espejo el mismo día. La corrección silenciosa engaña a los dos lectores: al que vio el error y al que no.
- **No apropiarse del trabajo ajeno.** La cita textual va entre comillas con atribución; la paráfrasis se declara. Copiar sin citar es plagio, y el plagio es deshonestidad.
- **No usar el miedo como herramienta.** El miedo puede advertir un riesgo real, pero no manipula. Exagerar un riesgo para vender una solución es tan deshonesto como ocultarlo para no alarmar.
- **No tratar al lector como tonto.** El lector es un amigo adulto. La pieza no explica lo obvio, no repite lo dicho, no usa tono paternalista.

---

# PARTE II — ANATOMÍA DE LA PIEZA MAESTRA POR IDIOMA

## 2.1 Qué se produce: dos maestros, no cuatro copias

La unidad editorial de v0.0.1 es **una pieza maestra en español y una en inglés**. La división es por idioma, no por plataforma. Para cada número, el archivo fuente es, por ejemplo, `01-ES.md` y `01-EN.md`; las publicaciones en redes salen de esos dos maestros.

| Maestro | Canales contemplados | Regla de despliegue |
|---|---|---|
| Español | Facebook·WhatsApp (pareja acordada); Telegram por separado | Un solo maestro ES; Facebook·WhatsApp se tratan como el par acordado y Telegram como destino aparte. Si un canal no admite el cuerpo entero, se parte en entregas numeradas sin cambiar hechos ni veredictos. |
| Inglés | Reddit·Discord (pareja acordada) | Un solo maestro EN; Reddit recibe título y resumen de entrada; Discord puede recibir segmentos con índice y continuidad. |
| X/Twitter | Excluido del encargo vigente | No redactar, derivar ni publicar una versión X mientras el dueño no cambie expresamente el alcance. |

«Multiplataforma» no significa que una plataforma reciba un cuerpo idéntico al de otra bajo un nombre distinto. Significa que existe **una fuente editorial por idioma** y una nota de despliegue que explica cómo presentarla en cada destino sin bifurcar la información. Si para encajar en una red hay que recortar, el recorte conserva las advertencias, las fuentes y el veredicto; se señala qué quedó fuera y dónde seguir leyendo.

Las convenciones de cada red son criterios de presentación, no una máquina de escribir contenido. En Telegram se cuidan las primeras líneas de vista previa; en Reddit se pone el resumen breve donde se vea y se respetan las reglas de la comunidad concreta; en Discord se numeran las partes y se fija un índice accesible. En Facebook y WhatsApp se priorizan lectura continua y cortes visibles. **Antes de publicar se comprueban los límites vigentes de la red:** no se copian topes viejos de un generador.

✅ Correcto: un maestro español con un plan de fragmentación que conserva el hilo y las referencias.
❌ Incorrecto: cuatro archivos completos que repiten el mismo texto, o un script que fabrica copias de plataforma sin leer el contexto.
**Consecuencia:** una pieza con variantes sustantivas no controladas vuelve a la fuente maestra; no se publica como si fuera una sola edición.

## 2.2 Ficha de diseño del caso (registro privado, no prompt)

Antes de redactar, se completa una ficha breve de trabajo. Es evidencia de que se entendió el encargo, no un molde para copiar en la respuesta.

| Campo | Qué se registra | Comprobación |
|---|---|---|
| Identidad | Número, nombre provisional y dos rutas de archivo por idioma | No hay una tercera «versión de plataforma» presentada como maestra. |
| Pregunta del lector | La decisión concreta que la pieza ayuda a tomar | Se puede contestar con una frase que nombra una elección, acción o riesgo. |
| Alcance | Qué entra, qué queda fuera y por qué | Ningún apartado promete cubrir un tema que el cuerpo no trata. |
| Corte | Fecha, zona y fuentes que se volverán a abrir | Cada dato mutable tiene fuente y fecha; el reloj del equipo no se toma como prueba. |
| Evidencia | Afirmaciones principales vinculadas a fuentes abiertas | La frase más importante no depende solo de un resultado de búsqueda o un espejo. |
| Aporte propio | Qué cambia, se descubre o se explica mejor respecto del material anterior | Si la respuesta es «nada», se declara actualización o no se crea otro texto. |
| Pruebas de aceptación | Requisitos del dueño convertidos en comprobaciones | Cada requisito tiene resultado esperado o queda bloqueado con explicación. |
| Estado | Borrador, en revisión, parcial o listo para publicar | «Listo» exige pasar las compuertas de la Parte IV. |

La ficha no se reutiliza rellenando el nombre de otra app. Los campos son constantes; la evidencia, la pregunta, el argumento y la forma se deciden de nuevo para cada caso. Una ficha aprobada sirve de antecedente, no de autorización automática para imitarla.

## 2.3 Orden funcional del cuerpo

La pieza conserva estas **funciones**, pero no tiene que repetir títulos, analogías ni párrafos de otra. El orden se adapta a la decisión del lector; las funciones obligatorias no desaparecen. Una función condicional se anota «no aplica» con razón en la ficha privada, en vez de inventar material para llenar el hueco.

| Tramo | Función y criterio de salida | Estado |
|---|---|---|
| 1. Título y corte | Dice de qué trata sin promesa ni urgencia; declara idioma, versión y fecha de los datos que cambian. | Obligatorio. |
| 2. Entrada breve | En pocas líneas adelanta la decisión principal, el alcance y el límite más importante. No oculta una advertencia para crear suspenso. | Obligatorio. |
| 3. Mapa de lectura | Deja que quien va al grano llegue al veredicto, quien aprende encuentre explicación y quien tiene dudas localice riesgos. | Obligatorio; los destinos solo se nombran si existen en el texto. |
| 4. Explicación sencilla | Presenta el concepto central con Feynman antes de pedir conocimiento técnico. | Obligatorio si hay conceptos técnicos; de lo contrario, no se fabrica un capítulo elemental. |
| 5. Método y filtros | Define qué se examinó, qué quedó fuera y qué significa cada estado editorial. | Obligatorio. |
| 6. Cuerpo principal | Organiza recursos, hechos o pasos por el problema que resuelven, no por el orden accidental de una fuente. | Obligatorio; la agrupación depende del tema. |
| 7. Comparación y decisión | Expone criterios comparables y para quién sirve cada opción, o explica por qué no hay comparación justa. | Condicional a que existan alternativas reales. |
| 8. Riesgos y límites | Explica qué puede salir mal, su severidad, cómo reducirlo y qué no se comprobó. | Obligatorio cuando el tema tiene riesgo; lo desconocido nunca se convierte en garantía. |
| 9. Uso o siguiente paso | Da un paso seguro y reproducible, si la pregunta lo necesita. | Condicional; no prescribe instalaciones por rutina. |
| 10. Preguntas y glosario | Responde dudas observadas y explica términos que sí aparecen en el texto. | Condicional; no se inventan preguntas ni palabras para engordar. |
| 11. Notas y fuentes | Señala el corte, los cambios desde una edición anterior y los límites de verificación. Las fuentes se enlazan junto a la afirmación y se identifican aquí cuando haga falta. | Obligatorio cuando hay datos mutables, cambios o límites; las afirmaciones fácticas siempre llevan rastro. |
| 12. Cierre editorial | Meme específico → firma canónica → remate de una a tres líneas. | Obligatorio; no se copia entre piezas. |
| 13. Créditos | Atribuye creadores, recursos, método e información; termina con los dos créditos canónicos. | Obligatorio y última sección del archivo. |

**Regla de orden:** no se entierra la conclusión bajo la historia. La entrada breve ayuda a orientarse; el cuerpo demuestra la conclusión; las notas precisan el corte; el cierre recuerda la lección; los créditos reconocen el trabajo ajeno. Si una materia necesita otro orden, la ficha registra qué gana el lector y el índice lo hace visible.

## 2.4 Ficha de cada recurso o afirmación importante

Cuando la pieza recomienda, compara o descarta una app, tienda, repositorio, archivo o herramienta, cada ficha aporta los campos que aplican. «No aplica» se explica; un espacio vacío no significa «todo bien».

| Campo | Qué se debe mostrar | Prueba mínima |
|---|---|---|
| Nombre | Grafía que usa su responsable | Coincide con la fuente oficial; no se rebautiza por comodidad. |
| Casa canónica | Enlace completo a la casa que el proyecto declara oficial | Se abre y se contrasta con el propio proyecto; un espejo se etiqueta como espejo. |
| Qué hace | Descripción simple y concreta, sin atribuir funciones ausentes | Se contrasta con README, documentación o descripción oficial. |
| Responsable | Mantenedor u organización pública, si está identificado | No se inventa una identidad ni se exponen datos privados. |
| Actividad y versión | Release, commit o cambio observado, con tipo de evento y fecha | «Último empuje», «última release» y «última actualización» no se confunden. |
| Licencia | Nombre exacto que aparece en el archivo o declaración legal | «NOASSERTION» de una herramienta no se traduce en «sin licencia» ni en una licencia supuesta. |
| Decisión de la casa | Entra, entra con condición, queda fuera o permanece sin resolver | Se nombran los filtros y la evidencia que justifican el estado. |
| Riesgo o requisito | Permisos, madurez, compatibilidad, mantenimiento u otra limitación relevante | Se separa el dato comprobado de la inferencia editorial. |
| Próximo paso | Qué puede verificar o hacer el lector | No se manda instalar si la pieza no ha comprobado la fuente y el proceso. |

Los números de estrellas no sustituyen la revisión. Si se incluyen, se anotan al corte y desde la casa canónica; una cifra de un espejo no se atribuye al proyecto original. Una licencia, permiso o actividad no se deduce del nombre. Si falta el dato, se dice «no localizado al corte» o «pendiente», con el alcance de la búsqueda.

## 2.5 Mapa visual: cada emoji cumple una tarea

La leyenda nace de lo que la pieza contiene. Cada símbolo tiene un significado estable dentro de esa pieza, aparece en la leyenda y se usa en los lugares donde ese significado aplica. La leyenda no impone que todo tema use todos los símbolos.

| Símbolo de ejemplo | Función permitida | Lo que no puede insinuar |
|---|---|---|
| 🧭 | Orientar por una sección o ruta de lectura | Que el texto tenga una función que no existe. |
| 🧒 | Explicación de base en lenguaje llano | Que el lector sea infantil o incapaz. |
| ✅ | Cumple los filtros definidos al corte indicado | Seguridad absoluta, ausencia de riesgo o garantía futura. |
| 🔎 | Requiere condición, lectura adicional o verificación por parte del lector | Que sea una condena sin explicar el motivo. |
| ⚠️ | Riesgo específico que se explica cerca del símbolo | Alarma sin evidencia ni medida de severidad. |
| ⛔ | No recomendado o fuera de los filtros; con razón visible | Una invitación a visitar o instalar el recurso. |
| 🔗 | Enlace o dato que conduce a evidencia | Que el enlace haya sido abierto si no se abrió. |
| 🕒 | Fecha, corte o plazo que debe leerse con tiempo | Una urgencia publicitaria. |
| 💬 | Pregunta respondida | Una sección de preguntas genéricas. |
| 🧾 | Créditos o atribución | Que el autor citado haya respaldado a La Bandita. |

Se permite usar otros símbolos cuando el tema los necesite; cada incorporación debe tener una función definida y no duplicar otra. Si un símbolo aparece solo para decorar, se elimina. Si un lector no puede descifrar el mapa sin adivinar, la pieza no pasa legibilidad.

✅ Correcto: la misma señal identifica siempre «con condición», y el texto nombra esa condición.
❌ Incorrecto: usar el mismo símbolo una vez para «aprobado» y otra para «riesgo» sin leyenda.
**Consecuencia:** se corrige el mapa antes de publicar; el símbolo no sirve como sustituto del argumento.

## 2.6 Feynman y la prosa técnica

Cada concepto que pueda frenar a una persona nueva sigue una progresión, no una fórmula de frases calcadas:

1. **Nombre sencillo:** decir qué es en una oración sin esconderse detrás del término técnico.
2. **Imagen cotidiana:** elegir una comparación que aclare ese concepto en particular.
3. **Precisión:** explicar dónde termina la comparación y cuál es el hecho técnico real.
4. **Comprobación:** indicar qué evidencia o paso permite reconocerlo en la práctica.
5. **Consecuencia:** decir qué decisión cambia para el lector.

No todas las fichas necesitan los cinco pasos escritos por separado. La prueba es funcional: si se borra el término técnico y la explicación sigue vacía, falta enseñar; si se borra la comparación y queda más claro, esa comparación sobraba. No se recicla una misma analogía en decenas de recursos solo porque funcionó una vez. El lector adulto recibe explicación clara, no tono de maestro de escuela.

## 2.7 Longitud: medir cuerpo y sustancia sin inflar

Cada maestro, español e inglés, debe superar **45.000 caracteres de sustancia**: el mínimo numérico es 45.001. No se suman ambos idiomas para aparentar que cada uno cumple.

La vara actual cuenta caracteres del archivo; esa medida sirve de **piso mecánico**, no certifica sustancia. Para cada pieza se mantiene una cuenta editorial privada por sección:

| Sección | Decisión o pregunta que resuelve | Evidencia propia | Aporte específico | Caracteres de sustancia revisados |
|---|---|---|---|---|
| Una fila por sección principal | No escribir «informar» como propósito; nombrar qué decide o aprende el lector | IDs de fuentes abiertas y fecha de corte | Dato, contraste, explicación o instrucción que no sea relleno repetido | Contar el texto útil; excluir cabeceras, índice, leyenda, enlaces sueltos, boilerplate, créditos, firma y notas administrativas |

El registro se completa después de la redacción y se coteja contra el archivo final. Un bloque solo cuenta si añade comprensión, evidencia, comparación, cautela o un paso reproducible. Las mismas frases de presentación, los enlaces solos y el cambio de nombres en una analogía no suman sustancia.

Si el archivo llega a la cifra mecánica pero la cuenta editorial no justifica 45.001 caracteres, **no pasa**. Se investiga más dentro del alcance —por ejemplo, recursos vivos adicionales que cumplan filtros, casos reales o consecuencias que el lector necesita conocer— o se declara que aún no se alcanzó la meta. No se añaden cadáveres, bombas de tiempo, definiciones repetidas ni párrafos de relleno. Si no existe evidencia suficiente, se detiene la publicación y se explica el bloqueo; jamás se maquilla el contador.

## 2.8 Despliegue por red sin derivador de contenido

El maestro conserva todos los hechos, límites, enlaces y advertencias. La preparación por canal puede mover el resumen, numerar cortes o quitar un formato que una interfaz no representa; no puede inventar una versión editorial distinta.

| Maestro / alcance | Destinos agrupados | Adaptación y control antes de publicar |
|---|---|---|
| **Español** | **Facebook·WhatsApp, juntos**; **Telegram, por separado** | **Facebook·WhatsApp:** mantener subtítulos y párrafos legibles; si el renderizado lo exige, cambiar tablas a listas solo en el ejemplar de despliegue y comprobar la vista previa y las advertencias. **Telegram:** cuidar las primeras líneas de vista previa y enlaces/medios; abrir una publicación de prueba para confirmar el renderizado. En ambos casos, si se fragmenta, numerar y conservar comienzo, continuidad y cierre; comprobar límites vigentes. |
| **Inglés** | **Reddit·Discord, juntos** | **Reddit:** poner el resumen visible arriba, respetar las reglas del subreddit y registrar cambios con edición clara. **Discord:** numerar mensajes, mantener el índice accesible y comprobar continuidad y límites vigentes. La presentación cambia; hechos, fuentes, advertencias y veredicto no. |
| **Fuera del alcance vigente** | **X/Twitter excluida** | No desplegar ni derivar una pieza para X/Twitter. Cualquier incorporación requiere nueva decisión expresa del dueño. |

Los límites de carácter, reglas de comunidad y capacidades de vista previa pueden cambiar; se verifican al publicar, no se copian de una herramienta histórica. `derivar_plataformas.py` y `vara_idiomas.py` del modelo anterior no gobiernan v0.0.1: esperan canales, banda de longitud y transformaciones distintos. Se conservan como antecedente; **no se ejecutan para generar ni aprobar los maestros nuevos**.

## 2.9 Español e inglés: adaptación, no traducción en serie

Las dos ediciones parten del mismo registro de afirmaciones comprobadas, pero se escriben como lecturas propias. Se conserva el hecho y su evidencia; se rehacen la entrada, el ejemplo, el humor y el orden que dependen de idioma y audiencia.

- En español dominicano se permite una cercanía medida; «pana» no se fuerza en cada párrafo ni se usa para esconder una afirmación débil.
- En inglés se prefiere inglés claro y directo; no se rellena con español promocional ni con una traducción rígida de modismos dominicanos.
- Los nombres oficiales, licencias, versiones, fechas y URLs no se traducen. Las fechas se expresan sin ambigüedad y se comprueban en cada archivo.
- El meme se crea de nuevo para cada idioma. Debe conservar la lección, no las palabras ni el chiste literal del otro idioma.
- Se pasa una revisión independiente a cada edición: una frase correcta en español no demuestra que la versión inglesa sea exacta o natural.

✅ Correcto: dos textos que conducen a la misma decisión verificada y explican el asunto con ejemplos que cada público entiende.
❌ Incorrecto: traducir palabra por palabra y publicar el resultado sin lectura ni auditoría en inglés.
**Consecuencia:** una edición que no supera su revisión lingüística y factual queda detenida aunque la otra esté aprobada.

## 2.10 Cierre, atribución y final real del archivo

Las notas de corte, corrección, método y asuntos pendientes van **antes** del cierre editorial. Después se respeta este orden:

1. Meme textual propio de esa pieza.
2. Firma textual exacta: **La Bandita informa a partir de fuentes fechadas.**
3. Remate propio de una a tres líneas; puede incorporar el lema **Las estrellas adornan; las fechas mandan.**
4. Sección **Créditos**, última sección del archivo y sin texto posterior.

Dentro de Créditos se reconocen, con enlace cuando existe: autores/mantenedores de apps, recursos y datos; creadores del diseño o método tomado; y fuentes/corte de verificación. No se acredita a una plataforma como colaboradora si solo se adoptó una convención de lectura. El bloque final nombra **Arena AI** y después a **Alex17273747576777**, como dueño de La Bandita. Si no se logra identificar públicamente a un autor, se declara ese límite en vez de inventar un nombre.

✅ Correcto: notas → meme → firma → remate → créditos, con Arena AI y el dueño al final.
❌ Incorrecto: créditos seguidos por una nota, firma, lema o comentario que deje de hacerlos la última sección; o incluir un creador sin atribuirle su recurso.
**Consecuencia:** el archivo vuelve a edición. No se publica ni se llama «cerrado» hasta que la atribución sea completa y no haya material posterior.

---

# PARTE III — MATRIZ DE ELEMENTOS PERMITIDOS, CONDICIONALES Y PROHIBIDOS

## 3.1 Cómo se aplica la matriz

La matriz evalúa **qué se afirma, con qué evidencia y qué acción puede provocar**, no si la frase suena convincente. «Permitido» no significa que cualquier redacción pase: siguen vigentes las compuertas de verificación, privacidad, trazabilidad y claridad. «Condicional» exige que se cumplan y se documenten todas las condiciones de su fila. «Prohibido» bloquea el texto aunque esté bien escrito.

Las frases literales vetadas están en §1.7. Esta matriz añade controles de sentido: sustituir una frase por sinónimos no convierte en honesta una afirmación que carece de prueba.

## 3.2 Elementos permitidos si pasan su prueba

| Elemento | Criterio observable para permitirlo | ✅ Ejemplo que pasa | ❌ Ejemplo que falla | Consecuencia del fallo |
|---|---|---|---|---|
| Hecho de un proyecto | La afirmación coincide con una fuente primaria abierta, enlazada y fechada. | «El archivo `LICENSE` del repositorio indica Apache-2.0; consultado en la ruta enlazada al corte.» | «Tiene licencia libre» sin abrir licencia ni declaración oficial. | Retirar la afirmación o volver a verificarla. |
| Dato que cambia | Se indica qué se midió, dónde y cuándo; no se presenta una medición antigua como actual. | «La release visible en la página oficial está etiquetada 2.4; consulta del día X.» | «Está al día» apoyado en una cifra sin fecha. | Bloqueo hasta fijar el corte o declarar que no está comprobado. |
| Opinión editorial | Se marca como juicio de La Bandita y se explican los criterios que la sostienen. | «A juicio de esta ficha, cumple para quien prioriza instalación desde un repositorio mantenido.» | «Es la opción correcta» como si fuera un hecho universal. | Reescribir como opinión condicionada o suprimirla. |
| Comparación | Las opciones usan la misma unidad, criterio y fecha, o se declara la diferencia que impide compararlas. | Comparar dos repositorios por fecha de release con el mismo corte y la misma fuente. | Ordenarlos por estrellas de hosts distintos como si el conteo fuera equivalente. | Retirar el orden o reconstruir la comparación con base común. |
| Nivel de confianza | Cada señal visual corresponde a un umbral definido y a una evidencia visible. | ✅ significa «pasa los filtros descritos al corte»; la ficha aún enumera límites. | ✅ se usa para prometer ausencia de riesgo. | Cambiar el estado y explicar el riesgo antes de continuar. |
| Recomendación | Se dice para quién sirve, bajo qué condición y qué debería revisar antes de actuar. | «Puede servirte si necesitas esa función y aceptas el requisito de Android que se indica.» | «Instálala» sin explicar compatibilidad, fuente o límite. | Bloqueo de la llamada a la acción; completar la ficha. |
| Incertidumbre | Lo no verificado aparece con palabras directas, alcance y fecha; no se disfraza de conclusión. | «El sitio respondió con protección anti-bot; no pude leer su página al corte.» | Convertir esa respuesta en «el sitio está vacío» o «el proyecto no existe». | Corregir la conclusión y conservar el resultado exacto de la herramienta. |
| Cita y paráfrasis | Cita textual con comillas y atribución; paráfrasis señalada y enlazada. | Cita breve del README con nombre del proyecto y URL. | Copiar descripción ajena como voz propia o atribuirla a quien no la escribió. | Retirar, atribuir correctamente y revisar derechos/alcance. |
| Riesgo | Se identifica el mecanismo, su impacto posible y la medida prudente; severidad proporcional a la evidencia. | «Pide acceso a contactos, que no se justifica por la función descrita; no concedas ese permiso sin entender el motivo.» | Alarmar sobre una infección sin análisis ni evidencia del archivo. | Detener el texto; verificar o reducir la afirmación a lo demostrable. |
| Error o cambio | Se corrige en la pieza y en sus espejos con fecha, nota y motivo. | Nota fechada que dice qué dato cambió y de qué fuente salió. | Cambiar el texto en silencio y dejar circulando el dato anterior. | Añadir corrección visible y comprobar cada destino. |
| Crédito | Cada creador, recurso, método e información ajena aparece con atribución suficiente. | Autor público + proyecto citado + enlace a su casa. | «Gracias a la comunidad» cuando se conocen los autores concretos. | Completar créditos; el archivo no cierra hasta resolverlo. |

## 3.3 Elementos condicionales: solo con señalización y alcance

| Caso | Condiciones acumulativas | Ejemplo aceptable | Si una condición falta |
|---|---|---|---|
| Proyecto pequeño, alpha o beta | Declarar etapa, fecha y limitación; no confundir novedad con madurez. | «Está en alpha al corte; sirve para probar si aceptas fallos y cambios.» | No recomendar como herramienta estable; dejar fuera o mantener como observación sin llamada a instalar. |
| Fork o migración | Enlazar la casa canónica, declarar la relación y diferenciar continuidad de sustitución. | «El repositorio indica que es un fork; el historial y responsable están aquí.» | No inferir que el original transfirió su autoridad; verificar antes de recomendar. |
| Licencia ambigua o ausente | Copiar el estado exacto de la fuente y explicar qué no se puede concluir. | «GitHub devuelve `NOASSERTION`; no se ha confirmado aquí una licencia estándar.» | No afirmar que sea libre, redistribuible o compatible. |
| Aplicación con privilegios altos | Explicar qué privilegio concede, qué barrera reduce y quién podría necesitarlo. | Guía para usuarios avanzados con advertencias antes de cualquier instrucción. | No incluir pasos que aumenten el riesgo sin necesidad. |
| Sitio de riesgo | Nombrarlo solo si sirve a una lección o alerta; sin enlace directo ni instrucción para obtener el archivo. | Describir señales de una página de mods sin dirigir tráfico. | Quitar enlaces, llamadas y rutas que faciliten la instalación peligrosa. |
| Pronóstico o plazo futuro | Fuente primaria, fecha del anuncio, jurisdicción, grado de incertidumbre y lenguaje de posibilidad. | «La política anuncia este hito para el territorio indicado; fecha consultada X.» | No escribirlo como hecho ya ocurrido ni como cuenta regresiva vigente. |
| Dato de popularidad | Fuente canónica de la métrica y hora/fecha del corte; explicar qué mide. | Conteo de estrellas del repositorio oficial, medido en el día indicado. | Omitirlo; no sustituirlo por el número de un espejo. |
| Pregunta anticipada | Se identifica como duda posible y nace de un riesgo o decisión que el cuerpo sí trata. | «Si vas a cambiar de tienda, esta es la duda que suele surgir: …» con respuesta verificada. | No fabricar una FAQ para alargar la pieza ni fingir que un lector real la preguntó. |
| Adaptación de plataforma | Cambia solo formato, orden de vista previa o segmentación; conserva fuente, advertencia y conclusión. | Índice y números de parte al dividir una publicación larga. | Corregir el maestro y regenerar manualmente el plan; no publicar derivados contradictorios. |
| Reutilización de frase | Solo texto canónico obligatorio o referencia necesaria; no cuenta como aporte nuevo. | Firma textual idéntica en ambas ediciones. | Reescribir lo demás desde el caso; no clonar aperturas ni argumentos por aprobación previa. |

## 3.4 Prohibiciones de fondo (además de las fórmulas de §1.7)

Estas condiciones bloquean la pieza, aunque una herramienta no las detecte todavía:

- Afirmar que se abrió una fuente, se probó una app o se inspeccionó un archivo cuando no ocurrió.
- Presentar una reseña, estrella, descarga, commit o fecha de mirror como dato de la casa canónica.
- Convertir «no encontrado» en «no existe»; convertir un silencio, error HTTP o protección anti-bot en conclusión sobre el proyecto.
- Equiparar código público con seguridad total, ausencia de rastreo, privacidad garantizada o ausencia de vulnerabilidades.
- Recomendar cadáveres o bombas de tiempo para completar una lista o llegar a una cifra. Si se mencionan para enseñar a reconocer un riesgo, no se enlazan ni se receta su instalación.
- Rellenar con analogías repetidas, sinónimos, definiciones circulares, datos duplicados, listas sin decisión o enlaces sin explicación.
- Convertir una aprobación concreta en permiso de copiar voz, orden, meme, argumento o formato para todas las piezas siguientes.
- Producir datos, citas, testimonios, resultados de prueba, encuestas o respuestas de usuarios que no existen.
- Exponer tokens, claves, datos privados de lectores o datos personales de colaboradores no públicos.
- Dejar una advertencia de seguridad fuera del resumen o del corte solo para que la entrada parezca más atractiva.
- Presentar el texto en inglés como traducción revisada si solo se hizo traducción literal o automática.
- Seguir escribiendo debajo de Créditos, cambiando así el final y haciendo que la atribución deje de cerrar el archivo.

## 3.5 Estados de decisión y severidad

| Estado editorial | Condición observable | Acción |
|---|---|---|
| **Pasa al corte** | Evidencia suficiente para los filtros definidos; los límites están a la vista. | Puede aparecer en el cuerpo con estado y corte expresos; no equivale a garantía absoluta. |
| **Pasa con condición** | La función es útil, pero una condición material debe entenderse antes de actuar. | Explicar la condición junto al estado, no esconderla en el pie. |
| **Observación, no recomendación** | Hay interés educativo, pero no se alcanzó la evidencia o madurez requerida para recomendar. | Se puede describir el hueco sin enlace de descarga ni llamada a instalar, si aporta a la decisión. |
| **Fuera de los filtros** | Falla una condición de entrada o hay un riesgo no mitigado. | No incluir en la lista recomendada; si se cita para advertir, aplicar §3.3. |
| **Sin determinar** | La evidencia disponible no permite decisión honesta. | Declararlo y detener el veredicto; no llenar el vacío con intuición. |

Los estados se asignan a partir de hechos concretos, no de simpatía por el autor, número de estrellas, presión del público ni deseo de llegar a la meta de tamaño. La prueba es reproducible: otra persona puede abrir las mismas fuentes, ver la misma fecha y reconstruir por qué se eligió el estado.

## 3.6 Prueba de aceptación de la matriz

Antes de aprobar una pieza, revisar cada afirmación importante y responder:

1. ¿Es un hecho, una opinión, una inferencia o una recomendación? ¿Está etiquetada como tal?
2. ¿Qué fuente abierta y fechada permite comprobarla?
3. ¿Qué límite o contraejemplo cambiaría la decisión?
4. ¿El nivel visual y el texto dicen lo mismo?
5. ¿Una aprobación anterior o una herramienta automática está influyendo donde debería mandar la evidencia de este caso?
6. ¿Se puede quitar una frase sin pérdida de decisión, comprensión, evidencia o seguridad? Si sí, quitarla.

✅ La persona que revisa puede reconstruir la conclusión y llegar a un veredicto con los mismos criterios.
❌ La pieza solo convence por adjetivos, cantidad, urgencia o reputación prestada.
**Consecuencia:** una respuesta «no» en las preguntas 1–4 detiene publicación; una respuesta «sí» en la pregunta 6 exige recortar el relleno y volver a medir.

---

# PARTE IV — VERIFICACIÓN, EVIDENCIA Y VARA EJECUTABLE

## 4.1 Dos pruebas distintas: verdad y forma

Una herramienta de texto puede encontrar ciertos patrones; no puede abrir la mente de quien redactó ni confirmar por sí sola que un repositorio sostiene una afirmación. Por eso la casa lleva dos resultados separados:

1. **Prueba de evidencia:** una persona abre fuentes primarias, anota fecha y registra qué dato respalda cada afirmación.
2. **Prueba mecánica:** la vara detecta los patrones y requisitos estructurales que tiene programados.

Las dos hacen falta. Una prueba mecánica verde con una fuente sin abrir **no** deja la pieza lista. Una investigación bien hecha con una frase prohibida o con una sección obligatoria ausente tampoco.

## 4.2 Registro de afirmaciones y fuentes

Por cada afirmación que pueda cambiar una recomendación, mantener una fila privada con estos campos:

| Campo | Registro necesario |
|---|---|
| ID y texto usado | Frase concreta del borrador y un identificador estable. |
| Fuente | URL completa y casa canónica, no solo el resultado de búsqueda. |
| Acceso | Fecha/hora y zona, respuesta observada, página o release efectivamente abierta. |
| Evidencia | Extracto breve, ruta, nombre de archivo, número de release o SHA si aplica. |
| Alcance | Qué demuestra y qué no demuestra la fuente. |
| Conflictos | Otras fuentes que discrepan y cómo se resolvió o por qué queda pendiente. |
| Estado | Verificado, acotado, pendiente o descartado. |
| Destino | Dónde aparece la afirmación en cada maestro de idioma. |

Jerarquía de fuentes:
- **Primaria:** repositorio o casa que el propio proyecto declara oficial; archivo de licencia, release, documentación o anuncio original.
- **Confirmación independiente:** medio u organización identificable, útil cuando la afirmación afecta seguridad, legalidad, política o impacto a terceros.
- **Índice o buscador:** sirve para descubrir una ruta, no para cerrar una verificación. Se abre la fuente que el resultado cita.

Reglas concretas:
- La estrella de GitHub pertenece al repositorio de GitHub abierto; no se atribuye a un proyecto cuya casa oficial está en GitLab o Codeberg.
- «Último commit», «última release», «última etiqueta» y «sitio responde» son señales diferentes; se escribe cuál se midió.
- El nombre de la licencia se copia del archivo o declaración legal; la etiqueta automática de una plataforma se conserva como etiqueta de esa plataforma.
- Un estado HTTP informa sobre esa petición y esa fecha; no prueba que el proyecto desapareció ni que el contenido sea malicioso.
- Una fuente sin abrir, un extracto de buscador y un dato heredado de una pieza antigua no cuentan como verificación nueva.
- Nunca se incluyen tokens, llaves, cabeceras de autorización ni URL privadas en la pieza o en un registro destinado a publicarse.

✅ Correcto: «La release 2.4 aparece en la casa oficial, abierta el día X; esta evidencia confirma la etiqueta, no la seguridad de cada uso».
❌ Incorrecto: copiar el número de la pieza anterior y cambiarle la fecha sin abrir la fuente.
**Consecuencia:** la afirmación se bloquea o se rotula pendiente; no se le da un tono más seguro para disimular la falta de evidencia.

## 4.3 Fecha, entorno y selección de herramientas

La puerta G0–G1 de §0.6 se ejecuta así:

1. Anotar la fecha de referencia y zona horaria que verá el lector.
2. Si el reloj del entorno contradice una fuente independiente, no escoger el reloj que conviene: comparar una referencia temporal fiable y dejar anotado cuál se usó.
3. Abrir el archivo de trabajo y comprobar su ruta, idioma, versión y estado antes de tocarlo.
4. Elegir la herramienta más pequeña que permita observar o comprobar el requisito. Preferir lectura antes que escritura, y operación sin red antes que dar acceso de red innecesario.
5. Registrar límites: acceso denegado, captcha, API caída, falta de credenciales o fuente no disponible. Nunca afirmar que una herramienta hizo algo que no hizo.

Una marca de tiempo del sistema es un dato del entorno, no una fuente del hecho externo. Si la fecha cambia el veredicto, se comprueba antes de continuar.

## 4.4 Qué comprueba `vara_bandita.py`

La herramienta es un **linter determinista**: lee el archivo, calcula condiciones programadas, imprime un informe y termina con un código. No genera, corrige, traduce, completa ni publica texto.

| Control actual | Resultado | Límite que el operador no debe ocultar |
|---|---|---|
| Fórmulas literales vetadas | ROJO si detecta una de las variantes programadas en una pieza pública | No detecta cada sinónimo posible; hay que leer también el sentido de la frase. |
| Autoridad vacía, meta-comentarios y promesas programadas | ROJO | La lista de patrones no sustituye la revisión humana de formas nuevas de humo. |
| Superlativos detectados | Aviso para revisar criterio; puede informar si encuentra una fórmula de criterio programada | El aviso no decide por sí solo si la comparación es justa o verificable. |
| Firma, lema, meme y notas al pie | Informa o avisa según los patrones presentes | Presencia textual no demuestra que el meme sea original ni que las notas sean ciertas. |
| Longitud del archivo | Banda mecánica por número de caracteres; piso predeterminado **45.001** y guía de despliegue de 63.000 | Cuenta caracteres del archivo, no sustancia. La ficha de §§2.7 y 4.7 decide si el cuerpo aporta de verdad. |
| Modo norma | Excluye del análisis de frases solo los bloques explícitos de mención; no aplica banda ni estructura de pieza | No certifica que cada bloque marcado sea realmente una cita necesaria; eso se revisa a mano. |

Uso desde la raíz del espacio de trabajo:

```bash
python3 work/edt/proyectos/la-bandita/manual-v0.0.1/vara_bandita.py ruta/PIEZA-ES.md
python3 work/edt/proyectos/la-bandita/manual-v0.0.1/vara_bandita.py ruta/MANUAL.md --modo-norma
python3 -m unittest discover -s work/edt/proyectos/la-bandita/manual-v0.0.1 -p 'test_*.py' -v
```

Códigos de salida:
- **0 — VERDE:** pasó los controles mecánicos activos; no es certificado de veracidad, originalidad ni seguridad.
- **1 — ROJO:** hay un bloqueo. No se publica.
- **2 — VENTANA:** quedan avisos. No se publica hasta resolver cada uno y volver a comprobar, o se entrega únicamente como parcial con el aviso visible.

`--meta-min N` y `--tope-max N` permiten una banda distinta para una prueba explícita; cualquier cambio de parámetro queda escrito junto al resultado. `--modo-norma` desactiva los requisitos de estructura de una pieza y la banda, pero **no** debe usarse para auditar una publicación pública.

## 4.5 Citas en documentos normativos: excepción estrecha y comprobable

Una norma debe poder nombrar una fórmula para prohibirla. Por eso sus menciones pedagógicas se delimitan en el archivo con este par exacto:

```markdown
<!-- VARA:MENCION:INICIO -->«cita didáctica exacta»<!-- VARA:MENCION:FIN -->
```

El bloque contiene solo la cita necesaria, no la regla que la prohíbe ni el párrafo entero. Debe aparecer balanceado y sin anidamiento. La vara conserva los saltos de línea para que los números de línea posteriores sigan siendo útiles.

- En `--modo-norma`, los controles de uso omiten solo esos bloques marcados y dan cuenta de cuántos encontraron.
- En el modo normal de pieza, las marcas no dan exención: la herramienta marca la fórmula y también bloquea el uso del marcador.
- Un bloque mal cerrado, anidado o usado para esconder prosa normativa deja la auditoría en ROJO o requiere corrección humana; no se borra el hallazgo en silencio.

La prueba unitaria cubre las dos caras: una cita marcada no salva una pieza pública; una cita marcada sí permite que una norma se revise sin confundir mención con uso; una frase fuera del bloque sigue bloqueando; los marcadores defectuosos bloquean; los números de línea no se desplazan; la forma «100 %» se detecta; y exactamente 45.000 caracteres no cumple el requisito «más de 45.000».

## 4.6 Autocontrol de la propia vara

Antes de confiar en un cambio de la herramienta:

1. Ejecutar sus pruebas unitarias: deben pasar todas.
2. Probar al menos un archivo conocido que cumpla y una muestra negativa diseñada para fallar.
3. Probar los dos contextos que pueden confundirse: norma con cita marcada y pieza pública con la misma cita.
4. Confirmar que una marca mal formada falla cerrado y no convierte el documento en VERDE.
5. Ejecutar la herramienta sobre el archivo que realmente se entregará.

La suite de la vara en `test_vara_bandita.py` contiene ocho pruebas para la frontera mención/uso, el umbral y la numeración. `test_manual_coverage.py` añade dos comprobaciones estructurales: que cada sección numerada tenga fila y que las 70 filas tengan cinco campos, ejemplos distintos y consecuencia no vacía. Estas dos no validan semántica; la lectura humana de correspondencia sigue siendo obligatoria. Si cambia una regla de la vara o de la matriz, se actualiza su prueba en el mismo trabajo. Una prueba aprobada no autoriza a cambiar parámetros para hacer pasar un documento particular.

## 4.7 Revisión de sustancia y lectura humana

Antes de aceptar una pieza, la persona revisora recorre el texto entero, no solo el informe:

- Abre las fuentes decisivas y comprueba que cada afirmación esté respaldada por el contenido real.
- Contrasta la cuenta de sustancia por sección de §2.7; confirma que se excluyeron aparato, créditos, notas administrativas, enlaces sueltos y texto repetido.
- Lee el inicio como lector que quiere una respuesta rápida, el cuerpo como lector que quiere aprender y las advertencias como lector que busca riesgos.
- Comprueba que ninguna analogía prometa más que el hecho, que los estados visuales coincidan con las condiciones escritas y que una opinión esté etiquetada.
- Revisa privacidad, atribución, cierre editorial y que Créditos sea literalmente la última sección.
- Compara con las piezas cercanas para detectar copia o convergencia; la comparación no puede ordenar a un generador que imite o produzca «variaciones» superficiales.

La máquina no firma esta revisión. El informe identifica qué comprobó el programa; la persona identifica qué comprobó leyendo fuentes y texto. Si ambas cosas se mezclan en una sola palabra («aprobado»), se vuelve imposible saber qué quedó probado.

## 4.8 Registro reproducible de una auditoría

Junto a cada entrega conservar, dentro del espacio de trabajo y sin secretos:

| Campo | Ejemplo de registro |
|---|---|
| Archivo final y idioma | Ruta exacta del maestro ES o EN. |
| Versión del contenido | `v0.0.1` y número/edición de la pieza. |
| Corte | Fecha/hora/zona que se usó para datos cambiantes. |
| Fuentes | Ruta al registro de afirmaciones y URLs abiertas. |
| Sustancia | Cuenta por sección y revisión humana de caracteres que sí aportan. |
| Comando | Texto exacto ejecutado, incluidos parámetros y modo. |
| Resultado | Código de salida, veredicto e informe sin recortar los bloqueos. |
| Integridad | SHA-256 del archivo probado para que se identifique esa versión exacta. |
| Pendientes | Límites, advertencias sin resolver y estado parcial/completo. |

Cualquier cambio después de calcular el SHA o correr la vara crea otra versión de archivo: se repite la comprobación y se conserva el resultado nuevo. No se presenta un informe viejo como si validara un archivo nuevo.

---

# PARTE V — AMBIGÜEDADES: RESOLVER SIN ADIVINAR

## 5.1 Cuándo preguntar y cuándo declarar el supuesto

Una ambigüedad importa si dos lecturas razonables producirían entregables, veredictos o riesgos distintos. Si cambia una de esas cosas, se hace una pregunta concreta antes de cruzar la puerta afectada. Si no cambia el resultado material, se elige la lectura mejor apoyada por el contexto y se declara el supuesto.

| Ambigüedad | Lectura que se puede sostener | Atajo que falla | Acción y consecuencia |
|---|---|---|---|
| Reloj del entorno vs fecha de una fuente | Distinguir fecha local, UTC y fecha de publicación; comprobar un reloj independiente si la decisión depende del día. | Copiar el reloj que coincide con el texto preparado. | Detener datos temporales hasta resolver; anotar la referencia usada. |
| Casa oficial vs espejo | La casa que el propio proyecto señala gobierna identidad y métricas; el espejo es una ruta secundaria. | Atribuir al proyecto original el conteo del espejo. | Corregir enlace y cifra; si la casa no se puede establecer, declarar «no resuelto». |
| Commit vs release | Commit = cambio al código; release = versión publicada; etiqueta = nombre de referencia. | Llamar «actualizada» a una app solo porque hubo un commit. | Reescribir el tipo de actividad medido y volver a abrir la página. |
| Sitio sin respuesta | Solo se afirma el resultado de esa petición al corte. | Concluir que el proyecto dejó de existir o es malicioso. | Registrar el código/respuesta; buscar la casa de código por separado. |
| Licencia ausente o incierta | Estado legal no confirmado; la etiqueta automática es una observación técnica. | Inferir derechos de uso del hecho de que el código sea visible. | No recomendar redistribución ni declarar licencia hasta ver fuente legal. |
| «Procede» o «aprobado» | Alcance explícito en el mensaje al que responde. | Tratar aceptación de un artefacto como permiso para todos los futuros. | Registrar qué decisiones abarca; fuera de ese ámbito se vuelve a G2. |
| Por idioma vs por plataforma | Un maestro ES y uno EN; segmentar el despliegue sin crear cuatro maestros. | Reactivar archivos viejos por canal porque el lote antiguo tenía esas columnas. | Usar el modelo ratificado; toda excepción requiere cambio expreso del dueño. |
| Meta de 45.000 caracteres vs sustancia | Cada idioma supera 45.000 caracteres sustantivos, además de pasar la medición bruta. | Sumar idiomas, créditos o párrafos repetidos para cruzar el umbral. | Completar la cuenta por sección; si no llega, detener la pieza o investigar más dentro del alcance. |
| Mensaje de issue vs estado del cambio | Una respuesta explica una posición; merge, cierre, release y CI son estados distintos. | Tomar un comentario como prueba de que el código se fusionó o el problema se resolvió. | Consultar cada estado en su fuente y nombrar por separado lo que confirmó. |
| Error de herramienta vs resultado del mundo | La salida describe esa ejecución, árbol, parámetro y momento. | Leer un árbol sintético, caché o espejo como si fuese producción. | Identificar el origen de la salida y repetir contra la fuente correcta. |
| Dato no encontrado vs búsqueda incompleta | «No localizado en estas fuentes/rutas» describe el alcance de búsqueda. | Convertirlo en «no existe». | Acotar el resultado; si el usuario necesita una conclusión más fuerte, preguntar o ampliar búsqueda. |
| Encargo parcial vs encargo completo | La etiqueta depende de los criterios acordados, no del esfuerzo invertido. | Llamar «listo» a la primera entrega de una serie. | Declarar números hechos y pendientes; E06 bloquea la falsa completitud. |

## 5.2 Prueba de materialidad de una duda

Antes de preguntar, completar mentalmente tres puntos:

1. ¿Qué dos resultados distintos producirían las lecturas posibles?
2. ¿Cuál afecta una decisión, una persona, una fuente, un archivo o el plazo?
3. ¿Qué pregunta corta separa las dos lecturas sin obligar al usuario a repetir todo?

✅ «¿Quieres que mantenga la lista como dos maestros, uno por idioma, o autorizas una excepción de idioma/plataforma para esta pieza?» — cambia el archivo que se va a producir.
❌ «¿Qué quieres exactamente?» — no identifica qué decisión está bloqueada.

Si la duda no altera sustancia, seguridad, identidad, idioma ni destino, no se interroga por cubrirse: se anota el supuesto y se sigue. Si sí altera alguno, no se adivina. **Consecuencia:** la puerta queda detenida hasta que el usuario responda o el operador encuentre evidencia suficiente para resolver sin suponer.

## 5.3 Desempate entre reglas

Cuando dos normas parecen chocar, se aplica este orden:

1. Seguridad, privacidad, no exposición de secretos y veracidad comprobable.
2. Instrucción expresa del dueño con alcance definido.
3. Modelo editorial ratificado de v0.0.1 y requisitos obligatorios del idioma.
4. Guía de la plataforma vigente en la fecha de despliegue.
5. Convención histórica, preferencia de estilo o comodidad del operador.

Una convención heredada nunca desplaza una decisión ratificada. La seguridad no se rebaja para llegar a la meta de longitud; la longitud tampoco se usa para esconder un hueco de evidencia. Si el conflicto no se resuelve con esta precedencia, se documenta y se pregunta.

---

# PARTE VI — TAXONOMÍA DE FALLOS Y CONTRAPARCHES

## 6.1 Registrar una falla para no volver a pagarla

Una falla se registra cuando hay evidencia de que una regla, herramienta o decisión produjo un resultado incorrecto o una afirmación engañosa. No se registra una sospecha como causa raíz.

Cada entrada contiene: **síntoma observable → evidencia → causa comprobada o «aún desconocida» → impacto → contraparche → prueba que debe fallar → prueba que debe pasar → estado**. La contramedida no se declara cerrada hasta correr ambos sentidos cuando sea posible. El registro describe el mecanismo; no humilla a una persona.

| Estado | Qué significa | Criterio de salida |
|---|---|---|
| ACTIVA | La causa sigue presente o la corrección no se ha probado. | No se marca la tarea relacionada como completa. |
| CONTRAPARCHADA | Hay cambio y una prueba positiva/negativa que demuestra el comportamiento previsto. | Conservar resultado, alcance y versión comprobada. |
| OBSERVADA | Se identificó un riesgo, pero todavía no ocurrió o no hay causa confirmada. | No presentarla como falla resuelta; mantenerla como riesgo. |
| RETIRADA | La regla o herramienta dejó de gobernar el modelo nuevo. | Indicar qué la reemplaza y conservarla solo como antecedente. |

## 6.2 Familias de fallos

| Familia | Qué vigila | Pregunta de diagnóstico | Acción inmediata |
|---|---|---|---|
| **A · Veracidad** | Dato incorrecto, fuente mal leída, fecha o repositorio equivocado. | ¿Qué fuente abierta respalda la frase exacta? | Retirar o corregir la afirmación; añadir fecha y evidencia. |
| **B · Calibración** | Opinión presentada como hecho, certeza excesiva o comparación injusta. | ¿El lenguaje tiene la misma fuerza que la evidencia? | Etiquetar el juicio, fijar criterio y rebajar solo lo que la evidencia exige. |
| **C · Alcance** | Responder otra pregunta, preguntar de más/de menos o declarar completo lo parcial. | ¿Se cumplió el encargo exacto y se resolvió la duda material? | Volver a G2; preguntar si el resultado cambia; marcar faltantes. |
| **D · Seguridad y privacidad** | Exposición, consejo que aumenta riesgo, falta de mitigación o datos personales innecesarios. | ¿Qué daño razonable puede causar y qué barrera se conserva? | Parar publicación; retirar dato o instrucción peligrosa y revisar P10. |
| **E · Evolución y cumplimiento** | Regla decorativa, compuerta sin prueba, molde que deriva o automatización fuera de alcance. | ¿Hay evidencia de que la regla se cumplió en el archivo final? | Ajustar la regla o herramienta, escribir una prueba y volver a auditar. |
| **F · Interacción y rol** | Promesa que no se puede cumplir, verificación fingida o confusión sobre capacidades. | ¿Se afirmó que se hará algo que no está habilitado o no se hizo? | Reconocer, corregir y describir el límite real sin prometer vigilancia futura. |

Los códigos heredados que ya aparecen en el cuerpo se conservan en su alcance documentado: B08, C05, C10–C12 y F05–F06. Si no está disponible la ficha histórica completa de un código, no se inventa una definición nueva bajo ese mismo número; se describe el síntoma y se registra una entrada nueva.

## 6.3 Familia E: fallos y riesgos de evolución documentados

| Código | Falla/riesgo y señal comprobable | Contraparche y prueba de cierre |
|---|---|---|
| E01 | Regla decorativa: escrita, pero sin criterio observable ni comprobación. | Añadir condición de salida, ejemplo de paso/fallo y control responsable; probarlo en una pieza. |
| E02 | Vara no auto-testeada o un «verde» afirmado sin correrla sobre el archivo íntegro. | Ejecutar modo correcto, guardar salida y probar un caso conocido que debe fallar. |
| E03 | Fórmula absoluta o metáfora gastada usada como recurso de venta. | Reformular con criterio y evidencia; la pieza pública debe quedar estricta en ROJO=0. |
| E04 | Firmas o cierres que compiten entre documentos. | Mantener una firma textual y un lema, ambos exactos; buscar colisiones y probar el cierre final. |
| E05 | Añadir material de baja calidad para satisfacer una cuota. | Quitar cadáveres, bombas de tiempo y repeticiones; ampliar solo con recursos que pasen filtros. |
| E06 | Presentar una hornada o entrega parcial como obra completa. | Declarar alcance, cantidades y pendientes; un estado parcial no se renombra como completo. |
| E07 · riesgo preventivo | Una aceptación local se convierte sin permiso en pauta de estilo para futuros casos. Aún se registra como riesgo, no como incidente consumado. | Guardar el alcance y exigir autorización expresa antes de generalizar; contrastar la siguiente pieza con sus propias fuentes. |
| E08 · incidente observado | Una versión temporal del manual perdió líneas citadas y su VERDE se describió como si probara el archivo entero. | Auditar el archivo completo con menciones delimitadas; registrar ruta y SHA; separar pruebas de cita y uso. |
| E09 · brecha observada | El conteo de caracteres brutos se podía leer como prueba de sustancia sin una cuenta semántica por sección. | Separar piso mecánico y sustancia; mantener cuenta humana por sección con función y evidencia (§2.7, §9.4). |

## 6.4 Cómo cerrar una entrada sin esconder la recaída

✅ Correcto: «El control falló por una lista de citas didácticas sin marcar; se añadieron delimitadores explícitos, ocho pruebas cubren usos/citas y el archivo íntegro da VERDE. La revisión factual sigue separada.»
❌ Incorrecto: «Ya está arreglado» después de retocar el archivo, sin ejecutar la prueba negativa ni guardar el resultado.

Si la contramedida causa otra falla, se añade la evidencia a la entrada o se abre una nueva que enlace la anterior; no se reescribe el historial como si la primera no hubiera ocurrido. **Consecuencia:** una falla activa impide declarar verde la compuerta que la cubre; una contramedida sin prueba queda en estado ACTIVA.

---

# PARTE VII — FLUJO DE PRODUCCIÓN Y PUBLICACIÓN

## 7.1 Del encargo al archivo publicado

La secuencia G0–G7 de §0.6 gobierna todo encargo. Esta Parte ordena el trabajo editorial de una pieza o lote, sin imponerle una voz ni un argumento genérico.

| Etapa | Trabajo | Evidencia para cerrar la etapa | Si no pasa |
|---|---|---|---|
| 1. Recibir y delimitar | Convertir el pedido en alcance, dos idiomas, destinos, exclusiones, estado de piezas previas y criterios de aceptación. | Ficha privada §2.2 completa; dudas materiales resueltas o suposiciones declaradas. | No se abre el borrador definitivo. |
| 2. Fijar fecha y entorno | Registrar corte; revisar archivo, permisos, ramas, herramientas y almacenamiento relevantes. | Ruta, versión, estado previo y herramientas efectivamente disponibles. | No se edita ni se informa como verificado. |
| 3. Investigar | Localizar fuentes primarias y corroboraciones necesarias; apuntar evidencia por afirmación. | Registro de afirmaciones §4.2; huecos y contradicciones visibles. | Acotar, preguntar o detener. |
| 4. Seleccionar | Aplicar criterios de entrada y salida a candidatos; quitar duplicados y opciones sin casa verificable. | Matriz de candidatos con evidencia, decisión y motivo de descarte. | No añadir recursos para engordar el total. |
| 5. Diseñar | Definir qué decisión resuelve el lector, qué es nuevo y qué orden conviene al tema. | Mapa de secciones, fuentes y pruebas; razones específicas para la estructura. | Replantear antes de redactar; no copiar una pieza aprobada. |
| 6. Escribir español | Crear el maestro ES desde el caso y sus fuentes, con voz natural y Feynman. | Lectura completa, cuenta de sustancia y verificación de cada dato ES. | No pasar a traducción ni declarar el par terminado. |
| 7. Escribir inglés | Crear un maestro EN de forma independiente con los mismos hechos verificados y adaptación idiomática. | Revisión nativa de claridad, hechos, fechas, links y meme EN. | Dejar el par parcial y decir qué falta. |
| 8. Auditar el par | Ejecutar controles mecánicos y lectura humana por archivo; revisar créditos y similitud semántica. | Dos comandos, dos resultados, dos SHA y dos cuentas de sustancia. | Corregir cada idioma y repetir la prueba sobre el archivo exacto. |
| 9. Preparar despliegue | Definir cortes por canal solo si hace falta; revisar vista previa y continuidad. | Mapa de publicación que apunta a los dos maestros y no cambia sus hechos. | Corregir el plan, no fabricar copias divergentes. |
| 10. Entregar y checkpoint | Presentar rutas, alcance, resultados, límites, estado y siguiente paso. | Registro persistente del hito y estado completo/parcial. | Sin checkpoint, el trabajo no se considera cerrado para otro turno. |

## 7.2 Lotes, checkpoint y continuidad

Un lote contiene piezas identificadas por número y etapa. El estado se guarda fuera del texto público con: tarea, archivo exacto, idioma, fase, hechos verificados, pruebas corridas, SHA, pendientes, bloqueos y próximo paso. Al retomar se vuelve a leer ese estado y se inspecciona el archivo; no se reconstruye de memoria.

Desde esta edición, el orden de cierre de cada hito es ejecutable y no decorativo: `manual-v0.0.1/guarda_lote.py` valida, sobre los archivos exactos, el piso mecánico por maestro (≥45.001 caracteres UTF-8), la similitud por shingles de 5 palabras contra referencias del corpus (alarma de convergencia por encima de 0,32), la secuencia de la bitácora (un ROJO previo bloquea el siguiente VERDE salvo `--aceptar-riesgo` con motivo escrito, que queda registrado) y el almacenamiento contra el límite de 50.000.000 bytes, y escribe su bitácora JSONL con SHA-256, fecha y procedencia de la fecha. Con `--exigir-git` exige además que ambos maestros estén bajo seguimiento de git antes de cerrar el hito: un trabajo que solo vive en local no cuenta como persistido. La guarda certifica esas compuertas mecánicas y el orden; no verifica hechos, originalidad ni sustancia, que siguen siendo humanas.

Por la falla histórica de perder trabajo al abarcar decenas de piezas en una sola ejecución, se trabaja como máximo con **dos maestros por hito de checkpoint**. Un par ES+EN ocupa esos dos espacios. Solo se agranda el lote si cada hito quedó escrito y espejado antes de empezar el siguiente. Si una herramienta agota tiempo o se reinicia el entorno, se retoma desde el último archivo persistido; no se repite un tramo que ya se pueda comprobar.

Cada pieza se mueve por estados separados:
- **Pendiente de investigación:** todavía no hay evidencia suficiente.
- **Investigada:** fuentes y decisión están registradas; no implica que exista texto.
- **Borrador:** hay texto, todavía no validado.
- **Auditada:** evidencia, lectura humana y vara terminadas; todavía puede faltar despliegue.
- **Lista:** ambos maestros superan sus compuertas y tienen créditos finales.
- **Publicada:** existe enlace real de publicación comprobado; un archivo local no recibe esa etiqueta.

## 7.3 Gestión de cambios y correcciones

Cada corrección deja cuatro cosas: qué frase estaba mal o incompleta, qué evidencia la corrige, cuándo se cambió y en qué destinos se propagó. La versión anterior se conserva como evidencia cuando haga falta reconstruir el incidente; no se borra para aparentar que nunca ocurrió.

Si cambia una fuente tras publicar, se decide según impacto:
1. **Sin cambio de conclusión:** actualizar dato/corte y explicar el ajuste.
2. **Cambia la recomendación o el riesgo:** corregir el encabezado/resumen, el cuerpo y los despliegues conectados el mismo ciclo posible.
3. **No puede comprobarse el cambio:** marcar pendiente y retirar temporalmente la llamada que dependa del dato.

No se promete seguimiento en el futuro. Se indica al lector dónde está el registro actual y qué fecha tiene.

## 7.4 Barrera de cierre por lote

Un lote solo se marca completo si todos los IDs previstos aparecen con estado, los dos idiomas de cada pieza están contados por separado, los fallos se resolvieron y el manifiesto coincide con los archivos reales.

✅ Correcto: «Piezas 01–02: dos pares investigados, editados y probados; 03–70 permanecen pendientes».
❌ Incorrecto: «Bilingües listos» cuando solo se fusionaron cuerpos antiguos o existe solo el español.

**Consecuencia:** la cifra de avance se calcula con archivos y pruebas existentes; cualquier diferencia se declara y el lote sigue abierto.

---

# PARTE VIII — MÉTRICAS, AUDITORÍA Y DERIVA

## 8.1 Métrica madre y medidas que la sostienen

La métrica madre sigue siendo **crecer sin diluir la confianza**. Las cifras de alcance, estrellas, comentarios o aprobación no son esa confianza; son observaciones parciales que pueden ayudar a encontrar preguntas, no a reemplazar verificación.

| Medida | Cálculo o evidencia | Objetivo de cumplimiento | Respuesta si falla |
|---|---|---|---|
| Cobertura del encargo | Maestros terminados con evidencia ÷ maestros exigidos, con numerador y denominador explícitos | 100 % para declarar el encargo completo | Declarar parcial con IDs que faltan; no redondear ni renombrar. |
| Trazabilidad | Afirmaciones que requieren fuente y tienen fuente abierta/corte ÷ afirmaciones que requieren fuente | 100 % en los hechos que sostienen el veredicto; ningún hueco oculto | Reducir el alcance o abrir la fuente antes de publicar. |
| Integridad mecánica | Piezas en ROJO y avisos sin resolver | 0 bloqueos y 0 avisos sin tratamiento al cierre | Volver a edición y repetir controles. |
| Sustancia | Cuenta humana por sección, separada del conteo bruto | Más de 45.000 caracteres sustantivos en cada maestro lingüístico | Investigar material pertinente o detener; nunca rellenar. |
| Correcciones | Notas fechadas y destinos corregidos frente a errores encontrados | 100 % de correcciones visibles y rastreables; no se premia «cero correcciones» | Corregir espejo, anotar fecha y buscar la causa. |
| Privacidad | Datos personales/secretos incluidos sin necesidad y permiso | 0 exposición no justificada | Retirar, contener y documentar el incidente antes de publicar. |
| Diferencia real entre piezas | Revisión humana del problema, fuentes, decisión y aporte | Cada nueva pieza tiene propósito propio; no hay cuota de «originalidad cosmética» | Fusionar, actualizar, recortar o detener si duplica sin aportar. |
| Comprensión del lector | Dudas o confusiones reales, con el menor dato personal posible | Resolver dudas observadas; no fingir una encuesta | Corregir el pasaje y anotar qué cambió. |

Las cifras de usuarios del proyecto describen escala y diversidad; no autorizan a inventar porcentajes de satisfacción, lectores tipo observados ni resultados de encuesta. Si no hay medición real, no se publica una cifra de impacto.

## 8.2 Auditoría de deriva sin optimizar por semejanza

Después de una hornada, revisar piezas cercanas en pares y registrar:

- si resuelven preguntas distintas o si una debe ser actualización de otra;
- qué afirmaciones comparten fuente y si el corte de cada una sigue vigente;
- qué estructura se repitió porque el lector la necesita y qué parte se repitió por inercia;
- si cada meme, analogía y entrada nació del tema y del idioma concretos;
- si una aprobación localizada se filtró a otros contextos sin permiso.

La comparación es una **alarma editorial humana**, no un puntaje que optimiza texto hacia el promedio del corpus. Si dos casos conducen a la misma conclusión por evidencia, se puede conservar la conclusión y explicar por qué; no se fuerzan diferencias para que parezcan novedosos.

Como apoyo mecánico existe `guarda_lote.py`: calcula shingles de 5 palabras e índice de Jaccard entre un maestro candidato y las referencias que se le indiquen, y marca ROJO por encima de 0,32, nombrando el archivo que disparó la alarma. Es una alarma asistida por máquina, no un medidor de calidad ni de originalidad: puede dejar pasar reescrituras superficiales y puede señalar falsos positivos en corpus legítimamente parecidos; ambos casos los decide una persona sobre el archivo exacto. Un «aprobado» nunca baja el umbral: cada pieza se audita contra sus propias fuentes.

Un «aprobado» no es una métrica de desempeño ni un multiplicador de frases aceptadas. La métrica no premia cuánto se parece la siguiente respuesta a la aprobada; mide si la tarea actual queda verificada, clara y dentro de su alcance.

## 8.3 Cuándo revisar una regla o el manual

Revisar una regla cuando ocurra cualquiera de estas señales:
- el mismo fallo aparece más de una vez;
- la vara produce un falso positivo o deja pasar un contraejemplo real;
- cambian las plataformas, las fuentes o el modelo de publicación;
- una regla impide cumplir otra decisión ratificada;
- un lector señala una confusión concreta que la pieza no anticipó.

El cambio sigue el mecanismo de §1.2: registrar lección, alcance, evidencia, efecto, prueba y nota de versión. Una reacción aislada puede abrir investigación, pero no modifica automáticamente una regla general.

✅ Correcto: registrar una crítica, comprobarla en el texto y corregir el apartado que causa confusión.
❌ Incorrecto: cambiar todas las piezas por una sola reacción o ignorar una evidencia incómoda porque hubo comentarios favorables.
**Consecuencia:** las reglas se actualizan con evidencia y alcance explícito, no por promedio de aprobación.

## 8.4 Registro de auditoría de la hornada

Al cerrar una hornada se informa: piezas previstas/hechas, estado por ID, cobertura ES/EN, fallos encontrados/corregidos, pruebas ejecutadas, avisos abiertos, cambios de regla, almacenamiento utilizado y siguiente paso. Las cifras se copian de los archivos o comandos medidos; no se calculan de memoria.

---

# PARTE IX — ANEXOS DE TRABAJO Y GLOSARIO

## 9.1 Los anexos son registros, no prompts

Los formatos de esta Parte guardan evidencia y estado. No se copian como instrucciones genéricas para producir textos. Se completan con los datos reales del encargo y no con ejemplos inventados; el cuerpo se escribe desde sus fuentes y su lector.

## 9.2 Registro privado de una pieza maestra

```text
ID de pieza:
Ruta ES / estado:
Ruta EN / estado:
Encargo exacto y alcance:
Decisión concreta del lector:
Exclusiones y motivo:
Corte y zona horaria:
Fuentes abiertas / registro de afirmaciones:
Aporte propio respecto del material previo:
Mapa de secciones y función de cada una:
Cuenta de sustancia ES / cuenta de sustancia EN:
Resultados de revisión humana:
Comando y salida de vara ES / SHA-256:
Comando y salida de vara EN / SHA-256:
Plan de despliegue por canal:
Créditos completos y última línea:
Pendientes / bloqueos:
Próximo paso verificable:
```

Una casilla vacía significa «sin registrar», no «cumplido». Si un campo no aplica, se anota la razón. No se rellena con «N/A» para esconder una fuente que falta.

## 9.3 Registro de evidencia

```text
ID | afirmación | URL canónica | fecha/hora de acceso | evidencia observada
   | qué demuestra | qué no demuestra | conflicto | estado | sección ES/EN
```

Los registros publicados no incluyen cabeceras, tokens, datos personales ni rutas privadas. Los detalles internos que pudieran exponer a una persona se eliminan o se guardan fuera de la pieza; la trazabilidad pública no justifica exponer secretos.

## 9.4 Cuenta de sustancia y revisión de cambios

```text
Sección:
Decisión/aprendizaje que sirve:
IDs de evidencia y fecha:
Texto que sí cuenta como aporte:
Texto excluido del conteo y motivo:
Caracteres de sustancia revisados:
Diferencia real frente a otra pieza:
Revisión humana y resultado:
```

Si el cambio es una actualización, también se registra: edición anterior, dato cambiado, motivo, fecha, destinos corregidos y estado de cada espejo. No se suma dos veces el mismo bloque solo porque aparezca en dos idiomas o redes.

## 9.5 Registro de aprobación

```text
Artefacto aceptado:
Criterio o decisión aceptada:
Alcance explícito (pieza, idioma, canal, regla):
Elementos que NO se generalizan:
¿El dueño pidió aplicar esto a otros casos?:
Dominio y excepciones, si la respuesta anterior es sí:
Fecha/evidencia del mensaje:
```

Un «sí» a «¿se aprueba esta pieza?» llena solo los dos primeros campos y el alcance de esa pieza. No se inventa una preferencia de estilo global.

## 9.6 Registro de falla y contraparche

```text
Código/familia:
Síntoma observado:
Evidencia (archivo, línea, salida, fuente):
Causa comprobada / desconocida:
Impacto:
Contraparche aplicado:
Prueba que debe fallar:
Prueba que debe pasar:
Resultado real de ambas:
Estado (ACTIVA / CONTRAPARCHADA / OBSERVADA / RETIRADA):
Alcance y versión:
```

La entrada se considera contraparcheada solo cuando se corre la prueba que debe fallar y la que debe pasar; no basta con escribir una solución probable.

## 9.7 Glosario sin dolor

- **Maestro:** el archivo editorial fuente de un idioma. Las redes no crean otros maestros.
- **Despliegue:** cómo se muestra o se parte un maestro en una red sin alterar su evidencia.
- **Casa canónica:** la ubicación que el propio proyecto reconoce como oficial. Un espejo puede ayudar a acceder, pero no recibe automáticamente sus cifras.
- **Corte:** fecha/hora a la que se midió un dato que cambia.
- **Afirmación:** frase verificable sobre el mundo, un proyecto, una persona o un plazo.
- **Evidencia:** contenido abierto que sostiene una afirmación; un enlace solo no dice qué demuestra.
- **Conteo bruto:** número mecánico de caracteres del archivo.
- **Sustancia:** explicación, evidencia, comparación, riesgo o paso que cambia lo que el lector entiende o decide; no equivale a volumen.
- **Aprobación local:** aceptación de un artefacto con alcance concreto, sin generalización automática.
- **Convergencia:** deriva en la que respuestas distintas terminan repitiendo la misma forma por reutilizar una aprobación o plantilla.
- **Cadáver / bomba de tiempo:** categorías de exclusión del catálogo; no son atajos para completar una lista.
- **Parcial:** entrega que cumple solo una parte del alcance y nombra claramente lo que falta.

## 9.8 Lecciones vivas

Las lecciones del dueño se guardan con su fecha y alcance en §1.2 y en el registro de evolución. La síntesis editorial no sustituye una cita que deba permanecer textual. Una lección nueva se evalúa por su efecto en reglas concretas; si cambia una compuerta, se actualizan el manual, la prueba y el registro de versión juntos.

## 9.9 Matriz de cobertura: prueba de cada unidad normativa

Esta matriz hace visible el control de aceptación de las 70 subsecciones numeradas de las Partes 0–X. Cada fila usa una sección como unidad de revisión: el criterio, el caso que pasa, el que falla y la consecuencia deben cubrir sus reglas materiales, no solo su título. Los ejemplos ilustran la prueba; no se copian en una publicación. La prueba automática de §4.6 verifica cobertura y campos, no la correspondencia semántica: una persona debe comparar cada regla incluida en la sección con su fila. Si una regla queda sin criterio observable o sin consecuencia, la sección no pasa y se amplía la matriz. Si cambia la norma, también se corrige su fila. Una celda vacía o estructuralmente completa no se interpreta por sí sola como cumplimiento.

| ID | Criterio observable | ✅ Caso que pasa | ❌ Caso que falla | Consecuencia |
|---|---|---|---|---|
| 0.1 | Una regla conduce a una acción y una compuerta. | Los cuatro pilares tienen comprobaciones. | Solo se declara que la casa «valora» el rigor. | Añadir prueba o retirar la regla decorativa. |
| 0.2 | Cada regla previene un daño reconocible. | Se vincula un riesgo de dato falso con fuente y fecha. | Un principio no identifica a quién protege ni de qué. | Reescribir el propósito antes de exigirlo. |
| 0.3 | La respuesta ayuda a decidir y evita una pérdida concreta. | «Compara estas dos vías y evita descargar de una fuente sin dueño». | Solo se enumera qué es una app. | No publicar hasta contestar ambas mitades. |
| 0.4 | La confianza no se sustituye por volumen; la escala y los perfiles declarados no se presentan como medición sin fuente y corte. | El brief conserva literalmente «1,358M», más de 200 cuentas y edades 30–40 como declaraciones del dueño, sin atribuirles medición independiente. | «Alcanzamos 1.358.000 personas hoy» sin aclarar la notación ni abrir una fuente fechada. | No reinterpretar ni publicar la cifra como medida hasta aclarar unidad, fuente y fecha; revisar también el incentivo de volumen. |
| 0.5 | Verificación, trazabilidad, legibilidad y honestidad quedan observables. | Una ficha abre fuente, registra fecha, explica y declara límite. | Una de las cuatro patas no tiene prueba. | Bloquear esa ficha hasta completar el pilar. |
| 0.6 | Las puertas G0–G7 se ejecutan en orden con salidas. | Hay corte, entorno, alcance, evidencia, diseño, texto, auditoría y estado. | El operador edita antes de revisar la fuente y el archivo. | Volver a la puerta omitida; no declarar listo. |
| 0.7 | La aprobación conserva su alcance y no generaliza sola. | «Pieza 01 ES» se registra como aceptación local. | Su gancho pasa a todas las piezas por inercia. | Retirar la generalización; volver a diseñar el caso nuevo. |
| 1.1 | La doctrina interna conserva el nombre indicado; el crédito público usa el handle y Arena AI; desacuerdos y elogios no sustituyen evidencia. | Norma interna con Alexis Placencia; pieza pública con Alex17273747576777 y Arena AI, y una corrección respaldada por fuente. | Se expone el nombre interno en público o se acepta un dato solo para complacer. | Corregir identidad y crédito; reabrir la evidencia y declarar el desacuerdo antes de entregar. |
| 1.2 | El número de lecciones coteja con la fuente canónica y cada entrada conservada tiene alcance/efecto práctico. | Las 18 entradas coinciden con el corpus fechado; la lección de lenguaje claro cambia una explicación técnica. | La tabla visible tiene 15 entradas mientras el manifiesto afirma 18, sin fuente para cotejar las tres restantes. | No declarar esta sección íntegra; pedir el corpus o confirmación del dueño y reconciliar el conteo antes de aceptar el manual. |
| 1.3 | Calidez y directividad se ven en el trato y el contenido. | El párrafo dice qué funciona y qué límite tiene. | El texto parece un anuncio y omite condiciones. | Reescribir voz y revisar llamadas a la acción. |
| 1.4 | La comparación aclara; la evidencia permanece independiente. | Se explica la analogía y luego se da el dato técnico. | La metáfora ocupa el lugar de la fuente. | Quitar o precisar la metáfora y volver a verificar. |
| 1.5 | La disposición ayuda a localizar una idea por párrafo. | Subtítulos, enlaces y respiros separan funciones distintas. | Un bloque mezcla cinco ideas y un enlace oculto. | Dividir y volver a leer en pantalla pequeña. |
| 1.6 | Frases y párrafos se entienden al leer en voz alta. | Una oración larga se separa en dos sin perder causalidad. | El operador tropieza o se queda sin aire en la misma frase. | Reescribir antes de auditar longitud total. |
| 1.7 | Una pieza pública no contiene fórmulas de la lista negra. | La opinión se convierte en criterio medible y fechado. | Una fórmula vetada aparece incluso dentro de una cita pública. | ROJO: retirar y volver a correr modo público. |
| 1.8 | Firma exacta, remate específico y créditos finales respetan el orden. | Firma intacta, remate propio y Créditos como última sección. | Firma alterada o nota añadida después de Créditos. | Reordenar el cierre y verificar la última línea. |
| 1.9 | El meme es propio de la pieza, ocupa dos líneas (tres como máximo), no humilla ni convierte un riesgo serio en chiste. | Dos líneas nuevas resumen la lección concreta sin burlarse del lector ni rebajar una advertencia. | Se repite el mismo meme o la broma trivializa una falla de seguridad. | Retirar y rehacer; volver a comparar con la lista de memes y leer el cierre en contexto. |
| 1.10 | La actitud se traduce en acciones: utilidad y opinión rotulada, error corregido con fecha, crítica examinada, límites declarados y ninguna publicación por prisa. | Una crítica concreta se contrasta con la fuente y, si procede, corrige pieza y registro; el elogio no detiene la revisión. | Se publica sin verificar por prisa o se presenta una inferencia como hecho para sonar útil. | Detener, corregir o preguntar según la evidencia; documentar el límite antes de entregar. |
| 1.11 | Límites de capacidad, privacidad y promesas están a la vista. | Se indica que una fuente no abrió y qué queda pendiente. | Se afirma que habrá vigilancia futura sin mecanismo. | Corregir la promesa y retirar el dato no verificado. |
| 2.1 | Hay un maestro por idioma; ES agrupa Facebook·WhatsApp y mantiene Telegram aparte; EN agrupa Reddit·Discord; X/Twitter queda excluida. | 01-ES alimenta Facebook·WhatsApp como pareja y Telegram como destino separado; 01-EN sirve Reddit·Discord; no existe maestro X. | Se crean maestros por red, se mezcla Telegram en la pareja ES o se publica/deriva X sin nueva decisión. | Reconstruir el mapa desde los dos maestros y detener cualquier despliegue fuera del alcance. |
| 2.2 | La ficha de diseño identifica decisión, alcance, corte y aporte propio. | La pregunta del lector y la evidencia llevan a un mapa específico. | Se recicla una ficha vieja cambiando nombres. | Volver a G2–G4 y completar el caso real. |
| 2.3 | Cada función requerida aparece o tiene motivo para no aplicar. | El riesgo tiene lugar visible y un capítulo irrelevante se omite con razón. | La conclusión queda detrás de historia que no ayuda a decidir. | Reordenar; no añadir secciones para llenar. |
| 2.4 | Las afirmaciones de cada recurso tienen casa, dato, fecha y límite. | La licencia se copia del archivo oficial y se fecha el acceso. | Se atribuye al proyecto el número de un espejo. | Corregir la ficha y revisar las afirmaciones relacionadas. |
| 2.5 | Cada símbolo usado figura en la leyenda con un solo sentido. | La señal de condición siempre lleva el mismo significado. | La misma señal representa aprobación y riesgo sin clave. | Corregir leyenda y repasar todos sus usos. |
| 2.6 | El concepto se explica simple, preciso y con una consecuencia. | Una analogía va seguida de su límite técnico y una comprobación. | La analogía es la explicación completa. | Rehacer el pasaje antes de pasar a distribución. |
| 2.7 | Cada idioma supera 45.000 caracteres de sustancia, con cuenta por sección. | 45.001 caracteres útiles respaldados por función y evidencia. | El bruto cruza la cifra por créditos, enlaces o duplicados. | No pasa; ampliar con material pertinente o detener. |
| 2.8 | El canal cambia presentación, no fuente, riesgo ni veredicto. | Mensajes numerados conservan advertencias y referencia al maestro. | Un derivador borra límites para caber en un formato. | Descartar el derivado y reconstruir el plan. |
| 2.9 | ES y EN conservan hechos pero se revisan como ediciones propias. | El ejemplo idiomático cambia y la fuente/cifra se mantiene. | Una traducción literal se publica sin revisión EN. | El par queda parcial hasta pasar revisión independiente. |
| 2.10 | Notas preceden al cierre; meme, firma y remate respetan el orden; Créditos es la última sección e incluye autores/recursos, fuentes y los créditos canónicos. | Notas → meme → firma exacta → remate propio → créditos completos con Arena AI y Alex17273747576777 al final. | Se omite un creador identificable, cambia la firma o aparece texto después de Créditos. | Completar atribución, ordenar el cierre y volver a auditar antes de publicar. |
| 3.1 | Cada afirmación se clasifica permitido, condicional o prohibido con razón. | La condición de entrada se enlaza a evidencia. | El tono persuasivo sustituye la clasificación. | Detener y clasificar antes de editar estilo. |
| 3.2 | Las filas permitidas cumplen su prueba de fuente/fecha/alcance. | Un dato se enlaza a la página oficial abierta al corte. | Una opinión se presenta como observación del repositorio. | Retirar o etiquetar la frase según su naturaleza. |
| 3.3 | Toda condición material queda junto al estado y a la recomendación. | Un alpha se presenta con etapa y limitación. | Se recomienda como estable sin hablar de madurez. | Cambiar a observación o excluir del catálogo. |
| 3.4 | Ninguna prohibición de fondo se esquiva con sinónimos. | Se omite un recurso que no cumple filtros aunque aumente el lote. | Se añade un proyecto abandonado para llenar espacio. | Quitar y volver a revisar la selección. |
| 3.5 | El estado editorial se reconstruye desde filtros y evidencia. | La etiqueta «con condición» nombra la condición. | El estado se decide por popularidad. | Reasignar desde evidencia; no desde simpatía. |
| 3.6 | La revisión responde las preguntas de aceptación de cada afirmación. | Otra persona llega al mismo criterio al abrir las fuentes. | La conclusión depende de una fuente no citada. | Bloquear hasta restaurar trazabilidad. |
| 4.1 | Evidencia y forma tienen resultados separados. | Registro de fuentes y salida de vara se guardan en campos distintos. | Un verde mecánico se presenta como verificación factual. | Corregir el informe y repetir la comprobación de fuentes. |
| 4.2 | Cada afirmación decisiva tiene fuente primaria abierta, fecha, evidencia observada, alcance y estado; los asuntos sensibles llevan corroboración cuando aplica y no se guardan secretos. | La fila identifica la release oficial, el corte y qué confirma/no confirma; el registro omite tokens y datos privados. | Un extracto de búsqueda se presenta como fuente o se incluye una URL con credenciales. | Abrir la fuente y completar el registro, o marcar la afirmación pendiente; retirar secretos y revisar exposición. |
| 4.3 | Fecha, ruta/versión, permisos, herramientas y límites se revisan antes de editar; el reloj se contrasta si cambia el resultado y se usa la herramienta mínima segura. | Se registra una discrepancia entre sistema y fecha de referencia, se escoge una fuente fiable y se limita la edición a la ruta acordada. | Se toma la hora del host como fecha editorial pese a la discrepancia, o se edita sin comprobar el árbol. | Detener el corte, fijar referencia y entorno, y solo entonces reanudar el trabajo. |
| 4.4 | La vara se describe dentro de su capacidad real. | Se reporta «el contador pasa; las fuentes aún esperan revisión». | Se dice que el script certifica privacidad o seguridad. | Retirar la afirmación y añadir revisión humana. |
| 4.5 | Solo una cita normativa estrecha queda marcada y el modo público es estricto. | Un fragmento didáctico se delimita; la misma frase en pieza da ROJO. | Un bloque amplio oculta prosa o una marca queda sin pareja. | ROJO en norma o pieza; corregir alcance del marcador. |
| 4.6 | Cada cambio de vara tiene positivo, negativo y ambos modos. | Prueba buena pasa y el caso diseñado para fallar queda bloqueado. | Solo se ejecuta el caso verde. | Contramedida sigue ACTIVA; no se entrega la herramienta. |
| 4.7 | Una persona abre fuentes y relee el archivo después del linter. | La revisión detecta una licencia ambigua pese a VERDE mecánico. | Se publica sin abrir ninguna fuente porque el contador pasó. | Detener hasta completar revisión de evidencia. |
| 4.8 | Comando, salida y SHA identifican el archivo probado. | El registro nombra la ruta y el hash de la versión final. | Se adjunta un informe de una versión anterior. | Repetir pruebas y reemplazar el registro. |
| 5.1 | Una ambigüedad que cambia entrega, veredicto o riesgo se pregunta/resuelve; un mensaje y un evento verificable se registran por separado. | La respuesta de un issue se distingue de merge y CI; la fecha que afecta el corte se coteja con una fuente fiable. | Un comentario se toma como fusión o el reloj discordante como corte cierto. | Consultar la fuente del estado, resolver la duda material y declarar los supuestos restantes. |
| 5.2 | La pregunta identifica qué decisión está bloqueada. | Se pregunta por el idioma faltante si cambia el archivo. | Se manda una pregunta abierta que obliga a repetir el encargo. | Formular la duda específica; no adivinar mientras tanto. |
| 5.3 | El desempate respeta el orden de precedencia. | La privacidad prevalece sobre una preferencia de diseño. | Una convención antigua contradice una decisión ratificada. | Aplicar la regla superior y documentar el conflicto. |
| 6.1 | Una falla tiene evidencia, causa honesta y dos pruebas. | Hay un caso que reproduce y otro que demuestra el arreglo. | Se cierra por haber editado el código, sin prueba. | Mantener estado ACTIVA y no declarar el flujo listo. |
| 6.2 | Cada falla se clasifica por causa primaria y efecto. | Error de fecha se registra en veracidad aunque también afecte alcance. | Se etiqueta todo como «problema de redacción». | Reclasificar y aplicar la contramedida pertinente. |
| 6.3 | Cada código distingue incidente, brecha y riesgo preventivo; el contraparche y la prueba de cierre corresponden al estado real. | E07 figura como riesgo OBSERVADO; E08 se prueba sobre el archivo íntegro; E09 separa conteo bruto de sustancia. | Se llama incidente consumado a E07 o se declara E08 cerrado con una copia recortada. | Corregir clasificación y mantener abierto cualquier cierre sin evidencia reproducible. |
| 6.4 | Contraparche solo se cierra con pruebas registradas. | Se guardan salida positiva y negativa con alcance. | Se escribe «resuelto» sin salida del comando. | No cerrar; obtener evidencia o declarar límite. |
| 7.1 | Cada etapa deja evidencia antes de avanzar. | La ficha y registro de fuente están listos antes del borrador final. | Se redacta sin fijar alcance ni fecha. | Volver a la etapa ausente y actualizar checkpoint. |
| 7.2 | El lote respeta checkpoint y máximo de dos maestros por hito. | Un par ES/EN queda guardado antes de pasar al siguiente ID. | Se empiezan decenas de maestros sin persistir progreso. | Detener el lote y guardar estado verificable. |
| 7.3 | Una corrección anota dato, fecha, evidencia y destinos. | Se corrigen maestro y despliegues conectados. | El espejo conserva el error anterior sin nota. | Propagar corrección y documentar lo pendiente. |
| 7.4 | Se cuentan todos los IDs y ambos idiomas antes de cerrar. | El manifiesto coincide con 01 ES/EN y 02–70 pendientes. | Se llama completo al lote que solo contiene fusiones antiguas. | Mantener lote abierto y publicar conteo real. |
| 8.1 | Cada métrica tiene denominador, evidencia y respuesta. | Cobertura 2/4 se informa como 50 % con los cuatro IDs. | «Avance alto» sin contar qué falta. | Recalcular desde archivos y no redondear. |
| 8.2 | La deriva se detecta por lectura humana, no por generación de imitaciones. | Se fusionan dos textos si resuelven la misma pregunta. | Un medidor obliga a hacer versiones de estilo casi idénticas. | Retirar el mecanismo y revisar contenido por evidencia. |
| 8.3 | Una regla cambia por evidencia y alcance registrados. | Una queja concreta abre comprobación y cambio acotado. | Una aprobación aislada se vuelve instrucción universal. | Revertir generalización y registrar alcance local. |
| 8.4 | El informe copia cifras y pruebas observadas. | El total sale del contador y los avisos quedan listados. | El avance se calcula de memoria. | Recontar antes del checkpoint. |
| 9.1 | Los anexos guardan estado, no redactan contenido. | Un registro vacío se completa con datos del caso actual. | El operador copia un prompt estándar como si fuera la pieza. | Retirar prompt y volver a investigación/diseño. |
| 9.2 | El registro de pieza consigna dos rutas/estados, alcance, corte, fuentes, aporte, cuentas de sustancia, dos auditorías con SHA, créditos y siguiente paso. | ES y EN tienen rutas, fuentes, cuentas, salida y SHA propios; los campos no aplicables explican por qué. | EN o su cuenta/SHA queda vacío y el par se marca completo. | Marcar parcial, completar los campos o declarar el bloqueo; no aceptar un registro incompleto. |
| 9.3 | Cada fuente dice qué demuestra y qué deja abierto. | URL, fecha y fragmento apuntan a una afirmación concreta. | Una lista de enlaces no explica su uso. | Completar la relación o quitar la cita. |
| 9.4 | La cuenta separa aporte útil de aparato y repetición. | Una sección tiene decisión y evidencia propias. | El mismo párrafo se cuenta varias veces. | Recalcular y detener si cae bajo el umbral. |
| 9.5 | El registro identifica alcance de la aprobación. | Se acepta una pieza específica sin extensión tácita. | Se marca «preferencia global» sin pedido explícito. | Borrar generalización y registrar solo aceptación local. |
| 9.6 | El fallo tiene prueba que debe pasar y prueba que debe fallar. | El linter detecta la frase prohibida y acepta la cita normativa marcada. | Solo se prueba que el caso bueno pase. | Mantener falla abierta y añadir prueba negativa. |
| 9.7 | Una definición explica el término y su límite. | «Mirror» se explica como copia y se advierte que no fija casa oficial. | La definición repite el mismo término sin aclararlo. | Reescribir en lenguaje simple y comprobar con Feynman. |
| 9.8 | Cada lección tiene fecha, alcance y efecto en una regla. | La nueva pauta enlaza su decisión y prueba actualizada. | Se confía en memoria de conversación sin registro. | Registrar antes de modificar la norma. |
| 9.9 | Todas las filas del registro contienen los cinco campos. | Cada fila tiene criterio, ambos ejemplos y consecuencia. | Una celda está vacía o usa un ejemplo genérico. | Completarla antes de declarar aceptación final. |
| 10.1 | Cada compromiso se puede rastrear a una regla y resultado. | Una fuente abierta y una corrección fechada sostienen el compromiso. | Se ofrece un resultado que no se puede probar. | Informarlo como límite y no como promesa cumplida. |
| 10.2 | Los límites dicen qué no se garantiza ni se vigila. | Se informa el corte y dónde consultar la fuente vigente. | Se afirma seguimiento futuro sin mecanismo. | Retirar la promesa y ofrecer ruta comprobable al lector. |
| 10.3 | El cierre completo exige todas las condiciones y cero pendientes críticos. | Partes 0–X están aceptadas y la lista externa muestra lo restante. | Se llama completo al manual con una parte o prueba pendiente. | Reabrir estado parcial y enumerar lo que falta. |
| 10.4 | El lector puede reconstruir fuente y decisión sin leer la mente del operador. | Sigue enlace, fecha, criterio y límite hasta el veredicto. | La conclusión depende de razonamiento no explicado. | Añadir evidencia o suspender la conclusión. |

---

# PARTE X — PROMESAS, LÍMITES Y CIERRE

## 10.1 Lo que La Bandita sí se compromete a hacer

- Poner fecha y fuente en los hechos que cambian.
- Distinguir hecho, opinión, inferencia y duda.
- Explicar términos difíciles con Feynman y ejemplos pertinentes.
- Decir qué no pudo comprobarse.
- Reconocer y corregir errores a la vista.
- Atribuir el trabajo ajeno y proteger datos privados.
- Revisar cada idioma y destino dentro del alcance acordado.
- Usar las compuertas disponibles y dejar sus resultados identificables.

Cada compromiso tiene una regla o una comprobación en este manual. Si el resultado no se obtuvo, se informa como pendiente; no se convierte en una promesa de que se hará solo después.

## 10.2 Lo que no promete

La Bandita no promete que una app no tendrá vulnerabilidades, que un proyecto seguirá activo, que un dato seguirá vigente después del corte, que una plataforma conservará sus límites, que cada usuario tendrá la misma experiencia o que el equipo vigilará cambios futuros sin mecanismo acordado. Tampoco se presenta como servicio profesional ni como certificador de seguridad.

La diferencia entre un límite y una excusa es visible: el límite nombra qué no puede afirmarse y qué evidencia faltaría; la excusa esconde el hueco bajo un tono confiado. Se escribe el límite, se pregunta o se detiene la recomendación.

## 10.3 Condiciones para declarar v0.0.1 completa

El manual no se declara completo hasta cumplir todo lo siguiente:

- Partes 0–X escritas y coherentes entre sí.
- Cada regla con criterio observable, ejemplo que pasa, ejemplo que falla y consecuencia.
- Feynman integrado donde haya conceptos que enseñar.
- Cinco decisiones canónicas ratificadas reflejadas sin contradicción.
- Vara probada con casos positivos y negativos, incluidos documentos normativos y piezas públicas.
- Auditoría del archivo íntegro, no de una copia recortada.
- Lista visible de trabajo pendiente fuera del manual; nada parcial se presenta como total.

Al completar una parte, el manifiesto cambia su estado con la evidencia de la entrega. Un índice verde no vuelve verdes las partes no escritas.

## 10.4 La última regla

Una regla sirve cuando alguien puede seguirla sin leer la mente del operador; una pieza sirve cuando una persona puede reconstruir de dónde sale y qué decisión le ayuda a tomar. La forma puede cambiar con el caso. La honestidad, la evidencia, el respeto y la responsabilidad no se negocian.

La Bandita informa a partir de fuentes fechadas. Las estrellas adornan; las fechas mandan.
