# Continuación cero-X — módulo web

Fecha: 2026-11-12 (UTC)

## Punto de partida

- El respaldo de Drive documentaba `main` en `d208af2f` (478 pruebas).
- El repo público ya tenía `ddaaec02`, con el módulo web y dos CI rojos (`43210437545` y `43210476320`), ambos en `compileDebugKotlin`.
- Causa localizada: `ui/MainActivity.kt` y `ui/main/MainActivity.kt` declaraban `com.ceroX.app.ui.main.MainActivity`; la primera era una copia de 292 líneas cuya única diferencia útil era el destino Web.

## Cambios

- Destino Web consolidado en `ui/main/MainActivity.kt` y copia sobrante retirada.
- 11 claves `web_*` traducidas en los 14 archivos de idioma (el mensaje anterior decía 10, pero el censo real es 11).
- `WebPantallaTest.kt`: 3 regresiones para MainActivity única y navegación, correspondencia de IDs y presencia de las cadenas en los 15 idiomas.
- La fixture de IDs excluye `b.root`, que es la raíz y no un `android:id` del layout.

## Evidencia local

- JDK Temurin 21.0.13; SDK Android 36; Gradle 8.11.1.
- `:app:compileDebugKotlin`: BUILD SUCCESSFUL.
- Pruebas dirigidas: 15/15 en verde (WebPantallaTest 3, WebPrivacidadTest 6, TraduccionesPresentesTest 6).
- Suite completa `:app:testDebugUnitTest`: **487 pruebas · 0 fallos · 0 errores · 6 saltadas**.
- `git diff --check`: limpio.
- Los límites de memoria se pasaron mediante un init script externo al repo; no se cambiaron las pruebas de estrés ni la configuración publicada.

## No hecho

- No se hizo push, no se despachó CI y no se modificó ninguna release.
- No se instaló en un teléfono; la navegación WebView sigue requiriendo validación en dispositivo.
