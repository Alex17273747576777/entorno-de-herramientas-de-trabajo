#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vara_bandita.py — VARA EJECUTABLE del Manual de La Bandita v0.0.1
Convierte reglas que antes eran adorno en COMPUERTAS verificables.

Uso:   python3 vara_bandita.py PIEZA.md [--meta-min 45001] [--tope-max 63000]
       python3 vara_bandita.py NORMA.md --modo-norma
Salida: reporte por categoría + veredicto VERDE / VENTANA / ROJO.
Exit:   0 = VERDE (lista) · 1 = ROJO (faltas graves) · 2 = VENTANA (avisos).

La vara solo comprueba condiciones deterministas; nunca redacta ni reescribe.
El modo público es estricto: las citas no eximen una fórmula vetada. En
--modo-norma, solo se aíslan menciones pedagógicas delimitadas explícitamente
con VARA:MENCION:INICIO / VARA:MENCION:FIN. Un VERDE no prueba la verdad factual.

Principio: la vara muerde primero a quien la sostiene. Se auto-testea contra
cualquier pieza, incluidas las del propio operador. Si no abre el enlace, no cita;
si la compuerta falla, la pieza no sale.
"""
import sys, re

FRASES_PROHIBIDAS = [
    "la mejor para todos","imprescindible","100% segura","100 % segura","totalmente segura",
    "todo el mundo sabe","ultimas 24 horas","últimas 24 horas","no te lo pierdas",
    "descargalo ya","descárgalo ya","el unico que necesitas","el único que necesitas",
    "revolucionario","revolucionaria","unico en su clase","único en su clase",
    "sin precedentes","el futuro es ahora","game changer","la navaja suiza de",
    "el santo grial de","mata a todos sus competidores","nadie te cuenta esto",
    "lo que no quieren que sepas","segun expertos","según expertos",
]
SUPERLATIVOS_ABSOLUTOS = [
    r"\bla mejor\b", r"\bel mejor\b", r"\blas mejores\b(?!\s+pr[aá]cticas)",
    r"\blos mejores\b", r"\bimperdible\b", r"\bel unico\b", r"\bel único\b",
]
AUTORIDAD_VACIA = ["según expertos","segun expertos","todo el mundo sabe",
    "nadie te cuenta","lo que no quieren que sepas"]
META_COMENTARIOS = ["como ia","como inteligencia artificial","aquí va un dato",
    "aqui va un dato","procedo a","en esta sección vamos","en esta seccion vamos",
    "como modelo de lenguaje"]
PROMESAS_INCUMPLIBLES = ["te avisare cuando","te avisaré cuando","te aviso cuando salga",
    "no te lo pierdas","descargalo ya","descárgalo ya"]
FIRMA_TEXTUAL = "La Bandita informa a partir de fuentes fechadas"
LEMA_IDENTIDAD = "las estrellas adornan"

def normal(s): return re.sub(r"\s+", " ", s.lower().replace("\u00a0", " ")).strip()

MARCA_MENCION_INICIO = "<!-- VARA:MENCION:INICIO -->"
MARCA_MENCION_FIN = "<!-- VARA:MENCION:FIN -->"
PATRON_MENCION = re.compile(re.escape(MARCA_MENCION_INICIO) + r".*?" +
                           re.escape(MARCA_MENCION_FIN), re.S)


def _enmascarar_menciones(txt):
    """En modo norma excluye solo bloques explícitos; conserva líneas para reportes."""
    inicios = txt.count(MARCA_MENCION_INICIO)
    finales = txt.count(MARCA_MENCION_FIN)
    bloques = list(PATRON_MENCION.finditer(txt))
    if inicios != finales or len(bloques) != inicios:
        return txt, 0, ("Marcadores VARA:MENCION mal formados: deben estar balanceados, "
                        "sin anidamiento y en pares INICIO/FIN.")

    def conservar_saltos(match):
        return "".join("\n" if c == "\n" else " " for c in match.group(0))

    enmascarado = PATRON_MENCION.sub(conservar_saltos, txt)
    return enmascarado, len(bloques), None


def comprobar_cierre(txt):
    """Comprueba orden textual; no decide si el meme o los créditos son buenos."""
    errores = []
    lineas = txt.splitlines()

    def limpia(linea):
        return re.sub(r"^[>\s]+", "", linea).strip().strip("*_ ")

    firmas = [i for i, l in enumerate(lineas)
              if limpia(l) == FIRMA_TEXTUAL + "."]
    if len(firmas) != 1:
        return ["Cierre: se exige una sola firma exacta, con punto final y en línea propia."]
    firma = firmas[0]
    encabezados = [(i, l) for i, l in enumerate(lineas) if re.match(r"^#{1,6}\s+", l)]
    creditos = [i for i, l in encabezados
                if re.match(r"^#{1,6}\s+(?:[^\w\s]+\s*)?(?:Créditos|Credits)\s*$", l, re.I)]
    if len(creditos) != 1:
        return ["Cierre: se exige una sola sección Créditos (Credits en inglés)."]
    credito = creditos[0]
    if credito <= firma or (encabezados and encabezados[-1][0] != credito):
        errores.append("Cierre: Créditos debe ir después de firma/remate y ser la última sección.")
    # El meme es el bloque inmediatamente anterior a la firma, no una lista del cuerpo.
    antes = firma - 1
    while antes >= 0 and not lineas[antes].strip():
        antes -= 1
    dialogos = 0
    while antes >= 0 and re.match(r"^\s*(?:>\s*)?[—–]\s*\S", lineas[antes]):
        dialogos += 1
        antes -= 1
    if dialogos not in (2, 3):
        errores.append("Cierre: meme de dos o tres líneas de diálogo inmediatamente antes de la firma.")
    remate = [l for l in lineas[firma + 1:credito] if l.strip() and l.strip() not in ("---", "***")]
    if not 1 <= len(remate) <= 3 or any(re.match(r"^#{1,6}\s+", l) for l in remate):
        errores.append("Cierre: remate de una a tres líneas entre firma y Créditos, sin secciones intermedias.")
    bloque = "\n".join(lineas[credito + 1:])
    if "Arena AI" not in bloque or "Alex17273747576777" not in bloque:
        errores.append("Cierre: faltan los dos créditos canónicos dentro de Créditos.")
    elif bloque.rfind("Arena AI") > bloque.rfind("Alex17273747576777"):
        errores.append("Cierre: Arena AI precede al crédito final Alex17273747576777.")
    no_vacias = [l for l in lineas if l.strip()]
    if not no_vacias or "Alex17273747576777" not in no_vacias[-1]:
        errores.append("Cierre: la última línea no vacía debe ser el crédito del dueño.")
    return errores


def auditar(path, meta_min=45001, tope_max=63000, modo_norma=False):
    with open(path, encoding="utf-8") as archivo:
        txt = archivo.read()
    n = len(txt)
    res = {"rojo":[], "amarillo":[], "info":[]}
    texto_revision = txt
    menciones = 0
    if modo_norma:
        texto_revision, menciones, error_marcadores = _enmascarar_menciones(txt)
        if error_marcadores:
            res["rojo"].append(error_marcadores)
        elif menciones:
            res["info"].append(f"Menciones pedagógicas aisladas explícitamente: {menciones} bloque(s).")
    elif MARCA_MENCION_INICIO in txt or MARCA_MENCION_FIN in txt:
        res["rojo"].append("Marcadores VARA:MENCION no se permiten como exención en una pieza pública.")
    lines = texto_revision.split("\n")

    # R1 frases prohibidas (ROJO)
    for i,l in enumerate(lines,1):
        low = normal(l)
        for p in FRASES_PROHIBIDAS:
            if p in low: res["rojo"].append(f"L{i} frase prohibida «{p}»: {l.strip()[:70]}")
    # R2 autoridad vacia (ROJO)
    for i,l in enumerate(lines,1):
        low = normal(l)
        for p in AUTORIDAD_VACIA:
            if p in low:
                res["rojo"].append(f"L{i} autoridad vacía «{p}»: {l.strip()[:70]}")
    # R3 meta-comentarios de proceso / ocultacion de IA (ROJO)
    for i,l in enumerate(lines,1):
        low = normal(l)
        for p in META_COMENTARIOS:
            if p in low: res["rojo"].append(f"L{i} meta-comentario «{p}»: {l.strip()[:70]}")
    # R4 promesas incumplibles (ROJO)
    for i,l in enumerate(lines,1):
        low = normal(l)
        for p in PROMESAS_INCUMPLIBLES:
            if p in low: res["rojo"].append(f"L{i} promesa incumplible «{p}»: {l.strip()[:70]}")
    # R5 superlativos absolutos comerciales (AMARILLO: requieren criterio declarado)
    for i,l in enumerate(lines,1):
        low = normal(l)
        for rg in SUPERLATIVOS_ABSOLUTOS:
            for m in re.finditer(rg, low):
                ctx = l.strip()[:70]
                salvo = ("a juicio" in low or "en nuestra lectura" in low or
                         "segun su" in low or "según su" in low or "en el corte" in low)
                tag = "amarillo" if not salvo else "info"
                res[tag].append(f"L{i} superlativo «{m.group(0)}» {'(sin criterio declarado)' if not salvo else '(con criterio)'}: {ctx}")
    # E1 firma textual obligatoria
    if FIRMA_TEXTUAL not in txt:
        res["amarillo"].append("Falta la firma textual obligatoria: «La Bandita informa a partir de fuentes fechadas»")
    else:
        res["info"].append("Firma textual presente.")
    if LEMA_IDENTIDAD in txt.lower():
        res["info"].append("Lema identitario presente (las estrellas adornan…).")
    # E2 meme del corte (dos líneas con raya de diálogo)
    meme = re.findall(r"^\s*(?:>\s*)?[—–]\s*\S.*$", txt, flags=re.M)
    if len(meme) < 2:
        res["amarillo"].append("No se detecta meme del corte (esperadas >=2 líneas de diálogo con —).")
    else:
        res["info"].append(f"Meme del corte detectado ({len(meme)} líneas de diálogo).")
    # E3 notas al pie (solo exigibles si hubo mudanza/corte/correccion declarada)
    if ("mudanza" in txt.lower() or "corte" in txt.lower() or "correccion" in txt.lower()
            or "corrección" in txt.lower()) and "notas al pie" not in txt.lower():
        res["amarillo"].append("Se mencionan mudanza/corte/corrección pero no hay sección «Notas al pie».")
    # M1 conteo de caracteres (meta de sustentación y tope sanitario)
    if n < meta_min:
        res["amarillo"].append(f"Caracteres {n:,} por debajo de la meta de sustentación {meta_min:,}. Ampliar con SUSTANCIA verificada, nunca relleno.")
    elif n > tope_max:
        res["amarillo"].append(f"Caracteres {n:,} sobre el tope sanitario {tope_max:,}. Prever despliegue fragmentado por red.")
    else:
        res["info"].append(f"Caracteres {n:,}: dentro de banda [{meta_min:,}–{tope_max:,}].")
    # Cierre obligatorio del maestro; las normas no son piezas públicas.
    if not modo_norma:
        res["rojo"].extend(comprobar_cierre(txt))
    # veredicto
    if res["rojo"]: verd = "ROJO"; code = 1
    elif res["amarillo"]: verd = "VENTANA"; code = 2
    else: verd = "VERDE"; code = 0
    return txt, n, res, verd, code

def main(argv):
    raw = argv[1:]
    args = [a for a in raw if not a.startswith("--")]
    modo_norma = "--modo-norma" in raw
    opts = dict(re.findall(r"--([\w-]+)\s+(\d+)", " ".join(argv)))
    if not args:
        print(__doc__); return 1
    path = args[0]
    meta_min = int(opts.get("meta-min", 45001)); tope_max = int(opts.get("tope-max", 63000))
    if modo_norma:
        meta_min = 0; tope_max = 10**9
    _, n, res, verd, code = auditar(path, meta_min, tope_max, modo_norma=modo_norma)
    # En modo norma, los checks de estructura de PIEZA (firma/meme/notas/banda) no aplican a un documento normativo.
    if modo_norma:
        prefijos_estructura = ("Falta la firma", "No se detecta meme", "Se mencionan mudanza",
                               "Caracteres ", "Lema identitario", "Meme del corte")
        for k in ("rojo", "amarillo", "info"):
            res[k] = [m for m in res[k] if not m.startswith(prefijos_estructura)]
        verd = "ROJO" if res["rojo"] else ("VENTANA" if res["amarillo"] else "VERDE")
        code = 1 if res["rojo"] else (2 if res["amarillo"] else 0)
    print("="*64)
    titulo_modo = " · MODO NORMA (documento normativo)" if modo_norma else ""
    print(f"VARA BANDITA v0.0.1 · {path}{titulo_modo}")
    print(f"caracteres: {n:,}")
    print("-"*64)
    for k,tit in (("rojo","GRAVES (bloquean)"),("amarillo","AVISOS (ventana)"),("info","OK")):
        if res[k]:
            print(f"[{tit}] x{len(res[k])}")
            for m in res[k][:40]: print("   -", m)
    print("="*64)
    print(f"VEREDICTO: {verd}")
    return code

if __name__ == "__main__":
    sys.exit(main(sys.argv))
