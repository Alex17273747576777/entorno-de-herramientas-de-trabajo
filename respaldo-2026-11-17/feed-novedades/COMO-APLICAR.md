# Parches de Fase 2 — cómo aplicarlos y qué están verificados

Dos parches mínimos y autocontenidos (el tope de 25 por pestaña + el idioma por defecto en
ShinKu), generados sobre los clones prístinos y **verificados con `git apply --check`**.

| Parche | Repo y commit base | Líneas | `git apply --check` |
|---|---|---|---|
| `parches/shinku-fase2-tope25-e-idioma.patch` | `Harrys-HQ/ShinKu` @ `043ab7d8e68e8a77752805c34969a2477195826a` | 83 (31 añadidas) | **APLICA_LIMPIO: sí** |
| `parches/anizen-fase2-tope25-por-pestana.patch` | `salmanbappi/AniZen` @ `95160a724d1147777dd1f7997fff4885a4cd9deb` | 66 | **APLICA_LIMPIO: sí** |

## Aplicación

```bash
git clone --depth 1 https://github.com/Harrys-HQ/ShinKu.git && cd ShinKu
git apply --check /ruta/shinku-fase2-tope25-e-idioma.patch && git apply /ruta/shinku-fase2-tope25-e-idioma.patch

git clone --depth 1 https://github.com/salmanbappi/AniZen.git && cd AniZen
git apply --check /ruta/anizen-fase2-tope25-por-pestana.patch && git apply /ruta/anizen-fase2-tope25-por-pestana.patch
```

## Qué toca cada uno

**ShinKu** (3 ficheros editados + 1 nuevo):
- nuevo `domain/.../source/service/FeedLimits.kt` (`MAX_SOURCES_PER_TAB = 25`,
  `MAX_CONCURRENT_FETCHES_PER_TAB = 6`);
- `ui/browse/feed/FeedScreenModel.kt`: `hasTooManyFeeds()` pasa de `> 10` a
  `>= FeedLimits.MAX_SOURCES_PER_TAB` (+ import);
- `ui/browse/source/feed/SourceFeedScreenModel.kt`: mismo cambio en el tope por fuente (+ import);
- `domain/.../exh/source/ShinKuPreferences.kt`: `feedLanguageFilter()` deja de valer `"en"` por
  defecto y pasa al idioma del dispositivo (`Locale.getDefault().language.ifBlank { "all" }`),
  con comentario que remite a `LocaleHelper.getDefaultEnabledLanguages()`.

**AniZen** (1 fichero editado + 1 nuevo):
- nuevo `domain/.../source/service/FeedLimits.kt` (mismas constantes);
- `ui/home/FeedManageScreenModel.kt`: guarda de pestaña llena en los **dos** sitios que insertan
  (`duplicate` y el movimiento entre categorías). La guarda del movimiento va **antes** del
  `deleteFeedSavedSearchById`, de modo que si el destino está lleno la entrada se queda donde
  estaba en vez de borrarse y luego ser rechazada. Usa la lista que esas funciones **ya**
  consultan (`getFeedSavedSearchGlobal.await(categoryId)`), así que no añade ninguna dependencia
  nueva ni ninguna consulta extra; avisa por `logcat` (imports ya usados en `FeedScreenModel`).

## Lo que estos parches NO hacen (deliberadamente)

- **No crean el esquema de categorías en ShinKu** (`feed_categories.sq`, columnas
  `category`/`feed_order`/`search_type`, migración 76f, backup): es la Fase 1 y necesita subir la
  versión de esquema SQLDelight y tocar el serializador de copias. Va en el issue como propuesta,
  no como parche a medias.
- **No cambian las cadenas traducidas**: `too_many_in_feed` sigue diciendo «10» en ~30 locales de
  ShinKu hasta que se aplique el placeholder `%1$d` (Fase 2 completa). Con el parche, el límite
  real es 25 y el texto dice 10: **divergencia conocida y declarada**, no un fallo silencioso.
- **No añaden el aviso visual en AniZen**: la guarda registra por `logcat` y aborta; el canal de
  eventos/snackbar lo elige el mantenedor (el `State` de `FeedManageScreenModel` no tiene hoy un
  campo de eventos, y añadirlo es decisión de diseño suya).
- **No están compilados**: este entorno no tiene Android SDK/Gradle ni `kotlinc`. Lo verificado es
  la aplicabilidad textual contra los árboles prístinos y la existencia/firma de cada símbolo usado
  (ver `VERIFICACION-SIMBOLOS.md`).
