#!/usr/bin/env python3
"""Assemble la liste des sources d'une page à partir des fiches d'une verticale.

Entrée : un fichier HTML « source » dans lequel les appels de sources sont des jetons :
  {{S:<fiche>:<n>}}   source n° n de la fiche <fiche> (1 à 6 pour les axes, M pour methode.md, T pour tendances.md)
  {{C:<nn>}}          document du corpus [C-<PARTI>-nn] décrit dans 01-corpus.md
  {{CSS}}             contenu de la feuille de style recopié depuis la page gabarit (--gabarit) ; le jeton se place entre <style> et </style>
  {{HERO_SVG}}        dessin d'en-tête (bloc <svg class="hero-art">…</svg>) recopié depuis la page gabarit
  Plusieurs jetons collés ({{S:1:27}}{{S:1:62}}) forment un seul exposant « 27,62 ».
  Un jeton peut porter plusieurs numéros : {{S:1:27;62}}.
  Le bloc {{SOURCES}} est remplacé par la liste numérotée, groupée (corpus d'abord, puis par fiche).

Sortie : le fichier HTML final, où chaque jeton devient <sup><a href="#sN">N</a></sup> et où les
sources sont numérotées s1..sN dans l'ordre de première apparition, sans doublon d'URL.

Usage :
  python3 _scripts/assemble-sources.py --parti rn --prefixe C-RN --nom-parti "Rassemblement national" \
      --src 05-artifacts/sources/rn.src.html --gabarit 05-artifacts/renaissance.html --out 05-artifacts/rn.html
Le fichier source d'une page vit dans 05-artifacts/sources/<slug>.src.html ; la page publiée est la sortie.
"""
import argparse, re, pathlib, html, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FICHES = {"1": "1-finances-publiques.md", "2": "2-travail-protection-sociale.md", "3": "3-immigration.md",
          "4": "4-pouvoir-achat-fiscalite.md", "5": "5-securite-libertes.md", "6": "6-institutions-democratie-europe.md"}
GROUPES = {"C": "Programme, textes et déclarations du parti (sources du parti, partie prenante)",
           "1": "Axe 1, finances publiques et dette", "2": "Axe 2, travail, protection sociale et fraude",
           "3": "Axe 3, immigration", "4": "Axe 4, pouvoir d'achat et fiscalité",
           "5": "Axe 5, sécurité, ordre public et libertés", "6": "Axe 6, institutions, démocratie et Europe",
           "M": "Comment ils gouvernent", "T": "Carte des tendances"}
URL_RE = re.compile(r"https?://[^\s<>\]\)»]+")

def clean_url(u):
    return u.rstrip(".,;:")

PARTI_HOSTS = ("rassemblementnational.fr", "marinelepen.com", "assemblee-nationale.fr", "web.archive.org", "mlafrance.fr", "senat.fr")

def strip_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    return s.strip()

def parse_sources(path):
    """Liste numérotée après « ## Sources » : {n: texte}."""
    t = path.read_text(encoding="utf-8")
    if "## Sources" not in t:
        return {}
    sec = t.split("## Sources", 1)[1]
    out = {}
    for m in re.finditer(r"^(\d+)\.\s+(.*?)(?=\n\d+\.\s|\n## |\n### |\Z)", sec, re.S | re.M):
        out[int(m.group(1))] = " ".join(strip_md(m.group(2)).split())
    return out

def parse_corpus(path, prefixe):
    """Pour chaque identifiant du corpus : (titre, date, url)."""
    t = path.read_text(encoding="utf-8")
    out = {}
    # fiches longues « ### [C-XX-nn] Titre »
    for m in re.finditer(rf"^### \[{prefixe}-(\d+)\] (.+?)\n(.*?)(?=^### |^## |\Z)", t, re.S | re.M):
        n, titre, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        d = re.search(r"^- Date : (.+)$", body, re.M)
        u = re.search(r"^- URL : (.+)$", body, re.M)
        url = clean_url(URL_RE.search(u.group(1)).group(0)) if u and URL_RE.search(u.group(1)) else ""
        out[n] = (strip_md(titre), d.group(1).strip() if d else "", url)
    # fiches courtes « **[C-XX-nn] Libellé.** https://… »
    for m in re.finditer(rf"^- \*\*\[{prefixe}-(\d+)\] (.+?)\*\*\s*(\S+)?", t, re.M):
        n = int(m.group(1))
        if n in out:
            continue
        url = clean_url(m.group(3)) if m.group(3) and m.group(3).startswith("http") else ""
        out[n] = (strip_md(m.group(2)).rstrip("."), "", url)
    # lignes de tableau « | C-XX-nn | … »
    for m in re.finditer(rf"^\| {prefixe}-(\d+) \| (.+)$", t, re.M):
        n = int(m.group(1))
        cells = [c.strip() for c in m.group(2).strip("|").split("|")]
        url_m = URL_RE.search(m.group(2))
        url = clean_url(url_m.group(0)) if url_m else ""
        if n in out:
            if not out[n][2] and url:
                out[n] = (out[n][0], out[n][1], url)
            continue
        # tableaux : 2022 (Document | Date | …), textes (N° | Titre | signataire | Dépôt …), déclarations (Date | Média | Format | Axe | Position | URL)
        if re.match(r"\d{4}-\d{2}", cells[0]):
            titre = f"déclaration, {cells[1]}, {cells[4][:140]}" if len(cells) > 4 else cells[1]
            date = cells[0]
        elif cells[0].startswith(("PPL", "PPR", "PPLC", "Amdt")):
            titre = f"{cells[0]}, {cells[1]}"
            date = cells[3] if len(cells) > 3 else ""
        else:
            titre = cells[0]
            date = cells[1] if len(cells) > 1 else ""
        out[n] = (strip_md(titre), date, url)
    return out

def li(key, text, url):
    text = html.escape(text, quote=False)
    if url:
        return f'<li id="{key}"><a href="{html.escape(url)}">{text}</a></li>'
    return f'<li id="{key}">{text}</li>'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parti", required=True)
    ap.add_argument("--prefixe", required=True)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--nom-parti", default="Rassemblement national")
    ap.add_argument("--gabarit", help="page HTML dont on recopie le bloc <style> ({{CSS}}) et le dessin d'en-tête ({{HERO_SVG}})")
    a = ap.parse_args()
    base = ROOT / "02-partis" / a.parti
    fiches = {k: parse_sources(base / "axes" / v) for k, v in FICHES.items()}
    fiches["M"] = parse_sources(base / "methode.md")
    fiches["T"] = parse_sources(base / "tendances.md")
    corpus = parse_corpus(base / "01-corpus.md", a.prefixe)
    src = pathlib.Path(a.src).read_text(encoding="utf-8")
    if a.gabarit:
        g = pathlib.Path(a.gabarit).read_text(encoding="utf-8")
        css = re.search(r"<style>.*?</style>", g, re.S)
        hero = re.search(r'<svg class="hero-art".*?</svg>', g, re.S)
        if not css or not hero:
            sys.exit("gabarit : bloc <style> ou <svg class=\"hero-art\"> introuvable")
        # {{CSS}} est posé entre <style> et </style> dans la source : on insère le contenu seul, sans balises
        css_inner = re.sub(r"</?style>", "", css.group(0)).strip("\n")
        src = src.replace("{{CSS}}", css_inner).replace("{{HERO_SVG}}", hero.group(0))
    for jeton in ("{{CSS}}", "{{HERO_SVG}}"):
        if jeton in src:
            sys.exit(f"jeton {jeton} présent dans la source : passer --gabarit")

    order = []          # clés (groupe, n) dans l'ordre d'apparition
    numero = {}         # clé -> numéro de page
    by_url = {}         # url -> numéro (déduplication)
    entries = {}        # numéro -> (groupe, texte, url)
    problems = []

    def register(groupe, n):
        key = (groupe, n)
        if key in numero:
            return numero[key]
        if groupe == "C":
            if n not in corpus:
                problems.append(f"corpus {a.prefixe}-{n:02d} introuvable"); return None
            titre, date, url = corpus[n]
            relais = url and not any(h in url for h in PARTI_HOSTS)
            etiq = " [source du parti, partie prenante ; connue par un relais de presse]" if relais else " [source du parti, partie prenante]"
            text = f"{a.nom_parti}, {titre}" + (f", {date}" if date else "") + etiq
        else:
            if n not in fiches.get(groupe, {}):
                problems.append(f"source {groupe}:{n} introuvable"); return None
            raw = fiches[groupe][n]
            um = URL_RE.search(raw)
            url = clean_url(um.group(0)) if um else ""
            text = URL_RE.sub("", raw).replace(" . ", " ").replace(" ; ;", " ;").strip() if um else raw
            text = re.sub(r"\s*;\s*(?=[\.\[]|$)", "", text)
            text = re.sub(r"\s+\.\s*$", ".", text)
            text = re.sub(r"\s{2,}", " ", text).strip(" .;") + "."
        if url and url in by_url:
            numero[key] = by_url[url]
            return by_url[url]
        num = len(entries) + 1
        numero[key] = num
        entries[num] = (groupe, text, url)
        if url:
            by_url[url] = num
        order.append(key)
        return num

    def repl(m):
        groupe, nums = m.group(1), m.group(2)
        out = []
        for n in nums.split(";"):
            num = register(groupe, int(n))
            if num:
                out.append(f'<a href="#s{num}">{num}</a>')
        return "\x00" + ",".join(out) + "\x01"

    # normalise {{S:k:n}} -> {{k:n}} ; {{C:n}} reste tel quel
    src = re.sub(r"\{\{S:([1-6MT]):(\d+(?:;\d+)*)\}\}", lambda m: "{{" + m.group(1) + ":" + m.group(2) + "}}", src)
    body = re.sub(r"\{\{([C1-6MT]):(\d+(?:;\d+)*)\}\}", repl, src)
    # fusion des exposants adjacents
    body = re.sub(r"\x01\s*\x00", ",", body)
    body = body.replace("\x00", "<sup>").replace("\x01", "</sup>")

    # liste des sources, groupée dans l'ordre : corpus, 1..6, M, T, mais numérotation globale conservée
    parts = []
    for g in ["C", "1", "2", "3", "4", "5", "6", "M", "T"]:
        nums = sorted(num for num, (gg, _, _) in entries.items() if gg == g)
        if not nums:
            continue
        parts.append(f'<p class="srcg">{GROUPES[g]}</p>')
        # une seule <ol> continue par groupe, avec start pour garder la numérotation globale
        chunks = []
        start = nums[0]
        prev = None
        for num in nums:
            if prev is not None and num != prev + 1:
                chunks.append((start, prev))
                start = num
            prev = num
        chunks.append((start, prev))
        for s, e in chunks:
            parts.append(f'<ol class="sources" start="{s}">')
            for num in range(s, e + 1):
                gg, text, url = entries[num]
                parts.append(li(f"s{num}", text, url))
            parts.append("</ol>")
    body = body.replace("{{SOURCES}}", "\n".join(parts))
    pathlib.Path(a.out).write_text(body, encoding="utf-8")
    print(f"{len(entries)} sources, {len(problems)} problèmes")
    for p in problems:
        print("  !", p)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
