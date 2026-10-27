# LR · Contrôle de fidélité, étape 2, axes 1 à 3

- Rédigé le : 2026-10-27
- Données arrêtées au : 2026-10-27
- Auteur : sous-agent Opus (contrôle étape 2)
- Statut : revu (étape 2)
- Version du socle : v2.2
- Fiches contrôlées : `../axes/1-finances-publiques.md`, `../axes/2-travail-protection-sociale.md`, `../axes/3-immigration.md`

Sigles : LR (Les Républicains), DR (groupe « Droite Républicaine » à l'Assemblée nationale), PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PJLC (projet de loi constitutionnelle), PLF (projet de loi de finances), RSA (revenu de solidarité active), RIA (revenu d'incitation à l'activité), CSU (compte social unique), ASU (allocation, ou aide, sociale unique), AME (aide médicale de l'État), OQTF (obligation de quitter le territoire français), APL (aides personnalisées au logement), RIP (référendum d'initiative partagée), Md€ (milliard d'euros).

Méthode. Couche texte de chaque PDF du corpus extraite avec `pdftotext` (page par page et en mise en page conservée) ; copies texte (`.md`) des livrets de plus de 20 Mo et fiches de déclarations lues directement. Chaque passage entre guillemets des trois fiches a été recherché par script (`python3 -I`, hors dépôt) dans le document cité, avec contrôle de la page citée ; les passages non trouvés ont été relus à la main (mise en page en colonnes du programme 2022 [C-LR-29], coupures de mots en fin de ligne). Documents lus en entier ou par section pour les mesures omises : fiches presse du plan [C-LR-12] (17 pages), livret « Travail gagnant » [C-LR-02] p. 3 à 37, note CSU [C-LR-03] p. 1 à 15, notes RIA, chômage et seniors (passages chiffrés), pacte [C-LR-19] (9 pages), PJLC [C-LR-13] et [C-LR-14] (deux versions comparées en code), PPLC n° 2352, PPL n° 378, 689, 693, 2229, 238 (exposés des motifs et articles), livret « Famille » [C-LR-07] p. 4, 11, 14-15, livret « IA » [C-LR-10] p. 26-28 et 45, livret « Logement » [C-LR-09] (recherche par termes, folios 38 à 47), fiches de déclarations [C-LR-15], [C-LR-17], [C-LR-25], [C-LR-32], [C-LR-64] à [C-LR-81]. Trois pages extérieures ouvertes le 2026-10-27 pour vérifier des formulations connues seulement par paraphrase : la page d'une élue portant le plan de 40 Md€ [C-LR-31], la dépêche AFP reprise par Fortuneo [C-LR-78], le compte rendu de la deuxième séance du 13 octobre 2026 [C-LR-80] ; les citations ainsi vérifiées ont été ajoutées aux fiches [C-LR-78] et [C-LR-80] du corpus. Sommes et écarts refaits en code (résultats ci-dessous et dans les fiches). Vocabulaire chargé recherché par script hors guillemets ; `python3 _scripts/lint-texte.py` : aucun tiret long. Les parties réservées aux étapes 3 à 5 étaient vides et le restent.

## Axe 1 : Finances publiques et dette

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q2, « État : Faire mieux » | Citation inexacte ; mesure incomplète | budgets « en base zéro » | budgets en « base zéro » ; ajout : tout programme de plus de 500 M€ évalué négativement est supprimé, sauf vote du Parlement | Le document écrit « Budgets en « base zéro » » | [C-LR-12], p. 5 |
| 3 | Q2, règle d'or de 2011 | Mesure incomplète | « plafond de dépenses annuel » | plafond de dépenses et minimum de mesures nouvelles en recettes chaque année | Les deux plafonds sont dans la même phrase | [C-LR-12], p. 17 |
| 4 | Q2, pacte législatif | Citation inexacte | Contribution « immédiate » | Prêts à contribuer « immédiatement » | Mot du document | [C-LR-19], p. 6 |
| 5 | Q2, PLF 2027 | Vocabulaire | abus de l'indemnisation chômage (hors guillemets) | « abus de l'indemnisation chômage ou des ruptures conventionnelles » | Mot du président du groupe, vérifié sur la dépêche | [C-LR-78] |
| 6 | Q2, PLF 2026 | Vocabulaire ; source | « travail plutôt qu'assistanat » hors guillemets ; titre « 40 milliards d'euros d'économies » non vérifié | Intitulés exacts des blocs, entre guillemets, relus sur la page ; écart de 7,6 Md€ confirmé | Page ouverte au contrôle | [C-LR-31] |
| 7 | Divergences, écart 2 | Citation inexacte | 250 000 ETP « mobilisés » | « l'équivalent de 250 000 emplois publics » | Le livret écrit « nous ne mobilisons que 250 000 » ; « mobilisés » n'y figure pas | [C-LR-10], p. 26 |
| 8 | Divergences, écart 3 | Source | annonce du 22 septembre « sans fiche au corpus » | relais archivé en [C-LR-82], citation exacte du cumul sur cinq ans | Fiche créée au contrôle | [C-LR-82] ; [C-LR-12], p. 8 |
| 9 | Écarts de chiffrage, fraude | Calcul en code | « articulation à vérifier » | 2,7 + 1,6 - 0,3 = 4,0 ; 4,0 + 5,0 = 9,0 ; 9,3 avant déduction ; le tableau déduit 0,3 Md€, le texte parle de 1 Md€ compté avec les retraites ; les « 10 Md€ nets » ne se retrouvent pas | Point 5 de la consigne | [C-LR-12], p. 8 et 12 |
| 10 | Écarts de chiffrage, plan | Calcul en code | Somme des fiches seule | Tableaux internes des fiches 3 à 11 refaits, tous conformes ; plan de 40 Md€ : 10,6 + 15,6 + 6,2 = 32,4 | Point 5 de la consigne | [C-LR-12] ; [C-LR-31] |
| 11 | Limites ; sources | Mise à jour | « À signaler à l'agent principal » (liste des 13 textes) | Correction déjà portée dans `01-corpus.md` ; source [C-LR-82] ajoutée | Constat | [C-LR-19], p. 7-9 |

Divergences ajoutées : aucune. Divergences retirées : aucune (aucune n'était retenue). Écarts vérifiés sur pièces :
- **150 contre 197 Md€** : confirmé. « réaliser les 150 milliards d'euros d'économies que je propose », sans horizon ni périmètre [C-LR-76] ; 197 Md€ en 2032, dont 146 pour le déficit et 51 rendus [C-LR-12, p. 4]. Classement du rédacteur maintenu (précision successive) ; écart de montant à l'étape 4.
- **Fonction publique** : confirmé, objets et horizons différents. « à peu près 250 000 postes » [C-LR-71] ; 250 000 emplois publics gagnés grâce à l'IA, moitié redéployés sans économie, moitié départs non remplacés (7,5 Md€) [C-LR-10, p. 26-27] ; 400 000 départs non remplacés sur le quinquennat, dont 150 000 postes supprimés grâce à l'IA (25 Md€, 62 000 € par poste) [C-LR-12, p. 5] ; 50 000 postes pour le budget 2027 [C-LR-78]. 7,5 Md€ / 125 000 = 60 000 € par poste (calcul en code).
- **40 contre 42 Md€ (retraites)** : unités différentes confirmées sur le relais (« en cumulé sur cinq ans ») et sur la fiche 6 (colonne « Md€ 2032 »).

### Vérifié sans correction

- Citations de Q1 et Q2 exactes et à la bonne page : [C-LR-02] p. 3 et 10, [C-LR-05] p. 5, [C-LR-10] p. 26 et 45, [C-LR-11] p. 10, [C-LR-12] p. 3 à 17, [C-LR-19] p. 6, [C-LR-20], [C-LR-25], [C-LR-29] p. 3, 6, 7, 9, [C-LR-32], [C-LR-35] p. 6/6, [C-LR-38] p. 2 et 5, [C-LR-71], [C-LR-75], [C-LR-76], [C-LR-79], [C-LR-80].
- Trajectoire (déficit, dette, dépense, prélèvements), hypothèses et ventilations des fiches 2 à 15 conformes au document ; écart de dette 137,4 - 122,7 = 14,7 points (« près de 15 points »).
- Couches conformes à `01-corpus.md` et au script `lr_textes_du_groupe.py` (PPLC n° 2352 : texte d'élus du groupe ; amendement n° I-269 : texte du groupe).

### Non vérifiable

- Plan de 50 Md€ d'octobre 2024 [C-LR-30] (relais LCP, non rouvert) ; détail des « plus de 30 milliards » votés au Sénat [C-LR-32].

### Appréciation avant correction

Fiche fidèle et chiffres exacts. Trois citations légèrement inexactes, une paraphrase d'un mot chargé, deux mesures tronquées.

## Axe 2 : Travail, protection sociale et fraude

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Introduction ; Q2 retraites ; déclarations ; sources | Source | Annonce du 22 septembre « non archivée », lue « tel que le corpus le résume » | Fiche [C-LR-82] créée et citée ; détail du relais ajouté (exceptions de pénibilité à définir avec les partenaires sociaux, âge du taux plein indexé sur l'espérance de vie, capitalisation « à peu près un quart », sans effet sur les retraités actuels) | Tâche du contrôle | [C-LR-82] |
| 3 | Q1, groupe (pacte) | Vocabulaire | « valoriser la France qui travaille ou qui a travaillé toute sa vie » plutôt que l'assistanat | Formule entière entre guillemets (15 mots) | Mot du document hors guillemets | [C-LR-19], p. 2 |
| 4 | Q2, durée du travail | Mesure omise | Livret, candidat, 2022 | Ajout : « une sortie intelligente et négociée des 35 heures » (parti, juillet 2025) | Texte du parti au corpus | [C-LR-25] |
| 5 | Q2, aide sociale unique | Citation (paraphrase remplacée) | « aides sociales fusionnées et plafonnées » (paraphrase) ; « allocation sociale unique plafonnée » présentée comme paraphrase | « toutes les aides sociales à 70 % du SMIC fusionnées en une aide unique » ; « notre proposition d'une allocation sociale unique et plafonnée à 70 % du smic » | Formulations relues sur la dépêche et le compte rendu | [C-LR-78] ; [C-LR-80] |
| 6 | Q2, nouvelle ligne | Mesure omise | Absente | Logement social réservé en priorité à ceux qui travaillent (parti, candidat ; PPL n° 687 inscrite à la niche du 6 février 2025, non archivée) | `01-corpus.md` signale cette mesure pour l'axe 2 | [C-LR-07], p. 14-15 ; [C-LR-09] ; [C-LR-67] ; [C-LR-36] |
| 7 | Q2, chômage ; déclarations | Vocabulaire | abus (hors guillemets) | « abus de l'indemnisation chômage ou des ruptures conventionnelles » | Mot du président du groupe | [C-LR-78] |
| 8 | Q2, fraude sociale | Vocabulaire | liste noire nationale des fraudeurs ; sanction des abus (hors guillemets) | Entre guillemets | Mots des documents | [C-LR-12], p. 12 ; [C-LR-19], p. 2 |
| 9 | Q1, aides non contributives | Source | « + 30,8 % » attribué au livret seul | Repris aussi par la fiche 8 du plan | Même chiffre, même attribution aux « dépenses sociales » | [C-LR-12], p. 10 |
| 10 | Divergences, écart 3 | Citation mal attribuée ; réécriture | « ne traiterait pas le problème de fond » attribué à la note CSU | La formule est dans le livret ; la note écrit « ne réglerait pas le cœur du problème » et « n'est pas la bonne réponse » ; écart réécrit avec les trois pièces (voir ci-dessous) | Texte des documents | [C-LR-02], p. 29 ; [C-LR-03], note CSU, p. 1 et 12 |
| 11 | Divergences, écarts 1 et 2 | Source | « relais non archivé » ; « Archiver une fiche avant l'étape 4 » | [C-LR-82] | Fiche créée | [C-LR-82] |
| 12 | Déclarations, 12 février | Vocabulaire | plutôt qu'à l'assistanat (hors guillemets) | « au travail plutôt qu'à l'assistanat » | Mot du candidat | [C-LR-17] |
| 13 | Limites | Calcul en code | Aucun | « + 30,8 % » : taux de la dépense moyenne par allocataire des minima sociaux (5 600 € à 7 300 €, + 30,4 % sur les montants arrondis) ; dépense totale des minima + 42,3 % ; sommes du tableau du livret (12,5 à 15,7 ; 28,5 à 31,7 Md€) conformes | Point 5 de la consigne | [C-LR-03], note CSU, p. 4-5 ; [C-LR-02], p. 29 et 35 |
| 14 | Sources | Forme | 22 sources | [C-LR-82], [C-LR-07], [C-LR-09] ajoutés | Nouvelles références | |

Divergences ajoutées : aucune. Divergences retirées : aucune. **Écart ASU contre CSU, vérifié sur les trois pièces (sans trancher)** :
- [C-LR-25], parti, 16 juillet 2025 : « nous nous félicitons » que le Premier ministre ait repris l'idée, « portée depuis longtemps par notre famille politique », d'une allocation sociale unique, qui « n'a de sens que si elle est plafonnée à 70% du SMIC ».
- [C-LR-02], parti, livret de janvier 2026, p. 29 : l'idée de « fusionner l'ensemble des aides en un versement unique » serait « coûteuse, complexe à mettre en œuvre et ne traiterait pas le problème de fond » ; le livret propose le CSU, plafond de 70 % du Smic net par adulte. La note technique du même mois : l'ASU « n'apporte pas la solution » (p. 1), « n'est pas la bonne réponse » (p. 12). Le plan du 12 octobre 2026 garde le CSU [C-LR-12, p. 10].
- Groupe, octobre 2026 ([C-LR-33] renvoie à [C-LR-78], aucun document du groupe) : « toutes les aides sociales à 70 % du SMIC fusionnées en une aide unique » (président du groupe, dépêche AFP) [C-LR-78] ; « notre proposition d'une allocation sociale unique et plafonnée à 70 % du smic » (orateur du groupe en séance, 13 octobre) [C-LR-80].
Le but est commun ; le parti écarte nommément l'instrument que le groupe propose trois semaines après la publication du plan. Le classement du rédacteur (deux instruments, évolution du parti selon la règle 11) est conservé dans la fiche, avec un signalement explicite à l'agent principal.

Autres écarts vérifiés sur pièces : RIA « coût nul » [C-LR-03, note RIA, p. 2] contre « gain » de 2,0 Md€ [C-LR-02, p. 35 ; C-LR-12, p. 10] : confirmé, écart de chiffrage. CSU « et lutte contre la fraude » 10,0 Md€ [C-LR-02, p. 35] contre CSU 10,0 et fraude 4,0 à part [C-LR-12, p. 10 et 12] : confirmé. Moins de 25 ans [C-LR-12, p. 10] : précision successive, confirmé.

### Vérifié sans correction

- Citations exactes et à la bonne page : [C-LR-02] p. 6, 10, 11, 13, 22, 29, 30, 35, [C-LR-03] (notes CSU, RIA, chômage, seniors), [C-LR-04], [C-LR-12] p. 3, 8 à 13, 16, [C-LR-17], [C-LR-19] p. 2, 6, 8, [C-LR-25], [C-LR-29] p. 6 (mise en page en colonnes relue), [C-LR-39], [C-LR-40], [C-LR-64], [C-LR-65], [C-LR-67], [C-LR-71], [C-LR-76], [C-LR-81].
- Chiffrages des tableaux (chômage, seniors 1,3 et 1,2 Md€, ruptures conventionnelles 515 000 et 6,8 à 8,0 Md€, arrêts maladie, retraites, gestion) conformes.
- Couches : PPL n° 765 du groupe (niche), PPL n° 2227 texte d'élus du groupe, conformes au script.

### Non vérifiable

- [C-LR-82] : relais seul ; aucune source primaire écrite (page vidéo du 23 septembre non visionnée).
- Plans du groupe de 2024 et 2025 : liens seuls.

### Appréciation avant correction

Fiche fidèle et complète sur « Travail gagnant » et le plan. Une citation attribuée au mauvais document dans l'écart le plus important de l'axe, deux mesures omises, plusieurs mots du parti laissés hors guillemets.

## Axe 3 : Immigration, intégration, droits sociaux des étrangers

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q1, le droit | Citation tronquée | L'État de droit a été « dévoyé par une approche idéologique » | L'État de droit a « parfois été dévoyé par une approche idéologique » | « parfois » omis | [C-LR-13], p. 1 |
| 3 | Q1, candidat, Algérie | Mesure déformée | plus de 200 000 visas délivrés en 2025 | délivrés à des Algériens en 2025 | Fiche de l'entretien | [C-LR-66] |
| 4 | Q2, étudiants étrangers | Mesure omise | Plan et candidat | Ajout du livret « Logement » : application stricte de la suppression des APL des étudiants étrangers hors UE non boursiers, 200 M€ par an | Texte du parti | [C-LR-09], folios 46-47 |
| 5 | Q2, hébergement d'urgence | Mesure omise | Parti : fermé aux personnes sous OQTF | Ajout : réviser l'article L. 345-2-2 du code de l'action sociale et des familles « pour conditionner l'hébergement d'urgence à la régularité du séjour » ; durée plafonnée à dix-huit mois ; renvoi à un « projet immigration » non publié | Texte du parti | [C-LR-09], folio 44 |
| 6 | Q2, hébergement ; durée de présence | Citation (paraphrase remplacée) | « limitation » ; « délai de carence pour les étrangers » (paraphrase) | « limitation des frais de l'hébergement d'urgence » ; « l'instauration, pour les étrangers, d'un délai de carence avant de percevoir des allocations », sans durée | Compte rendu relu | [C-LR-80] |
| 7 | Q2, rétention | Mesure omise | Articles 1, 2 et 4 de la PPL n° 378 | Ajout de l'article 3 (condition de délivrance « à bref délai » des documents de voyage supprimée) | Texte de la PPL | [C-LR-41], p. 4 et 6 |
| 8 | Q2, rétention (pacte) | Mesure déformée | « loi de 2024 » | « loi immigration » votée par le Parlement | Le pacte ne date pas la loi | [C-LR-19], p. 3 |
| 9 | Chiffrage de l'axe | Calcul en code | Postes listés | Les huit postes font 10,0 Md€ ; le tableau ne dit pas quels postes forment les 3 Md€ « État » | Point 5 de la consigne | [C-LR-12], p. 6 et 11 |
| 10 | Divergences, écart 5 | Mise à jour | Fiche 9 contre PPL n° 2229 | Livret « Logement » ajouté du côté du périmètre large ; classement inchangé | Mesure omise (correction 5) | [C-LR-09] ; [C-LR-44] |
| 11 | Limites | Pièce relevée | Aucune | Note de la PPL n° 238 : RIP de 2024 de députés et sénateurs LR sur l'accès des étrangers aux prestations, article 1er déclaré contraire à la Constitution (décision n° 2024-6 RIP du 11 avril 2024), à verser à l'étape 3 | Texte au corpus | [C-LR-45], p. 2 |
| 12 | Sources | Forme | 31 sources ; intitulé de la PPL n° 378 hors guillemets | [C-LR-09] ajouté ; intitulé officiel entre guillemets | Vocabulaire du titre | [C-LR-41] |

Divergences ajoutées : aucune. Divergences retirées : aucune. Écarts vérifiés sur pièces :
- **Cinq ans contre deux ans** : confirmé, pas de divergence établie. Charte : versement « peut être subordonné » à cinq ans de séjour régulier et d'activité (art. 12) [C-LR-14, p. 7] ; fiche 9 : cinq ans « Après la révision constitutionnelle soumise à référendum » [C-LR-12, p. 11] ; livret « Famille » : cinq ans pour les dispositifs familiaux, sans mention de révision [C-LR-07, p. 4 et 11] ; candidat [C-LR-67], [C-LR-68] ; président du groupe, pour le PLF 2027 : « conditionner à deux ans l'accès aux aides sociales » [C-LR-78] ; orateur du groupe : délai de carence sans durée, et soutien aux conditions d'accès prévues par le PLF [C-LR-80]. Horizons différents ; fragile (voir rapport).
- **AME** : confirmé, formulations de degré différent ; la PPL n° 238 présente l'AMU comme souhaitable et les mesures Évin-Stefanini comme l'étape possible [C-LR-45, p. 2] ; l'orateur dit « réformer, et non supprimer » [C-LR-80, compte rendu relu].
- **Espagne** : confirmé, précision successive (suspension demandée le 31 juillet [C-LR-73] ; Conseil européen extraordinaire, Schengen réservé aux Européens, visas territorialisés le 2 août [C-LR-74]).
- **Deux versions de la Charte** : comparaison refaite en code, conforme à la fiche (article 10 complété ; phrase sur les agents publics retirée de l'article 1er).

### Vérifié sans correction

- Citations exactes : [C-LR-07] p. 4, [C-LR-12] p. 11, [C-LR-13] p. 1-2, [C-LR-14] p. 2, 5 à 8, [C-LR-15], [C-LR-17], [C-LR-19] p. 3, 7, [C-LR-25], [C-LR-29] p. 5 (colonnes relues), [C-LR-41] à [C-LR-45], [C-LR-66], [C-LR-68], [C-LR-70], [C-LR-73], [C-LR-74], [C-LR-76], [C-LR-78].
- PPL n° 2229 (article unique), n° 693 (deux parents, au moins un an), n° 689 (article L. 425-9) : conformes.
- Couches conformes au script : PPL n° 378, 689, 693, 2229 du groupe ; PPL n° 238 texte d'élus du groupe.

### Non vérifiable

- Circulaire du 23 janvier 2025 [C-LR-55], loi du 11 août 2025, texte de la PPL sénatoriale [C-LR-54] : non ouverts.
- Proposition RIP de 2024 et décision n° 2024-6 RIP : hors corpus.

### Appréciation avant correction

Fiche complète sur les textes constitutionnels et les PPL. Le livret « Logement », seul texte du parti postérieur au pacte qui traite de l'hébergement d'urgence des étrangers, avait été omis.

## Fiche de corpus créée

[C-LR-82], `corpus/C-LR-82-annonce-retraites-2026-09-22-2026-10-27.md` : annonce du candidat sur LCI le 22 septembre 2026, relais franceinfo avec l'AFP (ouvert le 2026-10-27). Source primaire cherchée par l'interface publique du site (publications et médiathèque après le 20 septembre 2026) : seule la page vidéo du 23 septembre (59607), sans texte. `01-corpus.md` mis à jour : synthèse (24 déclarations, 82 fiches, 39 fichiers `.md`), introduction et tableau de la section f, répartition par axe, écart des retraites, « Trous », source secondaire 9.

## Bilan

| Axe | Corrections | Dont fond (citation, mesure, omission, vocabulaire, calcul) |
|---|---|---|
| 1 | 11 | 9 |
| 2 | 14 | 12 |
| 3 | 12 | 10 |

Aucune divergence v2 retenue sur les trois axes, après vérification ; aucune créée, aucune retirée. Aucun tiret long. Citations toutes de 15 mots au plus.

## Questions pour l'agent principal

1. Axe 2, ASU contre CSU : le parti écarte nommément l'ASU en janvier 2026, le groupe la défend comme « notre proposition » en octobre 2026. La fiche garde le classement « deux instruments, évolution du parti » ; la qualification de divergence (même objet : l'instrument de plafonnement) est à arbitrer.
2. Axe 3, cinq ans contre deux ans : non retenu comme divergence (horizons différents), mais le livret « Famille » pose cinq ans sans renvoyer à une révision constitutionnelle. À reprendre à l'étape 5.
3. Axe 1, fiche 10 : le document ne permet pas de retrouver ses « 10 Md€ nets » (0,3 ou 1 Md€ compté avec les retraites). À l'étape 4.

## Erreurs repérées dans `01-corpus.md`

- [C-LR-10] : « l'équivalent de 250 000 agents publics » n'est pas dans le livret ; corrigé en « l'équivalent de 250 000 emplois publics » (p. 26).
- [C-LR-31] : intitulés exacts des trois blocs ajoutés après lecture de la page.
- Fiches [C-LR-78] et [C-LR-80] : citations vérifiées ajoutées (abus de l'indemnisation chômage ; aides fusionnées en une aide unique ; allocation sociale unique ; délai de carence ; frais de l'hébergement d'urgence).
