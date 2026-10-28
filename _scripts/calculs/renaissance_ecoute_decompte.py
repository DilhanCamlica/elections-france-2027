#!/usr/bin/env python3
"""Décompte de l'écoute (Q5) pour Renaissance : les 47 demandes de l'inventaire gelé,
avec le statut lu dans les six fiches `02-partis/renaissance/axes/*.md` (tableaux Q5),
mêmes codes que `ps_ecoute_decompte.py`.

Statuts :
  T   traitée
  TP  traitée en partie
  NT  non traitée (silence)
  TC  traitée, mais le programme va contre sur un volet et l'assume
  TPC traitée en partie, et le programme va contre sur un volet et l'assume
  C   contredite en l'assumant (en tout ou en partie)
  P   demande à deux branches opposées (paire incompatible) ; la branche servie est notée

Traductions (les fiches Renaissance n'emploient pas les codes ; statut de la fiche, puis code) :
  "Oui" = T ; "En partie" = TP ; "Non" sans contre-pied = NT.
  "En partie" + "va contre et l'assume" = TPC (axe 1 hauts revenus, axe 4 Smic, axe 6 RIC).
  "Non" + contre-pied assume = C (axe 1 prestations, axe 2 pensions, RSA et dependance, axe 3 immigration de travail,
  axe 4 hauts patrimoines et indexation, axe 6 pouvoir national face a l'UE).
  "Non" + demande opposee servie "non comptee comme contredite" = NT (axe 3 regularisation, axe 5 usage de la force).
  Deux branches opposees = P (axe 4 ecarts de revenus, axe 6 majorite nette ou compromis).
Cas ambigus : axe 2 age de depart (NT : le groupe va contre, pas le candidat) ; axe 2 dependance (C : gel
  des prestations assume en termes generaux) ; axe 3 prestations aux etrangers (TP, alors que les deux
  formulations sont servies en partie) ; axe 5 droit de manifester (NT : verdict de la fiche, aucun contre-pied
  retenu) ; axe 6 vote blanc (NT).

Usage : python3 -I renaissance_ecoute_decompte.py

Normalisation du 2026-10-28 (synthèse) : les quatre demandes de l'inventaire à deux branches opposées
(prestations des étrangers, écarts de revenus, fermeté ou encadrement, majorité nette ou compromis)
sont codées P:<branche servie> pour les cinq forces, comme dans les scripts PS, LFI et LR ; le statut
lu dans la fiche est rappelé en commentaire sur la ligne.
"""

DEMANDES = [
    # axe, demande, statut
    (1, "Réduire le déficit surtout par la baisse des dépenses", "T"),
    (1, "Réduire le train de vie de l'État", "T"),
    (1, "Faire contribuer en priorité les grandes entreprises et les plus aisés", "TPC"),
    (1, "Traiter la dette comme une urgence et inscrire une règle d'or", "T"),
    (1, "Maintenir les prestations et les services publics, refuser les gels", "C"),
    (1, "Réduire le nombre de fonctionnaires", "T"),
    (1, "Garder dans le public ou renationaliser les services essentiels", "NT"),
    (2, "Ne pas reculer l'âge de départ", "NT"),
    (2, "Garder des retraites et une assurance maladie publiques", "T"),
    (2, "Maintenir l'indexation des pensions", "T"),
    (2, "Renforcer la lutte contre la fraude sociale, revoir les conditions", "T"),
    (2, "Lutter contre le non-recours", "C"),
    (2, "Durcir l'indemnisation du chômage et les arrêts de travail", "TP"),
    (2, "Augmenter les aides à la dépendance et au handicap", "C"),
    (2, "Revaloriser le RSA et les minima sociaux", "T"),
    (2, "Ne pas augmenter le reste à charge en santé", "C"),
    (2, "Aménager la fin de carrière, tenir compte de la pénibilité", "T"),
    (3, "Réduire le niveau de l'immigration", "T"),
    (3, "Accueillir les demandeurs d'asile persécutés", "TP"),
    (3, "Recourir moins à l'immigration de travail", "C"),
    (3, "Régulariser les travailleurs sans papiers des métiers en tension", "NT"),
    (3, "Restreindre l'accès des étrangers aux prestations (ou égalité)", "P:restriction en partie"),  # fiche : « En partie, de façon limitée »,
    (3, "Conditionner l'intégration à l'apprentissage du français", "T"),
    (4, "Augmenter le Smic et les salaires", "TPC"),
    (4, "Baisser les impôts des ménages, surtout des classes moyennes", "T"),
    (4, "Taxer davantage les très hauts patrimoines et les hauts revenus", "C"),
    (4, "Baisser la TVA sur les produits de première nécessité", "TP"),
    (4, "Indexer salaires, pensions et allocations sur l'inflation", "C"),
    (4, "Baisser le prix des carburants et de l'énergie", "T"),
    (4, "Bloquer ou encadrer les prix", "NT"),
    (4, "Encadrer les loyers, construire des logements abordables", "NT"),
    (4, "Réduire les écarts de revenus (ou mieux rémunérer le travail)", "P:travail"),
    (4, "Revaloriser les bourses et les aides aux étudiants", "TP"),
    (5, "Plus de fermeté dans le maintien de l'ordre (ou encadrer la force)", "P:fermeté"),  # fiche : « Oui » (fermeté servie),
    (5, "Donner plus de moyens à la police, à la gendarmerie et à la justice", "TP"),
    (5, "Rétablir la peine de mort", "NT"),
    (5, "Encadrer l'usage de la force", "NT"),
    (5, "Garantir le droit de manifester", "NT"),
    (5, "Sanctionner les violences et les contrôles abusifs", "NT"),
    (6, "Recourir plus souvent au référendum, y compris d'initiative citoyenne", "TPC"),
    (6, "Réduire le nombre et les avantages des élus", "TP"),
    (6, "Prendre en compte le vote blanc", "NT"),
    (6, "Changer de Constitution", "TP"),
    (6, "Démission ou destitution du président", "NT"),
    (6, "Gouverner avec une majorité nette (ou par compromis)", "P:compromis"),
    (6, "Plus de pouvoir au niveau national qu'à l'UE", "C"),
    (6, "Démarches accessibles et services publics de proximité", "TP"),
]



def main() -> None:
    assert len(DEMANDES) == 47, len(DEMANDES)
    codes = [s.split(":")[0] for _, _, s in DEMANDES]
    t = codes.count("T") + codes.count("TC")
    tp = codes.count("TP") + codes.count("TPC")
    nt = codes.count("NT")
    contre = codes.count("C") + codes.count("TC") + codes.count("TPC")
    contre_par_ailleurs = codes.count("TC") + codes.count("TPC")
    paires = codes.count("P")
    print(f"Demandes : {len(DEMANDES)}")
    print(f"Traitées : {t} (dont {codes.count('TC')} avec un contre-pied partiel assumé)")
    print(f"Traitées en partie : {tp} (dont {codes.count('TPC')} avec un contre-pied partiel assumé)")
    print(f"Non traitées (silence) : {nt}")
    print(f"Contredites en l'assumant : {contre} (dont {contre_par_ailleurs} traitées ou traitées en partie par ailleurs)")
    print(f"Paires à deux branches opposées : {paires}")
    distinct = t + tp + nt + codes.count("C") + paires
    assert distinct == 47, distinct
    for axe in range(1, 7):
        sub = [s.split(":")[0] for a, _, s in DEMANDES if a == axe]
        print(f"  axe {axe} : {len(sub)} demandes, statuts {sub}")


if __name__ == "__main__":
    main()
