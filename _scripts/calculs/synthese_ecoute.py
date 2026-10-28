#!/usr/bin/env python3
"""Synthèse de l'écoute (Q5) : matrice des 47 demandes gelées × cinq forces, à partir des
cinq scripts *_ecoute_decompte.py (statuts lus dans les fiches), et listes :
demandes que personne ne traite, demandes traitées par les cinq, demandes contredites par
trois forces ou plus. Aucun total par force au-delà des comptes déjà publiés.

Usage : python3 -I synthese_ecoute.py
"""
import importlib.util, pathlib

ICI = pathlib.Path(__file__).resolve().parent
FORCES = [("renaissance", "Renaissance"), ("rn", "RN"), ("lfi", "LFI"), ("ps", "PS"), ("lr", "LR")]
AXES = {1: "Finances publiques", 2: "Travail et protection sociale", 3: "Immigration",
        4: "Pouvoir d'achat et fiscalité", 5: "Sécurité et libertés", 6: "Institutions et Europe"}


def charger(slug):
    spec = importlib.util.spec_from_file_location(slug, ICI / f"{slug}_ecoute_decompte.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    assert len(mod.DEMANDES) == 47, slug
    return mod.DEMANDES


def code(statut):
    return statut.split(":")[0]


def main():
    brut = {slug: charger(slug) for slug, _ in FORCES}
    ref = [(a, t) for a, t, _ in brut["lr"]]
    # alignement par (axe, libellé) : le script LFI range trois demandes de l'axe 3 dans un autre ordre
    d = {}
    for slug, _ in FORCES:
        par_cle = {(a, t): (a, t, s) for a, t, s in brut[slug]}
        assert set(par_cle) == set(ref), f"{slug} : liste des demandes différente"
        d[slug] = [par_cle[k] for k in ref]
    noms = [n for _, n in FORCES]
    print("| Axe | Demande | " + " | ".join(noms) + " |")
    print("|---|---|" + "---|" * 5)
    personne, cinq, contre3, silence3 = [], [], [], []
    for i, (a, t) in enumerate(ref):
        st = [d[slug][i][2] for slug, _ in FORCES]
        print(f"| {a} | {t} | " + " | ".join(st) + " |")
        c = [code(s) for s in st]
        traite = [x in ("T", "TP", "TC", "TPC") for x in c]
        if not any(traite) and not any(x == "P" for x in c):
            personne.append((a, t, st))
        if all(x in ("T", "TC") for x in c):
            cinq.append((a, t))
        if sum(x in ("C", "TC", "TPC") for x in c) >= 3:
            contre3.append((a, t, st))
        if sum(x == "NT" for x in c) >= 3:
            silence3.append((a, t, st))
    print()
    print("Demandes qu'aucune force ne traite, même en partie (hors paires) :", len(personne))
    for a, t, st in personne: print(f"  axe {a} : {t} : {st}")
    print("Demandes traitées par les cinq :", len(cinq))
    for a, t in cinq: print(f"  axe {a} : {t}")
    print("Demandes contredites en l'assumant par trois forces ou plus :", len(contre3))
    for a, t, st in contre3: print(f"  axe {a} : {t} : {st}")
    print("Demandes passées sous silence par trois forces ou plus :", len(silence3))
    for a, t, st in silence3: print(f"  axe {a} : {t} : {st}")
    print()
    print("Comptes par force (T / TP / NT / C / P), T et TP incluant les contre-pieds partiels :")
    for slug, nom in FORCES:
        c = [code(s) for _, _, s in d[slug]]
        print(f"  {nom} : {c.count('T') + c.count('TC')} / {c.count('TP') + c.count('TPC')} / {c.count('NT')} / "
              f"{c.count('C')} (+{c.count('TC') + c.count('TPC')} partiels) / {c.count('P')}")


if __name__ == "__main__":
    main()
