# Parche retirado: `shinku-fase2-tope25-e-idioma.patch`

**Retirado el 2026-11-15 a las 17:27Z, antes de publicarlo como rama o PR.** Sigue siendo
`git apply --check`-limpio sobre `043ab7d8`; lo que está mal es su **semántica**, no su aplicabilidad.
Retirado también del issue ShinKu #32 (queda allí plegado y marcado «do not apply»).

Tres defectos, todos encontrados re-leyendo el árbol real antes de publicar:

1. **«Por pestaña» no es una unidad que ShinKu tenga.** `feed_saved_search.sq` tiene cuatro columnas
   (`_id, source, saved_search, global`) y no existe `feed_categories.sq` en todo el repo. El parche
   llamaba `MAX_SOURCES_PER_TAB` a una constante que aplicaba sobre
   `countFeedSavedSearchGlobal.await()`, un recuento **global**: no es un tope de 25 por pestaña, es el
   tope global de siempre subido de 10 a 25 con un nombre que promete otra cosa.
2. **Habría hecho que la app mintiera.** `too_many_in_feed` lleva el 10 literal en la cadena base
   (`i18n-sy/src/commonMain/moko-resources/base/strings.xml:469`) y en otros 15 locales. Subir el tope
   sin tocarla deja el snackbar de `FeedTab.kt:174` y el toast de `SourceFeedScreenModel.kt:270`
   diciendo 10 cuando la app ya aceptó 25.
3. **Decir la verdad ahí no es una línea.** Los dos sitios pasan un `StringResource` pelado, así que un
   `%1$d` en la base obliga a cambiar la firma de `onToast` y todas las pantallas que la suministran,
   más 16 ficheros de locales que son de Weblate (`pr_label.yml` etiqueta sus PR).

Retirado del mismo diff: el cambio del valor por defecto de `feedLanguageFilter()` (`"en"` → idioma del
dispositivo). Cambia en silencio el feed de toda instalación que nunca tocó el ajuste: es una decisión
de política del mantenedor, no un parche.

## Secuencia corregida (la que quedó en el issue #32)

- **Fase 1 — esquema**, prerrequisito para hablar de pestañas: `feed_categories.sq` + columnas
  `category`/`feed_order`/`search_type` en `feed_saved_search`, migración `76f`, y modelo de backup
  conservando los `@SerialName` legados (`AGENTS.md` §2).
- **Fase 2 — el tope**: `FeedLimits.MAX_SOURCES_PER_TAB` sobre un recuento **por categoría**, cadena
  base con `%1$d`, traducciones a Weblate.
- **Fase 3 — idioma**: defecto al idioma del dispositivo, sugerencias por escaneo, pestaña opcional de
  explorar idiomas.

## Contraste: por qué el de AniZen sí se publicó

AniZen **sí** tiene pestañas reales (`feed_categories.sq`, columna `category`,
`getFeedSavedSearchGlobal.await(categoryId)`), así que «25 por pestaña» es coherente hoy. Su parche se
corrigió (el tope fue al interactor `InsertFeedSavedSearch.await`, que es por donde pasan las **tres**
vías de inserción; `updateFeedCategory` conserva una comprobación **antes** de su delete porque mueve
borrando y reinsertando; `awaitAll` se deja sin tope a propósito porque es la vía de restauración) y se
publicó como rama `feed-cap-per-tab` (`f5f1bdd`, 3 ficheros, +55) referenciada en el issue #94 — sin PR,
porque su `AGENTS.md` los prohíbe. Su guard de procedencia se ejecutó de verdad: `0 violation(s),
0 warning(s)` → `✓ ok`.
