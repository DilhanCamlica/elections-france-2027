"""Scrutin public par appel nominal du 23 octobre 2024, commission des affaires sociales,
article 1er de la PPL n° 284 (abrogation de la réforme des retraites de 2023), compte rendu n° 10, p. 16-17.
Position de chaque groupe recalculée sur ses membres présents (règle des 60 %, `01-socle/03-sources-et-hierarchie.md` §5 bis),
appartenance au groupe à la date du vote lue dans le jeu open data AMO30 (tous acteurs, mandats, organes, historique).

Usage : python3 _scripts/calculs/commission_2024-10-23.py <dossier json d'AMO30 décompressé>
Source du jeu : https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
Écrit le 2026-10-27 (boucle de révision après la verticale PS), calcul par nos soins.
"""
import glob, json, sys, unicodedata
from collections import defaultdict

DATE = "2024-10-23"
POUR = """Christophe Bentz, Théo Bernhardt, Sandra Delannoy, Sandrine Dogor-Such, Gaëtan Dussausaye, Guillaume Florquin,
Thierry Frappé, Katiana Levavasseur, René Lioret, Christine Loir, Joëlle Mélin, Thomas Ménagé, Yannick Monnet, Serge Muller,
Lisette Pollet, Angélique Ranc, Emmanuel Taché de la Pagerie"""
CONTRE = """Thibault Bazin, Sylvie Bonnet, Nathalie Colin-Oesterlé, Paul-André Colombani, Josiane Corneloup, Sophie Delorme,
Fabien Di Filippo, Olivier Falorni, François Gernigon, Jean-Carles Grelier, Justine Gruet, Jérôme Guedj, Michel Lauzzana,
Christine Le Nabour, Brigitte Liso, Joséphine Missoffe, Christophe Mongardien, Laurent Panifous, Stéphanie Rist,
Sandrine Rousseau, Jean-François Rousset, Arnaud Simion, Prisca Thevenot, Nicolas Turquois, Frédéric Valletoux, Annie Vidal,
Philippe Vigier, Stéphane Viry"""
ABST = """Ségolène Amiot, Joël Aviragnet, Béatrice Bellay, Anaïs Belouassa-Cherifi, Louis Boyard, Elie Califer, Hadrien Clouet,
Hendrik Davi, Fanny Dombre Coste, Karen Erodi, Océane Godard, Zahia Hamdane, Florence Herouin-Léautey, Élise Leboucher,
Benjamin Lucas-Lundy, Damien Maudet, Sébastien Peytavie, Jean-Hugues Ratenon, Sandrine Runel"""

# Noms du compte rendu dont la graphie diffère de l'état civil du jeu AMO30
ALIAS = {"Emmanuel Taché de la Pagerie": "Emmanuel Taché", "Sophie Delorme": "Sophie Delorme Duret"}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return " ".join(s.replace("-", " ").split())

def main(root):
    organes = {}
    for f in glob.glob(f"{root}/organe/*.json"):
        o = json.load(open(f))["organe"]
        organes[o["uid"]] = o.get("libelleAbrev") or o.get("libelleAbrege") or o["libelle"]
    index = {}
    for f in glob.glob(f"{root}/acteur/*.json"):
        a = json.load(open(f))["acteur"]
        ident = a["etatCivil"]["ident"]
        key = norm(f"{ident['prenom']} {ident['nom']}")
        ms = a.get("mandats", {}).get("mandat", [])
        if isinstance(ms, dict):
            ms = [ms]
        gp = None
        for m in ms:
            if m.get("typeOrgane") != "GP":
                continue
            d0, d1 = m.get("dateDebut"), m.get("dateFin")
            if d0 and d0 <= DATE and (not d1 or d1 >= DATE):
                gp = organes.get(m["organes"]["organeRef"], m["organes"]["organeRef"])
        index.setdefault(key, []).append(gp)
    votes = {"pour": POUR, "contre": CONTRE, "abstention": ABST}
    tally = defaultdict(lambda: defaultdict(int))
    for pos, names in votes.items():
        for n in [x.strip() for x in names.replace("\n", " ").split(",")]:
            gps = index.get(norm(ALIAS.get(n, n)))
            if not gps:
                print(f"NON TROUVÉ : {n}", file=sys.stderr)
                continue
            gp = [g for g in gps if g] or ["(sans groupe)"]
            if len(gp) > 1:
                print(f"AMBIGU : {n} {gp}", file=sys.stderr)
            tally[gp[0]][pos] += 1
    print(f"| Groupe (AMO30, au {DATE}) | Pour | Contre | Abstention | Présents | Position (règle des 60 %) |")
    print("|---|---|---|---|---|---|")
    total = defaultdict(int)
    for g in sorted(tally, key=lambda g: -sum(tally[g].values())):
        t = tally[g]; n = sum(t.values())
        best = max(t, key=t.get)
        pos = best if t[best] / n > 0.6 else "divisé"
        print(f"| {g} | {t['pour']} | {t['contre']} | {t['abstention']} | {n} | {pos} ({t[best]} sur {n}, {100*t[best]/n:.0f} %) |")
        for k, v in t.items(): total[k] += v
    print(f"| Total | {total['pour']} | {total['contre']} | {total['abstention']} | {sum(total.values())} | compte rendu : 17 / 28 / 19, 64 votants |")

if __name__ == "__main__":
    main(sys.argv[1])
