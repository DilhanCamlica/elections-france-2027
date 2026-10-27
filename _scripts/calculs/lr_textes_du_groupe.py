#!/usr/bin/env python3
"""Contrôle de l'auteur des textes du corpus LR à liste nominative de signataires.

Objet : appliquer la règle de `01-socle/01-criteres.md` §6 (précision du 2026-10-27) :
un texte à liste nominative est « du groupe » si ses signataires réunissent au moins
90 % des membres du groupe Droite Républicaine (DR) à la date du dépôt, sinon c'est un
« texte d'élus du groupe », sauf s'il est porté autrement par le groupe (niche, dépôt
« et les membres du groupe », texte du président défendu en séance) : ce second critère
n'est pas calculé ici, il est écrit dans `02-partis/lr/01-corpus.md`.
Date : 2026-10-27.
Données : bloc « présentée par » (PPL, PPLC, PPR) ou « présenté par » (amendements) des
PDF archivés dans `02-partis/lr/corpus/` (pdftotext) ; jeu open data AMO30 (17e
législature) : mandats « GP » de l'organe PO845425 (groupe DR, libellé lu dans AMO10),
champs dateDebut et dateFin. Effectif retenu : membres (dont le président) plus
apparentés, le plus exigeant pour atteindre 90 %. Seuls les signataires membres ou
apparentés du groupe à la date comptent ; les autres sont listés à part.
La formule « les membres du groupe Droite Républicaine » dans le bloc des auteurs est
signalée (critère de dépôt par le groupe, sans calcul).
Limite constatée : le PDF diffusé en données ouvertes est régénéré et peut porter des
cosignatures postérieures au dépôt (PPL 1550 : une députée entrée à l'Assemblée et au
groupe en avril 2026 figure en fin de liste d'un texte déposé le 10 juin 2025). Le script
écarte les signataires qui n'étaient pas dans le groupe à la date du dépôt, mais ne peut
pas écarter un membre du groupe à cette date qui aurait cosigné plus tard ; les dates de
cosignature du jeu « Dossiers législatifs » ne permettent pas de trancher (dates de saisie
groupées, par exemple 2025-02-17 pour la plupart des cosignataires des PPL 378, 689, 693).
Le pourcentage est donc un plafond.
Usage : python3 -I _scripts/calculs/lr_textes_du_groupe.py [chemin du dossier json AMO30]
Calcul par nos soins.
"""
import glob, json, re, subprocess, sys, unicodedata

AMO = sys.argv[1] if len(sys.argv) > 1 else (
    "/private/tmp/claude-501/-Users-dilhan-Documents-Politique-elections-france-2027/"
    "b76c134b-7c20-477c-8622-eb16157ecf7e/scratchpad/amo/amo30/json")
CORPUS = "02-partis/lr/corpus/"
ORGANE_DR = "PO845425"

# (identifiant, texte, motif de nom de fichier, date de dépôt lue sur le PDF ou la page)
TEXTES = [
    ("C-LR-34", "amendement I-618 (PLF 2026)", "C-LR-34-", "2025-10-20"),
    ("C-LR-35", "amendement I-269 (PLF 2026)", "C-LR-35-", "2025-10-20"),
    ("C-LR-38", "PPLC 2352", "C-LR-38-", "2026-01-19"),
    ("C-LR-39", "PPL 765", "C-LR-39-", "2024-12-19"),
    ("C-LR-40", "PPL 2227", "C-LR-40-", "2025-12-09"),
    ("C-LR-41", "PPL 378", "C-LR-41-", "2024-10-15"),
    ("C-LR-42", "PPL 693", "C-LR-42-", "2024-12-03"),
    ("C-LR-43", "PPL 689", "C-LR-43-", "2024-12-03"),
    ("C-LR-44", "PPL 2229", "C-LR-44-", "2025-12-09"),
    ("C-LR-45", "PPL 238", "C-LR-45-", "2024-09-17"),
    ("C-LR-46", "PPL 753", "C-LR-46-", "2024-12-19"),
    ("C-LR-47", "PPL 3230", "C-LR-47-", "2026-10-06"),
    ("C-LR-48", "PPL 691", "C-LR-48-", "2024-12-03"),
    ("C-LR-49", "PPL 1550", "C-LR-49-", "2025-06-10"),
    ("C-LR-50", "PPL 3335", "C-LR-50-", "2026-10-13"),
    ("C-LR-51", "PPL 2167", "C-LR-51-", "2025-12-02"),
    ("C-LR-52", "PPLC 1477", "C-LR-52-", "2025-05-28"),
    ("C-LR-53", "PPR 1455", "C-LR-53-", "2025-05-23"),
]


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z]+", " ", t).strip()


def bloc_auteurs(pdf):
    txt = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True,
                         text=True, check=True).stdout
    m = re.search(r"présentée? par", txt)
    debut = m.end()
    fin = re.search(r"députés? et députées|députées? et députés|députée?s?\s*[,.]|\n\s*-{5,}", txt[debut:]).start() + debut
    bloc = re.sub(r"\s*[\u2013-]\d+[\u2013-]\s*", " ", txt[debut:fin])
    return re.sub(r"\s+", " ", bloc)


def signataires(bloc):
    bloc = re.sub(r"les membres du groupe [^,(]+(\(\d+\))?,?", " ", bloc)
    bloc = re.sub(r"\bet (?=(M\.|Mme) )", ", ", bloc)
    return [s.strip(" ,") for s in re.split(r"(?=\b(?:M\.|Mme) )", bloc) if s.strip(" ,")]


def membres_du_groupe(date):
    """Renvoie (membres, apparentés, liste des (prénom normalisé, nom normalisé))."""
    membres = apparentes = 0
    gens = []
    for f in glob.glob(AMO + "/acteur/*.json"):
        a = json.load(open(f))["acteur"]
        mandats = a["mandats"]["mandat"]
        mandats = mandats if isinstance(mandats, list) else [mandats]
        for m in mandats:
            if m["typeOrgane"] != "GP" or m["organes"]["organeRef"] != ORGANE_DR:
                continue
            if m["dateDebut"] <= date and (not m.get("dateFin") or date <= m["dateFin"]):
                ident = a["etatCivil"]["ident"]
                gens.append((norm(ident["prenom"]), norm(ident["nom"])))
                if "pparent" in m["infosQualite"]["codeQualite"]:
                    apparentes += 1
                else:
                    membres += 1
                break
    return membres, apparentes, gens


def dans_le_groupe(sig, gens):
    k = norm(re.sub(r"^(M\.|Mme) ", "", sig))
    for prenom, nom in gens:
        complet = prenom + " " + nom
        if k == complet or k == nom or k.startswith(complet + " ") or complet.startswith(k + " "):
            return True
        # amendements : « M. Jean-Pierre Vigier » ou « Mme Alexandra Martin »
        if k.endswith(" " + nom) and k.startswith(prenom):
            return True
        # nom d'usage plus long que le nom de l'état civil (« Vermorel-Marques » pour « Vermorel »)
        if k.startswith(nom + " ") or k.startswith(complet + " "):
            return True
    return False


for ident, texte, motif, date in TEXTES:
    pdf = sorted(glob.glob(CORPUS + motif + "*.pdf"))[0]
    bloc = bloc_auteurs(pdf)
    formule = "les membres du groupe" in bloc
    sig = signataires(bloc)
    membres, app, gens = membres_du_groupe(date)
    hors = [s for s in sig if not dans_le_groupe(s, gens)]
    du_groupe = len(sig) - len(hors)
    total = membres + app
    part = 100 * du_groupe / total
    if formule:
        verdict = "groupe (formule « les membres du groupe » au dépôt)"
    else:
        verdict = "groupe (90 % atteints)" if part >= 90 else "élus du groupe, sauf portage établi ailleurs"
    print(f"{ident} {texte} (dépôt {date}) : {len(sig)} signataires nommés dont {du_groupe} du groupe ; "
          f"groupe DR {membres} membres (dont le président) + {app} apparentés = {total} ; "
          f"part {part:.1f} % ; verdict : {verdict} ; signataires hors du groupe à la date : {len(hors)} {hors}")
