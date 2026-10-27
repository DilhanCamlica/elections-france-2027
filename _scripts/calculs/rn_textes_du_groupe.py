#!/usr/bin/env python3
"""Contrôle de l'auteur des textes du corpus RN à liste nominative de signataires.

Objet : appliquer la règle de `01-socle/01-criteres.md` §6 (précision du 2026-10-27) :
un texte à liste nominative est « du groupe » si ses signataires réunissent au moins
90 % des membres du groupe RN à la date du dépôt, sinon c'est un « texte d'élus du groupe ».
Date : 2026-10-27.
Données : bloc « présentée par » des PDF archivés dans `02-partis/rn/corpus/` (pdftotext) ;
jeu open data AMO30 (17e législature) : mandats « GP » de l'organe PO845401 (groupe RN),
champs dateDebut et dateFin ; deux effectifs sont donnés : membres seuls (codeQualite
« Membre », « Président », etc., hors apparentés) et membres plus apparentés. Le verdict
se fonde sur l'effectif le plus large (membres plus apparentés), le plus exigeant pour
atteindre 90 %.
Usage : python3 -I _scripts/calculs/rn_textes_du_groupe.py [chemin du dossier json AMO30]
Calcul par nos soins.
"""
import glob, json, re, subprocess, sys, unicodedata

AMO = sys.argv[1] if len(sys.argv) > 1 else (
    "/private/tmp/claude-501/-Users-dilhan-Documents-Politique-elections-france-2027/"
    "bd3ce823-20df-45ea-b09c-ea2fe350a07c/scratchpad/amo30/json")
CORPUS = "02-partis/rn/corpus/"
ORGANE_RN = "PO845401"

# (identifiant, PPL, motif de nom de fichier, date de dépôt lue sur le PDF)
TEXTES = [
    ("C-RN-36", "PPL 344", "C-RN-36", "2024-10-15"),
    ("C-RN-37", "PPL 364", "C-RN-37", "2024-10-15"),
    ("C-RN-38", "PPL 748", "C-RN-38", "2024-12-19"),
    ("C-RN-43", "PPL 2826", "C-RN-43", "2026-05-26"),
    ("C-RN-44", "PPL 1626", "C-RN-44", "2025-06-24"),
    ("C-RN-45", "PPL 425", "C-RN-45", "2024-10-15"),
    ("C-RN-49", "PPL 3109", "C-RN-49", "2026-08-25"),
]


def signataires(pdf):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True,
                         text=True, check=True).stdout
    debut = txt.index("présentée par") + len("présentée par")
    fin = re.search(r"députés? et députées|députés?\s*\.", txt[debut:]).start() + debut
    bloc = re.sub(r"\s*\u2013\d+\u2013\s*", " ", txt[debut:fin])
    bloc = re.sub(r"\s+", " ", bloc)
    return [s.strip(" ,") for s in re.split(r"(?=\b(?:M\.|Mme) )", bloc) if s.strip(" ,")]


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]+", " ", t).strip()


def effectifs(date):
    """Renvoie (membres, apparentés, noms normalisés des membres et apparentés à la date)."""
    membres = apparentes = 0
    noms = set()
    for f in glob.glob(AMO + "/acteur/*.json"):
        a = json.load(open(f))["acteur"]
        mandats = a["mandats"]["mandat"]
        mandats = mandats if isinstance(mandats, list) else [mandats]
        for m in mandats:
            if m["typeOrgane"] != "GP" or m["organes"]["organeRef"] != ORGANE_RN:
                continue
            if m["dateDebut"] <= date and (not m.get("dateFin") or date <= m["dateFin"]):
                ident = a["etatCivil"]["ident"]
                noms.add(norm(ident["prenom"] + " " + ident["nom"]))
                if "pparent" in m["infosQualite"]["codeQualite"]:
                    apparentes += 1
                else:
                    membres += 1
    return membres, apparentes, noms


for ident, ppl, motif, date in TEXTES:
    pdf = glob.glob(CORPUS + motif + "-*.pdf")[0]
    sig = signataires(pdf)
    n = len(sig)
    membres, app, noms = effectifs(date)
    def dans(x):
        k = norm(re.sub(r"^(M\.|Mme) ", "", x))
        return any(k == m or k.startswith(m + " ") or m.startswith(k + " ") for m in noms)
    hors = [x for x in sig if not dans(x)]
    total = membres + app
    part = 100 * (n - len(hors)) / total  # seuls les signataires du groupe comptent (les autres sont des députés d'un autre groupe)
    verdict = "groupe" if part >= 90 else "élus du groupe"
    print(f"{ident} {ppl} (dépôt {date}) : {n} signataires dont {n-len(hors)} du groupe ; groupe RN {membres} membres + "
          f"{app} apparentés = {total} ; part {part:.1f} % ; verdict : {verdict}"
          f" ; signataires non retrouvés dans le groupe à la date : {len(hors)} {hors}")
