# PS · Contrôle de fidélité, étape 2, axes 1 à 3

- Rédigé le : 2026-10-27
- Données arrêtées au : 2026-10-27
- Auteur : sous-agent Opus (contrôle étape 2)
- Statut : revu (étape 2)
- Version du socle : v2.2
- Fiches contrôlées : `../axes/1-finances-publiques.md`, `../axes/2-travail-protection-sociale.md`, `../axes/3-immigration.md`

Sigles : PS (Parti socialiste), SOC (groupe « Socialistes et apparentés »), NFP (Nouveau Front populaire), PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PPRE (proposition de résolution européenne), PLF (projet de loi de finances), PLFSS (projet de loi de financement de la sécurité sociale), RSA (revenu de solidarité active), ISF (impôt de solidarité sur la fortune), OQTF (obligation de quitter le territoire français), AES (admission exceptionnelle au séjour), CESEDA (code de l'entrée et du séjour des étrangers et du droit d'asile), Md€ (milliard d'euros).

Méthode. Couche texte de chaque PDF du corpus extraite avec `pdftotext`, page par page (une page du fichier par saut de page) et en mise en page conservée ; copies texte (Projet socialiste [C-PS-01] en six parties, contre-budget 2027 [C-PS-33], note du NFP [C-PS-26], communiqués [C-PS-11], [C-PS-27], [C-PS-28], [C-PS-29], [C-PS-32], [C-PS-38], fiches de déclarations [C-PS-72] à [C-PS-89]) lues directement. Chaque passage entre guillemets des trois fiches a été recherché par script (`python3 -I`, hors dépôt) dans le texte du document cité, avec la page où il apparaît ; les citations non trouvées ont été relues à la main. Pour [C-PS-01], un second script a rattaché chaque citation à sa partie, son chapitre et son intertitre. La profession de foi de 2012 [C-PS-70] (PDF image, sans couche texte) a été rendue en images et relue quart de page par quart de page : les citations des trois fiches sont conformes, et le document ne mentionne pas l'immigration. Sommes refaites en code : contre-budget 2027, 10 + 1 + 22 = 33 Md€, 39,5 - 11 = 28,5, 28,5 + 17,5 - 22 = 24 Md€, postes de dépenses chiffrés 20 Md€ ; propositions de 2025, 26,9 + 14 - 19,2 = 21,7 Md€ et volet PLFSS 7,5 + 4,6 = 12,1 Md€, déficit 24 - 12,1 + 1,7 = 13,6 Md€ ; note du NFP, 49 Md€ ; programme 2022, 50 et 50 Md€ : toutes conformes aux fiches. Documents parcourus pour les mesures omises : [C-PS-01] (six parties, recherche par termes de chaque axe puis lecture des sections pertinentes, chapitre 17 lu en entier), [C-PS-33] en entier, [C-PS-22] p. 4, 9, 13, 16, 17, 24, 25, [C-PS-16] p. 40 à 53, 82 à 85, [C-PS-41] à [C-PS-47] en entier. Pas de recherche web. Les parties réservées aux étapes 3 à 5 étaient vides et le restent.

## Axe 1 : Finances publiques et dette

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q2, ligne « Lutte contre la fraude 2027 » ; divergences, cas 1 | Citation inexacte | le tableau regroupe « économies et lutte contre la fraude » | le tableau regroupe les « mesures d'économies et de lutte contre la fraude » | Intitulé exact du tableau : « Total des mesures d'économies et de lutte contre la fraude » | [C-PS-33], tableau de chiffrage |
| 3 | Q1, programme 2022 | Vocabulaire | Le retour de l'austérité budgétaire « risquerait » | Le « retour de l'austérité budgétaire » risquerait | Le mot « austérité » est celui du document : il passe entre guillemets | [C-PS-24], p. 41 |
| 4 | Q2, ligne « Programme budgété de 2022 » | Page | p. 41-43 | p. 40-43 | « Un programme budgété et financé » est p. 40 | [C-PS-24], p. 40 |
| 5 | Engagements 2012, chiffrage du projet | Mesure déformée | effectif des fonctionnaires de l'État stable | « le nombre total des fonctionnaires de l'État n'augmentera pas » | « Stable » exclut une baisse que le texte n'exclut pas | [C-PS-69], p. 22 |
| 6 | Engagements 2012, profession de foi ; limites | Lecture OCR | « lecture par reconnaissance de caractères » ; « à relire sur l'image » | Texte relu sur l'image, conforme | Vérification demandée par l'agent principal | [C-PS-70], p. 2 |

Divergences ajoutées : aucune. Divergences retirées : aucune (aucune n'était retenue). Arbitrages vérifiés sur pièces :
- **12,1 contre 17,5 Md€** : confirmé, écart de périmètre et d'arrondi dans le même document (texte de la priorité 07 : 12,1 + 5,5 ; tableau : 17,5) [C-PS-33]. Étape 4.
- **ISF du NFP absent du projet** : confirmé. ISF « renforcé avec un volet climatique » [C-PS-22, p. 13], 15 Md€ [C-PS-26, folio 3], rétablissement annoncé par le groupe [C-PS-11] ; le projet retient taxe Zucman et impôt sur les grandes successions, sans ISF [C-PS-01, Refaire société, ch. 16]. Silence et instrument différent ; abandon non dit à l'étape 5.

### Vérifié sans correction

- Citations de Q1 et Q2 exactes et à la bonne page ou section : [C-PS-01] (ch. 3, 4, 6, 16, 18 ; intertitres vérifiés), [C-PS-08] p. 3, 4, 5, 9, [C-PS-16] p. 84-85, [C-PS-22] p. 5, 13, 25, 26, [C-PS-24] p. 41-42, [C-PS-26] folios 1 à 4 et 10, [C-PS-28], [C-PS-29], [C-PS-30] p. 1 à 3, [C-PS-32], [C-PS-37] p. 6, [C-PS-48] p. 4 à 6, [C-PS-69] p. 7, 8, 10, 22, déclarations [C-PS-72], [C-PS-77], [C-PS-79], [C-PS-82] à [C-PS-85], [C-PS-88], [C-PS-89].
- Contre-budget 2027 : toutes les lignes chiffrées figurent au tableau des mesures (recettes, économies, fraude, dépenses, effort net). Les mesures non chiffrées sur le crédit d'impôt recherche et le taux réduit d'impôt sur les sociétés relèvent de l'axe 4.
- Absence de cible de déficit en pourcentage du PIB dans [C-PS-33] et [C-PS-01] : confirmée.
- Couches : parti, groupe, texte commun, candidat, programme antérieur et mandat exercé conformes à `00-perimetre.md`.

### Non vérifiable

- Ventilation des 39,5 Md€ (15, 10, 10, 4) et classement de la fraude fiscale dans les 12,1 Md€ : connus par le relais LCP seulement [C-PS-82].
- [C-PS-29] : le document des propositions de Blois n'est pas au corpus ; ses chiffres viennent de [C-PS-30] et de LCP.

### Appréciation avant correction

Fiche fidèle et complète. Chiffres exacts. Corrections de forme : un intitulé de tableau mal cité, une page, un mot du document à mettre entre guillemets, une formule de 2012 resserrée.

## Axe 2 : Travail, protection sociale et fraude

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q2, ligne « Recettes sociales des propositions de 2025 » | Mesure déformée | Quatre mesures présentées comme des recettes | Ligne renommée « Mesures sociales » ; recettes (allégements, heures supplémentaires) et maîtrise des dépenses (cumul emploi-retraite, ruptures conventionnelles) distinguées ; déduction « forfaitaire », entreprises de moins de 250 salariés | Le cumul emploi-retraite (0,5 Md€) et le plafonnement des indemnités de rupture (1 Md€) figurent dans le bloc « maîtriser les dépenses » | [C-PS-30], p. 2-3 |
| 3 | Divergences, cas 6 | Citation inexacte | « inconditionnalité et automaticité » | « l'inconditionnalité et l'automaticité » | Texte du projet | [C-PS-01], Refaire société, ch. 16 |
| 4 | Divergences, cas 1 | Mesure déformée | « Le texte commun associe lui-même un retour immédiat aux 62 ans » | Abrogation immédiate des décrets de la réforme des 64 ans, citée ; le texte ne cite pas 62 ans, le retour à l'âge antérieur se déduit | Le programme du NFP n'écrit pas « 62 ans » | [C-PS-22], p. 4 et 16 |
| 5 | Convention de pagination ; engagements 2012 | Lecture OCR | « reconnaissance de caractères par nos soins » ; mention de la coquille « entin » | Texte relu sur l'image, conforme ; mention de la coquille retirée | Vérification demandée | [C-PS-70], p. 1 et 2 |
| 6 | Limites | Mise à jour | La fiche du corpus de [C-PS-53] dit l'inverse du document | La fiche du corpus a été corrigée au contrôle de l'étape 2 | Constat dans `01-corpus.md` (correction de l'autre agent de contrôle) | [C-PS-53], p. 2 |

Divergences ajoutées : aucune. Divergences retirées : aucune. Arbitrage vérifié sur pièces :
- **62 ans du projet contre objectif de 60 ans du NFP** : confirmé comme non-divergence. Projet : âge « ramené à 62 ans » qui « continuera de jouer un rôle de protection minimale » [C-PS-01, Vivre libres, ch. 1] ; NFP : abrogation immédiate des décrets de la réforme des 64 ans [C-PS-22, p. 4] et « objectif commun du droit à la retraite à 60 ans » sans échéance [C-PS-22, p. 16]. Nuance : le « 62 ans immédiat » du NFP est une déduction, pas un mot du texte (correction 4). Étape 5.

### Vérifié sans correction

- Citations exactes et à la bonne place : [C-PS-01] (Vivre libres ch. 1, intertitres « Redonner du sens et de la valeur au travail », « Avoir du temps libre », « Pouvoir profiter de sa retraite » ; Refaire société ch. 16 ; Être en sécurité(s) ch. 6 et 8 ; S'épanouir à égalité ch. 11 et 12), [C-PS-08] p. 12-13, [C-PS-11], [C-PS-16] p. 40, 42, 43, 53, [C-PS-22] p. 4, 9, 16, 19, [C-PS-24] p. 9, 24, 26, 42, [C-PS-25] p. 3, [C-PS-28], [C-PS-30] p. 2, [C-PS-32], [C-PS-38], [C-PS-39] p. 2, 3, 5, 6, [C-PS-40] p. 3, 4, 6, 7, [C-PS-48] p. 4, [C-PS-53] p. 1-2, [C-PS-69] p. 10, 11, 14, 22, déclarations [C-PS-72], [C-PS-76], [C-PS-78], [C-PS-80], [C-PS-82], [C-PS-88].
- Aucune mesure principale omise dans [C-PS-01] sur le travail, les retraites, le chômage, la pauvreté et l'autonomie. Le projet ne traite pas de fraude sociale (recherche « fraude » : fraude fiscale seulement), comme la fiche le dit.
- Cas 2 à 9 des divergences : qualifications conformes à la définition v2.

### Non vérifiable

- Version d'avril 2026 du projet (« le critère central ») : connue par LCP, hors corpus.
- [C-PS-78] (livre du candidat) et [C-PS-80] : relais de presse ; contenu repris des fiches du corpus.

### Appréciation avant correction

Fiche fidèle. Une ligne mêlait recettes et économies du volet social de 2025 ; une inférence sur le texte du NFP était présentée comme un mot du texte.

## Axe 3 : Immigration, intégration, droits sociaux des étrangers

### Corrections

| N° | Section | Type | Avant | Après | Motif | Référence |
|---|---|---|---|---|---|---|
| 1 | En-tête | Forme | « Auteur : sous-agent Opus, étape 2 » ; « Statut : brouillon » | Relecture ajoutée ; « brouillon, contrôlé (étape 2) » | Consigne de contrôle | |
| 2 | Q1, groupe, PPL n° 3253 | Forme | « n'aurait trouvé ni « appel d'air », mais » | « celle-ci n'aurait pas provoqué « d'appel d'air », mais » | Phrase incorrecte ; citation rendue à la forme du texte | [C-PS-41], p. 2 |
| 3 | Q1, groupe, PPL n° 3266 | Mesure déformée | Quatre causes : pouvoir discrétionnaire, crainte d'une OQTF, absence de circuit dédié, liste régionale instable | Discrétionnaire (avec la crainte d'une OQTF), lien circulaire entre séjour et travail, absence de circuit dédié et préfectures difficiles d'accès, liste régionale et annuelle | La deuxième cause du texte (« appréhension circulaire » entre immigration et travail) manquait ; la crainte d'une OQTF fait partie de la première | [C-PS-42], p. 2-4 |
| 4 | Q1, groupe, PPRE n° 2508 | Mesure déformée | pacte « en vigueur en juillet 2026 » | entrée en vigueur « prévue » en juillet 2026 selon le texte | Le texte (février 2026) parle d'une entrée en vigueur prévue | [C-PS-47], p. 7 |
| 5 | Q2, PPL n° 3266 | Citation inexacte | métiers « essentiels pour la continuité de la vie de la Nation » | métiers situés dans un « secteur essentiel pour la continuité de la vie de la Nation » | Formule exacte du texte | [C-PS-42], p. 6, 8, 9 |
| 6 | Q2, PPL n° 3259 | Mesure déformée | « résidents depuis 13 ans au plus » ; huit catégories décrites pour neuf annoncées | Arrivés en France à treize ans au plus ; les neuf catégories du texte, dont les résidents réguliers depuis plus de dix ans mariés à un étranger arrivé enfant (7°) | Lecture fautive du 2° et omission du 7° | [C-PS-43], p. 4-5 |
| 7 | Q2, voies légales | Mesure omise | Ligne « Candidat » seule | Ajout du texte commun : « Créer des voies légales et sécurisées d'immigration » | Mesure du programme du NFP sur la même page que les autres mesures reprises | [C-PS-22], p. 24 |
| 8 | Q2, renouvellement des titres | Source | Possibilité d'opposition attribuée au seul dossier de presse | L'exposé des motifs de la PPL le dit déjà (raisons juridiques, à démontrer par l'administration) ; le dossier de presse cite les motifs | Le texte déposé contient la réserve | [C-PS-44], p. 3 ; [C-PS-35], p. 13 |
| 9 | Q2 et déclarations, lignes Olivier Faure | Vocabulaire | « Régularisation massive » (intitulé et paraphrase, hors guillemets) | « Régularisation d'environ 400 000 travailleurs » ; « Régularisation des travailleurs sans papiers » | Adjectif non cité, repris d'un relais | [C-PS-80] ; [C-PS-81] |
| 10 | Divergences | Classement (arbitrage) | Titre de séjour de référence « non retenu », « à trancher par l'agent principal », avec « carte de résident de dix ans » | Cas 4 de la section des écarts : pas de divergence du parti ; écart entre texte commun et candidat, « à instruire à l'étape 5 (cohérence parti / candidat) » ; « carte de séjour de dix ans » | Décision de l'agent principal ; le texte commun écrit « carte de séjour de dix ans » | [C-PS-22], p. 24 ; [C-PS-16], p. 82 ; [C-PS-01], ch. 17 |
| 11 | Convergences | Section à laisser à la synthèse | Renvoi à la fiche LFI de l'axe | Renvoi retiré ; co-signature du texte commun conservée | La comparaison entre forces relève de la synthèse | [C-PS-22] |
| 12 | Pagination, sources | Lecture OCR | « lu par reconnaissance de caractères » | Relu sur l'image : aucune mention de l'immigration, confirmé | Vérification demandée | [C-PS-70] |

Divergences ajoutées : aucune. Divergences retirées : aucune. Arbitrages vérifiés sur pièces :
- **400 000 (Olivier Faure, primaire) contre PPL n° 3253** : confirmé, écart de chiffrage (300 000 contre « autour de 400 000 »), même règle [C-PS-41, p. 2-3] ; [C-PS-81]. Étape 4.
- **6 mois de contrat (projet) contre 6 mois d'activité sur 24 (PPL)** : confirmé, précision successive ; le critère de la PPL englobe celui du projet [C-PS-01, ch. 17] ; [C-PS-41, p. 3-4].
- **« Contrôle » et convention citoyenne du candidat contre la PPL** : confirmé, silence et méthodes différentes [C-PS-73] ; [C-PS-78] ; [C-PS-16, p. 82]. Étape 5.
- **Titre de séjour de référence** : références vérifiées, rédaction alignée sur la décision (correction 10).

### Vérifié sans correction

- Chapitre 17 du projet relu en entier : toutes les mesures des sections « politique migratoire » et « droit d'asile » sont au tableau (sauf détails mineurs : inclusion des travailleurs étrangers dans les missions des entreprises, reconnaissance mutuelle des décisions d'asile, asile des personnes LGBTQIA+ venues de pays dits sûrs).
- Citations exactes : [C-PS-01] ch. 17 et 18, Être en sécurité(s) introduction, [C-PS-08] p. 5, [C-PS-16] p. 43, 47, 82, [C-PS-19] p. 9, [C-PS-22] p. 17, 24, 25, [C-PS-24] p. 16, 38, [C-PS-35] p. 12, [C-PS-41] à [C-PS-45], [C-PS-47] p. 2-11, [C-PS-69] p. 10, 15, 18, déclarations [C-PS-73], [C-PS-78], [C-PS-80], [C-PS-81], [C-PS-85].
- Statuts « adoptée en première lecture » des PPL n° 1799 et n° 2021 : conformes à `01-corpus.md`.

### Non vérifiable

- [C-PS-46] (PPLC n° 3348 sur l'aide médicale de l'État) : texte non publié, lien seul.
- [C-PS-73], [C-PS-78], [C-PS-80], [C-PS-81], [C-PS-85] : relais de presse, contenu repris des fiches du corpus.

### Appréciation avant correction

Fiche très complète. Les erreurs portent sur le détail des PPL (catégories protégées contre les OQTF, causes de l'échec de l'AES, formule des métiers essentiels) et sur un adjectif repris d'un relais.

## Bilan

| Axe | Lignes vérifiées (Q1, Q2, 2012, divergences, déclarations) | Corrections | Dont fond (mesure, citation, omission, vocabulaire) |
|---|---|---|---|
| 1 | 16 + 22 + 6 + 5 + 9 | 6 | 3 |
| 2 | 17 + 22 + 7 + 9 + 8 | 6 | 3 |
| 3 | 23 + 26 + 3 + 10 + 5 | 12 | 8 |

Aucune divergence v2 retenue sur les trois axes, après vérification ; aucune créée. Tous les arbitrages de l'agent principal sont confirmés sur pièces. Aucun tiret long. Aucun passage en anglais.

## Questions pour l'agent principal

1. Axe 2 : le classement du cas 62 ans contre 60 ans repose sur l'idée que le NFP « combine 62 ans immédiat et 60 ans comme objectif ». Le texte n'écrit pas « 62 ans » : il abroge les décrets de la réforme des 64 ans. La qualification ne change pas, mais la rédaction de l'étape 5 devra le dire ainsi.
2. Les tableaux de mesures dépassent la cible de 10 à 20 lignes du brief (22, 22 et 26 lignes). Rien n'a été retiré : aucune ligne n'est redondante. À trancher si la symétrie de volume avec les autres verticales l'exige.
3. Profession de foi de 2012 [C-PS-70] : elle mentionne aussi « l'impôt sur la fortune sera rétabli », qui n'est cité dans aucune des trois fiches. Matière pour l'axe 4 (et le cas ISF de l'axe 1 à l'étape 5).

## Erreurs repérées dans `01-corpus.md`

Aucune nouvelle. La fiche de [C-PS-53] (prime carburant), signalée par le rédacteur de l'axe 2, est déjà corrigée dans `01-corpus.md`.
