# Calculs par nos soins pour 02-partis/lfi/methode.md, bloc (c) "Le comportement parlementaire".
# Modele : _scripts/calculs/rn_methode_parlement.py (memes jeux, memes regles, pour que les deux
# chapitres soient comparables).
#
# - Redige le : 2026-10-26 ; donnees arretees au 2026-10-26
# - Auteur : sous-agent Opus, etape 5 bis ; statut : brouillon
#
# SOURCE DES DONNEES (jeux open data de l'Assemblee nationale) :
#   - Scrutins XVIIe legislature (9 097 scrutins, n. 1 a 9 097, dernier date du 2026-10-23),
#     archive de 28 199 162 octets (meme taille que celle lue pour le RN le 2026-10-25), telechargee le 2026-10-26 :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/scrutins/Scrutins.json.zip
#   - Scrutins XVIe legislature (contexte seulement), telechargee le 2026-10-26 (10 107 912 octets) :
#     https://data.assemblee-nationale.fr/static/openData/repository/16/loi/scrutins/Scrutins.json.zip
#   - Amendements XVIIe legislature, telechargee le 2026-10-26 (346 844 201 octets ; 346 819 259 octets le
#     2026-10-25 pour le RN : le jeu est mis a jour en continu, les chiffres bougent de quelques unites) :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/loi/amendements_div_legis/Amendements.json.zip
#   - Acteurs (pour reconnaitre les deputes LFI-NFP parmi les auteurs des motions de rejet), AMO30 :
#     https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
#
# DONNEES BRUTES : non versionnees (taille). Les retelecharger aux URL ci-dessus, puis :
#   python3 -I _scripts/calculs/lfi_methode_parlement.py scrutins17.zip scrutins16.zip amendements17.zip amo30.zip [Leg_2017_Resultats_T1_c.xlsx]
#   (5e argument facultatif : resultats du 1er tour des legislatives 2017, ministere de l'Interieur,
#   https://static.data.gouv.fr/resources/elections-legislatives-des-11-et-18-juin-2017-resultats-du-1er-tour/20170613-095447/Leg_2017_Resultats_T1_c.xlsx)
# (les archives zip sont lues directement, sans decompression).
#
# HYPOTHESES (identiques au script RN sauf mention) :
#   - Groupes par code d'organe : LFI-NFP = PO845413 (XVIIe), LFI-NUPES = PO800490 (XVIe) ; autres codes
#     comme dans le script RN.
#   - Motions de censure : objet contenant "motion de censure" ; "sur un 49.3" = objet contenant "alinea 3" ;
#     "premier signataire LFI" = le premier nom cite dans l'objet est celui d'un depute LFI-NFP ;
#     "cosignee par LFI" = un depute LFI-NFP est cite dans l'objet ; "votee par LFI" = plus de la moitie
#     des membres du groupe pour.
#   - Motions de rejet prealable : objet contenant "motion de rejet prealable" (orthographes fautives
#     incluses) ; auteur LFI = un depute LFI-NFP cite apres "deposee par".
#   - Amendements : attribues au groupe du premier signataire ; commission et seance, toutes lectures ;
#     "par depute" de legislature avec les effectifs au scrutin 8707 (2026-10-13), approximation.
import json, re, sys, zipfile, collections

LFI17, LFI16 = "PO845413", "PO800490"
NOMS = {"PO845401": "RN", "PO845413": "LFI", "PO845419": "SOC", "PO845407": "EPR", "PO845425": "DR",
        "PO845439": "ECOS", "PO845454": "DEM", "PO845470": "HOR", "PO845485": "LIOT", "PO845514": "GDR",
        "PO872880": "UDR", "PO847173": "UDR", "PO840056": "NI"}
# Titres lus dans le jeu "Dossiers legislatifs" de la XVIIe (telecharge le 2026-10-26).
TITRES = {"DLR5L17N52655": "PPLO report des elections provinciales en Nouvelle-Caledonie",
          "DLR5L17N52984": "PJL constitutionnelle relatif a la Nouvelle-Caledonie",
          "DLR5L17N50819": "PPL lever les contraintes a l'exercice du metier d'agriculteur (dite Duplomb)",
          "DLR5L17N50588": "PLFSS 2025", "DLR5L17N54951": "PLFSS 2027", "DLR5L17N52428": "PLF 2026",
          "DLR5L17N50198": "PLF 2025", "DLR5L17N54629": "PLF 2027", "DLR5L17N52922": "PLFSS 2026",
          "DLR5L16N47697": "reforme de l'audiovisuel public", "DLR5L17N54085": "PJL urgence agricole",
          "DLR5L16N49075": "PPL mariages simules"}
DETAIL = ["DLR5L17N50819", "DLR5L17N52655", "DLR5L17N52984"]
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


def vote(s, org):
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        if g["organeRef"] == org:
            d = g["vote"]["decompteVoix"]
            return int(d["pour"] or 0), int(d["contre"] or 0), int(d["abstentions"] or 0), int(g["nombreMembresGroupe"])
    return 0, 0, 0, 0


def effectifs(s):
    m = collections.Counter()
    for g in s["ventilationVotes"]["organe"]["groupes"]["groupe"]:
        m[NOMS.get(g["organeRef"], g["organeRef"])] += int(g["nombreMembresGroupe"])
    return m


def noms_lfi(amo_zip, codes):
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


def censures(sc, org, noms, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = s["objet"]["libelle"] or ""
        if "motion de censure" in o.lower():
            p, c, a, eff = vote(s, org)
            prem = premier_nom(o)
            rows.append(dict(num=num, date=s["dateScrutin"], a3="alinéa 3" in o.lower(),
                             premier=bool(cite(prem, noms)), cosig=bool(cite(o, noms)),
                             vote=p > eff / 2, pour=p, eff=eff, sort=s["sort"]["code"],
                             total=int(s["syntheseVote"]["decompte"]["pour"])))
    print(f"[{leg}] motions de censure votees : {len(rows)} ; sur un 49.3 : {sum(r['a3'] for r in rows)}")
    prem = [r for r in rows if r["premier"]]
    print(f"[{leg}] premier signataire LFI : {len(prem)} (dont {sum(r['a3'] for r in prem)} sur un 49.3) : "
          f"{[(r['num'], r['date'], 'a3' if r['a3'] else 'a2', r['total']) for r in prem]}")
    cos = [r for r in rows if r["cosig"] and not r["premier"]]
    print(f"[{leg}] cosignees par LFI sans premier signataire LFI : {[(r['num'], r['date']) for r in cos]}")
    print(f"[{leg}] votees par LFI : {sum(r['vote'] for r in rows)} sur {len(rows)} ; "
          f"non votees : {[(r['num'], r['date'], r['pour']) for r in rows if not r['vote']]}")
    a3 = [r for r in rows if r["a3"] and not r["cosig"]]
    print(f"[{leg}] motions sur un 49.3 sans signataire LFI : {len(a3)} ; votees par LFI : {sum(r['vote'] for r in a3)}")
    print(f"[{leg}] adoptees : {[r['num'] for r in rows if r['sort'] == 'adopté']}")


def rejets(sc, org, noms, leg):
    rows = []
    for num, s in sorted(sc.items()):
        o = s["objet"]["libelle"] or ""
        if re.search(r"motion de rejet p[ré]*alable", o.lower()):
            auteurs = o.split("déposée par", 1)[-1].split(", d", 1)[0] if "déposée par" in o else ""
            p, c, a, eff = vote(s, org)
            rows.append((num, s["dateScrutin"], bool(cite(auteurs, noms)), p > c, c > p, s["sort"]["code"], o))
    lfi = [r for r in rows if r[2]]
    print(f"[{leg}] motions de rejet prealable votees : {len(rows)} ; deposees par LFI : {len(lfi)} "
          f"({100 * len(lfi) / len(rows):.1f} %) ; dont adoptees : {sum(r[5] == 'adopté' for r in lfi)} "
          f"{[r[0] for r in lfi if r[5] == 'adopté']}")
    autres = [r for r in rows if not r[2]]
    print(f"[{leg}] motions d'autres groupes : {len(autres)} ; LFI pour : {sum(r[3] for r in autres)} ; "
          f"LFI contre : {[(r[0], r[1]) for r in autres if r[4]]}")
    fin = [r for r in lfi if re.search(r"loi de finances|financement de la sécurité sociale|fin de gestion|fin des gestion", r[6])]
    print(f"[{leg}] motions LFI sur des textes financiers (PLF, PLFSS, fin de gestion) : {len(fin)} "
          f"{[(r[0], r[1]) for r in fin]}")
    cpt = [r for r in lfi if re.search(r"comptes|résultats de la gestion", r[6])]
    print(f"[{leg}] motions LFI sur l'approbation des comptes : {len(cpt)} {[(r[0], r[5]) for r in cpt]}")


def referendaires(sc, leg, org):
    rows = [(n, s["dateScrutin"], vote(s, org)[0], s["objet"]["libelle"][:120]) for n, s in sorted(sc.items())
            if "référendaire" in (s["objet"]["libelle"] or "").lower()]
    print(f"[{leg}] motions referendaires : {len(rows)} {rows}")


def amendements(zpath, sc):
    z = zipfile.ZipFile(zpath)
    tot, par_dossier = collections.Counter(), collections.defaultdict(collections.Counter)
    par_texte = collections.defaultdict(collections.Counter)
    for n in z.namelist():
        if not n.endswith(".json"):
            continue
        a = json.loads(z.read(n))["amendement"]
        au = a["signataires"]["auteur"]
        g = au.get("groupePolitiqueRef")
        g = NOMS.get(g, g) if isinstance(g, str) else ("GOUV" if au.get("typeAuteur") == "Gouvernement" else "autre")
        tot[g] += 1
        parts = n.split("/")
        par_dossier[parts[1]][g] += 1
        if parts[1] in DETAIL:
            par_texte[(parts[1], parts[2])][g] += 1

    def table(label, c, nscr):
        t = sum(c.values()); m = effectifs(sc[nscr])
        print(f"[amendements] {label} : total {t} (effectifs au scrutin {nscr})")
        for g in ["LFI", "RN", "SOC", "EPR", "DR", "ECOS", "GDR", "LIOT", "DEM", "HOR", "UDR"]:
            if c.get(g) and m.get(g):
                print(f"    {g:5s} {c[g]:6d}  {100*c[g]/t:5.1f} % des amendements  {100*m[g]/577:5.1f} % des sieges"
                      f"  {c[g]/m[g]:6.1f} par depute")
    table("legislature entiere", tot, 8707)
    for label, dossier, nscr in TEXTES:
        table(label, par_dossier[dossier], nscr)
    top = sorted(par_dossier.items(), key=lambda kv: -kv[1]["LFI"])[:12]
    print("[amendements] dossiers ou LFI depose le plus (dossier, LFI, total, part LFI) :")
    for d, c in top:
        print(f"    {d}  {c['LFI']:6d}  {sum(c.values()):6d}  {100*c['LFI']/sum(c.values()):5.1f} %  {TITRES.get(d, '')}")
    print("[amendements] detail par texte (BTC = texte de la commission, examine en seance) :")
    for (d, t), c in sorted(par_texte.items()):
        print(f"    {TITRES[d]} / {t} : total {sum(c.values())} ; {c.most_common(4)}")


def candidats_fi_2017(xlsx):
    # Ministere de l'Interieur, Leg_2017_Resultats_T1_c.xlsx, feuille "Circo. leg. T1" (xl/worksheets/sheet4.xml) :
    # nombre de cellules portant la nuance "FI" (une par candidat). Controle : la meme lecture donne 468 REM et
    # 69 MDM, les chiffres du chapitre Renaissance (source 81).
    z = zipfile.ZipFile(xlsx)
    ss = [re.sub(r"<[^>]+>", "", x) for x in re.findall(r"<si>(.*?)</si>", z.read("xl/sharedStrings.xml").decode(), re.S)]
    x = z.read("xl/worksheets/sheet4.xml").decode()
    c = collections.Counter(ss[int(v)] for v in re.findall(r'<c r="[A-Z]+\d+"[^>]*t="s"[^>]*><v>(\d+)</v>', x))
    print(f"[2017] candidats de nuance FI au premier tour : {c['FI']} (controle : REM {c['REM']}, MDM {c['MDM']})")
    return c["FI"]


def complements(fi2017):
    # Valeurs lues dans les sources du chapitre (numeros entre crochets dans 02-partis/lfi/methode.md).
    from datetime import date
    pct = lambda a, b: f"{100 * a / b:.1f} %"
    print("[c] part des motions de censure de la legislature dont LFI est premier signataire :", pct(11, 23))
    print("[c] part des motions de rejet prealable deposees par LFI :", pct(43, 60))
    print("[c] amendements LFI sur la PPLO Nouvelle-Caledonie (texte de la commission) :", pct(1624, 1659))
    print("[c] amendements LFI sur la loi Duplomb en seance :", pct(827, 3460), "; ECOS :", pct(1541, 3460))
    print("[c] amendements LFI et GDR sur le PJL constitutionnel Nouvelle-Caledonie :", pct(1450 + 1406, 3205))
    for txt, lfi, rn in [("PLF 2025", 35.0, 15.1), ("PLF 2026", 35.9, 25.1), ("PLFSS 2026", 15.9, 3.2), ("PLF 2027", 17.0, 10.4)]:
        print(f"[c] {txt} : amendements par depute LFI / RN (valeurs de la table ci-dessus) : {lfi / rn:.1f}")
    print("[c] PPR 178 en commission des lois : pour 15, contre 54 ; part pour :", pct(15, 69))
    print("[a] vote sur la feuille de route d'avril 2026 : pour", pct(65810, 68120), "; sans position", pct(1493, 68120),
          "; contre", pct(817, 68120), "; total controle :", 65810 + 1493 + 817)
    print("[a] parrainages citoyens au 2026-10-08 rapportes au seuil de 150 000 :", round(400000 / 150000, 2), "fois")
    print("[d] delai investiture -> retrait, 14e du Rhone 2022 (7 au 10 mai) :", (date(2022, 5, 10) - date(2022, 5, 7)).days, "jours")
    print("[d] delai publication -> retrait, 1re du Loir-et-Cher 2024 (26 au 27 juin) :", (date(2024, 6, 27) - date(2024, 6, 26)).days, "jour")
    print("[d] retrait avant le premier tour (27 au 30 juin 2024) :", (date(2024, 6, 30) - date(2024, 6, 27)).days, "jours")
    for elec, n in [("legislatives 2017 (nuance FI)", fi2017), ("legislatives 2022 (part LFI de la NUPES)", 328),
                    ("legislatives 2024 (liste LFI du 14 juin)", 230)]:
        print(f"[d] {elec} : {n} candidats")
    print("[d] 2024 : cas admis 1 sur 230 :", pct(1, 230), "; 2022 : 1 sur 328 :", pct(1, 328), "; 2017 : 0 sur", fi2017)
    print("[d] sortants non reinvestis en 2024 : 5 ; part des 230 investitures :", pct(5, 230))


if __name__ == "__main__":
    if len(sys.argv) not in (5, 6):
        sys.exit("usage : lfi_methode_parlement.py <scrutins17.zip> <scrutins16.zip> <amendements17.zip> <amo30.zip> [Leg_2017_Resultats_T1_c.xlsx]")
    s17, s16 = scrutins(sys.argv[1]), scrutins(sys.argv[2])
    n17 = noms_lfi(sys.argv[4], {LFI17})
    n16 = noms_lfi(sys.argv[4], {LFI16})
    print(f"deputes LFI-NFP reconnus (XVIIe, tous ceux qui ont ete membres) : {len(n17)} ; LFI-NUPES (XVIe) : {len(n16)}")
    censures(s17, LFI17, n17, "XVIIe")
    censures(s16, LFI16, n16, "XVIe")
    rejets(s17, LFI17, n17, "XVIIe")
    rejets(s16, LFI16, n16, "XVIe")
    referendaires(s17, "XVIIe", LFI17)
    referendaires(s16, "XVIe", LFI16)
    amendements(sys.argv[3], s17)
    complements(candidats_fi_2017(sys.argv[5]) if len(sys.argv) == 6 else 557)
