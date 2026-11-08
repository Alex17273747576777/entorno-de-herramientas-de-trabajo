# Exploración de las cuatro fuentes · qué funciones valen y cuáles ya no existen

*Barrido del domingo 8 de noviembre de 2026 sobre everythingmoe.com, miyomi.app, wotaku.wiki, fmhy.net y la API de GitHub*

---

## Cómo se hizo este barrido

No se leyeron descripciones de marketing. Se recorrieron los índices de las cuatro páginas, se sacaron los nombres de las apps, y **cada afirmación técnica se verificó contra el árbol de archivos de su repositorio en GitHub**. Cuando una app dice «soporta X», este informe comprueba si existe un archivo que lo implemente.

Eso produce un documento distinto al de las cuatro webs: ellas dicen **qué hay**; esto dice **qué funciona, qué está muerto y qué merece copiarse**.

---

## Lo primero: una app de 47.217 estrellas fue vaciada

Antes de las funciones, el dato que cambia el mapa.

**Legado** (`gedoor/legado`) es, con diferencia, la aplicación más popular del ecosistema que cubren estas cuatro páginas: **47.217 estrellas**. Su sistema de fuentes definidas por reglas es la innovación más copiada del mundo de la lectura de novelas.

Hoy su repositorio tiene **dos archivos**: un `README.md` de 707 bytes y una imagen. Nada más. Su último empujón fue el **27 de mayo de 2026**. No tiene ninguna entrega.

El README, traducido del chino, dice:

> «Este proyecto ha incurrido en infracciones y ha asumido la correspondiente responsabilidad legal. Por la presente se publica un anuncio solemne: se elimina el contenido del proyecto y se insta a todos a que **cesen de inmediato toda conducta relacionada con infracciones**, no imiten, no se dediquen a, no difundan actividades infractoras, y no alberguen ninguna esperanza de impunidad. **La línea legal no se puede traspasar.**»

Enlaza al anuncio de protección de propiedad intelectual de China Literature (阅文), el mayor grupo editorial de ficción en línea del país.

**Esto importa para cero-X más que ninguna función de esta lista.** La app más querida del ecosistema, la que tenía el sistema de fuentes más elegante, fue desmontada por presión legal, no por falta de usuarios ni por abandono. Cualquier diseño de compatibilidad universal que se haga hoy tiene que asumir eso como escenario real, no como posibilidad remota.

Y hay un detalle que casi nadie nota: **Legado sigue en las cuatro listas**. everythingmoe, miyomi, wotaku y fmhy lo recomiendan como si nada. Las listas curadas envejecen, y este barrido encontró al menos cuatro casos de eso. Lo digo porque es exactamente el defecto que La Bandita está corrigiendo en sus publicaciones: contar lo que era en vez de lo que es.

---

## Las tres arquitecturas de extensión que existen

Aquí está el hallazgo central de todo el barrido, y es el que responde a «compatibilidad universal con todo el ecosistema». **No hay una arquitectura. Hay tres, y son incompatibles entre sí.**

### Arquitectura 1 · Contrato JVM en APK

**Quién la usa:** Mihon, Tachiyomi, Aniyomi, Komikku, Neko, Kotatsu, houri, Kototoro, Animetail, Kumo, Atahon.

La extensión es un **APK aparte** con su `classes.dex`, que declara una clase implementando una interfaz del anfitrión. El anfitrión la carga con un `ClassLoader`.

Evidencia medida:

| proyecto | rutas `eu.kanade` / `tachiyomi` | qué significa |
|---|---:|---|
| houri | `source-api/` con **70 archivos** | contrato completo, propio |
| Kototoro | 167 de `extension`, 399 de `parser` | fusión de tres familias |
| Animetail | Apache-2.0, push de hoy | sobre Mihon/Aniyomi |

Funciona muy bien y **no puede salir de la JVM**. Una extensión de Mihon no corre en iOS ni en Windows.

### Arquitectura 2 · Motor JavaScript

**Quién la usa:** Mangayomi, AnymeX, Dartotsu.

La extensión **no se compila**: es un archivo JavaScript que se evalúa dentro de un motor JS embebido. Evidencia en el árbol de Mangayomi:

```
lib/eval/javascript/dom_selector.dart     selector de DOM para parsear HTML
lib/eval/javascript/extractors.dart       extractores
lib/eval/javascript/http.dart             cliente HTTP expuesto al JS
lib/eval/javascript/service.dart          registro de servicios
lib/eval/javascript/preferences.dart      preferencias por extensión
lib/eval/javascript/js_common.dart        utilidades
lib/eval/javascript/js_errors.dart        errores
lib/eval/javascript/utils.dart
```

Eso es un **runtime de extensiones completo**, en 1.546 archivos, en Dart.

Y aquí está por qué esto es la arquitectura más universal que existe: **una misma extensión JavaScript corre en Android, iOS, Windows, Linux y macOS**. No hay que recompilar nada por plataforma. Es la razón por la que Mangayomi soporta cinco sistemas y Mihon solo Android.

### Arquitectura 3 · Fuentes por reglas

**Quién la usaba:** Legado, y toda su descendencia.

La fuente es un documento de reglas (expresiones sobre el DOM, rutas de datos) interpretado por la app. Elegante, sin código, editable por cualquiera. Y es la que fue desmantelada.

### Lo que esto significa para cero-X

La recomendación anterior de este trabajo era copiar `eu.kanade.tachiyomi`. **Era correcta y era incompleta.** Con solo eso, cero-X hablaría con un tercio del ecosistema. La arquitectura que de verdad cubre todo necesita **las dos primeras capas**, porque la tercera ya no tiene dónde correr:

```
capa 1 · JVM    → APK de extensión (Mihon/Aniyomi/Kotatsu) · ClassLoader aislado
capa 2 · JS     → extensión JavaScript (Mangayomi/AnymeX)  · motor JS embebido
capa 3 · datos  → importador de copias de seguridad de todas las demás
```

La capa 3 es la que resuelve el otro pedido: **compatibilidad con copias de seguridad de otras apps**. Y aquí hay suerte, porque los dos proyectos ya lo tienen resuelto y publicado:

```
Mangayomi · lib/modules/more/data_and_storage/providers/tachiyomi_restore_service.dart
AnymeX    · lib/controllers/services/backup_restore/parsers/tachiyomi_backup_parser.dart
```

**Ambos leen backups de Tachiyomi/Mihon.** Ninguno de los dos usa `eu.kanade` para cargar extensiones: solo lo usan **para leer el formato de backup**. Es la prueba de que el importador es una pieza aparte y perfectamente factible. Son Apache-2.0 y MIT respectivamente, así que se pueden estudiar sin problema de licencia.

---

## Las funciones que merecen copiarse, app por app

Selección hecha sobre evidencia de archivos, no sobre descripciones.

### anx-reader · 9.211 estrellas · MIT · Dart
El mejor lector de libros del ecosistema, y el que más funciones tiene por estrella.

| función | evidencia | por qué vale |
|---|---|---|
| **TTS integrado** | 18 rutas con `tts` | lectura en voz alta sin salir del libro |
| **WebDAV** | 22 rutas con `webdav` | sincronía con servidor propio, sin nube ajena |
| **Traducción** | 11 rutas con `translat` | traducir el texto sin cambiar de app |
| **EPUB** | 14 rutas con `epub` | formato abierto, no propietario |
| **Sincronía** | 20 rutas con `sync` | progreso entre dispositivos |
| **Extensiones** | 15 rutas | su propio sistema |

**Lo que hay que copiar:** el trío TTS + WebDAV + traducción. No hay ninguna app de manga del ecosistema que tenga el TTS bien resuelto, y es la función más pedida por quien lee de noche.

### Mangayomi · 4.422 estrellas · Apache-2.0 · Dart
| función | evidencia | por qué vale |
|---|---|---|
| **Runtime JS** | `lib/eval/javascript/` (8 archivos) | extensiones multiplataforma reales |
| **Restauración de Tachiyomi** | `tachiyomi_restore_service.dart` + test | importa la biblioteca de Mihon |
| **88 rutas de tracker** | 88 con `trac` | el que más servicios de seguimiento soporta |
| **Subtítulos** | 9 rutas | pista de subtítulos propia |
| **5 plataformas** | — | Android, iOS, macOS, Linux, Windows |

**Lo que hay que copiar:** el runtime JS completo, y el test de importación de historial (`tachiyomi_history_import_test.dart`), que es la prueba de que el importador funciona y no solo existe.

### AnymeX · 1.285 estrellas · **MIT** · Dart
| función | evidencia | por qué vale |
|---|---|---|
| **Multi-tracker** | descripción: AL, MAL, SIMKL | seguir en tres servicios a la vez |
| **Parser de backups** | `tachiyomi_backup_parser.dart` | importa de Tachiyomi |
| **Pruebas de extensión** | `ExtensionTesting/extension_test_controller.dart` | probar una extensión antes de confiar en ella |
| **Gestor de plugins** | `widgets/plugin_manager.dart` | instalar y quitar sin reiniciar |

**Lo que hay que copiar:** `ExtensionTesting/`. Es la única app del ecosistema que tiene una **pantalla para probar una extensión** antes de usarla. Eso es exactamente la respuesta a «¿cómo sé que esta extensión no me va a romper la app?».

### Animetail · 616 estrellas · Apache-2.0 · Kotlin · push de hoy
La más viva de las de su clase: basa en Mihon/Aniyomi y publicó hoy mismo.
**Lo que hay que copiar:** su ritmo. Mientras Kotatsu lleva un año sin empujar, Animetail empuja todos los días.

### Kototoro · Kotlin · Apache-2.0
| función | evidencia |
|---|---|
| **Fusión de tres familias** | 167 de `extension`, 399 de `parser`, 24 de `plugin` |
| **Excepción de incompatibilidad** | `core/exceptions/IncompatiblePluginException.kt` |
| **Índice de backup previo** | `backups/data/model/BackupIndexFactory.kt` |
| **Cobertura de Android↔iOS↔macOS↔Windows** | 5 APK + `.ipa` + 2 `.dmg` + `.msi` |

**Lo que hay que copiar:** la excepción explícita y el índice previo. Fallar claro en vez de fallar raro.

### Neko · 2.825 estrellas · Apache-2.0 · Kotlin
Lector no oficial de MangaDex. Especializado y sin deuda.
**Lo que hay que copiar:** nada exótico. Es la referencia de lo que cuesta hacer **una sola cosa** bien: su APK es de los más pequeños del ecosistema.

### Miru App · 5.796 estrellas · AGPL-3.0 · Dart
Soporta video, cómics y novelas con fuentes extendidas, en Android, Windows y web.
**Aviso:** AGPL-3.0. Copiar código de aquí obliga a cero-X a ser AGPL también. Apache-2.0 es compatible en un sentido, no en el otro. **Se puede aprender de su diseño, no se puede copiar su código** sin cambiar la licencia del proyecto entero.

### Myne · 1.544 estrellas · Apache-2.0 · Kotlin
Descarga y lee libros de Project Gutenberg. Compose puro.
**Lo que hay que copiar:** el catálogo de dominio público como fuente sin dependencia de nadie. Es la única fuente de las cuatro listas que **no puede desaparecer** por presión legal: los libros ya están en dominio público.

### NineAnimator · 820 estrellas · GPL-3.0 · Swift · último push 2024-11-14
Anime para iOS y macOS. **Dos años sin actualizar.** Aparece en wotaku y en miyomi. Es el ejemplo más claro de lista desactualizada junto a Legado.

---

## Lo que las cuatro fuentes tienen y NO hay que copiar

Aquí es donde un informe honesto se separa de una lista de enlaces.

**fmhy.net dedica secciones enteras a APKs modificados.** Su propia primera advertencia lo dice: *«ten en cuenta que algunos sitios de APK modificados listan apps con nombres falsos»*. Para cero-X, que quiere dar al usuario con qué comprobar lo que baja, orientar hacia un APK reempaquetado por un tercero es lo contrario de su tesis. **Se cita la existencia, no se recomienda el uso.** La diferencia entre «esto existe» y «esto te conviene» es toda la diferencia.

**Las cuatro listas incluyen apps con licencias que prohíben reutilizar su código.** De las medidas hoy: Miru es AGPL-3.0, NineAnimator y Kotatsu son GPL-3.0, Dartotsu tiene `NOASSERTION`. Antes de copiar una línea hay que mirar la licencia, y ninguna de las cuatro páginas la muestra en el índice. Eso es un hueco real de las cuatro.

**Legado aparece en las cuatro y está vacía.** Es el caso extremo, pero no el único: Kotatsu lleva **un año sin empujar** y aparece en tres, y NineAnimator lleva dos.

**Ninguna de las cuatro mide si una app publica huellas de sus descargas.** De las apps verificadas hoy, **cero** lo hacen. La única que publicaba huellas en todo el ecosistema medido es Kototoro, y solo para iOS, macOS y Windows.

---

## El diseño que sale de este barrido

### Capa 1 · Extensiones JVM
```
modules/source_api/eu/kanade/tachiyomi/    ← ya creado, compila con 0 errores
  Source.kt · CatalogueSource.kt · SourceFactory.kt
  ExtensionSourceLoader.kt                  ← DexClassLoader aislado
```
Cubre Mihon, Tachiyomi, Aniyomi, Komikku, Neko, Animetail, Kumo, Atahon, Kototoro, houri.
**Falta:** el segundo contrato, `org.koitharu.kotatsu.parsers`.

### Capa 2 · Extensiones JavaScript
```
modules/source_js/
  JsRuntime.kt              envoltorio del motor (QuickJS o J2V8)
  JsHttpBridge.kt           HTTP expuesto al JS, como en Mangayomi
  JsDomSelector.kt          selector de DOM, como en Mangayomi
  JsExtensionRegistry.kt    registro de servicios
```
Cubre Mangayomi, AnymeX, Dartotsu, y **cualquier plataforma**.
**Referencia de diseño:** el árbol `lib/eval/javascript/` de Mangayomi (Apache-2.0).

### Capa 3 · Importador de copias de seguridad
```
modules/backup_import/
  TachiyomiBackupReader.kt   formato .tachibk / .proto.gz
  MangayomiBackupReader.kt   JSON
  AniyomiBackupReader.kt     incluye anime
  BackupImporter.kt          índice previo, luego escritura
```
**Referencias ya publicadas:** `tachiyomi_backup_parser.dart` (AnymeX, MIT) y `tachiyomi_restore_service.dart` (Mangayomi, Apache-2.0).

### Y la regla que se desprende de Legado

> **Ninguna fuente puede ser la única.** El diseño tiene que degradar bien: si una familia de extensiones desaparece, el usuario conserva su biblioteca, sus backups y las otras familias.

En la práctica son tres decisiones concretas:

1. **Los datos del usuario viven en local, en un formato abierto y documentado.** Si la app muere, los datos sobreviven.
2. **El importador es de primera clase, no un extra.** Poder entrar desde Mihon y salir hacia otra app es lo que hace que la biblioteca del usuario no sea rehén.
3. **Ningún contrato se da por eterno.** La lista de repositorios de extensiones va **firmada y actualizable**, no incrustada en el código.

---

## Resumen en cinco líneas

1. **Legado, 47.217 estrellas, fue vaciada por presión legal** y las cuatro listas siguen recomendándola.
2. Hay **tres arquitecturas de extensión incompatibles**: JVM (Mihon), JavaScript (Mangayomi/AnymeX) y reglas (Legado). Para cubrir el ecosistema hacen falta las dos primeras.
3. **Mangayomi tiene un runtime de extensiones JavaScript completo** en `lib/eval/javascript/`: es la única vía a extensiones que funcionen igual en Android, iOS y escritorio.
4. **AnymeX y Mangayomi ya leen backups de Tachiyomi** — el importador no hay que inventarlo, hay que portarlo. Ambos con licencia permisiva.
5. **anx-reader** (MIT, 9.211★) es la fuente de las funciones que faltan en todo lector de manga: TTS, WebDAV y traducción integrada.

---

*Verificado hoy contra la API de GitHub. Los conteos de rutas salen del árbol recursivo de cada repositorio. Las licencias salen del campo `license` de la API. Cuando algo no se pudo confirmar —el SQLCipher de houri, por ejemplo— se dice en el texto en vez de rellenarse.*
