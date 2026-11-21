# Revisión de reglas y formato — La Bandita

**Fecha de referencia de plataforma:** 2026-11-10, America/Santo_Domingo. No se atribuye a esta fecha el estado histórico de servicios remotos observado con relojes discordantes.

## Alcance real de la lectura

El chat anterior no está íntegro: parte llega condensada. Se preguntó por la fuente y el usuario eligió trabajar con lo conservado y señalar huecos. No se afirma una relectura de mensajes ausentes ni que se haya recuperado toda la doctrina.

Leídos completos en esta continuación:
- `proyectos/la-bandita/manual-v0.0.1/MANUAL-v0.0.1.md`, desde el inicio hasta la última regla, incluidas sus 70 filas de §9.9 (lectura secuencial por rangos, no solo títulos ni resúmenes).
- `proyectos/la-bandita/manual-v0.0.1/MANIFIESTO-DE-EVOLUCION-v0.0.1.md`, completo.
- Índice histórico de reglas de la reestructura por idiomas, checkpoint y registro de revisión factual/editorial existente.
- Implementación de vara y guarda; las pruebas de vara, guarda y cobertura relevantes.

Se hizo una búsqueda textual en los Markdown/TXT conservados de EDT, excluyendo metadata Git y el overlay de atestaciones, para localizar referencias a la nómina de lecciones. Los resultados remiten a la discrepancia ya documentada; no se recuperó una lista canónica íntegra. Una búsqueda sin hallazgo no demuestra inexistencia.

## Cambios concretos

1. **Polaridad de §3.6 y su fila §9.9:** la pregunta 5 indaga influencia indebida; su respuesta problemática es «sí», no «no». La matriz decía bloquear «no» en 1–5 y el cuerpo omitía la consecuencia de 5. Ahora coinciden: «no» en 1–4 detiene; «sí» en 5 exige retirar la influencia y repetir; «sí» en 6 exige recorte/medición.
2. **Ficha manual/manifiesto:** se explicitan descripción atribuida o ausencia, diferencia de empuje/release y estrellas solo con fuente canónica/pertinencia. No se fuerza cifra cuando no aplica ni se acepta una métrica de espejo.
3. **Cierre público comprobable:** firma literal con punto y línea propia; meme contiguo de 2–3 líneas; remate de 1–3; sección Créditos/Credits final; Arena AI antes del crédito final del dueño. Diez casos positivos/negativos. No se simula comprobar originalidad, totalidad de autores, atribución semántica ni renderizado del destino.
4. **Persistencia:** se aclara que `git ls-files` solo prueba seguimiento local; no demuestra commit/push. La persistencia remota exige comprobación independiente. Se elimina del comentario de guarda esa sobreafirmación.
5. **Pruebas aisladas:** dos tests que se esperaban verdes fallaron porque medían todo el workspace y este supera 50.000.000 bytes. Se corrigió el aislamiento con raíz temporal y se añadió un caso de exceso de presupuesto que debe bloquear. El presupuesto y raíz reales de producción NO se relajaron.
6. **Precedencia y actualización:** el manifiesto reconoce el cotejo 70/70 ya documentado y el trabajo en rama indicado por el checkpoint, en vez de imponer la antigua publicación directa en main. Las decisiones canónicas no se cambian.
7. **Guía completa de aplicación:** `FORMATO-Y-CONTROL-DE-PUBLICACIONES.md` reúne alcance ES/EN, funciones del cuerpo, fuente/ficha, voz, tamaño/sustancia, despliegue, cierre, estados, controles, presupuesto y bloqueos, con referencia al manual íntegro. No es plantilla ni generador de contenido.

## Evidencia ejecutada

- Suite editorial ampliada: **25/25** (8 originales de vara + 2 estructurales de cobertura + 10 de cierre + 5 de guarda).
- `make prueba`: **TODO BIEN**.
- Vara `--modo-norma`: manual, manifiesto y guía dan **VERDE mecánico**. No equivale a aceptación de contenido o integridad de lecciones.
- Pieza 01 ES sin editar: ahora da **ROJO**, por firma/cierre no conforme. Antes el linter no detenía este defecto; el cambio demuestra detección sobre un caso existente, no corrección de la pieza.
- `git diff --check`: sin errores sobre los cambios revisados; las diferencias locales de permisos ajenas siguen intactas y fuera de la publicación.
- Medición real de guarda en esta continuación: **73.092.630 bytes**, anterior a guardar este informe; supera su límite histórico **50.000.000 bytes**. No se convierte el verde de fixtures en aprobación de producción. El workspace permanece bajo la cuota de snapshot de plataforma, un presupuesto diferente.

## Pendientes que impiden declarar todo terminado

- Lista auténtica de lecciones: 15 visibles/18 declaradas; no inventar tres ni reemplazar con la candidata de 17 mencionada por el checkpoint. Trabajar con lo conservado no ratifica un cambio de esa cifra.
- Presupuesto editorial de 50.000.000 bytes: reducir almacenamiento real o acordar expresamente su revisión; no aumentar el límite para obtener un verde.
- Pieza 01: cierre, cronología/corte, verificación individual de afirmaciones, datos de candidatos y cuenta de sustancia. Su lectura crítica existe, no su aceptación factual.
- Lote 01–70 ES/EN: no se ha rehecho ni aceptado. Fusiones antiguas y piloto son referencia, no pares finales.
- Destinos: no se hicieron publicaciones de prueba ni se verificaron límites vivos de cada red en este trabajo normativo.

No se reinició una auditoría global de GitHub ni se publicaron piezas en redes. Solo se respalda el progreso normativo/técnico en la rama revisable. El archivo de publicaciones históricas no se modifica ni se resella.
