# FALLAS Y CONTRAPARCHES — registro de la casa

*Corte: 2026-11-14 (UTC-4). Cada falla que tumbe trabajo se registra aquí con su
contraparche u habilidad solucionadora antes de proseguir. Regla del dueño:
«registra la falla y un contraparche/habilidad solucionador para ella y luego procede».*

Formato de entrada: síntoma → causa → contraparche/habilidad → estado.

---

## FALLA-001 · Turno caído por tiempo («The AI took too long to respond»)

- **Síntoma:** el turno murió a mitad de faena; el dueño vio el mensaje de plataforma
  `The AI took too long to respond. Please try again.` con id de petición
  `01a1da29-208d-70f4-b9a4-bb9d34ea4bb6` (2026-11-14). Todo lo que el turno llevaba
  en vuelo (sin guardar a fichero) se perdió con él.
- **Causa:** un solo turno intentó abarcar el paquete completo de publicaciones
  (decenas de piezas de 40-63 k caracteres) sin persistir estados intermedios.
  Sin checkpoint, un timeout deja al turno siguiente empezando de cero.
- **Contraparche / habilidad solucionadora:** `SKILL-TURNO-CON-CHECKPOINT`
  (ver abajo) + herramienta `edt/bin/checkpoint.sh`.
- **Estado:** CONTRAPARCHADA (herramienta y habilidad vivas en este mismo corte).

### SKILL-TURNO-CON-CHECKPOINT (habilidad solucionadora)

1. **Al abrir el turno:** leer `edt/docs/CHECKPOINT-ACTUAL.md` antes de tocar nada.
   El checkpoint dice tarea, hecho y siguiente paso; se retoma desde ahí, nunca de cero.
2. **En cada hito:** escribir el checkpoint con `bash edt/bin/checkpoint.sh escribir
   "<tarea>" "<hecho>" "<siguiente paso>"`. Un hito sin checkpoint es un hito que el
   próximo turno no verá.
3. **Tope duro por turno:** máx. 2 piezas maestras nuevas, o 1 generador + su corrida,
   o 1 reestructura de sistema. Lo que pase del tope va al checkpoint como siguiente paso.
   **Enmienda 3-bis (2026-11-14):** se permite turno combinado (reestructura + generador +
   hasta 2 maestras) **sólo si** cada hito se checkpointea y se espeja en `edt/` antes de
   empezar el siguiente. La protección no es el tope: es que nada quede sin persistir.
4. **Todo contenido nuevo se espeja en `edt/` (persistente) el mismo turno en que se
   crea.** Lo que sólo vive en `/var/tmp` (clones) muere en el próximo reinicio.
5. **Invocar herramientas por `bash <ruta>`**, no por bit de ejecución: los reinicios
   vuelven `100755` a `100644` y la herramienta parece rota sin estarlo.
6. Si el dueño reenvía cualquier texto tras un timeout, **no es instrucción nueva**:
   es la misma faena; se retoma del checkpoint.

---

## FALLA-002 · Detector G19 cazaba slugs pelados y dejaba pasar cultura pop

- **Síntoma:** la primera versión de `edt/bin/compuerta-canal-y-mision.py` dio 44 falsos
  positivos (las piezas citan repos como `owner/repo` sin URL) y luego dejó pasar
  `EntityData/Q193835.json` (Wikidata) como «repo».
- **Causa:** medir por forma (regex de slug) en vez de por vocabulario de medición.
- **Contraparche:** G19 vigente = señal por vocabulario (`★|estrellas`, URLs github,
  `repositorio|repos`, licencias SPDX) con `en_mision = ★>=3 or urls>=1 or repos>=3 or
  licencias>=2`; validado pieza por pieza contra señales crudas (45/45 coinciden).
  Lección: todo detector se valida contra un positivo y un negativo conocidos.
- **Estado:** CONTRAPARCHADA y validada (2026-11-14).

---

## FALLA-003 · El reinicio se llevó el clon y con él las EDICIONES no espejadas

- **Síntoma:** segundo reinicio del turno al siguiente: `/var/tmp/la-bandita-archivo`
  desapareció otra vez (2026-11-14, entre el turno de la pieza 01 y éste). El espejo
  conservaba los ficheros NUEVOS (maestras, derivados, LEEMEs, generador, bandas) pero
  **no las ediciones hechas dentro del clon**: la nota fechada del CORAZON y las carpetas
  vacías de la estructura. Tocarlas de nuevo costó trabajo repetido.
- **Causa:** la SKILL mandaba espejar «todo contenido nuevo», pero no las **ediciones a
  ficheros existentes** (CORAZON, bandas.json). Un espejo de ficheros nuevos no es un
  espejo de estado.
- **Contraparche / habilidad solucionadora:** `reaplicar-estructura.sh` en el espejo:
  reconstruye en un mando carpetas, LEEMEs, herramientas, bandas.json y la nota del
  CORAZON (idempotente por marcador). Regla añadida: **toda edición a un fichero del repo
  se guarda además como fichero propio en el espejo** (la nota del CORAZON vive ahora en
  `CORAZON-nota-reestructura-2026-11-14.md`) y bandas.json se edita en el espejo y se copia
  al clon, nunca al revés.
- **Estado:** CONTRAPARCHADA (script vivo y clon reaplicado en este corte).

## FALLA-005 · El visor de present_file llega roto al dueño

- **Síntoma:** el dueño ve disfuncional el archivo presentado con `present_file`
  («deja de presentar ese recacha disfuncional de mierda», 2026-11-15). El preview corre
  en un iframe sandboxed sin red: cualquier recurso externo o renderer exigente llega roto.
- **Causa:** no es del todo reparable desde aquí: el sandbox del visor es de la plataforma.
- **Contraparche / habilidad:** no usar `present_file` para entregables de trabajo; dar la
  ruta en el chat y dejar el fichero en el espejo persistente. El contenido manda, el
  visor no.
- **Estado:** CONTRAPARCHADA (regla de oficio desde este corte).

## FALLA-006 · Tokens pegados en el chat y permisos 0644 tras reinicios

- **Síntoma:** el dueño pegó cuatro tokens en texto plano en el mensaje (2026-11-15) y
  `tokens.txt` amaneció 0644 otra vez tras el reinicio.
- **Causa:** pegado manual en canal conversacional + el reinicio relaja permisos.
- **Contraparche:** los cuatro entraron al llavero `~/.cerox-keys/tokens.txt` como
  `GHP_A/GHP_B/GHP_C/GP2` con 0600; toda autenticación de git se hace con URL de un solo
  uso (`x-access-token:$T@…`), nunca incrustada en `.git/config` (C13). Pendiente del
  dueño: **rotar los tokens pegados en el chat**, que ya quedaron expuestos en el historial.
- **Estado:** CERRADA POR DECISIÓN DEL DUEÑO (2026-11-15): las llaves NO se revocan; siguen vivas a largo plazo y el riesgo de exposición en el historial del chat queda aceptado por el dueño. Siguen las reglas de manejo: llavero 0600, URL de un solo uso, nunca imprimir ni citar las llaves.

---

## FALLA-007 · La salida sintética de la autoprueba se leía como aviso real (2026-11-15)

- **Síntoma:** `make verificar` de la-bandita imprimía «⚠ rutas vivas rotas:
  README.md:1 · cita a carpeta-vieja/» sin que el README real citara nada de eso;
  la nota de «aviso abierto» vivió dos turnos como si fuera deuda verdadera.
- **Causa:** `tools/autoprueba.py` hace eco de las primeras líneas de cada compuerta
  corriendo contra su ÁRBOL FALSO sin etiquetar el origen; el README sintético cita
  `carpeta-vieja/` en la línea 1 a propósito (para probar que la compuerta detecta).
- **Contraparche:** eco etiquetado («salida del árbol sintético — no es la casa») y
  líneas prefijadas con `|`; verificado en la corrida real (el aviso ahora se lee como
  lo que es). Regla: antes de cazar un aviso, comprobar de qué boca sale.
- **Estado:** CONTRAPARCHADA (commit a05ec2e6, empujado a main).

## FALLA-008 · `exit 0` dentro de una regla awk cae al END y voltea el veredicto (2026-11-15)

- **Síntoma:** una comprobación por lotes («¿está sellado este archivo?») declaró NO
  sellados a todos, incluido README.md, que el grep directo sí encontraba sellado.
- **Causa:** `awk '$1==p{exit 0} END{exit 1}'` — en awk, `exit` salta al bloque END y
  el `exit 1` del END pisa el estado de la regla.
- **Contraparche:** bandera en vez de exit directo (`$1==p{f=1} END{exit !f}`) o
  `grep -q "^ruta<TAB>"`. Regla: desconfiar de todo `exit` dentro de regla si hay END.
- **Estado:** CONTRAPARCHADA (misma corrida; sellado real confirmado con grep exacto).

---

## Plantilla de entrada nueva

```
## FALLA-NNN · <título>
- **Síntoma:** …
- **Causa:** …
- **Contraparche / habilidad solucionadora:** …
- **Estado:** ACTIVA | CONTRAPARCHADA
```
