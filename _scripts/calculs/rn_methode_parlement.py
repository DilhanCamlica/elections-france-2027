# Calculs par nos soins pour 02-partis/rn/methode.md, bloc (c) "Le comportement parlementaire".
#
# SOURCE DES DONNEES (jeux open data de l'Assemblee nationale, recuperes le 2026-10-25) :
#   - Scrutins XVIIe legislature (9 097 scrutins, n. 1 a 9 097, dernier date du 2026-10-23),
#     fichier modifie cote serveur le 2026-10-25 17:25 GMT, 28 199 162 octets :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/scrutins/Scrutins.json.zip
#     fichiers lus : json/VTANR5L17V<n>.json
#   - Scrutins XVIe legislature (4 106 scrutins, contexte seulement) :
#     https://data.assemblee-nationale.fr/static/openData/repository/16/loi/scrutins/Scrutins.json.zip
#     fichiers lus : json/VTANR5L16V<n>.json
#   - Amendements XVIIe legislature (142 200 fichiers, 346 819 259 octets) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/amendements_div_legis/Amendements.json.zip
#     fichiers lus : json/<dossier>/<texte>/AMANR5L17*.json
#
# OU SONT LES DONNEES BRUTES : non versionnees dans le repo (taille). Le 2026-10-25 elles etaient dans
# le repertoire de travail du sous-agent (scratchpad de session, ephemere) :
#   .../scratchpad/an-scrutins/s.zip, .../scratchpad/an16/s.zip, .../scratchpad/an-amdts/a.zip
# Pour les retrouver : les retelecharger aux URL ci-dessus (les jeux sont mis a jour en continu, les
# chiffres peuvent bouger apres le 2026-10-25), par exemple :
#   mkdir -p ~/an-data && cd ~/an-data
#   curl -o scrutins17.zip https://data.assemblee-nationale.fr/static/openData/repository/17/loi/scrutins/Scrutins.json.zip
#   curl -o scrutins16.zip https://data.assemblee-nationale.fr/static/openData/repository/16/loi/scrutins/Scrutins.json.zip
#   curl -o amendements17.zip https://data.assemblee-nationale.fr/static/openData/repository/17/loi/amendements_div_legis/Amendements.json.zip
# puis : python3 -I _scripts/calculs/rn_methode_parlement.py ~/an-data/scrutins17.zip ~/an-data/scrutins16.zip ~/an-data/amendements17.zip
# (les archives zip sont lues directement, sans decompression).
#
# HYPOTHESES :
#   - Groupes identifies par leur code d'organe (referentiel AMO) : RN = PO845401 (XVIIe), PO800520 (XVIe) ;
#     LFI PO845413, SOC PO845419, EPR PO845407, DR PO845425, ECOS PO845439, DEM PO845454, HOR PO845470,
#     LIOT PO845485, GDR PO845514, UDR PO847173 puis PO872880, NI PO840056.
#   - Amendements : tous ceux du jeu (commission et seance, toutes lectures), attribues au groupe du
#     premier signataire (champ signataires.auteur.groupePolitiqueRef) ; sous-amendements inclus s'ils
#     sont dans le jeu ; ni temps de parole ni rappels au reglement. Periode : juillet 2024 au 2026-10-25.
#   - "Par depute" de legislature : effectifs des groupes au scrutin 8707 (2026-10-13), approximation
#     (le RN a compte jusqu'a 125 membres). Par texte : effectifs au scrutin indique dans TEXTES.
#   - Motions de censure : scrutins dont l'objet contient "motion de censure" ; "sur un 49.3" = objet
#     contenant "alinea 3" ; "auteur RN" = objet citant Mme Le Pen ou M. Tanguy ; le RN "vote" une motion
#     d'un autre groupe si plus de 50 de ses deputes votent pour. Les 8 motions d'autres groupes sur un
#     49.3 correspondent aux 8 recours de la legislature (1 Barnier, 4 Bayrou, 3 Lecornu).
#   - Motions de rejet : objet contenant "motion de rejet prealable" (orthographes fautives incluses).
import json, re, sys, zipfile, collections

RN17, RN16 = "PO845401", "PO800520"
NOMS = {"PO845401": "RN", "PO845413": "LFI", "PO845419": "SOC", "PO845407": "EPR", "PO845425": "DR",
        "PO845439": "ECOS", "PO845454": "DEM", "PO845470": "HOR", "PO845485": "LIOT", "PO845514": "GDR",
        "PO872880": "UDR", "PO847173": "UDR", "PO840056": "NI"}
TEXTES = [("PLF 2025", "DLR5L17N50198", 438), ("PLF 2026", "DLR5L17N52428", 4241),
          ("PLFSS 2026", "DLR5L17N52922", 4241), ("PLF 2027", "DLR5L17N54629", 8707)]


def scrutins(zpath):
    z = zipfile.ZipFile(zpath)
    out = {}
    for n in z.namelist():
        if n.endswith(".json"):
            s = json.loads(z.read(n))["scrutin"]
            out[int(s["numero"])] = s
    return out


def pour(s, org):
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        if g["organeRef"] == org:
            return int(g["vote"]["decompteVoix"]["pour"] or 0), int(g["vote"]["decompteVoix"]["contre"] or 0)
    return 0, 0


def effectifs(s):
    m = collections.Counter()
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        m[NOMS.get(g["organeRef"], g["organeRef"])] += int(g["nombreMembresGroupe"])
    return m


def censures(sc, rn, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = (s["objet"]["libelle"] or "").lower()
        if "motion de censure" in o:
            rows.append((num, s["dateScrutin"], "alinéa 3" in o, "le pen" in o or "tanguy" in o,
                         pour(s, rn)[0], s["sort"]["code"]))
    a3 = [r for r in rows if r[2]]
    autres3 = [r for r in a3 if not r[3]]
    autres2 = [r for r in rows if not r[2] and not r[3]]
    print(f"[{leg}] motions de censure votees : {len(rows)} ; deposees par le RN : {sum(r[3] for r in rows)} "
          f"(dont {sum(r[3] for r in a3)} sur un 49.3)")
    print(f"[{leg}] motions d'autres groupes sur un 49.3 : {len(autres3)} ; votees par le RN : "
          f"{sum(r[4] > 50 for r in autres3)} {[ (r[0], r[1]) for r in autres3 if r[4] > 50]}")
    print(f"[{leg}]   non votees par le RN : {[(r[0], r[1]) for r in autres3 if r[4] <= 50]}")
    print(f"[{leg}] motions d'autres groupes, article 49 alinea 2 : {len(autres2)} ; votees par le RN : "
          f"{sum(r[4] > 50 for r in autres2)}")
    print(f"[{leg}] motions adoptees : {[r[0] for r in rows if r[5] == 'adopté']}")


def rejets(sc):
    rows = []
    for num, s in sc.items():
        o = s["objet"]["libelle"] or ""
        if re.search(r"motion de rejet p[ré]*alable", o.lower()):
            p, c = pour(s, RN17)
            rows.append((num, p > c, bool(re.search(r"Le Pen|Tanguy|Chenu|Bilde|Ménagé", o)), s["sort"]["code"]))
    print(f"[XVIIe] motions de rejet prealable votees : {len(rows)} ; deposees par un depute RN : "
          f"{sum(r[2] for r in rows)} ; votees par le RN : {sum(r[1] for r in rows)} ; adoptees : "
          f"{sum(r[3] == 'adopté' for r in rows)}")


def amendements(zpath, sc):
    z = zipfile.ZipFile(zpath)
    tot, par_dossier = collections.Counter(), collections.defaultdict(collections.Counter)
    for n in z.namelist():
        if not n.endswith(".json"):
            continue
        a = json.loads(z.read(n))["amendement"]
        au = a["signataires"]["auteur"]
        g = au.get("groupePolitiqueRef")
        g = NOMS.get(g, g) if isinstance(g, str) else ("GOUV" if au.get("typeAuteur") == "Gouvernement" else "autre")
        tot[g] += 1
        par_dossier[n.split("/")[1]][g] += 1

    def table(label, c, nscr):
        t = sum(c.values()); m = effectifs(sc[nscr])
        print(f"[amendements] {label} : total {t} (effectifs au scrutin {nscr})")
        for g in ["RN", "LFI", "SOC", "EPR", "DR", "ECOS", "GDR", "LIOT", "DEM", "HOR", "UDR"]:
            if c.get(g) and m.get(g):
                print(f"    {g:5s} {c[g]:6d}  {100*c[g]/t:5.1f} % des amendements  {100*m[g]/577:5.1f} % des sieges"
                      f"  {c[g]/m[g]:6.1f} par depute")
    table("legislature entiere", tot, 8707)
    for label, dossier, nscr in TEXTES:
        table(label, par_dossier[dossier], nscr)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__ or "usage : rn_methode_parlement.py <scrutins17.zip> <scrutins16.zip> <amendements17.zip>")
    s17, s16 = scrutins(sys.argv[1]), scrutins(sys.argv[2])
    censures(s17, RN17, "XVIIe")
    censures(s16, RN16, "XVIe")
    rejets(s17)
    amendements(sys.argv[3], s17)
