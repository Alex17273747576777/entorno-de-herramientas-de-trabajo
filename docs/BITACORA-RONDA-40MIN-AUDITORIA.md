# Bitácora de auditoría secuencial (ronda en curso)

> Registro de trabajo y evidencias, no sustituto del informe final. No declarar completa una revisión parcial.

## T0 y regla operativa

- **T0 del reloj del sandbox:** 2026-11-19 21:12:20 UTC; epoch `1795122740`; monotónico inicial `3664671352622 ns`. La duración se medirá en el mismo reloj monotónico.
- **Desfase observado:** la fecha local de referencia de plataforma es 2026-11-10 (America/Santo_Domingo), mientras que `datetime.now(UTC)` del sandbox marca 2026-11-19. No mezclar ambos cortes ni cambiar fechas por inferencia.
- **Regla viva localizada:** `docs/ESTADO-VARIABLES-2026-11-15.md` en `Alex17273747576777/entorno-de-herramientas-de-trabajo`, blob `0948dffd338cda162c2282ec61255a2bc2364ab2`; exige rondas exactas de 40 minutos, acciones registradas/verificadas, no imprimir tokens y, en repos ajenos, sólo issue/PR (sin push directo). También prohíbe `present_file`; a partir de aquí no se usará.

## Alcance que se ejecutará

- Perfil vivo + los **ocho repositorios propios/forks distintos de `entorno-de-herramientas-de-trabajo`**; revisar ramas/upstreams, contenido y código de riesgo, issues/PR, dependencias, Actions/CI, releases y sus metadatos. Mantener abierta la auditoría si falta una superficie o validación.
- Comparar explícitamente los tres forks (`anime-extensoes`, `AniZen`, `ShinKu`) con upstream; no sincronizar ni fusionar.
- Revisar §9.9 fila por fila y verificar de forma trazable las afirmaciones de `pieza-01-ES.md`; no inventar la lista ausente de 18 lecciones ni empezar los maestros 01–70 antes de cerrar los bloqueos previos.
- Preparar y, si los permisos lo permiten, abrir el issue autorizado de ShinKu sobre restauración de backups grandes/OOM. Ningún backup personal se adjuntará.

## Acciones verificadas hasta T0

1. El working tree local estaba limpio; `HEAD` y `origin/main` coincidían en `6d08fbc29c8714018e574c9bbe84e0499844f5c4`. `make limpiar` quitó `__pycache__` y `.tmp-prueba.md`; la credencial esperada permanece fuera del repositorio y no se leyó.
2. GitHub REST vivo devolvió 9 repositorios públicos propios, 0 gists, 5 seguidores y 194 seguidos. Los ocho distintos del repositorio de trabajo son `anime-extensoes`, `AniZen`, `ShinKu`, `normas-de-diseno`, `cero-X-app`, `gltools-reborn`, `la-bandita-archivo` y `bandwidth-hero-proxy2`.
3. El upstream `Harrys-HQ/ShinKu` tiene Issues habilitadas. Se revisaron 35 issues y se buscó coincidencia en títulos/cuerpos/PRs. La #21 está cerrada y describe otro fallo (un `NoSuchMethodError` al navegar/migrar tras importar Komikku; resuelto en v2.7.15), no el OOM durante restauración grande. La #39 es de chips de búsqueda guardada y no es relacionada.
4. El POST autorizado para abrir el issue nuevo devolvió HTTP 403, `Resource not accessible by personal access token`; no se creó issue. El conector GitHub de Arena devolvió `unsupported`. No se reintentará ni se sortearán permisos. Se preparará un borrador fiel para que pueda publicarse cuando haya una vía autorizada.

## Registro secuencial de hallazgos

- **T+00:00 — Inicio.** Reloj/timestamp y alcance arriba.
- **T+00:00 — Pendiente.** Continuar con inspección detallada por repositorio, anotar SHA/corte, fuentes primarias, resultado y limitaciones por cada uno; después revisar §9.9 y la pieza factual.
- **T+40:00 — Pendiente.** Registrar cierre real sólo si el reloj monotónico confirma al menos 2.400 s; si no, dejar la ronda abierta y no afirmar cumplimiento.
