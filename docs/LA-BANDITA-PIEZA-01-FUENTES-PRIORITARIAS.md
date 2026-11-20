# Pieza 01 ES — comprobaciones prioritarias, no cierre

**Estado:** evidencia parcial para preparar la corrección; la pieza original permanece sin editar y no es publicable. Referencia temporal de plataforma: 2026-11-10, Santo Domingo. Un sitio vivo puede cambiar; no adjudicar al 10-nov contenido con fecha posterior ni trasladar una comprobación de disponibilidad a una comprobación de cada afirmación.

## F01 · Compilación reproducible y F-Droid

- **Pieza afirma:** todas las aplicaciones publicadas en F-Droid deben reconstruirse idénticas; si no coinciden, no se publican.
- **Fuente primaria:** [F-Droid FAQ para desarrolladores](https://f-droid.org/docs/FAQ_-_App_Developers/), sección «Are reproducible builds required?»: dice que no son obligatorias. Explica también que las APK no configuradas para reproducibilidad son firmadas con claves de F-Droid y que APK firmadas por el desarrollador pueden incluirse tras verificar la reproducción.
- **Fuente fechada complementaria:** [F-Droid, 15-ene-2023](https://f-droid.org/2023/01/15/towards-a-reproducible-fdroid.html), sobre firma propia de F-Droid y avance gradual de compilaciones reproducibles.
- **Dictamen:** la afirmación universal es falsa frente a la documentación. Sustituir por la distinción entre compilación por repositorio, verificación de reproducción cuando se aplica y firma de cada APK. No decir que código abierto, coincidencia de compilación o firma prueban ausencia de vulnerabilidades.

## F02 · Firma y continuidad de actualización

- **Pieza afirma:** el sello de firma demuestra sin matices quién envió la APK y ausencia de cambios; las tiendas serias «firman todo».
- **Fuente primaria:** [F-Droid FAQ](https://f-droid.org/docs/FAQ_-_App_Developers/), apartado «What about signing?», explica que el APK de F-Droid puede tener otra firma respecto a la versión distribuida por el desarrollador y la importancia de la firma para actualización.
- **Dictamen:** la firma permite verificar integridad y continuidad respecto a una clave confiable, pero un certificado por sí solo no autentica una identidad real ni garantiza inocuidad. La rotación autorizada puede ser una excepción a exigir exactamente la misma clave; comparar el certificado con una referencia autenticada y la política aplicable. No aconsejar desinstalar sin advertir pérdida de datos y opciones de respaldo verificadas.

## F03 · Alcance del análisis de Exodus

- **Fuente primaria:** [Exodus, FAQ](https://exodus-privacy.eu.org/en/page/faq/): detección estática de firmas conocidas; presencia no demuestra actividad; lista no es exhaustiva. [Explicación del análisis, 17-ago-2018](https://exodus-privacy.eu.org/en/post/exodus_static_analysis/) describe el cotejo de nombres de clases contra firmas.
- **Dictamen:** un informe identifica indicios sobre una versión concreta, no demuestra ausencia de rastreo o que un SDK encontrado esté activo. No extrapolar la APK analizada a todas las versiones o tiendas.

## F04 · Calendario de verificación Android: todavía sin cierre

- La documentación de Google encontrada es dinámica y presenta textos y fechas distintas, incluso material del 19-nov o posterior al corte de plataforma. **No usar su estado vivo como prueba de qué política estaba vigente el 10-nov.** Fijar captura/versión archivada anterior al corte, comparar ámbitos (regiones, dispositivos certificados, tiendas, excepciones) y distinguir anuncio de despliegue efectivo.
- La pieza usa el 19-nov como «hoy»: fecha incompatible con el corte de plataforma y, por tanto, no validada. No cambiar esa fecha por 10-nov sin rehacer cada comprobación dependiente.

## Próximo control requerido

Crear registro por afirmación y por ficha con fuente primaria, versión/corte, licencia, descripción atribuida, disponibilidad y estado; comprobar Aurora, microG, Obtainium, IzzyOnDroid y cualquier otro candidato sin suponer seguridad. Recontar sustancia humana por sección y rehacer el cierre. No se han realizado esas tareas completas; tres hallazgos comprobables no convierten la pieza en aceptada.
