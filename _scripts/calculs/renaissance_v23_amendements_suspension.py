"""Boucle v2.3 (2026-10-28), Renaissance, axe 2 : part du groupe EPR parmi les signataires des amendements
au PLFSS 2027 (projet n° 3211) qui suppriment la suspension de la réforme des retraites de 2023
(article 105 de la loi n° 2025-1403). Appartenance au groupe à la date du dépôt lue dans le jeu open data AMO30.

Usage : python3 -I _scripts/calculs/renaissance_v23_amendements_suspension.py <dossier json d'AMO30 décompressé>
Source du jeu : https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
Amendements relevés par recherche plein texte sur les 3 066 amendements de séance (3211/AN/1 à 3180) et les
1 659 amendements de commission (3211/CION-SOC/AS1 à AS2000) téléchargés le 2026-10-28. Calcul par nos soins.
"""
import glob, json, sys, unicodedata
from collections import Counter

DATE = "2026-10-15"
AMENDEMENTS = {
    "AN 801 (2026-10-15)": ["Ferracci", "Vidal", "Midy", "Rousset"],
    "AN 2246 (2026-10-16)": ["Cazeneuve"],
    "CION-SOC AS717": ["Ferracci", "Rousset", "Vidal"],
    "AN 3122": ["Valletoux"],
    "AN 492 et 493": ["Juvin", "de Maistre", "Neuder", "Bonnefoy"],
    "AN 366 (quatre premiers signataires, groupe Horizons)": ["Colin-Oesterlé", "Marcangeli", "Gernigon", "Le Nabour"],
}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return " ".join(s.replace("-", " ").split())

def main(root):
    organes = {}
    for f in glob.glob(f"{root}/organe/*.json"):
        o = json.load(open(f))["organe"]
        organes[o["uid"]] = o.get("libelleAbrev") or o.get("libelleAbrege") or o["libelle"]
    by_nom, groupe = {}, Counter()
    for f in glob.glob(f"{root}/acteur/*.json"):
        a = json.load(open(f))["acteur"]
        ident = a["etatCivil"]["ident"]
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
        if gp:
            groupe[gp] += 1
            by_nom.setdefault(norm(ident["nom"]), []).append((f"{ident['prenom']} {ident['nom']}", gp))
    epr = groupe.get("EPR", 0)
    print(f"Membres du groupe EPR au {DATE} (AMO30) : {epr}")
    for am, noms in AMENDEMENTS.items():
        gps = []
        for n in noms:
            hits = by_nom.get(norm(n), [])
            if len(hits) != 1:
                print(f"  ambigu ou non trouvé : {n} -> {hits}", file=sys.stderr)
            gps += [g for _, g in hits[:1]]
        c = Counter(gps)
        part = 100 * c.get("EPR", 0) / epr if epr else 0
        print(f"{am} : {len(noms)} signataires, groupes {dict(c)}, part du groupe EPR {part:.1f} %")

if __name__ == "__main__":
    main(sys.argv[1])
