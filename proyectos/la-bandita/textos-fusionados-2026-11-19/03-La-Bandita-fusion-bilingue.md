# Pieza 03 — Verificación de Desarrolladores: 15 días para el hito y el reloj hacia 2027

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `9eb5c82111df` · ES-TG `31f92da3dfbc` · EN-Reddit `a6c2eaad6f86` · EN-Discord `5836c8e1755e`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 03 — Verificación de Desarrolladores: 15 días para el hito y el reloj hacia 2027

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 📅 El cronograma completo
├── 🪪 Qué es la verificación (en las palabras de Google)
├── 🛒 Las dos consolas y el flujo de registro
├── 🏪 Las siete tiendas del 30 de septiembre
├── 🎓 Cuentas de distribución limitada: la puerta chica
├── 🛠️ El flujo avanzado (el de la carta de 24 horas)
├── 👤 A quién le toca y a quién no (aún)
├── 📜 La carta abierta: las tres objeciones
├── 📣 La campaña y su reloj
├── 📗 La lectura contraria: F-Droid
├── 📌 Correcciones que este tema ya sufrió
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

Google está instalando un censo de desarrolladores para Android. El programa se llama «verificación de desarrolladores de Android» y funciona así: para que una aplicación se instale en dispositivos Android certificados, su desarrollador tendrá que estar registrado y verificado — con identidad real, nombres de paquete declarados y claves de firma vinculadas.

Hoy es 15 de septiembre. Faltan **15 días** para el primer hito público: el 30 de septiembre, cuatro países y siete tiendas entran en el filtro. Si vives en República Dominicana — o en cualquier país fuera del piloto — tu fecha es otra: 2027, cuando el filtro alcance a todas las apps de dispositivos certificados.

Las voces están en dos bandos que esta guía cita por su nombre: Google, que lo vende como rendición de cuentas contra el malware; y F-Droid con la campaña Keep Android Open, que lo leen como un censo que rompe la distribución libre de aplicaciones. Lo que sí tiene todo el mundo: un reloj. La campaña mantiene un contador público: 110 días constados el 14-sep — el contador corre solo.

## 📅 El cronograma completo

```
Ago 2025        Google anuncia el programa.

29-sep-2025     F-Droid publica su análisis crítico:
                «el decreto de registro de desarrolladores».

Mar 2026        El proceso se abre a todos los desarrolladores
                (Play Console y la nueva Android Developer
                Console). Blog oficial leído en su página.

Jun 2026        Google publica «Building a safer ecosystem
                together»: confirma el arranque en 7 tiendas
                y 4 países, presenta APIs de automatización
                y repite el plan global de 2027.

Ago 2026        Las cuentas de distribución limitada quedan
                disponibles para todos.

30-sep-2026     PRIMER HITO: 4 países (Brasil, Indonesia,
                Singapur, Tailandia) · 7 tiendas · Android 7+
                en dispositivos certificados.

2027            Despliegue global: todas las apps en
                dispositivos certificados.
~Ene 2027       La campaña sitúa aquí el bloqueo efectivo
                y lo cuenta con reloj público: 110 días al corte del 14-sep.
```

Los tres documentos oficiales (hub del programa, guías y blogs) se abrieron hoy; sus fechas de actualización son de finales de agosto y principios de septiembre. El mapa se mueve: esta guía lleva la fecha de corte en el título por una razón.

## 🪪 Qué es la verificación (en las palabras de Google)

La definición oficial cabe en una frase: «la verificación de desarrolladores de Android vincula entidades del mundo real —personas y organizaciones— con sus aplicaciones de Android».

El marco de Google: establece responsabilidad (accountability). Desalienta a los actores maliciosos, hace más difícil que quien hizo daño repita bajo otro nombre, y le da al usuario más confianza sobre quién hay detrás de una app. La tarifa del registro se compara en la propia FAQ con la cuota histórica de 25 dólares de la tienda de Google.

La lectura contraria (F-Droid, Keep Android Open, firmantes de la carta): eso no es un escáner de malware — es un censo. No analiza archivos: analiza personas. Y pone el peso del registro sobre quien distribuye, no sobre quien distribuye mal. Ambas lecturas se citan completas más abajo; esta guía no elige bando por ti.

## 🛒 Las dos consolas y el flujo de registro

Hay dos puertas, según por dónde distribuyas:

- **Play Console** — si tus apps viven en la tienda de Google. El registro se integra con lo que ya existía.
- **Android Developer Console** — la consola nueva, para todo lo demás: tiendas alternativas, distribución directa, sideload organizado.

El flujo de la consola nueva, según su guía oficial (abierta hoy), en siete pasos:

```
1. Crear la cuenta
2. Elegir cómo distribuyes tus apps
3. Completar la verificación de identidad
   (los requisitos cambian según el tipo de cuenta)
4. Registrar los nombres de paquete de tus apps
5. Automatizar el flujo con las APIs nuevas
6. Resolver duplicados de nombre de paquete
   (cuando dos proyectos reclaman el mismo)
7. Revisión
```

Los puntos delicados que la documentación confirma: el registro exige declarar TODOS los nombres de paquete que distribuyes, y evidencia de que controlas las claves de firma. Es decir: no es un formulario — es un inventario completo de lo que has publicado.

## 🏪 Las siete tiendas del 30 de septiembre

El hito del 30 de septiembre no toca «todas las tiendas»: toca las participantes declaradas.

```
1.  Google Play
2.  Galaxy Store   (Samsung)
3.  GetApps        (Xiaomi)
4.  HONOR Store
5.  OPPO Store
6.  Palm Store
7.  V-Appstore     (vivo)
```

Cuatro países en el piloto: Brasil, Indonesia, Singapur y Tailandia. Dispositivos certificados con Android 7 o superior. Si tu app vive en esas tiendas y esos países, el 30 de septiembre necesita que su desarrollador esté verificado. Si vives fuera del piloto, tu calendario es el de 2027 — pero el proceso se puede adelantar, y Google lo recomienda.

Lo que NO cambia el 30 de septiembre: el sideload directo de un APK (instalar un archivo a mano), F-Droid y las tiendas alternativas fuera de la lista. Ese es el tema de 2027.

## 🎓 Cuentas de distribución limitada: la puerta chica

La novedad del mes, confirmada hoy en tres fuentes oficiales (la FAQ, la guía dedicada y el blog de junio):

```
Para quién:   estudiantes, docentes, aficionados,
              quien aprende
Qué permite:  registrar apps y compartirlas con hasta
              20 dispositivos — que el usuario final
              autoriza explícitamente
Qué pide:     ni identificación gubernamental, ni tarifa
Su guía trae: fechas clave, qué puede hacer la cuenta,
              costo, cómo funciona compartir, si es para
              ti, y qué necesitas para registrarte
```

Es una ventana real para el aula, el taller y el hobby. Con techo duro: veinte dispositivos no sostienen un proyecto comunitario ni una distribución abierta. Es la puerta para aprender, no la puerta para vivir.

## 🛠️ El flujo avanzado (el de la carta de 24 horas)

Para quien no puede o no quiere pasar por el registro completo, existe un flujo avanzado. Según la documentación de la campaña (verificada también la semana pasada), funciona así:

- Nueve pasos, descritos en la guía.
- Una espera de aproximadamente 24 horas.
- Corre a través de Play Services — del servicio de Google, no del sistema operativo abierto.

Ese último punto es el que más discusión genera: el camino alternativo pasa por el mismo componente propietario que el camino estándar. Si Play Services no está — teléfonos sin Google — el flujo no aplica.

La FAQ oficial mantiene su sección «Advanced flow» como vía reconocida.

## 👤 A quién le toca y a quién no (aún)

```
Tu situación                                  ¿Cambia el 30-sep?
Publicas en las 7 tiendas, país piloto        Sí: dev verificado
                                              o tu app no entra
Publicas en las 7 tiendas, fuera del piloto   Tu fecha es 2027
Instalas APK a mano (sideload)                No. Aún. Tu tema: 2027
Usas F-Droid                                  No. Aún. La campaña
                                              dice que su fecha de
                                              impacto no está publicada
Teléfono sin certificación de Google          Otro mundo: el filtro
                                              va sobre certificados
```

La frase que resume todo: quien distribuye dentro del mundo certificado, está dentro del censo — hoy en cuatro países, mañana en todos. Quien vive fuera de ese mundo, tiene un año más de ventana.

## 📜 La carta abierta: las tres objeciones

Keep Android Open organizó una carta abierta a Google (leída hoy en su página). Su estructura son tres bloques:

**1. Nuestras preocupaciones.** El registro con identidad convierte la distribución de software en un acto identificado frente a una corporación; el impacto cae sobre desarrolladores pequeños, proyectos anónimos por seguridad y comunidades fuera de los circuitos formales.

**2. Las medidas existentes bastan.** Play Protect ya escanea; las tiendas ya filtran; los mecanismos de seguridad del sistema ya existen. El censo no añade un escáner: añade un registro de personas.

**3. La petición.** Que Google retire la exigencia de registro con identidad como condición de distribución.

Las cifras que la propia carta muestra: 71 firmantes, 23 países. Entre los visibles: AdGuard, Aurora Store, BEUC, Brave, Calyx, CCC, Codeberg, F-Droid, FUTO, GrapheneOS, IzzyOnDroid, KDE, microG, Nextcloud, Obtainium, Tor, Vivaldi y la Fundación Karisma, entre otros. Aparecer en la lista no es recomendación de instalar nada — es el mapa de quién firmó.

## 📣 La campaña y su reloj

https://keepandroidopen.org

La campaña mantenía en portada su contador público: **110 días** (constado el 14-sep) — hacia lo que su FAQ llama el bloqueo, situándolo alrededor de enero de 2027. Su frase de portada: «Your phone is about to stop being yours».

Lo que la campaña documenta del registro estándar: tarifa, identificación gubernamental, evidencia de posesión de la clave de firma, y la declaración de todos los nombres de paquete. Su consigna — «Do not sign up» — es de la campaña; esta guía la cita, no la dicta.

Su FAQ también aclara la pregunta que más repite la comunidad: septiembre NO incluye a F-Droid; la fecha en que el filtro alcanza a F-Droid no está publicada. El contador de la campaña es la única cuenta regresiva pública que existe sobre 2027 — por eso esta guía la cita con su fecha.

## 📗 La lectura contraria: F-Droid

https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

El análisis de F-Droid (publicado el 29 de septiembre de 2025, abierto hoy) titula al programa «el decreto de registro de desarrolladores de Google» y lo desarma en cuatro secciones:

- **El movimiento para romper la distribución libre** — la tesis: sin identidad, no hay distribución; sin distribución, no hay software libre en Android.
- **El señuelo de la seguridad** — el malware ya se combate con análisis; el censo no analiza archivos, analiza autores.
- **El derecho a ejecutar** — tu teléfono, tu software: la línea de fondo que la carta defiende.
- **Lo que proponen** — alternativas que no pasen por el registro con identidad.

F-Droid mantiene además su banner «under threat» en todo su sitio, con la campaña activa. Para el ecosistema libre, este es EL tema del año.

## 📌 Correcciones que este tema ya sufrió

Este asunto corrige versiones anteriores de sí mismo. Historial de lo que se creyó y dejó de ser cierto:

```
Se creyó antes              Lo confirmado después
«El 30-sep bloquea APKs»    30-sep = 4 países, 7 tiendas.
                            El bloqueo amplio es 2027.
«Android 8+»                Android 7+.
«6 tiendas»                 7.
«Anunciado en nov-2025»     Agosto de 2025.
«El flujo avanzado tarda    Es de una sola vez:
24 h por cada APK»          9 pasos + una espera de ~24 h.
«Limited = sin ID y ya»     Sin ID, pero con perfil de pagos,
                            2FA y cuenta Google para operar.
«El blog de junio no se     Se leyó: confirma 7 tiendas,
puede leer»                 4 países, APIs y plan 2027.
```

La lección del tema: cada mes trae su corrección. Reabre las fuentes el día que decidas algo — la de arriba son de hoy.

## ❓ Preguntas frecuentes

**¿El 30 de septiembre me bloquea instalar APKs a mano?**
No. Ese hito toca las tiendas participantes en cuatro países. El sideload directo y F-Droid quedan fuera — por ahora. Tu reloj serio es 2027.

**¿Tengo que hacer algo HOY?**
Si vives en el piloto o publicas en esas tiendas: sí, verificar. Si no: no — pero conviene conocer el proceso antes de que sea tu turno.

**¿La verificación cuesta?**
El registro se compara en la FAQ con los 25 dólares de Play. Las cuentas de distribución limitada no pagan tarifa ni piden ID.

**¿Y si solo hago apps para mí?**
Veinte dispositivos es el mundo de las cuentas limitadas: sin ID, sin tarifa. Para un círculo íntimo, alcanza.

**¿Esto mata a F-Droid en septiembre?**
No — y no está publicado cuándo, si ocurre. Es la pregunta más repetida y la respuesta honesta es: nadie fuera de Google tiene esa fecha.

**¿Qué es eso de «dispositivos certificados»?**
Los que salen de fábrica con los servicios de Google. Un teléfono sin certificación vive fuera del alcance del filtro — con todo lo demás que eso implica.

**¿El contador de 110 días es oficial?**
Es de la campaña, no de Google. Su fecha — el bloqueo en torno a enero de 2027 — es su lectura del calendario. Google dice «2027» a secas. Dos relojes, dos voces.

**¿Dónde leo las fuentes sin la interpretación de nadie?**
En los enlaces de abajo: hub, guías, FAQ y blogs son de Google; la carta y la FAQ son de la campaña; el análisis, de F-Droid. Todo se abre hoy.

## 🔗 Enlaces

- Hub oficial: https://developer.android.com/developer-verification
- FAQ oficial: https://developer.android.com/developer-verification/guides/faq
- Distribución limitada: https://developer.android.com/developer-verification/guides/limited-distribution
- Consola nueva: https://developer.android.com/developer-verification/guides/android-developer-console
- Blog de marzo: https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html
- Blog de junio: https://android-developers.googleblog.com/2026/06/android-developer-verification.html
- Campaña: https://keepandroidopen.org · https://keepandroidopen.org/faq/ · https://keepandroidopen.org/open-letter
- F-Droid: https://f-droid.org/en/2025/09/29/google-developer-registration-decree.html

> La Bandita informa a partir de fuentes fechadas. El reloj corre; el que lee las fuentes a tiempo, elige a tiempo.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: reloj: faltan 15 días; contador 110 constado al 14. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

### ▸ Telegram *(adaptación de canal)*

📌 Verificación de devs de Google: faltan 15 días pa' el primer hito

30-sep: Brasil, Indonesia, Singapur y Tailandia — 7 tiendas con filtro. ~ene-2027: bloqueo en dispositivos certificados.

Registro con identificación oficial + pago + **llaves de firma entregadas**. Sin registro, tu APK no instala — ni por sideloading.

La carta abierta (71 firmantes, 23 países): llaves = identidad · punto único de control · riesgo pa' F-Droid y el sideloading.

¿Publicas APKs? Mira las fechas de tu país ANTES del 30-sep.
*Fuente: pieza 3 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 03 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —Es solo un formulario, ¿no? —Es un formulario que pide las llaves de tu casa.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# 15 days left for Google's developer verification milestone (Sep 30): what changes and who it touches
**Reddit · ingles-US · fuente: pieza 3 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** September 30: Brazil, Indonesia, Singapore and Thailand — 7 stores applying the verification filter. Registration with official ID, payment and signing keys handed over; without registration, the APK won't install on a certified device.
## The schedule

- **Sep 30, 2026:** pilot in 4 countries, 7 stores
- **~Jan 2027:** what the campaign places as the effective block on certified devices
- Keep Android Open clock: 110 days as of the Sep 14 cutoff (checked on the front page)

## What Google asks

Developer registration with official ID, payment and signing keys handed over. **The small door:** limited-distribution accounts for a small audience. The "advanced flow" mentioned in November: a 24-hour letter, zero public details to this day.

## The open letter's three objections (71 signatories, 23 countries)

1. Handing over signing keys = handing over the app's identity
2. A single corporate control point
3. The impact on F-Droid and old-school sideloading

The counter-reading (F-Droid, Keep Android Open): not security, control — Play Protect already scans.

**Does it touch you TODAY?** If you publish APKs: check your country's dates before Sep 30. If you only install: not yet, but save the thread.

**Method trick:** WHOIS, the domain's birth date and the APK's signature — bait is always in a hurry.
> —It's just a form, right?
> —It's a form that asks for the keys to your house.
*La Bandita verifies before recommending: stars decorate; dates decide.*

> 

### ▸ Discord

# Developer Verification — 15 days to the milestone (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 03 (Sep 15) · **Verified:** today, September 15, 2026

Today is September 15. **15 days left** to the first big one: on September 30, four countries and seven stores enter Google's verification filter. If you publish APKs — even your buddy's mod of a mod — this touches you.

**The schedule in short:**
- **Sep 30, 2026:** pilot in Brazil, Indonesia, Singapore and Thailand — 7 stores applying the filter
- **~Jan 2027:** what the campaign places as the effective block on certified devices
- **The campaign clock:** 110 days as of the Sep 14 cutoff (checked on the front page; the counter runs by itself)

**What it is (in Google's words):** developer registration with official ID, payment, and signing keys handed over. Without registration, your APK won't install on a certified device — not even by sideloading.

**The small door:** limited-distribution accounts for those publishing only to a tiny audience. And the "advanced flow" Google mentioned in November: a 24-hour letter, zero public details to this day.

**The three objections of the open letter (71 signatories, 23 countries):** handing over signing keys = handing over the app's identity · a single corporate control point · the impact on F-Droid and old-school sideloading. The counter-reading (F-Droid, Keep Android Open): it's not security, it's control — Play Protect already scans.

**Do you have to do anything TODAY?**
- Do you publish APKs for other people? → check the registration and your country's dates BEFORE Sep 30
- Do you only install? → not your turn yet; save this guide and follow the thread

**How to read a domain without opening it (the channel's trick):** check the WHOIS record, the domain's birth date and the APK's signature — bait is always in a hurry.

The house meme:
> —It's just a form, right?
> —It's a form that asks for the keys to your house.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
