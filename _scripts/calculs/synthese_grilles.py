#!/usr/bin/env python3
"""Lit les cinq pages publiées (05-artifacts/*.html) et imprime la matrice des verdicts
D, F, C, E par axe, la ligne M, la base de chaque verdict C, et le compte des crans 2
de la ligne C par famille de base (votes seuls / votes + actes). Aucun total, aucune moyenne.

Usage : python3 -I synthese_grilles.py
"""
import re, pathlib

RACINE = pathlib.Path(__file__).resolve().parents[2]
FORCES = [("renaissance", "Renaissance"), ("rn", "RN"), ("lfi", "LFI"), ("ps", "PS"), ("lr", "LR")]
AXES = ["Finances publiques et dette", "Travail, protection sociale et fraude", "Immigration",
        "Pouvoir d'achat et fiscalité", "Sécurité et libertés", "Institutions, démocratie et Europe"]


def lire(slug):
    s = (RACINE / "05-artifacts" / f"{slug}.html").read_text(encoding="utf-8")
    i = s.find('<section class="grid'); j = s.find("</section>", i)
    seg = s[i:j]
    rows = re.findall(r'<a class="grow"[^>]*>(.*?)</a>', seg, re.S)
    assert len(rows) == 6, (slug, len(rows))
    grille = []
    for r in rows:
        pills = re.findall(r'<div class="pill (c\d)([^"]*)">(.*?)</div>', r, re.S)
        assert len(pills) == 4, (slug, r[:80])
        crans = [int(p[0][1]) for p in pills]
        base = re.search(r'class="pb">([^<]*)<', pills[2][2])
        grille.append((crans, base.group(1).replace("&nbsp;", " ") if base else "?"))
    m = re.search(r'<div class="mline[^"]*">(.*?)</div>\s*</div>', seg[seg.find('class="mline'):] if 'class="mline' in seg else s, re.S)
    mseg = s[s.find('class="mline'):s.find('class="mline') + 1500]
    mcran = re.search(r'class="(?:pill|dot) [^"]*?(?:c|d)(\d)', mseg)
    return grille, int(mcran.group(1)) if mcran else None


def main():
    donnees = {slug: lire(slug) for slug, _ in FORCES}
    noms = [n for _, n in FORCES]
    print("| Axe | " + " | ".join(noms) + " |")
    print("|---|" + "---|" * len(noms))
    for a, axe in enumerate(AXES):
        cases = []
        for slug, _ in FORCES:
            crans, base = donnees[slug][0][a]
            cases.append("D%d F%d C%d E%d" % tuple(crans))
        print(f"| {a+1}. {axe} | " + " | ".join(cases) + " |")
    print("| Méthode (M) | " + " | ".join(str(donnees[s][1]) for s, _ in FORCES) + " |")
    print()
    print("Base du verdict C (identique sur les six axes d'une force) :")
    familles = {}
    for slug, nom in FORCES:
        bases = {b for _, b in donnees[slug][0]}
        assert len(bases) == 1, (slug, bases)
        base = bases.pop()
        fam = "votes seuls" if "seuls" in base else "votes + actes"
        familles.setdefault(fam, []).append((nom, base, [c[2] for c, _ in donnees[slug][0]]))
        print(f"  {nom} : {base}")
    print()
    for fam, membres in familles.items():
        print(f"Famille « {fam} » : " + ", ".join(n for n, _, _ in membres))
        for nom, base, cs in membres:
            print(f"  {nom} : ligne C {'/'.join(map(str, cs))}, crans 2 : {cs.count(2)}, crans 4 : {cs.count(4)}")
    print()
    for e, lettre in enumerate("DFCE"):
        print(f"Échelle {lettre} : " + " ; ".join(
            f"{nom} {'/'.join(str(c[e]) for c, _ in donnees[slug][0])}" for slug, nom in FORCES))


if __name__ == "__main__":
    main()
