# Pieza 11 — AniZen está vivo en v0.5.211: el espejo no es el repo y el issue se escribe bien o no se escribe

> **Textos fusionados de La Bandita · generado 2026-11-19**
> Fuente única: repositorio `la-bandita-archivo`, rama `main`. Cuerpos copiados **textuales**, sin reescritura.
> Español: Facebook·WhatsApp (cuerpo idéntico en ambas) + Telegram. · Inglés: Reddit + Discord.
> Trazabilidad (sha blob GitHub): ES-FB/WA `744c78317036` · ES-TG `fc5ce64489d9` · EN-Reddit `6567db65bd1b` · EN-Discord `c5f0717a9528`

---

## 🇪🇸 ESPAÑOL

### ▸ Facebook / WhatsApp *(mismo cuerpo en ambas plataformas)*

# Publicación 11 — AniZen está vivo en v0.5.211: el espejo no es el repo y el issue se escribe bien o no se escribe

**La Bandita · 15 de septiembre de 2026**

## 🗺️ Mapa de esta guía

├── ⚡ En una página
├── 🧬 El linaje: Anikku → AniZen
├── 🪞 Canónico vs espejo
├── 🚫 Qué NO es AniZen (y su propio README lo dice)
├── 📋 El arte del buen reporte de bug
├── 📵 El caso del diagnóstico viejo
├── ❓ Preguntas frecuentes
└── 🔗 Enlaces

## ⚡ En una página

```
AniZen — verificado HOY, 14 de septiembre
Repositorio:   github.com/salmanbappi/AniZen
Estado:        vivo · push del 13-sep
Versión:       v0.5.211 (publicada el 13-sep)
               la serie: 0.5.209 (23-ago) · 0.5.210 (5-sep)
               · 0.5.211 (13-sep) — ritmo de correcciones
               semanal
Estrellas:     182 · Apache-2.0
Paquete:       app.anizen
```

**Pulso de re-verificación (14-sep, noche #20):** abierto el repo de nuevo HOY: **v0.5.211 sigue siendo la última release** — no existe versión más nueva que la de arriba. El ritmo real de la serie reciente: cinco releases en tres semanas (0.5.207 → 0.5.211) — cadencia semanal: la estable no va a velocidad de tren (la beta es otra historia — bloque siguiente) — pero no está parada. Y ojo con las tiendas: bajo el paquete `app.anizen` **no hay ficha pública en Google Play** (comprobado HOY) — si un grupo te muestra una «versión vieja de hace meses», es un espejo, no la casa. El espejo no es el repo: por eso esta guía solo da el enlace del repo.

**La beta, fichada (14-sep, noche #21 — el enlace que trajo el dueño):** github.com/salmanbappi/anizen-preview — «Automated Preview Builds for AniZen». Aquí está el tren, y de verdad: **981 releases** publicadas en automático (la r4620 es del 13 de septiembre; ocho builds en fila entre el 12 y el 13; el commit inicial lo firmó «Gemini Automation» — el repo compila y publica solo). Y el caso del «casi 1000» quedó resuelto con cuenta: no eran reseñas — eran **releases**: 981 y contando. La estable (arriba) viaja semanal; la beta, varias veces al día. Beta para probar lo de mañana; estable para vivir lo de hoy.

AniZen es un cliente libre de anime para Android, activo esta misma semana. Esta guía hace dos cosas con su nombre: te da el estado real del proyecto (arriba, de hoy), y enseña la parte que casi nadie enseña — cómo se reporta un fallo para que el desarrollador pueda arreglarlo. Porque hay una diferencia entre quejarse en un grupo y abrir un reporte que sirve.

## 🧬 El linaje: Anikku → AniZen

Ninguna app nace de la nada, y AniZen tiene pedigrí documentado en sus propios repos:

```
komikku-app/anikku          ★1.025
   «Free and open source anime watcher for Android»
   La organización de Komikku (uno de los lectores
   manga más activos del ecosistema) mantiene este
   cliente de anime.
   Versión 0.2.0 publicada el 11 de septiembre —
   esta misma semana.

        │  alguien toma ese código

「Anikku Mod」
   una versión modificada, de otro autor

        │  commit del 28 de enero de 2026

AniZen
   el rebrand: «transform Anikku Mod into AniZen»,
   consta en el historial del repo. Mismo linaje
   declarado, casa y nombre propios.
```

¿Qué significa un rebrand, en criollo? El proyecto cambió de nombre y de casa — y lo declara. No es un clon (eso aparece de la nada con el nombre de otro); es una continuidad documentada: mismo código base evolucionado, autor identificado, historial público. La diferencia entre rebrand y clon es exactamente esa declaración con historial — la misma que distingue una mudanza de un allanamiento.

Para quien busca el cliente de anime de la organización Komikku directamente: ese es Anikku, y su 0.2.0 de este mes es su versión más fresca. Dos casas hermanas, dos ritmos: la original con su organización detrás, la rebautizada con su desarrollador individual empujando semanalmente.

## 🪞 Canónico vs espejo

```
github.com/salmanbappi/AniZen    ← LA CASA
   El repo canónico: aquí empuja el autor,
   aquí salen las versiones, aquí se reporta.

github.com/Gaijin81/anizen       ← EL ESPEJO
   ★0, copia sin vida propia. Existe; no manda.
```

La regla que salva medias horas de confusión: **el espejo no es el repo.** Al espejo no se le reportan bugs (nadie ahí los va a leer ni arreglar), y sus versiones pueden tener retraso respecto a la casa. ¿Cómo se sabe cuál es la casa? Por donde hay actividad real: releases firmadas, push reciente, autor que responde. Lo demás son fotocopias — algunas fieles, ninguna con taller.

## 🚫 Qué NO es AniZen (y su propio README lo dice)

La frase está en el propio proyecto, y conviene subrayarla porque el nombre circula en conversaciones donde se espera otra cosa:

**«AniZen does not have or fix any extensions»** — AniZen no trae ni arregla extensiones.

El cliente es la app. Las fuentes son otra capa — la de los parsers del ecosistema — y los problemas de reproducción de una fuente concreta no se reportan al repo de la app: ahí los cierran por fuera de alcance, con razón. Antes de abrir cualquier reporte, la primera pregunta es: ¿esto falla en la APP (se cierra, no guarda, la interfaz rompe) o en la FUENTE (no carga tal serie, tal servidor va lento)? La segunda no es problema de la app — por más que duela.

## 📋 El arte del buen reporte de bug

El template del repo pide, con checkboxes incluidos, exactamente lo que un desarrollador necesita para reproducir tu problema. La anatomía del reporte que sí sirve:

```
Título:        una línea, específica
               ✗ "La app no funciona"
               ✓ "Crash al abrir la pestaña Historial
                  con más de 500 entradas"

Pasos:         cómo llegar al fallo, numerado,
               desde app abierta
               1. Abro AniZen
               2. Voy a Historial
               3. ...

Esperaba:      qué debería pasar
Obtuve:        qué pasa en su lugar

Crash log:     si la app se cierra sola, el log
               que ella misma ofrece compartir
               (sin datos personales de por medio)

Versión:       el número EXACTO — a HOY 15-sep, v0.5.211.
               "La última" no es un número: mañana
               es otra. La pestaña Acerca de lo dice.

Teléfono:      modelo y versión de Android

Antes de enviar (los checkboxes del template):
   □ No es duplicado de un issue abierto
   □ El título es específico
   □ Estoy en la última versión
   □ Los números son específicos
```

Y la gramática del canal: los issues de este repo se escriben en inglés, cortos, sin emojis, UN problema por reporte. Los reportes vagos — «no funciona, arreglen» — mueren cerrados como «not planned», y el ejemplo de la casa es el issue #50: una plantilla de lo que NO es un reporte. No es maldad de mantenedor: es que un bug que no se puede reproducir, no se puede arreglar.

La regla de fondo de esta familia: el reporte lo escribe una persona, con sus manos y su cuenta — nunca se envía a nombre de nadie ni por nadie. Un reporte de bug es correo institucional de la era digital: con remitente, con datos, con modales.

## 📵 El caso del diagnóstico viejo

En los textos viejos de la comunidad existía un diagnóstico de un fallo de AniZen en un teléfono TECNO. Ese texto circuló incompleto, así que aquí no se reconstruye de memoria ni se inventan pasos — la regla es simple: lo que no se puede abrir y verificar, no se receta.

Lo que sí sirve, genérico y verificado por el sentido común del oficio, es la lista de chequeo antes de culpar a la app:

```
□ ¿La versión es la de hoy? (v0.5.211)
□ ¿El fallo se reproduce dos veces seguidas
  con los mismos pasos?
□ ¿Pasa también con otra fuente, u otra serie?
  (si solo falla una fuente: es la capa de
  fuentes, no la app)
□ ¿Hay espacio libre y memoria suficiente?
□ ¿El log del crash dice algo coherente?
```

Si el fallo pasa la lista — reproduce, de app, en versión vigente — entonces sí existe un reporte que escribir, con la anatomía de arriba. Si no pasa, se observa y se anota: la mitad de los «bugs» del mundo son condiciones, no errores.

Y el aviso de privacidad que nunca sobra: al reportar no viajan tu IMEI, tus capturas con cuenta ni tu número de teléfono. El desarrollador necesita el crash log y los pasos — no tu identidad.

## ❓ Preguntas frecuentes

**¿AniZen es seguro / confiable?**
Es un proyecto vivo, con licencia Apache-2.0, push de esta semana y versiones semanales. «Confiable» a largo plazo lo construye el historial: la casa está, el taller empuja, y el linaje (Anikku) es de una organización seria del ecosistema. Cada quien abre el repo antes de instalar — como con todo.

**¿AniZen o Anikku?**
Hermanos de código: Anikku es el de la organización Komikku (0.2.0 esta semana); AniZen el rebautizado con desarrollo individual semanal. Mismo linaje declarado, casas distintas. La que prefieras seguir — pero desde su casa.

**¿Por qué mi fuente favorita no carga? ¿Lo reporto a AniZen?**
No: la app no tiene ni arregla extensiones (su README lo dice tal cual). El fallo de una fuente es tema de la capa de fuentes de tu ecosistema.

**¿Dónde descargo la versión buena?**
De Releases en la casa: github.com/salmanbappi/AniZen/releases — hoy v0.5.211. Siéntete libre de re-abrirlo el día que instales: esa página es el único reloj que manda.

**¿El espejo de Gaijin81 sirve para algo?**
Para nada que la casa no haga mejor. No se reporta ahí, no se descarga de ahí, no se cita como fuente.

**¿Puedo pedir funciones nuevas por issue?**
Cada repo tiene su política para eso (los templates lo dicen). Lo universal: una petición por issue, con caso de uso concreto — «me gustaría X porque cuando hago Y no puedo Z» vale más que «agreguen X».

**¿Quién escribe el issue si un grupo entero tiene el mismo bug?**
El que lo sepa reproducir mejor. Los demás suman un «me pasa igual, con tal versión y tal teléfono» — dato, no ruido.

## 🔗 Enlaces

- AniZen (la casa): https://github.com/salmanbappi/AniZen · https://github.com/salmanbappi/AniZen/releases/latest
- AniZen beta (el tren diario): https://github.com/salmanbappi/anizen-preview
- Anikku (el linaje original): https://github.com/komikku-app/anikku
- El espejo (nombrado, no usado): https://github.com/Gaijin81/anizen

> La Bandita informa a partir de fuentes fechadas. El espejo no es el repo, y el reporte que sirve tiene números, pasos y modales.

---

**Nota de mudanza (15-sep):** guía pasada de la hornada del 14 a esta, con re-verificación contra las casas: re-verificado a HOY. Lo no mencionado queda constado a su día (14-sep). Acta completa: Registro #71.

**Pulso de mudanza (15-sep):** re-abierto el repo HOY: v0.5.211 sigue siendo la última estable (★182); la preview sigue soltando — su build r4622 es de HOY mismo. Lo dicho: el espejo no es el repo.

### ▸ Telegram *(adaptación de canal)*

📌 AniZen viva en v0.5.211 — el espejo no es el repo

- **AniZen** ★182 · v0.5.211 (13-sep) · github.com/salmanbappi/AniZen
- Preview: r4622 de HOY · github.com/salmanbappi/anizen-preview
- El espejo (Gaijin81/anizen) ★0: existe; NO manda

Linaje: desciende de Anikku (org Komikku ★1.032), va pa' la comunidad hispana. Su README lo dice: sin fuentes garantizadas, sin legalidad prometida — el cliente es tuyo, las fuentes las pones tú.

Bug bueno: versión exacta + pasos + captura limpia. El bug que no llega a la casa, no existe pa' la casa.
*Fuente: pieza 11 (15-sep) · verificado HOY, 15-sep-2026*
Lo completo: tema fijado del foro (Rethubs) y pieza 11 de la casa.
Proyecto entre panas, nada profesional: solo fechas y fuentes.

> —Bajé AniZen del primer enlace de Google. —¿Y cuál repo era? El nombre no manda: el dueño sí.

*La Bandita verifica antes de recomendar: las estrellas adornan; las fechas mandan.*

---

## 🇬🇧 INGLÉS / ENGLISH

### ▸ Reddit

# AniZen is alive on v0.5.211: the mirror is not the repo (a verification lesson)
**Reddit · ingles-US · fuente: pieza 11 (15-sep) · verificado: 15 de septiembre de 2026**

**TL;DR:** The lesson serves the whole ecosystem: the house rules, never the mirror. AniZen ★182 · v0.5.211 (Sep 13), preview r4622 from TODAY; the Gaijin81/anizen mirror has ★0 and doesn't rule.
## Tonight's data (Sep 15)

- **AniZen** — ★182 · **v0.5.211** (Sep 13) is still the latest stable · github.com/salmanbappi/AniZen
- A preview that doesn't rest: build **r4622 from TODAY** · github.com/salmanbappi/anizen-preview
- The mirror (Gaijin81/anizen) — ★0, no life of its own: it exists; it doesn't rule

## The lineage and what it is NOT

It descends from Anikku (komikku-app, ★1,032) — the org that proves its trade with Komikku and Anikku — and heads for the Spanish-speaking community. Its README says so: not official streaming, no guaranteed sources — the client is yours, the sources are the ones you add.

## The art of a good bug report

Exact version · steps to reproduce · screenshot without personal data · what you expected vs what happened. And the old-diagnosis case: an issue stayed "unsent" — the repo compiles by automation but the report never reached the house. **A bug that isn't at the house doesn't exist for the house.**
**House edit (Sep 15):** verified twice in one day: alive and pushing.

> —I downloaded AniZen from Google's first link.
> —And which repo was that? The name doesn't rule, boss: the owner does.
*La Bandita verifies before recommending: stars decorate; dates decide.*

### ▸ Discord

# AniZen is alive on v0.5.211 — the mirror is not the repo (Discord · en-US)
**Platform:** Discord · **Language:** US English · **Source:** piece 11 (Sep 15) · **Verified:** today, September 15, 2026

This listing's lesson serves the whole channel: **the mirror never rules — the house rules.**

**Tonight's data (Sep 15):**
- **AniZen** — ★182 · **v0.5.211** (Sep 13) is still the latest stable · github.com/salmanbappi/AniZen
- The preview doesn't rest: build r4622 from TODAY · github.com/salmanbappi/anizen-preview
- The mirror (Gaijin81/anizen) — ★0, no life of its own: it exists; it doesn't rule

**The lineage:** it descends from Anikku (komikku-app, ★1,032) — the organization that proves its trade with Komikku and Anikku. AniZen takes that base and heads for the Spanish-speaking community.

**What AniZen is NOT (its README says so):** not official streaming, doesn't guarantee sources, doesn't promise legality — like the whole ecosystem: the client is yours, the sources are the ones you add.

**The art of a good bug report (the week teaches):** exact version · steps to reproduce · screenshot without personal data · what you expected vs what happened. The bad issue gets ignored; the good one gets fixed.

**The case of the old diagnosis:** an issue from the past stayed "unsent" — the repo compiles and publishes by automation, but the user's report never reached the house. Moral: a bug that isn't at the house doesn't exist for the house.

The house meme:
> —I downloaded AniZen from Google's first link.
> —And which repo was that? The name doesn't rule, boss: the owner does.

*La Bandita verifies before recommending: stars decorate; dates decide.* ✅

---

> _Nota honesta:_ la versión **X / Twitter** nunca fue creada en el corpus original; queda anotada como pendiente
> por decisión del dueño (2026-11-19). Este archivo reúne únicamente plataformas realmente versionadas.
