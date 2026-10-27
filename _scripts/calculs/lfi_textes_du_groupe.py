# Calcul par nos soins : qualification « texte du groupe » ou « texte d'élus du groupe » des textes
# parlementaires du corpus LFI (C-LFI-45 à C-LFI-66), selon la règle du socle
# (01-socle/01-criteres.md §6, précision du 2026-10-27).
#
# - Objet : pour chaque texte à liste nominative de signataires, compter les signataires qui sont
#   membres du groupe LFI-NFP à la date du dépôt, rapporter au nombre de membres du groupe à cette
#   date, et appliquer le seuil de 90 %. Un texte qui s'appuie sur la formule « les membres du groupe »
#   (note de bas de page « Ce groupe est composé de ») compte la liste de cette note.
# - Rédigé le : 2026-10-27 ; données arrêtées au 2026-10-26.
# - Source des effectifs : jeu open data AMO30 de l'Assemblée nationale (acteurs, mandats, organes),
#   https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
#   (à décompresser ; le groupe de la XVIIe législature est l'organe de libellé abrégé « LFI-NFP »).
#   Effectif = membres, président et apparentés (mandats de type GP), comme la note « Ce groupe est composé de ».
# - Source des signataires : bloc « présenté(e) par » des PDF archivés dans 02-partis/lfi/corpus/
#   (extraction pdftotext, à installer : poppler).
# - Usage : python3 -I _scripts/calculs/lfi_textes_du_groupe.py <dossier AMO30 décompressé contenant acteur/ et organe/>
#   (lancé depuis la racine du dépôt ; sans argument, lit le dossier de travail de la session).
# - Sortie : une ligne par texte (identifiant, signataires du groupe, effectif à la date, part, verdict),
#   puis le détail des signataires qui ne sont pas membres du groupe à la date.

import glob
import json
import os
import re
import subprocess
import sys
import unicodedata

DEFAUT = ("/private/tmp/claude-501/-Users-dilhan-Documents-Politique-elections-france-2027/"
          "bd3ce823-20df-45ea-b09c-ea2fe350a07c/scratchpad/amo30/json")
AMO = sys.argv[1] if len(sys.argv) > 1 else DEFAUT
CORPUS = "02-partis/lfi/corpus"
SEUIL = 0.90

# (identifiant, intitulé, date de dépôt, fragment du nom de fichier)
TEXTES = [
    ("C-LFI-45", "PPL 1834", "2025-09-16", "C-LFI-45-"),
    ("C-LFI-46", "Motion de censure 2025-05-30", "2025-05-30", "C-LFI-46-"),
    ("C-LFI-47", "PPL 438", "2024-10-15", "C-LFI-47-"),
    ("C-LFI-48", "PPL 2564", "2026-03-03", "C-LFI-48-"),
    ("C-LFI-49", "Amdt 283 PJL 2250", "2026-02-19", "C-LFI-49-"),
    ("C-LFI-50", "PPLC 1374", "2025-05-07", "C-LFI-50-"),
    ("C-LFI-51", "PPLC 2124", "2025-11-20", "C-LFI-51-"),
    ("C-LFI-52", "PPRE 467", "2024-10-18", "C-LFI-52-"),
    ("C-LFI-53", "PPL 3176", "2026-09-15", "C-LFI-53-"),
    ("C-LFI-54", "PPL 2893", "2026-06-09", "C-LFI-54-"),
    ("C-LFI-55", "PPL 2591", "2026-03-27", "C-LFI-55-"),
    ("C-LFI-56", "Amdt I-CF1275 PLF 2027", "2026-10-04", "C-LFI-56-"),
    ("C-LFI-57", "Amdt I-CF847 PLF 2027", "2026-10-04", "C-LFI-57-"),
    ("C-LFI-58", "PPL 1212", "2025-04-01", "C-LFI-58-"),
    ("C-LFI-59", "PPL 1317", "2025-04-17", "C-LFI-59-"),
    ("C-LFI-60", "PPL 577", "2024-11-19", "C-LFI-60-"),
    ("C-LFI-61", "Amdt II-3202 PLF 2025", "2024-11-08", "C-LFI-61-"),
    ("C-LFI-62", "PPR 1780", "2025-09-11", "C-LFI-62-"),
    ("C-LFI-63", "PPLC 722", "2024-12-17", "C-LFI-63-"),
    ("C-LFI-64", "PPR 788", "2025-01-21", "C-LFI-64-"),
    ("C-LFI-65", "PPR 2354", "2026-01-20", "C-LFI-65-"),
    ("C-LFI-66", "PPR 2044", "2025-10-29", "C-LFI-66-"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[-'’]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def uid_de(a):
    u = a["uid"]
    return u["#text"] if isinstance(u, dict) else u


# --- Effectif du groupe par date ---
groupe_uid = None
for f in glob.glob(os.path.join(AMO, "organe", "*.json")):
    o = json.load(open(f))["organe"]
    if o.get("libelleAbrev") == "LFI-NFP":
        groupe_uid = o["uid"]
acteurs = {}  # uid -> (prenom, nom, [(debut, fin)])
for f in glob.glob(os.path.join(AMO, "acteur", "*.json")):
    a = json.load(open(f))["acteur"]
    ident = a["etatCivil"]["ident"]
    m = a["mandats"]["mandat"]
    m = [m] if isinstance(m, dict) else m
    per = [(x["dateDebut"], x.get("dateFin")) for x in m
           if x.get("typeOrgane") == "GP" and x.get("organes", {}).get("organeRef") == groupe_uid]
    acteurs[uid_de(a)] = (ident["prenom"], ident["nom"], per)


def membres_a(date):
    r = []
    for u, (p, n, per) in acteurs.items():
        if any(d <= date and (fin is None or date <= fin) for d, fin in per):
            r.append((u, p, n))
    return r


def pdf_texte(fragment):
    fichiers = glob.glob(os.path.join(CORPUS, fragment + "*.pdf"))
    if len(fichiers) != 1:
        raise SystemExit("PDF introuvable ou ambigu : " + fragment)
    return subprocess.run(["pdftotext", "-layout", fichiers[0], "-"], capture_output=True, text=True).stdout


def nettoyer(t):
    t = re.sub(r"\u2013\s*\d+\s*\u2013", " ", t)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"-\s+", "-", t)


def bloc(texte):
    """Retourne (bloc présenté par, note du groupe ou '')."""
    t = nettoyer(texte)
    m = re.search(r"pr[ée]sent[ée]e? par", t)
    t = t[m.end():]
    fin = re.search(r"EXPOS[ÉE]|Mesdames|ARTICLE|-{5,}|PROPOSITION|R[ÉE]SOLUTION|Article", t)
    if fin:
        t = t[:fin.start()]
    note = ""
    n = re.search(r"\(1\)\s*Ce groupe est compos[ée] de\s*:", t)
    if n:
        note = t[n.end():]
        t = t[:n.start()]
    return t, note


def entrees(t):
    t = re.split(r"les membres du groupe|d[ée]put[ée]|\(d[ée]pos[ée]e", t)[0]
    t = re.sub(r"et \d+ de ses coll[èe]gues", " ", t)
    morceaux = re.split(r"(?=\b(?:Mme|M\.)\s)", t)
    out = []
    for c in morceaux:
        c = re.sub(r"^(Mme|M\.)\s+", "", c.strip())
        c = re.sub(r"(,|\.|\s+et)\s*$", "", c.strip()).strip(" ,.")
        c = re.sub(r"\s+et$", "", c).strip()
        if c:
            out.append(c)
    return out


def apparier(ents, membres):
    pleins, noms = {}, {}
    for u, p, n in membres:
        pleins[norm(p + " " + n)] = u
        noms.setdefault(norm(n), []).append(u)
    trouves, autres = set(), []
    for e in ents:
        k = norm(e)
        if k in pleins:
            trouves.add(pleins[k])
        elif k in noms and len(noms[k]) == 1:
            trouves.add(noms[k][0])
        else:
            autres.append(e)
    return trouves, autres


def main():
    print("Groupe LFI-NFP :", groupe_uid)
    resultats = []
    for ident, titre, date, frag in TEXTES:
        membres = membres_a(date)
        M = len(membres)
        t, note = bloc(pdf_texte(frag))
        ents = entrees(t)
        trouves, autres = apparier(ents, membres)
        formule = bool(note)
        if formule:
            n_note, _ = apparier(entrees(note.split("députés")[0]), membres)
            trouves = trouves | n_note
        N = len(trouves)
        part = N / M
        trans = [a for a in autres]
        if formule and not trans:
            verdict = "groupe (formule « les membres du groupe » ; liste de la note)"
        elif part >= SEUIL:
            verdict = "groupe (>= 90 %)"
        else:
            verdict = "élus du groupe (< 90 %)"
        if trans:
            verdict += " ; transpartisan : " + ", ".join(trans)
        resultats.append((ident, titre, date, N, M, part, verdict, len(ents)))
        total = "" if formule else f" | signataires au total {len(ents)}"
        print(f"{ident} | {titre} | dépôt {date} | signataires du groupe {N} | effectif {M} | "
              f"part {part*100:.1f} % | {verdict}{total}")
        manquants = sorted(f"{p} {n}" for u, p, n in membres if u not in trouves)
        if manquants and not formule:
            print("   membres du groupe non signataires :", "; ".join(manquants))
    print()
    print("Total textes :", len(resultats),
          "| du groupe :", sum(1 for r in resultats if r[6].startswith("groupe")),
          "| d'élus du groupe :", sum(1 for r in resultats if r[6].startswith("élus")))


main()
