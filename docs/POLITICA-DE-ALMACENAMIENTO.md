# Política de almacenamiento · GitHub es el disco, aquí no se guarda nada

*Regla de la casa, escrita el domingo 8 de noviembre de 2026*

---

## La regla

**Todo lo que se produce se sube a GitHub.** El workspace local es una mesa de trabajo que se barre al final, no un archivador.

**La única excepción es el token**, y vive en un solo archivo, con permisos de dueño y nada más:

```
/home/user/.gh-token       (0600 · 93 bytes · el único archivo local permanente)
```

No se copia a ningún repositorio, no se escribe en ningún `.git/config`, no se pega en ningún README. Si alguien clona cualquiera de estos repos, no encuentra ahí ni un rastro del token.

---

## Cómo se autentica sin escribir el token en ningún sitio

Git no necesita el token dentro de la URL del remoto. Se le da un *credential helper* que lo lee del archivo cuando hace falta:

```bash
git config credential.helper /home/user/.gh-credential
```

Y el helper, que son cuatro líneas, hace solo esto:

```sh
#!/bin/sh
case "$1" in
  get) printf 'username=x-access-token\npassword=%s\n' "$(cat /home/user/.gh-token)" ;;
esac
```

Con eso, los remotos quedan limpios:

```
https://github.com/Alex17273747576777/entorno-de-herramientas-de-trabajo.git
```

en vez de:

```
https://x-access-token:github_pat_...@github.com/...
```

La diferencia importa: un `.git/config` con el token embebido se filtra con un `zip`, con un `tar`, con una captura de pantalla o con un `git remote -v` que alguien pegue en un chat. Un helper no.

---

## Auditoría del 8 de noviembre

Se comprobó, en los tres repositorios:

| comprobación | resultado |
|---|---|
| token en algún commit del historial | **0 commits** en los tres |
| token en algún archivo versionado | **ninguno** |
| token en las URLs de los remotos | **3 de 3** → corregido |
| archivos locales permanentes | **1** (`.gh-token`) |

Los remotos con token embebido se limpiaron con `git remote set-url` y se sustituyeron por el helper. El historial de commits nunca lo contuvo, así que no hubo que reescribir nada.

---

## Qué se barre al terminar cada sesión

1. Los clones de trabajo (`/tmp/...`) — el repositorio ya está en GitHub, el clon no hace falta.
2. Los archivos de paso: los `.md`, `.py` y `.json` que se generaron para medir y ya están en un commit.
3. Las carpetas de compilación, los `__pycache__` y los `.tmp`.

Lo que **no** se barre: `/home/user/.gh-token`, porque sin él no hay push.

---

## Por qué esto no es solo orden

Un workspace local tiene tres problemas que GitHub no tiene:

- **Se pierde.** Un contenedor se recicla y se acaba el trabajo no subido.
- **No tiene historial.** Un archivo local no recuerda quién lo cambió ni cuándo.
- **No se puede revisar.** Lo que está en GitHub se lee, se comenta y se corrige por otra persona.

Y tiene uno que GitHub sí tiene y es peor: **el workspace es donde se acumulan los archivos que nadie usa**. El `INFORME-31-40.md` sirve aunque nadie lo abra; el `.txt` con una medición intermedia que ya se transcribió a un commit, no. La regla de subir todo es también la regla de no acumular basura: lo que no merece un commit, no merece guardarse.

## Decisión del 2026-11-13: los repos se quedan **públicos**

Preguntado el dueño, que había pedido «un remoto Git privado», la respuesta fue
dejarlos públicos con conocimiento de causa. Los seis repos de la cuenta son públicos
y siguen siéndolo. Eso no es un descuido sino una decisión, y tiene una consecuencia
que obliga: **si nada es privado, nada puede contener un secreto.** Nunca.

Lo que ya sostiene esa decisión, medido el 2026-11-10 sobre 19.528 ficheros y
236.902.990 bytes de los seis repos: 0 coincidencias de token de GitHub, clave privada
PEM y credencial de AWS; secret-scanning, push protection, alertas y Dependabot
activos en los seis. Ver `docs/AUDITORIA-REMOTA-2026-11-10.md`.

Lo que se añadió el 2026-11-13 al copiar herramientas de otros repos a `proyectos/`:
barrido de `github_pat_`, `ghp_`, `gho_`, `AKIA`, PEM, `AIza` y `x-access-token` con
valor sobre todo lo añadido, **0 coincidencias**. Las dos apariciones de esos patrones
en el árbol son texto sobre los patrones —este doc y `06-auditar-reglas.sh`, cuyo
oficio es justamente cazar un token dentro de la URL de un remoto— y una lectura de
`os.environ["GITHUB_TOKEN"]`, que no contiene ningún valor.

Y la autenticación sigue sin escribir el secreto en ningún sitio: helper
`/home/user/.gh-credential` leyendo del único archivo que tiene el token, y remotos con
URL limpia. En la auditoría del 2026-11-08 hubo que limpiar 3 de 3 URLs con
`git remote set-url`; hoy `git remote get-url origin` sale sin token en los dos repos
trabajados.
