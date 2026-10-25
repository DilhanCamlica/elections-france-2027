# Briefing : série « Vérification d'affirmations » (travail antérieur)

- Rédigé par : l'agent de la session précédente, transmis le 2026-10-25
- Rôle dans le projet : décrit la méthode, le format validé et les conclusions acquises des deux pages déjà publiées. Le présent projet en hérite (hiérarchie des sources, confusions à démêler, format visuel, garde-fous) et les étend aux programmes des partis.
- Les deux pages ont été relues dans leur version publiée le 2026-10-25 : « Qui paie pour qui ? » compte 41 sources (et non 40), « Immigration : vrai ou faux ? » en compte 38.

## 0. La mission en une phrase

Prendre une affirmation politique ou sociale qui circule, la découper en sous-affirmations, la vérifier avec des données publiques sourcées, puis publier une page de vérification visuelle et neutre, partagée directement avec les personnes qui tiennent ces affirmations. L'objectif n'est pas de « debunker » ni d'armer un camp. C'est d'établir ce qui est vrai, ce qui est faux, et dans quelle proportion, y compris quand l'affirmation contient une part de vérité.

## 1. Historique

| Étape | Contenu | Résultat |
|---|---|---|
| 1 | « trop de profiteurs (chômeurs, malades longue durée), l'État n'a plus d'argent » | Article long, puis artifact v1 |
| 2 | Reformulation : « trop de profiteurs et de fainéants, le reste paie pour eux » | Artifact v1 « Qui paie pour qui ? » (format « argumentaire », rejeté) |
| 3 | « les immigrés arrivent massivement, ne s'intègrent pas, et ont plus de droits sociaux que les Français dans le besoin » | Article long |
| 4 | Complément : comment les Français s'intègrent-ils à l'étranger ? | Section « miroir », avec ses limites |
| 5 | Artifact « Immigration : vrai ou faux ? » dans un nouveau format | Format validé par Dilhan |
| 6 | Refonte de « Qui paie pour qui ? » dans ce format | v2, même URL |

## 2. Pages existantes

| Titre | URL | Affirmation traitée | Statut |
|---|---|---|---|
| Qui paie pour qui ? | https://claude.ai/artifact/95kD4VLYrjVh3kH9rZXxfc | « Il y a trop de profiteurs et de fainéants en France, et le reste de la population paie pour eux » | v2, format validé, partagée |
| Immigration : vrai ou faux ? | https://claude.ai/artifact/V1w68c2LjyuVbLEgFnuan4 | « Les immigrés continuent à arriver massivement en France, ne s'intègrent pas, et ont plus de droits sociaux que des Français qui sont dans le besoin » | v1, format validé, partagée |

Leur code HTML est le gabarit visuel de la série. La version publiée fait foi.

## 3. Méthode de recherche

### 3.1 Principes

1. Découper l'affirmation en 2 ou 3 sous-affirmations vérifiables séparément.
2. Chercher avant d'affirmer : tout chiffre décrivant le monde actuel est vérifié par recherche web. Fin 2026 : les données 2025 et les budgets 2027 existent.
3. Hiérarchie des sources : statistique publique (Insee, Drees, Dares, Eurostat, OCDE) > institutions de contrôle (Cour des comptes, HCFiPS, Sénat, Banque de France) > presse qui relaie > think tanks, toujours étiquetés (iFRAP « think tank libéral », Fondation Jean-Jaurès « proche du PS », OID « classé à droite »).
4. Confronter les sources contradictoires : chercher activement l'argument du camp adverse et dire pourquoi il tient ou non.
5. Calculer en code, pas de tête.

### 3.2 Confusions à démêler systématiquement

| Confusion | Exemple rencontré |
|---|---|
| Coût total ≠ coût de l'abus | 37 Md€ d'allocations chômage ≠ 37 Md€ de « profiteurs » |
| Estimé ≠ détecté ≠ récupéré | Fraude sociale : 14 Md€ estimés, 2 Md€ détectés, 680 M€ récupérés |
| Montant brut ≠ part de quoi ? | Rapporter à la dépense publique, au déficit, au PIB, par habitant |
| Flux ≠ stock | Arrivées annuelles vs part des immigrés dans la population |
| Immigré ≠ étranger ≠ descendant | Un tiers des immigrés sont français ; les descendants sont français de naissance |
| Règles ≠ recours | Surreprésentation dans les HLM ≠ « plus de droits » |
| Moyenne brute ≠ à caractéristiques égales | Écarts d'emploi non corrigés de l'âge, du diplôme, du lieu |
| Mis en cause ≠ condamné | Statistiques de délinquance par nationalité |
| Effet de sélection | Émigrés français très diplômés vs immigrés en France |

### 3.3 Conventions de calcul

- Population pour les montants par habitant : 68,5 millions, divisée par 12 pour un montant mensuel.
- Dépense publique 2025 : 1 714,2 Md€. Déficit 2025 : 152,5 Md€ (5,1 % du PIB). Dette : 115,7 % du PIB (Insee IP 2106).
- Fraude des allocataires : 36 % des 14 Md€ du HCFiPS, soit environ 5 Md€.
- Titres de séjour par habitant : volumes Eurostat 2025 divisés par des populations arrondies (FR 69,1 M ; DE 83,6 M ; ES 49,1 M ; IT 58,9 M ; PL 36,5 M).

## 4. Workflow en deux temps

1. Article long dans la conversation : verdict par sous-affirmation, tableaux, un visuel, autocritique (« ce qui est vrai dans l'affirmation »), angles morts, sources numérotées. Dilhan challenge à ce stade.
2. Artifact dans le format validé, seulement quand Dilhan le demande.

Dilhan préfère qu'on fasse le travail plutôt qu'on demande. Une seule question, et seulement si l'énoncé est réellement ambigu.

## 5. Format de page validé

### 5.1 Retour de Dilhan à respecter strictement

Sur la v1 : « Un peu trop "mode d'emploi pour tenir l'argumentation" et pas assez "produit prêt à être consommé pour trancher la vérité derrière l'affirmation initiale". » Et : « Je partage ces artefacts en direct avec les principaux intéressés. Oubliez les "copier la réponse". Produire quelque chose d'agréable visuellement avec des images, graphiques, comparaisons faciles à comprendre lorsque c'est pertinent. Focus sur les conclusions et une argumentation simple, avec possibilité pour chaque argument de déplier pour creuser dans les données et explications plus longues. »

Concrètement : pas de bouton de copie, pas de « réponse en 30 secondes », pas de « contre-arguments à éviter », pas de ton coaching ou militant. Le lecteur croit à l'affirmation : il doit se sentir respecté, voir ce qui est vrai dans sa position, et trancher par lui-même.

### 5.2 Structure d'une page

1. En-tête : surtitre (« Vérification · données publiques 2019-2026 »), titre court en forme de question.
2. L'affirmation citée, découpée en 2 ou 3 segments soulignés (couleur = verdict), chacun lien d'ancre vers son chapitre.
3. Une illustration SVG qui pose le sujet.
4. Résumé des verdicts : échelle à 5 crans par sous-affirmation (Faux / Plutôt faux / Mitigé / Plutôt vrai / Vrai), une phrase, un lien « Voir l'analyse ».
5. Un chapitre par sous-affirmation : pastille hexagonale numérotée, segment en italique, titre-conclusion ; étiquette « Verdict : … » ; paragraphe de conclusion avec 2 ou 3 chiffres clés en gras et sources en exposant ; 1 à 3 panneaux visuels (barres, barres empilées, tuiles, matrice de points, ticket de caisse, axe d'estimations) ; encadré vert « Ce qui est vrai dans l'affirmation » (obligatoire, sincère) ; bloc repliable « Creuser les données ».
6. Chapitre « La question sous-jacente » si pertinent.
7. Chapitre « Éclairage » facultatif, avec ses limites explicites.
8. Encadré final sombre « Ce qu'il faut retenir » : 4 points maximum.
9. Sources numérotées, groupées par thème, relais et organismes engagés signalés, puis note de méthode.

### 5.3 Système visuel

- Google Fonts : Newsreader (titres), Public Sans (texte), IBM Plex Mono (chiffres, étiquettes).
- Palette en tokens CSS, thème clair et sombre complets. Accent bleu indigo, gris pour le contexte, orange pour les postes visés par l'affirmation. Verdicts : rouge (faux), orange (plutôt faux), ocre (mitigé), vert (plutôt vrai, et encadré « ce qui est vrai »), vert foncé (vrai).
- Graphiques en HTML/CSS ou SVG inline, à l'échelle. Pas d'images externes ni de librairie de graphiques.
- Mobile d'abord : vérifié à 390 px, en clair et en sombre, sans défilement horizontal.
- Repartir du HTML de la page immigration et remplacer le contenu.

### 5.4 Règles de rédaction

- Français, phrases courtes, actives, sans jargon. Pas de tiret cadratin ni demi-cadratin.
- Neutralité : mêmes exigences de preuve pour tous les camps ; étiquettes d'orientation identiques pour les think tanks de droite et de gauche.
- Chaque chiffre a une source en exposant. Les chiffres calculés par nous sont signalés.
- Le verdict porte sur l'affirmation telle qu'elle est formulée, y compris sa conclusion implicite. Un fait réel mal interprété donne un verdict nuancé, pas « vrai ».

### 5.5 Contrôle avant publication

Script : balises fermées, références `#sN` existantes et toutes citées, aucun tiret long, ancres valides. Capture à 390 px en clair et en sombre (Playwright), passe de corrections, publication. Rappeler qu'une nouvelle page est privée tant qu'elle n'est pas partagée.

## 6. Conclusions acquises

### 6.1 « Trop de profiteurs et de fainéants, le reste paie pour eux »

| Sous-affirmation | Verdict | Faits clés |
|---|---|---|
| Trop de profiteurs | Plutôt faux | Fraude sociale estimée 14 Md€/an (HCFiPS 2026) : 52 % employeurs et travail dissimulé, 36 % allocataires (≈ 5 Md€, 0,3 % de la dépense publique), 12 % professionnels de santé. Fraude au RSA 1,5 Md€ contre ≈ 3 Md€ de RSA non réclamé. Fraude aux arrêts maladie détectée : 42 M€ sur 12,1 Md€. |
| Trop de fainéants | Mitigé | Par personne en emploi, la France travaille plus que l'Allemagne (1 489 h contre 1 335 h). Par salarié à temps plein, un peu moins (1 664 h contre 1 786 h). Par habitant, moins (666 h contre 724 h). Taux d'emploi : 25-54 ans quasi égal (83,2 % contre 85,2 %), écarts chez les 15-24 ans (34,7 % contre 50,7 %) et les 55-64 ans (61,8 % contre 75,5 %). |
| Le reste paie pour eux | Faux | 56 % des personnes sont bénéficiaires nets de la redistribution élargie (Insee 2023), 90 % des plus de 60 ans. Par habitant et par mois : retraites 519 €, santé 412 €, intérêts 79 €, chômage 45 €, RSA 15 €, arrêts maladie 15 €, fraude des allocataires 6 €. |

Ce qui est vrai : les arrêts maladie augmentent plus vite que la démographie ne l'explique (≈ 40 % de la hausse non expliquée) ; la récupération de la fraude est très faible ; l'indemnisation chômage longue allonge le chômage (IPP : de 7 à 15 mois, environ +2,5 mois) ; le taux d'emploi global est faible (21e de l'UE).

Déficit : 152,5 Md€ en 2025, porté à 84 % par l'État. Leviers « profiteurs » : 1 à 5 Md€. Leviers structurels : écart de dépenses de retraite avec la zone euro ≈ 65 Md€, baisses d'impôts 2018-2023 non compensées 62 Md€ (Cour des comptes), hausse des intérêts +12 Md€ entre 2026 et 2027, effort du budget 2027 : 54 Md€.

### 6.2 « Les immigrés arrivent massivement, ne s'intègrent pas, ont plus de droits sociaux »

| Sous-affirmation | Verdict | Faits clés |
|---|---|---|
| Arrivent massivement | Mitigé | 384 230 premiers titres de séjour en 2025 (+11 %) : études 118 000, humanitaire 92 600 (+65 %), travail 51 190 (-13 %). Part des immigrés : 9,1 % en 2014, 11,2 % en 2024. Mais ≈ 5,5 titres pour 1 000 habitants contre 9 en moyenne UE. Solde naturel négatif en 2025, première fois depuis 1945. |
| Ne s'intègrent pas | Plutôt faux | Diplômés du supérieur à 30-39 ans : immigrés 43 %, descendants 47 %, sans ascendance migratoire 50 %. Emploi 2025 : sans ascendance 71,9 %, immigrés 61,9 %, descendants d'origine maghrébine 54,4 %, d'Afrique subsaharienne 46,7 %. Testing Dares : 31,5 % de rappels en moins pour un nom à consonance maghrébine. |
| Plus de droits sociaux | Faux | Étranger non européen : 5 ans de titre pour le RSA, 10 ans pour le minimum vieillesse ; sans titre, aucune allocation (AME pour les soins). Demandeur d'asile : 207 € ou 432 € par mois contre 646 € de RSA. Surreprésentation expliquée par la pauvreté (31,5 % contre 11,1 %). AME : 465 000 bénéficiaires, ≈ 1,4 Md€, ≈ 1,75 € par habitant et par mois. |

Ce qui est vrai : hausse des flux et bascule vers l'humanitaire ; échec d'intégration sur le marché du travail pour une partie des descendants d'origine africaine ; décrochage scolaire d'un tiers des fils d'immigrés d'Afrique, du Maghreb ou de Turquie ; surreprésentation des étrangers parmi les mis en cause (17,7 % pour ≈ 7 % de la population en 2019), causes non établies ; exécution faible des expulsions (23 % contre 44 % UE, 2010-2016).

Coût budgétaire : impact proche de zéro selon OCDE (≈ +1 % du PIB hors défense et dette, -0,85 % en les incluant) et CEPII (-0,5 % à +0,5 %). Chiffrages à 40-54 Md€ (OID, Contribuables associés) aux méthodes contestées.

Cadre juridique : le Conseil constitutionnel admet le principe d'une durée de résidence pour certaines prestations, mais a jugé 5 ans disproportionnés (décision 2024-6 RIP). Proposition sénatoriale à 2 ans.

### 6.3 Éclairage : Français à l'étranger

1,78 million d'inscrits consulaires (2026), 2,8 à 3,2 millions au total. 58 % des émigrés de 25-64 ans diplômés du supérieur contre 35 % de ceux restés. Au Québec, présence après admission : France 81 %, Algérie 90 %, Maroc 86 %, Haïti 91 %. 612 écoles françaises dans 138 pays, 11 députés des Français de l'étranger. Limite majeure : aucune donnée ne mesure l'intégration des Français à l'étranger selon les critères Insee.

### 6.4 Fils rouges

1. Fait réel, mauvaise cible : les deux affirmations partent d'un fait exact mais l'attribuent à la mauvaise cause ou se trompent d'un ordre de grandeur.
2. Le vrai sujet commun est l'emploi : jeunes, seniors, descendants d'immigrés d'origine africaine.
3. Les poids lourds budgétaires sont les retraites et la santé, qui profitent à l'électeur médian.
4. Surreprésentation ≠ privilège.
5. Le statut social change la perception d'un même comportement.

## 7. Limites connues et points à revérifier

| Point | Problème | À faire si réutilisé |
|---|---|---|
| Solde migratoire 2023-2025 (+176 000) | Valeur conventionnelle Insee | Toujours le préciser |
| Non-recours au RSA | Données 2018 | Chercher une mise à jour Drees |
| Délinquance par nationalité | Données 2019, non corrigées ; bilan SSMSI 2025 non lu | Réessayer Interstats |
| Coût budgétaire de l'immigration | Études 2006-2018 et 1979-2011 | Signaler l'absence d'étude officielle récente |
| Conversion OID et Contribuables associés en % du PIB | Méthodes reprises des auteurs | Revérifier |
| Proposition sénatoriale « 2 ans » | Statut parlementaire non vérifié | Vérifier |
| Comparaisons asile et expulsions | Données 2016-2020 | Chercher Eurostat récent |
| Part des immigrés : 11,2 % ou 11,3 % | Deux publications Insee | Citer la source exacte |
| Illustration page immigration | Arrivées 2025 vs départs 2018 | Actualiser si donnée récente |
| Baisses d'impôts (62 Md€) | Lu via relais citant la Cour des comptes | Remonter au rapport |

## 8. Sources : ce qui marche et ce qui bloque

Fonctionne : pages et PDF Insee, PDF Drees, rapports du Sénat, PDF Banque de France, Unédic, PDF du gouvernement du Québec, note HCFiPS (strategie-plan.gouv.fr).

Bloque : PDF de l'OCDE (passer par le Trésor ou la presse), Interstats (erreur), Statista, certains articles payants.

Sources de référence : Insee IP 2106 et IP 2093 ; Banque de France Bulletin 259/4 ; Drees comptes de la protection sociale 2024 et fiches minima sociaux 2025 ; HCFiPS janvier 2026 ; Insee « Immigrés et descendants d'immigrés » ; Insee Analyses n° 88 et n° 118 ; OCDE Perspectives des migrations internationales 2021.

## 9. Garde-fous

- Neutralité politique : même effort et même ton pour tous les camps. Ne pas reprendre les chiffres faibles du camp opposé (« la fraude fiscale, c'est 80 à 100 Md€ », jugé non étayé par la Cour des comptes ; « les immigrés rapportent plus qu'ils ne coûtent », vrai seulement hors défense et dette).
- Pas de verdict sur des valeurs.
- Distinguer faits, hypothèses et probabilités, donner des ordres de grandeur, comparer, exposer les compromis.
- Pages partagées : pas de personne privée, pas de citation inventée, pas d'usurpation d'identité visuelle.
