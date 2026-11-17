# ktlint local como oráculo de `spotlessCheck` · medido el 2026-11-17

*Receta sin otra casa: el código del PR #37 vive en el fork de ShinKu y el informe en la propia
incidencia; esto es el **cómo se midió**, que es lo que se pierde al reciclar el contenedor.*

## El problema

`build_check.yml` corre `./gradlew spotlessCheck assembleDevDebug`. Sin Gradle ni Android SDK en esta
máquina no se puede ejecutar nada de eso, así que el PR #37 salió **sin compilar**: no había forma de
saber si mis cuatro ficheros Kotlin pasaban el formato ni si el build llegaría a compilarlos.

## La receta

ktlint es un jar autocontenido y el proyecto lo tiene fijado en `gradle/libs.versions.toml:20`
(`ktlint-core = "1.8.0"`, módulo real `com.pinterest.ktlint:ktlint-cli`). Se descarga **esa** versión:

```bash
curl -sSL -o /tmp/ktlint https://github.com/pinterest/ktlint/releases/download/1.8.0/ktlint
stat -c%s /tmp/ktlint          # 71.471.207 B. Si salen <5000, es una página de error, no el jar.
export JAVA_HOME=/var/tmp/jdk/jdk-17.0.13+11; export PATH=$JAVA_HOME/bin:$PATH
java -jar /tmp/ktlint --version   # ktlint version 1.8.0
```

Se ejecuta **desde la raíz del módulo**, que es como lo invoca spotless
(`buildSrc/src/main/kotlin/shinku.code.lint.gradle.kts:23` hace `target("**/*.kt", "**/*.kts")` por
proyecto). El `.editorconfig` de la raíz se aplica solo:

```bash
cd <módulo> && java -jar /tmp/ktlint --relative "**/*.kt" "**/*.kts"
```

Dos trampas medidas:

- **`--code-style` ya no existe en 1.8.0.** Da `Parameter '--code-style' is no longer valid` y
  **EXIT=1**, que se parece muchísimo a «hay violaciones». El estilo se declara en `.editorconfig`
  (`ktlint_code_style = intellij_idea`). Medir siempre con la salida delante, no con el código.
- **Comparar contra una copia sin `.editorconfig` invalida la comparación.** Con el fichero de
  configuración, cuatro ficheros dan 5 violaciones; sin él, los mismos cuatro dan 94, porque ktlint
  aplica `class-signature`, `function-signature` y `function-expression-body`, que este proyecto tiene
  `disabled`. Es FALLA-013.

## La falsación (lo que hace creíble el oráculo)

Contra lo que CI dijo de verdad en las corridas 44077189841 y 44078747502:

| módulo | CI | ktlint 1.8.0 local |
|---|---|---|
| `core-metadata` | `spotlessKotlinCheck` **pasó** | 0 violaciones |
| `i18n` antes del arreglo | **falló** (`build.gradle.kts`, orden de imports) | 1, mismo fichero, misma regla |
| `i18n` después | **pasó** | 0 |
| `macrobenchmark` | **falló** en `BaselineProfileGenerator.kt:26:19` | 1, mismo fichero, misma línea, misma regla (`trailing-comma-on-call-site`) |

## Lo que salió

Violaciones por módulo sobre el `main` del mantenedor (`c7ab60c9`) + mi rama:

```
app 910 · domain 83 · source-api 55 · data 19 · core 16 · presentation-core 5
source-local 4 · macrobenchmark 1 · core-metadata 0 · i18n 0 · i18n-sy 0
```

1.113 en 621 ficheros; por regla: `import-ordering` 597, `indent` 350, `no-trailing-spaces` 48,
`statement-wrapping` 32, `trailing-comma-on-call-site` 22.

**Consecuencia, que es lo que importa:** como `spotlessCheck` va antes que `assembleDevDebug`, el
build de este repo **no compila nada** en ningún PR hasta que alguien pase `spotlessApply` a los 621
ficheros. Por eso las cuatro corridas registradas fallaron, incluida la del PR #36, que el mantenedor
fusionó igual. Un barrido de 621 ficheros no cabe en un PR de 16 cadenas: se ofrece aparte.

## El XML que spotless sí mira

`shinku.code.lint.gradle.kts:9-19` excluye `src/commonMain/moko-resources/**` del formato XML
**salvo `base/**`.** O sea: de los 16 `strings.xml` del PR, 15 están fuera del alcance de spotless y
`base/strings.xml` sólo se sujeta a `trimTrailingWhitespace()` y `endWithNewline()` — las dos
verificadas sobre el fichero cambiado (0 líneas con espacios al final, termina en salto de línea).

## La otra verificación, que no es de formato

Las 16 cadenas se formatearon **de verdad** con `Formatear16Locales.java` en este directorio: extrae
cada `too_many_in_feed` del XML modificado (desescapando `\'` y las entidades), lo pasa por
`java.util.Formatter` con su `Locale` en JDK 17 —el formateador que usa moko por debajo, vía
`StringDesc.ResourceFormatted`— y comprueba que no quede `%1$d` y que aparezca el número en los
dígitos de ese idioma. 16/16. En árabe sale `٢٥` y en asamés `২৫`, que es lo que un «10» escrito a
mano no puede producir nunca. Las cadenas extraídas están en `cadenas-16-locales.json`.
