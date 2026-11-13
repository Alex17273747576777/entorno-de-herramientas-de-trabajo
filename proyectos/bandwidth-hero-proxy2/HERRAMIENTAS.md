# bandwidth-hero-proxy2 · registro

Fuente canónica: [`bandwidth-hero-proxy2`](https://github.com/Alex17273747576777/bandwidth-hero-proxy2)
rama `main` (medido el 2026-11-13: 20 ficheros, JavaScript, **MIT**, 355 KB, sin
descripción en el repo). Dos workflows: `codeql-analysis.yml` y `tests.yml`.

## No se copia nada, y el motivo

Sus cuatro utilidades (`util/compress.js`, `util/networkPolicy.js`, `util/pick.js`,
`util/shouldCompress.js`) son del proxy y sólo tienen sentido dentro de él: deciden si
comprimir una respuesta, a qué destinos se permite salir y qué campo elegir. Fuera de ese
servicio no son herramientas reutilizables, y copiarlas aquí crearía un segundo sitio
donde pueden quedar obsoletas sin que nada lo avise.

El resto del repo son despliegue y CI: seis `.yml`, dos `.json`, un `.toml`, un `.yaml`,
un `.html` y seis `.js`.

Lo que sí se registra aquí es la auditoría que se le hizo, y vive en
`docs/AUDITORIA-REMOTA-2026-11-10.md` de este mismo repo: **destinos privados bloqueados**
y CodeQL activo. Eso es lo que otro proyecto puede reutilizar de aquí, y es una decisión,
no un fichero.
