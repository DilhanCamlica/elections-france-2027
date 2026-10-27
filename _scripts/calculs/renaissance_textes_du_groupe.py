#!/usr/bin/env python3
"""Renaissance / EPR : un texte est-il « du groupe » ou « d'élus du groupe » ?

Objet : appliquer la règle de 01-socle/01-criteres.md §6 (précision du
2026-10-27) aux propositions de loi du corpus Renaissance (C-R-21 à C-R-33).
Un texte est « du groupe » si la liste nominative de signataires réunit au moins
90 % des membres du groupe à la date du dépôt, ou s'il est déposé par le
président du groupe et défendu en séance par le groupe (règle du président,
saisie à la main ci-dessous : C-R-21). Sinon : texte d'élus du groupe ;
« transpartisan » si des cosignataires viennent d'autres groupes.

Date : 2026-10-27. Calcul par nos soins.

Usage :
    python3 renaissance_textes_du_groupe.py PPL_DIR AMO30_JSON_DIR
  PPL_DIR : dossier de textes extraits des PDF (ppl<numéro>.txt, obtenus par
    pdftotext -layout depuis https://www.assemblee-nationale.fr/dyn/opendata/PIONANR5L17B<numéro sur 4 chiffres>.pdf)
  AMO30_JSON_DIR : jeu open data AMO30 décompressé (sous-dossiers acteur/ et organe/).
Effectif du groupe = tous les mandats « GP » du groupe en cours à la date du
dépôt (membres, apparentés et président), comme dans les chiffres de l'Assemblée ;
la part calculée sur les seuls « membres » (hors apparentés) est donnée en plus.
Réserve : la liste « présentée par » du PDF officiel est celle de l'impression ;
des signataires dont le mandat de groupe ne commence qu'après la date de dépôt
(ex. entrés à l'EPR le 2024-10-23 ou en 2025) y figurent. Ils ne comptent pas
au numérateur (règle « à la date du dépôt ») ; leur nombre est affiché à part.
"""
import collections, glob, json, re, sys, unicodedata
from datetime import date

# (identifiant, numéro de PPL, règle du président : texte déposé par le président
# du groupe et défendu en séance par le groupe, vérifiée à la main)
TEXTES = [
    ("C-R-21", 448, True), ("C-R-22", 447, False), ("C-R-23", 1791, False),
    ("C-R-24", 1796, False), ("C-R-25", 2180, False), ("C-R-26", 1719, False),
    ("C-R-27", 1337, False), ("C-R-28", 905, False), ("C-R-29", 3090, False),
    ("C-R-30", 2107, False), ("C-R-31", 575, False), ("C-R-32", 1800, False),
    ("C-R-33", 1380, False),
]
MOIS = {m: i + 1 for i, m in enumerate(
    "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split())}


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]+", " ", s.lower()).strip()


def parse(txt):
    m = re.search(r"le (\d+)(?:er)? (\w+) (\d{4})\.", txt)
    d = date(int(m.group(3)), MOIS[m.group(2).lower()], int(m.group(1)))
    b = txt.split("présentée par", 1)[1]
    b = re.split(r"\n\s*député", b, maxsplit=1)[0]
    b = re.sub(r"\n\s*\u2013\s*\d+\s*\u2013\s*\n", "\n", b)
    b = re.sub(r"\s+", " ", b)
    noms = [x.strip(" ,.") for x in re.split(r"(?:^|\s)(?:M\.|Mme)\s", b) if x.strip(" ,.")]
    return d, noms


def charger(amo):
    organes = {}
    for f in glob.glob(f"{amo}/organe/*.json"):
        o = json.load(open(f))["organe"]
        if o.get("libelleAbrev") in ("EPR", "RE"):
            organes[o["uid"]] = o["libelleAbrev"]
    tous = {}
    for f in glob.glob(f"{amo}/organe/*.json"):
        o = json.load(open(f))["organe"]
        if o.get("codeType") == "GP":
            tous[o["uid"]] = o.get("libelleAbrev", "?")
    organes["__tous__"] = tous
    acteurs = []
    for f in glob.glob(f"{amo}/acteur/*.json"):
        a = json.load(open(f))["acteur"]
        ident = a["etatCivil"]["ident"]
        ms = a.get("mandats", {}).get("mandat", [])
        ms = [ms] if isinstance(ms, dict) else ms
        gp = []
        for x in ms:
            if x.get("typeOrgane") == "GP":
                fin = x.get("dateFin")
                gp.append((x["organes"]["organeRef"], x["dateDebut"],
                           fin if isinstance(fin, str) else "9999-12-31",
                           x.get("infosQualite", {}).get("codeQualite", "")))
        # le référentiel désambiguïse certains homonymes par « (département) » et
        # tronque certains noms composés : on retire la parenthèse ici, et la
        # correspondance par préfixe se fait plus bas
        acteurs.append((norm(ident["prenom"] + " " + re.sub(r"\(.*\)", "", ident["nom"])), gp))
    return organes, acteurs


def main(ppl_dir, amo):
    organes, acteurs = charger(amo)
    par_nom = {}
    for n, gp in acteurs:
        par_nom.setdefault(n, []).append(gp)
    print("id | PPL | dépôt | signataires | du groupe à la date | autres (dont membres du groupe à une autre date) | effectif (membres+apparentés) | part | part membres seuls | verdict")
    for ident, num, regle_pdt in TEXTES:
        txt = open(f"{ppl_dir}/ppl{num}.txt", encoding="utf-8").read()
        d, noms = parse(txt)
        iso = d.isoformat()
        sigle = "EPR" if d >= date(2024, 7, 18) else "RE"
        gref = [u for u, s in organes.items() if s == sigle and u != "__tous__"][0]
        tous = organes["__tous__"]

        def membre(gp):
            return [q for (o, db, df, q) in gp if o == gref and db <= iso <= df]

        eff = [q for n, gp in acteurs for q in membre(gp)]
        eff_all, eff_mem = len(eff), sum(1 for q in eff if q != "Membre apparenté")
        du_groupe, membres_seuls, inconnus, autre_date = 0, 0, [], 0
        ailleurs = collections.Counter()  # groupe, à la date, des cosignataires jamais membres du groupe
        for nom in noms:
            n = norm(nom)
            gps = par_nom.get(n)
            if not gps:  # nom composé tronqué dans le référentiel (ex. Vermorel-Marques)
                gps = [g for k, v in par_nom.items() if n.startswith(k + " ") for g in v]
            if not gps:
                inconnus.append(nom)
                continue
            # homonymes (ex. Alexandra Martin, deux députées) : on retient celui
            # qui a un mandat de groupe en cours à la date du dépôt
            vivants = [g for g in gps if any(db <= iso <= df for (_, db, df, _) in g)]
            gps = vivants or gps
            qs = [q for gp in gps for q in membre(gp)]
            if qs:
                du_groupe += 1
                membres_seuls += 1 if "Membre apparenté" not in qs else 0
            elif any(o == gref for gp in gps for (o, _, _, _) in gp):
                autre_date += 1  # a appartenu au groupe, mais pas à la date du dépôt
            else:
                en_cours = sorted((db, o) for gp in gps for (o, db, df, q) in gp if db <= iso <= df)
                ailleurs[tous.get(en_cours[-1][1], "?") if en_cours else "sans groupe"] += 1
        autres = len(noms) - du_groupe
        part, part_m = du_groupe / eff_all, membres_seuls / eff_mem
        if regle_pdt:
            v = "texte du groupe (règle du président du groupe)"
        elif part >= 0.9:
            v = "texte du groupe (part ≥ 90 %)"
        else:
            v = "texte d'élus du groupe"
            if autres:
                v += ", cosigné par des députés d'autres groupes"
        if len(noms) == 1:
            v = "texte d'élus du groupe (un seul signataire)"
        print(f"{ident} | {num} | {iso} | {len(noms)} | {du_groupe} | {autres} (dont {autre_date} membres du groupe à une autre date) | {eff_all} | {100*part:.1f} % | {100*part_m:.1f} % | {v}")
        if ailleurs:
            print("   jamais membres du groupe, par groupe à la date :", dict(ailleurs.most_common()))
        if inconnus:
            print(f"   noms non appariés au référentiel : {inconnus}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
