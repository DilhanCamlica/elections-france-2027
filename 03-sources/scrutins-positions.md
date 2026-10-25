# Positions de vote des groupes sur les scrutins sélectionnés

- Date d'extraction : 2026-10-25.
- Statut : extraction mécanique sur la liste gelée de `scrutins-selectionnes.md` (23 scrutins numérotés dans les six axes, 3 scrutins de réserve, 1 scrutin hors sélection : 27 extraits). Aucune interprétation : des chiffres et des faits.
- Source : jeu open data « Scrutins » de l'Assemblée nationale, XVIIe législature (https://data.assemblee-nationale.fr/travaux-parlementaires/votes), fichiers JSON `VTANR5L17V<n>.json`.
- Version du jeu de données : 9 097 scrutins (n° 1 à 9 097), le dernier daté du 23/10/2026. Archive récupérée le 2026-10-25 à 16:02 (heure de Paris), fichiers lus en lecture seule. Référentiel des organes : AMO10 (députés actifs et organes), complété par AMO30 (historique) pour l'ancien code du groupe UDR.

## Méthode

1. Pour chaque numéro, lecture du JSON : date, intitulé exact, sort, totaux, puis décompte par groupe (champ `decompteVoix`), pour, contre, abstentions, non votants.
2. Les codes d'organe (PO…) sont reliés aux noms de groupe par le référentiel AMO. Les 12 groupes sont présents dans chaque scrutin.
3. Position majoritaire d'un groupe, calculée ici : la position (pour, contre, abstention) qui dépasse 60 % des voix exprimées du groupe (pour + contre + abstention). Sinon « divisé ». Les non votants (présents qui ne prennent pas part au vote) et les absents ne comptent pas dans le dénominateur.
4. Format des cellules : `position (Np Nc Na)`, soit pour, contre, abstentions. Le champ `positionMajoritaire` du JSON est reproduit à part dans les sections, mais n'est pas utilisé (écarts : voir « Anomalies »).
5. Contrôles : somme des groupes égale aux totaux sur 27 scrutins sur 27. Vérification manuelle sur les pages web de 217, 4038 et 8279 (voir « Anomalies »).

Légende : `*` = motion de censure (scrutin 519), seuls les pour sont décomptés. Axe : « rés. » = scrutin de réserve, « hors » = hors sélection. Un groupe à « aucun vote exprimé » compte 0 voix pour, contre et abstention dans le JSON.

## Table de synthèse

Groupes suivis : LFI-NFP (La France insoumise - Nouveau Front Populaire), SOC (Socialistes et apparentés), EPR (Ensemble pour la République), DR (Droite Républicaine), RN (Rassemblement National).

| N° | Axe | Date | Objet court | Sort | LFI | SOC | EPR | DR | RN |
|---|---|---|---|---|---|---|---|---|---|
| 438 | 1 | 12/11/2024 | PLF 2025, 1re partie (recettes) | rejeté | pour (71p 0c 0a) | pour (66p 0c 0a) | contre (1p 87c 4a) | contre (0p 47c 0a) | contre (0p 125c 0a) |
| 519 | 1 | 04/12/2024 | Motion de censure Barnier (49.3 sur PLFSS 2025) | adopté | 71p* | 65p* | 0p* | 0p* | 123p* |
| 4241 | 1 | 21/11/2025 | PLF 2026, 1re partie (recettes) | rejeté | contre (0p 71c 0a) | contre (0p 57c 0a) | abstention (0p 7c 66a) | contre (0p 33c 0a) | contre (0p 117c 0a) |
| 8707 | 1 | 13/10/2026 | PLF 2027, motion de rejet préalable (Vallaud) | rejeté | pour (51p 0c 0a) | pour (64p 0c 0a) | contre (0p 64c 0a) | contre (0p 33c 0a) | contre (0p 62c 0a) |
| 217 | 2 | 31/10/2024 | PPL retraites RN, ensemble (abrogation âge et annuités) | rejeté | aucun vote exprimé (0p 0c 0a) | contre (1p 51c 0a) | contre (0p 58c 0a) | contre (0p 13c 0a) | pour (118p 0c 3a) |
| 468 | 2 | 28/11/2024 | PPL LFI abrogation 64 ans, amdts de suppression art. 1er | rejeté | contre (0p 69c 0a) | contre (0p 43c 0a) | pour (52p 0c 0a) | pour (13p 0c 1a) | contre (0p 81c 0a) |
| 3684 | 2 | 12/11/2025 | PLFSS 2026, art. 45 bis (suspension réforme retraites) | adopté | contre (0p 60c 0a) | pour (67p 0c 0a) | abstention (3p 5c 67a) | divisé (8p 25c 9a) | pour (112p 0c 0a) |
| 6023 | 2 | 07/04/2026 | PJL fraudes sociales et fiscales, ensemble | adopté | contre (0p 71c 0a) | contre (0p 69c 0a) | pour (87p 0c 0a) | pour (48p 0c 0a) | pour (122p 0c 0a) |
| 2958 | 3 | 08/07/2025 | PPL maintien en rétention des étrangers condamnés, ensemble | adopté | contre (0p 58c 0a) | contre (0p 59c 0a) | pour (61p 1c 0a) | pour (48p 0c 0a) | pour (108p 0c 0a) |
| 3260 | 3 | 30/10/2025 | Résolution dénonciation accords franco-algériens de 1968 | adopté | contre (0p 52c 0a) | contre (0p 53c 0a) | contre (0p 30c 3a) | pour (26p 0c 0a) | pour (122p 0c 0a) |
| 351 | 3 | 08/11/2024 | PLF 2025, amdt 58 Ciotti (titre de séjour 1 000 €) | rejeté | contre (0p 23c 0a) | contre (0p 12c 0a) | contre (0p 10c 0a) | divisé (0p 1c 1a) | pour (62p 0c 0a) |
| 881 | 4 | 20/02/2025 | PPL impôt plancher 2 % hauts patrimoines, ensemble | adopté | pour (37p 0c 0a) | pour (36p 0c 0a) | contre (0p 16c 0a) | contre (0p 3c 0a) | abstention (0p 0c 28a) |
| 3300 | 4 | 31/10/2025 | PLF 2026, amdt 2359 (taxe Zucman) | rejeté | pour (60p 0c 0a) | pour (61p 0c 0a) | contre (0p 60c 3a) | contre (0p 28c 0a) | contre (0p 88c 0a) |
| 4038 | 4 | 20/11/2025 | PLF 2026, amdt 792 Le Pen (TVA 5,5 % énergie) | rejeté | contre (0p 27c 0a) | contre (1p 35c 0a) | contre (0p 47c 0a) | contre (0p 10c 2a) | pour (87p 0c 0a) |
| 3089 | 4 | 25/10/2025 | PLF 2026, amdt 618 Wauquiez (heures supplémentaires) | adopté | contre (0p 57c 0a) | contre (0p 57c 0a) | pour (46p 1c 4a) | pour (32p 0c 0a) | pour (77p 0c 0a) |
| 8279 | 5 | 15/07/2026 | PJL réponses immédiates ordre public, ensemble | adopté | contre (0p 65c 0a) | contre (0p 63c 2a) | pour (89p 0c 0a) | pour (46p 0c 2a) | pour (119p 0c 0a) |
| 1194 | 5 | 01/04/2025 | PPL narcotrafic, ensemble | adopté | contre (0p 67c 0a) | pour (63p 0c 0a) | pour (88p 0c 1a) | pour (45p 0c 1a) | pour (123p 0c 0a) |
| 805 | 5 | 13/02/2025 | PPL justice des mineurs, ensemble | adopté | contre (0p 26c 0a) | contre (0p 10c 0a) | pour (56p 0c 0a) | pour (4p 0c 0a) | pour (42p 0c 0a) |
| 7987 | 5 | 07/07/2026 | PPL présomption de légitime défense, ensemble | adopté | contre (0p 69c 0a) | contre (0p 62c 0a) | pour (55p 12c 0a) | pour (48p 0c 0a) | pour (122p 0c 0a) |
| 7454 | 6 | 23/06/2026 | PJ constitutionnel Corse autonome, ensemble | adopté | pour (60p 2c 0a) | pour (41p 5c 19a) | pour (66p 5c 11a) | contre (1p 34c 10a) | contre (0p 120c 0a) |
| 4244 | 6 | 27/11/2025 | Résolution opposition accord UE-Mercosur | adopté | pour (68p 0c 0a) | pour (29p 1c 0a) | abstention (0p 0c 5a) | pour (11p 0c 0a) | pour (64p 0c 0a) |
| 8611 | 6 | 08/10/2026 | Résolution refondation Schengen | rejeté | contre (0p 57c 0a) | contre (0p 37c 0a) | contre (0p 41c 0a) | divisé (9p 1c 5a) | pour (118p 0c 0a) |
| 5313 | 6 | 04/02/2026 | Résolution européenne rejet accord UE-États-Unis | adopté | pour (17p 0c 0a) | pour (16p 0c 0a) | divisé (2p 7c 6a) | pour (4p 0c 0a) | pour (20p 0c 0a) |
| 8854 | rés. 4 | 16/10/2026 | [Réserve] PLF 2027, amdt 665 Roy (succession) | rejeté | contre (0p 14c 0a) | contre (0p 7c 0a) | contre (0p 8c 0a) | contre (0p 4c 0a) | pour (28p 0c 0a) |
| 3096 | rés. 4 | 25/10/2025 | [Réserve] PLF 2026, amdt 269 Wauquiez (indexation barème IR) | adopté | pour (59p 0c 0a) | contre (0p 59c 2a) | pour (39p 6c 4a) | pour (27p 0c 0a) | pour (80p 0c 0a) |
| 3182 | rés. 6 | 28/10/2025 | [Réserve] PPLO report renouvellement Nouvelle-Calédonie | adopté | contre (0p 66c 0a) | pour (56p 4c 6a) | pour (82p 0c 0a) | pour (43p 0c 0a) | contre (0p 116c 0a) |
| 8895 | hors | 20/10/2026 | [Hors sélection] PLFSS 2027, motion de rejet préalable (Panot) | rejeté | pour (53p 0c 0a) | pour (38p 0c 0a) | contre (0p 65c 0a) | contre (0p 31c 0a) | contre (0p 78c 0a) |

`*` Scrutin 519 : motion de censure, seuls les pour sont décomptés (voir la section du scrutin).


## Détail par scrutin

### Scrutin 438 (12/11/2024, axe 1)

- Intitulé exact : la première partie du projet de loi de finances pour 2025 (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **rejeté**. Votants : 573. Suffrages exprimés : 554.
- Totaux : pour 192, contre 362, abstention 19, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 71 | 0 | 0 | 0 | pour | pour |
| SOC | 66 | 66 | 0 | 0 | 0 | pour | pour |
| EPR | 94 | 1 | 87 | 4 | 1 | contre | contre |
| DR | 47 | 0 | 47 | 0 | 0 | contre | contre |
| RN | 125 | 0 | 125 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 16 | 0 | 0 | contre | contre |
| Dem | 36 | 0 | 36 | 0 | 0 | contre | contre |
| HOR | 34 | 0 | 34 | 0 | 0 | contre | contre |
| EcoS | 38 | 37 | 0 | 1 | 0 | pour | pour |
| GDR | 17 | 17 | 0 | 0 | 0 | pour | pour |
| LIOT | 23 | 0 | 12 | 11 | 0 | divisé | contre |
| NI | 8 | 0 | 5 | 3 | 0 | contre | contre |

### Scrutin 519 (04/12/2024, axe 1)

- Intitulé exact : la motion de censure déposée en application de l'article 49, alinéa 3, de la Constitution par Mme Mathilde Panot, M. Boris Vallaud, Mme Cyrielle Chatelain, M. André Chassaigne et 181 membres de l'Assemblée.
- Type de vote : motion de censure. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 331. Suffrages exprimés : 331.
- Totaux : pour 331, contre 0, abstention 0, non votants 1.
- **Motion de censure : seuls les pour sont décomptés** (majorité requise : 289). Les colonnes contre et abstention sont à 0 par construction, et ne signifient pas un vote contre ou une abstention.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 71 | 0 | 0 | 0 | 71p (motion) | pour |
| SOC | 66 | 65 | 0 | 0 | 0 | 65p (motion) | pour |
| EPR | 93 | 0 | 0 | 0 | 1 | 0p (motion) | pour |
| DR | 47 | 0 | 0 | 0 | 0 | 0p (motion) | pour |
| RN | 124 | 123 | 0 | 0 | 0 | 123p (motion) | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 16 | 0 | 0 | 0 | 16p (motion) | pour |
| Dem | 36 | 0 | 0 | 0 | 0 | 0p (motion) | pour |
| HOR | 34 | 0 | 0 | 0 | 0 | 0p (motion) | pour |
| EcoS | 38 | 38 | 0 | 0 | 0 | 38p (motion) | pour |
| GDR | 17 | 16 | 0 | 0 | 0 | 16p (motion) | pour |
| LIOT | 23 | 1 | 0 | 0 | 0 | 1p (motion) | pour |
| NI | 9 | 1 | 0 | 0 | 0 | 1p (motion) | pour |

### Scrutin 4241 (21/11/2025, axe 1)

- Intitulé exact : la première partie du projet de loi de finances pour 2026 (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **rejeté**. Votants : 489. Suffrages exprimés : 405.
- Totaux : pour 1, contre 404, abstention 84, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 71 | 0 | 0 | contre | contre |
| SOC | 69 | 0 | 57 | 0 | 0 | contre | contre |
| EPR | 91 | 0 | 7 | 66 | 1 | abstention | contre |
| DR | 49 | 0 | 33 | 0 | 0 | contre | contre |
| RN | 123 | 0 | 117 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 13 | 0 | 0 | contre | contre |
| Dem | 36 | 0 | 0 | 15 | 0 | abstention | abstention |
| HOR | 34 | 0 | 34 | 0 | 0 | contre | contre |
| EcoS | 38 | 0 | 37 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 16 | 0 | 0 | contre | contre |
| LIOT | 22 | 1 | 14 | 2 | 0 | contre | abstention |
| NI | 9 | 0 | 5 | 1 | 0 | contre | contre |

### Scrutin 8707 (13/10/2026, axe 1)

- Intitulé exact : la motion de rejet préalable, déposée par M. Boris Vallaud, du projet de loi de finances pour 2027 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "La France insoumise - Nouveau Front Populaire"Président du groupe "Socialistes et apparentés".
- Sort : **rejeté**. Votants : 385. Suffrages exprimés : 385.
- Totaux : pour 149, contre 236, abstention 0, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 70 | 51 | 0 | 0 | 0 | pour | pour |
| SOC | 68 | 64 | 0 | 0 | 0 | pour | pour |
| EPR | 90 | 0 | 64 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 33 | 0 | 0 | contre | contre |
| RN | 121 | 0 | 62 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 0 | 9 | 0 | 0 | contre | contre |
| Dem | 37 | 0 | 29 | 0 | 0 | contre | contre |
| HOR | 35 | 0 | 27 | 0 | 0 | contre | contre |
| EcoS | 38 | 26 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 8 | 0 | 0 | 0 | pour | pour |
| LIOT | 23 | 0 | 8 | 0 | 0 | contre | contre |
| NI | 11 | 0 | 4 | 0 | 0 | contre | contre |

### Scrutin 217 (31/10/2024, axe 2)

- Intitulé exact : l'ensemble de la proposition de loi visant à restaurer un système de retraite plus juste en annulant les dernières réformes portant sur l’âge de départ et le nombre d’annuités (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National".
- Sort : **rejeté**. Votants : 334. Suffrages exprimés : 316.
- Totaux : pour 119, contre 197, abstention 18, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |
| SOC | 66 | 1 | 51 | 0 | 0 | contre | contre |
| EPR | 94 | 0 | 58 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 13 | 0 | 1 | contre | contre |
| RN | 125 | 118 | 0 | 3 | 0 | pour | abstention |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 0 | 12 | 0 | abstention | abstention |
| Dem | 36 | 0 | 17 | 0 | 0 | contre | contre |
| HOR | 34 | 0 | 19 | 0 | 0 | contre | contre |
| EcoS | 38 | 0 | 26 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 9 | 0 | 0 | contre | contre |
| LIOT | 23 | 0 | 2 | 1 | 0 | contre | contre |
| NI | 8 | 0 | 2 | 2 | 0 | divisé | contre |

### Scrutin 468 (28/11/2024, axe 2)

- Intitulé exact : l'amendement de suppression n° 4 de M. Sitzenstuhl et les amendements identiques suivants à l'article premier de la proposition de loi d'abrogation de la retraite à 64 ans (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Président du groupe "Ensemble pour la République"Président du groupe "La France insoumise - Nouveau Front Populaire"Président du groupe "Droite Républicaine".
- Sort : **rejeté**. Votants : 342. Suffrages exprimés : 341.
- Totaux : pour 100, contre 241, abstention 1, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 69 | 0 | 0 | contre | contre |
| SOC | 66 | 0 | 43 | 0 | 0 | contre | contre |
| EPR | 94 | 52 | 0 | 0 | 2 | pour | pour |
| DR | 47 | 13 | 0 | 1 | 0 | pour | pour |
| RN | 124 | 0 | 81 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 3 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 18 | 0 | 0 | 0 | pour | pour |
| HOR | 34 | 14 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 0 | 33 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 13 | 0 | 0 | contre | contre |
| LIOT | 23 | 0 | 2 | 0 | 0 | contre | contre |
| NI | 9 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |

### Scrutin 3684 (12/11/2025, axe 2)

- Intitulé exact : l'article 45 bis (examen prioritaire) du projet de loi de financement de la sécurité sociale pour 2026 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National"Président du groupe "Ensemble pour la République"Présidente du groupe "La France insoumise - Nouveau Front Populaire"Président du groupe "Socialistes et apparentés"Président du groupe "Horizons & Indépendants"Président du groupe "Libertés, Indépendants, Outre-mer et Territoires".
- Sort : **adopté**. Votants : 505. Suffrages exprimés : 401.
- Totaux : pour 255, contre 146, abstention 104, non votants 13.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 60 | 0 | 0 | contre | contre |
| SOC | 69 | 67 | 0 | 0 | 0 | pour | pour |
| EPR | 92 | 3 | 5 | 67 | 6 | abstention | abstention |
| DR | 49 | 8 | 25 | 9 | 3 | divisé | abstention |
| RN | 123 | 112 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 14 | 0 | 0 | contre | contre |
| Dem | 36 | 11 | 1 | 18 | 1 | divisé | abstention |
| HOR | 34 | 0 | 29 | 1 | 2 | contre | contre |
| EcoS | 38 | 30 | 0 | 4 | 0 | pour | abstention |
| GDR | 17 | 1 | 11 | 0 | 0 | contre | contre |
| LIOT | 22 | 17 | 0 | 3 | 1 | pour | abstention |
| NI | 9 | 6 | 1 | 2 | 0 | pour | pour |

### Scrutin 6023 (07/04/2026, axe 2)

- Intitulé exact : l'ensemble du projet de loi relatif à la lutte contre les fraudes sociales et fiscales (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 566. Suffrages exprimés : 557.
- Totaux : pour 363, contre 194, abstention 9, non votants 0.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 71 | 0 | 0 | contre | contre |
| SOC | 69 | 0 | 69 | 0 | 0 | contre | contre |
| EPR | 91 | 87 | 0 | 0 | 0 | pour | pour |
| DR | 48 | 48 | 0 | 0 | 0 | pour | pour |
| RN | 122 | 122 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 17 | 0 | 0 | 0 | pour | pour |
| Dem | 37 | 36 | 0 | 0 | 0 | pour | pour |
| HOR | 35 | 32 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 0 | 35 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 17 | 0 | 0 | contre | contre |
| LIOT | 22 | 13 | 1 | 8 | 0 | divisé | abstention |
| NI | 10 | 8 | 1 | 1 | 0 | pour | pour |

### Scrutin 2958 (08/07/2025, axe 3)

- Intitulé exact : l'ensemble de la proposition de loi visant à faciliter le maintien en rétention des personnes condamnées pour des faits d’une particulière gravité et présentant de forts risques de récidive (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 472. Suffrages exprimés : 471.
- Totaux : pour 303, contre 168, abstention 1, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 58 | 0 | 0 | contre | contre |
| SOC | 66 | 0 | 59 | 0 | 0 | contre | contre |
| EPR | 93 | 61 | 1 | 0 | 1 | pour | pour |
| DR | 48 | 48 | 0 | 0 | 0 | pour | pour |
| RN | 123 | 108 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 13 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 25 | 0 | 1 | 0 | pour | pour |
| HOR | 34 | 24 | 0 | 0 | 1 | pour | pour |
| EcoS | 38 | 0 | 33 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 12 | 0 | 0 | contre | contre |
| LIOT | 23 | 19 | 1 | 0 | 0 | pour | pour |
| NI | 12 | 5 | 4 | 0 | 0 | divisé | pour |

### Scrutin 3260 (30/10/2025, axe 3)

- Intitulé exact : la proposition de résolution visant à dénoncer les accords franco-algériens du 27 décembre 1968 (article 34-1 de la Constitution).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National"Présidente du groupe "La France insoumise - Nouveau Front Populaire".
- Sort : **adopté**. Votants : 374. Suffrages exprimés : 369.
- Totaux : pour 185, contre 184, abstention 5, non votants 14.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 52 | 0 | 0 | contre | contre |
| SOC | 69 | 0 | 53 | 0 | 0 | contre | contre |
| EPR | 92 | 0 | 30 | 3 | 7 | contre | contre |
| DR | 50 | 26 | 0 | 0 | 3 | pour | pour |
| RN | 123 | 122 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 15 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 0 | 10 | 2 | 1 | contre | abstention |
| HOR | 34 | 17 | 0 | 0 | 2 | pour | pour |
| EcoS | 38 | 0 | 32 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 6 | 0 | 0 | contre | contre |
| LIOT | 22 | 2 | 1 | 0 | 1 | pour | pour |
| NI | 9 | 3 | 0 | 0 | 0 | pour | pour |

### Scrutin 351 (08/11/2024, axe 3)

- Intitulé exact : l'amendement n° 58 de M. Ciotti après l'article 26 du projet de loi de finances pour 2025 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente de séance.
- Sort : **rejeté**. Votants : 137. Suffrages exprimés : 136.
- Totaux : pour 66, contre 70, abstention 1, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 23 | 0 | 1 | contre | contre |
| SOC | 66 | 0 | 12 | 0 | 0 | contre | contre |
| EPR | 94 | 0 | 10 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 1 | 1 | 0 | divisé | contre |
| RN | 125 | 62 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 4 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 0 | 4 | 0 | 0 | contre | contre |
| HOR | 34 | 0 | 3 | 0 | 0 | contre | contre |
| EcoS | 38 | 0 | 12 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 2 | 0 | 0 | contre | contre |
| LIOT | 23 | 0 | 3 | 0 | 0 | contre | contre |
| NI | 8 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |

### Scrutin 881 (20/02/2025, axe 4)

- Intitulé exact : l'ensemble de la proposition de loi instaurant un impôt plancher de 2 % sur le patrimoine des ultra riches (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Écologiste et Social".
- Sort : **adopté**. Votants : 186. Suffrages exprimés : 155.
- Totaux : pour 116, contre 39, abstention 31, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 37 | 0 | 0 | 0 | pour | pour |
| SOC | 66 | 36 | 0 | 0 | 0 | pour | pour |
| EPR | 94 | 0 | 16 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 3 | 0 | 0 | contre | contre |
| RN | 124 | 0 | 0 | 28 | 0 | abstention | abstention |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 4 | 0 | 0 | contre | contre |
| Dem | 36 | 0 | 9 | 0 | 0 | contre | contre |
| HOR | 33 | 0 | 7 | 3 | 0 | contre | contre |
| EcoS | 38 | 38 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 5 | 0 | 0 | 0 | pour | pour |
| LIOT | 23 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |
| NI | 11 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |

### Scrutin 3300 (31/10/2025, axe 4)

- Intitulé exact : l'amendement n° 2359 de M. Vallaud et les amendements identiques suivants après l'article 3 (examen prioritaire) du projet de loi de finances pour 2026 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "La France insoumise - Nouveau Front Populaire".
- Sort : **rejeté**. Votants : 406. Suffrages exprimés : 400.
- Totaux : pour 172, contre 228, abstention 6, non votants 14.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 60 | 0 | 0 | 0 | pour | pour |
| SOC | 69 | 61 | 0 | 0 | 0 | pour | pour |
| EPR | 92 | 0 | 60 | 3 | 7 | contre | contre |
| DR | 50 | 0 | 28 | 0 | 3 | contre | contre |
| RN | 123 | 0 | 88 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 0 | 5 | 0 | 0 | contre | contre |
| Dem | 36 | 0 | 18 | 2 | 1 | contre | abstention |
| HOR | 34 | 0 | 21 | 1 | 2 | contre | contre |
| EcoS | 38 | 33 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 12 | 0 | 0 | 0 | pour | pour |
| LIOT | 22 | 5 | 5 | 0 | 1 | divisé | pour |
| NI | 9 | 1 | 3 | 0 | 0 | contre | contre |

### Scrutin 4038 (20/11/2025, axe 4)

- Intitulé exact : l'amendement n° 792 de Mme Le Pen après l'article 25 du projet de loi de finances pour 2026 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National".
- Sort : **rejeté**. Votants : 268. Suffrages exprimés : 264.
- Totaux : pour 97, contre 167, abstention 4, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 27 | 0 | 0 | contre | contre |
| SOC | 69 | 1 | 35 | 0 | 0 | contre | contre |
| EPR | 91 | 0 | 47 | 0 | 1 | contre | contre |
| DR | 49 | 0 | 10 | 2 | 0 | contre | abstention |
| RN | 123 | 87 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 8 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 0 | 10 | 0 | 0 | contre | contre |
| HOR | 34 | 0 | 11 | 1 | 1 | contre | contre |
| EcoS | 38 | 0 | 13 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 2 | 0 | 0 | contre | contre |
| LIOT | 22 | 0 | 9 | 1 | 0 | contre | contre |
| NI | 9 | 1 | 3 | 0 | 0 | contre | contre |

### Scrutin 3089 (25/10/2025, axe 4)

- Intitulé exact : l'amendement n° 618 de M. Wauquiez et l'amendement identique suivant après l'article 2 du projet de loi de finances pour 2026 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Président du groupe "Droite Républicaine".
- Sort : **adopté**. Votants : 346. Suffrages exprimés : 342.
- Totaux : pour 183, contre 159, abstention 4, non votants 15.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 57 | 0 | 0 | contre | contre |
| SOC | 69 | 0 | 57 | 0 | 0 | contre | contre |
| EPR | 92 | 46 | 1 | 4 | 7 | pour | pour |
| DR | 50 | 32 | 0 | 0 | 3 | pour | pour |
| RN | 123 | 77 | 0 | 0 | 1 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 4 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 6 | 11 | 0 | 1 | contre | pour |
| HOR | 34 | 11 | 0 | 0 | 2 | pour | pour |
| EcoS | 38 | 0 | 28 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 5 | 0 | 0 | contre | contre |
| LIOT | 22 | 3 | 0 | 0 | 1 | pour | pour |
| NI | 9 | 4 | 0 | 0 | 0 | pour | pour |

### Scrutin 8279 (15/07/2026, axe 5)

- Intitulé exact : l'ensemble du projet de loi visant à offrir des réponses immédiates aux phénomènes troublant l'ordre public, la sécurité et la tranquillité de nos concitoyens (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 556. Suffrages exprimés : 548.
- Totaux : pour 366, contre 182, abstention 8, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 65 | 0 | 0 | contre | contre |
| SOC | 68 | 0 | 63 | 2 | 0 | contre | contre |
| EPR | 91 | 89 | 0 | 0 | 1 | pour | pour |
| DR | 48 | 46 | 0 | 2 | 0 | pour | pour |
| RN | 122 | 119 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 17 | 0 | 0 | 0 | pour | pour |
| Dem | 37 | 35 | 0 | 0 | 0 | pour | pour |
| HOR | 35 | 33 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 0 | 36 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 16 | 0 | 0 | contre | contre |
| LIOT | 23 | 18 | 2 | 3 | 0 | pour | abstention |
| NI | 10 | 9 | 0 | 1 | 0 | pour | pour |

### Scrutin 1194 (01/04/2025, axe 5)

- Intitulé exact : l'ensemble de la proposition de loi visant à sortir la France du piège du narcotrafic (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 550. Suffrages exprimés : 511.
- Totaux : pour 436, contre 75, abstention 39, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 67 | 0 | 0 | contre | contre |
| SOC | 66 | 63 | 0 | 0 | 0 | pour | pour |
| EPR | 94 | 88 | 0 | 1 | 1 | pour | pour |
| DR | 47 | 45 | 0 | 1 | 0 | pour | pour |
| RN | 123 | 123 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 15 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 35 | 0 | 0 | 0 | pour | pour |
| HOR | 33 | 33 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 1 | 3 | 28 | 0 | abstention | contre |
| GDR | 17 | 1 | 5 | 8 | 0 | divisé | abstention |
| LIOT | 23 | 22 | 0 | 1 | 0 | pour | pour |
| NI | 11 | 10 | 0 | 0 | 0 | pour | pour |

### Scrutin 805 (13/02/2025, axe 5)

- Intitulé exact : l'ensemble de la proposition de loi visant à restaurer l'autorité de la justice à l'égard des mineurs délinquants et de leurs parents (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National"Président du groupe "Ensemble pour la République".
- Sort : **adopté**. Votants : 183. Suffrages exprimés : 183.
- Totaux : pour 125, contre 58, abstention 0, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 26 | 0 | 0 | contre | contre |
| SOC | 66 | 0 | 10 | 0 | 0 | contre | contre |
| EPR | 94 | 56 | 0 | 0 | 1 | pour | pour |
| DR | 48 | 4 | 0 | 0 | 0 | pour | pour |
| RN | 124 | 42 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 2 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 7 | 0 | 0 | 0 | pour | pour |
| HOR | 33 | 12 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 0 | 16 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 5 | 0 | 0 | contre | contre |
| LIOT | 23 | 2 | 0 | 0 | 0 | pour | pour |
| NI | 11 | 0 | 1 | 0 | 0 | contre | contre |

### Scrutin 7987 (07/07/2026, axe 5)

- Intitulé exact : l'ensemble de la proposition de loi visant à reconnaître une présomption de légitime défense pour les forces de l'ordre, dans l'exercice de leurs fonctions (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 517. Suffrages exprimés : 512.
- Totaux : pour 313, contre 199, abstention 5, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 69 | 0 | 0 | contre | contre |
| SOC | 68 | 0 | 62 | 0 | 0 | contre | contre |
| EPR | 91 | 55 | 12 | 0 | 1 | pour | pour |
| DR | 48 | 48 | 0 | 0 | 0 | pour | pour |
| RN | 122 | 122 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 14 | 0 | 0 | 0 | pour | pour |
| Dem | 37 | 28 | 1 | 5 | 0 | pour | abstention |
| HOR | 35 | 31 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 0 | 29 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 17 | 0 | 0 | contre | contre |
| LIOT | 23 | 9 | 8 | 0 | 0 | divisé | pour |
| NI | 10 | 6 | 1 | 0 | 0 | pour | pour |

### Scrutin 7454 (23/06/2026, axe 6)

- Intitulé exact : l'ensemble du projet de loi constitutionnelle pour une Corse autonome au sein de la République (première lecture).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 537. Suffrages exprimés : 473.
- Totaux : pour 271, contre 202, abstention 64, non votants 0.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 60 | 2 | 0 | 0 | pour | pour |
| SOC | 68 | 41 | 5 | 19 | 0 | pour | contre |
| EPR | 91 | 66 | 5 | 11 | 0 | pour | pour |
| DR | 48 | 1 | 34 | 10 | 0 | contre | contre |
| RN | 122 | 0 | 120 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 0 | 17 | 0 | 0 | contre | contre |
| Dem | 37 | 25 | 0 | 11 | 0 | pour | pour |
| HOR | 35 | 22 | 0 | 6 | 0 | pour | abstention |
| EcoS | 38 | 27 | 5 | 4 | 0 | pour | contre |
| GDR | 17 | 6 | 6 | 2 | 0 | divisé | pour |
| LIOT | 23 | 21 | 2 | 0 | 0 | pour | pour |
| NI | 10 | 2 | 6 | 1 | 0 | contre | contre |

### Scrutin 4244 (27/11/2025, axe 6)

- Intitulé exact : la proposition de résolution invitant le Gouvernement de la République française à s’opposer à l’adoption de l’accord commercial entre l’Union européenne et le Mercosur (article 34-1 de la Constitution).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "La France insoumise - Nouveau Front Populaire".
- Sort : **adopté**. Votants : 250. Suffrages exprimés : 245.
- Totaux : pour 244, contre 1, abstention 5, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 68 | 0 | 0 | 0 | pour | pour |
| SOC | 69 | 29 | 1 | 0 | 0 | pour | pour |
| EPR | 91 | 0 | 0 | 5 | 1 | abstention | abstention |
| DR | 49 | 11 | 0 | 0 | 0 | pour | pour |
| RN | 123 | 64 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 8 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 8 | 0 | 0 | 0 | pour | pour |
| HOR | 34 | 13 | 0 | 0 | 0 | pour | pour |
| EcoS | 38 | 26 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 8 | 0 | 0 | 0 | pour | pour |
| LIOT | 22 | 6 | 0 | 0 | 0 | pour | pour |
| NI | 9 | 3 | 0 | 0 | 0 | pour | pour |

### Scrutin 8611 (08/10/2026, axe 6)

- Intitulé exact : la proposition de résolution visant à refonder l'espace Schengen en instaurant une double frontière nationale et européenne (article 34-1 de la Constitution).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National".
- Sort : **rejeté**. Votants : 348. Suffrages exprimés : 343.
- Totaux : pour 144, contre 199, abstention 5, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 70 | 0 | 57 | 0 | 0 | contre | contre |
| SOC | 68 | 0 | 37 | 0 | 0 | contre | contre |
| EPR | 90 | 0 | 41 | 0 | 1 | contre | contre |
| DR | 47 | 9 | 1 | 5 | 0 | divisé | pour |
| RN | 121 | 118 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 17 | 0 | 0 | 0 | pour | pour |
| Dem | 37 | 0 | 11 | 0 | 1 | contre | contre |
| HOR | 35 | 0 | 5 | 0 | 0 | contre | contre |
| EcoS | 38 | 0 | 27 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 10 | 0 | 0 | contre | contre |
| LIOT | 23 | 0 | 9 | 0 | 0 | contre | contre |
| NI | 11 | 0 | 1 | 0 | 0 | contre | contre |

### Scrutin 5313 (04/02/2026, axe 6)

- Intitulé exact : l'article unique de la proposition de résolution européenne visant à rejeter le projet d’accord sur les droits de douane et le commerce du 27 juillet 2025 entre l’Union européenne et les États-Unis.
- Type de vote : scrutin public ordinaire. Demandeur : Président du groupe "Ensemble pour la République"Présidente du groupe "La France insoumise - Nouveau Front Populaire"Président du groupe "Gauche Démocrate et Républicaine".
- Sort : **adopté**. Votants : 97. Suffrages exprimés : 90.
- Totaux : pour 83, contre 7, abstention 7, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 17 | 0 | 0 | 0 | pour | pour |
| SOC | 69 | 16 | 0 | 0 | 0 | pour | pour |
| EPR | 92 | 2 | 7 | 6 | 2 | divisé | contre |
| DR | 49 | 4 | 0 | 0 | 0 | pour | pour |
| RN | 122 | 20 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 2 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 5 | 0 | 0 | 0 | pour | pour |
| HOR | 34 | 2 | 0 | 1 | 0 | pour | pour |
| EcoS | 38 | 9 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 3 | 0 | 0 | 0 | pour | pour |
| LIOT | 22 | 2 | 0 | 0 | 0 | pour | pour |
| NI | 10 | 1 | 0 | 0 | 0 | pour | pour |

### Scrutin 8854 (16/10/2026, axe rés. 4)

- Intitulé exact : l'amendement n° 665 de Mme Roy après l'article 4 du projet de loi de finances pour 2027 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National".
- Sort : **rejeté**. Votants : 82. Suffrages exprimés : 80.
- Totaux : pour 30, contre 50, abstention 2, non votants 2.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 70 | 0 | 14 | 0 | 0 | contre | contre |
| SOC | 68 | 0 | 7 | 0 | 0 | contre | contre |
| EPR | 90 | 0 | 8 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 4 | 0 | 0 | contre | contre |
| RN | 121 | 28 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 2 | 0 | 0 | 0 | pour | pour |
| Dem | 37 | 0 | 1 | 1 | 1 | divisé | contre |
| HOR | 35 | 0 | 3 | 1 | 0 | contre | contre |
| EcoS | 38 | 0 | 9 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 0 | 0 | 0 | aucun vote exprimé | pour |
| LIOT | 23 | 0 | 3 | 0 | 0 | contre | contre |
| NI | 11 | 0 | 1 | 0 | 0 | contre | contre |

### Scrutin 3096 (25/10/2025, axe rés. 4)

- Intitulé exact : l'amendement n° 269 de M. Wauquiez après l'article 2 du projet de loi de finances pour 2026 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Président du groupe "Droite Républicaine".
- Sort : **adopté**. Votants : 343. Suffrages exprimés : 330.
- Totaux : pour 226, contre 104, abstention 13, non votants 15.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 59 | 0 | 0 | 0 | pour | pour |
| SOC | 69 | 0 | 59 | 2 | 0 | contre | contre |
| EPR | 92 | 39 | 6 | 4 | 7 | pour | contre |
| DR | 50 | 27 | 0 | 0 | 3 | pour | pour |
| RN | 123 | 80 | 0 | 0 | 0 | pour | pour |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 3 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 2 | 16 | 0 | 2 | contre | pour |
| HOR | 34 | 1 | 6 | 4 | 2 | divisé | contre |
| EcoS | 38 | 8 | 11 | 3 | 0 | divisé | pour |
| GDR | 17 | 5 | 0 | 0 | 0 | pour | pour |
| LIOT | 22 | 2 | 4 | 0 | 1 | contre | contre |
| NI | 9 | 0 | 2 | 0 | 0 | contre | contre |

### Scrutin 3182 (28/10/2025, axe rés. 6)

- Intitulé exact : l'ensemble de la proposition de loi organique visant à reporter le renouvellement général des membres du congrès et des assemblées de province de la Nouvelle-Calédonie afin de permettre la poursuite de la discussion en vue d'un accord consensuel sur l'avenir institutionnel de la Nouvelle-Calédonie (texte de la commission mixte paritaire).
- Type de vote : scrutin public solennel. Demandeur : Conférence des Présidents.
- Sort : **adopté**. Votants : 535. Suffrages exprimés : 526.
- Totaux : pour 279, contre 247, abstention 9, non votants 13.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 71 | 0 | 66 | 0 | 0 | contre | contre |
| SOC | 69 | 56 | 4 | 6 | 0 | pour | abstention |
| EPR | 92 | 82 | 0 | 0 | 6 | pour | pour |
| DR | 50 | 43 | 0 | 0 | 3 | pour | pour |
| RN | 123 | 0 | 116 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 16 | 13 | 0 | 0 | 0 | pour | pour |
| Dem | 36 | 34 | 1 | 0 | 1 | pour | pour |
| HOR | 34 | 32 | 0 | 0 | 2 | pour | pour |
| EcoS | 38 | 1 | 35 | 0 | 0 | contre | contre |
| GDR | 17 | 0 | 17 | 0 | 0 | contre | contre |
| LIOT | 22 | 13 | 6 | 2 | 1 | pour | contre |
| NI | 9 | 5 | 2 | 1 | 0 | pour | pour |

### Scrutin 8895 (20/10/2026, axe hors)

- Intitulé exact : la motion de rejet préalable, déposée par Mme Mathilde Panot, du projet de loi de financement de la sécurité sociale pour 2027 (première lecture).
- Type de vote : scrutin public ordinaire. Demandeur : Présidente du groupe "Rassemblement National"Présidente du groupe "La France insoumise - Nouveau Front Populaire".
- Sort : **rejeté**. Votants : 387. Suffrages exprimés : 387.
- Totaux : pour 128, contre 259, abstention 0, non votants 1.

Groupes suivis en priorité :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| LFI-NFP | 70 | 53 | 0 | 0 | 0 | pour | pour |
| SOC | 68 | 38 | 0 | 0 | 0 | pour | pour |
| EPR | 90 | 0 | 65 | 0 | 1 | contre | contre |
| DR | 47 | 0 | 31 | 0 | 0 | contre | contre |
| RN | 121 | 0 | 78 | 0 | 0 | contre | contre |

Autres groupes (contexte) :

| Groupe | Membres | Pour | Contre | Abst. | Non votants | Position majoritaire (règle 60 %) | Champ JSON |
|---|---|---|---|---|---|---|---|
| UDR | 17 | 0 | 11 | 0 | 0 | contre | contre |
| Dem | 37 | 0 | 28 | 0 | 0 | contre | contre |
| HOR | 35 | 0 | 28 | 0 | 0 | contre | contre |
| EcoS | 38 | 28 | 0 | 0 | 0 | pour | pour |
| GDR | 17 | 9 | 1 | 0 | 0 | pour | pour |
| LIOT | 23 | 0 | 14 | 0 | 0 | contre | contre |
| NI | 11 | 0 | 3 | 0 | 0 | contre | contre |

## Anomalies

- **Nombre de scrutins** : la liste gelée contient 23 numéros dans les tableaux des six axes (4 + 4 + 3 + 4 + 4 + 4), et non 22. Avec les réserves 8854, 3096, 3182 et le hors sélection 8895, 27 scrutins sont extraits. Aucun scrutin introuvable.
- **Dates à confirmer dans la liste** : 7987 est daté du 07/07/2026 dans le JSON (la liste disait « 2026, date à confirmer »). 3096 (réserve, sans date dans la liste) est daté du 25/10/2025.
- **Groupes absents** : aucun. Chaque scrutin comporte 12 groupes. Le groupe UDR figure sous deux codes : PO847173 (« UDR », du 12/09/2024 au 04/09/2025) et PO872880 (« Union des droites pour la République », depuis le 05/09/2025). Le code PO847173 est absent du référentiel AMO10 et a été résolu par AMO30. Dans la table secondaire, les deux sont regroupés sous « UDR ».
- **Groupe sans vote** : LFI-NFP au scrutin 217 (71 membres, 0 pour, 0 contre, 0 abstention, 0 non votant), confirmé par la page web, qui n'affiche aucun vote pour ce groupe. Même cas, hors groupes suivis : GDR au 8854 (17 membres, 0 voix), LIOT au 881, NI aux 468, 351 et 881.
- **Champ JSON `positionMajoritaire` peu fiable** : sur les groupes ayant voté, il diffère de la position la plus fréquente dans 22 cas sur 27 scrutins. Exemples sur les groupes suivis : 4241 EPR (JSON contre, décompte 0p 7c 66a), 217 RN (JSON abstention, 118p 0c 3a), 3684 DR (JSON abstention, 8p 25c 9a), 4038 DR (JSON abstention, 0p 10c 2a), 7454 SOC (JSON contre, 41p 5c 19a), 3096 EPR (JSON contre, 39p 6c 4a), 3182 SOC (JSON abstention, 56p 4c 6a). Pour un groupe sans vote, le JSON affiche « pour » (6 cas). Les décomptes, eux, concordent avec les pages web. Ce fichier s'appuie sur les décomptes.
- **Non votants** : le champ « nonVotants » du JSON compte les présents qui ne prennent pas part au vote (par exemple la présidence de séance), pas les absents. Absents d'un groupe = membres moins (pour + contre + abstention + non votants).
- **Scrutin 519** : motion de censure, seuls les pour sont décomptés (331 pour, majorité requise de 289 ; le JSON affiche contre 0 et abstentions 0 par construction). Le JSON donne « pour » comme position majoritaire de tous les groupes, y compris ceux qui ont 0 voix pour : à ne pas lire.
- **Homonymie** : le n° 3176 désigne trois objets différents. Le scrutin n° 3176 (27/10/2025, amendement n° 2397 de M. Le Coq, PLF 2026), l'amendement n° 3176 de M. Courbon (scrutin 4112, 21/11/2025) et la proposition de loi n° 3176 (Smic, voir « Compléments au gel »).
- **Intitulés** : reproduits tels que dans le JSON, en minuscules initiales, sans retouche. Aucun tiret cadratin n'a dû être remplacé.
- **Écarts JSON et page web** : aucun sur les trois scrutins vérifiés (tableau ci-dessous). La page web n'affiche ni le champ `positionMajoritaire` ni le total des non votants, ils n'ont donc pas été comparés.

### Vérification manuelle sur les pages web de l'Assemblée

Pages https://www.assemblee-nationale.fr/dyn/17/scrutins/217, /4038 et /8279, lues le 2026-10-25. Les totaux et les décomptes des 12 groupes (pour, contre, abstention, non votant) ont été comparés au JSON.

| Scrutin | Totaux page web | Totaux JSON | Décomptes par groupe (12 groupes) | Concordance |
|---|---|---|---|---|
| 217 | 334 votants, 119 pour, 197 contre, 18 abst. | identiques | identiques (LFI-NFP : aucun vote sur les deux) | oui |
| 4038 | 268 votants, 97 pour, 167 contre, 4 abst. | identiques | identiques | oui |
| 8279 | 556 votants, 366 pour, 182 contre, 8 abst. | identiques | identiques | oui |

## Compléments au gel

### 1. Auteur des textes des scrutins 2958, 7987 et 1194

Méthode : fiche du dossier législatif (données ouvertes « Dossiers législatifs », champ « initiateur » du dossier, et notice du document pour 7987), mandat relié au groupe par le référentiel AMO. Les pages de scrutin n'ont pas servi à cet usage. La page web de la fiche de dossier n'affiche pas l'auteur dans son contenu statique, d'où le recours aux données ouvertes de la même fiche.

| Scrutin | Texte (dossier) | Dépôt | Premier signataire | Groupe |
|---|---|---|---|---|
| 2958 | PPL visant à faciliter le maintien en rétention des personnes condamnées pour des faits d'une particulière gravité et présentant de forts risques de récidive (DLR5L17N51429, texte Sénat n° 298, 2024-2025) | Sénat, 03/02/2025 | Mme Jacqueline Eustache-Brinio, sénatrice | Les Républicains (Sénat) |
| 7987 | PPL visant à reconnaître une présomption de légitime défense pour les forces de l'ordre (DLR5L17N51037, texte AN n° 691) | Assemblée nationale, 03/12/2024 | M. Éric Pauget, député | Droite Républicaine (groupe depuis le 19/07/2024) |
| 1194 | PPL visant à sortir la France du piège du narcotrafic (DLR5L17N50169, texte Sénat n° 735, 2023-2024) | Sénat, 12/07/2024 | M. Étienne Blanc, sénateur (premier des deux initiateurs listés) | Les Républicains (Sénat) |

- 2958 : un seul initiateur dans la fiche.
- 1194 : deux initiateurs dans la fiche, M. Étienne Blanc (Les Républicains) puis M. Jérôme Durain, sénateur (groupe Socialiste, Écologiste et Républicain).
- 7987 : auteur unique dans la notice du texte n° 691, plus 45 cosignataires enregistrés (dont 1 retrait), non détaillés ici. **Date exacte du scrutin 7987 : mardi 07/07/2026** (JSON ; la fiche du dossier donne la même date pour l'adoption en première lecture à l'Assemblée, texte adopté n° 328). Adopté par 313 pour, 199 contre, 5 abstentions.
- Les groupes sont ceux du Sénat pour 2958 et 1194 : ils ne correspondent pas à des groupes de l'Assemblée.

### 2. Projet de loi du scrutin 8279 : manifestations et droit de manifester

Texte lu : texte adopté n° 331 de l'Assemblée nationale du 15/07/2026 (celui qui a été voté au scrutin 8279). Dossier DLR5L17N53980 (déposé au Sénat le 25/03/2026, puis Assemblée, CMP le 21/07/2026, saisine du Conseil constitutionnel le 24/07/2026, décision le 14/08/2026, promulgation le 18/08/2026 d'après la fiche).

1. Le texte ne modifie aucune des dispositions du code de la sécurité intérieure sur la déclaration préalable des cortèges, défilés et manifestations sur la voie publique (articles L. 211-1 à L. 211-4 non touchés). Les mots « cortège », « défilé » et « droit de manifester » n'y figurent pas.
2. Il traite des « rassemblements » visés à l'article L. 211-5 du code de la sécurité intérieure : articles 2, 2 bis A, 2 ter, 2 quater A (déclaration au-delà de 250 personnes, délit d'organisation sans déclaration, 2 ans et 30 000 euros, amende forfaitaire pour les participants, remboursement des frais). D'après le code en vigueur, ces rassemblements sont les rassemblements festifs à caractère musical ; le texte lui-même les relie à des matériels de diffusion de musique amplifiée (art. 2).
3. Les articles 4 bis AA et 4 bis AB (code du sport) portent sur l'interdiction de paraître en marge d'une « manifestation sportive », pas sur des manifestations revendicatives.
4. L'article 19 prolonge jusqu'au 31/12/2030 l'expérimentation de traitement algorithmique d'images de vidéoprotection dans des lieux accueillant des « manifestations sportives, récréatives ou culturelles ».
5. Conclusion factuelle : aucune disposition du texte voté n'a pour objet les manifestations sur la voie publique ou le droit de manifester ; le mot « manifestation » y désigne des événements sportifs, récréatifs ou culturels. Lecture limitée au texte adopté le 15/07/2026, pas à la version finale après CMP et Conseil constitutionnel.

### 3. Proposition de loi n° 3176 (Smic)

1. Texte : proposition de loi n° 3176 « visant l'augmentation des salaires et des pensions », déposée le 15/09/2026 par M. Hadrien Clouet, Mme Mathilde Panot et les membres du groupe La France insoumise - Nouveau Front Populaire (dossier DLR5L17N54906). Son article 1er porte le Smic à 1 700 euros net mensuel.
2. Précision : ce n'est pas la proposition « échelle mobile des salaires » (n° 2893, dossier DLR5L17N54446, déposée le 09/06/2026, même auteur principal).
3. Commission des affaires sociales : nomination du rapporteur le 07/10/2026, réunion et rapport n° 3350 le 19/10/2026. 15 amendements déposés.
4. Séance publique : inscrite au jeudi **29/10/2026** (fiche du dossier). Nous sommes le 25/10/2026.
5. **Aucun scrutin n'a eu lieu** : le jeu de données s'arrête au 23/10/2026 (scrutin n° 9 097), aucun scrutin ne se rattache au dossier DLR5L17N54906, et aucun intitulé de scrutin ne contient « Smic » ou « salaire minimum ». Le scrutin remplaçant le n° 881 n'existe donc pas à ce jour. À refaire après le 29/10/2026 : l'examen en niche n'est pas garanti jusqu'à son terme.
