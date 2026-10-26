# RN : corpus programmatique

- Rédigé le : 2026-10-25
- Date d'arrêt des données : 2026-10-25
- Auteur : sous-agent Opus, étape 1 ; complété par les sous-agents des étapes 3 à 6 (C-RN-53 à C-RN-83)
- Statut : revu (verticale terminée)
- Règle appliquée : `01-socle/01-criteres.md` §6 (hiérarchie du corpus) et `01-socle/03-sources-et-hierarchie.md` (archivage, étiquetage)

Périmètre (voir `00-perimetre.md`) : le parti Rassemblement national (RN), le groupe Rassemblement National à l'Assemblée nationale, et sa candidate déclarée Marine Le Pen (présidente du groupe). Jordan Bardella, président du parti, parle pour le parti. Le groupe Union des droites pour la République (UDR) est hors périmètre ; un texte dont le premier signataire est UDR est signalé comme tel.

Sigles utilisés : PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PPR (proposition de résolution), PLF (projet de loi de finances), PLFSS (projet de loi de financement de la sécurité sociale), AN (Assemblée nationale), UE (Union européenne), AME (aide médicale de l'État), AMU (aide médicale d'urgence), IFI (impôt sur la fortune immobilière), IFF (impôt sur la fortune financière), CFE (cotisation foncière des entreprises), CVAE (cotisation sur la valeur ajoutée des entreprises), C3S (contribution sociale de solidarité des sociétés), TVA (taxe sur la valeur ajoutée), RSA (revenu de solidarité active), APL (aide personnalisée au logement), HLM (habitation à loyer modéré), RIC (référendum d'initiative citoyenne), OTAN (Organisation du traité de l'Atlantique Nord), IDEP (Institut de l'Entreprise), Md€ (milliard d'euros).

Étiquette commune : tous les documents émanant du RN, du groupe RN, de la campagne de Marine Le Pen (2022 et 2027) ou de la délégation RN au Parlement européen sont des **sources du parti, partie prenante**. Les textes de PPL, PPR et amendements hébergés par l'Assemblée sont des sources primaires (niveau 1) dont l'auteur est partie prenante.

Archivage : les fichiers sont dans `02-partis/rn/corpus/`, tous téléchargés le **2026-10-25**. Trois PDF dépassent 20 Mo et ne sont pas versionnés : programme des législatives 2024 (21,5 Mo), programme des européennes 2024 (24,2 Mo), manifeste présidentiel 2022 (27,6 Mo). Pour chacun : lien, somme de contrôle SHA-256 et copie texte (`.md`) de l'extraction du PDF. Le plus lourd des fichiers versionnés fait 7,9 Mo. Les tirets cadratins et demi-cadratins des textes d'origine ont été remplacés dans les copies texte (mention en tête de chaque fichier concerné).

Légende du statut d'archivage :
- **PDF archivé** : fichier original téléchargé.
- **Texte archivé** : copie texte de la page web ou du PDF (`.md`), avec URL et date de consultation.
- **Lien seul** : pas de fichier téléchargeable ou pas de source primaire accessible.

---

## Synthèse

| Catégorie (§6) | Nombre de fiches | Archivés |
|---|---|---|
| a. Programme 2027, textes de campagne, textes du parti depuis 2024 | 16 | 6 pages texte, 1 PDF parti, 1 copie texte de PDF (plus de 20 Mo), 1 PDF tiers (relais), 7 liens seuls |
| b. Programme législatives 2024 | 1 | 1 copie texte de PDF (PDF de 21,5 Mo : lien et somme de contrôle) |
| c. Programme présidentiel 2022 | 12 | 11 PDF, 1 copie texte de PDF (manifeste de 27,6 Mo : lien et somme de contrôle) |
| d. Contre-budgets et plans d'économies | 2 (plus le plan 2027-2032, fiche [C-RN-03]) | 2 PDF |
| e. Propositions de loi et de résolution, amendements du groupe RN | 17 textes et 3 amendements | 20 PDF |
| f. Déclarations depuis le 1er janvier 2026 | 23 (22 à l'étape 1, 1 ajoutée à l'étape 3) | 3 textes (site du parti), 20 liens |
| Actes | non applicable | |

Total du dossier `corpus/` : 45 fichiers (35 PDF, 10 `.md`), 36 Mo.

**Point principal :** aucun programme présidentiel 2027 complet n'est publié au 25 octobre 2026. Le site de campagne marinelepen.com ne contient aucune page programme [C-RN-01] ; le site du parti renvoie encore aux documents de 2022, 2024 et au contre-budget 2026 [C-RN-02]. **Le document le plus abouti est le plan financier 2027-2032 présenté le 6 octobre 2026** (125 mesures, 140 Md€ d'économies nettes annoncées en 2032) [C-RN-03] ; son dossier de presse n'est pas en ligne et n'est connu que par la presse et par la note de l'Institut de l'Entreprise, qui en cite les diapositives et l'annexe [C-RN-04]. La réforme des retraites détaillée est annoncée pour le 17 novembre 2026, hors corpus [C-RN-07]. Le pôle économie et finances de la campagne est coordonné par Jean-Philippe Tanguy depuis le 30 septembre 2026 [C-RN-12].

---

## a. Programme 2027 et textes de campagne (priorité 1)

### Programme présidentiel 2027 officiel

**Inexistant à la date d'arrêt.** Les engagements sont dispersés entre le plan financier du 6 octobre 2026 (non publié en ligne), des conférences de presse, des discours et des entretiens. La campagne ne publie pas de comptes rendus sur son site, à la différence de celle de Gabriel Attal : les seules sources primaires accessibles en texte sont les pages discours, conférences de presse et communiqués de rassemblementnational.fr.

### [C-RN-01] Site de campagne de Marine Le Pen, page d'accueil
- Auteur : candidate (campagne « Marine 2027 »)
- Date : non datée, consultée le 2026-10-25
- Nature : page web
- URL : https://marinelepen.com
- Archivage : texte archivé, `corpus/C-RN-01-site-campagne-marinelepen-com-2026-10-25.md`
- Utile pour : constat d'absence. La page annonce dans sa description un programme, mais ne contient qu'un formulaire d'adhésion et une inscription au meeting d'Orléans ; le plan du site ne liste que trois adresses (accueil, mentions légales, confidentialité).

### [C-RN-02] Site du parti, rubrique « Projet de gouvernement »
- Auteur : parti
- Date : non datée, consultée le 2026-10-25
- Nature : page web (rubrique de la page d'accueil)
- URL : https://rassemblementnational.fr
- Archivage : texte archivé, `corpus/C-RN-02-site-parti-rubrique-projet-2026-10-25.md`
- Utile pour : structure du corpus officiel affiché par le parti : législatives 2024 [C-RN-17], européennes 2024 [C-RN-15], contre-budget 2026 [C-RN-31], livret « La France entreprend » [C-RN-14], 22 mesures et livrets de 2022 [C-RN-18] à [C-RN-29]. Aucun lien vers un document 2027 ; les adresses supposées d'un contre-budget 2027 renvoient une erreur 404 le 2026-10-25.

### [C-RN-03] Plan financier 2027-2032 (« contre-budget 2027 »), conférence de presse au siège du RN
- Auteur : candidate et parti (Marine Le Pen, Jordan Bardella, Jean-Philippe Tanguy)
- Date : 2026-10-06
- Nature : conférence de presse et dossier de presse (diapositives et annexe de 125 mesures selon [C-RN-04])
- URL : document primaire non trouvé. Relais : https://www.publicsenat.fr/actualites/politique/140-milliards-deuros-deconomies-dici-2032-leffort-radical-propose-par-marine-le-pen-pour-redresser-les-f ; https://www.europe1.fr/politique/budget-2027-marine-le-pen-promet-140-milliards-deuros-nets-deconomies-dici-2032-pour-eviter-a-la-france-le-defaut-de-paiement-1126400 ; https://www.boursorama.com/actualite-economique/actualites/marine-le-pen-veut-ramener-le-deficit-budgetaire-a-3-d-ici-2030-e234d02e0ea563e2766ea6142c4a1bdc (Reuters)
- Archivage : lien seul. Le dossier n'est pas en ligne sur rassemblementnational.fr ni sur marinelepen.com au 2026-10-25 ; il n'existe qu'en relais de presse.
- Utile pour : axe 1 (140 Md€ d'économies nettes en 2032 par rapport à 2026, soit 15 Md€ de plus que les 125 Md€ annoncés au Medef [C-RN-05], selon Public Sénat ; déficit sous 3 % du PIB en 2030 ; solde primaire rétabli en 18 mois ; dette ramenée à 112 % du PIB en 2032 ; règle d'or constitutionnelle adoptée par référendum dans les douze mois suivant l'élection ; ventilation pour 2027 rapportée par Public Sénat : 20,7 Md€ de réorganisation de l'État, 8,2 Md€ sur les collectivités, 3,4 Md€ sur les agences et opérateurs) ; axe 3 (15 Md€ d'économies sur l'immigration en 2027, 29 Md€ en année pleine) ; axe 2 (15 à 20 Md€ d'économies sur les retraites par « corrections de mesures injustes », pilier de capitalisation, âge ramené à 62 voire 60 ans selon Europe 1) ; axe 4 (30 Md€ nets de baisses d'impôts sur le quinquennat) ; axe 6 (baisse de la contribution à l'UE, 9 Md€ selon Jordan Bardella ; appel à une intervention de la Banque centrale européenne).

### [C-RN-04] Relais : note de l'Institut de l'Entreprise sur le contre-budget du RN
- Auteur : Institut de l'Entreprise (IDEP), **think tank d'entreprises** (étiquette du registre). Source tierce de niveau 4, critique du document analysé, utilisée ici **seulement pour les chiffres du RN qu'elle rapporte**.
- Date : octobre 2026 (postérieure au 2026-10-06)
- Nature : note de contexte, 9 pages
- URL : https://www.institut-entreprise.fr/wp-content/uploads/2026/10/Analyse-primaire-contre-budget-RN-Note-de-contexte-IDEP.pdf
- Archivage : PDF archivé, `corpus/C-RN-04-relais-institut-entreprise-note-contre-budget-2027-2026-10-25.pdf` (0,4 Mo)
- Utile pour : chiffres du RN cités par la note, avec référence aux diapositives 11, 19 et 24 à 26 du dossier de presse : amélioration nette du solde de 71,6 Md€ en 2027 et 141,7 Md€ en 2031 ; recettes et économies brutes de 140,8 Md€ (2027) et 244,4 Md€ (2031) ; baisses d'impôts de 53,2 Md€ (2027) et 49,1 Md€ (2031) ; dépenses nouvelles de 16,1 Md€ et 53,7 Md€ ; déficit de 5,4 % du PIB en 2026, 3,7 % en 2027, 2,3 % en 2031, 2,2 % en 2032 ; dette de 119,3 % (2027), 113,3 % (2031), 112,1 % (2032) contre 136,9 % à politique inchangée selon le parti ; règle d'or avec ajustement minimal de 0,5 point de PIB par an et dérogation aux trois cinquièmes du Parlement ; TVA à 5,5 % sur les énergies (12,2 Md€), suppression de la CFE, de la CVAE et de la C3S (17,1 Md€), TVA nulle sur cent produits (3,5 Md€), exonération d'impôt sur le revenu des actifs de moins de 30 ans jusqu'à quatre Smic (2,0 Md€), contribution à l'UE réduite de 13,1 Md€ en 2031, prestations de solidarité après 5 ans de travail (12,2 Md€), prestations familiales conditionnées à un parent français (5,9 Md€), « réparation » du système de retraite (15 Md€), réforme des retraites (9,5 Md€ de coût en 2031), taxe de 1 000 € par an sur l'embauche d'un salarié extra-européen (1 Md€), TVA prélevée à la source (18 Md€ en 2031). Les évaluations propres de l'IDEP (7,5 Md€ d'amélioration crédible) ne sont pas reprises au corpus.

### [C-RN-05] Débat à la Rencontre des entrepreneurs de France (Medef)
- Auteur : candidate
- Date : 2026-08-27
- Nature : intervention publique et débat
- URL : https://www.sudradio.fr/societe/marine-le-pen-et-la-delicate-operation-seduction-du-monde-economique (relais)
- Archivage : lien seul. Aucun texte publié par le parti trouvé.
- Utile pour : axe 1 (trajectoire de 125 Md€ d'économies, à détailler avant le débat budgétaire ; règle d'or constitutionnelle) ; axe 2 (départ à 60 ans pour les personnes entrées dans l'emploi avant 20 ans, âge légal à 62 ans à terme, 42 annuités, coût chiffré par le RN à 9 Md€ selon la presse) ; axe 4 (suppression de la C3S, de la CVAE et de la CFE).

### [C-RN-06] Discours de rentrée politique, Hénin-Beaumont (Pas-de-Calais)
- Auteur : candidate
- Date : 2026-09-13
- Nature : discours devant environ 2 000 partisans (chiffre de presse)
- URL : https://france3-regions.franceinfo.fr/hauts-de-france/pas-calais/lens/marine-le-pen-fait-sa-rentree-politique-a-henin-beaumont-et-met-la-priorite-nationale-au-c-ur-de-son-programme-pour-la-presidentielle-de-2027-3416348.html (relais, avec AFP)
- Archivage : lien seul. Texte du discours non trouvé sur le site du parti (la page discours s'arrête au 2 mai 2026).
- Utile pour : axe 3 (priorité nationale dans l'accès au logement social, APL réservées aux Français, expulsion des familles délinquantes du logement social) ; axe 4 (abrogation de la loi SRU, vente de HLM à leurs occupants français, terrains publics cédés gratuitement contre des loyers modérés, fin des obligations liées au diagnostic de performance énergétique, « 100 % rénov » par prêts à taux zéro à la place de MaPrimeRénov'). Un coordinateur du pôle logement est nommé le lendemain [C-RN-12].

### [C-RN-07] Conférence de presse à Bruxelles (retraites, Union européenne)
- Auteur : candidate
- Date : 2026-10-14 selon franceinfo (Euronews situe la conférence « lundi », soit le 12 octobre : date à confirmer)
- Nature : conférence de presse après une réunion des dirigeants du groupe Patriotes pour l'Europe
- URL : https://www.franceinfo.fr/elections/presidentielle/marine-le-pen-presentera-de-maniere-extremement-precise-sa-reforme-des-retraites-le-17-novembre_8237821.html ; https://www.euronews.com/2026/10/14/le-pen-lands-in-brussels-lashing-out-at-the-european-commission
- Archivage : lien seul
- Utile pour : axe 2 (âge légal maintenu « entre 60 et 62 ans » selon l'âge d'entrée sur le marché du travail, 40 à 42 annuités ; réforme chiffrée présentée le 17 novembre 2026) ; axe 6 et axe 1 (contribution nette de la France à l'UE plafonnée à 5 Md€ par an, contre environ 8 Md€ selon Euronews ; arrêt du financement français de l'Ukraine ; fin des sanctions contre la Russie ; taxe carbone aux frontières ; impôt européen sur les sociétés pour les grands groupes à taux unique de 20 à 25 %).

### [C-RN-08] Discours de Jordan Bardella, « Fête de la Nation » (Saône-et-Loire)
- Auteur : président du parti
- Date : prononcé le 2026-05-01, page datée du 2026-05-02
- Nature : discours publié en texte intégral par le parti
- URL : https://rassemblementnational.fr/discours/fete-de-la-nation-discours-de-jordan-bardella
- Archivage : texte archivé, `corpus/C-RN-08-discours-bardella-fete-de-la-nation-2026-05-01-2026-10-25.md`
- Utile pour : axe 4 (« choc massif de baisse des taxes », dont la TVA ; fin des certificats d'économie d'énergie ; mesures chiffrées par l'orateur à « 15 milliards d'euros par an » ; fin de la « lourdeur » des impôts de production ; incitation fiscale à augmenter les salaires) ; axe 1 (économies sur les agences et les doublons) ; axe 3 (fin de l'AME, reconduite des étrangers en situation irrégulière, espace Schengen limité aux ressortissants de l'UE) ; hors grille (tenue commune à l'école).

### [C-RN-09] Conférence de presse de Jordan Bardella, « Le sursaut face à l'extrême gauche »
- Auteur : président du parti
- Date : 2026-02-18
- Nature : déclaration publiée en texte intégral par le parti
- URL : https://rassemblementnational.fr/conferences-de-presse/communique-de-presse-6
- Archivage : texte archivé, `corpus/C-RN-09-conference-presse-bardella-sursaut-extreme-gauche-2026-02-18-2026-10-25.md` (prénom de la victime retiré)
- Utile pour : axe 5 (renforcement des interdictions administratives de manifester ; obligation de pointage lors des manifestations à risques, sur le modèle des interdictions de stade ; liste publique d'organisations présentant un risque grave pour l'ordre public ; reconstitution de ligue dissoute pour un collectif issu d'un groupe dissous ; mise sous tutelle d'établissements universitaires) ; axe 6 (appel à un « cordon sanitaire » contre LFI dans les instances de l'Assemblée).

### [C-RN-10] 19e congrès du RN, Orléans : réélection de Jordan Bardella et bureau national
- Auteur : parti
- Date : 2026-10-24 (vote et communiqué) ; congrès les 24 et 25 octobre
- Nature : élection du président par les adhérents (candidat unique, 98,98 % des suffrages exprimés selon la presse) ; communiqué fixant le bureau national
- URL : https://rassemblementnational.fr/communiques/communique-de-presse-du-rassemblement-national-21 ; https://www.franceinfo.fr/politique/front-national/au-congres-du-rassemblement-national-l-unique-candidat-jordan-bardella-est-reelu-sans-surprise-a-la-presidence-du-parti-avec-98-98-des-voix_8252326.html
- Archivage : texte archivé (communiqué), `corpus/C-RN-10-communique-bureau-national-congres-2026-10-24-2026-10-25.md`
- Utile pour : gouvernance du parti (bureau national et bureau exécutif). Aucun texte d'orientation ni motion programmatique adopté au congrès n'a été trouvé.

### [C-RN-11] Discours de Marine Le Pen, meeting de lancement de campagne, Orléans
- Auteur : candidate
- Date : 2026-10-25
- Nature : discours de clôture du congrès
- URL : https://www.boursorama.com/actualite-economique/actualites/marine-le-pen-dit-vouloir-presider-a-la-renaissance-de-la-france-23c3b9f98b2bd33f3acb553dafc26e5b (Reuters) ; https://www.20min.ch/fr/story/france-marine-le-pen-promet-une-renaissance-sans-rupture-brutale-103656322 (AFP)
- Archivage : lien seul. Texte non publié au 2026-10-25 ; couverture de presse du jour même, susceptible d'être complétée.
- Utile pour : axe 6 (primauté de la Constitution : « Aucun texte, aucune autorité, et surtout pas étrangère, même européenne, ne lui sera supérieure » ; recours au référendum ; élection à la proportionnelle avec prime majoritaire ; Jordan Bardella Premier ministre d'un gouvernement « d'union nationale ») ; axe 3 (priorité nationale ; « l'expulsion automatique et définitive » des étrangers délinquants ; interdiction du communautarisme) ; axe 2 (selon Reuters : pas d'engagement à revenir à 60 ans, engagement à ne pas porter l'âge de départ au-delà de 64 ans ; voir Trous, divergences) ; axe 5 (civilité contre « l'ensauvagement », selon l'AFP). Slogan relevé par la presse : « Construire la France de demain ».

### [C-RN-12] Communiqués de nomination de l'équipe de campagne
- Auteur : direction de campagne (Julien Sanchez, directeur de campagne)
- Date : 2026-09-14, 2026-09-30, 2026-10-09, 2026-10-19 (premières nominations le 2026-07-03, citées dans le communiqué du 14 septembre, non archivées)
- Nature : quatre communiqués
- URL : https://rassemblementnational.fr/communiques/nouvelles-nominations-au-sein-de-lequipe-de-campagne-de-marine-le-pen (et suffixes -2, -3) ; https://rassemblementnational.fr/communiques/communique-de-presse-de-julien-sanchez-directeur-de-campagne-de-marine-le-pen-2
- Archivage : texte archivé (quatre pages réunies), `corpus/C-RN-12-communiques-equipe-de-campagne-2026-09-a-10-2026-10-25.md`
- Utile pour : qui parle pour la campagne. Jean-Philippe Tanguy coordonne le pôle économie et finances (30 septembre) ; Jean-Paul Garraud le pôle sécurité et immigration ; Gaëtan Dussausaye le pôle travail (19 octobre) ; un sénateur UDR coordonne le pôle santé et un député UDR le pôle éducation (9 et 19 octobre) ; Sébastien Chenu coordonne les élus. Slogan « Pour la France, la Renaissance » mentionné dans un communiqué du 2026-07-31.

### [C-RN-13] Maintien de la candidature après l'arrêt de la cour d'appel
- Auteur : candidate
- Date : 2026-07-07 (journal de 20 h de TF1) ; lancement commun de campagne avec Jordan Bardella le 2026-07-08 à La Flèche (Sarthe)
- Nature : entretien télévisé, puis déplacement
- URL : https://www.aljazeera.com/news/2026/7/7/french-far-right-leader-le-pen-says-will-run-in-2027-presidential-election ; https://www.france24.com/fr/france/20260708-marine-le-pen-candidate-en-2027-un-choix-dynastique-du-rn-qui-%C3%A9clipse-jordan-bardella (relais)
- Archivage : lien seul
- Utile pour : couche « candidat » (§1 du socle) et contrainte de calendrier judiciaire documentée dans `00-perimetre.md`. Pas de contenu programmatique relevé dans les relais.

### [C-RN-16] Discours de Jordan Bardella, meeting d'Orléans
- Auteur : président du parti
- Date : 2026-10-25
- Nature : discours, interrompu par des militants selon la presse
- URL : https://www.24heures.ch/bardella-le-president-du-rn-reelu-avec-pres-de-99-des-voix-642797530461 ; https://actu.orange.fr/politique/je-vous-demande-de-vous-arreter-le-discours-de-jordan-bardella-chahute-lors-du-congres-du-rn-l-express-via-6medias-CNT000002tnRYL.html (relais de L'Express)
- Archivage : lien seul. Texte non publié au 2026-10-25.
- Utile pour : axe 5 (présomption de légitime défense pour les policiers, peines planchers, majorité pénale à 16 ans ; usage de tous les moyens légaux pour rétablir l'ordre, selon l'AFP). Le reste du discours n'est connu que par extraits.

### Textes du parti adoptés ou publiés depuis 2024

### [C-RN-14] Livret « La France entreprend »
- Auteur : parti et groupe RN (préface signée Marine Le Pen et Jordan Bardella)
- Date : septembre 2024 (PDF créé le 2024-09-06)
- Nature : livret de 35 pages présenté comme « la version 2022 du programme présidentiel de Marine Le Pen mis à jour », base de travail pour les prochaines échéances
- URL : https://rassemblementnational.fr/documents/WEB-GRN-LIVRET-ENTREPRISE.pdf
- Archivage : PDF archivé, `corpus/C-RN-14-livret-la-france-entreprend-2024-09-2026-10-25.pdf` (7,7 Mo)
- Utile pour : axe 4 (suppression de la CFE, exonération de C3S, exonération d'impôt sur le revenu des moins de 30 ans, hausse des salaires de 10 % exonérée de cotisations patronales, transmission d'entreprises défiscalisée sous condition) ; axe 2 (système de retraites progressif favorisant l'entrée précoce) ; axe 1 (moins d'agences, ministère de la lutte contre les fraudes, baisse de la dépense sociale par la priorité nationale) ; axe 6 (sortie des règles européennes de fixation des prix de l'énergie). À relire en détail pour les fiches axes.

### [C-RN-15] Programme des élections européennes 2024, « Pour une Europe des nations »
- Auteur : parti (Marine Le Pen, Jordan Bardella tête de liste)
- Date : PDF créé le 2024-05-06 (scrutin du 9 juin 2024)
- Nature : programme de 10 pages
- URL : https://rassemblementnational.fr/documents/202411-programme-europeennes.pdf
- Archivage : copie texte, `corpus/C-RN-15-programme-europeennes-2024-texte-2026-10-25.md`. PDF de 24,2 Mo non versionné, SHA-256 `d8ca9c4af92be12b9ee9a1876742c9e0d578dfc2134b4bf63ce126624dd3fe80`.
- Utile pour : axe 6 (« Europe des nations » ; Schengen accepté à condition que la libre circulation profite aux seuls ressortissants des États membres ; Frontex autorisée à renvoyer les migrants illégaux ; refus d'une diplomatie et d'une défense européennes et de la gestion par l'UE de l'immigration à l'intérieur des États) ; axe 3.

---

## b. Programme des législatives 2024 (priorité 2)

### [C-RN-17] « L'union fait la France. Un projet, une méthode »
- Auteur : parti, présenté par Jordan Bardella, candidat au poste de Premier ministre
- Date : juin 2024 (PDF créé le 2024-06-25 ; scrutins des 30 juin et 7 juillet 2024)
- Nature : programme législatif, 12 pages en deux temps : « temps de l'urgence » (juillet à l'automne 2024) et « temps des réformes »
- URL : https://rassemblementnational.fr/documents/202406-programme.pdf
- Archivage : copie texte, `corpus/C-RN-17-programme-legislatives-2024-texte-2026-10-25.md`. PDF de 21,5 Mo non versionné, SHA-256 `8bc4d891a6011ab2f219bfefbdbd2b9eb75e2c47f8182a74ab64faf09b7e8ed4`.
- Utile pour : axe 4 (baisse de la TVA sur l'ensemble des produits énergétiques par loi de finances rectificative ; sortie des règles européennes de fixation du prix de l'électricité ; hausse de 10 % des salaires jusqu'à trois Smic exonérée de hausse de cotisations patronales pendant trois à cinq ans ; suspension de la TVA sur une centaine de produits en cas de forte inflation ; part fiscale complète dès le deuxième enfant ; demi-part des veufs) ; axe 2 (annulation par décret de la réforme de l'assurance chômage de juillet 2024 ; abrogation de la réforme des retraites et système « progressif » favorisant l'entrée précoce et la pénibilité ; carte vitale biométrique, ministère de la lutte contre la fraude, fraude sociale citée à 10 à 25 Md€ d'après la Cour des comptes) ; axe 3 (suppression du droit du sol, délit de séjour irrégulier, AME remplacée par une « aide d'urgence vitale », regroupement familial restreint, suspension des régularisations, demandes d'asile en ambassade, priorité nationale « si nécessaire par référendum constitutionnel », allocations familiales réservées aux Français, 5 ans de travail pour les prestations non contributives comme le RSA) ; axe 5 (peines planchers, suspension des allocations familiales des parents de mineurs récidivistes, majorité pénale à 16 ans, présomption de légitime défense, police municipale obligatoire au-delà de 10 000 habitants, places de prison) ; axe 1 (audit des comptes publics, rationalisation des agences, suppression des agences régionales de santé, privatisation de l'audiovisuel public) ; axe 6 (RIC législatif, révision de la Constitution réservée au référendum ; refus de transferts de compétences à l'UE en défense et diplomatie).

---

## c. Programme présidentiel 2022 (priorité 3)

Sources : le site du parti héberge la page des 22 mesures et 15 livrets ; le site de campagne 2022 (mlafrance.fr) n'est plus en ligne, ses PDF sont récupérés depuis web.archive.org (index CDX consulté le 2026-10-25). Les livrets « finances », « retraites », « pouvoir d'achat » et « institutions » n'existent pas comme livrets : ces thèmes sont couverts par le chiffrage, le dossier de presse retraites, le manifeste et la profession de foi.

| ID | Document | Date | Source de l'archive | Fichier | Axes |
|---|---|---|---|---|---|
| C-RN-18 | « 22 mesures pour 2022 » | février 2022 | web.archive.org, capture du 2022-02-22 de https://mlafrance.fr/pdfs/22-mesures-pour-2022.pdf ; texte aussi sur https://rassemblementnational.fr/22-mesures | `C-RN-18-programme-2022-22-mesures-2026-10-25.pdf` (3,5 Mo) | tous |
| C-RN-19 | Chiffrage du programme présidentiel | mars 2022 | capture du 2022-03-24, `tracts-chiffrage-programme-presidentiel.pdf` | `C-RN-19-programme-2022-chiffrage-2026-10-25.pdf` (1,8 Mo) | 1, 2, 4 |
| C-RN-20 | Dossier de presse « retraites » | 2022 | capture du 2022-04-10, `dossier-presse-retraites.pdf` | `C-RN-20-programme-2022-dossier-presse-retraites-2026-10-25.pdf` (1,0 Mo) | 2 |
| C-RN-21 | Dossier de presse « chiffrage immigration » | décembre 2021 | capture du 2021-12-02 | `C-RN-21-programme-2022-dossier-presse-chiffrage-immigration-2026-10-25.pdf` (1,0 Mo) | 1, 3 |
| C-RN-22 | Livret « Contrôle de l'immigration » | janvier 2022 | capture du 2022-01-09 ; aussi https://rassemblementnational.fr/documents/projet/projet-controle-de-limmigration.pdf | `C-RN-22-programme-2022-livret-controle-immigration-2026-10-25.pdf` (2,5 Mo) | 3, 6 |
| C-RN-23 | Livret « La sécurité » | février 2022 | capture du 2022-02-01 ; aussi sur le site du parti | `C-RN-23-programme-2022-livret-securite-2026-10-25.pdf` (2,4 Mo) | 5 |
| C-RN-24 | Livret « La lutte contre la fraude » | avril 2022 | capture du 2022-04-06 | `C-RN-24-programme-2022-livret-lutte-contre-fraude-2026-10-25.pdf` (1,8 Mo) | 1, 2 |
| C-RN-25 | Livret « La famille » | février 2022 | capture du 2022-02-10 | `C-RN-25-programme-2022-livret-famille-2026-10-25.pdf` (1,5 Mo) | 4 |
| C-RN-26 | Livret « La jeunesse » | février 2022 | capture du 2022-02-22 | `C-RN-26-programme-2022-livret-jeunesse-2026-10-25.pdf` (1,6 Mo) | 4 |
| C-RN-27 | Tract « Présidence française de l'UE » | 2022-01-18 (date confirmée au contrôle de l'étape 2) | capture du 2022-04-10 | `C-RN-27-programme-2022-presidence-francaise-ue-2026-10-25.pdf` (1,1 Mo) | 6 |
| C-RN-28 | Profession de foi du premier tour | mars 2022 | capture du 2022-03-29, `tracts-profession-de-foi-de-marine-le-pen.pdf` | `C-RN-28-programme-2022-profession-de-foi-t1-2026-10-25.pdf` (7,9 Mo) | tous |
| C-RN-29 | Manifeste « M la France », programme présidentiel complet | mars 2022 | capture du 2022-03-25 ; PDF de 27,6 Mo non versionné, SHA-256 `14cca0fdabd756dad324b44773aec11611ac6d28cca22d75c3a6d077ede10272` | copie texte `C-RN-29-programme-2022-manifeste-m-la-france-texte-2026-10-25.md` | tous |

**Utile pour (contenu factuel) :**
- **[C-RN-18]** Axe 3 : arrêt de l'immigration « par référendum », fin du regroupement familial, asile traité à l'étranger, aides sociales réservées aux Français et 5 ans de travail pour les prestations de solidarité, priorité nationale au logement social et à l'emploi, suppression du droit du sol. Axe 5 : peines planchers, suppression des réductions de peine pour les violences aux personnes, présomption de légitime défense, doublement du nombre de magistrats, 85 000 places de prison en 2027, perpétuité réelle. Axe 4 : TVA de 20 % à 5,5 % sur carburants, fioul, gaz et électricité ; hausse de 10 % des salaires jusqu'à 3 Smic exonérée de cotisations patronales ; exonération d'impôt sur le revenu des moins de 30 ans ; part fiscale complète dès le deuxième enfant ; IFF à la place de l'IFI ; suppression de la CFE. Axe 2 : réindexation des retraites, minimum vieillesse à 1 000 €, refus de tout allongement de l'âge, départ à 60 ans après 40 annuités pour les carrières commencées avant 20 ans. Axe 6 : RIC et proportionnelle (mesure 11), budget de la défense à 55 Md€ en 2027. Axe 1 et 2 : ministère de la lutte contre les fraudes (mesure 22).
- **[C-RN-19]** Axe 1 : 68,3 Md€ de mesures d'économies ou de recettes, dont immigration 16 Md€, fraude 15 Md€, baisse de la contribution à l'UE 5 Md€, agences 8 Md€, IFF 2,5 Md€, retours de TVA 6 Md€ ; 68,3 Md€ de dépenses ou baisses de recettes, dont TVA sur l'énergie 12 Md€, réindexation des retraites, réforme des retraites 6 Md€ lissés (9,6 Md€ en année pleine), exonération d'impôt sur le revenu des jeunes 2 Md€, suppression de la CFE et de la C3S en zones de relocalisation 10 Md€.
- **[C-RN-20]** Axe 2 : taux plein dès 60 ans avec 40 annuités pour les personnes entrées dans la vie professionnelle entre 17 et 20 ans ; dispositif progressif au-delà ; taux plein automatique maintenu à 67 ans pour les entrées tardives.
- **[C-RN-21] et [C-RN-22]** Axe 3 : chiffrage de l'immigration et projet de référendum sur l'immigration (révision constitutionnelle). À relire pour les fiches axes.
- **[C-RN-23]** Axe 5 : 1,5 Md€ par an de budget supplémentaire sécurité et justice, 7 000 postes de policiers et gendarmes, 3 000 postes administratifs, police municipale dans les communes de plus de 10 000 habitants.
- **[C-RN-24] à [C-RN-28]** : fraude (axes 1 et 2), famille et jeunesse (axe 4), présidence française de l'UE (axe 6), synthèse officielle de premier tour. Non lus en détail à cette étape.
- **[C-RN-29]** Axe 6 : référendum dans les six mois de l'élection pour réviser la Constitution sur l'immigration et la citoyenneté ; primauté de la loi nationale ; axe 1 : diagnostic de dette publique (2 834,3 Md€ cité).

---

## d. Contre-budgets et plans d'économies du groupe RN (priorité 4)

Le groupe RN présente un contre-budget à chaque PLF de la législature. Pour le PLF 2027, aucun contre-budget distinct du plan 2027-2032 de la candidate n'a été trouvé : le plan du 6 octobre 2026 [C-RN-03] en tient lieu, présenté deux jours avant l'examen en commission du PLF 2027 ; les amendements emblématiques du groupe au PLF 2027 sont en section e ([C-RN-51], [C-RN-52]).

### [C-RN-30] Contre-projet de budget du groupe RN pour 2025
- Auteur : groupe RN à l'AN
- Date : 2024-10-16 (présentation à la presse ; PDF créé le même jour)
- Nature : tableau de bilan des amendements RN au PLF et au PLFSS pour 2025, 8 pages avec trois annexes
- URL : https://rassemblementnational.fr/documents/GRN-CONTRE-BUDGET-2025.pdf ; relais : https://lcp.fr/actualites/budget-2025-les-deputes-du-rassemblement-national-presentent-leur-contre-budget-de
- Archivage : PDF archivé, `corpus/C-RN-30-contre-budget-plf-2025-groupe-rn-2024-10-16-2026-10-25.pdf` (0,1 Mo). La note de paysage (source 100) indiquait « pas de PDF primaire trouvé » : il existe.
- Utile pour : grandes masses, en Md€ (signe positif : amélioration du solde) : mesures ménages -22,8 ; entrepreneurs -5,35 ; mesures « anti-rentes, spéculation et fraudes » +21,79 ; collectivités +1,32 ; appareil d'État +4,06 ; immigration +4,1 ; mesures diverses +10,64 ; **bilan pour les finances publiques +13,7**. Axe 4 : TVA sur l'énergie (12 Md€ dont 2 Md€ de retour de TVA déduits, soit -10), TVA sur les produits de première nécessité (-6), part fiscale pleine dès le deuxième enfant (-3), IFF à la place de l'IFI (+3), taxe sur les rachats d'actions à 33 % (+8,8). Axe 2 : suppression de la désindexation des retraites de six mois (-3,6), jours de carence alignés entre public et privé (+0,4). Axe 3 : AME remplacée par l'AMU (+1,2), prime d'activité réservée aux Français (+1), hébergement d'urgence réservé aux personnes en situation régulière (+0,3). Axe 6 : baisse de la contribution à l'UE (+5).

### [C-RN-31] Contre-budget 2026 du groupe RN
- Auteur : groupe RN à l'AN
- Date : 2025-10-23 (conférence de presse ; PDF créé le 2025-10-24)
- Nature : présentation de 8 pages, base PLF 2026
- URL : https://rassemblementnational.fr/documents/GRN-CONTRE-BUDGET-2026.pdf
- Archivage : PDF archivé, `corpus/C-RN-31-contre-budget-plf-2026-groupe-rn-2025-10-23-2026-10-25.pdf` (0,9 Mo)
- Utile pour : grandes masses affichées : baisses de dépenses de 57 Md€ et nouvelles dépenses de 7 Md€ ; nouvelles recettes de 31 Md€ et baisses d'impôts de 45 Md€ ; **36 Md€ d'économies dégagées** (tableau détaillé : 88,274 Md€ d'économies et recettes, 52,674 Md€ de baisses de recettes et de hausses de dépenses, solde 35,6 Md€). Axe 1 : contribution à l'UE (-8,7), agences et opérateurs (-7,7), aide publique au développement (-2,3), dotation globale de fonctionnement des régions et intercommunalités (-5). Axe 3 : prestations de solidarité réservées aux étrangers ayant 5 ans de travail à temps plein (6,1), AME remplacée par l'AMU (1,3), fin de l'accord de 1968 avec l'Algérie (1,3), suppression du visa pour soins (1). Axe 2 : plan de lutte contre les fraudes (3,5), contrôle systématique de l'éligibilité aux affections de longue durée (0,45), lancement de la réforme des retraites de Marine Le Pen (coût 1,5), indexation des retraites et dégel des prestations (coût 3,61). Axe 4 : TVA sur les énergies, carburants compris (10,96), TVA supprimée sur 100 produits (3,5), indexation du barème de l'impôt sur le revenu (1,9), part fiscale pleine dès le deuxième enfant (2,86), suppression de la CFE, de la CVAE et de la C3S (16,2), IFF (+4), taxe sur les rachats d'actions (+8,4). Comparaison affichée avec le budget du gouvernement : prélèvements obligatoires +19 Md€ pour le budget Lecornu, -1 Md€ pour le contre-budget.

---

## e. Propositions de loi, de résolution et amendements du groupe RN (priorité 5)

Sélection : 17 textes déposés entre septembre 2024 et septembre 2026, premier signataire membre du groupe RN au moment du dépôt (sauf [C-RN-42], premier signataire UDR, retenu à la demande parce qu'il porte la priorité nationale), plus 3 amendements emblématiques. Identification par le jeu open data « Dossiers législatifs » de l'Assemblée (téléchargé le 2026-10-25), croisé avec les groupes des députés ; quatre premières signataires ont un mandat de députée clos au 25 octobre 2026 (Pascale Bordes le 13 avril 2026, Edwige Diaz, Sylvie Josserand et Manon Bouquin le 30 septembre 2026) ; leur fiche de députée les rattache au groupe Rassemblement National. Statuts relevés dans les actes du dossier au 2026-10-25. PDF : `https://www.assemblee-nationale.fr/dyn/opendata/<identifiant>.pdf` ; dossiers : `https://www.assemblee-nationale.fr/dyn/17/dossiers/<slug>`.

**Journées réservées du groupe RN :** 31 octobre 2024 (retraites, peines planchers, expulsions, médecins en cumul emploi-retraite, logement et diagnostic de performance énergétique, hydroélectricité) ; 30 octobre 2025 (accords franco-algériens, délit de séjour irrégulier, frais bancaires, étiquetage d'origine, handicap, parkings d'hôpitaux) ; 8 octobre 2026 (eau potable outre-mer, commande publique, Schengen, Panthéon, zones à faibles émissions ; logement social, subventions aux associations et mention « Mort pour le service de la Nation » annoncés par LCP, non discutés selon les actes).

| ID | N° | Titre court | Premier signataire | Dépôt | Axe | Statut au 2026-10-25 | Scrutin de la liste gelée | PDF archivé |
|---|---|---|---|---|---|---|---|---|
| C-RN-33 | PPL 284 | Annuler les dernières réformes sur l'âge de départ et les annuités (retraites) | Thomas Ménagé | 2024-09-18 | 2 | Rejetée en séance le 31/10/2024 (journée réservée), après suppression de ses articles en commission selon LCP | 217 | 127 Ko |
| C-RN-34 | PPL 262 | Peines planchers pour certains crimes et délits | Pascale Bordes | 2024-09-17 | 5 | Discutée le 31/10/2024, aucune décision enregistrée | | 105 Ko |
| C-RN-35 | PPL 265 | Assouplir l'expulsion des étrangers menaçant gravement l'ordre public | Edwige Diaz | 2024-09-17 | 3 et 5 | Retirée le 31/10/2024 | | 85 Ko |
| C-RN-36 | PPL 344 | Inciter les entreprises à augmenter les salaires nets de 10 % | Jean-Philippe Tanguy | 2024-10-15 | 4 | Déposée, en commission | | 105 Ko |
| C-RN-37 | PPL 364 | Abaisser la majorité pénale à 16 ans | Lionel Tivoli | 2024-10-15 | 5 | Déposée, en commission | | 99 Ko |
| C-RN-38 | PPL 748 | Présomption de légitime défense des forces de l'ordre | Michaël Taverne | 2024-12-19 | 5 | Déposée, en commission (redépôt de la PPL 658, retirée le 04/12/2024) | | 104 Ko |
| C-RN-39 | PPL 1839 | Rétablir le délit de séjour irrégulier | Sylvie Josserand | 2025-09-16 | 3 | Rapport de commission le 22/10/2025, retirée le 30/10/2025 (journée réservée) | | 115 Ko |
| C-RN-40 | PPR 1778 | Dénoncer les accords franco-algériens du 27 décembre 1968 | Guillaume Bigot | 2025-09-09 | 3 et 6 | Adoptée le 30/10/2025 (résolution, art. 34-1 de la Constitution, sans force contraignante) | 3260 | 115 Ko |
| C-RN-41 | PPL 1851 | Limiter les frais bancaires « injustes » | Jean-Philippe Tanguy | 2025-09-16 | 4 | Rapport le 22/10/2025, discutée le 30/10/2025, aucune décision enregistrée | | 107 Ko |
| C-RN-42 | PPLC 2237 | Priorité nationale et locale (révision constitutionnelle) | Christelle D'Intorni (UDR), 13 cosignataires dont 10 RN | 2025-12-11 | 3 et 6 | Déposée, en commission | | 96 Ko |
| C-RN-43 | PPL 2826 | Abroger le titre de séjour pour soins | René Lioret | 2026-05-26 | 3 | Déposée, en commission | | 103 Ko |
| C-RN-44 | PPL 1626 | TVA à 0 % sur des produits pour bébés | Caroline Parmentier | 2025-06-24 | 4 | Déposée, en commission (7 cosignataires) | | 98 Ko |
| C-RN-45 | PPL 425 | Transparence sur les détenteurs de la dette de l'État | Kévin Mauvieux | 2024-10-15 | 1 | Déposée, en commission | | 96 Ko |
| C-RN-46 | PPR 2067 | Commission d'enquête pour « lever les incertitudes budgétaires » de la sécurité sociale | Joëlle Mélin | 2025-11-06 | 1 et 2 | Rapport de commission le 02/12/2025, pas d'examen en séance relevé | | 106 Ko |
| C-RN-47 | PPR 3119 | Refonder l'espace Schengen par une double frontière nationale et européenne | Manon Bouquin | 2026-09-10 | 3 et 6 | Rejetée le 08/10/2026 (journée réservée) | 8611 | 124 Ko |
| C-RN-48 | PPR 3115 | Commande publique au service de l'emploi et de la production en France | Alexandre Loubet | 2026-09-07 | 4 et 6 | Rejetée le 08/10/2026 (journée réservée) | | 120 Ko |
| C-RN-49 | PPL 3109 | Responsabilité des occupants et des bailleurs dans le logement social | Lionel Tivoli | 2026-08-25 | 3, 4 et 5 | Rapport de commission le 29/09/2026, annoncée pour le 08/10/2026, pas de discussion relevée | | 113 Ko |
| C-RN-50 | Amdt I-792, PLF 2026 | TVA à 5,5 % sur gaz, électricité, fioul et carburants | Marine Le Pen et le groupe RN | 2025-10-21 | 4 | Rejeté | 4038 | 4 Ko |
| C-RN-51 | Amdt I-640, PLF 2027 | Exonération d'impôt sur le revenu des actifs jusqu'à 30 ans | Jean-Philippe Tanguy et le groupe RN | 2026-10-08 | 4 | Rejeté | 8747 (complément candidat, non retenu au gel) | 72 Ko |
| C-RN-52 | Amdt I-665, PLF 2027 | Exonération de droits de succession sur 300 000 € d'immeubles en ligne directe | Sophie-Laurence Roy et le groupe RN | 2026-10-08 | 4 | Rejeté | 8854 (réserve) | 8 Ko |

Fichiers : `corpus/C-RN-<nn>-<type>-<numéro>-<objet>-2026-10-25.pdf`. L'amendement n° 58 du scrutin 351 (taxe de délivrance des titres de séjour) est de l'UDR (Éric Ciotti) et n'entre pas dans ce corpus.

**Fiches courtes**

- **[C-RN-33] PPL n° 284.** https://www.assemblee-nationale.fr/dyn/17/dossiers/restaurer_systeme_retraite_juste_annulation_dernieres_reformes. Âge légal ramené de 64 à 62 ans ; durée de cotisation pour le taux plein fixée à 168 trimestres (42 annuités) à compter de la génération 1961 au lieu de 172 (43 annuités) ; dispositifs de carrières longues ajustés. Axe 2.
- **[C-RN-34] PPL n° 262.** https://www.assemblee-nationale.fr/dyn/17/dossiers/peines_planchers_crimes_delits. Seuils minimaux pour les crimes et délits en récidive, le trafic de stupéfiants et les atteintes aux personnes dépositaires de l'autorité publique (par exemple cinq ans pour un crime puni de quinze ans, dix-huit mois pour un délit puni de trois ans), dérogation par décision spécialement motivée. Axe 5.
- **[C-RN-35] PPL n° 265.** https://www.assemblee-nationale.fr/dyn/17/dossiers/assouplir_conditions_expulsion_etrangers_menace_grave_ordre_public. L'administration est « tenue d'expulser » l'étranger dont la présence constitue une menace grave pour l'ordre public, présumée après une condamnation à une peine d'au moins trois ans ; protections catégorielles réduites, mineurs exclus. Axes 3 et 5.
- **[C-RN-36] PPL n° 344.** https://www.assemblee-nationale.fr/dyn/17/dossiers/favoriser_augmentation_salaires_nets. Exonération de cotisations patronales sur la seule majoration, pour les entreprises qui augmentent d'au moins 10 % les salaires inférieurs à trois Smic par accord d'entreprise, de 2025 à 2027. Reprend la mesure 5 de 2022 [C-RN-18] et le programme 2024 [C-RN-17]. Axe 4.
- **[C-RN-37] PPL n° 364.** https://www.assemblee-nationale.fr/dyn/17/dossiers/abaisser_majorite_penale. Les règles propres aux mineurs ne s'appliquent plus qu'aux mineurs de moins de 16 ans ; abrogation de l'article L. 121-7 du code de la justice pénale des mineurs. Axe 5.
- **[C-RN-38] PPL n° 748.** https://www.assemblee-nationale.fr/dyn/17/dossiers/presomption_legitime_defense_forces_ordre_xvii. Policiers, gendarmes et militaires réquisitionnés, en uniforme et dans l'exercice de leurs fonctions, présumés en état de légitime défense ; rapport sur la formation au tir. Axe 5.
- **[C-RN-39] PPL n° 1839.** https://www.assemblee-nationale.fr/dyn/17/dossiers/retablissement_du_delit_de_sejour_irregulier_17e. Séjour irrégulier d'un majeur puni de 3 750 € d'amende et, en peine complémentaire, de trois ans d'interdiction du territoire. Texte proche de la PPL n° 764 (Antoine Villedieu, 2024-12-19, en commission). Axe 3.
- **[C-RN-40] PPR n° 1778.** https://www.assemblee-nationale.fr/dyn/17/dossiers/denoncer_accords_franco_algeriens_27_decembre_1968. Appelle les autorités compétentes à dénoncer l'accord de 1968, au motif d'un régime dérogatoire d'entrée et de séjour, d'une coopération jugée insuffisante sur les laissez-passer consulaires et de la situation des droits de l'homme en Algérie. Le contre-budget 2026 en chiffre la fin à 1,3 Md€ [C-RN-31]. Axes 3 et 6.
- **[C-RN-41] PPL n° 1851.** https://www.assemblee-nationale.fr/dyn/17/dossiers/limiter_frais_bancaires_injustes_17e. Interdiction des commissions d'intervention sur les incidents de paiement des particuliers, associations et petites entreprises ; plafonnement des frais de rejet de chèque à 15 ou 30 €. Axe 4.
- **[C-RN-42] PPLC n° 2237.** https://www.assemblee-nationale.fr/dyn/17/dossiers/priorite_nationale_locale_17e. Ajoute à l'article 1er de la Constitution une « priorité nationale et locale » dans l'accès à certains droits et avantages ; permet à une loi organique ou référendaire de déroger à la primauté du droit de l'Union, aucun traité ni principe constitutionnel n'étant opposable à son exécution ; crée un article 51-3 donnant compétence au Parlement en la matière. **Premier signataire UDR** ; dix députés RN cosignataires, dont Sébastien Chenu. Axes 3 et 6.
- **[C-RN-43] PPL n° 2826.** https://www.assemblee-nationale.fr/dyn/17/dossiers/abroger_titre_de_sejour_pour_soins_17e. Abrogation du titre de séjour pour étranger malade (articles L. 425-9 et L. 425-10 du code de l'entrée et du séjour), avec disposition transitoire. Correspond à la « suppression du visa pour soins » du contre-budget 2026 (1 Md€) [C-RN-31]. Axe 3.
- **[C-RN-44] PPL n° 1626.** https://www.assemblee-nationale.fr/dyn/17/dossiers/supprimer_taxe_sur_la_valeur_ajoutee_produits_premiere_necessite_pour_familles_accueillant_un_bebe_17e. TVA à 0 % sur une liste de produits alimentaires et d'hygiène pour bébés fixée par décret. Axe 4.
- **[C-RN-45] PPL n° 425.** https://www.assemblee-nationale.fr/dyn/17/dossiers/ameliorer_transparence_dette_exterieure_etat. Rapport annuel au Parlement sur les détenteurs de la dette de l'État par nationalité et type d'investisseur. Axe 1, portée limitée.
- **[C-RN-46] PPR n° 2067.** https://www.assemblee-nationale.fr/dyn/17/dossiers/incertitudes_budgetaires_securite_sociale. Commission d'enquête de 30 membres chargée d'auditer les financements et le contrôle de la sécurité sociale à partir des réserves de la Cour des comptes. Axes 1 et 2.
- **[C-RN-47] PPR n° 3119.** https://www.assemblee-nationale.fr/dyn/17/dossiers/refonder_lespace_schengen_en_instaurant_une_double_frontiere_nationale_et_europeenne. Invite le gouvernement à soutenir au Conseil une révision du code frontières Schengen pour une « double frontière » (extérieure européenne et nationale) et des vérifications des ressortissants de pays tiers aux frontières intérieures. Axes 3 et 6.
- **[C-RN-48] PPR n° 3115.** https://www.assemblee-nationale.fr/dyn/17/dossiers/mobiliser_commande_publique_service_emploi_production_innovation_france_17e. Appelle à autoriser les acheteurs publics à donner priorité aux offres exécutées en France ; cite une commande publique de près de 400 Md€ par an. Annoncée par LCP comme texte de « priorité nationale dans la commande publique ». Axes 4 et 6 (droit de l'Union).
- **[C-RN-49] PPL n° 3109.** https://www.assemblee-nationale.fr/dyn/17/dossiers/renforcer_responsabilite_occupants_bailleurs_logement_social_17e. Attribution d'un logement social subordonnée à l'absence de condamnation définitive pour un crime ou délit puni d'au moins deux ans dans les cinq ans précédents ; règlement intérieur opposable par immeuble. Rejoint la rentrée du 13 septembre 2026 [C-RN-06]. Axes 3, 4 et 5.
- **[C-RN-50] Amendement I-792 au PLF 2026.** https://www.assemblee-nationale.fr/dyn/17/amendements/1906A/AN/792. Taux de 5,5 % pour les « énergies de première nécessité » (gaz, électricité, fioul, carburants), gagé sur la taxe sur les transactions financières et les tabacs. Axe 4.
- **[C-RN-51] Amendement I-640 au PLF 2027.** https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/AN/640. Revenus d'activité des personnes de 30 ans au plus exonérés d'impôt sur le revenu dans la limite de quatre Smic annuels, à partir des revenus 2027 ; l'exposé indique reprendre l'engagement de Marine Le Pen du 22 février 2022 « dans la perspective de 2027 ». Axe 4.
- **[C-RN-52] Amendement I-665 au PLF 2027.** https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/AN/665. Exonération de droits de succession des immeubles détenus en direct, dans la limite de 300 000 €, pour les ascendants et enfants, cumulable avec l'abattement de 100 000 €. Le chiffrage 2022 prévoyait déjà une exonération à hauteur de 300 000 € [C-RN-19]. Axe 4.

**Annoncés ou cherchés, non trouvés :** aucune PPL du groupe RN sur le RIC, la proportionnelle ou le référendum dans la législature (thèmes présents dans les programmes [C-RN-17], [C-RN-18]) ; aucune PPL RN sur la règle d'or budgétaire (les PPLC sur ce thème sont Horizons, UDR et LR) ; aucune PPL RN sur l'AME ou la condition de 5 ans de travail pour les prestations (ces mesures figurent dans les contre-budgets). Aucune PPL constitutionnelle de Marine Le Pen elle-même n'a été trouvée sur la période.

---

## f. Déclarations publiques depuis le 1er janvier 2026 (priorité 6)

23 déclarations (22 à l'étape 1, plus [C-RN-83] ajoutée le 2026-10-25) : Marine Le Pen 13, Jordan Bardella 6, Jean-Philippe Tanguy 2, Sébastien Chenu 1, délégation RN au Parlement européen 1. « Site du parti » : texte publié par le RN (partie prenante), archivé. « Relais » : reprise par un média tiers, le média d'origine est indiqué. Une déclaration couvrant plusieurs axes tient sur une seule ligne. Les déclarations déjà fiches en section a sont renvoyées.

| ID | Date | Média d'origine | Format | Axe | Position (résumé) | URL |
|---|---|---|---|---|---|---|
| C-RN-61 | 2026-01-23 | séance de l'AN, rapportée par Euronews | intervention | 6 | Motion de censure RN contre le recours au 49.3 sur le PLF 2026 ; usage jugé légal mais qualifié d'abus de la Constitution (traduction de l'anglais) | https://euronews.com/2026/01/23/french-government-avoids-collapse-after-surviving-two-no-confidence-votes (relais) |
| C-RN-62 | 2026-02-18 | conférence de presse au siège | discours | 5 et 6 | Interdictions administratives de manifester, pointage, liste d'organisations à risque, tutelle d'universités ; voir [C-RN-09] | https://rassemblementnational.fr/conferences-de-presse/communique-de-presse-6 (site du parti, texte archivé) |
| C-RN-63 | 2026-05-01 | Fête de la Nation | discours | 1, 3 et 4 | Baisse massive des taxes dont la TVA, 15 Md€ par an ; fin de l'AME ; Schengen réservé aux ressortissants de l'UE ; voir [C-RN-08] | https://rassemblementnational.fr/discours/fete-de-la-nation-discours-de-jordan-bardella (site du parti, texte archivé) |
| C-RN-64 | 2026-05-05 | CNews | interview | 3 et 6 | Référendum sur l'immigration « dès notre arrivée au pouvoir » si le RN gagne | https://www.cnews.fr/france/2026-05-05/si-les-francais-nous-accorde-leur-confiance-nous-organiserons-un-referendum-sur (page non ouverte, 403 ; titre et extrait seulement) |
| C-RN-65 | 2026-05-22 (date déduite) | BFMTV | interview | 6 | Sortie du commandement militaire intégré de l'OTAN dans le quinquennat, maintien dans l'Alliance | https://www.21news.be/marine-le-pen-veut-sortir-la-france-du-commandement-integre-de-lotan/ (relais, fiabilité du site non établie) |
| C-RN-66 | 2026-07-07 | TF1 (20 h) | interview | 6 | Maintien de la candidature après l'arrêt d'appel, pourvoi en cassation ; voir [C-RN-13] | https://www.aljazeera.com/news/2026/7/7/french-far-right-leader-le-pen-says-will-run-in-2027-presidential-election (relais) |
| C-RN-67 | 2026-08-27 | Medef, Rencontre des entrepreneurs de France | débat | 1, 2 et 4 | 125 Md€ d'économies ; 60 ans pour les entrées avant 20 ans, 62 ans à terme, 42 annuités, 9 Md€ ; suppression C3S, CVAE, CFE ; voir [C-RN-05] | https://www.sudradio.fr/societe/marine-le-pen-et-la-delicate-operation-seduction-du-monde-economique (relais) |
| C-RN-68 | 2026-09-13 | discours de rentrée, Hénin-Beaumont | discours | 3 et 4 | Priorité nationale au logement social, APL réservées aux Français, abrogation de la loi SRU ; voir [C-RN-06] | https://france3-regions.franceinfo.fr/hauts-de-france/pas-calais/lens/marine-le-pen-fait-sa-rentree-politique-a-henin-beaumont-et-met-la-priorite-nationale-au-c-ur-de-son-programme-pour-la-presidentielle-de-2027-3416348.html (relais) |
| C-RN-69 | 2026-09-16 | LCI | interview | 3, 5 et 6 | Interdiction progressive du voile (universités, sorties scolaires, fédérations sportives, bâtiments publics) après un référendum contre les idéologies islamistes ; référendum constitutionnel sur l'immigration à la prise de fonction | https://www.lavenir.net/actu/monde/2026/09/17/france-en-cas-de-victoire-marine-le-pen-veut-interdire-le-voile-de-maniere-progressive-4BGF3FXFXZBX7OL5YSN42XFUXM/ (relais Belga) |
| C-RN-70 | septembre 2026 (date non précisée) | rapportée par LCP (Marine Le Pen, locutrice confirmée au contrôle de l'étape 2) | déclaration | 1 et 4 | Préfère un budget 2027 « imparfait » à une loi spéciale, sans chèque en blanc ; refus de toute hausse d'impôt ; exige des économies | https://lcp.fr/actualites/budget-2027-le-gouvernement-sur-un-fil-a-la-veille-de-l-ouverture-des-debats-a-l (relais) |
| C-RN-71 | 2026-10-06 | conférence de presse au siège | discours | 1, 2 et 4 | 140 Md€ nets en 2032, déficit sous 3 % en 2030, dette à 112 %, règle d'or par référendum, 30 Md€ nets de baisses d'impôts, retraites à 62 voire 60 ans avec capitalisation ; voir [C-RN-03] | https://www.europe1.fr/politique/budget-2027-marine-le-pen-promet-140-milliards-deuros-nets-deconomies-dici-2032-pour-eviter-a-la-france-le-defaut-de-paiement-1126400 (relais) |
| C-RN-72 | 2026-10-06 | conférence de presse au siège | discours | 1 et 6 | Jordan Bardella : 9 Md€ d'économies sur la contribution française à l'UE | https://www.publicsenat.fr/actualites/politique/140-milliards-deuros-deconomies-dici-2032-leffort-radical-propose-par-marine-le-pen-pour-redresser-les-f (relais) |
| C-RN-73 | 2026-10-11 | BFMTV | interview | 1 et 2 | Jean-Philippe Tanguy : la désindexation des retraites est une « ligne rouge » ; pas de censure automatique, Marine Le Pen décide | https://lcp.fr/actualites/budget-2027-le-gouvernement-sur-un-fil-a-la-veille-de-l-ouverture-des-debats-a-l (relais) |
| C-RN-74 | 2026-10-13 | déclaration à la presse | déclaration | 1 et 6 | Jean-Philippe Tanguy : le groupe ne votera pas la motion de rejet socialiste du PLF 2027 | https://entrevue.fr/politique/budget-2027-le-rn-refuse-de-suivre-les-socialistes-jean-philippe-tanguy/ (relais) |
| C-RN-75 | 2026-10-14 | conférence de presse à Bruxelles | discours | 2 | Âge légal « entre 60 et 62 ans » selon l'âge d'entrée, 40 à 42 annuités, réforme chiffrée le 17 novembre ; voir [C-RN-07] | https://www.franceinfo.fr/elections/presidentielle/marine-le-pen-presentera-de-maniere-extremement-precise-sa-reforme-des-retraites-le-17-novembre_8237821.html (relais) |
| C-RN-76 | 2026-10-12 ou 14 | conférence de presse à Bruxelles | discours | 1 et 6 | Contribution nette à l'UE plafonnée à 5 Md€ par an ; fin du financement de l'Ukraine et des sanctions contre la Russie ; voir [C-RN-07] | https://www.euronews.com/2026/10/14/le-pen-lands-in-brussels-lashing-out-at-the-european-commission (relais) |
| C-RN-77 | 2026-10-18 | vidéo sur ses réseaux, rapportée par Europe 1 | déclaration | 5 | Après les violences du 17 octobre : « la règle du casseur-payeur » ; appel au calme | https://www.europe1.fr/politique/violences-du-17-octobre-marine-le-pen-denonce-une-menace-sur-la-democratie-et-un-pouvoir-macroniste-epuise-1160592 (relais ; page de presse lue via outil, accès direct non testé) |
| C-RN-78 | 2026-10-18 | RTL et Public Sénat (Le Grand Jury), rapporté par Capital | interview | 2 | Sébastien Chenu : borne d'âge à 60 ou 62 ans avec 40 ou 42 annuités, coût de 9 Md€ ; « réforme de société », pas paramétrique | https://fr.finance.yahoo.com/actualites/s%C3%A9bastien-chenu-refuse-bidouiller-param%C3%A8tres-134630945.html (relais de Capital) |
| C-RN-79 | 2026-10-19 | conférence de presse au siège | déclaration | 5 | Jordan Bardella met en cause l'ultragauche dans les violences du 17 octobre ; appelle à « tous les moyens légaux possibles » pour rétablir l'ordre | https://www.titrespresse.com/25729932603/jordan-bardella-rn (relais de BFMTV) ; https://www.cnews.fr/france/2026-10-19/mobilisation-du-17-octobre-jordan-bardella-met-en-cause-lfi-et-fustige-une (page non ouverte) |
| C-RN-80 | 2026-10-22 | communiqué de la délégation RN au Parlement européen | communiqué | 1 et 6 | Vote contre le budget de l'UE pour 2027 ; demande la réduction de la contribution française | https://rassemblementnational.fr/communiques/budget-europeen-2027-bruxelles-depense-toujours-plus-sans-compter (site du parti, texte archivé `corpus/C-RN-80-...md`) |
| C-RN-81 | 2026-10-25 | meeting d'Orléans | discours | 2, 3, 5 et 6 | Primauté de la Constitution, priorité nationale, référendum, proportionnelle avec prime majoritaire, expulsion automatique des étrangers délinquants ; âge de départ pas au-delà de 64 ans (Reuters) ; voir [C-RN-11] | https://www.boursorama.com/actualite-economique/actualites/marine-le-pen-dit-vouloir-presider-a-la-renaissance-de-la-france-23c3b9f98b2bd33f3acb553dafc26e5b (relais Reuters) |
| C-RN-82 | 2026-10-25 | meeting d'Orléans | discours | 5 | Jordan Bardella : présomption de légitime défense, peines planchers, majorité pénale à 16 ans ; voir [C-RN-16] | https://www.24heures.ch/bardella-le-president-du-rn-reelu-avec-pres-de-99-des-voix-642797530461 (relais) |
| C-RN-83 | 2026-10-14 | conférence de presse à Bruxelles (rapportée par Les Surligneurs le 20 octobre, relais) | déclaration | 3 et 6 | La candidate précise la voie de l'article 11 de la Constitution pour « constitutionnaliser » le droit des étrangers par référendum, sans passer par l'article 89 ; ajout du 2026-10-25 à la demande de l'étape 3 (fiche axe 3) ; voir [C-RN-07] | https://lessurligneurs.eu/le-rassemblement-national-pourra-t-il-modifier-la-constitution-par-referendum/ (relais, site de vérification juridique animé par des universitaires) |

Répartition par axe (une déclaration peut compter pour plusieurs) : axe 1 : 9 ; axe 2 : 6 ; axe 3 : 5 ; axe 4 : 5 ; axe 5 : 6 ; axe 6 : 9.

Archivage (règle v2) : les trois déclarations publiées par le parti lui-même sont archivées en texte ([C-RN-62] dans `C-RN-09-...md`, [C-RN-63] dans `C-RN-08-...md`, [C-RN-80]). La campagne ne publie pas ses interventions sur marinelepen.com ; les autres déclarations sont en lien seul. Les comptes rendus de presse sur le discours d'Orléans datent du jour même et sont susceptibles d'être complétés.

---

## Actes

Non applicable : le RN n'a jamais exercé le pouvoir au niveau national (gouvernement ou majorité) sur la fenêtre couverte.
Renvoi : `00-perimetre.md`, section « Attribution des actes » (la comparaison programme / actes de Q4 est non applicable, le verdict C repose sur discours, programme et votes).
Les exécutifs locaux dirigés par le RN ne sont pas des actes de gouvernement national et n'entrent pas ici.

---

## Trous

**Non trouvé**
- Programme présidentiel 2027 complet : non publié au 25 octobre 2026.
- Dossier de presse et annexe des 125 mesures du plan du 6 octobre 2026 [C-RN-03] : non publiés en ligne sur les sites du parti et de la campagne ; chiffres connus par la presse et par [C-RN-04].
- Textes intégraux des discours d'Hénin-Beaumont (13 septembre), d'Orléans (25 octobre, Marine Le Pen et Jordan Bardella) et de l'intervention au Medef (27 août) : non publiés ; la page « discours » du parti s'arrête au 2 mai 2026.
- Contre-budget du groupe RN distinct pour le PLF 2027 : non trouvé (le plan du 6 octobre en tient lieu).
- Texte d'orientation ou motion adoptés par le congrès d'Orléans ou par un conseil national depuis 2024 : aucun trouvé.
- Réforme des retraites détaillée : annoncée pour le 17 novembre 2026, hors corpus.
- PPL RN sur le RIC, la proportionnelle, le référendum ou la règle d'or : aucune trouvée dans la législature.
- Livrets 2022 « finances », « retraites », « institutions » : n'existent pas comme livrets ; contenus couverts par [C-RN-19], [C-RN-20], [C-RN-29].
- Déclarations de 2026 sur l'assurance chômage, les arrêts maladie et la fraude sociale par Marine Le Pen ou Jordan Bardella : rien de vérifiable trouvé.

**Connu seulement par la presse**
- Toutes les déclarations de la section f sauf [C-RN-62], [C-RN-63] et [C-RN-80]. Pages CNews non ouvertes (accès refusé, 403) : contenu tiré des titres et extraits.
- Date de la conférence de presse de Bruxelles : 14 octobre selon franceinfo, « lundi » (12 octobre) selon Euronews.
- Positions sur l'OTAN : sortie du commandement intégré en 2022 [C-RN-29, p. 4] (absente des 22 mesures [C-RN-18], correction du contrôle de l'étape 2), gel « en période de guerre » en 2024 et relance en mai 2026 [C-RN-65] selon des analyses de presse ; la position de 2024 n'est pas documentée par une source primaire du corpus.
- Retraites en juin 2024 : report de l'abrogation par Jordan Bardella (« Nous verrons ») puis précisions sur TF1 (60 ans avec 40 annuités pour les entrées avant 20 ans, 62 ans et 42 annuités sinon), connues par la presse (sources secondaires 29 et 30), antérieures à la fenêtre des déclarations.

**Divergences internes à documenter (comptent pour Q4)**
- Âge de départ : la PPL n° 284 ramène l'âge légal à 62 ans pour tous [C-RN-33] et la candidate parle le 14 octobre d'un âge légal « entre 60 et 62 ans » [C-RN-75] ; selon Reuters, elle s'engage le 25 octobre seulement à ne pas porter l'âge au-delà de 64 ans [C-RN-81]. Incompatibilité à établir sur le texte prononcé (relais unique, formulation de l'agence) : cas limite, à confirmer avant de le compter.
- Contribution à l'UE : plafonnement de la contribution nette à 5 Md€ par an, soit une baisse d'environ 3 Md€ d'après Euronews [C-RN-76], contre une économie de 9 Md€ annoncée le 6 octobre [C-RN-72] et 13,1 Md€ en 2031 dans l'annexe selon [C-RN-04]. Possible divergence de montant sur le même objet ; à instruire, car la base (contribution nette ou brute) diffère peut-être.

**Écarts de chiffrage et précisions successives (pas des divergences au sens du socle §6, listés pour la vérification)**
- TVA à 5,5 % sur l'énergie : 12 Md€ (2022, [C-RN-19]), 12 Md€ bruts et 10 Md€ nets (contre-budget 2025, [C-RN-30]), 10,96 Md€ carburants compris (contre-budget 2026, [C-RN-31]), 12,2 Md€ en 2027 ([C-RN-04]). Même mesure, exercices et conventions de retour de TVA différents.
- Montant des économies : 125 Md€ annoncés au Medef [C-RN-67], 140 Md€ le 6 octobre [C-RN-71] ; Public Sénat présente l'écart comme un ajout de 15 Md€.
- Coût de la réforme des retraites : 6 Md€ lissés et 9,6 Md€ en année pleine (2022, [C-RN-19]), 1,5 Md€ pour son lancement (contre-budget 2026, [C-RN-31]), 9 Md€ ([C-RN-67], [C-RN-78]), 9,5 Md€ en 2031 dans l'annexe selon [C-RN-04].
- Contribution à l'UE dans les contre-budgets : 5 Md€ (2022 et 2025), 8,7 Md€ (2026), puis voir ci-dessus.
- Prestations aux étrangers : prime d'activité réservée aux Français (contre-budget 2025) puis condition de 5 ans de travail à temps plein pour les prestations de solidarité (contre-budget 2026) et prestations familiales conditionnées à un parent français (annexe 2027 selon [C-RN-04]) : instruments successifs pour un même but, à vérifier en fiche axe 3.

---

## Sources secondaires utilisées pour les statuts et le contexte

1. LCP, « INFO LCP. Les textes que le Rassemblement national défendra à l'Assemblée lors de sa niche parlementaire du 8 octobre », 2026-09-10, mis à jour le 2026-09-25. https://lcp.fr/actualites/info-lcp-les-textes-que-le-rassemblement-national-defendra-a-l-assemblee-lors-de-sa
2. LCP, « Retraites, peines planchers, expulsions... La "niche parlementaire" du RN pleine de pièges pour ses adversaires », 2024. https://lcp.fr/actualites/retraites-peines-planchers-expulsions-la-niche-parlementaire-du-rn-pleine-de-pieges-pour
3. LCP, « Abrogation de la réforme des retraites : après avoir été vidée de sa substance en commission... », 2024-10-31. https://lcp.fr/actualites/abrogation-de-la-reforme-des-retraites-apres-avoir-ete-vide-de-sa-substance-en
4. LCP, « Dénonciation des accords franco-algériens de 1968 : un texte du RN adopté, à une voix près, à l'Assemblée », 2025-10-30. https://lcp.fr/actualites/denonciation-des-accords-franco-algeriens-de-1968-un-texte-du-rn-adopte-a-une-voix-pres
5. LCP, « Budget 2025 : les députés du Rassemblement national présentent leur contre-budget », 2024-10-16. https://lcp.fr/actualites/budget-2025-les-deputes-du-rassemblement-national-presentent-leur-contre-budget-de
6. LCP, « Budget 2027 : le gouvernement sur un fil à la veille de l'ouverture des débats à l'Assemblée », 2026-10-12. https://lcp.fr/actualites/budget-2027-le-gouvernement-sur-un-fil-a-la-veille-de-l-ouverture-des-debats-a-l
7. Public Sénat, « 140 milliards d'euros d'économies d'ici 2032 : l'effort radical proposé par Marine Le Pen pour redresser les finances », 2026-10-06. https://www.publicsenat.fr/actualites/politique/140-milliards-deuros-deconomies-dici-2032-leffort-radical-propose-par-marine-le-pen-pour-redresser-les-f
8. Europe 1, « Budget 2027 : Marine Le Pen promet 140 milliards d'euros nets d'économies d'ici 2032 », 2026-10-06. https://www.europe1.fr/politique/budget-2027-marine-le-pen-promet-140-milliards-deuros-nets-deconomies-dici-2032-pour-eviter-a-la-france-le-defaut-de-paiement-1126400 [relais ; page lue via l'outil de lecture, Europe 1 étant signalé comme bloquant dans le socle §6]
9. Boursorama (dépêche Reuters), « Marine Le Pen veut ramener le déficit budgétaire à 3 % d'ici 2030 », 2026-10-06. https://www.boursorama.com/actualite-economique/actualites/marine-le-pen-veut-ramener-le-deficit-budgetaire-a-3-d-ici-2030-e234d02e0ea563e2766ea6142c4a1bdc
10. Institut de l'Entreprise, « Contre-budget du RN : 140 milliards affichés, moins de 10 milliards crédibles », octobre 2026. https://www.institut-entreprise.fr/wp-content/uploads/2026/10/Analyse-primaire-contre-budget-RN-Note-de-contexte-IDEP.pdf [think tank d'entreprises ; utilisé seulement pour les chiffres du RN qu'il rapporte]
11. franceinfo, « Marine Le Pen présentera "de manière extrêmement précise" sa réforme des retraites le 17 novembre », 2026-10-14. https://www.franceinfo.fr/elections/presidentielle/marine-le-pen-presentera-de-maniere-extremement-precise-sa-reforme-des-retraites-le-17-novembre_8237821.html
12. Euronews, « Le Pen lands in Brussels lashing out at the European Commission », 2026-10-14. https://www.euronews.com/2026/10/14/le-pen-lands-in-brussels-lashing-out-at-the-european-commission
13. France 3 Régions (avec AFP), « Marine Le Pen fait sa rentrée politique à Hénin-Beaumont et met "la priorité nationale" au cœur de son programme », 2026-09-13. https://france3-regions.franceinfo.fr/hauts-de-france/pas-calais/lens/marine-le-pen-fait-sa-rentree-politique-a-henin-beaumont-et-met-la-priorite-nationale-au-c-ur-de-son-programme-pour-la-presidentielle-de-2027-3416348.html
14. Sud Radio, « Marine Le Pen défend ses réformes économiques devant le Medef », août 2026. https://www.sudradio.fr/societe/marine-le-pen-et-la-delicate-operation-seduction-du-monde-economique [article non ouvert, contenu tiré de l'extrait et recoupé par d'autres reprises]
15. Boursorama (dépêche Reuters), « Marine Le Pen dit vouloir présider à la "Renaissance" de la France », 2026-10-25. https://www.boursorama.com/actualite-economique/actualites/marine-le-pen-dit-vouloir-presider-a-la-renaissance-de-la-france-23c3b9f98b2bd33f3acb553dafc26e5b
16. 20 minutes (Suisse, dépêche AFP), « Marine Le Pen promet une renaissance sans rupture brutale à Orléans », 2026-10-25. https://www.20min.ch/fr/story/france-marine-le-pen-promet-une-renaissance-sans-rupture-brutale-103656322
17. franceinfo, « Au congrès du Rassemblement national, l'unique candidat Jordan Bardella est réélu sans surprise à la présidence du parti avec 98,98 % des voix », 2026-10-24. https://www.franceinfo.fr/politique/front-national/au-congres-du-rassemblement-national-l-unique-candidat-jordan-bardella-est-reelu-sans-surprise-a-la-presidence-du-parti-avec-98-98-des-voix_8252326.html
18. 24 heures, « Bardella : le président du RN réélu avec près de 99 % des voix », 2026-10-24 ou 25. https://www.24heures.ch/bardella-le-president-du-rn-reelu-avec-pres-de-99-des-voix-642797530461
19. Orange actu (L'Express via 6medias), « "Je vous demande de vous arrêter" : le discours de Jordan Bardella chahuté lors du congrès du RN », 2026-10-25. https://actu.orange.fr/politique/je-vous-demande-de-vous-arreter-le-discours-de-jordan-bardella-chahute-lors-du-congres-du-rn-l-express-via-6medias-CNT000002tnRYL.html
20. France 24, « Marine Le Pen candidate en 2027 », 2026-07-08. https://www.france24.com/fr/france/20260708-marine-le-pen-candidate-en-2027-un-choix-dynastique-du-rn-qui-%C3%A9clipse-jordan-bardella
21. Al Jazeera, « French far-right leader Le Pen says will run in 2027 presidential election », 2026-07-07. https://www.aljazeera.com/news/2026/7/7/french-far-right-leader-le-pen-says-will-run-in-2027-presidential-election
22. L'Avenir (dépêche Belga), « En cas de victoire, Marine Le Pen veut interdire le voile "de manière progressive" », 2026-09-17. https://www.lavenir.net/actu/monde/2026/09/17/france-en-cas-de-victoire-marine-le-pen-veut-interdire-le-voile-de-maniere-progressive-4BGF3FXFXZBX7OL5YSN42XFUXM/
23. 21News, « Marine Le Pen veut sortir la France du commandement intégré de l'OTAN », 2026-05-23. https://www.21news.be/marine-le-pen-veut-sortir-la-france-du-commandement-integre-de-lotan/ [21News : site d'information belge, relais, fiabilité non établie ; étiquette proposée ci-dessous]
24. Europe 1, « Violences du 17 octobre : Marine Le Pen dénonce "une menace sur la démocratie" », 2026-10-18. https://www.europe1.fr/politique/violences-du-17-octobre-marine-le-pen-denonce-une-menace-sur-la-democratie-et-un-pouvoir-macroniste-epuise-1160592
25. Capital via Yahoo Finance, « Sébastien Chenu refuse de "bidouiller des paramètres" et chiffre à 9 milliards la réforme des retraites de Marine Le Pen », 2026-10-18. https://fr.finance.yahoo.com/actualites/s%C3%A9bastien-chenu-refuse-bidouiller-param%C3%A8tres-134630945.html
26. Entrevue, « Budget 2027 : le RN refuse de suivre les socialistes, Jean-Philippe Tanguy dénonce une opposition "grotesque" », 2026-10-13. https://entrevue.fr/politique/budget-2027-le-rn-refuse-de-suivre-les-socialistes-jean-philippe-tanguy/
27. CNews, « "Si les Français nous accorde leur confiance, nous organiserons un référendum sur l'immigration dès notre arrivée au pouvoir", promet Jordan Bardella », 2026-05-05. https://www.cnews.fr/france/2026-05-05/si-les-francais-nous-accorde-leur-confiance-nous-organiserons-un-referendum-sur [chaîne d'information classée à droite ; page non ouverte, 403]
28. Titres Presse (relais de BFMTV), « Jordan Bardella appelle au déploiement de "tous les moyens légaux possibles" », 2026-10-19. https://www.titrespresse.com/25729932603/jordan-bardella-rn [agrégateur, relais]
29. Public Sénat, « Réforme des retraites, impôts, prix planchers : comment le RN réajuste son programme au fil de la campagne », juin 2024. https://www.publicsenat.fr/actualites/politique/reforme-des-retraites-impots-prix-planchers-comment-le-rn-reajuste-son-programme-au-fil-de-la-campagne
30. Boursorama, « Retraites : Jordan Bardella n'est plus si pressé d'abroger la réforme de Macron », 2024-06-12. https://www.boursorama.com/bourse/actualites/retraites-jordan-bardella-n-est-plus-si-presse-d-abroger-la-reforme-de-macron-101b949b9967c92520b3be1c9ef2c30f
31. Euronews, « French government avoids collapse after surviving two no-confidence votes », 2026-01-23. https://euronews.com/2026/01/23/french-government-avoids-collapse-after-surviving-two-no-confidence-votes
32. Assemblée nationale, jeu de données « Dossiers législatifs » de la XVIIe législature (open data), téléchargé le 2026-10-25. https://data.assemblee-nationale.fr/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip ; et « Députés actifs, mandats et organes ». https://data.assemblee-nationale.fr/static/openData/repository/17/amo/deputes_actifs_mandats_actifs_organes/AMO10_deputes_actifs_mandats_actifs_organes.json.zip
33. Assemblée nationale, pages d'analyse des scrutins 4038, 8747 et 8854 (consultées pour le numéro d'amendement seulement). https://www.assemblee-nationale.fr/dyn/17/scrutins/4038 ; https://www.assemblee-nationale.fr/dyn/17/scrutins/8747 ; https://www.assemblee-nationale.fr/dyn/17/scrutins/8854
34. web.archive.org, index des PDF de mlafrance.fr (CDX), consulté le 2026-10-25. http://web.archive.org/cdx/search/cdx?url=mlafrance.fr*&filter=mimetype:application/pdf

## Ajouts proposés

- Étiquette proposée pour le registre : [21News : site d'information belge en ligne, relais ; ligne et fiabilité non établies]. Justification : aucune autodéfinition ni classement trouvé ; utilisé une seule fois, faute d'autre relais ouvert pour [C-RN-65].
- Discours de Jordan Bardella de la campagne municipale (Perpignan 28 février, Nîmes 4 mars, Menton 7 mars, Châlons-en-Champagne 18 mars 2026), publiés en texte sur rassemblementnational.fr/discours : non retenus (campagne municipale), archivables si une fiche axe en a besoin.
