# LFI · Contrôle de fidélité, étape 2, axes 1 à 3

- Rédigé le : 2026-10-26
- Données arrêtées au : 2026-10-26
- Auteur : sous-agent Opus (contrôle étape 2)
- Statut : revu (étape 2)
- Version du socle : v2.2
- Fiches contrôlées : `../axes/1-finances-publiques.md`, `../axes/2-travail-protection-sociale.md`, `../axes/3-immigration.md`

Sigles : LFI (La France insoumise), LAEC (« L'Avenir en commun », programme de LFI), NFP (Nouveau Front populaire), BCE (Banque centrale européenne), CDC (Caisse des dépôts et consignations), CADES (Caisse d'amortissement de la dette sociale), PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PPRE (proposition de résolution européenne), TVA (taxe sur la valeur ajoutée), PME et TPE (petites et moyennes entreprises, très petites entreprises), CDD et CDI (contrat à durée déterminée, indéterminée), Md€ (milliard d'euros), M€ (million d'euros).

Méthode. Couche texte de chaque PDF du corpus extraite deux fois avec `pdftotext` (mise en page conservée, page par page, et ordre de lecture brut, utile pour les PDF en deux colonnes [C-LFI-13], [C-LFI-42]) ; copies texte ([C-LFI-41], [C-LFI-43]) et billets archivés ([C-LFI-79], [C-LFI-81], [C-LFI-83], [C-LFI-72], [C-LFI-74]) lus en entier. Chaque passage entre guillemets des trois fiches a été recherché par script (`python3 -I`, hors dépôt) dans le texte du document cité, puis vérifié à la main pour les copies en colonnes entrelacées de [C-LFI-43]. Longueur des citations comptée par script (seuil : 15 mots). Sommes refaites en code : contre-budget 2027, recettes 106,4 Md€ (14 lignes) et dépenses 81,7 Md€ (37,5 + 22,2 + 10 + 12, chaque bloc recalculé), solde 24,7 Md€ ; contre-budget 2026, 26,6 Md€ (affiché 26,7) ; contre-budget 2025, 21,594 Md€ ; chiffrage 2022, 250 et 267 Md€ ; ASPA de la PPL n° 3176, 1 337 € par mois : toutes conformes aux fiches. Documents prioritaires relus pour les mesures omises : [C-LFI-03] en entier, [C-LFI-13] (chapitres dette, finance, travail, retraites, pauvreté, migrations, nationalité), [C-LFI-22], [C-LFI-42] (pages 10-18, 40, 51, 54, 61, 67, 76-77), [C-LFI-43] (introduction, dépenses sociales, recettes, tableau d'équilibre), [C-LFI-45], [C-LFI-47] à [C-LFI-53], [C-LFI-24], [C-LFI-27], [C-LFI-39], [C-LFI-40], et les déclarations de la section f marquées axes 1 à 3. Les parties réservées aux étapes 3 à 5 n'ont pas été remplies.

## Axe 1 : Finances publiques et dette

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q2, ligne « bilan d'ensemble » ; déclarations, ligne [C-LFI-83] | Citation | Le candidat présente le document comme l'avant-projet d'une loi de finances rectificative | ... comme « quasiment » l'avant-projet ... | Le billet écrit « se présente quasiment comme l'avant projet » | [C-LFI-83], copie du blog |
| 3 | Q2, ligne « pôle public bancaire » | Mesure déformée | Financement : centralisation « progressivement à 80 % », plafond du livret A à 30 000 €, création d'un « livret B » | Pistes : taux porté « par exemple » à 80 % ; plafond à 30 000 € cité d'après une annonce du président de la CDC ; « livret B » envisagé ; reprise du plafond par Éric Coquerel ajoutée | Le document présente ces trois points comme des exemples ou des pistes, et attribue le chiffre de 30 000 € (et le rendement de 30 à 40 Md€) au président de la CDC | [C-LFI-03], p. 16 ; [C-LFI-84] |
| 4 | Q2, ligne « pôle public bancaire », colonne chiffrage | Chiffrage mal attribué | 100 Md€ la première année, « dont » 18 Md€ « qui reviennent dans la poche de l'État » | 100 Md€ « dans le premier budget », qui produiraient « en plus » 18 Md€ de TVA ; citation rendue à l'orthographe du billet (« l'Etat ») | Les 18 Md€ sont une recette de TVA induite par les 100 Md€ investis, pas une part de ceux-ci ; citation inexacte | [C-LFI-83], copie du blog |
| 5 | Q2, ligne « pôle public bancaire » | Mesure omise | Pas de mention de 2022 | 2022 : pôle public bancaire « acheteur privilégié de la dette publique française » | Mesure de dette du plan Europe de 2022, parmi les mesures unilatérales | [C-LFI-40], p. 29 |
| 6 | Q2, ligne « circuit du Trésor » | Mesure déformée | « les banques, organismes de placement collectif et assureurs sous contrôle de l'État » | « les établissements de crédit, les organismes de placement collectif et les entreprises d'assurance et de réassurance contrôlées par l'État » | Le contrôle de l'État ne vise que les assureurs (8° de l'article 2) ; l'ancienne phrase pouvait se lire comme visant les trois catégories | [C-LFI-45], p. 7-8 |
| 7 | Q2, ligne « audit citoyen » | Citation de plus de 15 mots | Citation de 22 mots | Citation coupée à « la part illégitime », suite en paraphrase avec « réaménagement négocié » | Règle des 15 mots | [C-LFI-13], p. 26 |
| 8 | Q2, ligne « dette sociale » | Citation de plus de 15 mots | Citation de 18 mots | « Retirer la dette Covid des comptes de la Sécurité sociale » et réformer la CADES | Règle des 15 mots | [C-LFI-13], p. 26 |
| 9 | Q2, nouvelle ligne | Mesure omise | Absente | « Dettes privées des petites entreprises et des agriculteurs » : caisse de défaisance (2025) ; reprise des dettes des petites entreprises (2022) | Mesure de la section « annuler la dette publique » de LAEC 2025 et de la rubrique économie locale de 2022, absente du tableau | [C-LFI-13], p. 26 ; [C-LFI-24], p. 7 |
| 10 | Q2, ligne « dépenses nouvelles 2027 » | Page | Planification écologique [p. 11] | [p. 10-11] | Les 700 000 rénovations par an et le plan de rénovation des bâtiments publics sont p. 10 | [C-LFI-03], p. 10-11 |
| 11 | Divergences, cas 2 | Qualification et citation | « Non retenu [...] chaque déclaration du candidat entre dans l'une d'elles. Écart de formulation à décrire en étape 5 » ; citation « congélation ou annulation » | Non retenu comme divergence de corpus ; paragraphe « À instruire à l'étape 5 » : le billet du 15 octobre va plus loin que le document collectif (« abroger la dette française détenue dans les caisses de la BCE », « il s'agit purement et simplement d'un trait à tirer »), alors que le document présente le gel ou l'annulation comme une décision que la BCE « pourrait » prendre, à faire partager par les partenaires ; citation rendue exacte (« congélation ou l'annulation ») | Décision de l'agent principal ; l'ancienne phrase disait que les déclarations restaient dans le cadre du document, ce qui n'est pas exact pour le billet du 15 octobre ; formule citée inexacte | [C-LFI-03], p. 20 ; [C-LFI-79] ; [C-LFI-83] |
| 12 | Q2, ligne « dette détenue par la BCE » | Renvoi | Candidat : « il s'agit purement et simplement d'un trait à tirer » | Ajout de « abroger la dette française détenue dans les caisses de la BCE » et du renvoi « écart avec le document collectif à instruire à l'étape 5 » | Cohérence avec la correction 11 | [C-LFI-83] |
| 13 | Déclarations, lignes [C-LFI-77] et [C-LFI-83] | Citation | la BCE devrait « mettre au congélateur » | il propose que la BCE « mette au congélateur » ; ligne [C-LFI-83] : renvoi à l'étape 5 | Forme rapportée par la fiche du corpus : « mette au congélateur » | [C-LFI-77] ; [C-LFI-83] |

Divergences ajoutées : aucune. Divergences retirées : aucune (aucune n'était retenue). Les quatre cas examinés par la fiche restent « non retenus », motifs conformes à la définition v2. Le cas « annuler » (LAEC 2025) contre « stabiliser » (2027) est bien traité : l'intitulé « annuler la dette publique » recouvre des mesures portant sur la part détenue par la BCE et un « réaménagement négocié », et la stabilisation porte sur le ratio de la dette totale ; objets différents, positions toutes deux compatibles.

### Vérifié sans correction

- Citations de Q1 et Q2 exactes et à la bonne page : [C-LFI-03] p. 4 à 21 (« catastrophe », « pour moitié le déficit actuel », « est un mythe », « Les macronistes et le RN », « nous dépendons trop », « loin d'être un record », « geler ou annuler », « C'est la solution privilégiée que nous mettrons en œuvre. », « stabiliser notre dette par rapport au PIB en un quinquennat », « trajectoire pluriannuelle stabilisant le ratio dette / PIB », « dès l'année 2028 », « un chiffrage complet du programme », « non contraignantes et rémunératrices pour tous les épargnants ») ; [C-LFI-13] p. 8, 25 et 26 ; [C-LFI-22] p. 5, 13, 25 et 26 ; [C-LFI-24] p. 7 et 28 ; [C-LFI-40] p. 14 et 29 ; [C-LFI-41] folios 1 à 3 ; [C-LFI-42] p. 10-11, 61, 67, 76-77 ; [C-LFI-43] introduction et folios 61, 65-66 ; [C-LFI-45] p. 3 à 7 ; [C-LFI-14] p. 6 ; [C-LFI-79] ; [C-LFI-83] (« 25 milliards seraient consacrés à la diminution de la dette », « symbolique », « pas imposition, pas taxation », 166 Md€ d'aides, critique de la « règle d'or »).
- Q2 du contre-budget 2027 : les 14 lignes de recettes chiffrées et les quatre blocs de dépenses figurent tous au tableau ; aucune mesure chiffrée de l'axe n'est omise. Les mesures non chiffrées du document (Smic à 1 700 € net, blocage du prix du carburant, exonérations au-dessus de 2 Smic) relèvent de l'axe 4 ou sont déjà notées.
- Absence de cible de déficit en pourcentage du PIB dans [C-LFI-03] : confirmée (5 % seulement chez LCP, [C-LFI-84]).
- Locuteurs : distinction parti, groupe, candidat, texte commun et programme 2022 conforme à `00-perimetre.md` ; [C-LFI-46] bien écarté de l'axe (loi agricole dite Duplomb).
- Vocabulaire : aucun mot de jugement hors citation attribuée.

### Non vérifiable

- [C-LFI-77], [C-LFI-78], [C-LFI-80], [C-LFI-84] : relais de presse non archivés en texte ; contenu repris des fiches du corpus. La phrase « Les aides sont le déficit et le déficit, c'est la dette » vient du relais Public Sénat de [C-LFI-83] ; le billet archivé porte une formule voisine (« les aides sans contreparties ont fait le déficit »).
- [C-LFI-68] : la fiche du corpus ne contient que le résumé de l'intervention ; « 3 points de PIB » et le décompte de la motion (269 voix, 288 requises) n'ont pas été relus dans le compte rendu.
- [C-LFI-43] : copie texte en colonnes entrelacées ; les folios cités (« vers le folio 14, 16, 60 ») restent approximatifs, comme la fiche le signale.

### Appréciation avant correction

Chiffres du contre-budget 2027 exacts et complets, citations du document collectif fidèles. Corrections surtout de précision : des pistes du document présentées comme des mesures arrêtées (épargne), une recette induite de 18 Md€ présentée comme une part des 100 Md€, deux citations trop longues, une mesure de dette omise, et l'écart du candidat sur la dette BCE présenté comme couvert par le document alors qu'il va plus loin.

## Axe 2 : Travail, protection sociale et fraude

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q1, PPL n° 438 | Citation inexacte | relèverait de « l'insincérité budgétaire » | serait une « preuve d'insincérité budgétaire » | Le texte écrit « il fait, une nouvelle fois, preuve d'insincérité budgétaire » | [C-LFI-47], p. 5 |
| 3 | Q2, retraites, contre-budget 2025 | Citation de plus de 15 mots | Citation de 17 mots | Abroger la réforme et « repasser l'âge de la retraite à 60 ans avec 40 annuités » | Règle des 15 mots | [C-LFI-42], p. 16, 54 |
| 4 | Q2, retraite à 60 ans (2022) | Citation de plus de 15 mots | Citation de 17 mots | Citation arrêtée à « 40 annuités » | Règle des 15 mots | [C-LFI-24], p. 10 |
| 5 | Q2, pension minimale | Attribution | « 2024 : minimum contributif [...] parmi les mesures des 15 premiers jours [C-LFI-22, p. 4 ; C-LFI-42, p. 40] » | Texte commun 2024 [C-LFI-22, p. 4] et contre-budget 2025 du groupe [C-LFI-42, p. 40] séparés | Le contre-budget n'est pas un texte des « 15 premiers jours » ; deux locuteurs fondus en un | [C-LFI-22], p. 4 ; [C-LFI-42], p. 40 |
| 6 | Q2, assurance chômage | Mesure omise | Présomption de démission seule | Ajout : abroger la fin des allocations pour les intérimaires et les CDD qui refusent un CDI | Même puce de la liste de LAEC 2025 | [C-LFI-13], p. 35 |
| 7 | Q2, garantie d'autonomie | Citations de plus de 15 mots | Deux citations de 18 mots | Citations arrêtées à « seuil de pauvreté », montants (1 337 € et 1 216 €) en paraphrase | Règle des 15 mots | [C-LFI-03], p. 8 ; [C-LFI-13], p. 29 |
| 8 | Q2, garantie d'emploi | Citation de plus de 15 mots | Citation de 20 mots | « d'être embauché au moins au SMIC revalorisé », reste en paraphrase | Règle des 15 mots | [C-LFI-13], p. 33 |
| 9 | Q2, santé au travail | Mesure omise | Pas de texte commun | NFP 2024 : plan d'action « zéro mort au travail » (CHSCT, inspecteurs et médecins du travail, burn-out) | Mesure du texte commun sur l'axe, absente | [C-LFI-22], p. 19 |
| 10 | Q2, nouvelle ligne | Mesure omise | Absente | « Contrats précaires et droit du travail » : quota maximal de contrats précaires (mesure clé de LAEC 2025, 10 % et 5 %), abrogation des ordonnances Pénicaud et de la loi El Khomri, « principe de faveur », présomption de salariat ; mêmes mesures en 2024 et 2022 | Mesure clé du chapitre travail de LAEC 2025, absente du tableau | [C-LFI-13], p. 33-34 ; [C-LFI-22], p. 19 ; [C-LFI-24], p. 9 |
| 11 | Q2, gouvernance de la Sécurité sociale | Citation de plus de 15 mots | Citation de 21 mots | Citation arrêtée à « par les assurés eux-mêmes », suite en paraphrase | Règle des 15 mots | [C-LFI-13], p. 12 |
| 12 | Q2, nouvelle ligne | Mesure omise | Absente | « Non-recours et contrôle des allocataires » : lutte contre le non-recours, automatisation des prestations, « Interdire les pratiques de notation des allocataires » (2025) ; versement automatique contre le non-recours (2022) | Seule position du programme du parti sur le contrôle des allocataires ; l'axe couvre la fraude sociale | [C-LFI-13], p. 29 ; [C-LFI-39], p. 19 |
| 13 | Divergences, cas 1 | Qualification | « L'objectif [...] est le même dans tous les documents [...] C'est une évolution de calendrier, à décrire en étape 5 » | « Non retenu : évolution de calendrier vers le même objectif, pas une divergence », avec les deux références (60 ans en mesure clé de LAEC 2025 ; 62 ans dès 2027, 60 ans « objectif sur un mandat ») et renvoi à l'étape 5 ; « tous les documents » limité aux programmes et contre-budgets | Décision de l'agent principal ; la PPL n° 438 ne fixe pas l'objectif de 60 ans | [C-LFI-13], p. 37 ; [C-LFI-03], p. 11 ; [C-LFI-43] ; [C-LFI-47] |
| 14 | Convergences | Citation inexacte | le programme « réaffirme l'objectif commun du droit à la retraite à 60 ans » | veut « Réaffirmer l'objectif commun du droit à la retraite à 60 ans » | Forme verbale du texte | [C-LFI-22], p. 16 |

Divergences ajoutées : aucune. Divergences retirées : aucune. Les cas 2 (durée de cotisation), 3 (RSA et garantie d'autonomie) et 4 (montant de la fraude sociale) restent « non retenus », motifs conformes à la définition v2 (étape intermédiaire, deux instruments, écart de chiffre sans position contraire).

### Vérifié sans correction

- Citations exactes à la bonne page : [C-LFI-03] p. 8, 11 et 12 ; [C-LFI-13] p. 29, 33, 35, 36, 37, 55-56 ; [C-LFI-22] p. 4, 9, 16, 19 ; [C-LFI-24] p. 9-10 ; [C-LFI-37] p. 19 ; [C-LFI-39] p. 10, 18-19 ; [C-LFI-42] p. 16-18, 40 ; [C-LFI-43] (« un retour à la retraite à 62 ans puis à 60 ans avec 40 annuités », tableau à 10,3 Md€ et note de montée en charge, élections à la Sécurité sociale, 1 600 € net, franchises 1,5 Md€) ; [C-LFI-47] p. 3 à 7 et 12 à 14 ; [C-LFI-48] p. 3, 5-6 ; [C-LFI-49] p. 1 à 3 ; [C-LFI-53] p. 16 ; [C-LFI-71], [C-LFI-72], [C-LFI-81] (14, 15, 16 et 25 jours, « record d'Europe des morts au travail », « d'ordre public »).
- Q2 du contre-budget 2027 : les quatre lignes de l'axe (retraites 9 Md€, assurance chômage 3 Md€, indexation 8 Md€, garantie d'autonomie 9,5 Md€) et la pension minimale au Smic sont présentes.
- Garantie d'autonomie de 2022 : remplacement du RSA « à l'horizon 2023 » et versement sans contrepartie conformes au plan pauvreté.
- Locuteurs : parti, groupe, candidat, texte commun et programme 2022 bien séparés ; la position du candidat au débat du Medef est bien signalée comme rapportée par Moneyvox seul.

### Non vérifiable

- [C-LFI-78] (62 ans « dans un premier temps », 60 ans « le plus vite possible ») et la partie Public Sénat de [C-LFI-83] (retour à 62 ans pour 9 Md€ annoncé en conférence) : relais non archivés en texte.
- Durée de cotisation fixée par l'article 1er de la PPL n° 438 : le texte modifie le 2° et abroge les 3° à 6° de l'article L. 161-17-3 du code de la sécurité sociale ; la durée qui en résulte suppose le texte consolidé du code, hors corpus (à faire en étape 3, comme la fiche le prévoit).

### Appréciation avant correction

Fiche fidèle sur les retraites et la fraude, chiffres exacts. Cinq citations dépassaient 15 mots, deux formules étaient inexactes, un locuteur était fondu dans un autre. Trois mesures principales du chapitre travail de LAEC 2025 (contrats précaires, droit du travail, contrôle des allocataires) manquaient au tableau.

## Axe 3 : Immigration, intégration, droits sociaux des étrangers

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q3, Q4, Q5 | Forme | Pas de ligne de verdict | « **Verdict Faisabilité / Cohérence / Écoute : (étape 3 à 5).** » | Gabarit `_gabarit/axes/fiche-axe.md` ; alignement sur les fiches 1 et 2 | |
| 3 | Q2, nationalité et droit du sol | Citation de plus de 15 mots | Citation de 16 mots (2022) | Deux citations : « Rétablir le droit du sol pour les enfants nés en France », « sous réserve de leur consentement » | Règle des 15 mots | [C-LFI-27], p. 19 |
| 4 | Q2, nationalité et droit du sol | Citation de plus de 15 mots | Phrase de la PPLC citée en entier (16 mots) | la loi « garantit l'accès à la nationalité française » à tout enfant né sur le sol français | Règle des 15 mots | [C-LFI-50], p. 8 |
| 5 | Q2, sauvetage en mer | Mesure déformée | « suspension des traités du Touquet et de Sandhurst (renvoyée à la commission des affaires européennes) » | « invitation au gouvernement à suspendre les traités [...] ; PPRE renvoyée à la commission des affaires européennes » | Le point 5 de la résolution « invite » le gouvernement ; le renvoi en commission concerne la PPRE entière | [C-LFI-52], p. 1, 9 |
| 6 | Q2, causes des départs et codéveloppement | Mesure omise | Absente | 2025 : « S'opposer aux accords commerciaux inégaux » pour éviter aux migrants de devoir fuir leur pays | Puce de la section migrations de LAEC 2025 | [C-LFI-13], p. 62 |
| 7 | Convergences | Attribution | « dont ceux du Royaume-Uni et de l'Italie, nommés » | « nomme le Premier ministre britannique et la présidente du Conseil italien » | Le communiqué nomme deux dirigeants, pas des gouvernements | [C-LFI-74] |
| 8 | Déclarations, ligne [C-LFI-69] | Vocabulaire | qualifie l'offensive de raciste et islamophobe | « raciste » et « islamophobe » entre guillemets | Mots du locuteur hors guillemets (biais 13) | [C-LFI-69] |

Divergences ajoutées : aucune. Divergences retirées : aucune. Les sept rapprochements « non retenus » (droit du sol, droit de vote, droit de travailler des demandeurs d'asile, lois visées, régularisations, sauvetage en mer, Frontex) sont conformes à la définition v2 : silence, précision successive ou deux instruments pour un même but. Le cas du consentement au droit du sol est bien renvoyé à l'étape 5.

### Vérifié sans correction

- Citations exactes à la bonne page : [C-LFI-13] p. 6, 23, 32, 40, 62 ; [C-LFI-15] p. 4 ; [C-LFI-22] p. 17 et 24 ; [C-LFI-24] p. 25 ; [C-LFI-27] p. 2, 5, 6, 8, 13 à 19 ; [C-LFI-42] p. 51 et 61 ; [C-LFI-43] (« hostilité des politiques migratoires », 80 M€) ; [C-LFI-50] p. 4 à 8 ; [C-LFI-51] p. 4 à 6 ; [C-LFI-52] p. 3 à 9 ; [C-LFI-74].
- Absence de ligne sur l'immigration, l'asile ou l'AME dans [C-LFI-03] : confirmée par recherche des termes (aucune occurrence).
- Chiffrage : 18, 80 et 100 M€ (2025), 80 M€ (2026) ; somme de 198 M€ refaite.
- Locuteurs : [C-LFI-75] bien signalé comme relais unique traduit ; textes du groupe et programme 2022 bien séparés.

### Non vérifiable

- [C-LFI-75] : relais unique en anglais, date déduite, traduction par nos soins.
- [C-LFI-68] : critique de l'article qui renchérit les titres de séjour, reprise de la fiche du corpus sans relecture du compte rendu.

### Appréciation avant correction

Extraction complète et prudente, vocabulaire déjà neutralisé par crochets. Deux citations à 16 mots, une mesure de la PPRE mal rendue, une mesure de LAEC 2025 omise, une attribution approximative, deux lignes de verdict manquantes.

## Bilan

| Axe | Citation (inexacte ou trop longue) | Mesure déformée | Mesure omise | Chiffrage mal attribué | Divergence (qualification) | Vocabulaire | Attribution, page, forme | Total |
|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 2 | 2 | 1 | 1 | 0 | 3 | 13 |
| 2 | 7 | 0 | 4 | 0 | 1 | 0 | 2 | 14 |
| 3 | 2 | 1 | 1 | 0 | 0 | 1 | 3 | 8 |

Aucune divergence ajoutée ni retirée. Les écarts listés dans la section « Trous » du corpus ont été relus pour les trois axes : dette (« annuler » contre « stabiliser » et « congeler ») et retraites (60 puis 62 ans) restent hors divergence, avec les motifs écrits dans les fiches ; l'écart du candidat sur la dette détenue par la BCE est désormais présenté comme un écart discours / programme à instruire à l'étape 5.

## Questions pour l'agent principal

1. **Smic et ISF.** Les écarts de la section « Trous » sur le Smic (1 400, 1 600, 1 700 € net, 2 176 € brut) et sur l'ISF (15 puis 10 Md€) relèvent de l'axe 4 ; ils n'ont pas été instruits ici. La fiche 1 garde l'ISF et la taxe Zucman en « écarts de chiffrage », ce qui est conforme.
2. **Mayotte dans le contre-budget 2025.** Le document chiffre deux fois 100 M€ pour Mayotte : « Étendre le RSA et le SMIC à Mayotte » [C-LFI-42, p. 17, 54] et un ensemble AME, RSA, Smic et scolarisation [C-LFI-42, p. 51, 61], les deux comptés dans le total des dépenses. Les fiches 2 et 3 citent chacune l'une des deux lignes. Double compte possible dans le document lui-même : à instruire en étape 4 ?
3. **Sauvetage en mer en 2026.** Le contre-budget 2026 porte « Augmenter les moyens publics de sauvetage en mer » dans sa section maritime, sans lien écrit avec les migrations [C-LFI-43] ; non ajouté à la fiche 3. À ajouter, ou à laisser hors axe ?
4. **Forme du tableau des déclarations.** La fiche 3 n'a pas de colonne « Locuteur » (le locuteur figure dans la paraphrase), contrairement aux fiches 1 et 2. Harmonisation laissée à la décision de l'agent principal.

Typographie : `python3 _scripts/lint-texte.py` sans tiret long sur les trois fiches et sur ce rapport.
