# Suite Adobe → código abierto — guía curada y medida

*Armada el 2026-11-14 a partir de las apps que salen en tu captura de Adobe Creative Cloud
(Photoshop, Illustrator, Firefly/Firefly Boards, Acrobat, Premiere, Express, InDesign,
Lightroom, Adobe Fonts y Adobe Stock), cruzadas con [fmhy.net/image-tools](https://fmhy.net/image-tools)
y **verificadas una por una contra la API de GitHub/GitLab el mismo día**.*

> **Nota honesta:** FMHY es un índice comunitario enorme y en sus listas mezcla código abierto con
> propietario sin marcarlo (Affinity, Paint.net, Photopea y Pixlr aparecen junto a GIMP). Esta guía
> aplica un filtro propio: **sólo entra software con licencia abierta comprobada en su repositorio**.
> Las estrellas (★) y las fechas de último cambio no son de memoria: se midieron hoy contra la API.
> Donde GitHub no tiene el repo canónico (Inkscape, digiKam), se midió en su GitLab real.

Leyenda: ⭐ = la recomendación principal de cada categoría · 🟢 vivo (último empujón ≤ 90 días) ·
🟡 en mantenimiento (usable, pero con poco movimiento) · 🪞 el GitHub es un espejo; el desarrollo vive en otro lado.

---

## 0. Tabla maestra (empieza aquí)

| App de Adobe (tu captura) | Alternativa abierta ⭐ | Licencia (leída en el repo) | ★ | Último empujón | Estado |
|---|---|---|--:|---|---|
| **Photoshop** | GIMP (+ parche PhotoGIMP) | GPL-3.0 | 6.585 | 2026-11-14 (hoy) | 🟢 |
| **Illustrator** | Inkscape | GPL-2.0+ (binarios GPL-3.0+) | 4.027 (GitLab) | 2026-11-14 (hoy) | 🟢 |
| **Firefly / Firefly Boards** | ComfyUI | GPL-3.0 | 146.837 | 2026-11-14 (hoy) | 🟢 |
| **Acrobat** | Stirling-PDF | MIT | 96.594 | 2026-11-14 (hoy) | 🟢 |
| **Premiere** | Kdenlive | GPL-3.0 | 6.108 | 2026-11-14 (hoy) | 🟢 |
| **Adobe Express** | Penpot | MPL-2.0 | 62.357 | 2026-11-14 (hoy) | 🟢 |
| **InDesign** | Scribus | GPL-2.0+ | 657 (espejo sincronizado) | 2026-11-14 (hoy) | 🟢 |
| **Lightroom** | darktable | GPL-3.0 | 13.446 | 2026-11-14 (hoy) | 🟢 |
| **Adobe Fonts** | catálogo Google Fonts | OFL por familia | 20.765 | 2026-11-14 (hoy) | 🟢 |
| **Adobe Stock** | Openverse | MIT | 643 | 2026-11-14 (hoy) | 🟢 |

---

## 1. Photoshop → GIMP ⭐

En tu captura: *«Create beautiful graphics, photos and art anywhere.»*

- ⭐ **[GIMP](https://www.gimp.org/)** — [GNOME/gimp](https://github.com/GNOME/gimp) — ★6.585 · GPL-3.0 (su `COPYING` es la GPL v3) · empujado **hoy**. El reemplazo abierto más completo: capas, máscaras, curvas, canales, plugins y scripts. FMHY lo marca con ⭐ en *Editing Software*.
- **[PhotoGIMP](https://github.com/Diolinux/PhotoGIMP)** — ★18.556 · GPL-3.0 · 2026-10-25 (hace 20 d) 🟢. No es otro editor: es un parche que deja GIMP con la interfaz, los iconos y **los atajos de Photoshop**. Instálalo encima de GIMP y la migración duele la mitad.
- **[PhotoCraft](https://github.com/storytold/photocraft)** — ★79.407 · Apache-2.0 · creado el 2026-09-30 y empujado **hoy** 🟢. La novedad: editor escrito desde cero en Rust puro que abre y guarda **PSD reales** (capas, máscaras, capas de ajuste, estilos, vectores). Aún es joven: úsalo como segundo editor, no como único.
- **[Krita](https://krita.org/)** — [KDE/krita](https://github.com/KDE/krita) — ★10.745 · GPL-3.0 · **hoy** 🟢. Si tu Photoshop es sobre todo pintar e ilustrar, Krita lo supera en pinceles.
- **[PhotoDemon](https://photodemon.org/)** — [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon) — ★2.430 · licencia tipo BSD (su `LICENSE.md`) · 2026-11-09 🟢. Windows, portátil (un solo exe), edición no destructiva y macros.
- **[miniPaint](https://viliusle.github.io/miniPaint/)** — [viliusle/miniPaint](https://github.com/viliusle/miniPaint) — ★3.498 · MIT (`MIT-LICENSE.txt`) · 2026-11-09 🟢. En el navegador, sin instalar nada.
- Menores pero vivos: **[LazPaint](https://lazpaint.github.io/)** (★557 · GPL-3.0 · ayer) y **[Pixelitor](https://pixelitor.sourceforge.net/)** (★268 · GPL-3.0 · hace 7 d), ambos 🟢.

**Empieza por:** GIMP + PhotoGIMP el mismo día.

## 2. Illustrator → Inkscape ⭐

En tu captura: *«Create stunning illustrations and graphics.»*

- ⭐ **[Inkscape](https://inkscape.org/)** — [GitLab inkscape/inkscape](https://gitlab.com/inkscape/inkscape) — ★4.027 en GitLab · GPL-2.0+ en el código y GPL-3.0+ en los binarios (su `COPYING` lo dice) · actividad **hoy** 🟢. Vectorial completo: Bézier, nodos, tipografía en trazados, SVG nativo, exportación a PDF/EPS. **Ojo:** su repo de GitHub está parado desde 2022 porque es un espejo viejo; el desarrollo real vive en GitLab.
- **[Graphite](https://graphite.art/)** — [GraphiteEditor/Graphite](https://github.com/GraphiteEditor/Graphite) — ★27.938 · Apache-2.0 · **hoy** 🟢. Editor vectorial moderno (Rust + web) con diseño procedural por nodos. La apuesta nueva de la categoría.

**Empieza por:** Inkscape estable desde inkscape.org; Graphite si quieres probar lo nuevo en el navegador.

## 3. Adobe Firefly y Firefly Boards → ComfyUI ⭐

En tu captura: *«Ideate, generate, create, share on Adobe Firefly»* y el tablero *«Visualize and refine new ideas in Firefly Boards»*.

- ⭐ **[ComfyUI](https://www.comfyui.com/)** — [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — ★146.837 · GPL-3.0 · **hoy** 🟢. Generación por nodos: el estándar abierto para Stable Diffusion, Flux y compañía. (El repo cambió de org en 2025: antes era `comfyanonymous/ComfyUI`; el redirect sigue vivo.)
- **[InvokeAI](https://invoke-ai.github.io/InvokeAI/)** — [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) — ★29.093 · Apache-2.0 · **hoy** 🟢. La interfaz más pulida: inpainting, outpainting y tablero de lienszo unificado.
- **[Krita + plugin AI Diffusion](https://github.com/Acly/krita-ai-diffusion)** — ★10.899 · GPL-3.0 · 2026-11-06 🟢. Generar y retocar con IA **dentro del pincel**, como el relleno generativo de Photoshop/Firefly.
- **[stable-diffusion-webui (A1111)](https://github.com/AUTOMATIC1111/stable-diffusion-webui)** — ★165.313 · AGPL-3.0 · 2026-03-02 🟡. El clásico con más extensions, pero en mantenimiento: ocho meses sin empujón.
- Casi parados, citados por honestidad: **[Fooocus](https://github.com/lllyasviel/Fooocus)** (★53.930 · GPL-3.0 · 2025-12-01 🟡) y **[Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)** (★13.126 · AGPL-3.0 · 2025-07-31 🟡).

> **Nota honesta:** Firefly presume modelos «entrenados éticamente» con contenido licenciado. Los modelos
> abiertos (SDXL, Flux, etc.) tienen licencias propias y distintas entre sí: **revísala antes de uso comercial**.
> Y Firefly Boards (moodboard colaborativo con IA) no tiene clon abierto exacto; lo más cercano es un tablero
> de Penpot (§6) alimentado con salidas de ComfyUI.

**Empieza por:** InvokeAI si vienes de clic-y-listo; ComfyUI cuando quieras controlar el flujo.

## 4. Acrobat → Stirling-PDF ⭐

En tu captura: *«View, share, or comment on PDFs for free.»*

- ⭐ **[Stirling-PDF](https://www.stirlingpdf.com/)** — [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) — ★96.594 · **MIT** (su `LICENSE`, pese a que GitHub marque NOASSERTION) · **hoy** 🟢. Navaja suiza del PDF servida en local: unir, dividir, rotar, comprimir, firmar, marca de agua, OCR, converter a/de todo.
- **[OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF)** — ★35.316 · MPL-2.0 · **hoy** 🟢. Convierte PDFs escaneados en PDFs con texto buscable, por línea de comandos o carpeta vigilada.
- **[Xournal++](https://xournalpp.github.io/)** — [xournalpp/xournalpp](https://github.com/xournalpp/xournalpp) — ★15.679 · GPL-2.0 · **hoy** 🟢. Anotar, subrayar y **firmar a mano** sobre el PDF, con lápiz o mouse.
- **[pdfarranger](https://github.com/pdfarranger/pdfarranger)** — ★6.052 · GPL-3.0 · ayer 🟢. Reordenar, recortar y unir páginas arrastrando, sin salir de la ventanita.

**Empieza por:** Stirling-PDF en su versión de escritorio (o Docker si prefieres servirla en casa).

## 5. Premiere → Kdenlive ⭐

En tu captura: *«Edit and craft polished films and video.»*

- ⭐ **[Kdenlive](https://kdenlive.org/)** — [KDE/kdenlive](https://github.com/KDE/kdenlive) — ★6.108 · GPL-3.0 · **hoy** 🟢 (espejo de GitHub sincronizado con el GitLab de KDE). Multicámara, proxies para máquinas modestas, keyframes, mezcla de audio y títulos.
- **[Shotcut](https://shotcut.org/)** — [mltframework/shotcut](https://github.com/mltframework/shotcut) — ★15.680 · GPL-3.0 · **hoy** 🟢. Traga cualquier formato vía FFmpeg; curva de entrada suave.
- **[OpenShot](https://www.openshot.org/)** — [OpenShot/openshot-qt](https://github.com/OpenShot/openshot-qt) — ★6.784 · GPL-3.0 (su `COPYING` en la rama `develop`) · **hoy** 🟢. El más simple de los tres: para cortar y publicar sin pelear.

**Empieza por:** Kdenlive si editas en serio; OpenShot si sólo quieres recortar y subir.

## 6. Adobe Express → Penpot ⭐

En tu captura: *«Create standout social posts, flyers, videos, and more in minutes.»*

- ⭐ **[Penpot](https://penpot.app/)** — [penpot/penpot](https://github.com/penpot/penpot) — ★62.357 · MPL-2.0 · **hoy** 🟢. Diseño y prototipado abierto (el rival libre de Figma), SVG nativo, auto-hosteable, con librerías de componentes compartibles para el equipo.

> **Nota honesta:** el corazón de Express es su **catálogo de plantillas cerradas**; no existe un clon abierto
> con ese catálogo. El stack abierto equivalente: Penpot para componer + GIMP para la foto + Scribus (§7) si
> acaba impreso. Las plantillas se consiguen en librerías comunitarias de Penpot o se hacen una vez y se reusan.

## 7. InDesign → Scribus ⭐

En tu captura: *«Design and publish professional print and digital layouts.»*

- ⭐ **[Scribus](https://www.scribus.net/)** — [scribusproject/scribus](https://github.com/scribusproject/scribus) — espejo de GitHub ★657 empujado **hoy** 🟢 (el proyecto publica también desde SourceForge) · GPL-2.0+ (su `COPYING`: «version 2 of the License, or any later version»). Maquetación de verdad: CMYK, perfiles ICC, exportación PDF/X-1a para imprenta, páginas maestras, estilos enlazados.

**Empieza por:** la rama estable de scribus.net; para folletos y revistas es sustituto directo.

## 8. Lightroom → darktable ⭐

En tu captura: *«Edit, organize, and share photos across desktop, mobile, and web.»*

- ⭐ **[darktable](https://www.darktable.org/)** — [darktable-org/darktable](https://github.com/darktable-org/darktable) — ★13.446 · GPL-3.0 · **hoy** 🟢. Cuarto oscuro RAW no destructivo + mesa de luz: es la alternativa abierta canónica a Lightroom (no a Photoshop).
- **[RawTherapee](https://rawtherapee.com/)** — [RawTherapee/RawTherapee](https://github.com/RawTherapee/RawTherapee) — ★4.296 · GPL-3.0 · 2026-11-09 🟢. Más control crudo del RAW; menos gestión de colección.
- **[digiKam](https://www.digikam.org/)** — 🪞 su GitHub murió en 2019, pero en el [GitLab de KDE](https://invent.kde.org/graphics/digikam) hay actividad **hoy** · GPL-2.0. La mitad «biblioteca» de Lightroom: catalogar, etiquetar caras, metadatos, álbumes.

**Empieza por:** darktable para revelar + digiKam para ordenar el archivo.

## 9. Adobe Fonts → catálogo Google Fonts ⭐

En tu captura: *«Thousands of fonts to explore and use in any application.»*

- ⭐ **[Google Fonts](https://fonts.google.com/)** — [google/fonts](https://github.com/google/fonts) — ★20.765 · empujado **hoy** 🟢. Miles de familias con licencia abierta (casi todas OFL: uso comercial permitido). El repo es el catálogo completo versionado.
- **[Fontsource](https://fontsource.org/)** — [fontsource/fontsource](https://github.com/fontsource/fontsource) — ★6.285 · MIT · 2026-11-09 🟢. Las mismas fuentes abiertas **auto-alojadas** vía npm: sin rastreo de terceros en tu web.
- **[FontForge](https://fontforge.org/)** — [fontforge/fontforge](https://github.com/fontforge/fontforge) — ★8.084 · GPL-3.0 (`COPYING.gplv3`) · **hoy** 🟢. Crear y editar fuentes: lo que Adobe Fonts no te deja hacer nunca.
- **[Font Manager](https://github.com/FontManager/font-manager)** — ★1.103 · GPL-3.0 · 2026-11-12 🟢. Instalar, agrupar y previsualizar familias en el escritorio (el «sync» local que hacía Typekit).

> **Nota honesta:** Adobe Fonts es un **servicio de licenciamiento y sincronización**, no software. Su
> equivalente abierto no es una app sino un circuito: catálogo OFL → descarga/auto-alojamiento → gestión local.

## 10. Adobe Stock → Openverse ⭐

En tu captura: *«Find the perfect image for your creative project.»*

- ⭐ **[Openverse](https://openverse.org/)** — [WordPress/openverse](https://github.com/WordPress/openverse) — ★643 · MIT · **hoy** 🟢. Buscador de código abierto sobre cientos de millones de obras con licencias Creative Commons, con filtro por licencia y atribución lista para copiar.
- **[Wikimedia Commons](https://commons.wikimedia.org/)** — más de 100 millones de archivos libres, con su propio buscador de licencias.

> **Nota honesta:** aquí «abierto» significa **licencia abierta del contenido**, no del sitio. Creative Commons
> no es una sola licencia: las variantes NC (no comercial) y ND (sin derivados) limitan el uso. Filtra y lee.

---

## 11. Rutas de migración por perfil

- **Retocador que vive en Photoshop:** GIMP + PhotoGIMP (§1). Si tu día a día son PSD de cliente, prueba PhotoCraft como visor/editor ligero de PSD.
- **Fotógrafo:** darktable + digiKam (§8); RawTherapee si darktable se te queda corto en RAW puro.
- **Editor de video:** Kdenlive (§5); OpenShot para cortes rápidos.
- **Diseñador gráfico / imprenta:** Inkscape + Scribus + Penpot (§2, §7, §6).
- **Generativo / IA:** InvokeAI para empezar, ComfyUI cuando quieras nodos (§3).
- **Oficina de PDF:** Stirling-PDF + OCRmyPDF + Xournal++ (§4).

## 12. Lo que NO es código abierto (sale en toda comparativa y no aplica aquí)

**DaVinci Resolve** (gratis, cerrado) · **Affinity** (pago, cerrado) · **Photopea** (web gratis, cerrada) ·
**Canva** (freemium, cerrado) · **Pixlr** y **Fotor** (freemium, cerrados) · **Paint.net** (freeware cerrado) ·
**Figma** (cerrado). Si el criterio es licencia abierta, quedan fuera aunque sean gratis.

## 13. Cómo se midió cada número

- Fecha de corte: **2026-11-14**, hora local de Santo Domingo (UTC-4).
- GitHub API: `GET /repos/{owner}/{repo}` → `stargazers_count`, `pushed_at`, `created_at`; y el fichero de licencia real del repo (`LICENSE`, `COPYING`, `MIT-LICENSE.txt`…) cuando el campo `license.spdx_id` daba `NOASSERTION` o el repo no estaba en GitHub.
- GitLab API para lo que no vive en GitHub: `gitlab.com` (Inkscape) e `invent.kde.org` (digiKam).
- Regla de estado: 🟢 vivo = último empujón ≤ 90 días; 🟡 mantenimiento = más de 90 días pero usable; 🪞 = el GitHub es espejo y se midió el repo canónico.
- Cambios de org detectados al medir: ComfyUI (`comfyanonymous` → `Comfy-Org`) e InvokeAI (`invoke-ai`). Sin redirect habrían parecido muertos: **no lo están**.
- Las ★ se escriben con punto de miles al estilo de la casa (★79.407 = setenta y nueve mil).

## 14. Dónde ver esto en FMHY

- [fmhy.net/image-tools](https://fmhy.net/image-tools) — lista GIMP, Krita, Inkscape, miniPaint, Pinta, Graphite, LazPaint, PhotoDemon y más… **mezclados con propietarios**; el filtro abierto de esta guía es el que separa.
- [fmhy.net/video-tools](https://fmhy.net/video-tools) — sección de editores de video (Kdenlive/Shotcut/OpenShot aparecen en el ecosistema FMHY).
- [fmhy.net/text-tools](https://fmhy.net/text-tools) — herramientas de texto/PDF y tipografía.

FMHY indexa; **no certifica licencias ni vigencia**. Para eso está la tabla del §0, medida hoy.

---

*Guia hermana: [guia-programacion-de-novato-a-experto.md](guia-programacion-de-novato-a-experto.md) (misma casa, mismo método).*
