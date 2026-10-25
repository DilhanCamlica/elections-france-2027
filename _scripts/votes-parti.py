#!/usr/bin/env python3
"""Produit `02-partis/<parti>/votes/scrutins.md` à partir de `03-sources/scrutins-positions.md`.

Pour chaque scrutin détaillé dans le registre (liste gelée, réserves, hors sélection,
compléments), reporte la position du groupe étudié et celle du groupe « hors périmètre,
cité quand il diverge » défini au socle (`01-socle/01-criteres.md` §1), puis signale les
divergences entre les deux. Aucune interprétation : des positions recalculées par la règle
des 60 % telles qu'elles figurent dans le registre.

Usage :
  python3 _scripts/votes-parti.py --parti rn --groupe RN --allie UDR --nom-groupe "Rassemblement National" --nom-allie "Union des droites pour la République"
"""
import argparse, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REG = ROOT / "03-sources" / "scrutins-positions.md"

def parse(text):
    """Retourne la liste des scrutins détaillés : numéro, date, axe, intitulé, sort, positions par groupe."""
    out = []
    blocks = re.split(r"\n(?=### Scrutin )", text)
    for b in blocks:
        m = re.match(r"### Scrutin (\d+) \(([^,]+), ([^)]*)\)", b)
        if not m:
            continue
        num, date, axe = m.group(1), m.group(2), m.group(3)
        tit = re.search(r"- Intitulé exact : (.+)", b)
        sort = re.search(r"- Sort : \*\*([^*]+)\*\*", b)
        rows = {}
        for r in re.finditer(r"^\| ([A-Za-z\-]+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| ([^|]+) \| ([^|]+) \|$", b, re.M):
            g = r.group(1)
            if g in ("Groupe",):
                continue
            pos = r.group(7).strip()
            if pos.endswith("(motion)"):
                pos = "pour (motion)" if int(r.group(3)) > 0 else "ne vote pas (motion)"
            rows[g] = dict(membres=int(r.group(2)), pour=int(r.group(3)), contre=int(r.group(4)),
                           abst=int(r.group(5)), nv=int(r.group(6)), pos=pos)
        out.append(dict(num=num, date=date, axe=axe, titre=tit.group(1).strip() if tit else "",
                        sort=sort.group(1) if sort else "", rows=rows))
    return out

def objets_courts(text):
    """Objet court de la table de synthèse (section « Table de synthèse » seulement), par numéro."""
    sec = text.split("## Table de synthèse", 1)[1].split("## Détail par scrutin", 1)[0]
    d = {}
    for r in re.finditer(r"^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", sec, re.M):
        d.setdefault(r.group(1), r.group(4).strip())
    return d

def cell(row):
    if row is None:
        return "non extrait"
    return f"{row['pos']} ({row['pour']}p {row['contre']}c {row['abst']}a)"

def diverge(a, b):
    if a is None or b is None:
        return "n.d."
    pa, pb = a["pos"], b["pos"]
    if pa == pb:
        return "non"
    if "aucun" in pa or "aucun" in pb:
        return "non évaluable (aucun vote exprimé)"
    if "divisé" in (pa, pb):
        return "partielle"
    return "oui"

def axe_court(axe):
    return re.sub(r"^axe ", "", axe)

def axe_key(axe):
    a = axe_court(axe)
    m = re.search(r"\d", a)
    base = 0
    if a.startswith("rés."):
        base = 7
    elif a.startswith("compl"):
        base = 8
    elif a.startswith("hors"):
        base = 9
    return (base, int(m.group(0)) if m else 0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parti", required=True, help="slug du dossier 02-partis/<parti>")
    ap.add_argument("--groupe", required=True, help="code du groupe dans le registre (RN, EPR, LFI-NFP, SOC, DR)")
    ap.add_argument("--allie", required=True, help="code du groupe hors périmètre cité quand il diverge")
    ap.add_argument("--nom-groupe", required=True)
    ap.add_argument("--nom-allie", required=True)
    a = ap.parse_args()
    text = REG.read_text(encoding="utf-8")
    scr = parse(text)
    oc = objets_courts(text)
    scr.sort(key=lambda s: axe_key(s["axe"]))
    today = datetime.date.today().isoformat()
    L = []
    L.append(f"# {a.nom_groupe} : positions sur les scrutins gelés, et divergences du groupe {a.allie}")
    L.append("")
    L.append(f"- Produit le : {today} par `_scripts/votes-parti.py` (mécanique, aucune interprétation)")
    L.append(f"- Source : `03-sources/scrutins-positions.md` (extraction du 2026-10-25, jeu open data « Scrutins » de l'Assemblée nationale, règle des 60 %)")
    L.append(f"- Groupe étudié : {a.nom_groupe} ({a.groupe}). Groupe hors périmètre, cité quand il diverge (`01-socle/01-criteres.md` §1) : {a.nom_allie} ({a.allie}).")
    L.append("- Lecture : une « divergence » est une position majoritaire différente entre les deux groupes sur le même scrutin ; « partielle » quand l'un des deux est divisé ; un groupe qui n'exprime aucun vote n'est pas comparé. Un vote sur un texte global est pondéré à part (`01-criteres.md` §4, échelle C).")
    L.append("- Les fiches par axe (`../axes/`) reportent ces positions dans leur tableau Q4, avec celles des quatre autres groupes suivis.")
    L.append("")
    L.append("## Tableau")
    L.append("")
    L.append(f"| N° | Axe | Date | Objet court | Sort | {a.groupe} | {a.allie} | Divergence |")
    L.append("|---|---|---|---|---|---|---|---|")
    n_div = n_part = n_tot = 0
    for s in scr:
        g = s["rows"].get(a.groupe); al = s["rows"].get(a.allie)
        d = diverge(g, al)
        if d == "oui": n_div += 1
        if d == "partielle": n_part += 1
        n_tot += 1
        L.append(f"| {s['num']} | {axe_court(s['axe'])} | {s['date']} | {oc.get(s['num'], s['titre'][:80])} | {s['sort']} | {cell(g)} | {cell(al)} | {d} |")
    L.append("")
    L.append("## Compte")
    L.append("")
    L.append(f"- Scrutins détaillés dans le registre : {n_tot}.")
    L.append(f"- Divergences nettes entre {a.groupe} et {a.allie} : {n_div}. Divergences partielles (un groupe divisé) : {n_part}.")
    L.append("")
    L.append("## Intitulés exacts")
    L.append("")
    for s in scr:
        L.append(f"- {s['num']} ({s['date']}) : {s['titre']} Page : https://www.assemblee-nationale.fr/dyn/17/scrutins/{s['num']}")
    out = ROOT / "02-partis" / a.parti / "votes" / "scrutins.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"écrit {out.relative_to(ROOT)} : {n_tot} scrutins, {n_div} divergences nettes, {n_part} partielles")

if __name__ == "__main__":
    main()
