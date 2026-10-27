# PS : corpus programmatique

- Rédigé le : 2026-10-27
- Date d'arrêt des données : 2026-10-27
- Auteur : sous-agent Opus, étape 1 (section f préparée par un second sous-agent Opus, relue et intégrée par l'agent principal)
- Statut : brouillon (étape 1)
- Règle appliquée : `01-socle/01-criteres.md` §6 (hiérarchie du corpus ; programme du mandat exercé pour une force qui a gouverné) et `01-socle/03-sources-et-hierarchie.md` (archivage, étiquetage)

Périmètre (voir `00-perimetre.md`) : le Parti socialiste (PS), le groupe « Socialistes et apparentés » (SOC) à l'Assemblée nationale, et son candidat Raphaël Glucksmann (Place publique), vainqueur de la primaire du 11 octobre 2026. Olivier Faure, premier secrétaire, parle pour le parti ; Boris Vallaud, président du groupe, parle pour le groupe. Place publique est hors périmètre, sauf au titre du candidat : ses textes sont classés « position du candidat ». Les textes communs du Nouveau Front populaire (NFP) sont signalés « texte commun ».

Sigles utilisés : AN (Assemblée nationale), SOC (groupe Socialistes et apparentés), SER (groupe Socialiste, Écologiste et Républicain du Sénat), NFP (Nouveau Front populaire), NUPES (Nouvelle Union populaire écologique et sociale, 2022), GRS (Gauche républicaine et socialiste), COP (commission d'organisation de la primaire), CN (conseil national), BN (bureau national), APN (Assemblée politique nationale de Place publique), PPL (proposition de loi), PPLO (proposition de loi organique), PPLC (proposition de loi constitutionnelle), PPRE (proposition de résolution européenne), PLF (projet de loi de finances), PLFSS (projet de loi de financement de la sécurité sociale), UE (Union européenne), AME (aide médicale de l'État), ASPA (allocation de solidarité aux personnes âgées), OQTF (obligation de quitter le territoire français), CSG (contribution sociale généralisée), IS (impôt sur les sociétés), ISF (impôt de solidarité sur la fortune), VSS (violences sexistes et sexuelles), Md€ (milliard d'euros).

Étiquette commune : tous les documents émanant du PS, du groupe SOC, du groupe SER ou de leurs élus sont des **sources du parti, partie prenante**. Les documents de Place publique et du candidat sont des **sources du candidat, partie prenante**. Les textes communs du NFP et de la primaire sont des sources des partis signataires, partie prenante. Les textes de PPL, PPLC, PPRE et amendements hébergés par l'Assemblée sont des sources primaires (niveau 1) dont l'auteur est partie prenante.

Archivage : les fichiers sont dans `02-partis/ps/corpus/`, tous téléchargés ou consultés le **2026-10-27**. Deux PDF dépassent 20 Mo et ne sont pas versionnés : le contre-budget 2027 « Les 7 priorités budgétaires » (22,4 Mo) et la note budgétaire commune du NFP pour 2025 (46,4 Mo) ; pour chacun, lien, somme de contrôle SHA-256 et copie texte (`.md`). Le plus lourd des fichiers versionnés fait 18,2 Mo (dossier de presse de la niche de janvier 2025). Les deux programmes NFP de 2024 sont réarchivés sous C-PS (copie à l'identique des fichiers C-LFI-22 et C-LFI-23) pour que la verticale soit autonome. Les tirets cadratins et demi-cadratins des textes d'origine ont été remplacés dans les copies texte, et les césures invisibles retirées (mention en tête de chaque fichier). Les articles de presse ne sont pas reproduits : quand une presse sert de relais, la fiche en donne un résumé rédigé par nos soins et une citation de 15 mots au plus. Scripts d'extraction tenus hors du dépôt (dossier temporaire de la session), PDF lus avec `pdftotext`.

Légende du statut d'archivage :
- **PDF archivé** : fichier original téléchargé.
- **Texte archivé** : copie texte de la page web ou du PDF (`.md`), avec URL et date de consultation.
- **Lien seul** : pas de fichier téléchargeable, fichier non retenu, ou pas de source primaire accessible.

---

## Synthèse

| Catégorie (§6) | Nombre de fiches | Archivés |
|---|---|---|
| a. Programme 2027, textes de campagne, textes du parti depuis 2024 (dont couche candidat : 8 fiches, C-PS-14 à C-PS-21) | 21 | 7 PDF, 12 fiches texte (dont 6 fichiers pour le projet socialiste), 2 liens seuls |
| b. Programme des législatives 2024 (NFP, texte commun) | 2 | 2 PDF |
| c. Programme présidentiel 2022 | 2 | 2 PDF |
| d. Contre-budgets et négociations budgétaires du groupe SOC et du NFP | 8 | 2 PDF (amendements), 6 fiches texte (dont 2 copies texte de PDF de plus de 20 Mo) |
| e. PPL, PPLO, PPLC, PPRE, amendements et motions du groupe SOC | 35 | 32 fichiers PDF (dont 2 dossiers de presse de niche et 3 textes dans une même fiche), 5 fiches texte, 2 liens seuls |
| Mandat exercé (2012) | 2 | 2 PDF |
| f. Déclarations depuis le 1er janvier 2026 | 23 | 23 fiches texte (9 avec copie de la page du parti ou du candidat, 4 comptes rendus de l'Assemblée, 1 note publiée par une fondation, 9 relais de presse) |
| Actes | applicable (2012-2017) | renvoi à `00-perimetre.md` |

Total : **93 fiches** (C-PS-01 à C-PS-93, sans trou ni doublon ; C-PS-71 à C-PS-93 pour la section f). Dossier `corpus/` : 98 fichiers (47 PDF, 51 `.md`), 62Mo.

**Point principal :** **le candidat n'a pas de programme au 27 octobre 2026, et aucun programme commun n'est engagé.** Raphaël Glucksmann annonçait le 25 août un programme sous un mois et demi ; rien n'est paru, ni sur glucks2027.fr, ni sur le site de Place publique (voir `00-perimetre.md`). La charte de la primaire prévoit un « programme commun » avec les autres partis de la gauche démocratique et écologique : aucune trace d'ouverture. **Les documents les plus aboutis pour 2027 sont donc ceux du parti : (1) le « Projet socialiste »** adopté par les adhérents le 25 juin 2026 à 83 % [C-PS-01], [C-PS-02], document programmatique complet (20 chapitres en six parties ; environ 600 propositions selon la presse), **non chiffré** et sans trajectoire de déficit ; son PDF intégral n'est pas public (espace militant et édition imprimée), mais son texte intégral est en ligne par parties sur projet-socialiste.fr et archivé ici ; **(2) le contre-budget 2027 du groupe SOC, « Les 7 priorités budgétaires »** (24 septembre 2026) [C-PS-33], **document primaire trouvé** sur le site du parti : 33 Md€ de mesures (10 Md€ de pouvoir d'achat, 1 Md€ pour les PME, 22 Md€ de dépenses nouvelles), 39,5 Md€ de recettes nouvelles, 12,1 Md€ d'économies et 5,5 Md€ de lutte contre la fraude (soit 17,5 Md€ d'« économies et lutte contre la fraude » au tableau de chiffrage), effort net de réduction du déficit affiché de 24 Md€ en 2027 (« 0,8 point de PIB »), sans cible de déficit en pourcentage du PIB ; **(3) la couche candidat** : profession de foi de primaire [C-PS-14], lettre du 25 août [C-PS-15] et « Acte I » de Place publique (42 chantiers) [C-PS-16].

---

## a. Programme 2027, textes de campagne, textes du parti depuis 2024 (priorité 1)

### Programme du parti pour 2027

### [C-PS-01] « Projet socialiste » 2026 (texte intégral, six parties)
- Auteur : Parti socialiste (coordination : Chloé Ridel, secrétaire nationale à la coordination du projet, selon le site)
- Date : présenté à la presse le 2026-04-22 (version soumise aux amendements des militants, 144 pages selon LCP, source secondaire 1) ; **adopté par les adhérents le 2026-06-25** (83 %), version adoptée présentée le 2026-06-30 ; site mis en ligne le 2026-07-02
- Nature : projet du parti, 20 chapitres en six parties (« Vivre libres », « Être en sécurité(s) », « S'épanouir à égalité », « Vivre avec la nature », « Refaire société », « Pacifier le monde »), constats puis « Propositions »
- URL : https://projet-socialiste.fr/projet/ (une page par partie)
- Archivage : texte archivé, six fichiers `corpus/C-PS-01-projet-socialiste-<partie>-2026-10-27.md` (vivre-libres, etre-en-securites, sepanouir-a-egalite, vivre-avec-la-nature, refaire-societe, pacifier-le-monde ; environ 50 000 mots au total). PDF intégral non public (voir « Trous »).
- Statut : programme officiel du parti (texte adopté)
- Étiquette : source du parti, partie prenante
- Utile pour : les six axes. Exemples à reprendre de la page même aux étapes suivantes : axe 4 (Smic à 1 690 € net et conférence sociale ; taxe Zucman de 2 % au-delà de 100 M€ de patrimoine ; « impôt sur les grandes successions » ; IS progressif ; suppression des exonérations de cotisations entre 2 et 3,5 Smic, 11 Md€ par an) ; axe 2 (abrogation de la réforme de 2023, conférence sociale, 43 annuités réductibles selon la pénibilité, âge légal « ramené à 62 ans » qui « continuera de jouer un rôle de protection minimale ») ; axe 3 (titre de séjour pour tout étranger ayant un contrat de travail depuis au moins 6 mois ; renouvellement automatique des titres de longue durée ; défendre l'AME) ; axe 5 (police de contact, récépissés de contrôle d'identité, autorité externe de contrôle des forces de sécurité) ; axe 6 (convention de citoyens, juristes et élus, réformes constitutionnelles validées par référendum ; RIP à 1 million de signatures et référendum d'initiative citoyenne ; droits de l'opposition ; budget européen triplé à 3 % du PIB européen, emprunt commun de 500 Md€). Pas de chiffrage global ni de trajectoire de déficit.

### [C-PS-02] Projet socialiste : adoption, construction, sommaire et édition
- Auteur : Parti socialiste
- Date : pages publiées du 2026-06-19 au 2026-09-16 (métadonnées du site), consultées le 2026-10-27
- Nature : cinq pages web (adoption le 25 juin 2026 « à 83 % » après plus de 3 000 amendements et 600 contributions citoyennes ; conférence de presse du 30 juin ; construction : tour de France, plus de 200 auditions ; sommaire des 20 chapitres ; édition imprimée « Le livre du projet »)
- URL : https://projet-socialiste.fr/le-projet-socialiste-adopte-par-les-militantes/ et pages liées (liste en tête du fichier)
- Archivage : texte archivé, `corpus/C-PS-02-projet-socialiste-adoption-et-sommaire-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : statut du projet (texte adopté, donc position du parti) ; méthode d'élaboration (Q5, Q6 bloc a). Le nombre de votants et le nombre exact de propositions ne sont pas publiés.

### Stratégie présidentielle et désignation du candidat

### [C-PS-03] Consultation militante sur la stratégie présidentielle (9 juillet 2026)
- Auteur : Parti socialiste (direction ; textes des deux options rédigés par leurs dépositaires, les textes d'orientation A d'une part, B et C d'autre part)
- Date : annonce 2026-07-07, résultat 2026-07-10
- Nature : deux pages web : texte des deux choix soumis au vote, résultat (choix 2 à 55,5 %)
- URL : https://parti-socialiste.fr/actualites/jeudi-les-militantes-socialistes-votent-sur-la-strategie-presidentielle/ ; https://parti-socialiste.fr/actualites/les-militantes-socialistes-ont-adopte-leur-strategie-presidentielle-pour-2027/
- Archivage : texte archivé, `corpus/C-PS-03-consultation-strategie-presidentielle-2026-07-09-2026-10-27.md`
- Statut : texte du parti (décision des adhérents)
- Étiquette : source du parti, partie prenante
- Utile pour : procédure de désignation ; engagement de construire « un programme commun, un accord législatif et un contrat de gouvernement » avec la gauche démocratique, écologique et républicaine ; Q6 bloc a (méthode : vote des adhérents).

### [C-PS-04] Conseil national du 25 août 2026 : processus « Choisir 2027 »
- Auteur : Parti socialiste
- Date : 2026-08-25
- Nature : page web : modalités de la primaire (vote électronique à deux tours, 9-10 et 16-17 octobre ; parrainages ; participation de 15 € ou 10 € ; charte des valeurs communes annexée)
- URL : https://parti-socialiste.fr/actualites/choisir-2027-le-processus-de-designation-du-ou-de-la-candidat-e-socialiste-a-lelection-presidentielle-est-lance/
- Archivage : texte archivé, `corpus/C-PS-04-conseil-national-choisir-2027-2026-08-25-2026-10-27.md`
- Statut : texte du parti (décision du CN) ; c'est l'acte du parti qui fonde la candidature, aucun acte d'investiture postérieur n'ayant été trouvé
- Étiquette : source du parti, partie prenante
- Utile pour : investiture du candidat ; engagement de programme commun ; texte de l'accord et de la charte non publié (voir « Trous »).

### [C-PS-05] Bureau national du 16 septembre 2026 et communiqués du 23 septembre 2026
- Auteur : Parti socialiste (BN)
- Date : 2026-09-16 et 2026-09-23
- Nature : trois communiqués : ratification de trois candidatures socialistes à la primaire ; suspension conservatoire d'un député candidat après un signalement, « à l'unanimité moins une opposition et trois abstentions » ; validation de la procédure en référé puis en appel
- URL : https://parti-socialiste.fr/communiques-de-presse/bureau-national-du-16-septembre-2026/ et deux pages liées (liste en tête du fichier)
- Archivage : texte archivé, `corpus/C-PS-05-bureau-national-ratification-candidatures-2026-09-16-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : liste des candidats ; Q6 bloc d (acte public du parti sur un élu, motif donné par le parti : défense des droits des femmes et « exemplarité »), à instruire selon les règles 1 à 5 et précisions i à iv du socle.

### [C-PS-06] « Choisir 2027 », site de la primaire, et communiqué de la COP du 9 octobre 2026
- Auteur : organisations signataires (PS, Place publique, GRS) ; COP présidée par Patrick Mennucci, communiqué cosigné par les cinq candidats
- Date : capture du site du 2026-09-19 ; communiqué du 2026-10-09
- Nature : page d'accueil (texte d'appel « 2027 : Construisons l'alternative », calendrier, règles de vote, liste des cinq candidats) ; communiqué sur les attaques informatiques et la prolongation du vote jusqu'au dimanche 11 octobre, 18 h
- URL : https://choisir2027.fr/ (hors ligne au 2026-10-27), lu sur https://web.archive.org/web/20260919221245/https://choisir2027.fr/ ; https://parti-socialiste.fr/actualites/choisir-2027_les-electeurs-pourront-voter-jusqua-dimanche-18h/
- Archivage : texte archivé, `corpus/C-PS-06-choisir-2027-site-primaire-2026-10-27.md`
- Statut : texte commun des organisateurs de la primaire
- Étiquette : source des partis organisateurs, partie prenante
- Utile pour : procédure ; texte d'appel commun (axe 6 : critique du refus de tenir compte du résultat des législatives de 2024 ; hors grille). Les résultats proclamés par la COP ne sont pas en ligne (voir « Trous »).

### [C-PS-07] Profession de foi d'Olivier Faure à la primaire
- Auteur : Olivier Faure, premier secrétaire, candidat à la primaire
- Date : PDF créé le 2026-09-24
- Nature : profession de foi, 2 pages
- URL : https://choisir2027.fr/wp-content/uploads/2026/09/Prof.foi_A4_OF-1.pdf (site hors ligne) ; archive : https://web.archive.org/web/20260925081050/https://choisir2027.fr/wp-content/uploads/2026/09/Prof.foi_A4_OF-1.pdf
- Archivage : PDF archivé, `corpus/C-PS-07-profession-de-foi-faure-primaire-2026-09-2026-10-27.pdf` (1,1 Mo)
- Statut : position individuelle du premier secrétaire comme candidat à la primaire (pas un texte adopté)
- Étiquette : source du parti, partie prenante
- Utile pour : comparaison avec la ligne du candidat désigné (rassemblement, Smic, justice fiscale). Les professions de foi de Jérôme Guedj, Ségolène Royal et Emmanuel Maurel existent dans la même archive (lien seul, voir « Ajouts proposés »).

### [C-PS-08] Discours d'Olivier Faure à l'université d'été de Blois (29 août 2026)
- Auteur : Olivier Faure, premier secrétaire
- Date : 2026-08-29 (PDF créé le même jour ; « seul le prononcé fait foi »)
- Nature : discours, 17 pages
- URL : https://parti-socialiste.fr/wp-content/uploads/2026/08/BLOIS26_Discours.pdf
- Archivage : PDF archivé, `corpus/C-PS-08-discours-faure-blois-2026-08-29-2026-10-27.pdf` (4,1 Mo)
- Statut : position du parti (discours du premier secrétaire à la tribune du parti)
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1, 4 et 6 (ligne du parti à la rentrée 2026, avant la primaire) ; hors grille (climat). Postérieur au 1er janvier 2026 : à signaler au second sous-agent pour éviter un doublon en section f.

### Textes du parti et du groupe depuis 2024

### [C-PS-09] 81e congrès (Nancy, 2025) : textes d'orientation et élection du premier secrétaire
- Auteur : Parti socialiste
- Date : 2025-04-26 (enregistrement des textes), 2025-05-28 (résultats du vote du 27 mai), ratification au congrès (communiqué daté du 27 mai 2025 sur le site, congrès des 13 au 15 juin 2025)
- Nature : trois communiqués : texte A « Le cœur de la gauche » (Olivier Faure) 42,21 % puis 42,02 % ; texte B « Unir » (Boris Vallaud) 17,41 % puis 17,60 % ; texte C « Changer pour gagner » (Nicolas Mayer-Rossignol) 40,38 % ; Olivier Faure réélu à 51,15 % sur 25 163 votants
- URL : https://parti-socialiste.fr/communiques-de-presse/81e-congres-du-parti-socialiste-resultats-du-vote-sur-les-textes-dorientation/ et deux pages liées
- Archivage : texte archivé, `corpus/C-PS-09-congres-nancy-2025-resultats-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : direction du parti et rapports de force internes. **Le texte d'orientation A lui-même n'a pas été trouvé** (voir « Trous »).

### [C-PS-10] Convention nationale « Sécurité et prévention de la délinquance » (2025)
- Auteur : Parti socialiste (convention copilotée par Roger Vicot, député, et une secrétaire nationale)
- Date : vote des militants le 2025-04-03 (plus de 90 %), ratification le 2025-04-26
- Nature : communiqué (plus de 160 propositions selon le parti)
- URL : https://parti-socialiste.fr/communiques-de-presse/le-parti-socialiste-ratifie-sa-convention-securite-et-prevention-de-la-delinquance/
- Archivage : texte archivé du communiqué, `corpus/C-PS-10-convention-securite-prevention-2025-04-26-2026-10-27.md` ; texte de la convention non trouvé
- Statut : texte du parti (adopté)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (doctrine : égalité d'accès au service public de sécurité, prévention, lien police-justice-population, narcotrafic). La partie « Être en sécurité(s) » du projet [C-PS-01] en reprend l'essentiel à vérifier à l'étape 2.

### [C-PS-11] Déclaration politique du groupe SOC pour la XVIIe législature
- Auteur : groupe Socialistes et apparentés
- Date : 2024-07-22
- Nature : déclaration politique (page web, environ 3 800 mots)
- URL : https://parti-socialiste.fr/vie-parlementaire/notre-declaration-politique-17eme-legislature/
- Archivage : texte archivé, `corpus/C-PS-11-declaration-politique-groupe-17e-legislature-2024-07-22-2026-10-27.md`
- Statut : texte du groupe parlementaire
- Étiquette : source du parti, partie prenante
- Utile pour : engagements du groupe au début de la législature, articulation avec le programme du NFP (six axes ; Q6 bloc c).

### [C-PS-12] Statuts du Parti socialiste
- Auteur : Parti socialiste
- Date : PDF créé le 2021-09-27, mis en ligne le 2026-06-23 (fichier « REFORME_Statuts_V9 »)
- Nature : statuts, 24 pages (préambule, déclaration de principes, organisation, discipline)
- URL : https://parti-socialiste.fr/wp-content/uploads/2026/06/REFORME_Statuts_V9.pdf (page « Les textes de référence »)
- Archivage : PDF archivé, `corpus/C-PS-12-statuts-parti-socialiste-2026-10-27.pdf` (1,2 Mo)
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : Q6 bloc d (valeurs affichées, procédures de sanction ; l'article 4.3.4 est invoqué par le BN du 16 septembre 2026 [C-PS-05]) ; institutions internes. Version en vigueur au 2026-10-27 à confirmer (le nom de fichier évoque une réforme).

### [C-PS-13] Charte éthique du Parti socialiste (2025)
- Auteur : Parti socialiste
- Date : PDF créé le 2025-02-20
- Nature : charte, 2 pages
- URL : https://parti-socialiste.fr/wp-content/uploads/2026/06/charte-ethique_2025.pdf
- Archivage : PDF archivé, `corpus/C-PS-13-charte-ethique-2025-2026-10-27.pdf` (0,1 Mo)
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : Q6 bloc d (règle d'investiture ou de sanction éventuelle, à qualifier selon la précision i du socle).

### Couche candidat (position du candidat, distincte de celle du parti)

### [C-PS-14] Profession de foi de Raphaël Glucksmann à la primaire
- Auteur : Raphaël Glucksmann, candidat à la primaire (Place publique)
- Date : PDF créé le 2026-09-24
- Nature : profession de foi, 1 page, « Refonder la gauche, réveiller la France ! » ; aucune mesure chiffrée
- URL : https://choisir2027.fr/wp-content/uploads/2026/09/Profession-de-foi-RG.pdf (connexion refusée le 2026-10-27, comme lors de l'essai précédent) ; **récupérée par l'archive** : https://web.archive.org/web/20260925081255/https://choisir2027.fr/wp-content/uploads/2026/09/Profession-de-foi-RG.pdf
- Archivage : PDF archivé, `corpus/C-PS-14-profession-de-foi-glucksmann-primaire-2026-09-2026-10-27.pdf` (0,5 Mo)
- Statut : candidat
- Étiquette : source du candidat, partie prenante
- Utile pour : thèmes affichés (souveraineté énergétique et technologique, « révolution écologique », « révolution féministe », contribution des plus fortunés, services publics, école) ; axe 6 (refondation de la gauche, refus des « compromissions »).

### [C-PS-15] Raphaël Glucksmann, « Sa lettre aux Français »
- Auteur : Raphaël Glucksmann, coprésident de Place publique
- Date : 2026-08-25 (publiée sur le site de Place publique)
- Nature : lettre ouverte
- URL : https://place-publique.eu/posts/2fgDdljEIy36rgxBjRyiQZ/raphael-glucksmann-sa-lettre-aux-francais
- Archivage : texte archivé, `corpus/C-PS-15-glucksmann-lettre-aux-francais-2026-08-25-2026-10-27.md`
- Statut : candidat (alors candidat à la primaire)
- Étiquette : source du candidat, partie prenante
- Utile pour : lignes de campagne au moment de la déclaration ; couche candidat des axes 4 et 6.

### [C-PS-16] Place publique, « Acte un. Notre vision pour la France. Les chantiers de Place publique pour redonner vie à la promesse républicaine »
- Auteur : Place publique (travail collectif depuis octobre 2024 selon le parti)
- Date : PDF créé le 2026-10-15 (date de création du fichier en ligne ; un profil de candidat le date de juin 2025, à vérifier)
- Nature : document programmatique, 88 pages, 42 chantiers en deux parties (« Une France puissante grâce à une Europe souveraine » ; « Un nouveau contrat social et démocratique pour une France plus juste »)
- URL : https://place-publique.eu/document/6J8wjk3EW8dBCLwKxa7J96/projet-placepublique-acte1.pdf ; page : https://place-publique.eu/pages/6mRSwq5tuSrSi68Cw1IADX/l-acte-i
- Archivage : PDF archivé, `corpus/C-PS-16-place-publique-acte-1-vision-pour-la-france-2026-10-27.pdf` (2,0 Mo)
- Statut : candidat (texte du parti du candidat, hors périmètre du PS)
- Étiquette : source du candidat, partie prenante
- Utile pour : le document le plus détaillé de la couche candidat à la date d'arrêt : six axes (défense et Europe, travail, démocratie, santé, sécurité et justice, protection sociale), à comparer avec le Projet socialiste.

### [C-PS-17] Place publique, pages « Le projet », « L'Acte I », « Les urgences », « Le parti »
- Auteur : Place publique
- Date : consultées le 2026-10-27 (non datées)
- Nature : pages web (méthode de « co-construction », plus de 3 000 contributeurs revendiqués ; « urgences » ; présentation du parti)
- URL : https://place-publique.eu/pages/69jA2SKIG5udlNX7wI3dmc/le-projet et pages liées
- Archivage : texte archivé, `corpus/C-PS-17-place-publique-pages-projet-urgences-2026-10-27.md`
- Statut : candidat
- Étiquette : source du candidat, partie prenante
- Utile pour : couche candidat ; Q6 bloc a (méthode revendiquée).

### [C-PS-18] Place publique : protocole de désignation (APN du 25 août 2026) et annonce du résultat de la primaire
- Auteur : Place publique
- Date : 2026-08-26 (article) ; page d'accueil consultée le 2026-10-27
- Nature : article (adoption à l'unanimité par l'APN du « Protocole d'accord relatif à la désignation du candidat de la gauche socialiste et démocratique » et de la « Charte d'engagement des candidats ») ; bandeau « Raphaël Glucksmann remporte la primaire ! » (66,17 %, « 79 613 votants »)
- URL : https://place-publique.eu/posts/4eeAyKK12GlgUWF8zbaWjY/election-presidentielle-2027-vote-de-l-assemblee-politique-nationale ; https://place-publique.eu/
- Archivage : texte archivé, `corpus/C-PS-18-place-publique-protocole-primaire-et-resultat-2026-10-27.md`
- Statut : candidat
- Étiquette : source du candidat, partie prenante
- Utile pour : procédure ; écart sur les chiffres de la primaire (voir « Écarts »).

### [C-PS-19] Place publique, « Charte des principes »
- Auteur : Place publique
- Date : PDF créé le 2022-12-06
- Nature : charte, 10 pages
- URL : https://place-publique.eu/document/2qhnD4gywppQ8YM1XS2O26/charte-des-principes.pdf
- Archivage : PDF archivé, `corpus/C-PS-19-place-publique-charte-des-principes-2026-10-27.pdf` (0,1 Mo)
- Statut : candidat (parti du candidat)
- Étiquette : source du candidat, partie prenante
- Utile pour : valeurs revendiquées par le parti du candidat (couche candidat de Q6 bloc d, contexte seulement).

### [C-PS-20] Raphaël Glucksmann, *Nous avons encore envie* (livre)
- Auteur : Raphaël Glucksmann
- Date : parution le 2026-05-28 (Allary éditions), selon LCP (source secondaire 6)
- Nature : livre
- URL : pas de page éditeur ouverte ; présentation par LCP, 2026-05-26 : https://lcp.fr/actualites/presidentielle-raphael-glucksmann-devoile-les-premieres-lignes-de-son-possible-programme
- Archivage : lien seul (règle du socle : livres du candidat en lien seul). La présentation du livre par la presse fait l'objet d'une fiche de la section f ([C-PS-78], identifiant attribué à l'intégration).
- Statut : candidat
- Étiquette : source du candidat, partie prenante ; LCP en relais
- Utile pour : premières propositions du candidat selon LCP (convention citoyenne sur l'immigration avec membres tirés au sort ; service civique obligatoire de dix mois ; espérance de vie en bonne santé comme critère de départ en retraite ; plan de souveraineté européenne, grand emprunt européen, fin du droit de veto dans l'UE). Le texte du livre n'est pas au corpus.

### [C-PS-21] Programme de la liste « Réveiller l'Europe » (PS et Place publique) aux européennes de 2024
- Auteur : liste conduite par Raphaël Glucksmann, soutenue par le PS et Place publique
- Date : printemps 2024 (scrutin du 9 juin 2024)
- Nature : programme européen (338 mesures selon la presse)
- URL : PDF non trouvé (site reveillerleurope.fr injoignable le 2026-10-27, aucune archive de PDF dans l'index web.archive.org) ; présentation : Public Sénat, « Européennes 2024 : Raphaël Glucksmann prône dans son programme une "révolution écologique" » : https://www.publicsenat.fr/actualites/politique/europeennes-2024-raphael-glucksmann-prone-dans-son-programme-une-revolution-ecologique (non ouvert)
- Archivage : lien seul
- Statut : candidat (programme du candidat tête de liste ; classé en couche candidat parce que son auteur est le candidat, même si la liste était soutenue par le PS)
- Étiquette : source du candidat et du parti, partie prenante ; Public Sénat en relais
- Utile pour : axe 6 (Europe) en couche candidat, si le texte est retrouvé.

---

## b. Programme des législatives 2024 (priorité 2)

Les deux fichiers sont réarchivés sous C-PS à partir des fichiers de la verticale LFI ([C-LFI-22], [C-LFI-23], téléchargés le 2026-10-26), copie à l'identique, pour que la verticale PS soit autonome.

### [C-PS-22] « Nouveau Front populaire, contrat de législature », version du 27 juin 2024
- Auteur : Nouveau Front populaire (PS, LFI, Les Écologistes, PCF, Génération·s, Place publique et autres)
- Date : PDF créé le 2024-06-27
- Nature : programme commun en trois temps, 26 pages
- URL : voir la fiche [C-LFI-22] de `02-partis/lfi/01-corpus.md`
- Archivage : PDF archivé, `corpus/C-PS-22-programme-nfp-legislatives-2024-version-27-juin-2026-10-27.pdf` (0,2 Mo)
- Statut : texte commun (engagement du PS) ; version de référence
- Étiquette : source des partis signataires, partie prenante
- Utile pour : axe 4 (Smic à 1 600 € net ; ISF « renforcé » ; CSG progressive) ; axe 2 (abrogation de la réforme portant l'âge à 64 ans ; « objectif commun du droit à la retraite à 60 ans ») ; axe 6 (proportionnelle, abrogation du 49.3) ; axes 1, 3, 5.

### [C-PS-23] « Nouveau Front populaire, contrat de législature », version du 14 juin 2024
- Auteur : Nouveau Front populaire
- Date : PDF créé le 2024-06-14
- Nature : première version, 24 pages
- URL : voir la fiche [C-LFI-23]
- Archivage : PDF archivé, `corpus/C-PS-23-programme-nfp-legislatives-2024-version-14-juin-2026-10-27.pdf` (0,2 Mo)
- Statut : texte commun
- Étiquette : source des partis signataires, partie prenante
- Utile pour : contrôle de version.

---

## c. Programme présidentiel 2022 (priorité 3)

### [C-PS-24] Programme d'Anne Hidalgo, « Programme officiel » (2022)
- Auteur : campagne d'Anne Hidalgo (candidate du PS)
- Date : PDF créé le 2022-02-25 (programme présenté le 13 janvier 2022)
- Nature : programme, 44 pages : lettre aux Français, « 70 propositions pour la France », « un programme budgété et financé » (page 40)
- URL : https://www.2022avechidalgo.fr/2022avechidalgo/pages/208/attachments/original/1645795527/Anne_Hidalgo_Programme_officiel_en_A4_l%C3%A9ger_1645795527.pdf ; archive : https://web.archive.org/web/20260308164648/https://www.2022avechidalgo.fr/2022avechidalgo/pages/208/attachments/original/1645795527/Anne_Hidalgo_Programme_officiel_en_A4_l%C3%A9ger_1645795527.pdf
- Archivage : PDF archivé, `corpus/C-PS-24-programme-hidalgo-2022-2026-10-27.pdf` (1,3 Mo). Original du site de campagne, préféré à la copie hébergée par Les Économistes atterrés (source secondaire 7).
- Statut : programme officiel (présidentielle 2022)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (Smic augmenté de 15 % dès l'arrivée au pouvoir) ; axe 2 (retraites) ; axe 6 (RIP à 1 million de signatures, création d'un RIC, encadrement du 49.3 hors lois budgétaires) ; axe 1 (chiffrage du programme, page 40).

### [C-PS-25] Profession de foi d'Anne Hidalgo, premier tour 2022 (version accessible)
- Auteur : campagne d'Anne Hidalgo
- Date : PDF créé le 2022-03-18
- Nature : profession de foi, 4 pages
- URL : https://www.2022avechidalgo.fr/2022avechidalgo/pages/134/attachments/original/1648288493/Profession_de_foi_Anne_Hidalgo_accessible__1648288493.pdf (via web.archive.org, capture du 2026-03-08)
- Archivage : PDF archivé, `corpus/C-PS-25-profession-de-foi-hidalgo-2022-t1-2026-10-27.pdf` (3,8 Mo)
- Statut : programme officiel (document électoral)
- Étiquette : source du parti, partie prenante
- Utile pour : mesures mises en avant en 2022.

---

## d. Contre-budgets et négociations budgétaires du groupe SOC et du NFP (priorité 4)

Il n'existe pas de contre-budget autonome du groupe SOC pour 2025 : le groupe a porté la note commune du NFP [C-PS-26] et ses amendements. Pour 2026, les propositions de Blois [C-PS-29] ne sont connues que par l'exposé d'un amendement [C-PS-30] et la presse. Pour 2027, le document primaire existe [C-PS-33].

### [C-PS-26] NFP, « Budget 2025 : les 10 mesures phares » (texte commun)
- Auteur : groupes du NFP à l'Assemblée
- Date : 2024-10-10 (PDF créé le même jour) ; page du PS du 2024-10-09
- Nature : dossier de presse, 12 pages : dix mesures de recettes prioritaires, amendements communs au PLF 2025
- URL : https://parti-socialiste.fr/wp-content/uploads/2024/10/Dossier-de-presse-Budget-NFP_20241010_085302_0000-1.pdf ; https://parti-socialiste.fr/vie-parlementaire/budget-2025-les-10-mesures-phares-du-nouveau-front-populaire/
- Archivage : copie texte, `corpus/C-PS-26-nfp-budget-2025-dix-mesures-2024-10-10-texte-2026-10-27.md`. PDF de 46,4 Mo non versionné, SHA-256 `54910f8d4534806e7a7c51c3b967a70c19ffe9c66d0d8177aeaa84646267a8fc`. Même document que [C-LFI-41] (hébergé par LFI en version texte).
- Statut : texte commun (engagement du PS)
- Étiquette : source des partis signataires, partie prenante
- Utile pour : axes 1 et 4 (recettes communes du NFP pour 2025).

### [C-PS-27] Groupe SOC, positions et propositions sur le PLF 2025 (septembre à novembre 2024)
- Auteur : groupe Socialistes et apparentés
- Date : 2024-09-30, 2024-10-21, 2024-11-12
- Nature : trois pages web (déclaration des parlementaires socialistes ; amendements adoptés en commission ; mobilisation sur le budget)
- URL : https://parti-socialiste.fr/vie-parlementaire/pour-un-budget-plus-juste-la-mobilisation-continue/ et deux pages liées
- Archivage : texte archivé, `corpus/C-PS-27-groupe-soc-plf-2025-positions-2024-2026-10-27.md`
- Statut : texte du groupe
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1 et 4 (propositions du groupe sur le PLF 2025, sans document de contre-budget propre).

### [C-PS-28] Non-censure du gouvernement Bayrou (janvier et février 2025)
- Auteur : Parti socialiste
- Date : 2025-01-16, 2025-01-31, 2025-02-04
- Nature : trois communiqués : concessions obtenues pour ne pas censurer (réouverture de la réforme des retraites devant les partenaires sociaux, avec dernier mot au Parlement) ; vote contre le budget ; « non au gouvernement, oui à la nécessité d'un budget »
- URL : https://parti-socialiste.fr/communiques-de-presse/une-opposition-qui-arrache-des-victoires-pour-les-francais%c2%b7es/ et deux pages liées
- Archivage : texte archivé, `corpus/C-PS-28-non-censure-bayrou-janvier-fevrier-2025-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : actes de négociation 2024-2026 (`00-perimetre.md`) ; axes 1 et 2 ; Q6 bloc c.

### [C-PS-29] Propositions budgétaires des socialistes pour 2026 (Blois, 30 août 2025)
- Auteur : Parti socialiste et groupes parlementaires socialistes
- Date : 2025-08-30
- Nature : contre-budget présenté à l'université d'été ; **document primaire non trouvé**
- URL : relais LCP, 2025-08-30 : https://lcp.fr/actualites/le-ps-volontaire-pour-gouverner-a-presente-son-budget-alternatif-a-celui-de-francois ; résumé primaire dans l'exposé de [C-PS-30]
- Archivage : texte archivé (synthèse rédigée par nos soins, pas de reproduction de presse, et copie du communiqué du parti du 2025-07-15), `corpus/C-PS-29-propositions-budgetaires-blois-2025-08-30-2026-10-27.md`
- Statut : texte du parti, connu par un amendement du groupe et par la presse
- Étiquette : source du parti, partie prenante ; LCP en relais
- Utile pour : axe 1 (déficit de 5 % du PIB en 2026, 3 % à l'horizon 2032 ; 26,9 Md€ de recettes, 14 Md€ d'économies, 19,2 Md€ de dépenses ; réduction du déficit de 21,7 Md€, cohérente avec ces trois montants, calcul par nos soins) ; axe 2 (suspension de la réforme des retraites, retour à 62 ans) ; axe 4 (taxe Zucman, baisse de CSG entre 1 et 1,4 Smic).

### [C-PS-30] Amendement n° 125 au PLFSS 2026 (CSG sur les revenus du capital)
- Auteur : Jérôme Guedj et les membres du groupe SOC
- Date : 2025-10-27
- Nature : amendement après l'article 6 (taux de CSG sur les revenus du capital porté de 9,2 % à 11,2 %, 3,8 Md€ selon l'exposé) ; exposé qui résume les propositions de Blois
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/1907/AN/125.pdf
- Archivage : PDF archivé, `corpus/C-PS-30-amdt-125-plfss-2026-csg-capital-2026-10-27.pdf` (10 Ko)
- Statut : groupe parlementaire ; sort : rejeté
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1 et 4 ; seule source primaire trouvée des chiffres de Blois 2025.

### [C-PS-31] Amendement n° I-2359 au PLF 2026 (« taxe Zucman »)
- Auteur : Boris Vallaud, Olivier Faure et les membres du groupe SOC
- Date : 2025-10-22
- Nature : amendement après l'article 3 : prélèvement plancher de 2 % sur les patrimoines nets supérieurs à 100 M€
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/1906A/AN/2359.pdf
- Archivage : PDF archivé, `corpus/C-PS-31-amdt-I-2359-plf-2026-taxe-zucman-2026-10-27.pdf` (0,1 Mo)
- Statut : groupe parlementaire ; sort : rejeté (scrutin n° 3300 du 31 octobre 2025, liste gelée, axe 4)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (objet du scrutin gelé 3300) ; axe 1 (recettes).

### [C-PS-32] Conditions de non-censure posées au gouvernement Lecornu (septembre et octobre 2025)
- Auteur : Parti socialiste (communiqué ; BN)
- Date : 2025-09-26, 2025-10-07 ; relais de presse du 2025-10-14
- Nature : communiqué (refus par le Premier ministre de la taxe Zucman, de l'ISF, de la suspension de la réforme des retraites ; menace de censure) ; déclaration du BN après la démission du Premier ministre (demande d'un Premier ministre de gauche « s'engageant à ne pas utiliser le 49.3 », taxation des « ultras-riches », débat sur les retraites au Parlement) ; résumé de LCP sur la non-censure du 14 octobre 2025 (suspension de la réforme jusqu'à la présidentielle, renoncement au 49.3)
- URL : https://parti-socialiste.fr/communiques-de-presse/reaction-a-linterview-du-premier-ministre-sans-changement-majeur-dorientation-nous-censurerons-ce-gouvernement/ ; https://parti-socialiste.fr/communiques-de-presse/declaration-du-bureau-national-du-parti-socialiste-a-la-suite-de-la-demission-de-sebastien-lecornu/ ; LCP : https://lcp.fr/actualites/le-ps-ne-censurera-pas-le-gouvernement-le-risque-de-chute-s-eloigne-pour-sebastien
- Archivage : texte archivé (deux communiqués, résumé du relais par nos soins), `corpus/C-PS-32-conditions-non-censure-lecornu-2025-09-10-2026-10-27.md`
- Statut : texte du parti ; LCP en relais
- Étiquette : source du parti, partie prenante
- Utile pour : actes de négociation (suspension de la réforme des retraites, scrutin gelé 3684) ; Q6 blocs a et c (demande de renoncement au 49.3). Le communiqué des « conditions » de la mi-octobre mentionné par LCP n'a pas été trouvé.

### [C-PS-33] Contre-budget 2027 du groupe SOC : « Les 7 priorités budgétaires des socialistes »
- Auteur : groupe Socialistes et apparentés (édito signé par Estelle Mercier, cheffe de file PLF, Sandrine Runel, cheffe de file PLFSS, Boris Vallaud, président du groupe)
- Date : 2026-09-24 (édito ; PDF créé le même jour, mis en ligne le 2026-10-01) ; conférence de presse présentée par la presse au 2026-09-16 (source secondaire 2 et fiche [C-PS-82] de la section f)
- Nature : document de 12 pages : sept priorités et tableau de chiffrage
- URL : https://parti-socialiste.fr/wp-content/uploads/2026/10/7-priorites-budgetaires_SYNTHESE-V3.pdf ; page : https://parti-socialiste.fr/vie-parlementaire/les-7-priorites-des-socialistes-pour-le-budget-2027/
- Archivage : copie texte, `corpus/C-PS-33-contre-budget-2027-7-priorites-2026-09-24-texte-2026-10-27.md`. PDF de 22,4 Mo non versionné, SHA-256 `b1d4a55026d4e43b0fc2b457abf4aa862032aa9369bd6c77d734284ef214d1bb`.
- Statut : groupe parlementaire (document le plus abouti du parti pour l'axe 1 en 2027)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 1 (recettes 39,5 Md€ ; économies 12,1 Md€ et fraude 5,5 Md€, total 17,5 Md€ au tableau ; dépenses nouvelles 22 Md€ ; effort net 24 Md€, « 0,8 point de PIB de déficit public en moins » ; surplus de croissance de 0,3 point affiché ; pas de cible de déficit en pourcentage du PIB) ; axe 4 (CSG progressive pour les revenus sous 2 700 € par mois, financée par une « CSG sur les héritages très élevés » ; Smic à 1 700 € net et conférence sociale ; taxe Zucman ; taxe sur les géants du numérique ; IS réduit pour les PME) ; axe 5 (sécurité civile doublée, 1 Md€) ; loi intégrale (3 Md€) ; services publics (mutuelle publique gratuite 18-25 ans, 19 élèves par classe). Chiffres à reprendre de la page même aux étapes suivantes. La page web est aussi archivée en section f ([C-PS-84]).

---

## e. PPL, PPLO, PPLC, PPRE, amendements et motions du groupe SOC (priorité 5)

Sélection : textes **dont le premier signataire était membre du groupe SOC à la date du dépôt** (croisement du jeu open data « Dossiers législatifs », téléchargé le 2026-10-27, avec l'historique des mandats de groupe du jeu AMO30), choisis par axe sur leur objet. Le jeu de données compte **213 textes** (178 PPL, PPLO ou PPLC et 35 propositions de résolution) déposés par un premier signataire SOC sur la législature au 2026-10-27 (comptage par nos soins). Aucune PPL du groupe sur l'abrogation de la réforme des retraites, l'ISF, la proportionnelle ou le 49.3 n'apparaît dans ce jeu pour la XVIIe législature (voir « Trous »). Statuts relevés dans les actes des dossiers au 2026-10-27 ; un texte sans acte de séance est noté « déposé, en commission ». PDF des textes : `https://www.assemblee-nationale.fr/dyn/opendata/<identifiant>.pdf`. Les motions de censure ne sont pas téléchargeables sur le site de l'Assemblée (erreur 404 aux adresses open data, comme pour LFI) : leur texte est pris sur le site du parti.

**Journées réservées du groupe SOC** (d'après les dates de séance des dossiers et les dossiers de presse) : 23 janvier 2025 (huit PPL annoncées ; en séance : n° 516 rénovation énergétique, sans décision ; n° 517 crèches privées, n° 518 pannes d'ascenseurs, n° 519 repas à 1 € pour les étudiants, n° 522 vie chère outre-mer, adoptées) ; 11 décembre 2025 (onze PPL annoncées ; adoptées : n° 1799 renouvellement des titres de séjour, n° 1831 avocat pour l'enfant, n° 1909 innovation thérapeutique, n° 2021 mineurs isolés, n° 2028 vie chère outre-mer dans les services, n° 2039 rapports locatifs). Aucune date de journée réservée postérieure au 2026-10-27 n'a été trouvée.

### [C-PS-34] Dossier de presse et page de la niche du 23 janvier 2025
- Auteur : groupe Socialistes et apparentés
- Date : page du 2024-11-28 ; PDF créé le 2025-01-21
- Nature : dossier de presse, 24 pages ; page web (huit PPL, bilan des lois adoptées lors des journées réservées précédentes)
- URL : https://parti-socialiste.fr/wp-content/uploads/2024/11/Niche25_DossierDePresseVDef-1.pdf ; https://parti-socialiste.fr/vie-parlementaire/niche-parlementaire-socialiste-rendez-vous-le-23-janvier/
- Archivage : PDF archivé, `corpus/C-PS-34-dossier-presse-niche-2025-01-23-2026-10-27.pdf` (18,2 Mo ; encodage des polices qui rend l'extraction de texte inutilisable) ; texte archivé de la page, `corpus/C-PS-34-niche-2025-01-23-page-2026-10-27.md`
- Statut : groupe parlementaire
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (vie chère, [C-PS-49]) ; Q6 bloc c (usage des journées réservées).

### [C-PS-35] Dossier de presse et page de la niche du 11 décembre 2025 (« Protéger les droits, protéger les Français·es »)
- Auteur : groupe Socialistes et apparentés
- Date : PDF créé le 2025-12-10 ; page du 2025-11-28
- Nature : dossier de presse, 28 pages (onze PPL) ; page web
- URL : https://parti-socialiste.fr/wp-content/uploads/2025/11/Niche-dossier-de-presse_VSeance-5.pdf ; https://parti-socialiste.fr/vie-parlementaire/proteger-les-droits-proteger-les-francais%c2%b7es-niche-parlementaire-socialiste-du-11-decembre-2025/
- Archivage : PDF archivé, `corpus/C-PS-35-dossier-presse-niche-2025-12-11-2026-10-27.pdf` (16,8 Mo) ; texte archivé de la page, `corpus/C-PS-35-niche-2025-12-11-page-2026-10-27.md`. Le fichier `2026/06/Niche-dossier-de-presse_VSeance.pdf` du site est le même document (même taille, même date de création).
- Statut : groupe parlementaire
- Étiquette : source du parti, partie prenante
- Utile pour : axes 3 ([C-PS-44], [C-PS-45]), 4, 6 ([C-PS-65]) ; Q6 bloc c.

### Axe 1 : Finances publiques et dette

### [C-PS-36] Motion de rejet préalable du PLF 2027 (Boris Vallaud), scrutin n° 8707
- Auteur : Boris Vallaud et le groupe SOC (défendue en séance par Estelle Mercier selon le compte rendu, fiche [C-PS-88] de la section f)
- Date : 2026-10-13 (deuxième séance)
- Nature : motion de procédure (pas de texte écrit déposé) ; rejetée par 236 voix contre 149 (page du scrutin)
- URL : https://www.assemblee-nationale.fr/dyn/17/scrutins/8707 ; compte rendu : https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-mardi-13-octobre-2026
- Archivage : lien seul (le discours est archivé en texte par le second sous-agent, [C-PS-88])
- Statut : groupe parlementaire ; scrutin gelé 8707 (axe 1)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 1 (scrutin gelé) ; Q6 bloc c.

### [C-PS-37] PPL n° 2780 « taxation des bénéfices exceptionnels liés aux crises »
- Auteur : Boris Vallaud (premier signataire) et le groupe SOC
- Date : dépôt 2026-05-12
- Nature : PPL, 10 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/taxation_benefices_exceptionnels_lies_aux_crises_16e
- Archivage : PDF archivé, `corpus/C-PS-37-ppl-2780-taxation-benefices-exceptionnels-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1 et 4 (recettes).

### Axe 2 : Travail, protection sociale et fraude

### [C-PS-38] Motion de censure contre le gouvernement Bayrou sur les retraites (26 juin 2025)
- Auteur : Boris Vallaud (premier signataire, identifiant open data MIONANR5L17-N11) et le groupe SOC ; communiqué du parti du 24 juin 2025
- Date : 2025-06-26
- Nature : texte de la motion (article 49, alinéa 2) : rupture de l'engagement du Premier ministre d'un « dernier mot » au Parlement sur les retraites après l'échec du « conclave »
- URL : https://parti-socialiste.fr/vie-parlementaire/nous-deposons-une-motion-de-censure-contre-le-gouvernement-de-francois-bayrou/ ; https://parti-socialiste.fr/communiques-de-presse/francois-bayrou-trahit-sa-parole-sur-les-retraites-le-parti-socialiste-depose-une-motion-de-censure/
- Archivage : texte archivé, `corpus/C-PS-38-motion-censure-bayrou-retraites-2025-06-26-2026-10-27.md` ; PDF de l'Assemblée introuvable (erreur 404)
- Statut : groupe parlementaire ; sort à relever dans le scrutin correspondant
- Étiquette : source du parti, partie prenante
- Utile pour : axe 2 (retraites) ; Q6 bloc c ; actes de négociation 2025.

### [C-PS-39] PPL n° 3267 : ASPA au niveau du seuil de pauvreté et versement automatique
- Auteur : Gérard Leseul (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 6 pages (ASPA au moins égale au seuil de pauvreté monétaire de l'Insee ; versement automatique sauf refus)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/revaloriser_aspa_automaticite_versement_17e
- Archivage : PDF archivé, `corpus/C-PS-39-ppl-3267-aspa-seuil-pauvrete-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 2 (minimum vieillesse, non-recours).

### [C-PS-40] PPL n° 1318 « lutter contre le non-recours aux droits sociaux »
- Auteur : Sandrine Runel (première signataire) et le groupe SOC
- Date : dépôt 2025-04-17
- Nature : PPL, 8 pages (maintien des démarches papier ; partage des données entre administrations pour ouvrir les droits)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/lutter_contre_non_recours_droits_sociaux_17e
- Archivage : PDF archivé, `corpus/C-PS-40-ppl-1318-non-recours-droits-sociaux-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 2 (prestations, à mettre en regard de la fraude sociale).

### Axe 3 : Immigration, intégration, droits sociaux des étrangers

### [C-PS-41] PPL n° 3253 « régulariser les travailleurs sans-papiers »
- Auteur : Paul Christophle (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 4 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/regulariser_travailleurs_sans_papiers_17e
- Archivage : PDF archivé, `corpus/C-PS-41-ppl-3253-regularisation-travailleurs-sans-papiers-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3 (régularisation par le travail, à comparer au projet [C-PS-01] et aux positions de candidats à la primaire, section f).

### [C-PS-42] PPL n° 3266 : carte de séjour pluriannuelle pour les étrangers travaillant dans un métier essentiel ou en tension
- Auteur : Céline Hervieu (première signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 9 pages (titre de plein droit d'une durée maximale de quatre ans, en remplacement de l'admission exceptionnelle au séjour expérimentale qui court jusqu'au 31 décembre 2026)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/regulariser_metier_essentiel_tension_17e
- Archivage : PDF archivé, `corpus/C-PS-42-ppl-3266-carte-sejour-metiers-essentiels-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3.

### [C-PS-43] PPL n° 3259 « rétablir un régime de protection contre les OQTF »
- Auteur : Marc Pena (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 5 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/retablir_regime_protection_oqtf_17e
- Archivage : PDF archivé, `corpus/C-PS-43-ppl-3259-protections-oqtf-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3 (éloignements ; retour sur la loi de 2024).

### [C-PS-44] PPL n° 1799 « garantir un renouvellement automatique des titres de séjour de longue durée »
- Auteur : Fatiha Keloua Hachi (première signataire) et le groupe SOC
- Date : dépôt 2025-09-16 ; discutée le 2025-12-11 (journée réservée)
- Nature : PPL, 4 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/renouvellement_automatique_titres_sejour_longue_duree_17e
- Archivage : PDF archivé (texte déposé), `corpus/C-PS-44-ppl-1799-renouvellement-titres-sejour-2026-10-27.pdf`
- Statut : groupe parlementaire ; **adoptée en première lecture**, transmise au Sénat le 2025-12-12
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3 (mesure reprise dans le projet [C-PS-01]).

### [C-PS-45] PPL n° 2021 « protéger les mineurs isolés et lutter contre le sans-abrisme »
- Auteur : Emmanuel Grégoire (premier signataire) et le groupe SOC
- Date : dépôt 2025-10-28 ; discutée le 2025-12-11
- Nature : PPL, 8 pages (présomption de minorité, recours suspensif, maintien de l'accueil provisoire)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/proteger_mineurs_isoles_lutter_sans_abrisme_17e
- Archivage : PDF archivé (texte déposé), `corpus/C-PS-45-ppl-2021-mineurs-isoles-sans-abrisme-2026-10-27.pdf`
- Statut : groupe parlementaire ; **adoptée en première lecture**, transmise au Sénat le 2025-12-11
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3.

### [C-PS-46] PPLC n° 3348 « inscrire l'aide médicale de l'État dans la Constitution »
- Auteur : Paul Christophle (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-19
- Nature : PPLC
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/aide_medicale_etat_constitution
- Archivage : lien seul (texte pas encore publié en PDF : erreur 404 le 2026-10-27)
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 3 (AME). À télécharger à la boucle de révision.

### [C-PS-47] PPRE n° 2508 : s'opposer à la révision de la directive « retour » et mettre en œuvre le pacte asile et migration de façon respectueuse des droits
- Auteur : Paul Christophle (premier signataire) et le groupe SOC
- Date : dépôt 2026-02-18
- Nature : proposition de résolution européenne, 12 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/opposer_revision_directive_retour_assurer_meo_Pacte_asile_migration_respectueuse_dignite_humaine_conforme_obligations_francaises_europeennes_droits_humains
- Archivage : PDF archivé, `corpus/C-PS-47-ppre-2508-directive-retour-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axes 3 et 6 (droit de l'Union).

### Axe 4 : Pouvoir d'achat et fiscalité

### [C-PS-48] PPL n° 3252 « augmenter massivement et immédiatement la rémunération des travailleuses et travailleurs »
- Auteur : Boris Vallaud (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 11 pages (baisse ciblée de la CSG sur les revenus d'activité, coût de 15 Md€ selon l'exposé, compensée par une réforme de la fiscalité des héritages, 10 Md€, et d'autres recettes)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/_augmenter_massivement_et_immediatement_la_remuneration_des_travailleuses_et_travailleurs_17e
- Archivage : PDF archivé, `corpus/C-PS-48-ppl-3252-remuneration-travailleurs-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (traduction législative de la priorité n° 1 du contre-budget 2027 [C-PS-33]).

### [C-PS-49] PPL n° 522 « mesures d'urgence contre la vie chère et régulation de la concentration des acteurs économiques » (outre-mer)
- Auteur : Boris Vallaud (premier signataire) et le groupe SOC
- Date : dépôt 2024-10-29 ; discutée le 2025-01-23
- Nature : PPL, 11 pages (bouclier qualité prix effectif, prix alignés sur la moyenne hexagonale pour les biens de première nécessité)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/mesures_urgence_vie_chere_outre_mer
- Archivage : PDF archivé (texte déposé), `corpus/C-PS-49-ppl-522-vie-chere-outre-mer-2026-10-27.pdf`
- Statut : groupe parlementaire ; **adoptée en première lecture** le 2025-01-23, transmise au Sénat
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (prix).

### [C-PS-50] PPL n° 3269 « baisser les prix du carburant à la pompe par l'encadrement des marges des raffineurs »
- Auteur : Mélanie Thomin (première signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 9 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/baisser_prix_carburants_encadrement_marges_raffineurs_17e
- Archivage : PDF archivé, `corpus/C-PS-50-ppl-3269-marges-raffineurs-carburant-2026-10-27.pdf`
- Statut : groupe parlementaire ; en commission (réunions inscrites le 2026-10-27 et le 2026-11-10)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (énergie).

### [C-PS-51] PPL n° 3271 « instaurer un barème progressif de l'impôt sur les sociétés »
- Auteur : Gérard Leseul (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 6 pages (barème progressif à la place du taux de 25 %)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/bareme_progressf_impot_societes_17e
- Archivage : PDF archivé, `corpus/C-PS-51-ppl-3271-bareme-progressif-impot-societes-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axes 4 et 1 (mesure du projet [C-PS-01]).

### [C-PS-52] Amendement n° I-471 au PLF 2027 (« impôt plancher sur la fortune », taxe Zucman)
- Auteur : Mickaël Bouloux et les membres du groupe SOC
- Date : 2026-10-08
- Nature : amendement après l'article 4 : impôt plancher sur les patrimoines supérieurs à 100 M€, 7 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/AN/471.pdf
- Archivage : PDF archivé, `corpus/C-PS-52-amdt-I-471-plf-2027-impot-plancher-fortune-2026-10-27.pdf`
- Statut : groupe parlementaire ; sort : rejeté
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (taxe Zucman 2027) ; déclaration associée en section f ([C-PS-89]).

### [C-PS-53] Amendement n° I-CF384 au PLF 2027 (article 2)
- Auteur : Estelle Mercier, Boris Vallaud et les membres du groupe SOC
- Date : 2026-10-02 (commission des finances)
- Nature : amendement : supprime de l'article 2 la fiscalisation de certaines indemnités journalières (accidents du travail, affections de longue durée) et la hausse de l'exonération de la prime carburant, en conservant l'indexation du barème
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/CION_FIN/CF384.pdf
- Archivage : PDF archivé, `corpus/C-PS-53-amdt-I-CF384-plf-2027-article-2-2026-10-27.pdf`
- Statut : groupe parlementaire ; sort : **adopté** en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axes 2 et 4 (arrêts maladie, fiscalité des indemnités).

### Axe 5 : Sécurité, ordre public et libertés

### [C-PS-54] PPL n° 1091 « préciser et contrôler les conditions d'ouverture du feu par la police nationale »
- Auteur : Roger Vicot (premier signataire) et le groupe SOC
- Date : dépôt 2025-03-11
- Nature : PPL, 9 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/conditions_ouverture_feu_police_nationale_17e
- Archivage : PDF archivé, `corpus/C-PS-54-ppl-1091-ouverture-du-feu-police-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (usage des armes ; à comparer à la PPL d'abrogation de LFI, hors périmètre).

### [C-PS-55] PPL n° 1795 « expérimentation des brigades de tranquillité publique de la police nationale »
- Auteur : Roger Vicot (premier signataire) et le groupe SOC
- Date : dépôt 2025-09-16
- Nature : PPL, 11 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/experimentation_brigades_tranquillite_publique_17e
- Archivage : PDF archivé, `corpus/C-PS-55-ppl-1795-brigades-tranquillite-publique-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (police de proximité).

### [C-PS-56] PPL n° 1841 « encadrer le recours aux contrôles d'identité »
- Auteur : Paul Christophle (premier signataire) et le groupe SOC
- Date : dépôt 2025-09-16
- Nature : PPL, 8 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/encadrer_recours_controle_identite_17e
- Archivage : PDF archivé, `corpus/C-PS-56-ppl-1841-controles-identite-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (contrôles d'identité, récépissés).

### [C-PS-57] PPL n° 3321 « protéger les mineurs en interdisant l'utilisation des armes mutilantes et des techniques d'immobilisation létale dans les manifestations »
- Auteur : Boris Vallaud (premier signataire) et le groupe SOC
- Date : dépôt 2026-10-13
- Nature : PPL, 6 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/_proteger_les_mineurs_en_interdisant_l_utilisation_des_armes_mutilantes_et_des_techniques_d_immobilisation_letale_dans_les_manifestations_17e
- Archivage : PDF archivé, `corpus/C-PS-57-ppl-3321-armes-mutilantes-mineurs-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (maintien de l'ordre, manifestations d'octobre 2026 ; voir aussi la déclaration du 19 octobre 2026 en section f, [C-PS-90]).

### [C-PS-58] « Loi intégrale » contre les violences sexistes et sexuelles : PPL n° 2169, PPL n° 3106 et PPLO n° 3107
- Auteur : Céline Thiébault-Martinez (première signataire) et le groupe SOC
- Date : PPL n° 2169 déposée le 2025-12-02 (première version) ; PPL n° 3106 et PPLO n° 3107 déposées le 2026-08-11, discutées le 2026-10-13
- Nature : PPL n° 2169 (70 pages), PPL n° 3106 (121 pages, version examinée), PPLO n° 3107 (6 pages, adaptation de l'autorité judiciaire)
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/apporter_reponse_integrale_phenomene_violences_sexuelles_sexistes_contre_femmes_enfants_17e ; https://www.assemblee-nationale.fr/dyn/17/dossiers/adapter_autorite_judiciaire_lutte_contre_violences_sexuelles_intrafamiliales_17e ; https://www.assemblee-nationale.fr/dyn/17/dossiers/_lutter_contre_violences_sexistes_et_sexuelles_commises_contre_femmes_et_enfants_17e
- Archivage : PDF archivés (textes déposés), `corpus/C-PS-58-ppl-2169-loi-integrale-vss-v1-2026-10-27.pdf`, `corpus/C-PS-58-ppl-3106-loi-integrale-vss-2026-10-27.pdf`, `corpus/C-PS-58-pplo-3107-autorite-judiciaire-vss-2026-10-27.pdf`
- Statut : groupe parlementaire ; PPL n° 3106 et PPLO n° 3107 **adoptées en première lecture le 2026-10-13** et transmises au Sénat (adoption « à l'unanimité » selon le parti, page du 2026-10-15) ; PPL n° 2169 restée en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 5 (justice, police) ; hors grille (droits des femmes) ; financement de 3 Md€ dans le contre-budget 2027 [C-PS-33].

### Axe 6 : Institutions, démocratie et Europe

### [C-PS-59] PPLC n° 2001 « établir un meilleur équilibre entre pouvoirs constitutionnels »
- Auteur : Marietta Karamanli (première signataire) et le groupe SOC
- Date : dépôt 2025-10-23
- Nature : PPLC, 7 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/etablir_meilleur_equilibre_entre_pouvoirs_constitutionnels_17e
- Archivage : PDF archivé, `corpus/C-PS-59-pplc-2001-equilibre-pouvoirs-constitutionnels-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (équilibre des pouvoirs, 49.3 éventuel, à lire à l'étape 2) ; Q6 bloc a.

### [C-PS-60] PPLC n° 3215 : étendre aux membres du gouvernement l'interdiction du cumul avec une fonction exécutive locale
- Auteur : Anna Pic (première signataire) et le groupe SOC
- Date : dépôt 2026-10-05
- Nature : PPLC, 4 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/etendre_membres_Gouvernement_interdiction_cumul_fonction_executive_locale_17e
- Archivage : PDF archivé, `corpus/C-PS-60-pplc-3215-cumul-ministres-executif-local-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6.

### [C-PS-61] PPL n° 3263 : inscription automatique et continue des citoyens sur les listes électorales
- Auteur : Anna Pic (première signataire) et le groupe SOC
- Date : dépôt 2026-10-06
- Nature : PPL, 6 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/inscription_automatique_continue_citoyens_listes_electorales_17e
- Archivage : PDF archivé, `corpus/C-PS-61-ppl-3263-inscription-automatique-listes-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (participation électorale).

### [C-PS-62] PPL n° 2031 : droit de vote à seize ans aux élections municipales
- Auteur : Céline Hervieu (première signataire) et le groupe SOC
- Date : dépôt 2025-10-28
- Nature : PPL, 7 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/instaurer_droit_vote_seize_ans_elections_municipales_17e
- Archivage : PDF archivé, `corpus/C-PS-62-ppl-2031-vote-16-ans-municipales-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6.

### [C-PS-63] PPL n° 1935 : prévenir la concentration des médias, protéger leur liberté éditoriale et renforcer le pluralisme
- Auteur : Emmanuel Grégoire (premier signataire) et le groupe SOC
- Date : dépôt 2025-10-14
- Nature : PPL, 7 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/prevenir_concentration_medias_proteger_liberte_editioriale_renforcer_pluralisme_17e
- Archivage : PDF archivé, `corpus/C-PS-63-ppl-1935-concentration-medias-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (médias).

### [C-PS-64] PPLO n° 1116 : obligations déontologiques des membres du Conseil constitutionnel
- Auteur : Marietta Karamanli (première signataire) et le groupe SOC
- Date : dépôt 2025-03-14
- Nature : PPLO, 17 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/obligations_deontologiques_conseil_constitutionnel
- Archivage : PDF archivé, `corpus/C-PS-64-pplo-1116-deontologie-conseil-constitutionnel-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (juridictions, état de droit).

### [C-PS-65] PPLC n° 2000 : création d'un Défenseur de la laïcité et définition de ce principe
- Auteur : Jérôme Guedj (premier signataire) et le groupe SOC
- Date : dépôt 2025-10-23 ; rapport de commission le 2025-12-03
- Nature : PPLC, 6 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/creation_defenseur_laicite_et_definition_de_ce_principe_17e_
- Archivage : PDF archivé, `corpus/C-PS-65-pplc-2000-defenseur-laicite-2026-10-27.pdf`
- Statut : groupe parlementaire ; examinée en commission (rapport déposé), pas d'acte de séance relevé
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (laïcité) ; hors grille.

### [C-PS-66] PPRE n° 3180 : moyens financiers, industriels et politiques de l'Union européenne (infrastructure satellitaire)
- Auteur : Marietta Karamanli (première signataire) et le groupe SOC
- Date : dépôt 2026-09-17
- Nature : proposition de résolution européenne, 10 pages
- URL : https://www.assemblee-nationale.fr/dyn/17/dossiers/infrastructure_satellitaire_vocation_europeenne_17e
- Archivage : PDF archivé, `corpus/C-PS-66-ppre-3180-moyens-union-europeenne-2026-10-27.pdf`
- Statut : groupe parlementaire ; déposée, en commission
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (Europe, souveraineté).

### [C-PS-67] Motion de censure contre le gouvernement Barnier (4 octobre 2024, texte commun du NFP)
- Auteur : Boris Vallaud (premier signataire, identifiant open data MIONANR5L17-N1), Mathilde Panot, Cyrielle Chatelain, André Chassaigne « et 188 de leurs collègues »
- Date : 2024-10-04
- Nature : texte de la motion (article 49, alinéa 2) : deux motifs, dont la « négation du résultat » des législatives de 2024
- URL : https://parti-socialiste.fr/vie-parlementaire/nous-deposons-une-motion-de-censure-contre-le-gouvernement-barnier/
- Archivage : texte archivé, `corpus/C-PS-67-motion-censure-barnier-2024-10-04-2026-10-27.md` ; PDF de l'Assemblée introuvable (erreur 404)
- Statut : groupe parlementaire, texte commun du NFP ; sort à relever dans le scrutin correspondant
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 ; Q6 bloc c.

### [C-PS-68] Position des députés socialistes sur la proposition de destitution du président de la République
- Auteur : groupe Socialistes et apparentés
- Date : 2024-09-17
- Nature : page web (position du groupe sur la procédure de l'article 68 engagée par LFI)
- URL : https://parti-socialiste.fr/vie-parlementaire/motion-de-destitution-la-position-des-depute-es-socialistes/
- Archivage : texte archivé, `corpus/C-PS-68-position-groupe-motion-destitution-2024-09-17-2026-10-27.md`
- Statut : groupe parlementaire
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (institutions) ; divergence possible avec LFI à documenter.

---

## Mandat exercé (règle §6 v2) : programme présidentiel de 2012

### [C-PS-69] François Hollande, « Le changement c'est maintenant. Mes 60 engagements pour la France »
- Auteur : François Hollande, candidat du PS
- Date : PDF créé le 2012-01-26 (programme présenté le 26 janvier 2012)
- Nature : programme présidentiel, 23 pages
- URL : http://francoishollande.fr/assets/Uploads/Projet_presidentiel_Francois_Hollande.pdf ; archive : https://web.archive.org/web/20120130232757/http://francoishollande.fr:80/assets/Uploads/Projet_presidentiel_Francois_Hollande.pdf
- Archivage : PDF archivé, `corpus/C-PS-69-hollande-2012-60-engagements-2026-10-27.pdf` (0,6 Mo)
- Statut : programme officiel du mandat exercé (2012-2017)
- Étiquette : source du parti, partie prenante
- Utile pour : comparaison programme / actes sur 2012-2017 (pondérée par l'ancienneté) ; exemples : départ à 60 ans pour les carrières longues, 60 000 postes dans l'éducation, réduction de la part du nucléaire, mariage et adoption pour les couples de même sexe, droit de vote des étrangers aux élections locales, « part de proportionnelle » à l'Assemblée, déficit ramené à 3 % du PIB en 2013 et équilibre budgétaire en fin de mandat (à reprendre de la page même) ; Q6 bloc b.

### [C-PS-70] Profession de foi de François Hollande, premier tour 2012
- Auteur : François Hollande
- Date : PDF créé le 2012-04-06
- Nature : profession de foi, 2 pages
- URL : http://francoishollande.fr/assets/Uploads/professiondefoi.pdf ; archive : https://web.archive.org/web/20120418173034/http://francoishollande.fr/assets/Uploads/professiondefoi.pdf
- Archivage : PDF archivé, `corpus/C-PS-70-hollande-2012-profession-de-foi-t1-2026-10-27.pdf` (7,3 Mo)
- Statut : programme officiel (document électoral)
- Étiquette : source du parti, partie prenante
- Utile pour : engagements mis en avant devant les électeurs en 2012.

---

## f. Déclarations publiques depuis le 1er janvier 2026 (priorité 6)

23 déclarations : communiqués et résolutions du Parti socialiste 6 (dont un cosigné avec les deux groupes parlementaires), textes du groupe Socialistes et apparentés publiés sur parti-socialiste.fr 2, interventions en séance au nom du groupe 4 (Laurent Baumel, Sandrine Runel, Estelle Mercier, Mickaël Bouloux), Boris Vallaud 3, conférence de presse du groupe 1, lettre de Boris Vallaud, Patrick Kanner et Johanna Rolland 1, Raphaël Glucksmann 4 (deux comme candidat avant la primaire, deux comme candidat désigné), Olivier Faure comme candidat à la primaire 2 (déclarations individuelles retenues parce que deux de leurs mesures figurent dans des documents du parti ou du groupe selon la note de paysage : Smic à 1 700 euros net, titre de séjour après six mois de contrat). Chaque déclaration a sa fiche texte dans `corpus/` (date, locuteur, qualité, média, format, axe, URL ouverte, date de consultation, position en paraphrase, citations de 15 mots au plus) ; neuf fiches contiennent en plus la copie de la page du parti ou du candidat. « Site du parti » : texte publié sur parti-socialiste.fr (partie prenante). « Candidat » : texte du site de campagne. « Relais » : reprise par un média tiers, le média d'origine est indiqué. « Compte rendu de l'AN » : source primaire. Aucune déclaration de Patrick Kanner seul, de Jérôme Guedj, de Ségolène Royal, d'Emmanuel Maurel ou de Karim Bouamrane n'a été retenue (voir Trous).

| ID | Date | Média d'origine | Format | Axe | Position (résumé) | URL |
|---|---|---|---|---|---|---|
| C-PS-71 | 2026-01-08 | parti-socialiste.fr | communiqué | 6 | La France doit voter contre l'accord UE-Mercosur au Conseil ; aucune clause de sauvegarde ne le rend acceptable ; saisine de la CJUE si nécessaire | https://parti-socialiste.fr/communiques-de-presse/la-france-doit-voter-contre-laccord-ue-mercosur-au-conseil-de-lunion-europeenne/ (site du parti) |
| C-PS-72 | 2026-01-23 | séance de l'AN (Laurent Baumel) | intervention en séance | 1, 2 et 6 | Le groupe ne vote pas la censure LFI après le 49.3 sur le PLF 2026 : budget « passable », suspension de la réforme des retraites, réindexation, prime d'activité ; défaite sur les hauts patrimoines reconnue | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/seance-du-vendredi-23-janvier-2026 (compte rendu de l'AN) |
| C-PS-73 | 2026-01-29 | franceinfo (Raphaël Glucksmann) | interview | 3 | Pas de « submersion » ; contrôle de l'immigration irrégulière et exécution des OQTF ; immigration de travail, étudiante et asile défendues ; migrations « pendulaires » contre laissez-passer consulaires | https://www.lagazettefrance.fr/article/immigration-glucksmann-prone-le-controle-mais-refute-toute-submersion (relais AFP, candidat avant la primaire) |
| C-PS-74 | 2026-02-24 | parti-socialiste.fr | communiqué | 6 | Ukraine : bouclier anti-drones, avoirs russes gelés pour la reconstruction, majorité qualifiée dans l'Union sur la sécurité collective, réarmement industriel européen | https://parti-socialiste.fr/communiques-de-presse/quatre-ans-apres-lagression-russe-contre-lukraine-leurope-doit-franchir-un-cap/ (site du parti) |
| C-PS-75 | 2026-03-31 | parti-socialiste.fr (bureau national) | résolution | 4 et 6 | Moyen-Orient (cessez-le-feu au Liban, suspension de l'accord UE-Israël) ; carburants : chèque énergie, réserves stratégiques, refus de la baisse de TVA du RN, surtaxes pétrolières rendues aux ménages | https://parti-socialiste.fr/communiques-de-presse/resolution-du-bureau-national-du-31-mars-2026/ (site du parti) |
| C-PS-76 | 2026-04-07 | séance de l'AN (Sandrine Runel) | intervention en séance | 2 | Vote contre le projet de loi fraudes : volet fiscal « coquille vide », fraude sociale 2 Md€ contre fraude fiscale 100 Md€, refus des sanctions automatiques et suspensions sur suspicion | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-mardi-07-avril-2026 (compte rendu de l'AN) |
| C-PS-77 | 2026-05-19 | parti-socialiste.fr (vie parlementaire) | communiqué | 1 et 6 | Vote pour l'actualisation de la LPM (+36 Md€), sans affaiblir les services publics ; nouvelles recettes « justement réparties » | https://parti-socialiste.fr/vie-parlementaire/les-nouveaux-credits-accordes-aux-armees-sont-indispensables-mais-ils-ne-peuvent-en-aucun-cas-etre-un-pretexte-a-laffaiblissement-des-services-publics/ (site du parti) |
| C-PS-78 | 2026-05-26 | livre « Nous avons encore envie » (Raphaël Glucksmann), extraits au Nouvel Obs | livre | 2, 3, 4, 5 et 6 | Convention citoyenne sur l'immigration, service civique obligatoire, sécurité « axe majeur », suppression du veto et grand emprunt européens, retraites selon l'espérance de vie en bonne santé | https://lcp.fr/actualites/presidentielle-raphael-glucksmann-devoile-les-premieres-lignes-de-son-possible-programme (relais, candidat avant la primaire) |
| C-PS-79 | 2026-07-03 | Fondation Jean-Jaurès (Boris Vallaud) | note | 1 et 6 | Scrutin proportionnel, régime « primo-ministériel » (dissolution par le Premier ministre, censure constructive), contrat de législature avant candidature commune | https://www.jean-jaures.org/publication/souvenirs-pour-demain-de-lexercice-de-lopposition-a-lexercice-du-pouvoir/ (texte de l'auteur ; relais LCP) |
| C-PS-80 | 2026-09-16 | Le Nouvel Obs (Olivier Faure) | interview | 2, 3, 4 et 5 | Candidat à la primaire : Smic à 1 700 € net, retraite à 62 ans, faire cotiser l'IA, régularisation massive, contrôles au faciès | https://www.lagazettefrance.fr/article/smic-a-1-700-euros-regularisation-des-travailleurs-sans-papiers-retraites-faure-developpe-ses-propositions (relais AFP) |
| C-PS-82 | 2026-09-16 | conférence de presse du groupe (Estelle Mercier, Sandrine Runel) | conférence de presse | 1, 2 et 4 | Contre-budget 2027 : 39,5 Md€ de recettes (Zucman 15, CSG héritages 10, numérique 10), CSG progressive, 12,1 Md€ d'économies, refus de la désindexation des pensions, pas de pacte de non-censure | https://lcp.fr/actualites/budget-a-l-assemblee-les-socialistes-presentent-leurs-propositions-et-previennent-qu-ils (relais) |
| C-PS-81 | 2026-09-17 | BFMTV (Olivier Faure) | interview | 3 | Candidat à la primaire : régulariser « autour de 400 000 » travailleurs sans papiers, modèle espagnol | https://www.publicsenat.fr/actualites/politique/immigration-a-quoi-correspond-la-proposition-dolivier-faure-de-regulariser-400-000-travailleurs-sans-papiers (relais) |
| C-PS-83 | 2026-09-22 | Public Sénat (Boris Vallaud) | déclaration rapportée | 1 et 4 | Budget 2027 « provocation », risque de récession ; taxer les pétroliers, encadrer les marges, hausse du chèque énergie | https://www.publicsenat.fr/actualites/politique/budget-2027-boris-vallaud-ps-denonce-un-budget-qui-risque-de-nous-enfoncer-dans-la-crise (relais) |
| C-PS-84 | 2026-09-24 | parti-socialiste.fr (Mercier, Runel, Vallaud) | tribune signée | 1 et 4 | Sept priorités budgétaires : salaires par baisse de CSG, climat, agriculteurs, violences sexistes, services publics, PME ; Zucman, héritages, numérique, fraude, niches « tout en réduisant le déficit » | https://parti-socialiste.fr/vie-parlementaire/les-7-priorites-des-socialistes-pour-le-budget-2027/ (site du parti) |
| C-PS-85 | 2026-10-02 | lettre au Premier ministre (Vallaud, Kanner, Rolland) | lettre | 1, 3 et 4 | Budget 2027 « pas acceptable » en l'état ; lettre rectificative demandée ; critique de la « préférence nationale » dans certaines prestations ; volonté de compromis | https://lcp.fr/actualites/budget-2027-les-plus-modestes-continuent-de-payer-pour-les-plus-riches-denoncent-les (relais) |
| C-PS-86 | 2026-10-02 | parti-socialiste.fr | communiqué | 5 | Mobilisation lycéenne : entendre les syndicats, liberté de manifester, LBD contre des lycéens « intolérables », violences condamnées | https://parti-socialiste.fr/communiques-de-presse/le-parti-socialiste-appelle-le-gouvernement-a-entendre-les-revendications-legitimes-des-representants-syndicaux/ (site du parti) |
| C-PS-87 | 2026-10-11 | discours au Solaris et France 2 (Raphaël Glucksmann) | discours et interview | 6 | Candidat désigné : « candidat du Parti socialiste », rupture avec le macronisme et avec LFI, « pas d'accord avec LFI » | https://www.publicsenat.fr/actualites/politique/ce-soir-la-bataille-de-france-commence-apres-sa-victoire-a-la-primaire-de-la-gauche-raphael-glucksmann-assure-que-rien-ne-le-fera-l (relais, candidat désigné) |
| C-PS-88 | 2026-10-13 | séance de l'AN (Estelle Mercier) | intervention en séance | 1, 2 et 4 | Motion de rejet du PLF 2027 : 21 Md€ d'effort sur les ménages, aucune contribution des hauts patrimoines, « une sommation » ; rejetée 236 contre 149 | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-mardi-13-octobre-2026 (compte rendu de l'AN) |
| C-PS-89 | 2026-10-16 | séance de l'AN (Mickaël Bouloux) | intervention en séance | 4 | Amendement n° 471 : plancher de 2 % au-delà de 100 M€ de patrimoine net, environ 1 800 foyers, 15 à 25 Md€ ; rejeté 68 contre 35 | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-vendredi-16-octobre-2026 (compte rendu de l'AN) |
| C-PS-90 | 2026-10-19 | parti-socialiste.fr (parti et deux groupes) | communiqué | 4 et 5 | « Faillite du maintien de l'ordre » le 17 octobre ; commission d'enquête, droit de manifester, interdiction des armes mutilantes contre les mineurs ; salaires, marges des raffineurs, abrogation de Parcoursup | https://parti-socialiste.fr/actualites/entendre-la-colere-sociale-garantir-le-droit-de-manifester-proteger-les-personnes-et-les-biens/ (site du parti) |
| C-PS-91 | 2026-10-21 | LCP (Boris Vallaud) | interview rapportée | 5 | Projet de loi « casseurs-payeurs » : « une mauvaise loi » ; sénateurs PS réservent leur vote | https://www.lagazettefrance.fr/article/casseurs-payeurs-apres-les-violences-du-17-octobre-la-reponse-legislative-au-senat (relais AFP) |
| C-PS-92 | 2026-10-23 | parti-socialiste.fr | communiqué | 5 | Fusillades de Trappes et La Verrière : solidarité, nature raciste à reconnaître si confirmée, moyens pour le renseignement, la police et la justice | https://parti-socialiste.fr/communiques-de-presse/avec-la-disparition-de-jean-paul-huchon-la-gauche-perd-un-compagnon-de-longue-route/ (site du parti ; adresse erronée, voir fiche) |
| C-PS-93 | non datée | glucks2027.fr | texte de site | 4 et 6 | Appel du candidat : vivre de son travail, école, rupture avec le macronisme, contre « trumpistes » et « poutinistes » | https://glucks2027.fr/ (candidat, candidat désigné) |

Fichiers : `corpus/C-PS-<nn>-<locuteur>-<objet>-<date de la déclaration>-2026-10-27.md` (pour [C-PS-93], `nd` à la place de la date).

Répartition par axe (une déclaration peut compter pour plusieurs) : axe 1 : 8 ; axe 2 : 6 ; axe 3 : 5 ; axe 4 : 11 ; axe 5 : 6 ; axe 6 : 9. L'axe 3 est le plus mince : sur cinq déclarations, une seule vient du parti ou du groupe ([C-PS-85], par relais, sur la « préférence nationale ») ; les quatre autres sont du candidat (avant la primaire) ou d'Olivier Faure comme candidat à la primaire. Aucun communiqué du parti sur l'immigration n'a été publié en 2026 sur parti-socialiste.fr (voir Trous).

Archivage (règle v2) : huit déclarations publiées sur parti-socialiste.fr ont leur page copiée dans la fiche ([C-PS-71], [C-PS-74], [C-PS-75], [C-PS-77], [C-PS-84], [C-PS-86], [C-PS-90], [C-PS-92]), textes relevés par l'interface publique de contenus du site (WordPress), césures invisibles retirées ; une neuvième copie est celle du site de campagne du candidat ([C-PS-93]). Quatre viennent du compte rendu intégral de l'Assemblée (version web, ouverte) ; une ([C-PS-79]) est le texte de l'auteur publié par la Fondation Jean-Jaurès (PDF ouvert, paraphrasé, pas copié : source engagée, pas une page du parti) ; neuf sont des relais de presse, tous ouverts (LCP 3, Public Sénat 3, dépêches AFP reprises par La Gazette France 3). Aucune position n'est tirée d'un résumé de moteur de recherche.

Intégration (2026-10-27, agent principal) : identifiants C-PS-71 à C-PS-93 attribués dans l'ordre du brouillon du second sous-agent (identifiants provisoires C-PS-F01 à C-PS-F23), fichiers renommés en conséquence ; aucune fiche de la section a ne double la page d'accueil du site de campagne [C-PS-93] ni le communiqué du 19 octobre [C-PS-90].

---

## Actes

Applicable : le PS a exercé le pouvoir national de mai 2012 à mai 2017. Renvoi : `00-perimetre.md`, section « Attribution des actes » (comparaison programme / actes de Q4 applicable sur 2012-2017, pondérée par l'ancienneté ; opposition depuis 2017 ; accords de non-censure de 2025 documentés comme actes de négociation [C-PS-28], [C-PS-32] ; Q6 : blocs a, b, c et d applicables, le bloc b sur 2012-2017). Programme du mandat exercé : [C-PS-69], [C-PS-70]. Les sources des actes 2012-2017 (lois votées, budgets exécutés, usages du 49.3, rapports de la Cour des comptes) sont à réunir aux étapes 3 à 5 ; aucune n'est archivée à cette étape.

---

## Trous

**Non trouvé**
- **Programme présidentiel du candidat** : non publié au 2026-10-27 (sites glucks2027.fr et place-publique.eu, presse ; annoncé en août « d'ici un mois, un mois et demi »).
- **Programme commun** prévu par la stratégie du 9 juillet et la charte de la primaire : aucune trace d'ouverture de négociation.
- **Texte de l'accord de désignation et de la « charte des valeurs communes »** (CN du PS et APN de Place publique du 25 août 2026) : non publié sur les sites des deux partis ; le site choisir2027.fr est hors ligne ; l'archive web ne contient que la page d'accueil, les pages des candidats, les professions de foi et les règles de vote.
- **Proclamation officielle des résultats de la primaire** par la COP : non trouvée (chiffres connus par la presse et par Place publique) ; aucun communiqué du PS sur le résultat.
- **Acte d'investiture du PS postérieur à la primaire** (CN, vote) : aucun trouvé.
- **PDF intégral du Projet socialiste** : non public (« consultable sur l'espace militant », édition imprimée en commande) ; le texte intégral est archivé à partir du site, partie par partie [C-PS-01]. Le nombre exact de propositions (« environ 600 » selon la presse) n'est pas publié ; le nombre de votants à la consultation du 25 juin non plus.
- **Texte d'orientation A « Le cœur de la gauche »** du congrès de Nancy (2025) et les textes B et C : non trouvés sur le site du parti ni dans la presse ouverte.
- **Texte de la convention « Sécurité et prévention de la délinquance »** (2025, plus de 160 propositions) : non trouvé.
- **Document des propositions budgétaires de Blois 2025** : non trouvé ; contenu connu par l'exposé de l'amendement n° 125 [C-PS-30] et par LCP [C-PS-29].
- **Communiqué des « conditions » de non-censure de la mi-octobre 2025** mentionné par LCP : non trouvé sur le site du parti.
- **Projet du PS pour 2012 « Le changement »** (adopté en mai 2011) : PDF non trouvé (index web.archive.org de parti-socialiste.fr trop volumineux pour être interrogé : erreur 504 ; recherche de presse sans lien vers le document).
- **Programme de la liste PS-Place publique aux européennes 2024** : PDF non trouvé [C-PS-21].
- **PPL du groupe SOC sur l'abrogation de la réforme des retraites, l'ISF, la proportionnelle ou le 49.3 dans la XVIIe législature** : aucune dans le jeu « Dossiers législatifs » avec un premier signataire SOC (une PPL d'abrogation des retraites existe pour la XVIe législature, `parti-socialiste.fr/wp-content/uploads/2023/04/PPL_Abrogation_reforme_des_retraites.pdf`, hors fenêtre du corpus). À vérifier à l'étape 2 dans les textes cosignés d'autres groupes.
- **Motion de censure du 17 février 2025** dont Boris Vallaud est premier signataire (MIONANR5L17-N9) : texte non trouvé (ni PDF de l'Assemblée, ni page du parti).
- **Date de la prochaine journée réservée du groupe SOC** : non trouvée.
- PPLC n° 3348 (AME) : PDF pas encore publié [C-PS-46].

**Accès refusés ou partiels**
- choisir2027.fr : connexion refusée en https et page de parking de l'hébergeur en http le 2026-10-27 ; profession de foi du candidat récupérée sur web.archive.org (capture du 2026-09-25) [C-PS-14].
- web.archive.org : service temporairement hors ligne ou limité (erreurs « Temporarily Offline » et 429) à plusieurs reprises pendant la session ; requêtes reprises avec succès ensuite, sauf l'index des PDF de parti-socialiste.fr pour 2011-2012 (erreur 504).
- Le Monde : accès refusé à l'outil de lecture (article du 9 juin 2026 sur la candidature de Karim Bouamrane) ; fait recoupé par une dépêche AFP reprise par Brut.
- *Le Parisien* (entretien d'Olivier Faure du 17 octobre 2026) : non ouvert ; connu par un relais (Entrevue).
- reveillerleurope.fr : injoignable.
- Site du groupe (socialistes-assemblee.fr) : domaine qui ne répond pas ; les textes du groupe sont publiés dans la rubrique « Vie parlementaire » de parti-socialiste.fr.
- Textes des motions de censure sur le site de l'Assemblée : erreur 404 aux adresses open data (comme pour LFI).
- Dossier de presse de la niche de janvier 2025 [C-PS-34] : extraction de texte inutilisable (encodage des polices).

**Connu seulement par la presse**
- Résultats chiffrés de la primaire (Public Sénat, franceinfo) ; maintien d'Olivier Faure après la primaire (Entrevue relayant *Le Parisien*) ; candidature de Karim Bouamrane (AFP via Brut) ; contenu du livre du candidat (LCP) ; propositions de Blois 2025 au-delà de l'exposé de l'amendement n° 125 (LCP) ; non-censure du 14 octobre 2025 (LCP).

**Écarts entre documents à vérifier aux étapes suivantes (précisions successives ou divergences possibles, sans qualification à cette étape)**
- **Smic** : 1 690 € net dans le Projet socialiste adopté [C-PS-01] (et dans la version d'avril selon LCP) ; 1 700 € net dans le contre-budget 2027 du groupe [C-PS-33] ; 1 600 € net dans le programme du NFP 2024 [C-PS-22] ; hausse de 15 % dans le programme de 2022 [C-PS-24].
- **Retraites, âge légal** : version d'avril 2026, âge « ramené à 62 ans » qui ne serait « pas le critère central » (LCP) ; version adoptée, âge « ramené à 62 ans » qui « continuera de jouer un rôle de protection minimale », avec 43 annuités réductibles [C-PS-01] ; NFP 2024, « objectif commun du droit à la retraite à 60 ans » [C-PS-22] ; Blois 2025, suspension et retour à 62 ans [C-PS-29] ; candidat, espérance de vie en bonne santé comme critère (livre, selon LCP [C-PS-20]) ; 2012, départ à 60 ans pour les carrières longues [C-PS-69].
- **Fiscalité du patrimoine** : ISF « renforcé » dans le NFP 2024 [C-PS-22] ; pas de rétablissement de l'ISF dans le projet 2026, qui retient la taxe Zucman et un impôt sur les grandes successions [C-PS-01] ; le communiqué du 26 septembre 2025 reproche au Premier ministre de refuser « le retour de l'ISF » [C-PS-32] ; impôt plancher de 2 % au-delà de 100 M€ dans les amendements [C-PS-31], [C-PS-52].
- **Contre-budget 2027, économies** : 12,1 Md€ d'« économies » et 5,5 Md€ de lutte contre la fraude au texte, 17,5 Md€ d'« économies et lutte contre la fraude » au tableau de chiffrage [C-PS-33] (12,1 + 5,5 = 17,6 Md€, calcul par nos soins, écart d'arrondi de 0,1 Md€) ; la note de paysage signalait « 12,1 ou 17,5 Md€ selon les sources » : les deux chiffres figurent dans le même document, avec un périmètre différent. Recettes de 39,5 Md€ brutes, 28,5 Md€ nettes de 11 Md€ de soutien aux ménages et aux entreprises au tableau.
- **Trajectoire de déficit** : 5 % du PIB en 2026 et 3 % en 2032 (Blois 2025) [C-PS-29], [C-PS-30] ; aucune cible en pourcentage du PIB dans le contre-budget 2027 [C-PS-33] ni dans le projet [C-PS-01].
- **Primaire** : 66,17 % (Public Sénat, Place publique) ou 66,13 % (franceinfo) ; Olivier Faure 14,46 % ou 14,48 % ; « 79 613 votants » selon Place publique [C-PS-18] contre 120 787 votants selon Public Sénat.
- **Congrès 2025** : texte A à 42,21 % au 28 mai, 42,02 % à la ratification ; texte B à 17,41 % puis 17,60 % [C-PS-09].
- **Effectif du groupe SOC** : 69 députés au 27 octobre 2026 (open data, président compris) contre 68 dans la note de paysage ; le parti écrit « 66 député·es » en novembre 2024 [C-PS-34].
- **Loi intégrale** : la note de paysage cite le n° 2169 ; le texte adopté le 13 octobre 2026 est la PPL n° 3106 (redéposée le 11 août 2026) [C-PS-58].
- **Stratégie présidentielle** : la direction (texte A) proposait un vote ouvert puis une candidature commune de la gauche (« choix 1 ») ; les adhérents ont retenu une primaire réservée aux adhérents du « pôle socialiste » (« choix 2 ») [C-PS-03].
- **Date de l'« Acte I » de Place publique** : PDF créé le 2026-10-15 ; un profil de candidat le date de juin 2025 [C-PS-16].
- **Statuts** : fichier « REFORME_Statuts_V9 » créé en 2021 ; version en vigueur à confirmer [C-PS-12].

---

### Trous propres à la section f (déclarations)

**Non trouvé**
- Immigration : parmi les 120 publications de parti-socialiste.fr datées du 1er janvier au 26 octobre 2026 (liste complète relevée par l'interface publique du site le 2026-10-27), aucune ne porte sur l'immigration, l'AME, les OQTF, l'asile ou le pacte européen sur la migration et l'asile. Aucune déclaration de 2026 du parti ou du groupe sur l'AME trouvée.
- Appartenance à l'Union : aucune déclaration explicite de 2026 du parti ou du candidat sur le maintien dans l'Union, la révision des traités ou la désobéissance. Éléments indirects seulement : majorité qualifiée sur la sécurité collective [C-PS-74], suppression du droit de veto et grand emprunt européen rapportés par LCP [C-PS-78]. Deux sites agrégateurs (ElyséeScope, votons-2027.fr) attribuent au candidat un « saut fédéral », un pouvoir d'initiative du Parlement européen et un emprunt de 500 milliards : non retenus, fiabilité non établie et source primaire non trouvée. À chercher dans le projet socialiste (section a) et dans le programme du candidat quand il paraîtra.
- Programme du candidat : le site glucks2027.fr n'a ni page programme ni publications (l'interface de contenus renvoie « page introuvable ») ; le site du parti Place publique (place-publique.eu) renvoie une erreur 404 ; place-publique.fr est un site de magazine distinct, non utilisé.
- Déclaration de candidature du 23 août 2026 : dépêche AFP reprise par Les Nouvelles Calédoniennes, seul le chapô est lisible ; pages Euronews (23 et 29 août) refusées à l'outil (erreur 406). Non archivée.
- Texte intégral de la lettre du 2 octobre [C-PS-85] et document du contre-budget du 16 septembre [C-PS-82] : non trouvés ; les sept priorités du 24 septembre renvoient à un document et une vidéo non ouverts.
- Smic à 1 700 euros net : trouvé seulement dans la bouche d'Olivier Faure candidat [C-PS-80] ; l'article LCP sur le contre-budget [C-PS-82] ne le mentionne pas (il décrit la hausse du net par la CSG progressive).
- Sécurité : aucune déclaration de 2026 du parti ou du groupe trouvée sur le narcotrafic, la légitime défense ou la justice des mineurs (recherche limitée à la liste des publications du site du parti et à LCP).
- Patrick Kanner ou le groupe socialiste du Sénat parlant seul : rien retenu ; position des sénateurs socialistes sur « casseurs-payeurs » réservée à la séance du 27 octobre (non recherchée).
- Candidats à la primaire issus du PS autres qu'Olivier Faure (Jérôme Guedj, Ségolène Royal) et Karim Bouamrane : aucune déclaration reprise ensuite par le parti ou le candidat, ni contraire au projet, trouvée ; recherche sommaire. Emmanuel Maurel est intervenu en séance le 7 avril sur le projet de loi fraudes, mais comme député d'un autre groupe : non retenu.
- Glucksmann, convention citoyenne sur l'immigration : la page Sud Radio est en erreur 404 ; source retenue : LCP [C-PS-78].

**Accès refusés ou partiels**
- deputes-socialistes.fr : connexion impossible (aucune réponse du serveur) le 2026-10-27.
- Comptes rendus de l'Assemblée d'octobre 2026 : le PDF « n'est pas publié », version web lue (13 et 16 octobre).
- Le Nouvel Obs, BFMTV, franceinfo, France 2 (médias d'origine de [C-PS-73], [C-PS-78], [C-PS-80], [C-PS-81], [C-PS-87]) : non ouverts, positions lues dans les relais.
- LCP (déclaration de Boris Vallaud sur « casseurs-payeurs ») : non retrouvée, connue par l'AFP seulement.

**Relais uniques**
- Tous les relais sont uniques : [C-PS-73], [C-PS-80] et [C-PS-91] (une seule reprise de dépêche AFP chacun), [C-PS-78], [C-PS-82] et [C-PS-85] (LCP seul), [C-PS-81], [C-PS-83] et [C-PS-87] (Public Sénat seul). Pour [C-PS-81] et [C-PS-83], la date exacte de la déclaration n'est pas donnée par le relais (date de l'article retenue).

### Écarts relevés dans les déclarations, à vérifier aux étapes suivantes (listés, non qualifiés)

- Smic : 1 700 euros net (Olivier Faure candidat [C-PS-80] ; contre-budget 2027 selon la note de paysage) contre 1 690 euros net (projet socialiste selon la presse, note de paysage) ; le contre-budget décrit par LCP [C-PS-82] passe par la CSG progressive (environ 130 euros net de plus au Smic).
- Retraites : 62 ans, « aucun candidat se revendiquant des socialistes ne saurait s'en éloigner » (Olivier Faure [C-PS-80]) ; 62 ans « sans être le critère central » (projet socialiste selon la presse) ; critère d'espérance de vie en bonne santé, cadres partant plus tard (Raphaël Glucksmann [C-PS-78]) ; suspension présentée comme un acquis qui n'est « pas l'abrogation » ([C-PS-72], [C-PS-88]).
- Régularisation : « autour de 400 000 », 500 000 ne « choque pas » (Olivier Faure [C-PS-80], [C-PS-81]) ; titre de séjour après six mois de contrat (projet socialiste selon la note de paysage) ; « contrôle » de l'immigration irrégulière, convention citoyenne, s'installer en France n'est pas « un droit universel » (Raphaël Glucksmann [C-PS-73], [C-PS-78]).
- Alliances : « pas d'accord avec LFI » (candidat désigné [C-PS-87]) ; stratégie votée par les militants le 9 juillet 2026 : rassemblement de « la gauche démocratique, écologique et républicaine » (communiqué du parti du 10 juillet, non retenu en section f, https://parti-socialiste.fr/actualites/les-militantes-socialistes-ont-adopte-leur-strategie-presidentielle-pour-2027/).
- Contre-budget 2027 : économies de 12,1 milliards (LCP [C-PS-82]) ou 17,5 milliards (note de paysage) ; réduction du déficit de 24 milliards (Public Sénat [C-PS-83]) ; aucune cible de déficit en pourcentage du PIB trouvée.
- Discipline de groupe : selon LCP citant L'Opinion, François Hollande et Sacha Houlié ne devaient pas voter la motion de rejet du 13 octobre ([C-PS-88]) ; à vérifier dans le scrutin.
- « Préférence nationale » dans certaines prestations ([C-PS-85]) : texte (PLF ou PLFSS 2027) et article à identifier.
- Institutions : proportionnelle et régime « primo-ministériel » (Boris Vallaud [C-PS-79]) ; à comparer au projet socialiste et au programme du candidat.
- TVA : refus de la baisse de TVA sur les carburants proposée par le RN ([C-PS-75]) ; TVA à 5,5 % sur un panier de produits contre la précarité (projet socialiste selon la note de paysage) : objets différents, à vérifier.
- Dates à vérifier : communiqué Mercosur daté du 27 janvier par le site mais dont le texte évoque la fin du Salon de l'agriculture ([C-PS-71], Contexte) ; résolution du bureau national publiée au 1er mars pour une réunion du 31 mars ([C-PS-75]) ; note de Boris Vallaud datée du 2 juillet par la Fondation et du 3 par LCP ([C-PS-79]) ; adresse de [C-PS-92] reprenant le titre d'un autre communiqué.

---

## Sources secondaires utilisées pour les statuts et le contexte

1. LCP (avec AFP), « Smic, retraites, immigration… le PS présente un projet de 144 pages pour préparer 2027 », 2026-04-22. https://lcp.fr/actualites/smic-retraites-immigration-le-ps-presente-un-projet-de-144-pages-pour-preparer-2027
2. franceinfo, « Retour de la taxe Zucman, augmentation du Smic, taxation des gros héritages : le PS propose son contre-budget à l'Assemblée nationale », 2026-09-16 (cité par la note de paysage, source 35 ; non rouvert à cette étape, le document primaire [C-PS-33] ayant été trouvé). https://www.franceinfo.fr/economie/budget/retour-de-la-taxe-zucman-augmentation-du-smic-taxation-des-gros-heritages-le-ps-propose-son-contre-budget-a-l-assemblee-nationale_8195063.html
3. LCP, « Le PS, "volontaire" pour gouverner, a présenté son budget alternatif à celui de François Bayrou », 2025-08-30. https://lcp.fr/actualites/le-ps-volontaire-pour-gouverner-a-presente-son-budget-alternatif-a-celui-de-francois
4. LCP, « Le PS ne censurera pas le gouvernement, le risque de chute s'éloigne pour Sébastien Lecornu », 2025-10-14. https://lcp.fr/actualites/le-ps-ne-censurera-pas-le-gouvernement-le-risque-de-chute-s-eloigne-pour-sebastien
5. LCP, « Présidentielle 2027 : s'il gagne, Raphaël Glucksmann engagera "les 100 jours de la révolution écologique" », 2026-08-25. https://lcp.fr/actualites/presidentielle-2027-s-il-gagne-raphael-glucksmann-engagera-les-100-jours-de-la
6. LCP, « Présidentielle : Raphaël Glucksmann dévoile les premières lignes de son possible programme », 2026-05-26. https://lcp.fr/actualites/presidentielle-raphael-glucksmann-devoile-les-premieres-lignes-de-son-possible-programme
7. Les Économistes atterrés, copie du programme d'Anne Hidalgo, mars 2022 (hébergeur, pas auteur ; non utilisée, l'original de campagne ayant été trouvé). https://www.atterres.org/wp-content/uploads/2022/03/Programme-presidentiel-Anne-Hidalgo.pdf [collectif d'économistes classé à gauche]
8. Public Sénat, « Primaire de la gauche : Raphaël Glucksmann plie le match et remporte le scrutin dès le premier tour avec 66 % », 2026-10-11. https://www.publicsenat.fr/actualites/politique/primaire-de-la-gauche-raphael-glucksmann-plie-le-match-et-remporte-le-scrutin-des-le-premier-tour-avec-66
9. franceinfo, « Raphaël Glucksmann remporte dès le premier tour la primaire à gauche », 2026-10-11. https://www.franceinfo.fr/politique/raphael-glucksmann/raphael-glucksmann-remporte-des-le-premier-tour-la-primaire-a-gauche_8232967.html
10. Brut (dépêche AFP), « Le maire de Saint-Ouen Karim Bouamrane (PS), "candidat pour être le prochain président de la République" », daté du 2026-06-24. https://www.brut.media/fr/articles/le-maire-de-saint-ouen-karim-bouamrane-ps-candidat-pour-etre-le-prochain-president-de-la-republique [média en ligne, relais d'une dépêche AFP]
11. Entrevue, « Après sa déroute face à Glucksmann, Olivier Faure sort du silence et refuse de lâcher le Parti socialiste », 2026-10-19 (relais d'un entretien au *Parisien* du 2026-10-17). https://entrevue.fr/politique/apres-sa-deroute-face-a-glucksmann-olivier-faure-sort-du-silence-et-refuse/ [étiquette proposée ci-dessous]
12. Assemblée nationale, jeu de données « Dossiers législatifs » de la XVIIe législature, et jeux AMO10 et AMO30, téléchargés le 2026-10-27. https://data.assemblee-nationale.fr/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip
13. Assemblée nationale, page du scrutin public n° 8707 (2026-10-13), consultée le 2026-10-27. https://www.assemblee-nationale.fr/dyn/17/scrutins/8707 ; page du scrutin n° 3300. https://www.assemblee-nationale.fr/dyn/17/scrutins/3300
14. Parti socialiste, interface publique du site (articles et fichiers PDF), interrogée le 2026-10-27. https://parti-socialiste.fr/wp-json/wp/v2/media?mime_type=application/pdf [source du parti, partie prenante] ; même interrogation sur https://projet-socialiste.fr/wp-json/wp/v2/media (aucun PDF ; trois vidéos).
15. web.archive.org, index des fichiers de choisir2027.fr, francoishollande.fr et 2022avechidalgo.fr (CDX), consulté le 2026-10-27. http://web.archive.org/cdx/search/cdx?url=choisir2027.fr/*
16. Sénat, « Liste des groupes politiques », mise à jour le 2026-10-27. https://www.senat.fr/senateurs/grp.html

Sources de la section f (déclarations), numérotées à la suite :

17. LCP, « Présidentielle : Raphaël Glucksmann dévoile les premières lignes de son possible programme », 2026-05-26. https://lcp.fr/actualites/presidentielle-raphael-glucksmann-devoile-les-premieres-lignes-de-son-possible-programme
18. LCP, « VIe République, proportionnelle, rôle du Premier ministre : les propositions de Boris Vallaud avant 2027 », 2026-07-03. https://lcp.fr/actualites/sixieme-republique-proportionnelle-role-du-premier-ministre-les-propositions-de-boris
19. Fondation Jean-Jaurès, Boris Vallaud, « Souvenirs pour demain. De l'exercice de l'opposition à l'exercice du pouvoir », 2026-07-02 (page) et PDF. https://www.jean-jaures.org/publication/souvenirs-pour-demain-de-lexercice-de-lopposition-a-lexercice-du-pouvoir/ ; https://www.jean-jaures.org/wp-content/uploads/2026/06/souvenirs-pour-demain.pdf [proche du PS]
20. LCP, « Budget : à l'Assemblée, les socialistes présentent leurs propositions et préviennent qu'ils ne "toperont pas avec le gouvernement" », 2026-09-16. https://lcp.fr/actualites/budget-a-l-assemblee-les-socialistes-presentent-leurs-propositions-et-previennent-qu-ils
21. La Gazette France (AFP), « Smic à 1.700 euros, régularisation des travailleurs sans papiers, retraites : Faure développe ses propositions », 2026-09-16. https://www.lagazettefrance.fr/article/smic-a-1-700-euros-regularisation-des-travailleurs-sans-papiers-retraites-faure-developpe-ses-propositions [relais de dépêche AFP, étiquette proposée]
22. Public Sénat, « Immigration : à quoi correspond la proposition d'Olivier Faure de régulariser 400 000 travailleurs sans-papiers ? », 2026-09-17. https://www.publicsenat.fr/actualites/politique/immigration-a-quoi-correspond-la-proposition-dolivier-faure-de-regulariser-400-000-travailleurs-sans-papiers
23. Public Sénat, « Budget 2027 : Boris Vallaud (PS) dénonce un budget qui risque de "nous enfoncer dans la crise" », 2026-09-22. https://www.publicsenat.fr/actualites/politique/budget-2027-boris-vallaud-ps-denonce-un-budget-qui-risque-de-nous-enfoncer-dans-la-crise
24. LCP, « Budget 2027 : "Les plus modestes continuent de payer pour les plus riches", dénoncent les socialistes », 2026-10-02. https://lcp.fr/actualites/budget-2027-les-plus-modestes-continuent-de-payer-pour-les-plus-riches-denoncent-les
25. Public Sénat, « "Ce soir, la bataille de France commence" : après sa victoire à la primaire de la gauche, Raphaël Glucksmann assure que "rien" ne le "fera lâcher" », 2026-10-11. https://www.publicsenat.fr/actualites/politique/ce-soir-la-bataille-de-france-commence-apres-sa-victoire-a-la-primaire-de-la-gauche-raphael-glucksmann-assure-que-rien-ne-le-fera-l
26. LCP, « "Il laisse la porte fermée" : les députés PS répondent à Lecornu et maintiennent leur motion de rejet sur le budget », 2026-10-13. https://lcp.fr/actualites/il-laisse-la-porte-fermee-les-socialistes-repondent-a-sebastien-lecornu-et-maintiennent
27. LCP, « La motion de rejet des socialistes n'ayant pas été adoptée, l'examen du budget 2027 aura bien lieu à l'Assemblée », 2026-10-14. https://lcp.fr/actualites/la-motion-de-rejet-des-socialistes-n-ayant-pas-ete-adoptee-l-examen-du-budget-2027-aura
28. Datan, « Législature 17, vote n° 8860 » (amendement n° 471 au PLF 2027), 2026-10-16. https://datan.fr/votes/legislature-17/vote_8860 [agrégateur des données ouvertes de l'Assemblée]
29. La Gazette France (AFP), « "Casseurs-payeurs" : après les violences, la réponse législative franchit une première étape au Sénat », 2026-10-21. https://www.lagazettefrance.fr/article/casseurs-payeurs-apres-les-violences-du-17-octobre-la-reponse-legislative-au-senat [relais de dépêche AFP, étiquette proposée]
30. La Gazette France (AFP), « Immigration : Glucksmann prône le "contrôle" mais réfute toute "submersion" », 2026-01-29. https://www.lagazettefrance.fr/article/immigration-glucksmann-prone-le-controle-mais-refute-toute-submersion [relais de dépêche AFP, étiquette proposée]
31. Parti socialiste, liste des publications du 1er janvier au 26 octobre 2026 relevée par l'interface publique du site, 2026-10-27. https://parti-socialiste.fr/wp-json/wp/v2/posts?after=2026-01-01T00:00:00&per_page=100 [source du parti, partie prenante]

## Ajouts proposés

Aucune fiche ajoutée après l'étape 1. Étiquettes absentes de `03-sources/etiquettes.md`, proposées pour le registre (le registre n'est pas modifié) :

- [Place publique : source du candidat, partie prenante]. Justification : parti du candidat, hors périmètre du PS (`01-criteres.md` §1) ; à distinguer de « source du parti » pour garder la règle parti / candidat lisible.
- [Entrevue : magazine en ligne d'actualité et de divertissement, relais]. Justification : média grand public sans ligne politique revendiquée identifiée ; utilisé une fois, comme relais d'un entretien au *Parisien* non accessible.
- [Brut : média en ligne, relais de dépêches AFP]. Justification : média vidéo et web grand public ; utilisé ici pour une dépêche AFP.
- [Les Économistes atterrés : collectif d'économistes classé à gauche]. Justification : autodéfinition hétérodoxe et classement usuel ; cité seulement comme hébergeur d'une copie non utilisée.
- Documents repérés et non retenus, archivables si une fiche axe en a besoin : professions de foi de Jérôme Guedj, Ségolène Royal et Emmanuel Maurel à la primaire (web.archive.org, captures du 2026-09-25) ; règlement intérieur du PS (2022) et « Charte des socialistes pour le progrès humain » ; « Repères socialistes » (laïcité, ONU) ; « Batailles communes » des municipales 2026 ; dossiers « stratégie énergétique » (juin 2025) ; PPL n° 2033 (VSS au travail), n° 2028 (vie chère outre-mer dans les services), n° 2039 (rapports locatifs), n° 3270 (protection des locataires), n° 3251 (mutuelle publique 18-25 ans), n° 2286 (droits des personnes LGBTQIA) ; PPL de la XVIe législature hébergées sur le site du parti (abrogation de la réforme des retraites de 2023, contre-budget 2024) ; profession de foi de 2012 en version longue non vérifiée.
- Recoupement avec la section f, fait à l'intégration : le discours de Blois d'Olivier Faure (29 août 2026) est en fiche [C-PS-08] ; la page web des « 7 priorités » est en [C-PS-84] et le document primaire en [C-PS-33] ; le livre du candidat est en lien seul [C-PS-20] et sa présentation de presse en [C-PS-78] ; le site de campagne est en [C-PS-93] (aucune fiche en section a pour éviter le doublon) ; le communiqué du 19 octobre 2026 sur le droit de manifester est en [C-PS-90] (aucune fiche en section a).

Étiquettes proposées par le second sous-agent (section f), à inscrire au registre si une étape ultérieure les utilise :

- [La Gazette France : site d'information et d'annonces légales, relais de dépêches AFP] : utilisé pour trois dépêches AFP ; le média d'origine est indiqué dans chaque fiche.
- [LCP (La Chaîne parlementaire, Assemblée nationale) : chaîne parlementaire publique, presse généraliste, pas d'étiquette] : déjà utilisée dans les verticales sans ligne au registre.
- [Site ou document d'un candidat : source du candidat, partie prenante] : pendant de « Site ou document d'un parti » pour glucks2027.fr, utile quand le candidat n'est pas membre du parti étudié.
- [L'Obs (Le Nouvel Obs) : hebdomadaire classé à gauche] et [BFMTV : chaîne d'information, presse généraliste] : médias d'origine non ouverts, à inscrire seulement si une étape ultérieure les lit.
