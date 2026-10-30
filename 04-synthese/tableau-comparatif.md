# Cinq programmes côte à côte : tableau comparatif

- Date de rédaction : 2026-10-28
- Date d'arrêt des données : 2026-10-28 (dates d'arrêt des cinq corpus réalignées, voir `note-de-methode.md`)
- Auteur : agent principal, à partir des cinq verticales (`02-partis/`) et des scripts de `_scripts/calculs/` (`synthese_grilles.py`, `synthese_tendances.py`, `synthese_ecoute.py`)
- Statut : revu (option B sur les revirements, 2026-10-28 ; compléments 9123 et 9140 à 9142, 2026-10-30)
- Socle : v2.3 (précisions du 2026-10-28)

Ce tableau met côte à côte les verdicts des cinq verticales, sans en ajouter aucun. Chaque case renvoie à la fiche qui la justifie (`02-partis/<force>/axes/<n>-*.md`) et au chapitre de la page publiée. Aucun classement, aucune note globale, aucune moyenne : le socle l'interdit (`01-socle/01-criteres.md`, §4 ; `04-format-artifacts.md`, §3).

Sigles : LFI (La France insoumise), PS (Parti socialiste), LR (Les Républicains), RN (Rassemblement national) ; D, F, C, E : les quatre questions par axe (diagnostic, faisabilité, cohérence, écoute) ; M : la question Méthode ; EPR, SOC, DR : groupes Ensemble pour la République, Socialistes et apparentés, Droite républicaine à l'Assemblée nationale.

## 1. La matrice des verdicts (six axes × cinq forces)

Lecture d'une case : D (le problème est-il réel ?), F (est-ce faisable ?), C (votent-ils ce qu'ils disent ?), E (répondent-ils aux demandes ?). Échelle de 1 (rouge) à 5 (vert foncé), définitions dans `01-socle/01-criteres.md` §4. Calcul : `python3 -I _scripts/calculs/synthese_grilles.py`, qui lit les cinq pages publiées (`05-artifacts/*.html`).

| Axe | Renaissance | RN | LFI | PS | LR |
|---|---|---|---|---|---|
| 1. Finances publiques et dette | D4 F3 C2 E3 | D4 F3 C3 E3 | D4 F3 C4 E3 | D4 F3 C2 E3 | D3 F3 C2 E3 |
| 2. Travail, protection sociale et fraude | D3 F3 C2 E3 | D3 F3 C4 E3 | D3 F3 C3 E3 | D3 F3 C3 E3 | D3 F3 C2 E3 |
| 3. Immigration | D4 F3 C3 E3 | D3 F2 C2 E3 | D3 F3 C4 E3 | D4 F3 C3 E3 | D4 F2 C3 E3 |
| 4. Pouvoir d'achat et fiscalité | D4 F2 C2 E3 | D4 F3 C3 E3 | D4 F3 C3 E3 | D3 F3 C2 E3 | D4 F3 C2 E3 |
| 5. Sécurité et libertés | D3 F2 C2 E4 | D3 F3 C4 E4 | D4 F3 C4 E3 | D3 F3 C2 E3 | D3 F2 C4 E4 |
| 6. Institutions, démocratie et Europe | D4 F2 C2 E3 | D4 F2 C4 E3 | D4 F2 C4 E3 | D4 F2 C2 E3 | D4 F2 C4 E3 |
| Comment ils gouvernent (M) | 2 | 3 | 4 | 3 | 3 |

Base du verdict C, affichée (socle v2.3) : Renaissance « votes 2022-2026 + actes 2017-2026 » ; PS « votes + actes 2012-2017 » ; LR « votes + actes 2024-2025 » ; RN et LFI « votes seuls ».

### Ce que la matrice montre, échelle par échelle

**Diagnostic (D).** Aucun cran 1 ni 2, aucun cran 5. Les cinq forces décrivent le monde avec des chiffres qui se vérifient dans la statistique publique sur l'essentiel ; les crans 3 sont des lectures à contresens d'un chiffre exact ou un chiffre faux sur une partie du périmètre (règle 19, LR axe 1 ; RN axes 2, 3, 5 ; LFI axes 2, 3 ; PS axes 2, 4, 5 ; Renaissance axes 2, 5). Les cinq ont le cran 4 à l'axe 6 : le constat institutionnel (instabilité, Parlement sans majorité) est partagé et fondé.

**Faisabilité (F).** Aucun cran 4 ni 5 : aucun programme n'est entièrement chiffré par une source de niveau 2 ou 3 avec le véhicule juridique nommé. Les cinq ont le cran 2 à l'axe 6 : les réformes institutionnelles promises exigent une révision constitutionnelle, parfois un traité, et aucune force ne décrit la voie complète pour y parvenir. Les autres crans 2 : Renaissance axes 4 et 5 ; RN axe 3 ; LR axes 3 et 5.

**Cohérence (C).** C'est la seule ligne où les cinq forces se séparent nettement, et c'est la ligne qui ne se compare qu'à base égale (section 2).

**Écoute (E).** Vingt-six cases sur trente au cran 3 (« répond en partie »), quatre au cran 4 (axe 5 pour Renaissance, le RN et LR, où la demande de fermeté, de premier rang, est servie et dite). Aucun cran 2 : aucune force ne va contre une demande de premier rang sans le dire.

**Méthode (M).** Un seul cran 2 (Renaissance : six objets de rupture, dont le 49.3 et la procédure des retraites de 2023, sur un mandat exercé), un cran 4 (LFI : parole de méthode et comportement parlementaire concordants, sans mandat exercé), trois crans 3. La réserve de la ligne 14 du registre des biais s'applique : les forces qui ont gouverné ont des actes de méthode à confronter, les deux autres n'ont que leur parole et leur comportement parlementaire.

## 2. Lire la colonne cohérence : deux familles

Règle v2.3 (`01-socle/01-criteres.md`, échelle C) : un acte de gouvernement contraire à une promesse maintenue vaut à lui seul le cran 2. Une force qui n'a pas gouverné n'est pas plus cohérente, elle est moins testée. Les verdicts C ne se comparent donc qu'au sein d'une même famille (registre des biais, ligne 2).

| Famille | Force | Ligne C (axes 1 à 6) | Crans 2 | Crans 4 | Dont crans 2 par la règle v2.3 |
|---|---|---|---|---|---|
| Votes + actes | Renaissance (2017-2026) | 2 / 2 / 3 / 2 / 2 / 2 | 5 | 0 | 1 (axe 2 : décret du 30 juin 2024 suspendant la réforme de l'assurance chômage) ; axe 5 au cran 2 depuis l'option B du 2026-10-28 (trois objets, dont la libération sous contrainte de 2021) |
| Votes + actes | PS (2012-2017) | 2 / 3 / 3 / 2 / 2 / 2 | 4 | 0 | 2 (axe 1 : TSCG ratifié sans renégociation ; axe 5 : récépissé refusé en 2012-2013) |
| Votes + actes | LR (2024-2025) | 2 / 2 / 3 / 2 / 4 / 4 | 3 | 2 | 3 (axe 1 : dépôt du PLF 2025 ; axes 2 et 4 : 49.3 du 2 décembre 2024, pensions et allègements de cotisations) |
| Votes seuls | RN | 3 / 4 / 2 / 3 / 4 / 4 | 1 | 3 | 0 (axe 3 : règle v2.1, mesure structurante) |
| Votes seuls | LFI | 4 / 3 / 4 / 3 / 4 / 4 | 0 | 4 | 0 |

Compte par famille, sans total ni moyenne : famille « votes + actes », 12 crans 2 sur 18 verdicts, dont 6 par la règle v2.3 ; famille « votes seuls », 1 cran 2 sur 12 verdicts. L'écart entre les deux familles est pour partie mécanique (les forces qui ont gouverné ont plus d'objets d'écart possibles) et pour partie documenté (six crans 2 de la famille « votes + actes » viennent des votes, des textes, des promesses non réalisées et des revirements, pas de la règle v2.3 : Renaissance axes 1, 4, 5, 6 ; PS axes 4, 6). Option B sur les revirements décidée par Dilhan le 2026-10-28 : une case a bougé, Renaissance axe 5 (`note-de-methode.md` §3.1). La note de méthode (`note-de-methode.md`, §2) détaille ce compte.

Les crans 4 de la ligne C : LFI (axes 1, 3, 5, 6), RN (axes 2, 5, 6), LR (axes 5 et 6, où le groupe DR a voté et porté ce que le programme écrit, sans acte de coalition contraire).

## 3. La carte des tendances lourdes, cinq forces côte à côte

Quatorze tendances gelées (`03-sources/tendances-lourdes.md`), quatre statuts (traitée, traitée en partie, nommée sans mesure, absente ; `01-socle/01-criteres.md` §8). Calcul : `python3 -I _scripts/calculs/synthese_tendances.py`, qui lit les cinq cartes `02-partis/<force>/tendances.md`.

| N° | Tendance | Renaissance | RN | LFI | PS | LR | Forces qui traitent |
|---|---|---|---|---|---|---|---|
| 1 | Vieillissement et ratio actifs / seniors | T | T | T | T | T | 5 |
| 2 | Solde naturel négatif, migrations seule source de croissance démographique | TP | T | TP | TP | T | 2 |
| 3 | Hausse du nombre de ménages, portée par les personnes seules | TP | TP | TP | TP | TP | 0 |
| 4 | Charge d'intérêts de la dette | T | T | T | T | T | 5 |
| 5 | Productivité et écart avec les États-Unis | T | T | TP | T | T | 4 |
| 6 | Intelligence artificielle et transformation des emplois | T | TP | TP | T | T | 3 |
| 7 | Départs massifs en fin de carrière et tensions de recrutement | TP | TP | TP | TP | TP | 0 |
| 8 | Réchauffement, événements extrêmes et coût de l'adaptation | T | TP | T | T | TP | 3 |
| 9 | Transition énergétique et électrification | T | TP | T | T | T | 4 |
| 10 | Tensions sur l'eau et relève agricole | TP | TP | T | T | T | 3 |
| 11 | Concentration du patrimoine et poids de l'héritage | TP | TP | T | T | TP | 2 |
| 12 | Perte d'autonomie des personnes âgées et démographie médicale | TP | TP | T | T | TP | 2 |
| 13 | Dépenses de défense et dégradation de l'environnement stratégique | T | T | T | T | T | 5 |
| 14 | Bascule de l'accès à l'information vers les plateformes | T | TP | TP | T | TP | 2 |

Comptes par force (traitées / en partie / nommées / absentes) : Renaissance 8 / 6 / 0 / 0 ; RN 5 / 9 / 0 / 0 ; LFI 8 / 6 / 0 / 0 ; PS 11 / 3 / 0 / 0 ; LR 8 / 6 / 0 / 0.

**Les problèmes que personne ne regarde.** Aucune tendance n'est absente ni seulement nommée chez l'une des cinq forces : les quatorze sont au moins traitées en partie partout. Deux tendances ne sont traitées à fond par personne : la hausse du nombre de ménages portée par les personnes seules (n° 3 : chaque programme touche le logement, aucun ne part de la taille des ménages) et les départs massifs en fin de carrière avec les tensions de recrutement (n° 7 : chaque programme touche l'emploi ou la formation, aucun ne traite le remplacement des départs comme un problème en soi). Trois tendances sont traitées par les cinq : le vieillissement (n° 1), la charge d'intérêts de la dette (n° 4), les dépenses de défense (n° 13). La carte ne juge pas si les réponses suffisent.

## 4. Les demandes exprimées, cinq forces côte à côte

Quarante-sept demandes gelées avant lecture des programmes (`03-sources/demandes-exprimees.md`), statut lu dans les tableaux Q5 des fiches. Codes : T (traitée), TP (traitée en partie), NT (non traitée, silence), C (le programme va contre et le dit), TC et TPC (traitée ou traitée en partie, avec un contre-pied partiel assumé), P (demande à deux branches opposées, la branche servie est nommée). Calcul : `python3 -I _scripts/calculs/synthese_ecoute.py`, qui lit les cinq scripts `<force>_ecoute_decompte.py`.

| Axe | Demande | Renaissance | RN | LFI | PS | LR |
|---|---|---|---|---|---|---|
| 1 | Réduire le déficit surtout par la baisse des dépenses | T | T | C | C | T |
| 1 | Réduire le train de vie de l'État | T | T | TP | T | T |
| 1 | Faire contribuer en priorité les grandes entreprises et les plus aisés | TPC | TPC | T | T | TPC |
| 1 | Traiter la dette comme une urgence et inscrire une règle d'or | T | T | TPC | TP | T |
| 1 | Maintenir les prestations et les services publics, refuser les gels | C | TP | T | T | C |
| 1 | Réduire le nombre de fonctionnaires | T | TP | C | C | T |
| 1 | Garder dans le public ou renationaliser les services essentiels | NT | TP | T | NT | C |
| 2 | Ne pas reculer l'âge de départ | NT | T | T | T | C |
| 2 | Garder des retraites et une assurance maladie publiques | T | T | T | T | T |
| 2 | Maintenir l'indexation des pensions | T | T | T | T | T |
| 2 | Renforcer la lutte contre la fraude sociale, revoir les conditions | T | T | TPC | TPC | T |
| 2 | Lutter contre le non-recours | C | NT | T | T | TP |
| 2 | Durcir l'indemnisation du chômage et les arrêts de travail | TP | TPC | C | C | T |
| 2 | Augmenter les aides à la dépendance et au handicap | C | TP | T | T | NT |
| 2 | Revaloriser le RSA et les minima sociaux | T | TP | T | TP | C |
| 2 | Ne pas augmenter le reste à charge en santé | C | TP | T | T | C |
| 2 | Aménager la fin de carrière, tenir compte de la pénibilité | T | T | T | T | T |
| 3 | Réduire le niveau de l'immigration | T | T | C | C | T |
| 3 | Accueillir les demandeurs d'asile persécutés | TP | TPC | T | T | C |
| 3 | Recourir moins à l'immigration de travail | C | C | NT | C | T |
| 3 | Régulariser les travailleurs sans papiers des métiers en tension | NT | T | T | T | C |
| 3 | Restreindre l'accès des étrangers aux prestations (ou égalité) | P:restriction en partie | P:restriction | P:égalité | P:égalité | P:restriction |
| 3 | Conditionner l'intégration à l'apprentissage du français | T | NT | NT | TP | T |
| 4 | Augmenter le Smic et les salaires | TPC | TP | T | T | TP |
| 4 | Baisser les impôts des ménages, surtout des classes moyennes | T | T | TPC | TC | T |
| 4 | Taxer davantage les très hauts patrimoines et les hauts revenus | C | TPC | T | T | C |
| 4 | Baisser la TVA sur les produits de première nécessité | TP | T | TC | TC | TP |
| 4 | Indexer salaires, pensions et allocations sur l'inflation | C | TP | T | TP | TP |
| 4 | Baisser le prix des carburants et de l'énergie | T | T | T | T | T |
| 4 | Bloquer ou encadrer les prix | NT | TP | T | T | TP |
| 4 | Encadrer les loyers, construire des logements abordables | NT | TPC | T | T | C |
| 4 | Réduire les écarts de revenus (ou mieux rémunérer le travail) | P:travail | P:travail | P:redistribution | P:redistribution | P:travail |
| 4 | Revaloriser les bourses et les aides aux étudiants | TP | TP | TP | TP | NT |
| 5 | Plus de fermeté dans le maintien de l'ordre (ou encadrer la force) | P:fermeté | P:fermeté | P:encadrement | P:encadrement | P:fermeté |
| 5 | Donner plus de moyens à la police, à la gendarmerie et à la justice | TP | TP | TP | T | TP |
| 5 | Rétablir la peine de mort | NT | NT | NT | NT | NT |
| 5 | Encadrer l'usage de la force | NT | C | T | T | C |
| 5 | Garantir le droit de manifester | NT | C | T | T | NT |
| 5 | Sanctionner les violences et les contrôles abusifs | NT | NT | T | T | NT |
| 6 | Recourir plus souvent au référendum, y compris d'initiative citoyenne | TPC | T | T | T | TP |
| 6 | Réduire le nombre et les avantages des élus | TP | TP | TP | NT | NT |
| 6 | Prendre en compte le vote blanc | NT | NT | T | T | NT |
| 6 | Changer de Constitution | TP | TP | T | T | TP |
| 6 | Démission ou destitution du président | NT | NT | T | C | NT |
| 6 | Gouverner avec une majorité nette (ou par compromis) | P:compromis | P:majorité | P:aucune | P:compromis | P:majorité nette |
| 6 | Plus de pouvoir au niveau national qu'à l'UE | C | T | T | C | T |
| 6 | Démarches accessibles et services publics de proximité | TP | TP | T | T | TP |

**Les demandes que personne ne traite.** Une seule demande sur 47 est passée sous silence par les cinq forces : le rétablissement de la peine de mort (axe 5, intensité contestée). Trois autres sont passées sous silence par trois forces (Renaissance, RN, LR) et traitées par deux (LFI, PS) : sanctionner les violences et les contrôles abusifs des forces de l'ordre, prendre en compte le vote blanc, la démission ou la destitution du président (que le PS contredit en l'assumant). Quatre demandes sont traitées par les cinq : garder des retraites et une assurance maladie publiques, maintenir l'indexation des pensions, aménager la fin de carrière, baisser le prix des carburants et de l'énergie. Quatre demandes sont contredites en l'assumant, en tout ou en partie, par trois forces ou plus : faire contribuer en priorité les grandes entreprises et les plus aisés (Renaissance, RN, LR, qui la traitent en partie et vont contre sur un volet), durcir l'indemnisation du chômage (LFI et PS vont contre, le RN en partie), recourir moins à l'immigration de travail (Renaissance, RN, PS vont contre), taxer davantage les très hauts patrimoines (Renaissance et LR vont contre, le RN en partie).

Comptes par force (traitées / en partie / silence / contredites / paires) : Renaissance 13 / 11 / 11 / 8 (+ 3 partielles) / 4 ; RN 15 / 19 / 6 / 3 (+ 5 partielles) / 4 ; LFI 29 / 7 / 3 / 4 (+ 4 partielles) / 4 ; PS 27 / 6 / 3 / 7 (+ 3 partielles) / 4 ; LR 15 / 10 / 8 / 10 (+ 1 partielle) / 4. Ces comptes décrivent la couverture de l'inventaire, pas sa qualité : le socle ne sanctionne pas d'aller contre une demande, seulement de ne pas le dire (ligne 15 du registre des biais). Les quatre demandes à deux branches opposées sont codées « branche servie » pour les cinq forces (normalisation du 2026-10-28, `note-de-methode.md` §4).

## 5. Ce qu'ils proposent en commun, axe par axe

Relevé consolidé par trois agents à partir des trente fiches d'axe (`travail/convergences-axes-1-2.md`, `-3-4.md`, `-5-6.md`), sans relais de presse ni recherche web ; les ampleurs sont celles que chaque fiche attribue à sa force, « non chiffré » quand la fiche n'en donne pas. Un objet est commun quand deux forces ou plus le portent dans le même sens dans leur corpus vivant (pas un programme antérieur non repris). Les votes sont ceux des scrutins gelés (`03-sources/scrutins-positions.md`).

### Axe 1 : finances publiques et dette (29 objets communs)

**À quatre forces.** La fraude fiscale comptée en recette : RN (TVA à la source 18 Md€ et cartels 5,8 Md€ en 2031), LFI (2 Md€ la première année), PS (5,5 Md€ en 2027, fraude sociale comprise), LR (5 Md€ en 2032) ; Renaissance n'a rien de nouveau en 2026.

**À trois forces.** Renaissance, RN et LR partagent la structure du redressement : un plan d'économies chiffré sur le quinquennat (150, 140 et 197 Md€), un déficit sous 3 % avant 2032 (RN 2030, LR 2031, Renaissance « avant 2032 »), une règle d'or dans la Constitution par référendum (non chiffrée pour les trois ; la lettre d'octobre de Renaissance ne mentionne plus le référendum), la réduction de l'immobilier de l'État. Renaissance, PS et LR : les doublons entre l'État et les collectivités (plus de 7 Md€, plus de 7,5 Md€, 4 Md€). LFI, PS et LR : la réduction des niches fiscales (22 Md€, incluses dans 12,1 Md€, 4,9 Md€). Renaissance (parti), PS et LFI : assouplir les règles budgétaires européennes, par trois instruments différents.

**Deux blocs.** Sur le levier du redressement, Renaissance, RN et LR mettent la dépense d'abord, LFI et PS les recettes d'abord (106,4 Md€ et 39,5 Md€ bruts de recettes en 2027). Même partage sur le niveau global des prélèvements (aucune hausse d'un côté, hausses ciblées de l'autre) et sur les effectifs publics (baisse de 100 000 et 400 000 postes contre des recrutements ciblés). La règle d'or oppose Renaissance, RN et LR à LFI ; le PS ne la traite pas. Les votes suivent le même partage : LFI et SOC contre EPR, DR et RN sur la première partie du PLF 2025 (438) et la motion de rejet du PLF 2027 (8707) ; la motion de censure de décembre 2024 (519) réunit LFI, SOC et RN. Deux compléments ajoutés le 30 octobre 2026 (scrutins du 27 octobre sur le budget 2027) : sur la fin de la contribution exceptionnelle des grandes entreprises (9123, adoptée à deux voix), EPR et RN votent pour, LFI, SOC et DR contre, le groupe DR se retrouvant avec la gauche pour maintenir une contribution que son programme exclut ; sur l'impôt des multinationales assis sur l'activité en France (9140 à 9142, un objet, trois amendements), LFI et SOC votent pour les véhicules de LFI et du groupe GDR, EPR et DR contre les trois, le RN pour le sien et s'abstient sur les deux autres.

**Silence commun.** Aucune demande de l'inventaire n'est passée sous silence par trois forces ; la plus proche, garder dans le public ou renationaliser les services essentiels (intensité forte), est sans mesure chez Renaissance et le PS, et LR va contre en partie.

### Axe 2 : travail, protection sociale et fraude (25 objets communs)

**À quatre forces.** L'indexation des pensions maintenue (LFI, RN, PS et LR ; pour LR, le discours seulement, la fiche relevant l'acte de décembre 2024 en sens inverse) ; le versement automatique des prestations (Renaissance, LR, PS, LFI, aucune des quatre ne le chiffre) ; la pénibilité dans les conditions de départ (PS, LFI, RN, LR, non chiffrée).

**À trois forces.** LFI, RN et PS reviennent à 62 ans ou moins (LFI 9 Md€, RN 9,5 Md€ en 2031, PS non chiffré) et abrogent les réformes de l'assurance chômage depuis 2017. Renaissance, LR et RN ajoutent un pilier de capitalisation (LR : environ un quart de la retraite des jeunes, 17,8 Md€ de ressources en 2032), durcissent les arrêts maladie et les jours de carence (LR 7 Md€), renforcent le contrôle des allocataires et allègent les heures supplémentaires. Renaissance et LR durcissent les règles de 2024 de l'assurance chômage (3,6 Md€ et 4 à 5 Md€). LFI et PS : garantie d'autonomie des jeunes (LFI 9,5 Md€), ASPA au seuil de pauvreté (mêmes montants, 16 044 € par an), RSA inconditionnel, présomption de salariat des plateformes.

**Deux blocs.** Sur l'assurance chômage, Renaissance et LR durcissent, LFI, RN et PS abrogent : les cinq se répartissent en deux camps. Sur l'âge de départ, LFI, RN et PS d'un côté, Renaissance (système sans âge légal) et LR (63 ans avec décote) de l'autre. Sur l'indexation, Renaissance est seule avec son année blanche de 2028. Les votes : EPR et DR contre LFI, SOC et RN sur la suppression de l'article 1er de la PPL d'abrogation (468) ; EPR, DR et RN contre LFI et SOC sur la loi contre les fraudes (6023). Le 217 (PPL RN sur les retraites) n'est pas exploitable pour LFI, qui n'a exprimé aucune voix.

**Silence commun.** Augmenter les aides à la dépendance et au handicap (intensité large) : aucune mesure de hausse chez Renaissance, LR et le RN (le RN traite en partie, sans hausse) ; LFI et le PS la traitent.

### Axe 3 : immigration (33 objets communs)

**À quatre forces.** La coopération des pays d'origine sur la réadmission, par les visas, l'aide au développement ou l'admission : Renaissance, RN, LR, PS, aucune ne la chiffre.

**À trois forces.** Renaissance, RN et LR : éloignement plus systématique des étrangers condamnés, regroupement familial restreint (LR 1,5 Md€ en 2032), contrôles aux frontières renforcés, AME restreinte (RN 1,3 Md€, LR 0,7 Md€ ; Renaissance réforme selon le rapport Évin-Stefanini, sans suppression). Renaissance, LFI et PS : droit au travail des demandeurs d'asile ouvert ou avancé. RN et LR partagent dix autres objets (condition de durée pour les prestations non contributives, 12,2 et 3,6 Md€ ; hébergement d'urgence réservé ; titre pour soins abrogé ; frais des étudiants étrangers ; accord de 1968 ; Schengen réservé aux citoyens de l'Union ; asile examiné hors du territoire ; délit de séjour irrégulier). LFI et PS en partagent douze (régularisation des travailleurs, carte de dix ans, abrogation des lois récentes, Ofpra hors de l'Intérieur, présomption de minorité, Dublin, statut des déplacés climatiques, vote local des étrangers).

**Deux blocs.** Dix oppositions nettes, presque toutes entre RN et LR d'un côté, LFI et PS de l'autre : AME, régularisations, prestations des étrangers en situation régulière, droit du sol (Renaissance refuse sa suppression dans l'Hexagone), centres de retour dans des pays tiers (LR seul pour), règles européennes de retour (Renaissance et LR durcissent), frais des étudiants, coût des titres, minorité des mineurs non accompagnés. Les votes : EPR, DR et RN contre LFI et SOC sur la rétention des étrangers condamnés (2958) ; DR et RN contre LFI, SOC et EPR sur la dénonciation des accords de 1968 (3260).

**Silence commun.** Conditionner l'intégration à l'apprentissage du français et de l'histoire (intensité forte) : comme condition, seul LR la porte pour les deux ; Renaissance pour le français ; RN (mesures de 2022 non reprises), LFI et PS ne la traitent pas.

### Axe 4 : pouvoir d'achat et fiscalité (33 objets communs)

**À quatre forces.** Baisser les prélèvements sur le salaire pour augmenter le net : Renaissance (250 € nets par mois au salaire médian), LR (15 Md€), PS (CSG baissée sous 2 700 € par mois, 15 Md€), RN (non chiffré), par des instruments différents. Fonder le prix de l'électricité sur les coûts de production : RN (9,3 Md€ en 2031), LFI, PS, LR (moins 5 %, puis 5 à 10 %) ; Renaissance donne une cible (75 €/MWh) sans instrument.

**À trois forces.** Renaissance, RN et LR : baisse des cotisations patronales et des impôts de production (RN 17,1 Md€, LR près de 15 Md€), allègement des successions en ligne directe, pacte Dutreil défendu, refus de toute hausse d'impôt. Renaissance, RN et LFI : taxe sur les rachats d'actions (RN 8,4 à 11,35 Md€, LFI 2,5 Md€). RN, LFI et PS : TVA réduite ou nulle sur les produits de première nécessité (RN 3,5 Md€), taxe des profits exceptionnels, indexation des pensions et prestations. LFI et PS partagent treize objets (Smic à environ 1 700 € net, impôt plancher de 2 % à 15 Md€ et 15 à 25 Md€, suppression du PFU, successions sur les transmissions reçues sur la vie, pacte Dutreil supprimé, écarts de rémunération de 1 à 20, encadrement des loyers).

**Deux blocs.** Douze oppositions nettes, sur le partage Renaissance, RN, LR contre LFI, PS : niveau des prélèvements, impôt plancher, successions, pacte Dutreil, allègements de cotisations, impôts de production. Trois cas sortent du partage : la TVA à 5,5 % sur l'énergie (RN seul pour, LFI et PS la refusent par écrit), le quotient familial (LFI et LR le remplacent par un montant par enfant, le RN le renforce), l'indexation des prestations (Renaissance seule avec son année blanche). Les votes : LFI et SOC contre EPR, DR et RN sur la taxe Zucman (3300) et la défiscalisation des heures supplémentaires (3089) ; le RN seul pour la TVA à 5,5 % sur l'énergie (4038) ; SOC seul contre l'indexation du barème (3096). Sur le Smic, pas d'opposition nette dans le corpus de 2026 : Renaissance, le RN et LR se taisent.

**Silences communs.** Quatre demandes de l'inventaire sans mesure chez trois forces ou plus : augmenter le Smic (large, premier rang : Renaissance, RN, LR), indexer les salaires sur l'inflation (Renaissance, RN, LR, PS ; LFI seule, par l'échelle mobile), bloquer ou encadrer les prix alimentaires (Renaissance, LR, RN), revaloriser les bourses étudiantes (RN, LFI, PS, LR ; Renaissance seule, sans montant).

### Axe 5 : sécurité, ordre public et libertés (39 objets communs)

**À quatre forces.** La construction de places de prison (Renaissance, RN, LR, PS, aucune chiffrée en 2024-2026) et des établissements différenciés selon le profil des détenus (les mêmes quatre).

**À trois forces.** Renaissance, RN et LR : des seuils minimaux de peine que le juge ne peut écarter que par décision motivée, un régime pénal rapproché de celui des majeurs dès 16 ans, la dissolution accélérée des organisations jugées violentes. Renaissance et LR : révision de la Constitution pour lever les censures de 2025 sur la justice des mineurs, rétention de sûreté étendue, vidéoprotection algorithmique, pouvoirs judiciaires des polices municipales, interdiction du voile aux mineures. RN et LR : présomption de légitime défense des policiers (PPL n° 748 et n° 691), « casseur-payeur », suspension des allocations des parents de mineurs délinquants. LFI et PS partagent vingt et un objets, la plupart signés en commun dans le texte du Nouveau Front populaire de 2024 : police de proximité (LFI 40 000 agents), doctrine de désescalade, interdiction des armes intermédiaires et des techniques d'immobilisation, restriction de l'ouverture du feu en cas de refus d'obtempérer, autorité de contrôle externe des forces de l'ordre, récépissé de contrôle d'identité.

**Deux blocs.** Onze oppositions nettes, presque toutes sur le même partage : présomption de légitime défense (RN et LR pour ; LFI et PS contre, par l'abrogation ou la réécriture de l'article L. 435-1), justice des mineurs (Renaissance, RN, LR durcissent ; PS et LFI abrogent), restrictions de manifester en période de violences (Renaissance, RN, LR ; LFI et PS garantissent le droit), reconnaissance faciale (Renaissance pour, LFI contre, LR entre les deux), amendes forfaitaires délictuelles, apologie du terrorisme. Les quatre scrutins gelés de l'axe séparent EPR, DR et RN d'un côté, LFI et SOC de l'autre (8279, 805, 7987) ; SOC rejoint le premier bloc sur le narcotrafic (1194), LFI reste seule contre.

**Silences communs.** Rétablir la peine de mort : aucune position dans aucun corpus. Sanctionner les violences et les contrôles abusifs des forces de l'ordre (intensité forte) : aucune mesure chez Renaissance, le RN et LR (LR en avait une dans le projet de Charte du 31 août 2026, retirée le lendemain) ; LFI et le PS la traitent.

### Axe 6 : institutions, démocratie et Europe (33 objets communs)

**À quatre forces.** L'opposition à l'accord UE-Mercosur (LFI, PS, RN, LR ; Renaissance s'est abstenue au scrutin 4244 avec cinq votants, non exploitable) ; la réduction des échelons ou doublons territoriaux (Renaissance plus de 7 Md€, PS plus de 7,5 Md€, RN et LFI non chiffrés, objets visés différents) ; la révision de la Constitution par référendum.

**À trois forces.** Renaissance, RN et LR : la règle d'or budgétaire dans la Constitution par référendum. RN, LR et LFI : la primauté de la Constitution sur le droit de l'Union, par trois voies (PPLC portée par un premier signataire UDR pour le RN ; contrôle « ultra vires » à l'article 88-1 pour LR ; Constitution de la 6e République pour LFI). Renaissance, PS et LFI : des impôts européens comme ressources propres et l'assouplissement des règles budgétaires européennes. PS, RN et LR : la réciprocité dans les accords commerciaux. Renaissance et PS : une Union de type fédéral, le budget et l'emprunt commun accrus (PS 500 Md€), une dimension européenne de la dissuasion, les avoirs russes mobilisés. RN et LR : Schengen réservé aux citoyens de l'Union, une loi organique pour soustraire des lois à l'autorité des traités. LFI et PS : assemblée constituante, vote blanc reconnu, vote à 16 ans, vote local des étrangers, indépendance du parquet, concentration des médias.

**Deux blocs.** Treize oppositions nettes, qui ne suivent pas le partage des axes 4 et 5. Sur le degré d'intégration de l'Union, Renaissance et le PS (« États-Unis d'Europe », « Europe fédérale ») font face au RN, à LR et à LFI, pour des raisons différentes. Sur la défense européenne et la dissuasion, Renaissance et le PS face au RN et à LR. Sur l'OTAN, LFI (sortie) et le RN (commandement intégré, source de fiabilité non établie) face aux trois autres. Sur l'Ukraine, Renaissance et le PS face au RN. Sur l'audiovisuel public, le RN (privatisation) face à LFI et au PS. Sur la destitution du président, LFI face au PS. Un seul scrutin gelé sépare les cinq en deux blocs : la Corse autonome (7454), LFI, SOC et EPR pour, DR et RN contre ; les résolutions européennes rapprochent LFI, SOC, DR et RN face à EPR, et isolent le RN sur Schengen (8611).

**Silences communs.** Prendre en compte le vote blanc, démission ou destitution du président (intensité forte, l'une et l'autre) : sans mesure chez Renaissance, le RN et LR ; LFI et le PS les traitent, le PS contredit la seconde en l'assumant. Réduire le nombre de parlementaires (large, premier rang) : aucune mesure chez le RN, LFI, le PS et LR ; Renaissance seule, par la presse. Rendre les démarches accessibles : rien chez Renaissance, le RN et LR.

### La méthode de gouvernement (12 objets communs)

Le recours accru au référendum est le seul objet porté par les cinq forces, avec des objets différents (journée référendaire annuelle pour Renaissance ; immigration et justice pour LR ; priorité nationale et règle d'or pour le RN ; constituante et révocation pour LFI ; révisions constitutionnelles pour le PS). La proportionnelle est voulue par LFI, le PS et le RN, refusée par LR seul (scrutin majoritaire inscrit dans la Constitution, PPLC n° 1477) ; Renaissance ne la porte plus. Le référendum d'initiative citoyenne est voulu par LFI, le RN et le PS, refusé par le groupe EPR en commission des lois le 4 février 2026 ; le RN n'en veut pas en matière constitutionnelle, LFI oui. Le seuil du référendum d'initiative partagée est abaissé par le PS (1 million), LR (environ 2,4 millions) et LFI. Le 49.3 n'est restreint que par LFI et le PS ; Renaissance, le RN et LR n'en disent rien. Le cumul n'est limité que par LFI et le PS. Sur le mode de gouvernement, LR et le RN cherchent les instruments d'une majorité nette, Renaissance et le PS la coalition et le compromis. Aucun scrutin gelé ne porte sur ces objets.


## 6. Renvois

- Fiches : `02-partis/<force>/axes/<n>-*.md` (un verdict par question, sources numérotées) ; méthode : `02-partis/<force>/methode.md` ; tendances : `02-partis/<force>/tendances.md`.
- Pages publiées : Renaissance https://claude.ai/artifact/DvTLMrSY4DesQbiNN1NkW2 ; RN https://claude.ai/artifact/K4r1V5pr5MTEYm6XHd1Y6b ; LFI https://claude.ai/artifact/Y5vhGKqsBcXhtgtzBpGq6i ; PS https://claude.ai/artifact/NRgowSK65vkZ99HWXb1Bj3 ; LR https://claude.ai/artifact/CGuLPnwpGdtJcDZN8fcXzJ.
- Note de méthode de la synthèse : `04-synthese/note-de-methode.md`.
