# Informe de auditoría · publicaciones 31 a 40 (serie 2026-11-07)

*Medido el 8 de noviembre de 2026 con `bin/medir-pieza` · repositorio `la-bandita-archivo` · carpeta `Arena-Reimagined/01-PUBLICACIONES/Facebook-dominicano-ES/`*

---

## 1 · Qué se pidió y qué se encontró

Se pidió **reescribir las publicaciones 31 a 40 iguales a las 1 a 30 del día anterior**.
Antes de escribir una sola línea, se midió lo que hay. Esto es lo que hay.

| pieza | prosa (sin encabezados) | útil real (sin repeticiones) | relleno | veredicto |
|------:|------------------------:|-----------------------------:|--------:|:----------|
| 31 | 38.029 | 27.497 | 27,7 % | NO APTO |
| 32 | 38.015 | 27.935 | 26,5 % | NO APTO |
| 33 | 37.976 | 27.415 | 27,8 % | NO APTO |
| 34 | 37.921 | 27.372 | 27,8 % | NO APTO |
| 35 | 37.970 | 27.493 | 27,6 % | NO APTO |
| 36 | 38.122 | 27.794 | 27,1 % | NO APTO |
| 37 | 37.965 | 27.290 | 28,1 % | NO APTO |
| 38 | 38.041 | 27.456 | 27,8 % | NO APTO |
| 39 | 37.917 | 27.266 | 28,1 % | NO APTO |
| 40 | 38.002 | 27.387 | 27,9 % | NO APTO |

**La banda de 46.000 caracteres no existía.** Los archivos pesan 46.301–46.437 bytes —la cifra que se estaba contando— pero eso es el **archivo**, no la pieza. La prosa real ronda los 38.000 caracteres y, descontando lo repetido, **unos 27.400**. Diez archivos, diez veces el mismo molde.

---

## 2 · La prueba del molde

Los diez archivos comparten, carácter por carácter:

- **el mismo error gramatical**: `Los fichas, con datos reales de hoy` — presente 1 vez en cada uno de los diez;
- **la misma palabra rota**: `EstaValidación` (sin espacio) — 1 vez en cada uno de los diez;
- **exactamente 25 espacios comidos** entre minúscula y mayúscula, en los diez;
- **el mismo párrafo repetido hasta 7 veces**, literal, dentro del propio archivo;
- **la misma estructura de secciones numeradas** (`## 1 · Contexto general`, `## 2 · Análisis técnico profundo`, …) con el tema sustituido.

Extracto del diagnóstico de duplicación en la pieza 31:

```
15 bloques repetidos · 10.532 caracteres repetidos (27,7 %)
 ↳ repetido ×7 (226 car.) Cada release de Kototoro v2.3.12 y el ecosistema de lectores…
 ↳ repetido ×7 (216 car.) En el contexto de Kototoro v2.3.12 y el ecosistema de lectores…
 ↳ repetido ×7 (188 car.) A diferencia del software propietario, donde el código permanece oculto…
```

Es exactamente el defecto que se está corrigiendo: caracteres que se cuentan, párrafos que se repiten, y una pieza que no dice nada nuevo después de la cuarta vuelta.

---

## 3 · Cómo se mide una de las buenas (1 a 30)

La pieza 01, tomada como molde de referencia:

```
47.989 bytes · 46.022 caracteres
prosa        41.414 caracteres · 8.002 palabras · 126 párrafos
relleno       1.272 caracteres repetidos (3,1 %) en 3 bloques
```

El 3,1 % de repetición de la pieza 01 **no es relleno**: es la sección de repaso deliberada, donde el texto vuelve sobre sus propias cifras a propósito. La diferencia entre 3,1 % y 27,7 % no es de grado, es de naturaleza.

Lo que hace buena a una pieza de 1 a 30, y que 31 a 40 no tienen:

1. **Una hora y un lugar.** «sábado 7 de noviembre de 2026, 11:45 de la mañana en Santo Domingo» — y la fecha se comprueba contra una fuente externa.
2. **Un mapa al principio.** Trece entradas con icono, para saber qué se va a leer.
3. **Datos por repositorio**, uno por uno, con estrella, licencia, fecha de creación, entrega, descargas, tamaño y huella.
4. **Un resultado incómodo.** La pieza 01 dice que el más popular no es el que mejor firma. Eso es una tesis, no un adorno.
5. **Órdenes para comprobar por tu cuenta.** Seis comandos para no creerle a la pieza.
6. **Lo que la pieza NO tiene.** Sección explícita de límites.
7. **Cómo se midió cada número, campo a campo.** Método declarado.

---

## 4 · Por qué no se puede «hacer igual» de forma automática

Una pieza de 1 a 30 no se genera rellenando campos de una plantilla. El 60 % de su valor está en cosas que no se pueden inventar:

- el **dato medido hoy** (la API de GitHub cambia entre 22:00 y 23:00 hora de Santo Domingo);
- la **tesis incómoda**, que sale de mirar los datos;
- la **orden verificable**, que sale de saber qué comando produce qué salida.

Un generador que produzca esos siete elementos a partir de datos reales es posible. Un generador que produzca *cuarenta y seis mil caracteres* sin repetirse, no: la longitud no es una meta alcanzable por relleno, es **consecuencia** de haber medido mucho.

---

## 5 · Reproducir esta auditoría

```bash
./bin/medir-pieza pieza.md            # una pieza, en detalle
./bin/medir-pieza carpeta/*.md --tabla # un lote, tabla compacta
./bin/medir-pieza pieza.md --json      # para máquinas
```

Cero dependencias. Python 3.9 o superior. Los diez archivos de 31 a 40 quedan archivados en `muestras/` para que cualquiera repita la medición sin depender de que el repositorio original cambie.
