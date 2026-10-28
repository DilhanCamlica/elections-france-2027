"""Matrice tendances x forces, comptes par force, comparaison avec le tableau de bord.

Lecture seule. Usage : python3 -I _scripts/calculs/synthese_tendances.py
"""
import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
FORCES = [("Renaissance", "renaissance"), ("RN", "rn"), ("LFI", "lfi"), ("PS", "ps"), ("LR", "lr")]
CODES = ["T", "TP", "N", "A"]
anomalies = []


def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[*_`]", "", s).lower()
    return re.sub(r"\s+", " ", s).strip(" .")


def code_statut(brut):
    n = norm(brut)
    if n in ("traitee", "traite"):
        return "T"
    if re.fullmatch(r"traitee? en partie|partiellement traitee?", n):
        return "TP"
    if re.fullmatch(r"nommee? sans mesure", n):
        return "N"
    if n in ("absente", "absent"):
        return "A"
    return None


def cellules(ligne):
    return [c.strip() for c in ligne.strip().strip("|").split("|")]


def liste_gelee():
    out = {}
    for l in (RACINE / "03-sources/tendances-lourdes.md").read_text(encoding="utf-8").splitlines():
        if l.startswith("|"):
            c = cellules(l)
            if c[0].isdigit() and len(c) >= 2:
                out[int(c[0])] = c[1]
    return out


def carte(slug, attendues):
    chemin = RACINE / f"02-partis/{slug}/tendances.md"
    res = {}
    entete = False
    for l in chemin.read_text(encoding="utf-8").splitlines():
        if not l.startswith("|"):
            continue
        c = cellules(l)
        if len(c) >= 3 and norm(c[0]) in ("n°", "no", "n") and "statut" in norm(c[2]):
            entete = True
            continue
        if entete and c[0].isdigit():
            n = int(c[0])
            if n not in attendues:
                anomalies.append(f"{slug}: numero {n} hors liste gelee")
                continue
            code = code_statut(c[2])
            if code is None:
                anomalies.append(f"{slug}: tendance {n} statut inconnu {c[2]!r}")
            elif n in res:
                anomalies.append(f"{slug}: tendance {n} en double")
            else:
                res[n] = code
    if not entete:
        anomalies.append(f"{slug}: tableau a en-tete 'N° | Tendance | Statut' introuvable")
    for n in attendues:
        if n not in res:
            anomalies.append(f"{slug}: tendance {n} manquante ou illisible")
    return res


def annoncees():
    """Carte 'x / y / z / w' par force, depuis le tableau de bord."""
    out = {}
    for l in (RACINE / "02-partis/README.md").read_text(encoding="utf-8").splitlines():
        if not l.startswith("|"):
            continue
        c = cellules(l)
        for nom, _ in FORCES:
            if len(c) > 3 and c[1] == nom:
                m = re.findall(r"carte\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)", l)
                if len(m) == 1:
                    out[nom] = tuple(int(x) for x in m[0])
                elif len(m) > 1:
                    anomalies.append(f"README: {nom} plusieurs motifs carte {m}")
    return out


def main():
    tend = liste_gelee()
    if len(tend) != 14:
        anomalies.append(f"liste gelee: {len(tend)} tendances au lieu de 14")
    mat = {nom: carte(slug, tend) for nom, slug in FORCES}

    print("## Matrice (T traitee, TP en partie, N nommee sans mesure, A absente)\n")
    print("| N° | Tendance | " + " | ".join(n for n, _ in FORCES) + " | Nb T |")
    print("|---|---|" + "---|" * (len(FORCES) + 1))
    nbT = {}
    for n in sorted(tend):
        titre = tend[n] if len(tend[n]) <= 60 else tend[n][:57] + "..."
        codes = [mat[f].get(n, "?") for f, _ in FORCES]
        nbT[n] = codes.count("T")
        print(f"| {n} | {titre} | " + " | ".join(codes) + f" | {nbT[n]} |")

    print("\n## Comptes par force (T / TP / N / A)\n")
    ann = annoncees()
    for nom, _ in FORCES:
        v = [list(mat[nom].values()).count(c) for c in CODES]
        ligne = f"{nom}: {' / '.join(map(str, v))}"
        if nom not in ann:
            ligne += "  | README: aucune carte annoncee (motif absent)"
        elif tuple(v) == ann[nom]:
            ligne += "  | README identique"
        else:
            ligne += f"  | ECART: README annonce {' / '.join(map(str, ann[nom]))}"
        print(ligne)

    print("\n## Classement des tendances\n")
    aucun = [n for n in sorted(tend) if all(mat[f].get(n) != "T" for f, _ in FORCES)
             and all(mat[f].get(n) != "TP" for f, _ in FORCES)]
    partie = [n for n in sorted(tend) if nbT[n] == 0 and n not in aucun]
    cinq = [n for n in sorted(tend) if nbT[n] == 5]
    print(f"Traitee par personne (aucun T ni TP): {aucun or 'aucune'}")
    print(f"Traitees en partie au mieux (aucun T, au moins un TP): {partie or 'aucune'}")
    print(f"Traitees par les cinq (5 T): {cinq or 'aucune'}")
    print("\nNombre de forces en T par tendance: " + ", ".join(f"{n}={nbT[n]}" for n in sorted(tend)))

    if anomalies:
        print("\n## Anomalies de format")
        for a in anomalies:
            print("- " + a)
        sys.exit(1)


main()
