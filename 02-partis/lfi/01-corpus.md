# LFI : corpus programmatique

- Rédigé le : 2026-10-26
- Date d'arrêt des données : 2026-10-28 (réalignée à la synthèse le 2026-10-28 ; arrêt initial le 2026-10-26 ; veille commune `04-synthese/travail/veille-2026-10-28.md`)
- Auteur : sous-agent Opus, étape 1 (section f préparée par un second sous-agent Opus, relue et intégrée)
- Statut : brouillon (étape 1)
- Règle appliquée : `01-socle/01-criteres.md` §6 (hiérarchie du corpus) et `01-socle/03-sources-et-hierarchie.md` (archivage, étiquetage)

Périmètre (voir `00-perimetre.md`) : le mouvement La France insoumise (LFI), le groupe « La France insoumise - Nouveau Front Populaire » (LFI-NFP) à l'Assemblée nationale, et son candidat déclaré Jean-Luc Mélenchon (fondateur du mouvement). Manuel Bompard, coordinateur national, parle pour le mouvement ; Mathilde Panot, présidente du groupe, parle pour le groupe. Les autres composantes du Nouveau Front populaire (NFP) sont hors périmètre ; leurs textes communs avec LFI sont signalés « texte commun », un texte dont le premier signataire appartient à un autre groupe est signalé comme tel.

Sigles utilisés : AN (Assemblée nationale), AR (Assemblée représentative, instance de LFI), NFP (Nouveau Front populaire), NUPES (Nouvelle Union populaire écologique et sociale, 2022), LAEC (« L'Avenir en commun », programme de LFI), PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PPR (proposition de résolution, article 34-1 de la Constitution), PPRE (proposition de résolution européenne), PJL (projet de loi), PLF (projet de loi de finances), PLFSS (projet de loi de financement de la sécurité sociale), UE (Union européenne), OTAN (Organisation du traité de l'Atlantique Nord), AME (aide médicale de l'État), RSA (revenu de solidarité active), APL (aide personnalisée au logement), RIC (référendum d'initiative citoyenne), ISF (impôt de solidarité sur la fortune), PFU (prélèvement forfaitaire unique, dit « flat tax »), CSG (contribution sociale généralisée), CVAE (cotisation sur la valeur ajoutée des entreprises), CFE (cotisation foncière des entreprises), BCE (Banque centrale européenne), BAC (brigade anticriminalité), BRAV-M (brigades de répression de l'action violente motorisées), LBD (lanceur de balles de défense), CSI (code de la sécurité intérieure), AFD (amende forfaitaire délictuelle), FALC (facile à lire et à comprendre), Md€ (milliard d'euros).

Étiquette commune : tous les documents émanant de LFI, du groupe LFI-NFP, de la campagne « Mélenchon 2027 » (et des campagnes de 2022) ou du blog du candidat (melenchon.fr) sont des **sources du parti, partie prenante**. Les textes communs du NFP sont des sources des partis signataires, partie prenante. Les textes de PPL, PPR et amendements hébergés par l'Assemblée sont des sources primaires (niveau 1) dont l'auteur est partie prenante.

Archivage : les fichiers sont dans `02-partis/lfi/corpus/`, tous téléchargés ou consultés le **2026-10-26**. Quatre PDF dépassent 20 Mo et ne sont pas versionnés : plan d'investissement automobile (22,1 Mo), plan d'investissement BTP et logement (23,6 Mo), note budgétaire commune du NFP pour 2025 (37,8 Mo), contre-budget 2026 du groupe (23,0 Mo). Pour chacun : lien, somme de contrôle SHA-256 et copie texte (`.md`) de l'extraction du PDF. Deux dossiers de presse de campagne (14,2 et 12,0 Mo) sans contenu programmatique sont en lien seul avec leur somme de contrôle, pour alléger le dépôt (décision confirmée par l'agent principal le 2026-10-26). Le plus lourd des fichiers versionnés fait 13,2 Mo. Les tirets cadratins et demi-cadratins des textes d'origine ont été remplacés dans les copies texte (mention en tête de chaque fichier concerné). Scripts d'extraction tenus hors du dépôt (dossier temporaire de la session), PDF lus avec `pdftotext`.

Légende du statut d'archivage :
- **PDF archivé** : fichier original téléchargé.
- **Texte archivé** : copie texte de la page web ou du PDF (`.md`), avec URL et date de consultation.
- **Lien seul** : pas de fichier téléchargeable, fichier non retenu, ou pas de source primaire accessible.

---

## Synthèse

| Catégorie (§6) | Nombre de fiches | Archivés |
|---|---|---|
| a. Programme 2027, textes de campagne, textes du parti depuis 2024 | 21 | 13 PDF, 3 pages texte, 2 copies texte de PDF (plus de 20 Mo), 3 liens seuls (dont 2 dossiers de presse téléchargés, avec somme de contrôle) |
| b. Programme législatives 2024 (NFP, texte commun) | 2 | 2 PDF |
| c. Programme présidentiel 2022 | 17 | 16 PDF, 1 lien seul (livre-programme) |
| d. Contre-budgets du groupe et du NFP | 3 (plus le contre-budget 2027, fiche [C-LFI-03]) | 1 PDF, 2 copies texte de PDF (plus de 20 Mo) |
| e. Propositions de loi et de résolution, amendements, motion de censure du groupe LFI-NFP | 1 dossier de presse, 17 textes, 4 amendements, 1 motion | 23 PDF |
| f. Déclarations depuis le 1er janvier 2026 | 23 | 23 fiches texte (dont 9 avec copie de la page du parti) |
| Actes | non applicable | |

Total : **89 fiches** (C-LFI-01 à C-LFI-89, sans trou ni doublon). Dossier `corpus/` : 85 fichiers (55 PDF, 30 `.md`), 101 Mo.

**Contrôle des auteurs, 2026-10-27 (règle du socle, `01-socle/01-criteres.md` §6) :** les 22 textes de la section e ont été relus sur le bloc « présenté par » de leur PDF archivé ; signataires du groupe et effectif du groupe LFI-NFP à la date du dépôt comptés en code (`_scripts/calculs/lfi_textes_du_groupe.py`, jeu AMO30, calcul par nos soins). Résultat : 21 textes du groupe (dont 8 sous la formule « les membres du groupe » et 13 sur liste nominative de 90 % ou plus des membres) et **1 texte d'élus du groupe** : la motion de censure de mai 2025 [C-LFI-46], 56 membres du groupe sur 71 (78,9 %).

**Point principal :** **le programme présidentiel 2027 n'est pas paru au 26 octobre 2026.** « L'Avenir en commun », 5e édition, « programme de la Nouvelle France » (1 069 mesures annoncées, six parties), sort en librairie le 6 novembre 2026 et sera présenté à une convention au Bourget le 7 novembre [C-LFI-01], [C-LFI-02], [C-LFI-10] ; son texte n'est pas en ligne, et le lien « Lire » du site de campagne renvoie à la version de 2025, dont la page indique qu'elle est « en cours de réactualisation » [C-LFI-13]. **Les documents les plus aboutis en catégorie a sont donc : (1) le contre-budget 2027 « Comment nous allons remettre de l'ordre dans les comptes publics » du 14 octobre 2026** (106,4 Md€ de recettes, 81,7 Md€ de dépenses, 24,7 Md€ de réduction du déficit pour 2027, présenté par le candidat et Éric Coquerel comme l'avant-projet d'une loi de finances rectificative ; il « ne constitue pas un chiffrage complet du programme », selon le site) [C-LFI-03] ; **(2) la 4e version de « L'Avenir en commun » (janvier 2025)** [C-LFI-13] ; (3) trois plans de campagne publiés en septembre et octobre 2026 (ruralités, automobile, BTP et logement) [C-LFI-04] à [C-LFI-06]. Le contre-budget 2025 du groupe existe en document autonome de 100 pages [C-LFI-42] (la note de paysage indiquait le contraire) et celui de 2026 en document de 68 pages [C-LFI-43] (la note n'avait trouvé que la presse). Le chiffrage complet du programme 2027 n'existe pas à la date d'arrêt.

---

## a. Programme 2027 et textes de campagne (priorité 1)

### Programme présidentiel 2027 officiel

**Non paru à la date d'arrêt** (voir Point principal). Le site de campagne melenchon2027.fr publie depuis septembre 2026 des « plans thématiques » et des « plans d'investissement productif » présentés comme des compléments de L'Avenir en commun, le contre-budget 2027, des dossiers de presse et la « Lettre au peuple de France ». Inventaire des pages et des PDF du site fait par l'interface publique du site (liste des pages, des articles et des fichiers PDF, interrogée le 2026-10-26) : aucun PDF de la 5e édition n'y figure.

### [C-LFI-01] Site de campagne, page « Découvrir le programme »
- Auteur : campagne « Mélenchon 2027 »
- Date : page créée le 2026-09-25, modifiée le 2026-10-15 (métadonnées du site), consultée le 2026-10-26
- Nature : page web
- URL : https://melenchon2027.fr/programme/decouvrir/
- Archivage : texte archivé, `corpus/C-LFI-01-site-campagne-decouvrir-le-programme-2026-10-26.md`
- Utile pour : constat de non-parution. La page annonce 1 069 mesures appliquées « dès mai 2027 », « Disponible le 6 novembre en librairie » ; le bouton « Lire » mène à l'édition 2025 [C-LFI-13]. Elle décrit le PDF du 14 octobre [C-LFI-03] comme les « grandes orientations budgétaires » pour 2027, sans chiffrage complet du programme. Mentionne plus de 24 000 contributions citoyennes [C-LFI-12].

### [C-LFI-02] Site de campagne, page « Comment a été conçu le programme »
- Auteur : campagne « Mélenchon 2027 »
- Date : page créée le 2026-04-03, modifiée le 2026-09-23, consultée le 2026-10-26
- Nature : page web (chronologie)
- URL : https://melenchon2027.fr/comment-a-ete-concu-le-programme/
- Archivage : texte archivé, `corpus/C-LFI-02-site-campagne-comment-a-ete-concu-le-programme-2026-10-26.md`
- Utile pour : généalogie du programme : première version (décembre 2016), 2e actualisation (novembre 2020), 3e version (18 novembre 2021, 694 propositions, 41 livrets et 13 plans), chiffrage (mars 2022), programmes partagés NUPES (2022) et NFP (2024) bâtis sur LAEC selon le mouvement, 4e version (janvier 2025), 5e version datée du 6 novembre 2026. Sert à la règle « qui parle pour le parti » (programme « porté par Jean-Luc Mélenchon et la France insoumise »).

### [C-LFI-03] Contre-budget 2027 : « Comment nous allons remettre de l'ordre dans les comptes publics »
- Auteur : La France insoumise, campagne de Jean-Luc Mélenchon (présenté par le candidat et Éric Coquerel)
- Date : 2026-10-14 (PDF créé le même jour ; conférence de presse au siège de LFI)
- Nature : document de 24 pages, en-tête « Élection présidentielle - 18 avril 2027 »
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/Comment-nous-allons-remettre-de-l-ordre-dans-les-comptes-publics.pdf
- Archivage : PDF archivé, `corpus/C-LFI-03-contre-budget-2027-ordre-comptes-publics-2026-10-14-2026-10-26.pdf` (4,0 Mo)
- Utile pour : axe 1 (bilan affiché : 106,4 Md€ de recettes, 81,7 Md€ de dépenses, 24,7 Md€ de réduction du déficit en 2027 ; « trajectoire crédible pour stabiliser notre dette par rapport au PIB en un quinquennat » ; pôle public bancaire et 100 Md€ d'investissements portés hors budget de l'État ; graphique de dette publique 2007-2026 ; cible de déficit en pourcentage du PIB absente du document) ; axe 2 (abrogation de la réforme de 2023, coût annoncé 9 Md€, « premier pas » vers 60 ans et 40 annuités ; abrogation des réformes de l'assurance chômage, 3 Md€) ; axe 4 (Smic à 1 700 € net avec conférence sur les salaires ; suppression du PFU 9 Md€ ; ISF renforcé 10 Md€ ; taxe Zucman au-delà de 100 M€ de patrimoine 15 Md€ ; niches 22 Md€ ; CVAE des plus grandes entreprises 3 Md€ ; impôt sur le revenu à 14 tranches au cours du mandat ; impôt sur les sociétés 3 Md€ ; taxe sur les multinationales 5 Md€ la première année) ; dépenses (hôpitaux 3 Md€ et 10 000 postes, logements d'urgence 3 Md€, plan contre les violences sexistes et sexuelles). Chiffres à reprendre de la page même aux étapes suivantes.

### [C-LFI-04] Plan thématique « Comment nous allons garantir l'égalité pour des ruralités où il fait bon vivre ? »
- Auteur : La France insoumise, espace programme (coordination Clémence Guetté et Hadrien Clouet selon la page des plans)
- Date : PDF créé le 2026-10-09, page publiée le 2026-10-09
- Nature : plan de 32 pages, seul plan thématique publié à la date d'arrêt
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/plan_RURALITE_web.pdf ; page : https://melenchon2027.fr/programme/plans-thematiques/ruralite/
- Archivage : PDF archivé, `corpus/C-LFI-04-plan-thematique-ruralites-2026-10-2026-10-26.pdf` (1,5 Mo)
- Utile pour : hors grille principalement (services publics en zone rurale, désenclavement, agriculture) ; axe 6 pour l'organisation territoriale (pouvoir de décision des communes). La page des plans annonce « la quarantaine d'objectifs politiques » du quinquennat : un seul plan est en ligne au 26 octobre.

### [C-LFI-05] Plan d'investissement productif « Automobile », édition 2027
- Auteur : La France insoumise, campagne
- Date : PDF créé le 2026-10-14, page publiée le 2026-10-10
- Nature : plan de 26 pages
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/PLAN-AUTO_Vf_ST.pdf ; page : https://melenchon2027.fr/programme/plans-investissement/automobile/
- Archivage : copie texte, `corpus/C-LFI-05-plan-investissement-automobile-2026-10-2026-10-26-texte.md`. PDF de 22,1 Mo non versionné, SHA-256 `c97c3dbd8a49e04f18a23c73cf04d49fb14b4fd3083563abc6e83aa92177441c`.
- Utile pour : hors grille (politique industrielle) ; axe 1 pour l'investissement public chiffré ; objectifs affichés : 2 millions de véhicules électriques produits en France par an, service public de la location, batteries, recharge. Version antérieure : plan « industrie automobile » du groupe (février et mai 2025, site du parti), non archivé.

### [C-LFI-06] Plan d'investissement productif « BTP et logement », édition 2027
- Auteur : La France insoumise, campagne
- Date : PDF créé le 2026-09-28, page publiée le 2026-09-24
- Nature : plan de 20 pages
- URL : https://melenchon2027.fr/wp-content/uploads/2026/09/M-27-PLAN-BTP-LOGEMENT.pdf ; page : https://melenchon2027.fr/programme/plans-investissement/btp-logement/
- Archivage : copie texte, `corpus/C-LFI-06-plan-investissement-btp-logement-2026-09-2026-10-26-texte.md`. PDF de 23,6 Mo non versionné, SHA-256 `39c0f0e8207a9aebc966cdfa9cbac99ed6e0217c987e13f59c24798474fd7874`.
- Utile pour : axe 4 (logement et loyers) et axe 1 (investissement) : 400 000 logements abordables par an pendant cinq ans dont 200 000 logements publics, isolation d'au moins 700 000 logements par an, accession à la propriété non spéculative.

### [C-LFI-07] « Lettre au peuple de France »
- Auteur : candidat
- Date : 2026-05-05 (page créée le même jour), deux jours après la déclaration de candidature [C-LFI-73]
- Nature : lettre ouverte, appel aux parrainages
- URL : https://melenchon2027.fr/lettre-au-peuple-de-france/
- Archivage : texte archivé, `corpus/C-LFI-07-lettre-au-peuple-de-france-2026-05-05-2026-10-26.md`
- Utile pour : couche « candidat » ; axe 6 (passage à la 6e République, RIC, droit de révoquer tout élu ; critique du refus présidentiel de tenir compte du résultat des législatives) ; axe 4 (salaires, vie chère) ; axe 2 (temps libéré, qualité du travail) ; hors grille (dénatalité, grand âge, santé environnementale, paix : Gaza, Liban, Iran, Ukraine).

### [C-LFI-08] Dossier de presse de campagne du 7 juin 2026 (meeting de lancement à Saint-Denis)
- Auteur : campagne
- Date : 2026-06-07 (PDF créé le 2026-06-05)
- Nature : dossier de presse, 12 pages (déroulé du meeting, intervenants)
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/DOSSIER-DE-PRESSE_7juin.pdf
- Archivage : lien seul (téléchargé, 14,2 Mo, non versionné faute de contenu programmatique), SHA-256 `e6fe05ad4c424636f969bdf677badd1614753fd243aa6b633f1460191bb98678`
- Utile pour : chronologie de campagne seulement.

### [C-LFI-09] Dossier de presse de campagne du 2 juillet 2026 (conférence de presse)
- Auteur : campagne
- Date : 2026-07-02 (PDF créé le 2026-07-01)
- Nature : dossier de presse, 12 pages (chiffres militants, nouvelles émissions, ouverture du programme aux contributions du 20 mai au 20 juin 2026)
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/DOSSIER-DE-PRESSE_2juillet.pdf
- Archivage : lien seul (téléchargé, 12,0 Mo, non versionné), SHA-256 `727a4422a612a0df0a7b9bba2e2e581d00df687c424543cb6df1f77deff6524d`
- Utile pour : méthode d'élaboration du programme (contributions citoyennes) ; chronologie.

### [C-LFI-10] Dossier de presse de campagne du 23 septembre 2026 (conférence de presse)
- Auteur : campagne
- Date : 2026-09-23 (PDF créé le 2026-09-22)
- Nature : dossier de presse, 12 pages
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/DOSSIER-DE-PRESSE_23septembre.pdf
- Archivage : PDF archivé, `corpus/C-LFI-10-dossier-presse-campagne-2026-09-23-2026-10-26.pdf` (13,2 Mo)
- Utile pour : annonce de la 5e édition (sortie le 6 novembre 2026, six parties : bifurcations écologique, économique, sociale, scientifique, démocratique et diplomatique ; coordination par Clémence Guetté et Hadrien Clouet) ; convention du 7 novembre au Bourget ; tract « contre la vie chère » tiré à plus de 4 millions d'exemplaires (non trouvé en ligne).

### [C-LFI-11] Dossier de presse de campagne du 8 octobre 2026
- Auteur : campagne
- Date : 2026-10-08 (PDF créé le même jour)
- Nature : dossier de presse, 8 pages
- URL : https://melenchon2027.fr/wp-content/uploads/2026/10/DOSSIER-DE-PRESSE_0810.pdf
- Archivage : PDF archivé, `corpus/C-LFI-11-dossier-presse-campagne-2026-10-08-2026-10-26.pdf` (6,2 Mo)
- Utile pour : calendrier (meeting de Clermont-Ferrand le 11 octobre, sortie du programme le 6 novembre, convention) ; 400 000 « parrainages citoyens » revendiqués.

### [C-LFI-12] « Synthèse des contributions citoyennes » sur le programme
- Auteur : campagne
- Date : 2026-07-17 (18 pages de chapitres publiées le même jour, premières synthèses le 2026-07-03)
- Nature : pages web, une par chapitre de LAEC 2025
- URL : https://melenchon2027.fr/synthese-des-contributions/
- Archivage : lien seul. Ce sont des synthèses de contributions de citoyens, pas des engagements du parti : à ne pas citer comme position de LFI.
- Utile pour : méthode d'élaboration (question Méthode, bloc a) seulement.

### Textes du parti adoptés ou publiés depuis 2024

### [C-LFI-13] « L'Avenir en commun », 4e version (édition 2025)
- Auteur : La France insoumise
- Date : janvier 2025 selon le site (PDF créé le 2025-02-18)
- Nature : livre-programme, 69 pages (format A5), quatre parties et 18 chapitres
- URL : https://melenchon2027.fr/wp-content/uploads/2025/02/A5-PROGRAMME-SITE.pdf (l'adresse citée par la note de paysage sur programme.lafranceinsoumise.fr redirige vers la page d'accueil de la campagne le 2026-10-26) ; version en ligne : https://melenchon2027.fr/programme2025/livre/ (bandeau : « L'Avenir en commun est en cours de réactualisation »)
- Archivage : PDF archivé, `corpus/C-LFI-13-avenir-en-commun-4e-version-2025-2026-10-26.pdf` (0,9 Mo)
- Utile pour : tous les axes. Repérés à cette étape (à relire en détail aux étapes suivantes) : axe 2 (mesure clé : abroger la réforme portant l'âge à 64 ans et restaurer le départ à 60 ans à taux plein pour 40 annuités ; pensions d'une carrière complète au niveau du Smic ; garantie d'emploi ; assurance chômage « protectrice ») ; axe 4 (Smic à 1 600 € net « immédiatement », point d'indice +10 %, impôt sur le revenu à 14 tranches, CSG progressive, taxe Zucman, suppression du PFU, droits de succession) ; axe 3 (régulariser travailleurs, étudiants, parents d'enfants scolarisés ; carte de séjour de dix ans comme titre de référence ; abroger les dernières lois asile et immigration ; garantir l'accès à l'AME) ; axe 5 (mesure clé : rétablir la police de proximité, démanteler les BAC et les BRAV-M) ; axe 6 (Assemblée constituante pour la 6e République, RIC dont révocatoire, « désobéir » aux règles européennes « bloquantes ») ; axe 1 (section intitulée « Refuser le chantage : annuler la dette publique »).

### [C-LFI-14] Texte d'orientation stratégique, Assemblée représentative de décembre 2024
- Auteur : La France insoumise (Assemblée représentative)
- Date : 2024-12-14 (version définitive ; projet du 2024-11-15)
- Nature : texte d'orientation, 17 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2024/12/ORIENTATION-STRATEGIQUE-VDEF.pdf
- Archivage : PDF archivé, `corpus/C-LFI-14-texte-orientation-strategique-ar-2024-12-2026-10-26.pdf` (9,5 Mo)
- Utile pour : question Méthode (blocs a et d) et axe 6 : stratégie d'opposition aux gouvernements, NFP « comme alternative », préparation d'une « présidentielle anticipée », hypothèse d'une nouvelle dissolution.

### [C-LFI-15] « Notre appel à l'unité populaire », texte de l'Assemblée représentative de juin 2025
- Auteur : La France insoumise (Assemblée représentative)
- Date : 2025-06-21
- Nature : texte politique, 5 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2025/06/TEXTE-AR-JUIN-2025_VF.pdf
- Archivage : PDF archivé, `corpus/C-LFI-15-texte-ar-appel-unite-populaire-2025-06-2026-10-26.pdf` (0,2 Mo)
- Utile pour : question Méthode (bloc a) ; diagnostic général (retraites, emplois, services publics).

### [C-LFI-16] « Notre feuille de route 2025 », Assemblée représentative de juin 2025
- Auteur : La France insoumise (Assemblée représentative)
- Date : 2025-06-21
- Nature : feuille de route, 16 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2025/06/FEUILLE-DE-ROUTE-AR-JUIN-2025_VF.pdf
- Archivage : PDF archivé, `corpus/C-LFI-16-feuille-de-route-ar-2025-06-2026-10-26.pdf` (0,3 Mo)
- Utile pour : question Méthode (bloc d : fonctionnement interne, « espaces » du mouvement, remontées de 99 boucles départementales).

### [C-LFI-17] Texte de l'Assemblée représentative d'avril 2026
- Auteur : La France insoumise (Assemblée représentative)
- Date : 2026-03-30 (PDF ; Assemblée représentative d'avril 2026)
- Nature : texte politique, 12 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2026/03/Texte-ARavril26.pdf
- Archivage : PDF archivé, `corpus/C-LFI-17-texte-ar-2026-04-2026-10-26.pdf` (0,3 Mo)
- Utile pour : bilan des municipales des 15 et 22 mars 2026 vu par le mouvement (entrée dans plus de 400 conseils municipaux, une dizaine de communes de plus de 20 000 habitants) ; axe 6 (« la Ve République à bout de souffle ») ; mouvement fondé il y a dix ans.

### [C-LFI-18] « Feuille de route de la France insoumise », Assemblée représentative d'avril 2026
- Auteur : La France insoumise (Assemblée représentative)
- Date : 2026-04-12
- Nature : feuille de route, 13 pages en trois axes (développement du mouvement, batailles de 2026, campagne de 2027)
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2026/04/FEUILLE-DE-ROUTE_VF.pdf
- Archivage : PDF archivé, `corpus/C-LFI-18-feuille-de-route-ar-2026-04-2026-10-26.pdf` (0,9 Mo)
- Utile pour : question Méthode (bloc a, préparation de 2027 ; point 13 « Poursuivre notre travail programmatique »).

### [C-LFI-19] Plan de lutte « Du "narcotrafic" à une approche globale de la criminalité organisée »
- Auteur : groupe LFI-NFP à l'AN
- Date : novembre 2024 (version de 30 pages mise en ligne le 2025-01-28 ; version de 11 pages du 2024-11-08 non archivée)
- Nature : plan de 14 propositions
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2025/01/Plan-de-lutte-Narcotrafic.pdf
- Archivage : PDF archivé, `corpus/C-LFI-19-plan-lutte-criminalite-organisee-2024-11-2026-10-26.pdf` (2,8 Mo)
- Utile pour : axe 5 (légaliser le cannabis, saisir les avoirs des trafiquants, lutter contre le blanchiment, statut de repenti, réparer la police judiciaire, police de proximité, moyens de la justice, plan pour les Outre-mer).

### [C-LFI-20] « Protectionnisme solidaire » : plan de 10 mesures face à Donald Trump
- Auteur : La France insoumise
- Date : 2025-04-16
- Nature : plan, 20 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2025/04/PLAN_10_MESURES_FACE_A_TRUMP_V10.pdf
- Archivage : PDF archivé, `corpus/C-LFI-20-plan-10-mesures-face-a-trump-2025-04-2026-10-26.pdf` (3,2 Mo)
- Utile pour : axe 6 (rapport à l'UE et à la politique commerciale) ; axe 4 (prix) ; hors grille (industrie).

### [C-LFI-21] « Flambée des prix de l'énergie : le plan d'urgence du groupe parlementaire de la France insoumise »
- Auteur : groupe LFI-NFP à l'AN
- Date : mars 2026 (PDF créé le 2026-03-27, même jour que la PPL n° 2591 [C-LFI-55])
- Nature : livret, 12 pages
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2026/03/1.-LIVRET-PlanUrgenceEnergie-A-Site.pdf
- Archivage : PDF archivé, `corpus/C-LFI-21-plan-urgence-prix-energie-groupe-2026-03-2026-10-26.pdf` (0,2 Mo)
- Utile pour : axe 4 (blocage des prix et des marges des carburants et de l'énergie, précédents de 1989 et 1990 cités ; refus d'une baisse de TVA, présentée comme une position du PS et du RN).

---

## b. Programme des législatives 2024 (priorité 2)

Le programme des législatives 2024 est le **programme commun du Nouveau Front populaire** (« Contrat de législature »), signé par LFI avec le PS, les Écologistes, le PCF et d'autres organisations. Il entre au corpus comme engagement de LFI ; c'est un **texte commun**, et une divergence entre ce texte et un texte propre de LFI sera notée aux étapes suivantes. LFI le présente comme construit sur la base de L'Avenir en commun [C-LFI-02] ; ce n'est pas une source pour attribuer une mesure à LFI seule.

### [C-LFI-22] « Nouveau Front populaire, contrat de législature », version du 27 juin 2024
- Auteur : Nouveau Front populaire (texte commun ; hébergé par LFI)
- Date : PDF créé le 2024-06-27 (scrutins des 30 juin et 7 juillet 2024)
- Nature : programme en trois temps (« 15 premiers jours : la rupture », « 100 jours : l'été des bifurcations », « les mois suivants : les transformations »), 26 pages, 6 240 mots
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2024/06/PROGRAMME-FRONT-POPULAIRE.pdf (fichier identique, même SHA-256, sur https://melenchon2027.fr/wp-content/uploads/2026/04/PROGRAMME-FRONT-POPULAIRE.pdf)
- Archivage : PDF archivé, `corpus/C-LFI-22-programme-nfp-legislatives-2024-version-27-juin-2026-10-26.pdf` (0,2 Mo)
- Utile pour : axe 2 (abroger immédiatement les décrets de la réforme portant l'âge à 64 ans et les réformes de l'assurance chômage ; minimum contributif au niveau du Smic) ; axe 4 (Smic à 1 600 € net, point d'indice +10 %, blocage des prix de première nécessité par décret, impôt sur le revenu à 14 tranches, CSG progressive, ISF « renforcé avec un volet climatique », suppression du PFU, exit tax) ; axe 3 (abroger les lois asile et immigration, voies légales et sécurisées d'immigration, révision du pacte asile et migration, agence de sauvetage en mer, accès à l'AME garanti et AME étendue à Mayotte) ; axe 5 (premières équipes de police de proximité, interdiction des LBD et des grenades mutilantes, démantèlement des BRAV-M) ; axe 6 (abroger le 49.3, proportionnelle, RIC, droit de vote des résidents étrangers aux élections locales, 6e République par une constituante citoyenne élue, refus des « contraintes austéritaires » du pacte budgétaire européen) ; hors grille et axe 6 (soutien à l'Ukraine par la livraison d'armes nécessaires, selon le texte commun).

### [C-LFI-23] « Nouveau Front populaire, contrat de législature », version du 14 juin 2024
- Auteur : Nouveau Front populaire (texte commun ; hébergé par LFI)
- Date : PDF créé le 2024-06-14 (jour de la présentation du programme), mis en ligne par LFI le 2024-06-19
- Nature : première version, 24 pages, 5 394 mots
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2024/06/Programme-nouveaufrontpopulaire.pdf
- Archivage : PDF archivé, `corpus/C-LFI-23-programme-nfp-legislatives-2024-version-14-juin-2026-10-26.pdf` (0,2 Mo)
- Utile pour : contrôle de version. La comparaison des deux textes (phrases présentes dans la version du 27 juin et absentes de celle du 14 juin, comparaison mécanique) fait apparaître surtout des différences de mise en page et quelques ajouts (rubriques Outre-mer, sport, Europe) ; aucune analyse à cette étape. La version du 27 juin est la version de référence.

---

## c. Programme présidentiel 2022 (priorité 3)

Sources : le livre-programme « L'Avenir en commun » (3e version, éditions du Seuil, novembre 2021, 694 propositions) n'existe pas en PDF officiel gratuit. Les 41 livrets thématiques et les 13 plans de 2022 sont rehébergés par la campagne 2027 (dossier `wp-content/uploads/2024/02/` de melenchon2027.fr, inventaire du site interrogé le 2026-10-26) ; la version abrégée et la déclaration du candidat viennent de web.archive.org (captures de melenchon2022.fr). Sélection : les livrets et plans qui couvrent les six axes ; les autres (écologie, santé, culture, numérique, agriculture...) sont hors grille et listés dans « Trous ».

| ID | Document | Date | Source de l'archive | Fichier | Axes |
|---|---|---|---|---|---|
| C-LFI-24 | « L'Avenir en commun, le programme en version abrégée » | avril 2022 (PDF créé le 2022-04-03) | web.archive.org, capture du 2022-04-04 de https://melenchon2022.fr/wp-content/uploads/2022/04/LAvenir-en-commun-le-programme-en-version-abregee.pdf | `C-LFI-24-programme-2022-version-abregee-2026-10-26.pdf` (4,1 Mo) | tous |
| C-LFI-25 | Déclaration du candidat au premier tour (version « accessible ») | mars 2022 (PDF créé le 2022-03-24) | capture du 2022-04-02 de https://melenchon2022.fr/wp-content/uploads/2022/04/Candidat-08-Jean-Luc-Melenchon-Declaration-accessible.pdf | `C-LFI-25-programme-2022-declaration-candidat-t1-2026-10-26.pdf` (1,0 Mo) | tous |
| C-LFI-26 | Livre-programme « L'Avenir en commun », 3e version | 2021-11-18 | lien seul : texte intégral en ligne sur https://laec.fr (site militant indépendant du « Discord insoumis », qui précise n'engager que son équipe) ; livre aux éditions du Seuil | lien seul | tous |
| C-LFI-27 | Livret n° 6 « Pour une politique migratoire humaniste et réaliste » | février 2022 | https://melenchon2027.fr/wp-content/uploads/2024/02/Livret_UP_06_MIGRATION_web-1-ok.pdf | `C-LFI-27-programme-2022-livret-06-migrations-2026-10-26.pdf` (0,9 Mo) | 3 |
| C-LFI-28 | Livret n° 28 « Refonder le service public de la police » | mars 2022 | .../Livret_UP_28_SECURITE_web-ok.pdf | `C-LFI-28-programme-2022-livret-28-securite-2026-10-26.pdf` (1,5 Mo) | 5 |
| C-LFI-29 | Livret n° 25 « Une justice au nom du peuple » | mars 2022 | .../Livret_UP_25_JUSTICE_web-1-ok.pdf | `C-LFI-29-programme-2022-livret-25-justice-2026-10-26.pdf` (1,3 Mo) | 5 |
| C-LFI-30 | Livret n° 40 « Pour une Assemblée constituante » | mars 2022 | .../Livret_UP_40_6e-REP_web-1-ok.pdf | `C-LFI-30-programme-2022-livret-40-6e-republique-2026-10-26.pdf` (0,3 Mo) | 6 |
| C-LFI-31 | Livret n° 21 « Travailler moins, travailler mieux, travailler toutes et tous » | février 2022 | .../Livret_UP_21_EMPLOI_web-ok.pdf | `C-LFI-31-programme-2022-livret-21-plein-emploi-2026-10-26.pdf` (1,5 Mo) | 2 |
| C-LFI-32 | Livret n° 30 « Pour la citoyenneté dans l'entreprise » (droit du travail) | avril 2022 | .../Livret_UP_30_DROIT_TRAVAIL_web.pdf | `C-LFI-32-programme-2022-livret-30-droit-du-travail-2026-10-26.pdf` (0,4 Mo) | 2 |
| C-LFI-33 | Livret n° 36 « Construire un service public de la dépendance » | mars 2022 | .../Livret_UP_36_VIEILLIR_web-ok.pdf | `C-LFI-33-programme-2022-livret-36-vieillir-2026-10-26.pdf` (1,3 Mo) | 2 |
| C-LFI-34 | Livret n° 15 « Pour un service public bancaire sous contrôle citoyen » | mars 2022 | .../Livret_UP_15_BANQUES_web.pdf | `C-LFI-34-programme-2022-livret-15-banques-2026-10-26.pdf` (1,3 Mo) | 1, 4 |
| C-LFI-35 | Plan « Justice fiscale » | mars 2022 | .../Plan_UP_JUSTICE-FISCALE_web-3.pdf | `C-LFI-35-programme-2022-plan-justice-fiscale-2026-10-26.pdf` (9,3 Mo) | 1, 4 |
| C-LFI-36 | Plan « Pouvoir d'achat » | mars 2022 | .../Plan_UP_POUVOIR_ACHAT_web.pdf | `C-LFI-36-programme-2022-plan-pouvoir-achat-2026-10-26.pdf` (5,3 Mo) | 4 |
| C-LFI-37 | Plan « Plein emploi » | février 2022 | .../Plan_UP_PLEIN-EMPLOI_sans_tdc.pdf | `C-LFI-37-programme-2022-plan-plein-emploi-2026-10-26.pdf` (6,7 Mo) | 2 |
| C-LFI-38 | Plan « 6e République » | mars 2022 | .../Plan_UP_6e-REPUBLIQUE_web.pdf | `C-LFI-38-programme-2022-plan-6e-republique-2026-10-26.pdf` (4,1 Mo) | 6 |
| C-LFI-39 | Plan « Pauvreté » | février 2022 | .../Plan_UP_PAUVRETE.pdf | `C-LFI-39-programme-2022-plan-pauvrete-2026-10-26.pdf` (7,2 Mo) | 2, 4 |
| C-LFI-40 | Plan « Europe » | janvier 2022 | .../PLAN-EUROPE_AVENIR-EN-COMMUN.pdf | `C-LFI-40-programme-2022-plan-europe-2026-10-26.pdf` (3,6 Mo) | 6 |

Les dates sont celles de création des PDF ; les fichiers rehébergés en 2024 sont identiques en taille, à quelques octets près, aux captures de 2022 de melenchon2022.fr (index des archives consulté le 2026-10-26 ; comparaison des sommes de contrôle non faite).

**Utile pour (contenu factuel) :**
- **[C-LFI-24]** Tous axes. Axe 4 : Smic à 1 400 € net ; écart de salaires limité de 1 à 20 dans l'entreprise. Axe 2 : retraite à 60 ans à taux plein pour 40 annuités, petites retraites au niveau du Smic revalorisé, minimum vieillesse au seuil de pauvreté, retraites indexées sur les salaires. Axe 6 : processus constituant pour la 6e République. **Axe 1 : page « Comment le programme est financé » : 250 Md€ de dépenses et 267 Md€ de recettes en plus par an** (dépenses : 50 Md€ pour la bifurcation et les services publics, 75 Md€ pour un million d'emplois publics, 125 Md€ de redistribution ; recettes : 163 Md€ d'impôt « plus juste », 52 Md€ de lutte contre la fraude et l'évasion fiscales, recettes induites par l'activité). C'est le seul résumé officiel du chiffrage de 2022 retrouvé (voir Trous).
- **[C-LFI-25]** Synthèse officielle de premier tour (déclaration du candidat publiée par la commission de propagande, version accessible).
- **[C-LFI-27]** Axe 3 : politique migratoire (titres de séjour, asile, régularisations). À relire pour la fiche axe 3.
- **[C-LFI-28], [C-LFI-29]** Axe 5 : refondation de la police, police de proximité, désarmement de certaines unités, justice.
- **[C-LFI-30], [C-LFI-38]** Axe 6 : Assemblée constituante, RIC, révocation des élus.
- **[C-LFI-31], [C-LFI-32], [C-LFI-33], [C-LFI-37], [C-LFI-39]** Axe 2 : garantie d'emploi, temps de travail, droit du travail, dépendance, pauvreté.
- **[C-LFI-34], [C-LFI-35], [C-LFI-36]** Axes 1 et 4 : pôle public bancaire, fiscalité (impôt sur le revenu, ISF, héritage), pouvoir d'achat.
- **[C-LFI-40]** Axe 6 : stratégie européenne (plan A de renégociation, plan B de désobéissance, selon le sommaire). Non lus en détail à cette étape.

---

## d. Contre-budgets du groupe LFI-NFP et du NFP (priorité 4)

Le groupe LFI-NFP présente un contre-budget à chaque PLF de la législature, présenté par Éric Coquerel. Pour le PLF 2027, le contre-budget est celui de la campagne, présenté le 14 octobre 2026 par le candidat et Éric Coquerel [C-LFI-03] (fiche en section a, comme le plan financier 2027-2032 du RN) ; les amendements emblématiques du groupe au PLF 2027 sont en section e ([C-LFI-56], [C-LFI-57]).

### [C-LFI-41] « Budget 2025 : les dix mesures phares » du Nouveau Front populaire (texte commun)
- Auteur : groupes du NFP à l'AN (texte commun ; hébergé par LFI)
- Date : 2024-10-10 (PDF créé le même jour)
- Nature : note de 12 pages identifiant « 10 mesures de recettes prioritaires » devant faire l'objet d'amendements communs des groupes du NFP au PLF 2025
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2024/10/Dossier_Presse_Budget_NFP_V4_Version-nume%CC%81rique.pdf (adresse avec un accent décomposé, la forme composée renvoie une erreur 404)
- Archivage : copie texte, `corpus/C-LFI-41-nfp-budget-2025-dix-mesures-recettes-2024-10-10-2026-10-26-texte.md`. PDF de 37,8 Mo non versionné, SHA-256 `e9ff5a15ac79159f7568e43e1764fbfcb704e5b5a517fd5dc21de10a0f1d7a6c`.
- Utile pour : axes 1 et 4 (recettes communes du NFP pour 2025). **Texte commun** : à distinguer du contre-budget propre du groupe [C-LFI-42].

### [C-LFI-42] Contre-budget 2025 du groupe LFI-NFP : « Budget 2025 : notre projet pour changer la vie »
- Auteur : groupe LFI-NFP à l'AN
- Date : novembre 2024 (version « E » mise en ligne le 2024-11-07, version « H » archivée créée le 2024-11-20)
- Nature : livret de 100 pages : dépenses, recettes, « 10 mesures phares majoritaires à l'Assemblée », comptes rendus des « États généraux des budgets sacrifiés » d'octobre 2024
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2024/11/1.-LIVRET-ContreProjet-2025-H-Site.pdf
- Archivage : PDF archivé, `corpus/C-LFI-42-contre-budget-plf-2025-groupe-lfi-2024-11-2026-10-26.pdf` (2,9 Mo). La note de paysage (source 27) indiquait « pas de document autonome » : il existe.
- Utile pour : grandes masses affichées : **total des dépenses 161,181 Md€, total des recettes 182,775 Md€** (écart de 21,594 Md€, calcul par nos soins ; le document ne l'affiche pas en solde dans les pages lues). Axe 2 : retraite à 60 ans avec 40 annuités, coût net 26,5 Md€. Axe 4 : point d'indice +10 % (21 Md€ bruts, 5,1 Md€ de recettes induites) ; recettes : « abolir les privilèges fiscaux » 126,725 Md€ (dont taxe sur les superprofits 15 Md€, ISF renforcé 15 Md€, CVAE 11 Md€, héritage 10 Md€, taxe sur les dividendes 6 Md€, impôt sur les sociétés majoré 5 Md€, suppression du PFU 2,7 Md€, taxe sur les rachats d'actions 1 Md€ ; lutte contre l'évitement fiscal 36,025 Md€) et « fiscalité plus progressive » 56,050 Md€. Axe 3 et 5 : lignes de dépenses à relire. Chiffres à reprendre de la page même aux étapes suivantes.

### [C-LFI-43] Contre-budget 2026 du groupe LFI-NFP : « Budget 2026 pour une bifurcation écologique et sociale »
- Auteur : groupe LFI-NFP à l'AN
- Date : 2025-10-24 (date d'impression en dernière page ; PDF créé le même jour)
- Nature : document de 68 pages : « la politique de l'offre est un échec », « une économie de paix », dépenses, recettes, tableau d'équilibre ; méthode : cahier de variantes du modèle FR-BDF de la Banque de France
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2025/10/Budget-2026_LFI_web_pages.pdf (une version compressée et une version en planches de 34 pages, « Pour une économie de paix », du même jour, ont le même contenu et ne sont pas archivées)
- Archivage : copie texte, `corpus/C-LFI-43-contre-budget-plf-2026-groupe-lfi-2025-10-24-2026-10-26-texte.md`. PDF de 23,0 Mo non versionné, SHA-256 `98a1d0396ecdefca4e4ff61167b4f1fca2b46eb30de4c8e0e9f3d63ba33c5720`. La note de paysage (source 17) n'avait trouvé que la presse : le document primaire existe.
- Utile pour : **tableau d'équilibre affiché : recettes 183,6 Md€, pertes de recettes 4,5 Md€, dépenses 167,9 Md€, économies en dépenses 15,4 Md€, solde 26,7 Md€** ; « plus de 180 milliards » de recettes et « près de 170 milliards » de dépenses ; réduction du déficit de 27 Md€ dès 2026 selon le texte. Axe 4 : taxe Zucman de 2 % au-delà de 100 M€ (20 Md€), ISF renforcé à volet climatique (15 Md€), héritage (10 Md€), taxe de 10 % sur les dividendes (6 Md€), suppression du PFU (2,7 Md€), impôt sur le revenu à 14 tranches et CSG progressive (5,5 Md€), taxe Zucman sur les multinationales (26 Md€), suppression des exonérations patronales au-dessus de deux Smic (8 Md€), CVAE rétablie (11 Md€), taxe d'habitation rétablie pour les 20 % les plus aisés (8 Md€), suppression de la « taxe Macron » de 10 % sur les factures d'énergie (perte de 3,5 Md€), TVA à 5,5 % sur les transports en commun (perte de 1 Md€). Axe 2 : retraite à 60 ans et 40 annuités financée « progressivement » par les recettes induites. Axe 6 : contribution au budget de l'UE (« engager le rapport de force »).

---

## e. Propositions de loi, de résolution, amendements et motion du groupe LFI-NFP (priorité 5)

Sélection : 17 textes déposés entre octobre 2024 et septembre 2026 et une motion de censure, **premier signataire membre du groupe LFI-NFP à la date du dépôt** (vérifié par croisement du jeu open data « Dossiers législatifs », téléchargé le 2026-10-26, avec l'historique des mandats de groupe du jeu AMO30), plus 4 amendements du groupe (premier signataire LFI-NFP, cosignés par l'ensemble du groupe) et le dossier de presse de la niche du 29 octobre 2026. Le jeu open data compte **352 textes** (PPL, PPLC, PPR, PPRE) déposés par un premier signataire LFI-NFP sur la législature. Statuts relevés dans les actes des dossiers au 2026-10-26 ; un texte sans acte de séance est noté « déposé, en commission ». PDF des textes : `https://www.assemblee-nationale.fr/dyn/opendata/<identifiant>.pdf` ; dossiers : `https://www.assemblee-nationale.fr/dyn/17/dossiers/<slug>`.

**Journées réservées du groupe LFI-NFP** (d'après les dates de séance des dossiers) : 28 novembre 2024 (dont la PPL n° 438 sur les retraites, discutée sans vote sur l'ensemble) ; 27 novembre 2025 (dont la PPR n° 2044 sur le Mercosur, adoptée, et la PPL n° 1950 de nationalisation d'ArcelorMittal France, adoptée en première lecture) ; **29 octobre 2026**, après la date d'arrêt (douze textes inscrits, dont la PPL n° 3176 sur les salaires et la PPL n° 3173 abrogeant les amendes forfaitaires délictuelles) [C-LFI-44].

### [C-LFI-44] Dossier de presse de la niche parlementaire 2026 du groupe LFI-NFP
- Auteur : groupe LFI-NFP (édito de Mathilde Panot, « Dernière niche avant l'Élysée »)
- Date : 2026-10-08 (PDF), niche du 29 octobre 2026
- Nature : dossier de presse, 20 pages (textes et rapporteurs)
- URL : https://lafranceinsoumise.fr/wp-content/uploads/2026/10/DOSSIER-DE-PRESSE-NICHE-LFI-26-WEB-V4.pdf
- Archivage : PDF archivé, `corpus/C-LFI-44-dossier-presse-niche-groupe-2026-10-29-2026-10-26.pdf` (7,1 Mo)
- Utile pour : liste des textes défendus le 29 octobre (Smic à 1 700 € net, pensions et indexation des salaires ; corps de fonctionnaires pour les accompagnants d'élèves en situation de handicap ; prise en charge des soins des victimes de violences sexuelles ; défiscalisation des pensions alimentaires ; jeunes majeurs de l'aide sociale à l'enfance ; abrogation des AFD ; radiations des listes électorales ; acétamipride ; canal Seine-Nord ; jeux vidéo ; propriété en Outre-mer ; investissements étrangers). Le dossier de presse de la niche de 2025 existe aussi (https://lafranceinsoumise.fr/wp-content/uploads/2025/11/DOSSIER-DE-PRESSE-NICHE-LFI-25_WEB.pdf), non archivé.

| ID | N° | Titre court | Premier signataire | Dépôt | Axe | Statut au 2026-10-26 | Fichier archivé |
|---|---|---|---|---|---|---|---|
| C-LFI-45 | PPL 1834 | Définanciarisation de la dette publique | Hadrien Clouet | 2025-09-16 | 1 | Déposée, en commission | 113 Ko |
| C-LFI-46 | Motion de censure (article 49 alinéa 2) | Motion de censure de mai 2025 (sur la loi agricole dite Duplomb, après la motion de rejet préalable) | Aurélie Trouvé et 57 collègues | 2025-05-30 | 6 et Méthode (marquage corrigé le 2026-10-26 : la motion ne porte pas sur les finances) | Déposée (sort à relever dans le scrutin correspondant) | 217 Ko |
| C-LFI-47 | PPL 438 | Abrogation de la retraite à 64 ans | Ugo Bernalicis | 2024-10-15 | 2 | Rapport le 20/11/2024 ; discutée le 28/11/2024 (journée réservée), pas de vote sur l'ensemble | 157 Ko |
| C-LFI-48 | PPL 2564 | Participations forfaitaires « sous contrôle populaire » (franchises médicales, forfait hospitalier) | Hadrien Clouet | 2026-03-03 | 2 | Déposée, en commission | 102 Ko |
| C-LFI-49 | Amdt 283, PJL 2250 | Suppression des programmes de contrôle antifraude des organismes de sécurité sociale (article 4) | Louis Boyard et le groupe | 2026-02-19 | 2 | Rejeté | 64 Ko |
| C-LFI-50 | PPLC 1374 | Droit du sol inscrit dans la Constitution | Mathilde Panot | 2025-05-07 | 3 | Déposée, en commission | 124 Ko |
| C-LFI-51 | PPLC 2124 | Droit de vote et d'éligibilité des étrangers aux élections locales | Danièle Obono | 2025-11-20 | 3 et 6 | Déposée, en commission | 107 Ko |
| C-LFI-52 | PPRE 467 | Corps européen civil de sauvetage en mer, opération « Mare Nostrum II » | Gabriel Amard | 2024-10-18 | 3 et 6 | Renvoyée à la commission des affaires européennes | 113 Ko |
| C-LFI-53 | PPL 3176 | Augmentation des salaires et des pensions (Smic, échelle mobile) | Hadrien Clouet | 2026-09-15 | 4 | Rapport le 19/10/2026 ; inscrite à la niche du 29/10/2026 | 177 Ko |
| C-LFI-54 | PPL 2893 | Échelle mobile des salaires | Hadrien Clouet | 2026-06-09 | 4 | Déposée, en commission | 141 Ko |
| C-LFI-55 | PPL 2591 | Blocage temporaire des prix de l'énergie | Aurélie Trouvé | 2026-03-27 | 4 | Déposée, en commission | 97 Ko |
| C-LFI-56 | Amdt I-CF1275, PLF 2027 | Impôt plancher sur la fortune | Éric Coquerel et le groupe | 2026-10-04 | 4 | Rejeté en commission des finances | 104 Ko |
| C-LFI-57 | Amdt I-CF847, PLF 2027 | Taux d'impôt du PFU porté de 12,8 % à 15,8 % (amendement « de repli ») | Marianne Maximi et le groupe | 2026-10-04 | 4 | Rejeté en commission des finances | 77 Ko |
| C-LFI-58 | PPL 1212 | Abrogation de l'article L. 435-1 du CSI (usage des armes par les policiers) | Thomas Portes | 2025-04-01 | 5 | Déposée, en commission | 137 Ko |
| C-LFI-59 | PPL 1317 | Interdiction de la reconnaissance faciale | Élisa Martin | 2025-04-17 | 5 | Déposée, en commission | 112 Ko |
| C-LFI-60 | PPL 577 | Abrogation du délit d'apologie du terrorisme | Ugo Bernalicis | 2024-11-19 | 5 | Déposée, en commission | 116 Ko |
| C-LFI-61 | Amdt II-3202, PLF 2025 | Ligne budgétaire « police nationale de proximité » de 1,2 Md€ (mission Sécurités) | Élisa Martin et le groupe | 2024-11-08 | 5 | Sort non relevé (le document porte la mention « sous réserve de sa recevabilité ») | 13 Ko |
| C-LFI-62 | PPR 1780 | Réunion du Parlement en Haute Cour pour la destitution du président de la République | Mathilde Panot et 103 collègues | 2025-09-11 | 6 | Déposée ; pas d'acte ultérieur dans les données ouvertes | 112 Ko |
| C-LFI-63 | PPLC 722 | Référendum constitutionnel d'initiative citoyenne | Jean-François Coulomme | 2024-12-17 | 6 | Déposée, en commission | 113 Ko |
| C-LFI-64 | PPR 788 | Convocation d'une Assemblée constituante pour la 6e République | Pierre-Yves Cadalen | 2025-01-21 | 6 | Déposée ; pas d'acte ultérieur | 130 Ko |
| C-LFI-65 | PPR 2354 | Retrait de la France de l'OTAN, en commençant par le commandement intégré | Clémence Guetté | 2026-01-20 | 6 | Déposée ; pas d'acte ultérieur | 108 Ko |
| C-LFI-66 | PPR 2044 | Opposition à l'accord commercial UE-Mercosur | Mathilde Panot | 2025-10-29 | 6 | Adoptée le 27/11/2025 (journée réservée ; résolution sans force contraignante ; scrutin 4244, candidat au complément) | 113 Ko |

Fichiers : `corpus/C-LFI-<nn>-<type>-<numéro>-<objet>-2026-10-26.pdf`.

**Fiches courtes**

- **[C-LFI-45] PPL n° 1834.** https://www.assemblee-nationale.fr/dyn/17/dossiers/definanciarisation_dette_publique_17e. Obligation pour les banques, organismes de placement collectif et assureurs sous contrôle de l'État d'employer au moins 15 % de leurs fonds propres en obligations du Trésor, taux relevable par décret. Axe 1. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27).
- **[C-LFI-46] Motion de censure de mai 2025.** https://lafranceinsoumise.fr/wp-content/uploads/2025/05/motion-de-censure-mai-2025.pdf (texte publié par le parti ; la motion figure au jeu open data sous l'identifiant MIONANR5L17-N10). Les motions de censure dont le premier signataire est LFI-NFP, d'après le même jeu : 2024-12-02 (article 49.3, PLFSS 2025 ; le scrutin 519 de la liste gelée porte sur cette motion, déposée par Mathilde Panot, Boris Vallaud, Cyrielle Chatelain, André Chassaigne et 181 membres, premier signataire LFI-NFP : rattachement confirmé par l'agent principal le 2026-10-26 d'après `03-sources/scrutins-positions.md`), 2025-01-14 (49.2), 2025-02-03, 06 et 10 (49.3, quatre motions), 2025-05-30 (49.2), 2025-10-13 (49.2), 2026-01-09 (49.2), 2026-01-20 (49.3, PLF 2026), 2026-02-23 (49.2). Leurs textes sont publiés au Journal officiel et ne sont pas tous en ligne en PDF sur le site de l'Assemblée (adresses open data testées en erreur 404). Axe 6 et chapitre Méthode. Texte d'élus du groupe (liste nominative de 58 signataires dont 56 membres du groupe sur un groupe de 71, 78,9 %, hors niche ; règle du 2026-10-27) : la présidente du groupe et quatorze autres membres ne signent pas ; cosigné par des élus d'autres groupes (deux élus d'un autre groupe).
- **[C-LFI-47] PPL n° 438.** https://www.assemblee-nationale.fr/dyn/17/dossiers/abrogation_retraite_64. Âge légal ramené de 64 à 62 ans et abrogation de l'accélération de la hausse de la durée d'assurance de la loi du 14 avril 2023. Correspond au scrutin 468 de la liste gelée (amendements de suppression de l'article 1er, pas de vote sur l'ensemble). Axe 2. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27 ; présidente du groupe non nommée parmi les premiers signataires ; journée réservée du 28 novembre 2024).
- **[C-LFI-48] PPL n° 2564.** https://www.assemblee-nationale.fr/dyn/17/dossiers/placer_participations_forfaitaires_controle_populaire_17e. Forfait journalier hospitalier et participations forfaitaires votés par le conseil d'administration de l'assurance maladie et plafonnés à leur montant du 1er janvier 2026. Axe 2. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27).
- **[C-LFI-49] Amendement n° 283 au PJL n° 2250 (fraudes sociales et fiscales).** https://www.assemblee-nationale.fr/dyn/17/amendements/2250/AN/283. Supprime à l'article 4 les programmes de contrôle et de lutte contre la fraude adossés aux plans de contrôle interne des organismes de sécurité sociale ; l'exposé refuse « la mise en équivalence » de la fraude fiscale et de la fraude sociale. Le projet de loi est le scrutin 6023 de la liste gelée. Axe 2. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-50] PPLC n° 1374.** https://www.assemblee-nationale.fr/dyn/17/dossiers/garantir_droit_sol_fondement_nationalite_francazise. Ajoute à l'article 1er de la Constitution : la loi garantit l'accès à la nationalité française à tout enfant né sur le sol français. Axe 3. Texte du groupe (liste nominative de 70 signataires sur un groupe de 71, 98,6 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-51] PPLC n° 2124.** https://www.assemblee-nationale.fr/dyn/17/dossiers/accorder_droit_vote_elections_locales_personnes_etrangeres_residant_France_17e. Nouvel article 72-5 accordant le droit de vote et d'éligibilité aux élections locales aux étrangers résidant en France ; abrogation de l'article 88-3 (régime propre aux citoyens de l'UE). Reprend une mesure du programme commun de 2024 [C-LFI-22]. Axes 3 et 6. Texte du groupe (liste nominative de 74 signataires dont 71 sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27) ; cosigné par des élus d'autres groupes.
- **[C-LFI-52] PPRE n° 467.** https://www.assemblee-nationale.fr/dyn/17/dossiers/corps_sauvetage_mer_mare_nostrum. Appelle le Conseil, la Commission et le Parlement européens à créer un corps européen civil de secours en mer et une opération sur le modèle de Mare Nostrum (Italie, 2013-2014). Axes 3 et 6. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-53] PPL n° 3176.** https://www.assemblee-nationale.fr/dyn/17/dossiers/augmenter_salaires_pensions_17e. Smic au moins égal à 2 176 € brut mensuels au 1er janvier 2027 (le contre-budget l'exprime en 1 700 € net) ; suppression du groupe d'experts sur le Smic ; autorisation des clauses d'indexation des salaires et échelle mobile des salaires (chapitre nouveau du code du travail). Scrutin attendu le 29 octobre 2026 (règle de remplacement du 881, voir `00-perimetre.md`). Axe 4. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27 ; inscrit à la niche du 29 octobre 2026).
- **[C-LFI-54] PPL n° 2893.** https://www.assemblee-nationale.fr/dyn/17/dossiers/garantir_conditions_vie_dignes_salaires_17e. Hausse automatique des salaires du privé deux fois par an (1er mars, 1er septembre), au moins égale à un indice d'inflation fixé par une commission, sauf au-dessus de deux fois le salaire médian ; caisse de péréquation pour les petites entreprises et les associations. Axe 4. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27 ; présidente du groupe non nommée parmi les premiers signataires).
- **[C-LFI-55] PPL n° 2591.** https://www.assemblee-nationale.fr/dyn/17/dossiers/blocage_temporaire_prix_energie_17e. En cas de crise internationale majeure, gel ou plafonnement de plein droit des prix de détail des carburants, du gaz et de l'électricité pour trois mois, renouvelable une fois, par décret en Conseil d'État (article L. 410-2 du code de commerce). Accompagne le plan d'urgence [C-LFI-21]. Axe 4. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-56] Amendement I-CF1275 au PLF 2027.** https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/CION_FIN/CF1275. Crée un « impôt plancher sur la fortune » (chapitre nouveau du code général des impôts, articles 885 AA et suivants). Comparable à la taxe Zucman (scrutin 3300, PS) et à la PPL écologiste du scrutin 881 ; à relire pour le seuil et le taux. Axe 4. Texte du groupe (liste nominative de 70 signataires sur un groupe de 70, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-57] Amendement I-CF847 au PLF 2027.** https://www.assemblee-nationale.fr/dyn/17/amendements/3210A/CION_FIN/CF847. Taux de l'article 117 quater du code général des impôts (part impôt du PFU) porté de 12,8 % à 15,8 % ; présenté par l'exposé comme « amendement de repli » par rapport à la suppression du PFU. Axe 4. Texte du groupe (liste nominative de 70 signataires sur un groupe de 70, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-58] PPL n° 1212.** https://www.assemblee-nationale.fr/dyn/17/dossiers/abroger_article_l_435_1_code_securite_interieure_17e. Abroge le chapitre du CSI sur l'usage des armes par les policiers (article L. 435-1, issu de la loi de 2017) et l'article L. 511-5-1 (polices municipales), et réécrit les cas d'usage de la force armée par les gendarmes. L'exposé des motifs cite des personnes tuées lors de refus d'obtempérer ; elles ne sont pas nommées ici. Axe 5. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27).
- **[C-LFI-59] PPL n° 1317.** https://www.assemblee-nationale.fr/dyn/17/dossiers/interdiction_reconnaissance_faciale_17e. Interdit d'installer, d'activer ou d'utiliser une technologie de reconnaissance faciale aux fins d'identification d'une personne (nouvel article 2 bis de la loi de 1978). Axe 5. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-60] PPL n° 577.** https://www.assemblee-nationale.fr/dyn/17/dossiers/abroger_delit_apologie_terrorisme_code_penal. Abroge l'article 421-2-5 du code pénal (apologie du terrorisme) et demande deux rapports sur son usage, dont un depuis la circulaire consécutive au 7 octobre 2023. Axe 5. Texte du groupe (liste nominative de 69 signataires sur un groupe de 71, 97,2 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-61] Amendement II-3202 au PLF 2025.** https://www.assemblee-nationale.fr/dyn/17/amendements/0324C/AN/3202. Crée un programme « Police nationale de proximité » doté de 1,2 Md€ dans la mission « Sécurités », par redéploiement de crédits (montants des programmes débités à relire). Axe 5. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-62] PPR n° 1780.** https://www.assemblee-nationale.fr/dyn/17/dossiers/reunion_du_parlement_en_haute_cour_destitution_president_republique. Réunion du Parlement en Haute Cour (article 68 de la Constitution) pour destituer le président de la République, au motif d'un « manquement » tenant à son incapacité à assurer la stabilité des institutions et à respecter la souveraineté populaire. Quatrième texte du même objet (n° 178 et 489 en 2024, n° 1777 le 2025-09-09) ; le parti en publie le texte (https://lafranceinsoumise.fr/wp-content/uploads/2025/09/motion-de-destitution-septembre-2025.pdf). Axe 6. Texte du groupe (liste nominative de 104 signataires dont 71 sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27) ; cosigné par des élus d'autres groupes.
- **[C-LFI-63] PPLC n° 722.** https://www.assemblee-nationale.fr/dyn/17/dossiers/referendum_constitutionnel_initiative_citoyenne2. Initiative de révision de la Constitution ouverte à tout électeur soutenu par deux centièmes des inscrits ; référendum obligatoire dans un délai de trois mois à un an. Voir aussi la PPLC n° 313 (référendum révocatoire, Bastien Lachaud, 2024-10-07), non archivée. Axe 6. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-64] PPR n° 788.** https://www.assemblee-nationale.fr/dyn/17/dossiers/convocation_assemblee_constitution_sixieme_republique. Appelle à convoquer une Assemblée constituante chargée de rédiger la Constitution de la 6e République ; considérants sur le refus de nommer la candidate du NFP à Matignon en 2024. Axe 6. Texte du groupe (liste nominative de 71 signataires sur un groupe de 71, 100 %, hors niche ; règle du 2026-10-27).
- **[C-LFI-65] PPR n° 2354.** https://www.assemblee-nationale.fr/dyn/17/dossiers/organiser_retrait_France_OTAN_commandement_integre. Invite le gouvernement à « interroger la place de la France » dans l'OTAN, retrait possible en deux temps en commençant par le commandement intégré. Communiqué du groupe du 2026-01-19 en section f [C-LFI-67]. Axe 6. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27 ; présidente du groupe non nommée parmi les premiers signataires).
- **[C-LFI-66] PPR n° 2044.** https://www.assemblee-nationale.fr/dyn/17/dossiers/opposition_accord_commercial_mercosur2. Invite le gouvernement à s'opposer à l'adoption de l'accord UE-Mercosur ; fait suite à une PPRE de même objet adoptée le 30 janvier 2025 (n° 608, Arnaud Le Gall, LFI-NFP). Axe 6. Texte du groupe (formule « les membres du groupe » : liste du groupe de 71 membres, 100 % ; règle du 2026-10-27 ; journée réservée du 27 novembre 2025).

**Annoncés ou cherchés, non trouvés :** aucune PPL du groupe LFI-NFP abrogeant la loi immigration de janvier 2024 (mesure présente dans [C-LFI-13] et [C-LFI-22]) ; aucune PPL LFI-NFP rétablissant l'ISF ou instituant un impôt sur les hauts patrimoines (la PPL du scrutin 881 est écologiste ; l'outil du groupe est l'amendement budgétaire, [C-LFI-56]) ; aucune PPL LFI-NFP sur l'AME, l'assurance chômage ou le RSA (ces mesures figurent dans les contre-budgets et les programmes) ; aucune PPL LFI-NFP sur la fraude sociale. Aucun texte dont Jean-Luc Mélenchon serait premier signataire (il n'est pas député sous la XVIIe législature).

---

## f. Déclarations publiques depuis le 1er janvier 2026 (priorité 6)

23 déclarations : Jean-Luc Mélenchon 12, communiqués du groupe LFI-NFP 3, communiqués du mouvement 2, Éric Coquerel 2, Mathilde Panot 2, Manuel Bompard 1, Mathilde Feld 1 (explication de vote au nom du groupe). Chaque déclaration a sa fiche texte dans `corpus/` (date, locuteur, média, format, axe, URL ouverte, date de consultation, position en paraphrase, citations de 15 mots au plus) ; neuf fiches contiennent en plus la copie de la page du parti. « Site du parti » : texte publié par LFI ou sur melenchon.fr (partie prenante). « Relais » : reprise par un média tiers, le média d'origine est indiqué. « Compte rendu de l'AN » : source primaire. La « Lettre au peuple de France » est en section a [C-LFI-07].

| ID | Date | Média d'origine | Format | Axe | Position (résumé) | URL |
|---|---|---|---|---|---|---|
| C-LFI-67 | 2026-01-19 | lafranceinsoumise.fr (groupe) | communiqué | 6 | Proposition de résolution pour un retrait de l'OTAN, en commençant par le commandement intégré ; France « non-alignée » ; voir [C-LFI-65] | https://lafranceinsoumise.fr/2026/01/19/le-groupe-parlementaire-de-la-france-insoumise-propose-de-sortir-de-lotan/ (site du parti) |
| C-LFI-68 | 2026-01-23 | séance de l'AN (Éric Coquerel) | intervention en séance | 1, 3, 4 et 6 | Motion de censure après le 49.3 sur le PLF 2026 ; déficit imputé aux baisses de recettes (ISF, PFU, pacte Dutreil) ; contre la hausse du coût des titres de séjour ; motion rejetée (269 voix, 288 requises) | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/seance-du-vendredi-23-janvier-2026.pdf (compte rendu de l'AN) |
| C-LFI-69 | 2026-02-10 | melenchon.fr | billet de blog | 3 | « Nouvelle France » : créolisation de la population, rejet du modèle de l'assimilation | https://melenchon.fr/2026/02/10/pourquoi-veulent-ils-salir-la-nouvelle-france/ (site du parti) |
| C-LFI-70 | 2026-02-16 | LCP (Mathilde Panot) | interview | 5 | Condamne une agression mortelle à Lyon, refuse toute responsabilité de LFI, dénonce une instrumentalisation, demande que les auteurs soient punis | https://lcp.fr/actualites/mort-de-quentin-a-lyon-mathilde-panot-denonce-une-instrumentalisation-du-drame-visant-a (relais ; l'adresse contient le prénom de la victime, à ne pas reprendre en page) |
| C-LFI-71 | 2026-04-07 | séance de l'AN (Mathilde Feld, au nom du groupe) | explication de vote | 2 | Vote contre le projet de loi fraudes ; fraude des allocataires évaluée à un tiers des 14 Md€ de fraude sociale, fraude fiscale à 80 à 120 Md€ | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-mardi-07-avril-2026.pdf (compte rendu de l'AN) |
| C-LFI-72 | 2026-04-23 | lafranceinsoumise.fr (mouvement) | communiqué | 4 | Blocage des prix des carburants et de l'énergie, taxation des superprofits de l'énergie, hausse du Smic, réduction du temps de travail | https://lafranceinsoumise.fr/2026/04/23/bloquer-les-prix-liberer-nos-vies-le-1er-mai-dans-la-rue/ (site du parti) |
| C-LFI-73 | 2026-05-03 | TF1, journal de 20 h | interview | 6 | Déclaration de candidature ; « une équipe, un programme et un seul candidat » ; RN « adversaire principal » ; voir [C-LFI-07] | https://lcp.fr/actualites/presidentielle-jean-luc-melenchon-officialise-sa-candidature-pour-2027-435851 (relais) |
| C-LFI-74 | 2026-05-20 | lafranceinsoumise.fr (groupe) | communiqué | 3 et 6 | Contre la déclaration de Chișinău sur la Convention européenne des droits de l'homme et les migrants ; contre le pacte asile et migration et la directive retour | https://lafranceinsoumise.fr/2026/05/20/la-france-valide-un-recul-historique-des-droits-humains-en-europe/ (site du parti) |
| C-LFI-75 | 2026-06-24 (date déduite) | conférence de presse en ligne, rapportée par Brussels Signal | conférence de presse | 3 et 6 | Régularisation des travailleurs sans papiers, procédures accélérées pour familles et résidents anciens ; contre les renvois vers des pays tiers ; désobéissance aux règles européennes (relais unique, en anglais, traduction par nos soins) | https://brusselssignal.eu/2026/06/melenchon-backs-regularisation-migrant-scheme-and-criticises-eu-return-policy/ (relais, étiquette proposée) |
| C-LFI-76 | 2026-07-03 | lafranceinsoumise.fr (groupe) | communiqué | 5 | Contre la présomption de légitime défense des forces de l'ordre (« permis de tuer ») ; tirs mortels « multipliés par cinq » depuis 2017 selon le groupe | https://lafranceinsoumise.fr/2026/07/03/presomption-de-legitime-defense-policiere-non-a-laggravation-du-permis-de-tuer/ (site du parti) |
| C-LFI-77 | 2026-08-23 | université d'été de LFI, rapportée par LCP | discours | 1, 4 et 6 | Censure annoncée du budget 2027 ; dette détenue par la BCE « au congélateur » ; taxe sur les superprofits, fin de niches ; hausse des salaires | https://lcp.fr/actualites/jean-luc-melenchon-annonce-la-censure-du-budget-et-estime-que-la-victoire-est-possible (relais) |
| C-LFI-78 | 2026-08-27 | débat organisé par le Medef, rapporté par LCP et Moneyvox | débat | 1, 2, 4 et 6 | Hausse des salaires et du Smic, sinon récession ; gel d'une partie de la dette ; désobéissance européenne ; retraite à 62 puis 60 ans (Moneyvox seul pour ce point) | https://lcp.fr/actualites/presidentielle-2027-ce-qu-il-faut-retenir-du-premier-debat-entre-les-candidats-440670 (relais) |
| C-LFI-79 | 2026-09-04 | Mediapart (tribune), republiée sur melenchon.fr le 5 septembre | tribune | 1 et 6 | Congélation ou annulation de la dette détenue par la BCE, présentée comme compatible avec l'article 123 du traité sur le fonctionnement de l'UE ; alliance avec les pays du Sud | https://melenchon.fr/2026/09/05/la-dette-sans-tabou/ (site du parti ; original Mediapart payant, non ouvert) |
| C-LFI-80 | 2026-09-15 | franceinfo, rapporté par LCP (Mathilde Panot) | interview | 1 et 6 | Refus des consultations budgétaires, « rien à négocier » ; censure « quoi qu'il arrive » | https://lcp.fr/actualites/budget-lfi-n-a-rien-a-negocier-avec-le-gouvernement-et-le-censurera-quoi-qu-il-arrive (relais) |
| C-LFI-81 | 2026-09-19 | melenchon.fr | billet de blog | 2 | Contre les jours de carence ; 14 jours d'arrêt par an en moyenne, hausse imputée au vieillissement et à la santé au travail ; rétablir les CHSCT et la médecine du travail | https://melenchon.fr/2026/09/19/edouard-philippe-lopen-bar-des-reactionnaires-contre-les-salaries/ (site du parti) |
| C-LFI-82 | 2026-09-23 | conférence de presse, rapportée par Public Sénat | conférence de presse | 4 | Prix des carburants plafonné à 1,70 € le litre (article L. 410-2 du code de commerce), marges des raffineurs plafonnées ; refus d'une baisse de TVA ; pas de nationalisation | https://www.publicsenat.fr/actualites/politique/jean-luc-melenchon-denonce-un-gouvernement-depasse-face-a-la-flambee-des-prix-des-carburants (relais) |
| C-LFI-83 | 2026-10-14 | conférence de presse au siège, rapportée par Public Sénat ; billet du 15 octobre sur melenchon.fr | conférence de presse et billet | 1, 2 et 4 | Présentation du contre-budget 2027 [C-LFI-03] comme avant-projet de loi de finances rectificative : 106,4 Md€ de recettes, 81,7 Md€ de dépenses ; « les aides sont le déficit » ; épargne réorientée, dette BCE « congelée » | https://www.publicsenat.fr/actualites/politique/presidentielle-2027-jean-luc-melenchon-table-sur-106-milliards-de-recettes-supplementaires-et-82-milliards-de-depenses-nouvelles-pour-2027 (relais) ; https://melenchon.fr/2026/10/15/tirer-les-comptes-publics-de-lorniere-liberale/ (site du parti, copie dans la fiche) |
| C-LFI-84 | 2026-10-14 | même conférence, rapportée par Public Sénat et LCP (Éric Coquerel) | conférence de presse | 1, 2 et 4 | Recettes « raisonnables » ; déficit présenté à 5 % du PIB selon LCP ; abrogation des réformes chômage, Smic à 1 700 € net, APL +10 % | https://lcp.fr/actualites/contre-budget-lfi-propose-1064-milliards-d-euros-de-recettes-supplementaires-et-817 (relais) |
| C-LFI-85 | 2026-10-17 | message sur X, rapporté par LCP ; propos dans le cortège rapportés par l'AFP via Sud Radio | réseau social et déclaration | 5 | Appel à rester à l'écart des pillages ; met en cause le commandement policier parisien et une stratégie de « pourrissement » du gouvernement | https://lcp.fr/actualites/manifestations-du-17-octobre-soutien-aux-policiers-ou-critiques-du-maintien-de-l-ordre (relais) |
| C-LFI-86 | 2026-10-20 | franceinfo (Manuel Bompard) | interview | 4 et 5 | Condamne les dégradations ; maintien de l'ordre par la désescalade ; ISF renforcé, blocage des prix des carburants, hausse du Smic, abrogation de Parcoursup | https://www.franceinfo.fr/politique/la-france-insoumise/le-coordinateur-de-lfi-manuel-bompard-denonce-une-strategie-de-pourrissement-ou-de-chaos-face-a-une-crise-politique_8245321.html (média d'origine) |
| C-LFI-87 | 2026-10-23 | Mediapart (entretien), reproduit sur melenchon.fr le 25 octobre | interview | 5 et 6 | Non-violence revendiquée ; refonte de la police (proximité, formation, armes intermédiaires, contrôle hors de l'inspection générale de la police) ; 6e République et constituante ; censure « inévitable » sans les revendications | https://melenchon.fr/2026/10/25/le-pouvoir-naura-quun-seul-choix-accepter-les-revendications-ou-sen-aller-entretien-avec-mediapart/ (site du parti, paraphrase seule : reproduction d'un entretien de presse) |
| C-LFI-88 | 2026-10-23 | lafranceinsoumise.fr (mouvement) | communiqué | 5 | Contre les interdictions de manifester et les couvre-feux ; appel à manifester pacifiquement ; soutien aux recours | https://lafranceinsoumise.fr/2026/10/23/nous-denoncons-la-fuite-en-avant-autoritaire-du-pouvoir/ (site du parti) |
| C-LFI-89 | 2026-10-24 | point presse dans la manifestation parisienne, rapporté par La Provence via Titres presse | déclaration | 6 | Appelle le président à céder aux revendications, sinon « la porte de sortie » (relais limité au titre et au chapô) | https://www.titrespresse.com/26376932603/melenchon-macron-jean (relais) |

Fichiers : `corpus/C-LFI-<nn>-<locuteur>-<objet>-<date de la déclaration>-2026-10-26.md`.

Répartition par axe (une déclaration peut compter pour plusieurs) : axe 1 : 7 ; axe 2 : 5 ; axe 3 : 4 ; axe 4 : 8 ; axe 5 : 6 ; axe 6 : 11. L'axe 3 est le plus mince : aucune déclaration de 2026 sur l'AME n'a été trouvée.

Archivage (règle v2) : neuf déclarations publiées par le parti ont leur page copiée dans la fiche ([C-LFI-67], [C-LFI-69], [C-LFI-72], [C-LFI-74], [C-LFI-76], [C-LFI-79], [C-LFI-81], [C-LFI-83], [C-LFI-88]) ; une dixième ([C-LFI-87]) est paraphrasée parce qu'elle reproduit un entretien de presse ; deux viennent du compte rendu de l'Assemblée ; les onze autres sont des relais de presse, tous ouverts. Correction faite à l'intégration : la copie de [C-LFI-83] provient du billet de melenchon.fr du 15 octobre (vérifié le 2026-10-26), pas de Public Sénat comme l'indiquait le brouillon.

---

## Actes

Non applicable : LFI n'a jamais exercé le pouvoir au niveau national (gouvernement ou majorité) sur la fenêtre couverte (2012-2026).
Renvoi : `00-perimetre.md`, section « Attribution des actes » (la comparaison programme / actes de Q4 est non applicable ; le verdict C repose sur discours, programme et votes ; pour Q6, blocs a, c et d applicables, bloc b non applicable).
Les exécutifs locaux dirigés par LFI ne sont pas des actes de gouvernement national et n'entrent pas ici.

---

## Trous

**Non trouvé**
- Programme présidentiel 2027 (« L'Avenir en commun », 5e édition) : non paru au 26 octobre 2026 ; parution annoncée le 6 novembre 2026. Aucun chapitre publié en avance trouvé sur melenchon2027.fr, lafranceinsoumise.fr ou dans la presse (seules les six parties sont annoncées).
- Chiffrage complet du programme 2027 : inexistant ; le contre-budget 2027 [C-LFI-03] ne chiffre que l'année 2027 et ne donne pas de cible de déficit en pourcentage du PIB (5 % selon LCP, [C-LFI-84], non vérifié dans le document).
- Document de chiffrage de 2022 : non trouvé en PDF. Le chiffrage a été présenté dans une émission en direct le 12 mars 2022 (page https://melenchon2022.fr/2022/03/12/emission-chiffrage/, capture du 2022-03-13 sur web.archive.org, sans document joint) ; son résumé figure dans la version abrégée [C-LFI-24]. L'index des archives de melenchon2022.fr ne contient aucun PDF de chiffrage ; une seconde recherche sur les domaines du parti a échoué (service d'archives temporairement hors ligne pendant la session).
- Programme abrégé FALC de 2026 (https://melenchon2027.fr/wp-content/uploads/2026/05/A4_PROGRAMME_ABREGE_FALC_web.pdf) : fichier tronqué sur le serveur (5 242 880 octets exactement, PDF illisible), non archivé.
- Livre-programme 2022 complet (éditions du Seuil) : pas de PDF officiel ; texte en ligne seulement sur laec.fr, site militant indépendant [C-LFI-26].
- Tract « contre la vie chère » de septembre 2026 annoncé dans [C-LFI-10] : non trouvé en ligne.
- Textes des discours du candidat : meeting de lancement à Saint-Denis (7 juin 2026), Clermont-Ferrand (11 octobre) ; aucun texte publié trouvé ; les pages vidéo de melenchon.fr n'ont pas de transcription. Le « discours sur la paix » (La Souterraine, 11 novembre 2026) et le meeting du Havre (5 décembre 2026) sont postérieurs à la date d'arrêt (pages d'événement du site de campagne, publiées les 17 et 19 octobre, consultées le 2026-10-26) ; la consigne de recherche donnée au sous-agent des déclarations les datait à tort d'octobre.
- PPL du groupe sur la loi immigration de 2024, l'ISF, l'AME, l'assurance chômage, le RSA ou la fraude sociale : aucune (voir section e).
- Déclarations de 2026 sur l'AME : aucune trouvée.

**Accès refusés ou partiels**
- programme.lafranceinsoumise.fr : l'adresse du PDF de 2025 citée par la note de paysage redirige vers la page d'accueil de la campagne ; fichier récupéré sur melenchon2027.fr.
- Mediapart (tribune du 4 septembre, entretien du 23 octobre) : payant ; textes lus dans leur reproduction sur melenchon.fr.
- Europe 1 : une page ouverte par l'outil de lecture (relais secondaire de [C-LFI-71]), accès direct non testé.
- Textes des motions de censure en PDF sur le site de l'Assemblée : erreur 404 aux adresses open data ; texte de la motion de mai 2025 récupéré sur le site du parti [C-LFI-46].
- web.archive.org : service temporairement hors ligne pendant une partie de la session (recherches de PDF de 2022 interrompues, reprises ensuite pour [C-LFI-24] et [C-LFI-25]).

**Connu seulement par la presse**
- Toutes les déclarations de la section f sauf les dix pages du parti et les deux comptes rendus de l'Assemblée.
- [C-LFI-75] : relais unique, en anglais, date déduite ; [C-LFI-89] : titre et chapô d'un agrégateur seulement ; [C-LFI-78] : la position sur les retraites (62 puis 60 ans) n'est rapportée que par Moneyvox.

**Écarts entre documents à vérifier aux étapes suivantes (précisions successives ou divergences possibles, sans qualification à cette étape)**
- Smic : 1 400 € net (2022, [C-LFI-24]) ; 1 600 € net (programme commun 2024 [C-LFI-22] et LAEC 2025 [C-LFI-13]) ; 1 700 € net (contre-budget 2027 [C-LFI-03], niche 2026 [C-LFI-44]) ; 2 176 € brut dans la PPL n° 3176 [C-LFI-53].
- Retraites : départ à 60 ans pour 40 annuités comme mesure clé (2022, 2025) ; abrogation de la réforme de 2023 et retour à 62 ans en 2027, 60 ans comme objectif du mandat (contre-budget 2027 [C-LFI-03], [C-LFI-83]) ; PPL n° 438 limitée à 62 ans [C-LFI-47]. Coût de la retraite à 60 ans : 26,5 Md€ nets (contre-budget 2025 [C-LFI-42]) ; coût du retour à 62 ans : 9 Md€ (2027).
- Dette : section « annuler la dette publique » dans LAEC 2025 [C-LFI-13] ; « stabiliser » le ratio de dette en un quinquennat (2027, [C-LFI-03]) ; « congélation » de la dette détenue par la BCE ([C-LFI-77], [C-LFI-79], [C-LFI-83]).
- ISF : 15 Md€ (contre-budgets 2025 et 2026) puis 10 Md€ (2027) ; taxe Zucman : 20 Md€ (2026) puis 15 Md€ (2027).
- Ukraine : livraison d'armes nécessaires dans le programme commun du NFP [C-LFI-22] ; positions propres de LFI à relever dans LAEC 2025 et les déclarations (hors grille, axe 6 pour l'OTAN).

---

## Sources secondaires utilisées pour les statuts et le contexte

1. LCP, « Présidentielle : le programme remanié de la "Nouvelle France" de Jean-Luc Mélenchon sera présenté début novembre », 2026-09-23, mis à jour le 2026-10-09. https://lcp.fr/actualites/presidentielle-le-programme-remanie-de-la-nouvelle-france-de-jean-luc-melenchon-sera
2. France 24, « Jean-Luc Mélenchon (LFI) officialise sa candidature à l'élection présidentielle de 2027 », 2026-05-03. https://www.france24.com/fr/france/20260503-jean-luc-m%C3%A9lenchon-lfi-officialise-sa-candidature-%C3%A0-l-%C3%A9lection-pr%C3%A9sidentielle-de-2027 [presse généraliste, relais]
3. LCP, « Présidentielle : Jean-Luc Mélenchon officialise sa candidature pour 2027 », 2026-05-03. https://lcp.fr/actualites/presidentielle-jean-luc-melenchon-officialise-sa-candidature-pour-2027-435851
4. LCP, « Jean-Luc Mélenchon annonce la censure du budget et estime que "la victoire est possible" en 2027 », 2026-08-23. https://lcp.fr/actualites/jean-luc-melenchon-annonce-la-censure-du-budget-et-estime-que-la-victoire-est-possible
5. LCP, « Présidentielle 2027 : ce qu'il faut retenir du premier débat entre les candidats », 2026-08-27. https://lcp.fr/actualites/presidentielle-2027-ce-qu-il-faut-retenir-du-premier-debat-entre-les-candidats-440670
6. Moneyvox, « Présidentielle 2027 : dette, retraites, ce qu'il faut retenir du premier débat des candidats », 2026-08-27 ou 28. https://www.moneyvox.fr/votre-argent/actualites/110159/presidentielle-2027-dette-retraites-ce-quil-faut-retenir-du-premier-debat-des-candidats [site d'information sur l'argent et la consommation, relais ; étiquette proposée]
7. LCP, « Budget : LFI n'a "rien à négocier" avec le gouvernement et le censurera "quoi qu'il arrive" », 2026-09-15. https://lcp.fr/actualites/budget-lfi-n-a-rien-a-negocier-avec-le-gouvernement-et-le-censurera-quoi-qu-il-arrive
8. Public Sénat, « Jean-Luc Mélenchon dénonce un gouvernement "dépassé" face à la flambée des prix des carburants », 2026-09-23. https://www.publicsenat.fr/actualites/politique/jean-luc-melenchon-denonce-un-gouvernement-depasse-face-a-la-flambee-des-prix-des-carburants
9. Public Sénat (avec AFP), « Présidentielle 2027 : Jean-Luc Mélenchon table sur 106 milliards de recettes supplémentaires et 82 milliards de dépenses nouvelles pour 2027 », 2026-10-14. https://www.publicsenat.fr/actualites/politique/presidentielle-2027-jean-luc-melenchon-table-sur-106-milliards-de-recettes-supplementaires-et-82-milliards-de-depenses-nouvelles-pour-2027
10. LCP, « Contre-budget : LFI propose 106,4 milliards d'euros de recettes supplémentaires et 81,7 milliards de dépenses nouvelles », 2026-10-14. https://lcp.fr/actualites/contre-budget-lfi-propose-1064-milliards-d-euros-de-recettes-supplementaires-et-817
11. LCP, « Manifestations du 17 octobre : soutien aux policiers ou critiques du maintien de l'ordre », 2026-10-17. https://lcp.fr/actualites/manifestations-du-17-octobre-soutien-aux-policiers-ou-critiques-du-maintien-de-l-ordre
12. Sud Radio (AFP), « Violences en marge du 17 octobre : duel à distance entre Mélenchon et Le Pen », 2026-10-18. https://www.sudradio.fr/societe/violences-en-marge-du-17-octobre-duel-a-distance-entre-melenchon-et-le-pen [presse généraliste, relais ; Sud Radio à ligne marquée, classée à droite]
13. franceinfo, « Le coordinateur de LFI Manuel Bompard dénonce une "stratégie de pourrissement ou de chaos" face à une crise politique », 2026-10-20. https://www.franceinfo.fr/politique/la-france-insoumise/le-coordinateur-de-lfi-manuel-bompard-denonce-une-strategie-de-pourrissement-ou-de-chaos-face-a-une-crise-politique_8245321.html
14. Titres presse (reprise de La Provence), « Manifestations du 24 octobre : Mélenchon appelle Macron "à céder" », 2026-10-24. https://www.titrespresse.com/26376932603/melenchon-macron-jean [agrégateur, relais]
15. LCP, « Mort [d'un militant] à Lyon : Mathilde Panot dénonce une instrumentalisation du drame visant à "marginaliser" LFI », 2026-02-16. https://lcp.fr/actualites/mort-de-quentin-a-lyon-mathilde-panot-denonce-une-instrumentalisation-du-drame-visant-a (prénom de la victime retiré du titre ; il figure dans l'adresse)
16. Europe 1, « L'Assemblée nationale approuve largement un texte pour lutter contre les fraudes sociales et fiscales », 2026-04-07. https://www.europe1.fr/politique/lassemblee-nationale-approuve-largement-un-texte-pour-lutter-contre-les-fraudes-sociales-et-fiscales-921835 [radio du groupe Lagardère, contrôlé par le groupe Bolloré, classée à droite]
17. Brussels Signal, « Mélenchon backs regularisation migrant scheme and criticises EU return policy », 2026-06-25. https://brusselssignal.eu/2026/06/melenchon-backs-regularisation-migrant-scheme-and-criticises-eu-return-policy/ [étiquette proposée ci-dessous]
18. Assemblée nationale, compte rendu intégral de la séance du vendredi 23 janvier 2026. https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/seance-du-vendredi-23-janvier-2026.pdf
19. Assemblée nationale, compte rendu intégral de la 2e séance du mardi 7 avril 2026. https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-mardi-07-avril-2026.pdf
20. Assemblée nationale, jeu de données « Dossiers législatifs » de la XVIIe législature (open data), téléchargé le 2026-10-26. https://data.assemblee-nationale.fr/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip ; « Députés actifs, mandats et organes » (AMO10) et « Tous acteurs, mandats et organes » (AMO30). https://data.assemblee-nationale.fr/static/openData/repository/17/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip
21. Cryptoast, « PLF 2027 : LFI veut augmenter la flat tax sur les dividendes à 34,4 % », 2026-10-07. https://cryptoast.fr/plf-2027-lfi-amendement-flat-tax-dividendes-pfu-2/ [site d'information sur les cryptoactifs, relais ; utilisé seulement pour retrouver le numéro de l'amendement [C-LFI-57], dont le texte est lu sur le site de l'Assemblée ; étiquette proposée]
22. Mélenchon 2027, interface publique du site (listes des pages, des articles et des fichiers PDF), interrogée le 2026-10-26. https://melenchon2027.fr/wp-json/wp/v2/media?mime_type=application/pdf [source du parti, partie prenante] ; même interrogation sur https://lafranceinsoumise.fr/wp-json/wp/v2/media (fichiers PDF publiés depuis juin 2024).
23. web.archive.org, index des PDF de melenchon2022.fr (CDX), consulté le 2026-10-26. http://web.archive.org/cdx/search/cdx?url=melenchon2022.fr/*&filter=mimetype:application/pdf
24. LAEC.fr, page d'accueil, consultée le 2026-10-26. https://laec.fr [site militant indépendant ; étiquette proposée]

## Ajouts proposés

Aucune fiche ajoutée après l'étape 1. Étiquettes absentes de `03-sources/etiquettes.md`, proposées pour le registre (le registre n'est pas modifié) :

- [Brussels Signal : média en ligne bruxellois classé à droite conservatrice, relais]. Justification : site d'information basé à Bruxelles, ligne éditoriale conservatrice revendiquée sur l'UE et les migrations ; utilisé une seule fois, comme relais d'une conférence de presse dont la vidéo n'a pas de transcription [C-LFI-75].
- [Moneyvox : site d'information sur l'argent et la consommation, relais]. Justification : site grand public sur la banque et l'épargne, sans ligne politique revendiquée ; proche de la ligne « presse financière spécialisée » du registre [C-LFI-78].
- [Cryptoast : site d'information sur les cryptoactifs, relais]. Justification : média spécialisé sans ligne politique revendiquée ; utilisé seulement pour retrouver un numéro d'amendement.
- [LAEC.fr : site militant indépendant (« Discord insoumis »), relais du programme 2022]. Justification : le site indique être « une initiative indépendante » dont le contenu « n'engage que l'équipe » ; il ne peut tenir lieu de source du parti [C-LFI-26].
- La Provence peut se ranger dans la ligne existante « presse régionale » ; Politis (hebdomadaire classé à gauche) a été rencontré en recherche sans être utilisé.
- Documents du parti repérés et non retenus, archivables si une fiche axe en a besoin (inventaire du site du parti, source 22) : « Les années Macron : une décennie de guerre sociale contre les mal-logé·es » (2026-03-31), livret « Pour une République antiraciste » (2025-03), récapitulatif « Égalité, lutte contre le racisme et les discriminations » (2026-05), recours du groupe au Conseil constitutionnel sur la loi de finances pour 2025 (2025-02-06) et sur la loi d'urgence agricole (2026-07-24), plan « industrie automobile » du groupe (2025), plan « climat et agriculture » (2026-09), programme des sénatoriales (2026-09), dossier de presse de la niche 2025 ; PPLC n° 313 (référendum révocatoire), PPL n° 412 (rémunération maximale), PPL n° 415 (pénibilité des métiers féminisés), PPL n° 432 (praticiens à diplôme hors UE), PPL n° 647 (encadrement des loyers), PPL n° 3173 (abrogation des AFD), téléchargées mais non archivées.
