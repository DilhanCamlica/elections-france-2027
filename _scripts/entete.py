#!/usr/bin/env python3
"""En-tête commun des pages de la série « Lecture » (décision de Dilhan du 2026-10-30).

Transforme l'en-tête d'une page (fichier source à jetons `sources/<slug>.src.html`, ou page
assemblée sans source comme `renaissance.html`) :
  surtitre en bas de casse qui nomme la force ; titre ; empreinte des 24 verdicts (SVG produit
  depuis les pastilles de la grille) ; ligne de résultat comptée depuis la grille, de structure
  identique pour les cinq forces ; la grille tout de suite ; sous la grille, la durée de lecture
  et les liens vers les chapitres, puis « Comment lire cette page » replié (ancienne règle du jeu
  et base du verdict de cohérence) ; les citations « dans leurs mots » après la grille.
Le dessin d'en-tête générique est retiré. Le CSS de l'en-tête est inséré après {{CSS}} (source)
ou avant </style> (page assemblée), entre des marqueurs, de façon idempotente.

Usage :
  python3 _scripts/entete.py --page 05-artifacts/sources/rn.src.html --force "le RN" --non-gouverne
  python3 _scripts/entete.py --page 05-artifacts/renaissance.html --force "Renaissance" --actes "2017-2026"
  python3 _scripts/entete.py --synthese 05-artifacts/sources/synthese.src.html
"""
import argparse, re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK_A, MARK_B = "/* entete-commun:debut */", "/* entete-commun:fin */"
CSS = MARK_A + """
.hero{padding:1.6rem 0 .25rem;gap:.9rem}
.hero-top{display:grid;gap:1rem;align-items:center}
@media (min-width:600px){.hero-top{grid-template-columns:minmax(0,1fr) auto}}
.eyebrow2{display:block;font-family:var(--sans);font-size:.86rem;color:var(--muted);margin-bottom:.45rem}
.lede{font-size:1.02rem;line-height:1.5;margin:0;color:var(--ink);max-width:44rem}
.imprint{width:8rem;height:auto;display:block;justify-self:start}
@media (min-width:600px){.imprint{width:9rem;justify-self:end}}
.imprints{display:flex;flex-wrap:wrap;gap:.9rem 1.4rem;margin:.2rem 0 .4rem}
.imprints figure{margin:0;display:grid;gap:.25rem;justify-items:center}
.imprints svg{width:5.6rem;height:auto}
.imprints figcaption{font-family:var(--sans);font-size:.74rem;color:var(--muted)}
.path{margin-top:1.1rem;padding-top:1rem;border-top:2px solid var(--line)}
.ptime{font-size:.88rem;color:var(--muted);margin:0 0 .5rem}
.chips{display:flex;flex-wrap:wrap;gap:.4rem}
.chips a{font-size:.8rem;padding:.3rem .65rem;border-radius:999px;border:1px solid var(--line);background:var(--bg);text-decoration:none;color:var(--ink)}
.chips a:hover{border-color:var(--accent);color:var(--accent)}
details.lire{margin-top:.6rem;border-top:0}
details.lire summary{font-weight:500;font-size:.92rem;color:var(--muted);padding:.6rem 0}
.quotes{margin-top:1.25rem}
""" + MARK_B

AXES_COURT = {0: "les finances", 1: "le travail et le social", 2: "l'immigration", 3: "le pouvoir d'achat", 4: "la sécurité", 5: "les institutions"}
NOMBRES = {0: "aucun", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six"}
CHIPS = ('<div class="chips"><a href="#finances">1 Finances</a><a href="#travail">2 Travail et social</a>'
         '<a href="#immigration">3 Immigration</a><a href="#pouvoir-achat">4 Pouvoir d\'achat</a>'
         '<a href="#securite">5 Sécurité</a><a href="#institutions">6 Institutions et Europe</a><a href="#methode">+ Méthode</a></div>')


def lire_grille(html):
    """Retourne la liste des six lignes [D, F, C, E] de crans, et la base (votes seuls ou actes)."""
    i = html.index('<section class="grid'); j = html.index('</section>', i)
    rows = re.findall(r'<a class="grow"[^>]*>(.*?)</a>', html[i:j], re.S)
    if len(rows) != 6:
        sys.exit(f"grille : {len(rows)} lignes trouvées, 6 attendues")
    grille, votes_seuls = [], None
    for r in rows:
        pills = re.findall(r'class="pill (c\d)([^"]*)"', r)
        if len(pills) != 4:
            sys.exit("grille : 4 pastilles attendues par ligne")
        grille.append([int(p[0][1]) for p in pills])
        if votes_seuls is None:
            votes_seuls = "base-votes" in pills[2][1]
    return grille, votes_seuls


def imprint_svg(grille, votes_seuls, titre="Empreinte des vingt-quatre verdicts", petit=False):
    cx = [14, 34, 54, 74, 94, 114]; cy = [12, 32, 52, 72]
    dots = []
    for q in range(4):
        for a in range(6):
            v = grille[a][q]
            extra = ""
            if q == 2:
                extra = ' stroke="var(--muted)" stroke-width="1.5"' + (' stroke-dasharray="2 2"' if votes_seuls else "")
            dots.append(f'<circle cx="{cx[a]}" cy="{cy[q]}" r="6.5" fill="var(--v{v})"{extra}/>')
    base = "la rangée des votes est cerclée en pointillé, lecture sur votes seuls" if votes_seuls else "la rangée des votes est cerclée d'un trait plein, lecture sur votes et actes"
    aria = "" if petit else ' aria-labelledby="imp-t imp-d"'
    cls = "" if petit else ' class="imprint"'
    desc = "" if petit else f'<title id="imp-t">{titre}</title><desc id="imp-d">Six colonnes pour les six sujets, quatre rangées pour les quatre questions, un point coloré par verdict, du rouge au vert ; {base}.</desc>'
    return f'<svg{cls} viewBox="0 0 128 84" role="img"{aria}>{desc}' + "".join(dots) + "</svg>"


def compte(grille, q):
    return {v: [a for a in range(6) if grille[a][q] == v] for v in (1, 2, 3, 4, 5)}


def nomme(axes):
    return " et ".join(AXES_COURT[a] for a in axes)


def ligne_resultat(grille, votes_seuls, force, periode):
    d, f, c, e = (compte(grille, q) for q in range(4))
    parts = []
    # constat
    seg = []
    if d[4]: seg.append(f"fondé sur {NOMBRES[len(d[4])]} sujet{'s' if len(d[4]) > 1 else ''}")
    if d[3]: seg.append(f"partiel sur {NOMBRES[len(d[3])]}")
    if d[2]: seg.append(f"faux en partie sur {nomme(d[2])}")
    parts.append("constat " + ", ".join(seg))
    seg = []
    if f[4]: seg.append(f"plutôt faisable sur {NOMBRES[len(f[4])]}")
    if f[3]: seg.append(f"faisable sous conditions sur {NOMBRES[len(f[3])]} sujet{'s' if len(f[3]) > 1 else ''}")
    if f[2]: seg.append(f"très incertain sur {nomme(f[2]) if len(f[2]) <= 2 else NOMBRES[len(f[2])]}")
    parts.append(", ".join(seg))
    seg = []
    if c[4]: seg.append(f"cohérence plutôt tenue sur {NOMBRES[len(c[4])]} sujet{'s' if len(c[4]) > 1 else ''}")
    if c[3]: seg.append(("écart partiel sur " if c[4] else "cohérence en écart partiel sur ") + (nomme(c[3]) if len(c[3]) <= 2 else NOMBRES[len(c[3])]))
    if c[2]: seg.append(("écart important sur " if (c[4] or c[3]) else "cohérence en écart important sur ") + (nomme(c[2]) if len(c[2]) <= 2 else NOMBRES[len(c[2])]))
    if c[1]: seg.append("contradiction sur " + nomme(c[1]))
    parts.append(", ".join(seg))
    seg = []
    if e[3]: seg.append(f"demandes servies en partie sur {NOMBRES[len(e[3])]}")
    if e[4]: seg.append(f"pleinement sur {nomme(e[4]) if len(e[4]) <= 2 else NOMBRES[len(e[4])]}")
    if e[2]: seg.append(f"contredites sans le dire sur {nomme(e[2])}")
    parts.append(", ".join(seg))
    base = (f"Lecture sur les votes seuls, {force} n'ayant pas gouverné." if votes_seuls
            else f"Lecture sur les votes et les actes de {periode}.")
    return "Vingt-quatre verdicts en un regard&nbsp;: " + "&nbsp;; ".join(parts) + ". " + base


def transforme_page(path, force, nom_long, periode, non_gouverne, eyebrow_txt):
    s = path.read_text(encoding="utf-8")
    if "hero-top" in s:
        sys.exit(f"{path} : en-tête déjà transformé")
    grille, votes_seuls = lire_grille(s)
    if non_gouverne != votes_seuls:
        sys.exit(f"{path} : base lue dans la grille ({'votes seuls' if votes_seuls else 'actes'}) contraire à l'option")
    h0 = s.index('<header class="hero">'); q0 = s.index('<section class="quotes"'); g0 = s.index('<section class="grid"'); h1 = s.index('</header>')
    hero_old = s[h0:q0]
    h1_tag = re.search(r"<h1>.*?</h1>", hero_old, re.S).group(0)
    rule = re.search(r'<p class="rule">(.*?)</p>', hero_old, re.S).group(1).strip()
    quotes = s[q0:g0]
    grid = s[g0:h1]
    base_txt = (f"Les verdicts de cohérence sont marqués « votes seuls »&nbsp;: {force} n'a pas gouverné depuis 2012, sa parole est confrontée aux scrutins retenus et aux textes de son groupe, et à rien d'autre. Les forces qui ont gouverné portent la marque « votes + actes »."
                if votes_seuls else
                f"Les verdicts de cohérence sont marqués « votes + actes »&nbsp;: la parole de {force} est confrontée aux scrutins retenus, aux textes de son groupe et à ses décisions de gouvernement de {periode}. Les forces qui n'ont pas gouverné portent la marque « votes seuls » et ne se comparent qu'entre elles.")
    hero = f'''<header class="hero">
  <div class="hero-top">
    <div>
      <span class="eyebrow2">{eyebrow_txt} · {nom_long}</span>
      {h1_tag}
    </div>
    {imprint_svg(grille, votes_seuls)}
  </div>
  <p class="lede">{ligne_resultat(grille, votes_seuls, force, periode)}</p>

'''
    grid = grid.replace('<p class="sub">Quatre questions par sujet. Chaque pastille est un verdict sur une échelle de cinq crans, du rouge au vert. Touchez une ligne pour aller au chapitre.</p>',
                        '<p class="sub">Quatre questions par sujet, un verdict par case, du rouge au vert. Touchez une ligne pour aller au chapitre.</p>')
    path_html = f'''
    <div class="path">
      <p class="ptime">Trois minutes pour la grille, vingt pour les six chapitres.</p>
      {CHIPS}
    </div>
    <details class="dig lire"><summary>Comment lire cette page <span class="chev">›</span></summary><div class="body"><p>{rule}</p><p>{base_txt}</p></div></details>
'''
    k = grid.rindex('</section>')
    grid = grid[:k] + path_html + grid[k:]
    s = s[:h0] + hero + grid + "\n" + quotes + s[h1:]
    s = insere_css(s)
    path.write_text(s, encoding="utf-8")
    print(path, ": en-tête transformé ;", "votes seuls" if votes_seuls else f"actes {periode}")


def insere_css(s):
    if MARK_A in s:
        s = s[:s.index(MARK_A)] + s[s.index(MARK_B) + len(MARK_B):]
    if "{{CSS}}" in s:
        return s.replace("{{CSS}}", "{{CSS}}\n" + CSS, 1)
    return s.replace("</style>", CSS + "\n</style>", 1)


FORCES_SYNTH = [("renaissance", "Renaissance"), ("rn", "RN"), ("lfi", "LFI"), ("ps", "PS"), ("lr", "LR")]


def transforme_synthese(path):
    s = path.read_text(encoding="utf-8")
    if "hero-top" in s:
        sys.exit(f"{path} : en-tête déjà transformé")
    figs = []
    for slug, nom in FORCES_SYNTH:
        page = (ROOT / "05-artifacts" / f"{slug}.html").read_text(encoding="utf-8")
        g, vs = lire_grille(page)
        figs.append(f'<figure>{imprint_svg(g, vs, petit=True)}<figcaption>{nom}</figcaption></figure>')
    h0 = s.index('<header class="hero">'); h1 = s.index('</header>')
    hero_old = s[h0:h1]
    h1_tag = re.search(r"<h1>.*?</h1>", hero_old, re.S).group(0)
    rule = re.search(r'<p class="rule">(.*?)</p>', hero_old, re.S).group(1).strip()
    forces = re.search(r'<div class="forces".*?</div>\s*', hero_old, re.S).group(0)
    hero = f'''<header class="hero">
  <span class="eyebrow2">Synthèse · cinq forces, même grille, mêmes scrutins</span>
  {h1_tag}
  <div class="imprints" role="img" aria-label="Les cinq empreintes de verdicts, une par force, dans la même grille de six sujets et quatre questions">
    {"".join(figs)}
  </div>
  <p class="lede">Cinq empreintes dans la même grille&nbsp;: aucun constat faux, aucun programme « plutôt faisable », la cohérence en deux familles, deux problèmes que personne ne regarde. Chaque point est un verdict qu'on peut aller vérifier sur la page de la force.</p>
  {forces}
  <div class="path">
    <p class="ptime">Cinq minutes pour les matrices, vingt pour les chapitres.</p>
    <div class="chips"><a href="#h-grid">Les verdicts</a><a href="#tendances">Tendances</a><a href="#demandes">Demandes</a><a href="#finances">1 Finances</a><a href="#travail">2 Travail et social</a><a href="#immigration">3 Immigration</a><a href="#pouvoir-achat">4 Pouvoir d'achat</a><a href="#securite">5 Sécurité</a><a href="#institutions">6 Institutions et Europe</a><a href="#methode">+ Méthode</a></div>
  </div>
  <details class="dig lire"><summary>Comment lire cette page <span class="chev">›</span></summary><div class="body"><p>{rule}</p></div></details>
'''
    s = s[:h0] + hero + s[h1:]
    s = insere_css(s)
    path.write_text(s, encoding="utf-8")
    print(path, ": en-tête de synthèse transformé")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page"); ap.add_argument("--force", help="« le RN », « LFI », « Renaissance », « le PS », « LR »")
    ap.add_argument("--nom-long", help="nom en toutes lettres pour le surtitre")
    ap.add_argument("--actes", help="période des actes, par exemple 2017-2026 ; absent si --non-gouverne")
    ap.add_argument("--non-gouverne", action="store_true")
    ap.add_argument("--eyebrow", default=None, help="texte du surtitre sans le nom ; par défaut lu dans la page")
    ap.add_argument("--synthese")
    a = ap.parse_args()
    if a.synthese:
        transforme_synthese(pathlib.Path(a.synthese)); return
    p = pathlib.Path(a.page)
    eyebrow = a.eyebrow
    if eyebrow is None:
        m = re.search(r'<span class="eyebrow">(.*?)</span>', p.read_text(encoding="utf-8"))
        eyebrow = m.group(1) if m else "Lecture"
    transforme_page(p, a.force, a.nom_long or a.force, a.actes or "", a.non_gouverne, eyebrow)


if __name__ == "__main__":
    main()
