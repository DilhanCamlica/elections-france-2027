# Calculs par nos soins pour 02-partis/ps/methode.md, blocs (b) et (c).
# Modele : _scripts/calculs/lfi_methode_parlement.py et rn_methode_parlement.py (memes jeux, memes regles,
# pour que les chapitres soient comparables).
#
# - Redige le : 2026-10-27 ; donnees arretees au 2026-10-27
# - Auteur : sous-agent Opus, etape 5 bis ; statut : brouillon
#
# SOURCE DES DONNEES (jeux open data de l'Assemblee nationale), telechargees le 2026-10-27 :
#   - Scrutins XVIIe (archive de 28 199 155 octets) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/scrutins/Scrutins.json.zip
#   - Scrutins XVIe (contexte, 10 107 912 octets) :
#     https://data.assemblee-nationale.fr/static/openData/repository/16/loi/scrutins/Scrutins.json.zip
#   - Scrutins XIVe (bloc b, mandat 2012-2017, 671 420 octets) :
#     https://data.assemblee-nationale.fr/static/openData/repository/14/loi/scrutins/Scrutins_XIV.json.zip
#   - Amendements XVIIe (347 569 058 octets, 142 526 fichiers) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/amendements_div_legis/Amendements.json.zip
#   - Acteurs, AMO30 (reconnaitre les deputes socialistes parmi les auteurs des motions) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
#   - Dossiers legislatifs XIVe (sort du projet de loi constitutionnelle sur la democratie sociale) :
#     https://data.assemblee-nationale.fr/static/openData/repository/14/loi/dossiers_legislatifs/Dossiers_Legislatifs_XIV.json.zip
#
# Usage :
#   python3 -I _scripts/calculs/ps_methode_parlement.py scrutins17.zip scrutins16.zip scrutins14.zip amendements17.zip amo30.zip dl14.zip [Leg_2017_Resultats_T1_c.xlsx]
#   (7e argument : https://static.data.gouv.fr/resources/elections-legislatives-des-11-et-18-juin-2017-resultats-du-1er-tour/20170613-095447/Leg_2017_Resultats_T1_c.xlsx)
#
# HYPOTHESES (identiques aux scripts LFI et RN sauf mention) :
#   - Groupes : SOC = PO845419 (XVIIe) ; XVIe : PO800496 (2022-06-28 au 2023-10-18) puis PO830170 ;
#     XIVe : SRC = PO656002 (2012-06-26 au 2016-05-24) puis PO713077 (Socialiste, ecologiste et republicain).
#   - Motions de censure : objet contenant "motion de censure" ; "sur un 49.3" = "alinea 3" ;
#     "premier signataire SOC" = premier nom cite dans l'objet est celui d'un depute ayant appartenu au groupe ;
#     "cosignee" = un depute du groupe cite dans l'objet ; "votee" = plus de la moitie des membres pour.
#   - Motions de rejet prealable : auteur = depute du groupe cite apres "deposee par".
#   - Amendements : groupe du premier signataire ; commission et seance, toutes lectures ; effectifs au scrutin 8707.
import json, re, sys, zipfile, collections

SOC17 = "PO845419"
SOC16 = {"PO800496", "PO830170"}
SRC14 = {"PO656002", "PO713077"}
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
            else:  # XIVe : un seul fichier
                for s in d["scrutins"]["scrutin"]:
                    out[int(s["numero"])] = s
    return out


def vote(s, orgs):
    p = c = a = eff = 0
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        if g["organeRef"] in orgs:
            d = g["vote"]["decompteVoix"]
            p += int(d.get("pour") or 0); c += int(d.get("contre") or 0)
            a += int(d.get("abstentions") or d.get("abstention") or 0); eff += int(g["nombreMembresGroupe"])
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
    print(f"[{leg}] premier signataire socialiste : {len(prem)} : "
          f"{[(r['num'], r['date'], 'a3' if r['a3'] else 'a2', r['total'], r['pour']) for r in prem]}")
    cos = [r for r in rows if r["cosig"] and not r["premier"]]
    print(f"[{leg}] cosignees sans premier signataire socialiste : {[(r['num'], r['date'], r['pour']) for r in cos]}")
    print(f"[{leg}] votees par le groupe socialiste : {sum(r['vote'] for r in rows)} sur {len(rows)}")
    print(f"[{leg}] non votees : {[(r['num'], r['date'], 'a3' if r['a3'] else 'a2', r['pour'], r['eff']) for r in rows if not r['vote']]}")
    a3 = [r for r in rows if r["a3"]]
    print(f"[{leg}] motions sur un 49.3 : {len(a3)} ; votees par le groupe : {sum(r['vote'] for r in a3)} "
          f"{[(r['num'], r['date'], r['pour']) for r in a3]}")
    print(f"[{leg}] adoptees : {[r['num'] for r in rows if r['sort'] == 'adopté']}")
    return rows


def rejets(sc, orgs, noms, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = s["objet"]["libelle"] or ""
        if re.search(r"motion de rejet p[ré]*alable", o.lower()):
            auteurs = o.split("déposée par", 1)[-1].split(", d", 1)[0] if "déposée par" in o else ""
            p, c, a, eff = vote(s, orgs)
            rows.append((num, s["dateScrutin"], bool(cite(auteurs, noms)), p > c, c > p, s["sort"]["code"], o))
    soc = [r for r in rows if r[2]]
    print(f"[{leg}] motions de rejet prealable votees : {len(rows)} ; deposees par un depute socialiste : {len(soc)} "
          f"{[(r[0], r[1], r[5], r[6][:90]) for r in soc]}")
    autres = [r for r in rows if not r[2]]
    print(f"[{leg}] motions d'autres groupes : {len(autres)} ; groupe pour : {sum(r[3] for r in autres)} ; "
          f"groupe contre : {[(r[0], r[1], r[6][60:150]) for r in autres if r[4]]}")


def referendaires(sc, leg, orgs):
    rows = [(n, s["dateScrutin"], vote(s, orgs), s["objet"]["libelle"][:110]) for n, s in sorted(sc.items())
            if "référendaire" in (s["objet"]["libelle"] or "").lower()]
    print(f"[{leg}] motions referendaires : {len(rows)} {rows}")


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
        for g in ["SOC", "LFI", "RN", "EPR", "DR", "ECOS", "GDR", "LIOT", "DEM", "HOR", "UDR"]:
            if c.get(g) and m.get(g):
                print(f"    {g:5s} {c[g]:6d}  {100*c[g]/t:5.1f} % des amendements  {100*m[g]/577:5.1f} % des sieges"
                      f"  {c[g]/m[g]:6.1f} par depute")
    table("legislature entiere", tot, 8707)
    for label, dossier, nscr in TEXTES:
        table(label, par_dossier[dossier], nscr)
    top = sorted(par_dossier.items(), key=lambda kv: -kv[1]["SOC"])[:6]
    print("[amendements] dossiers ou SOC depose le plus (dossier, SOC, total, part SOC) :")
    for d, c in top:
        print(f"    {d}  {c['SOC']:6d}  {sum(c.values()):6d}  {100*c['SOC']/sum(c.values()):5.1f} %")


def mandat_2012(s14, dl14):
    # Bloc (b) : situation de majorite du groupe socialiste et votes cles de la XIVe.
    print("[XIVe] effectif SRC puis SER (sieges sur 577, majorite absolue 289) aux scrutins cles :")
    for num in [259, 481, 559, 1191, 1237, 1238, 1326]:
        s = s14[num]; p, c, a, eff = vote(s, SRC14)
        print(f"    {num} {s['dateScrutin']} effectif {eff} ; pour {p} contre {c} abst {a} ; {s['objet']['libelle'][:95]}")
    for num in [1044, 1133, 1270]:
        s = s14[num]; p, c, a, eff = vote(s, SRC14)
        print(f"    censure {num} {s['dateScrutin']} : {s['syntheseVote']['decompte']['pour']} voix pour ; socialistes pour : {p}")
    # 49.3 du gouvernement Valls (sources de presse, voir le chapitre) : loi Macron 3, loi travail 3.
    uses = [("2015-02-17", "loi Macron, 1re lecture"), ("2015-06 (mi-juin)", "loi Macron, nouvelle lecture"),
            ("2015-07-09", "loi Macron, lecture definitive"), ("2016-05-10", "loi travail, 1re lecture"),
            ("2016-07-05", "loi travail, nouvelle lecture"), ("2016-07-20", "loi travail, lecture definitive")]
    print(f"[XIVe] engagements de responsabilite (49.3) : {len(uses)} sur 2 textes ; dont motion votee : 3 ; "
          f"part des 49.3 suivis d'une motion : {100*3/len(uses):.0f} %")
    print(f"[XIVe] frondeurs, motion de gauche de mai et juillet 2016 : 56 signatures sur 58 requises, il en manque {58-56}")
    p, c, a, eff = vote(s14[1237], SRC14)
    print(f"[XIVe] revision constitutionnelle (1237) : socialistes contre ou abstention {c+a} sur {eff} ({100*(c+a)/eff:.1f} %)")
    p, c, a, eff = vote(s14[481], SRC14)
    print(f"[XIVe] loi de securisation de l'emploi (481) : socialistes contre ou abstention {c+a} sur {eff} ({100*(c+a)/eff:.1f} %)")
    raw = json.loads(zipfile.ZipFile(dl14).read("Dossiers_Legislatifs_XIV.json"))
    for D in raw["export"]["dossiersLegislatifs"]["dossier"]:
        dp = D["dossierParlementaire"]
        if dp["titreDossier"]["titre"] == "Pouvoirs publics : démocratie sociale":
            acc = []
            def walk(x):
                if isinstance(x, dict):
                    if "codeActe" in x: acc.append(x["codeActe"])
                    for v in x.values(): walk(v)
                elif isinstance(x, list):
                    for v in x: walk(v)
            walk(dp.get("actesLegislatifs"))
            print(f"[XIVe] PJL constitutionnelle democratie sociale : actes {sorted(set(acc))} ; seance publique : "
                  f"{any('DEBATS' in x for x in acc)}")


def candidats_2017(xlsx):
    # Ministere de l'Interieur, Leg_2017_Resultats_T1_c.xlsx (data.gouv.fr), feuille "Circo. leg. T1" :
    # cellules portant la nuance "SOC" (une par candidat). Controle : FI 557, REM 468, MDM 69 (chapitres LFI et Renaissance).
    z = zipfile.ZipFile(xlsx)
    ss = [re.sub(r"<[^>]+>", "", x) for x in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    x = z.read("xl/worksheets/sheet4.xml").decode()
    c = collections.Counter(ss[int(v)] for v in re.findall(r'<c r="[A-Z]+\d+"[^>]*t="s"[^>]*><v>(\d+)</v>', x))
    print(f"[2017] candidats de nuance SOC au premier tour : {c['SOC']} (controle : FI {c['FI']}, REM {c['REM']}, MDM {c['MDM']})")
    return c["SOC"]


def complements(soc2017=413):
    from datetime import date
    pct = lambda a, b: f"{100 * a / b:.1f} %"
    print("[b] consultation NDDL 2016-06-26 : oui 55,17 %, participation 51,08 % (source) ; delai jusqu'a l'abandon de l'evacuation"
          " promise (2016-12-09) :", (date(2016, 12, 9) - date(2016, 6, 26)).days, "jours")
    print("[b] age des faits au 2026-10-27 (annees) :")
    for lab, d in [("ANI / loi securisation emploi", date(2013, 6, 14)), ("49.3 loi Macron (1er)", date(2015, 2, 17)),
                   ("49.3 loi travail (1er)", date(2016, 5, 10)), ("49.3 loi travail (dernier)", date(2016, 7, 20)),
                   ("abandon revision constitutionnelle", date(2016, 3, 30)), ("report evacuation NDDL", date(2016, 12, 9)),
                   ("5e prorogation etat d'urgence (avis CNCDH publie)", date(2017, 3, 4)), ("ecotaxe suspendue", date(2013, 10, 29)),
                   ("grenades offensives interdites", date(2014, 11, 13))]:
        print(f"    {lab} : {(date(2026, 10, 27) - d).days / 365.25:.1f}")
    print("[b] seuil des dix ans : faits posterieurs au", date(2016, 10, 27))
    print("[d] delai information de la direction (2026-09-15 au soir) -> suspension conservatoire (BN du 2026-09-16) :",
          (date(2026, 9, 16) - date(2026, 9, 15)).days, "jour")
    print("[d] Dordogne : article de presse du 2025-12-10, exclusion le mardi 2025-12-09 ; commentaire publie 'la semaine derniere'"
          " : delai de publication a exclusion de", (date(2025, 12, 9) - date(2025, 12, 4)).days, "jours au plus (article commente du 4 decembre)")
    for elec, n, k in [("legislatives 2017 (nuance SOC)", soc2017, 0), ("legislatives 2022 (part PS de la NUPES)", 70, 0),
                       ("legislatives 2024 (part PS du NFP)", 175, 0)]:
        print(f"[d] {elec} : {n} candidats ; cas admis : {k}")
    print("[c] motions de rejet prealable deposees par SOC :", pct(6, 60), "; par LFI (chapitre LFI) :", pct(43, 60))
    print("[c] motions de censure votees par SOC :", pct(4, 23), "; sur un 49.3 :", pct(1, 11), "(1 sur 8 recours)")
    print("[b] effectif socialiste en 2016 (287) rapporte a la majorite absolue (289) : manque", 289 - 287)


if __name__ == "__main__":
    if len(sys.argv) not in (7, 8):
        sys.exit("usage : ps_methode_parlement.py <scrutins17.zip> <scrutins16.zip> <scrutins14.zip> <amendements17.zip> <amo30.zip> <dl14.zip> [Leg_2017_Resultats_T1_c.xlsx]")
    s17, s16, s14 = scrutins(sys.argv[1]), scrutins(sys.argv[2]), scrutins(sys.argv[3])
    n17 = noms_groupe(sys.argv[5], {SOC17})
    n16 = noms_groupe(sys.argv[5], SOC16)
    print(f"deputes reconnus : SOC XVIIe {len(n17)} ; SOC XVIe {len(n16)}")
    censures(s17, {SOC17}, n17, "XVIIe")
    censures(s16, SOC16, n16, "XVIe")
    rejets(s17, {SOC17}, n17, "XVIIe")
    rejets(s16, SOC16, n16, "XVIe")
    referendaires(s17, "XVIIe", {SOC17})
    referendaires(s16, "XVIe", SOC16)
    mandat_2012(s14, sys.argv[6])
    amendements(sys.argv[4], s17)
    complements(candidats_2017(sys.argv[7]) if len(sys.argv) == 8 else 413)
