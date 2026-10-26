#!/usr/bin/env python3
"""Décompte de l'écoute (Q5) pour LFI : les 47 demandes de l'inventaire gelé,
avec le statut lu dans les six fiches `02-partis/lfi/axes/*.md` (tableaux Q5).

Statuts :
  T   traitée
  TP  traitée en partie
  NT  non traitée (silence)
  TC  traitée, mais le programme va contre sur un volet et l'assume
  TPC traitée en partie, et le programme va contre sur un volet et l'assume
  C   contredite en l'assumant
  P   demande à deux branches opposées (paire incompatible) ; la branche servie est notée

Usage : python3 -I lfi_ecoute_decompte.py
"""

DEMANDES = [
    # axe, demande, statut
    (1, "Réduire le déficit surtout par la baisse des dépenses", "C"),
    (1, "Réduire le train de vie de l'État", "TP"),
    (1, "Faire contribuer en priorité les grandes entreprises et les plus aisés", "T"),
    (1, "Traiter la dette comme une urgence et inscrire une règle d'or", "TPC"),
    (1, "Maintenir les prestations et les services publics, refuser les gels", "T"),
    (1, "Réduire le nombre de fonctionnaires", "C"),
    (1, "Garder dans le public ou renationaliser les services essentiels", "T"),
    (2, "Ne pas reculer l'âge de départ", "T"),
    (2, "Garder des retraites et une assurance maladie publiques", "T"),
    (2, "Maintenir l'indexation des pensions", "T"),
    (2, "Renforcer la lutte contre la fraude sociale, revoir les conditions", "TPC"),
    (2, "Lutter contre le non-recours", "T"),
    (2, "Durcir l'indemnisation du chômage et les arrêts de travail", "C"),
    (2, "Augmenter les aides à la dépendance et au handicap", "T"),
    (2, "Revaloriser le RSA et les minima sociaux", "T"),
    (2, "Ne pas augmenter le reste à charge en santé", "T"),
    (2, "Aménager la fin de carrière, tenir compte de la pénibilité", "T"),
    (3, "Réduire le niveau de l'immigration", "C"),
    (3, "Accueillir les demandeurs d'asile persécutés", "T"),
    (3, "Régulariser les travailleurs sans papiers des métiers en tension", "T"),
    (3, "Restreindre l'accès des étrangers aux prestations (ou égalité)", "P:égalité"),
    (3, "Recourir moins à l'immigration de travail", "NT"),
    (3, "Conditionner l'intégration à l'apprentissage du français", "NT"),
    (4, "Augmenter le Smic et les salaires", "T"),
    (4, "Baisser les impôts des ménages, surtout des classes moyennes", "TPC"),
    (4, "Taxer davantage les très hauts patrimoines et les hauts revenus", "T"),
    (4, "Baisser la TVA sur les produits de première nécessité", "TC"),
    (4, "Indexer salaires, pensions et allocations sur l'inflation", "T"),
    (4, "Baisser le prix des carburants et de l'énergie", "T"),
    (4, "Bloquer ou encadrer les prix", "T"),
    (4, "Encadrer les loyers, construire des logements abordables", "T"),
    (4, "Réduire les écarts de revenus (ou mieux rémunérer le travail)", "P:redistribution"),
    (4, "Revaloriser les bourses et les aides aux étudiants", "TP"),
    (5, "Plus de fermeté dans le maintien de l'ordre (ou encadrer la force)", "P:encadrement"),
    (5, "Donner plus de moyens à la police, à la gendarmerie et à la justice", "TP"),
    (5, "Rétablir la peine de mort", "NT"),
    (5, "Encadrer l'usage de la force", "T"),
    (5, "Garantir le droit de manifester", "T"),
    (5, "Sanctionner les violences et les contrôles abusifs", "T"),
    (6, "Recourir plus souvent au référendum, y compris d'initiative citoyenne", "T"),
    (6, "Réduire le nombre et les avantages des élus", "TP"),
    (6, "Prendre en compte le vote blanc", "T"),
    (6, "Changer de Constitution", "T"),
    (6, "Démission ou destitution du président", "T"),
    (6, "Gouverner avec une majorité nette (ou par compromis)", "P:aucune"),
    (6, "Plus de pouvoir au niveau national qu'à l'UE", "T"),
    (6, "Démarches accessibles et services publics de proximité", "T"),
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
