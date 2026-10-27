# Calculs par nos soins pour 02-partis/lr/methode.md, blocs (b), (c) et (d).
# Modele : _scripts/calculs/ps_methode_parlement.py (memes jeux, memes regles, pour que les chapitres
# soient comparables).
#
# - Redige le : 2026-10-27 ; donnees arretees au 2026-10-27
# - Auteur : sous-agent Opus, etape 5 bis ; statut : brouillon
#
# SOURCE DES DONNEES, telechargees le 2026-10-27 :
#   - Scrutins XVIIe : https://data.assemblee-nationale.fr/static/openData/repository/17/loi/scrutins/Scrutins.json.zip
#   - Scrutins XVIe (contexte) : https://data.assemblee-nationale.fr/static/openData/repository/16/loi/scrutins/Scrutins.json.zip
#   - Amendements XVIIe : https://data.assemblee-nationale.fr/static/openData/repository/17/loi/amendements_div_legis/Amendements.json.zip
#   - Acteurs AMO30 (reconnaitre les deputes DR et LR parmi les auteurs des motions) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
#   - Legislatives 2017, 1er tour (nuances) : https://static.data.gouv.fr/resources/elections-legislatives-des-11-et-18-juin-2017-resultats-du-1er-tour/20170613-095447/Leg_2017_Resultats_T1_c.xlsx
#   - Legislatives 2022, codage des nuances : https://static.data.gouv.fr/resources/legis-2022-codage-des-nuances-politiques-des-candidats-a-lelection-legislatives-du-12-juin-2022/20220628-101302/codage-legis-2022.csv
#   - Legislatives 2024, candidatures du 1er tour : https://static.data.gouv.fr/resources/candidatures-aux-elections-legislatives-2024/20240619-141809/candidatures-legislatives2024-t1.csv
#
# Usage :
#   python3 -I _scripts/calculs/lr_methode_parlement.py scrutins17.zip scrutins16.zip amendements17.zip amo30.zip \
#       Leg_2017_Resultats_T1_c.xlsx codage-legis-2022.csv candidatures-legislatives2024-t1.csv
#
# HYPOTHESES (identiques au script PS sauf mention) :
#   - Groupes : DR = PO845425 (XVIIe, depuis le 2024-07-18) ; XVIe : LR = PO800508 (2022-06-28 au 2024-06-09).
#   - Motions de censure : objet contenant "motion de censure" ; "sur un 49.3" = "alinea 3" ;
#     "premier signataire DR" = premier nom cite dans l'objet est celui d'un depute ayant appartenu au groupe ;
#     "votee" = plus de la moitie des membres du groupe pour ; "pas pris part" = aucun vote exprime du groupe.
#   - Motions de rejet prealable : auteur = depute du groupe cite apres "deposee par".
#   - Amendements : groupe du premier signataire ; commission et seance, toutes lectures ; effectifs au scrutin 8707.
#   - Candidats : 2017, cellules de nuance "LR" ; 2022, nuance du ministere "LR" (et, pour controle, "UDI", "DVD") ;
#     2024, codeNuance "LR" (les candidats investis par l'alliance d'Eric Ciotti portent la nuance "UXD").
import csv, json, re, sys, zipfile, collections
from datetime import date

DR17 = "PO845425"
LR16 = {"PO800508"}
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
            d = json.loads(z.read(n))
            if "scrutin" in d:
                out[int(d["scrutin"]["numero"])] = d["scrutin"]
    return out


def vote(s, orgs):
    p = c = a = npv = eff = 0
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        if g["organeRef"] in orgs:
            d = g["vote"]["decompteVoix"]
            p += int(d.get("pour") or 0); c += int(d.get("contre") or 0)
            a += int(d.get("abstentions") or d.get("abstention") or 0)
            npv += int(d.get("nonVotants") or 0); eff += int(g["nombreMembresGroupe"])
    return p, c, a, eff


def effectifs(s):
    m = collections.Counter()
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        m[NOMS.get(g["organeRef"], g["organeRef"])] += int(g["nombreMembresGroupe"])
    return m


def noms_groupe(amo_zip, codes):
    z = zipfile.ZipFile(amo_zip)
    noms = set()
    for n in z.namelist():
        if "/acteur/" in n and n.endswith(".json"):
            a = json.loads(z.read(n))["acteur"]
            ms = a["mandats"]["mandat"]
            ms = ms if isinstance(ms, list) else [ms]
            orgs = set()
            for m in ms:
                o = m.get("organes", {}).get("organeRef")
                orgs |= {o} if isinstance(o, str) else set(o or [])
            if orgs & codes:
                noms.add(a["etatCivil"]["ident"]["nom"])
    return noms


def cite(texte, noms):
    return [n for n in noms if re.search(r"\b" + re.escape(n) + r"\b", texte)]


def premier_nom(o):
    m = re.search(r"par (?:M\.|Mme|MM\.|Mmes) ([^,]+?)(?:,| et )", o)
    return m.group(1) if m else ""


def censures(sc, orgs, noms, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = s["objet"]["libelle"] or ""
        if "motion de censure" in o.lower():
            p, c, a, eff = vote(s, orgs)
            rows.append(dict(num=num, date=s["dateScrutin"], a3="alinéa 3" in o.lower(),
                             premier=bool(cite(premier_nom(o), noms)), cosig=bool(cite(o, noms)),
                             vote=eff > 0 and p > eff / 2, pour=p, eff=eff, sort=s["sort"]["code"],
                             total=int(s["syntheseVote"]["decompte"]["pour"]), o=o))
    print(f"[{leg}] motions de censure votees : {len(rows)} ; sur un 49.3 : {sum(r['a3'] for r in rows)}")
    prem = [r for r in rows if r["premier"]]
    print(f"[{leg}] premier signataire du groupe : {len(prem)} : "
          f"{[(r['num'], r['date'], 'a3' if r['a3'] else 'a2', r['total'], r['pour'], r['o'][:120]) for r in prem]}")
    cos = [r for r in rows if r["cosig"] and not r["premier"]]
    print(f"[{leg}] cosignees sans premier signataire du groupe : {[(r['num'], r['date'], r['pour']) for r in cos]}")
    print(f"[{leg}] votees par le groupe : {sum(r['vote'] for r in rows)} sur {len(rows)} : "
          f"{[(r['num'], r['date'], r['pour'], r['eff']) for r in rows if r['vote']]}")
    print(f"[{leg}] voix du groupe pour, motion par motion (num, date, a2/a3, pour du groupe / effectif, total pour) :")
    for r in rows:
        print(f"    {r['num']} {r['date']} {'a3' if r['a3'] else 'a2'} {r['pour']}/{r['eff']} total {r['total']} {r['sort']}")
    return rows


def rejets(sc, orgs, noms, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = s["objet"]["libelle"] or ""
        if re.search(r"motion de rejet p[ré]*alable", o.lower()):
            auteurs = o.split("déposée par", 1)[-1].split(", d", 1)[0] if "déposée par" in o else ""
            p, c, a, eff = vote(s, orgs)
            rows.append((num, s["dateScrutin"], bool(cite(auteurs, noms)), p > c, c > p, s["sort"]["code"], o))
    grp = [r for r in rows if r[2]]
    print(f"[{leg}] motions de rejet prealable votees : {len(rows)} ; deposees par un depute du groupe : {len(grp)} "
          f"{[(r[0], r[1], r[5], r[6][:110]) for r in grp]}")
    autres = [r for r in rows if not r[2]]
    print(f"[{leg}] motions d'autres groupes : {len(autres)} ; groupe pour : {sum(r[3] for r in autres)} "
          f"{[(r[0], r[1], r[6][:120]) for r in autres if r[3]]}")
    return rows


def referendaires(sc, leg, orgs):
    rows = [(n, s["dateScrutin"], vote(s, orgs), s["objet"]["libelle"][:120]) for n, s in sorted(sc.items())
            if "référendaire" in (s["objet"]["libelle"] or "").lower()]
    print(f"[{leg}] motions referendaires : {len(rows)} {rows}")


def confiance(sc, orgs, leg):
    for n, s in sorted(sc.items()):
        o = (s["objet"]["libelle"] or "").lower()
        if "article 49, alinéa premier" in o or "alinéa 1er" in o or "49-1" in o or "déclaration de politique générale" in o \
                or "la confiance" in o:
            p, c, a, eff = vote(s, orgs)
            print(f"[{leg}] confiance {n} {s['dateScrutin']} : groupe pour {p} contre {c} abst {a} / {eff} ; "
                  f"total pour {s['syntheseVote']['decompte']['pour']} contre {s['syntheseVote']['decompte']['contre']} ; {s['objet']['libelle'][:90]}")


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
        for g in ["DR", "SOC", "LFI", "RN", "EPR", "ECOS", "GDR", "LIOT", "DEM", "HOR", "UDR"]:
            if c.get(g) and m.get(g):
                print(f"    {g:5s} {c[g]:6d}  {100*c[g]/t:5.1f} % des amendements  {100*m[g]/577:5.1f} % des sieges"
                      f"  {c[g]/m[g]:6.1f} par depute")
    table("legislature entiere", tot, 8707)
    for label, dossier, nscr in TEXTES:
        table(label, par_dossier[dossier], nscr)
    top = sorted(par_dossier.items(), key=lambda kv: -kv[1]["DR"])[:6]
    print("[amendements] dossiers ou DR depose le plus (dossier, DR, total, part DR) :")
    for d, c in top:
        print(f"    {d}  {c['DR']:6d}  {sum(c.values()):6d}  {100*c['DR']/sum(c.values()):5.1f} %")


def candidats_2017(xlsx):
    # Ministere de l'Interieur, feuille "Circo. leg. T1" : cellules portant la nuance "LR" (une par candidat).
    z = zipfile.ZipFile(xlsx)
    ss = [re.sub(r"<[^>]+>", "", x) for x in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    x = z.read("xl/worksheets/sheet4.xml").decode()
    c = collections.Counter(ss[int(v)] for v in re.findall(r'<c r="[A-Z]+\d+"[^>]*t="s"[^>]*><v>(\d+)</v>', x))
    print(f"[2017] candidats de nuance LR au premier tour : {c['LR']} (controle : SOC {c['SOC']}, FI {c['FI']}, UDI {c['UDI']})")
    return c["LR"]


def candidats_2022(path):
    with open(path, encoding="utf-8") as f:
        r = list(csv.DictReader(f))
    n = collections.Counter(x["NUANCE_CANDIDAT"] for x in r)
    cod = collections.Counter(x["CODAGE_LEGIS2022"] for x in r if x["NUANCE_CANDIDAT"] in ("LR", "UDI", "DVD"))
    print(f"[2022] candidats : {len(r)} ; nuance LR {n['LR']} ; UDI {n['UDI']} ; DVD {n['DVD']}")
    print(f"[2022] codage detaille des nuances LR, UDI, DVD (10 premiers) : {cod.most_common(10)}")
    return n["LR"]


def candidats_2024(path):
    with open(path, encoding="utf-8") as f:
        r = list(csv.DictReader(f))
    n = collections.Counter(x["codeNuance"] for x in r)
    print(f"[2024] candidats : {len(r)} ; nuance LR {n['LR']} ; UXD (alliance Ciotti) {n['UXD']} ; RN {n['RN']}")
    return n["LR"]


def complements(n17, n22, n24):
    age = lambda d: (date(2026, 10, 27) - d).days / 365.25
    print("[b] age des actes de coalition au 2026-10-27 (annees) :")
    for lab, d in [("gouvernement Barnier", date(2024, 9, 21)), ("49.3 Barnier PLFSS 2025", date(2024, 12, 2)),
                   ("49.3 Bayrou (premier)", date(2025, 2, 3)), ("interdiction TA Paris 7 mars", date(2025, 3, 7)),
                   ("dissolutions Jeune Garde, Lyon populaire", date(2025, 6, 12)), ("10 septembre 2025", date(2025, 9, 10)),
                   ("non-participation Lecornu II", date(2025, 10, 11))]:
        print(f"    {lab} : {age(d):.1f}")
    print("[b] seuil des dix ans : aucun acte de coalition anterieur au", date(2016, 10, 27))
    print("[b] part des sieges du groupe DR au 49.3 du 2024-12-02 : 47 sur 577 =", f"{100*47/577:.1f} %")
    print("[b] delai entre l'annonce de la consultation des adherents (2025-10-13) et la date d'arret :",
          (date(2026, 10, 27) - date(2025, 10, 13)).days, "jours, resultat non trouve")
    print("[d] delai de reaction, Meurthe-et-Moselle 2024 (alliance Ciotti) : publication et retrait le 2024-06-19 :",
          (date(2024, 6, 19) - date(2024, 6, 19)).days, "jour")
    tot = n17 + n22 + n24
    print(f"[d] candidatures de nuance LR aux legislatives 2017, 2022, 2024 : {n17} + {n22} + {n24} = {tot} ; cas admis : 0")


if __name__ == "__main__":
    if len(sys.argv) != 8:
        sys.exit("usage : lr_methode_parlement.py <scrutins17.zip> <scrutins16.zip> <amendements17.zip> <amo30.zip> "
                 "<Leg_2017_Resultats_T1_c.xlsx> <codage-legis-2022.csv> <candidatures-legislatives2024-t1.csv>")
    s17, s16 = scrutins(sys.argv[1]), scrutins(sys.argv[2])
    n17 = noms_groupe(sys.argv[4], {DR17})
    n16 = noms_groupe(sys.argv[4], LR16)
    print(f"deputes reconnus : DR XVIIe {len(n17)} ; LR XVIe {len(n16)}")
    censures(s17, {DR17}, n17, "XVIIe")
    censures(s16, LR16, n16, "XVIe")
    rejets(s17, {DR17}, n17, "XVIIe")
    rejets(s16, LR16, n16, "XVIe")
    referendaires(s17, "XVIIe", {DR17})
    referendaires(s16, "XVIe", LR16)
    confiance(s17, {DR17}, "XVIIe")
    amendements(sys.argv[3], s17)
    complements(candidats_2017(sys.argv[5]), candidats_2022(sys.argv[6]), candidats_2024(sys.argv[7]))
