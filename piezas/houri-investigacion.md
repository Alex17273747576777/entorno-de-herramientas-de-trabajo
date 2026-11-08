# houri, medido · y por qué es la pieza que cero-X necesita copiar

*Investigación del domingo 8 de noviembre de 2026 contra la API de GitHub y contra miyomi.app*

---

## Qué es houri, sin adornos

**houri es una bifurcación de Komikku**, y esa cadena importa más que la descripción:

```
Tachiyomi → TachiyomiSY → Mihon → Komikku → houri
```

Cuatro generaciones. Todo lo que houri sabe hacer, lo heredó de esa cadena, y houri no reescribió ninguno de los contratos: los **importó**.

| dato | valor medido |
|---|---|
| repositorio | `PineappleTwilight/houri` |
| licencia | **Apache-2.0** |
| lenguaje | Kotlin |
| estrellas | 45 |
| creado | **26 de julio de 2026** |
| último empujón | 4 de noviembre de 2026 |
| tamaño del repositorio | 105.209 KB |
| archivos | **2.829** |
| última entrega | **v1.25.3**, 4 de noviembre de 2026 |

Y un detalle que corrige la ficha oficial: **miyomi.app muestra la versión v1.21.17 del 14 de octubre de 2026**. La entrega real de GitHub es la **v1.25.3 del 4 de noviembre**. La ficha del sitio lleva tres semanas de retraso. No es un error de nadie: es lo que pasa cuando una página estática cuenta lo que un repositorio mueve todos los días.

---

## El peso, que aquí sí está resuelto

Seis APK en la entrega v1.25.3:

| APK | bytes | MiB | descargas |
|---|---:|---:|---:|
| `houri-arm64-v8a` | 163.133.833 | **155,58** | 90 |
| `houri-armeabi-v7a` | 112.064.941 | 106,87 | 9 |
| `houri-nomtl-arm64-v8a` | 90.502.078 | **86,31** | 35 |
| `houri-nomtl-armeabi-v7a` | 78.918.614 | 75,26 | 9 |
| `houri-x86` | 127.445.132 | 121,54 | 2 |
| `houri-x86_64` | 155.093.180 | 147,91 | 2 |
| **total** | **727.157.778** | **693,47** | **147** |

Dos cosas que solo se ven mirando los nombres:

**Primera: `nomtl` no es una versión menor, es una versión sin el motor de traducción.** La diferencia entre `arm64-v8a` (155,58 MiB) y `nomtl-arm64-v8a` (86,31 MiB) es de **69,27 MiB**. Eso es lo que cuesta el motor de traducción por IA dentro del APK: **el 44,5 % del archivo**. Y aquí está la lección de empaquetado del ecosistema: houri **publica las dos**, y deja que el usuario decida si quiere pagar 69 MiB por la traducción automática. Las 90 descargas del completo contra las 35 del `nomtl` dicen que la mayoría sí la quiere — pero la decisión es del usuario, no del empaquetador.

**Segunda: no hay APK universal.** Cinco variantes por arquitectura y ni una «universal». Cada quien baja la de su teléfono. Es la decisión opuesta a la de Kototoro, que publica un universal de 300,86 MiB además de los splits. Comparar los dos casos es la mejor lección de empaquetado que hay hoy en el ecosistema: **mismo ecosistema, dos filosofías opuestas, las dos defendibles.**

**Y la tercera, que es la de la pieza 31 repetida:** houri **no publica ni una huella**. Cero archivos `.sha256`, cero checksums, en una entrega de seis APK y 693,47 MiB. Con esto el hallazgo de la pieza 31 deja de ser un caso y pasa a ser un patrón: veinte repositorios medidos ayer, houri medido hoy, y sigue habiendo un solo proyecto en todo el ecosistema que publica huellas — y las publica para todo menos para Android.

---

## La arquitectura que hay que copiar

Aquí está lo que de verdad importa para cero-X. houri tiene **2.829 archivos**. Repartidos así:

| carpeta | archivos |
|---|---:|
| `app/` | 1.416 |
| `flagkit/` | 256 |
| `domain/` | 239 |
| `data/` | 143 |
| `i18n/` | 138 |
| `core/` | 110 |
| `presentation-core/` | 98 |
| **`source-api/`** | **70** |

Ese `source-api/` de 70 archivos es la pieza clave, y su contenido lo explica todo:

```
source-api/src/commonMain/kotlin/eu/kanade/tachiyomi/source/Source.kt
source-api/src/commonMain/kotlin/eu/kanade/tachiyomi/source/CatalogueSource.kt
source-api/src/commonMain/kotlin/eu/kanade/tachiyomi/source/ConfigurableSource.kt
source-api/src/commonMain/kotlin/eu/kanade/tachiyomi/source/SourceFactory.kt
```

**`eu.kanade.tachiyomi`** es el espacio de nombres de Mihon. No es un homenaje ni una inspiración: es **el mismo paquete, con las mismas firmas**. Una extensión de Mihon compilada como APK declara una clase que implementa `eu.kanade.tachiyomi.source.CatalogueSource`. Si la app que la carga tiene esa interfaz —con ese nombre exacto, en ese paquete exacto— la extensión carga. Si no la tiene, no carga, y no hay forma de adaptarla sin recompilar la extensión.

Eso es **todo** el secreto de la compatibilidad universal de extensiones. No es un motor genérico de plugins. No es un intérprete. Es **copiar el contrato con el nombre exacto**.

Y de ahí salen los otros recuentos, que confirman la tesis:

| palabra clave | archivos | qué significa |
|---|---:|---|
| `extension` | 108 | gestión de extensiones instalables |
| `backup` | 48 | copias de seguridad, con decodificador e índice |
| `tracker` | 27 | MAL, AniList, Kitsu… |
| `discord` | 17 | Rich Presence de Discord |
| `webhook` | 7 | avisos por webhook |

Y las piezas que la ficha oficial presume y que los nombres de archivo no muestran igual de claro: **subcategorías jerárquicas** (`DeleteOrphanedSubcategories`, `SubcategoryUpdateScope`), **relectura** (`StartRereading`, `CompleteRereadIfNeeded`), **integridad de copias** (`BackupIntegrityHandler`) y **traducción** (`TranslateMangaStore`, `TranslatedPageStore`).

Un dato de honestidad: **busqué `sqlcipher` en las 2.829 rutas y no aparece ninguna**. La ficha dice que houri lo soporta. Puede ser que venga como dependencia de Gradle sin módulo propio, y lo más probable es que sea eso. Pero desde las rutas no se puede confirmar, y por eso lo digo como lo que es: **no verificado**.

---

## Lo que esto le dice a cero-X

cero-X tiene hoy dos módulos que apuntan a esto y no llegan:

```
modules/extension_factory/   ExtensionFactory.kt, ExtensionCompiler.kt, ExtensionBuilder.kt
modules/extension_sandbox/   ExtensionInstaller.kt, ExtensionIsolator.kt, ExtensionStore.kt, ExtensionValidator.kt
```

La intención está. Lo que falta es lo que houri tiene y cero-X no:

**cero-X no menciona `eu.kanade.tachiyomi` en ninguno de sus 102 archivos.** Lo comprobé buscando el paquete en todo el árbol: cero resultados.

Eso significa que hoy, cero-X podría instalar una extensión de Mihon en su sandbox y **no podría cargarla**, porque el contrato que la extensión espera no existe en su classpath. Todo el trabajo de `ExtensionIsolator` y `ExtensionValidator` está construido sobre una interfaz que cero-X tendría que escribir primero.

### La receta, en cuatro pasos

1. **Crear el módulo `source-api/`** con el paquete `eu.kanade.tachiyomi.source` y las interfaces base: `Source`, `CatalogueSource`, `HttpSource`, `ParsedHttpSource`. Sin eso, no hay compatibilidad posible con el ecosistema Mihon, que es la inmensa mayoría de las extensiones que existen.
2. **Añadir el segundo contrato: `org.koitharu.kotatsu.parsers`.** Kotatsu tiene su propia familia. Con los dos, cero-X hablaría los dos idiomas del ecosistema de lectura.
3. **Aislar con `ClassLoader` propio** — `ExtensionIsolator.kt` ya apunta ahí, y es lo correcto. Un plugin que trae bytecode se carga aislado o tumba la app.
4. **Verificar antes de cargar**: firma del APK, versión del contrato y hash del origen. El `ExtensionValidator.kt` que ya existe es el sitio.

Y una decisión que hay que tomar antes de escribir una línea, la misma que planteé en la investigación de Kototoro:

> **¿cero-X acepta extensiones de cualquier origen o solo de repositorios de confianza firmados?**

Un lector que carga APKs de extensión de cualquier sitio está ejecutando bytecode de terceros con los permisos de la app. La respuesta que se puede defender sin engaño no es «sí» ni «no», es **una lista de repositorios firmada, más una advertencia explícita para el origen que no está en la lista**. houri lo resuelve así: gestiona repositorios de extensiones (Kavita, Keiyoushi, MHRepo, Nyora y más) en vez de aceptar cualquier archivo suelto.

---

## Las extensiones que houri sí reconoce

De la ficha de miyomi.app, y esto sirve como mapa del ecosistema real:

| repositorio | fuente | cuántas |
|---|---|---:|
| Keiyoushi | la tienda principal del ecosistema Mihon | 485 |
| Yuzono Cursed | tienda para contenido 18+ | 132 |
| Kavita | servidor propio de biblioteca | 147 |
| Suwayomi | servidor propio | 62 |
| Nyora | **un solo paquete con el motor de kotatsu-parsers: ~900 fuentes on-device** | 36 |
| MHRepo | repositorio comunitario, proyecto MHExtensions | 29 |
| Project Nox | arreglos, fuentes propias y sincronía con Keiyoushi | 29 |
| TheNano | fuentes en chino | 14 |

Que Nyora empaquete **~900 fuentes** dentro de un solo paquete es la prueba definitiva de la tesis de esta investigación: no hacen falta 900 extensiones, hace falta **un motor de parsers y un contrato**. Exactamente lo que houri heredó y cero-X no tiene.

---

## Resumen en cuatro líneas

1. houri es Komikku con cuatro generaciones de herencia detrás, y no reescribió ningún contrato: **importó** `eu.kanade.tachiyomi`.
2. Su APK completo pesa **155,58 MiB**; sin el motor de traducción, **86,31 MiB**. La diferencia de 69,27 MiB es lo que cuesta el ML, y publica las dos versiones.
3. No publica ni una huella, y con esto el patrón de la pieza 31 queda confirmado en un tercer ecosistema.
4. **cero-X no tiene el contrato `eu.kanade.tachiyomi`**, y sin él su sandbox de extensiones es una caja fuerte sin puerta.

---

*Datos medidos hoy contra la API de GitHub con la entrega v1.25.3. La ficha de miyomi.app muestra v1.21.17: tres semanas de retraso, dicho aquí para que nadie cite la versión equivocada.*
