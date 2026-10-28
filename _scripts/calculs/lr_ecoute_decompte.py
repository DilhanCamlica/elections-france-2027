#!/usr/bin/env python3
"""Décompte de l'écoute (Q5) pour LR : les 47 demandes de l'inventaire gelé,
avec le statut lu dans les six fiches `02-partis/lr/axes/*.md` (tableaux Q5),
mêmes codes que `ps_ecoute_decompte.py`.

Statuts :
  T   traitée
  TP  traitée en partie
  NT  non traitée (silence)
  TC  traitée, mais le programme va contre sur un volet et l'assume
  TPC traitée en partie, et le programme va contre sur un volet et l'assume
  C   contredite en l'assumant (en tout ou en partie)
  P   demande à deux branches opposées (paire incompatible) ; la branche servie est notée

Usage : python3 -I lr_ecoute_decompte.py
"""

DEMANDES = [
    # axe, demande, statut
    (1, "Réduire le déficit surtout par la baisse des dépenses", "T"),
    (1, "Réduire le train de vie de l'État", "T"),
    (1, "Faire contribuer en priorité les grandes entreprises et les plus aisés", "TPC"),
    (1, "Traiter la dette comme une urgence et inscrire une règle d'or", "T"),
    (1, "Maintenir les prestations et les services publics, refuser les gels", "C"),
    (1, "Réduire le nombre de fonctionnaires", "T"),
    (1, "Garder dans le public ou renationaliser les services essentiels", "C"),
    (2, "Ne pas reculer l'âge de départ", "C"),
    (2, "Garder des retraites et une assurance maladie publiques", "T"),
    (2, "Maintenir l'indexation des pensions", "T"),
    (2, "Renforcer la lutte contre la fraude sociale, revoir les conditions", "T"),
    (2, "Lutter contre le non-recours", "TP"),
    (2, "Durcir l'indemnisation du chômage et les arrêts de travail", "T"),
    (2, "Augmenter les aides à la dépendance et au handicap", "NT"),
    (2, "Revaloriser le RSA et les minima sociaux", "C"),
    (2, "Ne pas augmenter le reste à charge en santé", "C"),
    (2, "Aménager la fin de carrière, tenir compte de la pénibilité", "T"),
    (3, "Réduire le niveau de l'immigration", "T"),
    (3, "Accueillir les demandeurs d'asile persécutés", "C"),
    (3, "Recourir moins à l'immigration de travail", "T"),
    (3, "Régulariser les travailleurs sans papiers des métiers en tension", "C"),
    (3, "Restreindre l'accès des étrangers aux prestations (ou égalité)", "P:restriction"),
    (3, "Conditionner l'intégration à l'apprentissage du français", "T"),
    (4, "Augmenter le Smic et les salaires", "TP"),
    (4, "Baisser les impôts des ménages, surtout des classes moyennes", "T"),
    (4, "Taxer davantage les très hauts patrimoines et les hauts revenus", "C"),
    (4, "Baisser la TVA sur les produits de première nécessité", "TP"),
    (4, "Indexer salaires, pensions et allocations sur l'inflation", "TP"),
    (4, "Baisser le prix des carburants et de l'énergie", "T"),
    (4, "Bloquer ou encadrer les prix", "TP"),
    (4, "Encadrer les loyers, construire des logements abordables", "C"),
    (4, "Réduire les écarts de revenus (ou mieux rémunérer le travail)", "P:travail"),
    (4, "Revaloriser les bourses et les aides aux étudiants", "NT"),
    (5, "Plus de fermeté dans le maintien de l'ordre (ou encadrer la force)", "P:fermeté"),
    (5, "Donner plus de moyens à la police, à la gendarmerie et à la justice", "TP"),
    (5, "Rétablir la peine de mort", "NT"),
    (5, "Encadrer l'usage de la force", "C"),
    (5, "Garantir le droit de manifester", "NT"),
    (5, "Sanctionner les violences et les contrôles abusifs", "NT"),
    (6, "Recourir plus souvent au référendum, y compris d'initiative citoyenne", "TP"),
    (6, "Réduire le nombre et les avantages des élus", "NT"),
    (6, "Prendre en compte le vote blanc", "NT"),
    (6, "Changer de Constitution", "TP"),
    (6, "Démission ou destitution du président", "NT"),
    (6, "Gouverner avec une majorité nette (ou par compromis)", "P:majorité nette"),
    (6, "Plus de pouvoir au niveau national qu'à l'UE", "T"),
    (6, "Démarches accessibles et services publics de proximité", "TP"),
]


def main() -> None:
    assert len(DEMANDES) == 47, len(DEMANDES)
    codes = [s.split(":")[0] for _, _, s in DEMANDES]
    t = codes.count("T") + codes.count("TC")
    tp = codes.count("TP") + codes.count("TPC")
    nt = codes.count("NT")
    contre = codes.count("C") + codes.count("TC") + codes.count("TPC")
    paires = codes.count("P")
    print(f"Demandes : {len(DEMANDES)}")
    print(f"Traitées : {t} (dont {codes.count('TC')} avec un contre-pied partiel assumé)")
    print(f"Traitées en partie : {tp} (dont {codes.count('TPC')} avec un contre-pied partiel assumé)")
    print(f"Non traitées : {nt}")
    print(f"Contredites en l'assumant : {contre} (dont {codes.count('TC') + codes.count('TPC')} traitées par ailleurs)")
    print(f"Paires incompatibles : {paires} ; branche servie : "
          + ", ".join(s.split(":")[1] for _, _, s in DEMANDES if s.startswith("P:")))
    assert t + tp + nt + codes.count("C") + paires == 47


if __name__ == "__main__":
    main()
