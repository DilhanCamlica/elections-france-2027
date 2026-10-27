# LR : corpus programmatique

- Rédigé le : 2026-10-27
- Date d'arrêt des données : 2026-10-27
- Auteur : sous-agent Opus, étape 1 (section f préparée par un second sous-agent Opus, relue, complétée d'une fiche [C-LR-73] et intégrée par le sous-agent de l'étape 1)
- Statut : brouillon (étape 1)
- Version du socle appliquée : v2.2 (précisions du 2026-10-27)
- Règle appliquée : `01-socle/01-criteres.md` §6 (hiérarchie du corpus ; texte « du groupe » ; programme du mandat exercé pour une force qui a gouverné : sans objet ici, le mandat 2007-2012 étant hors fenêtre) et `01-socle/03-sources-et-hierarchie.md` (archivage, étiquetage)

Périmètre (voir `00-perimetre.md`) : le parti Les Républicains (LR), le groupe « Droite Républicaine » (DR) à l'Assemblée nationale, et son candidat Bruno Retailleau, président du parti, désigné par les adhérents le 19 avril 2026. Laurent Wauquiez, président du groupe, parle pour le groupe. Le groupe LR du Sénat est cité en contexte. L'Union des droites pour la République (UDR) d'Éric Ciotti est hors périmètre.

Sigles utilisés : AN (Assemblée nationale), DR (groupe Droite Républicaine), UDR (Union des droites pour la République), BP (Bureau politique), CNI (Commission nationale d'investiture), PPL (proposition de loi), PPLC (proposition de loi constitutionnelle), PPR (proposition de résolution), PJLC (projet de loi constitutionnelle), PLF (projet de loi de finances), PLFSS (projet de loi de financement de la sécurité sociale), UE (Union européenne), AME (aide médicale de l'État), RSA (revenu de solidarité active), OQTF (obligation de quitter le territoire français), CC (Conseil constitutionnel), CE (Conseil d'État), CJR (Cour de justice de la République), Md€ (milliard d'euros).

Étiquette commune : tous les documents émanant de LR, du groupe DR, du groupe LR du Sénat, de leurs élus ou du candidat sont des **sources du parti, partie prenante**. Les textes de PPL, PPLC, PPR et amendements hébergés par l'Assemblée sont des sources primaires (niveau 1) dont l'auteur est partie prenante. Les actes de gouvernement de la période 2024-2025 (circulaires, lois promulguées) sont des **sources officielles, partie prenante** quand le gouvernement est partie prenante (`03-sources-et-hierarchie.md` §2).

Archivage : les fichiers sont dans `02-partis/lr/corpus/`, tous téléchargés ou consultés le **2026-10-27**. Trois PDF dépassent 20 Mo et ne sont pas versionnés : les livrets « Réarmer notre agriculture » (version liée depuis la page « Nos propositions », 26,9 Mo), « Électricité » (37,9 Mo) et « Logement » (32,1 Mo) ; pour chacun, lien, somme de contrôle SHA-256 et copie texte (`.md`), et, pour l'agriculture, la version courte du livret (2,4 Mo) en PDF. Le plus lourd des fichiers versionnés fait 17,7 Mo (diaporama de la conférence de presse du 7 janvier 2026). Les tirets cadratins et demi-cadratins des textes d'origine ont été remplacés dans les copies texte (mention en tête de chaque fichier). Les entretiens publiés sur le site du parti ne sont pas copiés en entier (règle de citation : la page reprend un entretien conduit par un journaliste) : la fiche donne une paraphrase, une ou deux citations de 15 mots au plus, la structure de la page et l'adresse de l'interface publique du site qui permet de relever le texte. Les articles de presse ne sont pas reproduits. Les textes du parti (communiqués, lettres, déclarations, pages programmatiques) sont copiés en entier. Scripts d'extraction tenus hors du dépôt (dossier temporaire de la session), PDF lus avec `pdftotext` ; contrôle des auteurs en code : `_scripts/calculs/lr_textes_du_groupe.py`.

Légende du statut d'archivage :
- **PDF archivé** : fichier original téléchargé.
- **Texte archivé** : copie texte de la page web ou du PDF (`.md`), avec URL et date de consultation.
- **Fiche texte** : paraphrase et citations courtes d'un entretien ou d'un relais, avec URL et date de consultation.
- **Lien seul** : pas de fichier téléchargeable, fichier non retenu, ou pas de source primaire accessible.

---

## Synthèse

| Catégorie (§6) | Nombre de fiches | Archivés |
|---|---|---|
| a. Programme 2027, textes de campagne, textes du parti depuis 2024 | 27 (C-LR-01 à C-LR-27) | 24 PDF (dont 5 notes techniques sous une fiche, 2 versions d'un même projet sous une autre, 2 pièces de la conférence du 7 janvier), 14 fichiers texte (dont 3 copies texte de PDF de plus de 20 Mo et 2 fiches d'entretien) |
| b. Programme des législatives 2024 | 1 (C-LR-28) | lien seul (aucun programme écrit trouvé) |
| c. Programme présidentiel 2022 | 1 (C-LR-29) | 1 PDF |
| d. Contre-budgets, plans d'économies et amendements budgétaires du groupe DR et de LR | 6 (C-LR-30 à C-LR-35) | 2 PDF (amendements), 1 fiche texte, 3 liens seuls (dont un renvoi à [C-LR-78]) |
| e. PPL, PPLC, PPR du groupe DR, par axe, et textes du groupe LR du Sénat | 19 (C-LR-36 à C-LR-54) | 16 PDF, 3 liens seuls |
| Actes de coalition (2024-2025) | 4 (C-LR-55 à C-LR-58) | liens seuls |
| f. Déclarations depuis le 1er janvier 2026 | 23 (C-LR-59 à C-LR-81) | 23 fiches texte (1 avec copie intégrale d'un communiqué du parti) |
| Mandat exercé dans la fenêtre | sans objet | mandat 2007-2012 hors fenêtre (`00-perimetre.md`) |

Total : **81 fiches** (C-LR-01 à C-LR-81, sans trou ni doublon). Dossier `corpus/` : 81 fichiers (43 PDF, 38 `.md`), 77,7 Mo.

**Point principal :** **LR n'a pas de programme présidentiel unique au 27 octobre 2026.** Le corpus 2027 est fait de **huit livrets « Nos propositions pour la France »** publiés par le parti entre janvier et septembre 2026 (Travail gagnant, Produire plus, Agriculture, Famille, Électricité, Logement, Intelligence artificielle, École) [C-LR-01] à [C-LR-11], du **plan « Rétablir l'ordre dans les comptes publics » (197 Md€ d'économies en 2032, dont 146 Md€ pour le déficit et 51 Md€ rendus ; déficit sous 3 % en 2031, 2,2 % en 2032)**, dont les **fiches presse (17 pages) sont en ligne** sur le site du parti, contrairement à ce qu'indiquait la note de paysage [C-LR-12], et de **deux projets de loi constitutionnelle** rédigés article par article (souveraineté du peuple et État de droit ; « Charte républicaine ») [C-LR-13], [C-LR-14]. **Aucun livret sur l'immigration, la sécurité ou les retraites n'est paru** : ces axes reposent sur les projets constitutionnels, les fiches du plan d'économies (fiches 6 et 9), les entretiens du candidat et les textes du groupe DR. Le **pacte législatif d'urgence** du groupe et des sénateurs (22 juillet 2024) a été trouvé en PDF, par un relais de presse qui l'héberge [C-LR-19].

---

## a. Programme 2027, textes de campagne, textes du parti depuis 2024 (priorité 1)

### Livrets « Nos propositions pour la France » et page programmatique

### [C-LR-01] Page « Nos propositions » (republicains.fr)
- Auteur : Les Républicains
- Date : page créée le 2026-06-01, modifiée le 2026-09-03 (métadonnées du site)
- Nature : page programmatique : huit thèmes, mesures principales de chacun, liens vers les livrets, les notes techniques (Travail gagnant : cinq PDF ; Produire plus : treize notes hébergées sur Calaméo) et des annexes (conférences de presse, « réponse au vrai du faux de France Info »)
- URL : https://republicains.fr/nos-propositions/
- Archivage : texte archivé, `corpus/C-LR-01-page-nos-propositions-2026-10-27.md`
- Statut : position du parti (texte publié par le parti ; aucun vote d'instance trouvé)
- Étiquette : source du parti, partie prenante
- Utile pour : inventaire du programme publié ; axes 2 et 4 (Travail gagnant), hors grille (agriculture, logement, école, IA). Aucune rubrique sur l'immigration, la sécurité, les institutions ou les retraites.

### [C-LR-02] Livret « Travail gagnant »
- Auteur : Les Républicains
- Date : PDF créé le 2026-01-09 (version définitive liée depuis la page « Nos propositions » ; une version du 2026-01-06 au contenu identique à deux coquilles près existe sur le site) ; présenté en conférence de presse le 2026-01-07
- Nature : livret, 40 pages
- URL : https://republicains.fr/wp-content/uploads/2026/01/51705_LesRepublicains_Brochures_A5-40P_DEF.pdf
- Archivage : PDF archivé, `corpus/C-LR-02-brochure-travail-gagnant-2026-10-27.pdf` (8,0 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axes 2 et 4 : suppression des cotisations sociales au-delà de 1 623 heures par an (« seuil zéro cotisation ») ; cumul des aides non contributives plafonné à 70 % du Smic net par adulte (« compte social unique ») ; revenu d'incitation à l'activité ; réforme de l'assurance chômage ; travail des seniors ; « au moins 30 milliards d'euros » rendus aux salariés et aux entreprises, moitié chacun. Axe 1 : diagnostic chiffré de la dette.

### [C-LR-03] Notes techniques de « Travail gagnant » (cinq notes)
- Auteur : Les Républicains
- Date : PDF créés les 2026-01-07 et 2026-01-08
- Nature : cinq notes : seuil zéro cotisation (18 p.), revenu d'incitation à l'activité (12 p.), réforme de l'assurance chômage (8 p.), compte social unique (15 p.), travail des seniors (6 p.)
- URL : https://republicains.fr/wp-content/uploads/2026/01/Note-technique-Seuil-zero-cotisation.pdf et quatre adresses du même dossier (noms de fichiers en tête des PDF archivés)
- Archivage : 5 PDF archivés, `corpus/C-LR-03-note-technique-<objet>-2026-10-27.pdf`
- Statut : position du parti (chiffrage)
- Étiquette : source du parti, partie prenante
- Utile pour : chiffrage des mesures des axes 2 et 4 (Q2, Q3).

### [C-LR-04] Conférence de presse du 7 janvier 2026 (« Nos propositions sur le travail et la compétitivité ») et réponse aux Décodeurs
- Auteur : Les Républicains (Bruno Retailleau, avec Véronique Louwagie, Christine Lavarde, François Asselin et Pierre Danon selon la page)
- Date : page du 2026-01-07 ; diaporama créé le 2026-01-09 ; réponse aux Décodeurs du 2026-01-09
- Nature : page d'annonce ; diaporama de présentation (49 pages) ; « Réponse aux Décodeurs » (7 pages, réponse du parti à une vérification du *Monde*)
- URL : https://republicains.fr/actualites/2026/01/07/nos-propositions-sur-le-travail-et-la-competitivite/ ; https://republicains.fr/wp-content/uploads/2026/01/Slide-presentation-Travail-gagnant-07-01-26.pdf ; https://republicains.fr/wp-content/uploads/2026/01/Reponse-aux-Decodeurs-090126.pdf
- Archivage : texte archivé `corpus/C-LR-04-page-nos-propositions-travail-competitivite-2026-01-07-2026-10-27.md` ; PDF archivés `corpus/C-LR-04-diaporama-travail-gagnant-2026-01-07-2026-10-27.pdf` (17,7 Mo) et `corpus/C-LR-04-reponse-aux-decodeurs-2026-01-09-2026-10-27.pdf` (0,1 Mo). Un « droit de réponse » du même jour existe sur le site (lien seul : https://republicains.fr/wp-content/uploads/2026/01/Droit-de-reponse-Les-Decodeurs-090126-2.pdf).
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axes 2 et 4 ; débat public sur le chiffrage (la vérification du *Monde* elle-même n'a pas été ouverte : article payant).

### [C-LR-05] Livret « Produire plus pour vivre mieux »
- Auteur : Les Républicains
- Date : PDF créé le 2026-02-18
- Nature : livret, 40 pages ; treize notes techniques sur Calaméo (liens seuls, depuis [C-LR-01])
- URL : https://republicains.fr/wp-content/uploads/2026/02/LR_Produire_Plus_LIVRET.pdf
- Archivage : PDF archivé, `corpus/C-LR-05-livret-produire-plus-2026-10-27.pdf` (14,0 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (baisse des prélèvements obligatoires, impôts de production, transmission du capital productif), axe 2 (code du travail refondé sur 50 principes, 50 normes supprimées), hors grille (industrie).

### [C-LR-06] Livret « Réarmer notre agriculture »
- Auteur : Les Républicains
- Date : PDF créés le 2026-03-03 (version liée, 40 pages) et le 2026-03-02 (version courte, 36 pages)
- Nature : livret
- URL : https://republicains.fr/wp-content/uploads/2026/03/LR_Agriculture.pdf (version liée) ; https://republicains.fr/wp-content/uploads/2026/03/Livret_LR_Agriculture_VF.pdf
- Archivage : version liée de plus de 20 Mo (26,9 Mo) non versionnée : copie texte `corpus/C-LR-06-livret-agriculture-copie-texte-2026-10-27.md` avec SHA-256 ; version courte en PDF `corpus/C-LR-06-livret-agriculture-version-courte-2026-10-27.pdf` (2,4 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : hors grille (agriculture) ; axe 6 (« aligner nos règles sur l'Europe, pas au-delà », PAC, réciprocité commerciale, Mercosur).

### [C-LR-07] Livret « Une politique pour toutes les familles de France »
- Auteur : Les Républicains
- Date : PDF créé le 2026-04-28 (version finale mise en ligne le 2026-05-04 ; une version du 2026-04-30 existe)
- Nature : livret, 24 pages ; issu d'une consultation des adhérents (page du 2026-04-15, lien seul : https://republicains.fr/actualites/2026/04/15/consultation-des-adherents-famille-vos-avis-ont-ete-entendus/)
- URL : https://republicains.fr/wp-content/uploads/2026/05/LR_Famille_vFinale.pdf
- Archivage : PDF archivé, `corpus/C-LR-07-livret-famille-2026-10-27.pdf` (12,9 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (revenu familial remplaçant douze dispositifs, doublé au troisième enfant) ; axe 3 (pour les dispositifs familiaux, les étrangers devront justifier de cinq années de résidence et d'activité professionnelle) ; logement social recentré sur ceux qui travaillent.

### [C-LR-08] Livret « Baisser la facture d'électricité des Français »
- Auteur : Les Républicains
- Date : PDF créé le 2026-05-06 (mis en ligne le 2026-05-07)
- Nature : livret, 40 pages
- URL : https://republicains.fr/wp-content/uploads/2026/05/LR_Electricite_vFF070626.pdf
- Archivage : PDF de plus de 20 Mo (37,9 Mo) non versionné : copie texte `corpus/C-LR-08-livret-electricite-copie-texte-2026-10-27.md` avec SHA-256
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (prix de l'électricité, fin des subventions aux nouvelles capacités éoliennes et photovoltaïques) ; axe 6 (subsidiarité et souveraineté sur le mix énergétique au niveau européen) ; hors grille (énergie).

### [C-LR-09] Livret « Se loger mieux et moins cher »
- Auteur : Les Républicains
- Date : PDF créé le 2026-05-28
- Nature : livret, 48 pages
- URL : https://republicains.fr/wp-content/uploads/2026/05/LR_Logement.pdf
- Archivage : PDF de plus de 20 Mo (32,1 Mo) non versionné : copie texte `corpus/C-LR-09-livret-logement-copie-texte-2026-10-27.md` avec SHA-256
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (accession, marché locatif) ; axe 3 et 2 (logement social recentré sur ceux qui travaillent) ; hors grille (urbanisme, loi SRU : quotas de 20 et 25 % supprimés).

### [C-LR-10] Livret « L'IA au service des Français »
- Auteur : Les Républicains
- Date : PDF créé le 2026-07-07
- Nature : livret, 56 pages
- URL : https://republicains.fr/wp-content/uploads/2026/07/LR_IA.pdf
- Archivage : PDF archivé, `corpus/C-LR-10-livret-intelligence-artificielle-2026-10-27.pdf` (7,3 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : axe 1 (« l'équivalent de 250 000 agents publics » mobilisés, dont 125 000 départs non remplacés, environ 15 Md€ d'économies nettes annoncées) ; hors grille (numérique).

### [C-LR-11] Livret « Pour une école de la transmission, de l'égalité des chances, de l'autorité et de la liberté »
- Auteur : Les Républicains
- Date : PDF créé le 2026-08-31 (mis en ligne le 2026-09-03)
- Nature : livret, 36 pages
- URL : https://republicains.fr/wp-content/uploads/2026/09/LR_Ecole_vF.pdf
- Archivage : PDF archivé, `corpus/C-LR-11-livret-ecole-2026-10-27.pdf` (6,1 Mo)
- Statut : position du parti
- Étiquette : source du parti, partie prenante
- Utile pour : hors grille (école : salaire des professeurs, « mille écoles libres dans l'école publique »).

### Plan budgétaire du candidat et projets constitutionnels

### [C-LR-12] « Rétablir l'ordre dans les comptes publics » : fiches presse du plan de 197 Md€ (12 octobre 2026)
- Auteur : Les Républicains (présentation par Bruno Retailleau, candidat, au siège du parti, le 2026-10-12, selon LCP)
- Date : fiches datées du 2026-10-12 ; PDF mis en ligne le 2026-10-15 dans la médiathèque du site (aucune page d'actualité ne le relie)
- Nature : 17 pages, quinze fiches : situation des finances publiques ; trajectoire (197 Md€ d'économies en 2032, dont 146 Md€ pour le déficit et 51 Md€ rendus ; déficit 4,8 % en 2027, 2,8 % en 2031, 2,2 % en 2032 ; dette 122,7 % du PIB en 2032 ; hypothèses de croissance) ; État (56 Md€, dont 400 000 départs en retraite non remplacés et 1 623 heures de travail effectif ; 32 Md€ ; 8 Md€ de fraude) ; sphère sociale (retraites 42 Md€, arrêts maladie 4 Md€, Travail gagnant 30 Md€, immigration 10 Md€ dont 7 Md€ sur le volet social, fraude sociale 4 Md€, gestion de la Sécurité sociale 4 Md€) ; collectivités 10 Md€ ; prospérité (51 Md€ rendus) ; règle d'or
- URL : https://republicains.fr/wp-content/uploads/2026/10/20261011_Fiches_presse_comptes_publics_mise_en_page.pdf ; relais : LCP, « Face à une France "quasiment en faillite", Bruno Retailleau présente un plan d'économies de 197 milliards », 2026-10-12, https://lcp.fr/actualites/face-a-une-france-quasiment-en-faillite-bruno-retailleau-presente-un-plan-d-economies-de (21 Md€ rendus aux ménages, 30 Md€ aux entreprises, « sans augmentation d'impôts »)
- Archivage : PDF archivé, `corpus/C-LR-12-fiches-presse-comptes-publics-197-md-2026-10-12-2026-10-27.pdf` (0,5 Mo)
- Statut : position du candidat et du parti (document du parti) ; c'est le document chiffré le plus complet du corpus 2027
- Étiquette : source du parti, partie prenante (le document cite le HCFP, l'Insee, l'AFT, l'OID et l'Institut Montaigne : sources à remonter et à étiqueter aux étapes suivantes)
- Utile pour : axe 1 (trajectoire), axe 2 (retraites, arrêts maladie, fraude), axe 3 (fiche 9 : regroupement familial divisé par deux, AME réduite aux soins essentiels, hébergement d'urgence fermé aux personnes sous OQTF ; après révision constitutionnelle, cinq ans de séjour et de travail pour les prestations, asile examiné hors des frontières), axe 4 (sommes rendues). Postérieur au 1er janvier 2026 : non doublé en section f.

### [C-LR-13] Projet de loi constitutionnelle « restaurant la souveraineté du peuple et réconciliant l'État de droit avec la démocratie »
- Auteur : Les Républicains (projet du candidat, sans signature)
- Date : version « V280826 » (28 août 2026), PDF créé le 2026-08-28, mis en ligne le 2026-09-03
- Nature : projet de texte constitutionnel, 8 pages : exposé des motifs et articles (référendum élargi, contrôle de constitutionnalité, article 88-1 : le droit de l'Union garde une autorité supérieure aux lois sauf contrariété à la Constitution ou méconnaissance de la répartition des compétences)
- URL : https://republicains.fr/wp-content/uploads/2026/09/0523ceeb-5312-4629-a1f0-a7eba5aaefbb.pdf
- Archivage : PDF archivé, `corpus/C-LR-13-pjlc-souverainete-du-peuple-v280826-2026-10-27.pdf` (0,2 Mo)
- Statut : position du candidat, publiée par le parti (projet, non déposé)
- Étiquette : source du parti, partie prenante
- Utile pour : axe 6 (référendum, Conseil constitutionnel, rapport au droit de l'Union : **texte primaire sur l'appartenance à l'Union**, qui maintient la participation de la République à l'Union et la primauté du droit de l'Union sur la loi dans les limites indiquées) ; Q6 bloc a.

### [C-LR-14] Projet de loi constitutionnelle « proclamant la Charte républicaine »
- Auteur : Les Républicains (projet du candidat, sans signature)
- Date : deux versions : « V310826 » (PDF créé le 2026-08-31) et « V010926 » (mise en ligne le 2026-09-04, version la plus récente)
- Nature : projet de texte constitutionnel, 8 pages : « Charte républicaine de 2027 » ajoutée au Préambule (ordre public, sécurité, nationalité, immigration ; article 12 : prestations sociales non contributives aux étrangers hors UE subordonnables à cinq ans de séjour régulier et d'activité)
- URL : https://republicains.fr/wp-content/uploads/2026/09/PJLC-Charte-republicaine-v010926.pdf ; https://republicains.fr/wp-content/uploads/2026/09/e644aaa8-03c6-4cdc-bd38-dc83e51a4dde.pdf
- Archivage : 2 PDF archivés, `corpus/C-LR-14-pjlc-charte-republicaine-v010926-2026-10-27.pdf` et `corpus/C-LR-14-pjlc-charte-republicaine-v310826-2026-10-27.pdf` (0,2 Mo chacun)
- Statut : position du candidat, publiée par le parti (projet, non déposé) ; nommée « Charte de l'ordre républicain » dans l'entretien [C-LR-15] et dans la presse
- Étiquette : source du parti, partie prenante
- Utile pour : axes 3, 5 et 6. La comparaison des deux versions (écart éventuel entre V310826 et V010926) n'a pas été faite à cette étape.

### [C-LR-15] Entretien du candidat sur la réforme constitutionnelle (*Le Figaro*, repris le 2 septembre 2026)
- Auteur : Bruno Retailleau, candidat désigné (entretien)
- Date : page du parti du 2026-09-02 ; relais Public Sénat du 2026-09-03
- Nature : entretien
- URL : https://republicains.fr/actualites/2026/09/02/en-france-la-seule-cour-supreme-cest-le-peuple-je-lui-donnerai-le-dernier-mot/
- Archivage : fiche texte, `corpus/C-LR-15-retailleau-entretien-reforme-constitutionnelle-2026-09-02-2026-10-27.md`
- Statut : position du candidat
- Étiquette : source du parti, partie prenante ; *Le Figaro* : quotidien classé à droite (non ouvert)
- Utile pour : axes 3, 5 et 6 (calendrier : référendum à la rentrée 2027 ; « censurer la censure » ; article 88). Postérieur au 1er janvier 2026, classé ici comme texte de campagne (présentation du projet constitutionnel), non doublé en section f.

### [C-LR-16] Entretien du candidat sur les successions (*L'Opinion*, repris le 26 août 2026)
- Auteur : Bruno Retailleau, candidat désigné (entretien)
- Date : 2026-08-26
- Nature : entretien
- URL : https://republicains.fr/actualites/2026/08/26/je-serai-le-president-qui-baissera-les-impots-de-succession/
- Archivage : fiche texte, `corpus/C-LR-16-retailleau-entretien-successions-2026-08-26-2026-10-27.md`
- Statut : position du candidat
- Étiquette : source du parti, partie prenante ; [L'Opinion : étiquette proposée, voir « Étiquettes proposées »]
- Utile pour : axe 4 (engagement de baisse des droits de succession ; pas de modalité chiffrée dans la page). Texte de campagne, non doublé en section f.

### Désignation du candidat

### [C-LR-17] Déclaration de candidature de Bruno Retailleau (12 février 2026)
- Auteur : Bruno Retailleau, président des Républicains
- Date : 2026-02-12
- Nature : texte de l'allocution vidéo, publié sur le site du parti ; relais : Public Sénat, 2026-02-12 (`00-perimetre.md`, source 5)
- URL : https://republicains.fr/actualites/2026/02/12/je-suis-candidat-a-lelection-presidentielle/
- Archivage : texte archivé, `corpus/C-LR-17-declaration-candidature-retailleau-2026-02-12-2026-10-27.md`
- Statut : position du président du parti, candidat déclaré
- Étiquette : source du parti, partie prenante
- Utile pour : thèmes de campagne (immigration, travail, vérité) ; Q6 bloc a (engagement « de toujours vous dire la vérité » : formule d'intention, pas un engagement de méthode au sens du socle, à classer à l'étape 5 bis).

### [C-LR-18] Désignation du candidat : Bureau politique du 24 mars 2026 et consultation des adhérents des 18 et 19 avril 2026
- Auteur : Les Républicains
- Date : 2026-03-24 (BP) ; 2026-04-20 (résultat)
- Nature : communiqué du BP (bilan des municipales, élections internes, trois options de désignation) ; communiqué des résultats (participation 60,01 %, 151 blancs, 12,2 % / 14 % / 73,8 %)
- URL : https://republicains.fr/wp-content/uploads/2026/03/CP_LR_240326_V2.pdf ; https://republicains.fr/actualites/2026/04/20/bruno-retailleau-largement-designe-comme-candidat-des-republicains-pour-lelection-presidentielle/
- Archivage : PDF archivé `corpus/C-LR-18-communique-bureau-politique-2026-03-24-2026-10-27.pdf` ; texte archivé `corpus/C-LR-18-designation-candidat-2026-04-19-2026-10-27.md` (les deux textes)
- Statut : texte du parti (décision des adhérents au titre de l'article 21 des statuts)
- Étiquette : source du parti, partie prenante
- Utile pour : acte de désignation ; Q6 bloc a (vote des adhérents). Le nombre d'inscrits et de votants n'est pas publié.

### Textes du parti et du groupe depuis 2024

### [C-LR-19] « Pacte législatif d'urgence. Revaloriser le travail, restaurer l'autorité » (22 juillet 2024)
- Auteur : la Droite républicaine (députés du groupe DR et sénateurs LR ; présenté par Laurent Wauquiez et Bruno Retailleau, alors président du groupe LR du Sénat)
- Date : PDF créé le 2024-07-22
- Nature : 9 pages : une priorité (travail plutôt qu'assistanat : heures supplémentaires sans impôt ni charge, aide sociale unique plafonnée par rapport au Smic, assurance chômage), trois axes (autorité et immigration : peines planchers, suspension d'aides sociales pour délinquants et parents de mineurs délinquants, présomption de légitime défense ; réindustrialisation ; services publics locaux), deux « lignes rouges » (hausse d'impôts ; économies sur les retraités), 13 textes législatifs annoncés
- URL : document hébergé par un média : https://reporterre.net/IMG/pdf/pacte-legislatif-droite-republicaine-2.pdf (lien depuis l'article de Reporterre du 2024-07-24) ; relais : franceinfo (2024-07-23) et Public Sénat (2024-07-22), voir `00-perimetre.md`, source 13
- Archivage : PDF archivé, `corpus/C-LR-19-pacte-legislatif-urgence-2024-07-22-2026-10-27.pdf` (0,1 Mo)
- Statut : position du groupe DR et du groupe LR du Sénat (pas de vote d'instance du parti trouvé ; le parti était alors en crise de direction après l'alliance d'Éric Ciotti avec le RN)
- Étiquette : source du parti, partie prenante ; hébergeur : [Reporterre : étiquette proposée, voir « Étiquettes proposées »]. L'original n'a pas été trouvé sur un site du parti ou du groupe ; l'authenticité repose sur la concordance avec les relais (13 textes, deux lignes rouges, mesures citées).
- Utile pour : axes 2, 3, 4, 5 ; référence de la période 2024 (catégorie b, en l'absence de programme législatif écrit [C-LR-28]). La liste des 13 textes n'est pas dans le document (voir « Trous »).

### [C-LR-20] Déclaration politique du groupe Droite Républicaine (19 juillet 2024, et version en ligne actualisée)
- Auteur : groupe DR (47 députés signataires)
- Date : PDF du 2024-07-19 ; version de la page du site du groupe non datée, postérieure à la nomination de Michel Barnier (elle mentionne le « pacte législatif », le soutien au Premier ministre « issu de la droite républicaine » et le « plan d'économies détaillé »)
- Nature : déclaration politique (article 19 du règlement de l'Assemblée)
- URL : https://www.deputesdroiterepublicaine.fr/images/documents/DECLARATION-POLITIQUE-LA-DROITE-REPUBLICAINE-DEPUTES-ET-APPARENTES-19-JUILLET-2024.pdf ; https://www.deputesdroiterepublicaine.fr/vie-du-groupe/declaration-politique
- Archivage : PDF archivé `corpus/C-LR-20-declaration-politique-groupe-dr-2024-07-19-2026-10-27.pdf` (1,0 Mo) ; texte archivé de la page `corpus/C-LR-20-declaration-politique-groupe-dr-2026-10-27.md`
- Statut : position du groupe
- Étiquette : source du parti, partie prenante
- Utile pour : statut du groupe (« opposition responsable » en juillet 2024, puis soutien au gouvernement Barnier) ; Q6 bloc c. Les deux versions ne portent pas sur le même moment : précision successive, pas divergence.

### [C-LR-21] Élection du président de LR (18 mai 2025) et nomination de l'équipe dirigeante (22 mai 2025)
- Auteur : Les Républicains (Haute Autorité ; président)
- Date : 2025-05-18 et 2025-05-22
- Nature : deux pages : résultats proclamés (Bruno Retailleau 74,31 %, Laurent Wauquiez 25,69 % ; 121 617 inscrits, 98 110 votants) ; équipe dirigeante
- URL : https://republicains.fr/actualites/2025/05/18/election-du-president-des-republicains-resultats-du-vote/ ; https://republicains.fr/actualites/2025/05/22/nomination-de-la-nouvelle-equipe-dirigeante-des-republicains/
- Archivage : texte archivé, `corpus/C-LR-21-election-president-et-equipe-2025-05-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : direction du parti ; qui parle pour le parti.

### [C-LR-22] Statuts de 2025 (projet soumis au congrès des 6 et 7 septembre 2025) et résultat du vote
- Auteur : Les Républicains
- Date : projet daté du 2025-08-29 ; vote des 6 et 7 septembre 2025 (97,24 %, 42 701 votants) ; page du 2025-09-08
- Nature : statuts (35 articles, 23 pages) ; page de résultat
- URL : https://republicains.fr/wp-content/uploads/2025/11/2025-08-29-lR-congres-statuts-projet.pdf ; https://republicains.fr/actualites/2025/09/08/9724-des-adherents-approuvent-les-nouveaux-statuts/
- Archivage : PDF archivé `corpus/C-LR-22-statuts-2025-2026-10-27.pdf` (0,3 Mo) ; texte archivé `corpus/C-LR-22-page-adoption-statuts-2025-09-08-2026-10-27.md`
- Statut : texte du parti (adopté par les adhérents)
- Étiquette : source du parti, partie prenante
- Utile pour : instances, article 21 (désignation du candidat), article 30 (suspensions et sanctions) pour le bloc (d) ; article 2 (le mouvement défend « l'intérêt national au sein de l'Union européenne ») pour l'axe 6. Le fichier en ligne porte la mention « projet » : le texte définitif n'a pas été trouvé (voir « Trous »).

### [C-LR-23] Charte des principes fondamentaux des Républicains (2019)
- Auteur : Les Républicains
- Date : PDF créé le 2019-09-26 (fichier daté du 2019-10-02)
- Nature : charte, 48 pages, douze principes, notes d'approbation des adhérents et des sympathisants
- URL : https://republicains.fr/wp-content/uploads/2025/11/2019-10-02-lR-charte-principes-fondamentaux.pdf
- Archivage : PDF archivé, `corpus/C-LR-23-charte-principes-fondamentaux-2019-2026-10-27.pdf` (0,5 Mo)
- Statut : texte du parti (principes)
- Étiquette : source du parti, partie prenante
- Utile pour : bloc (d) (principe, pas engagement explicite, au sens de la précision i du socle, sauf règle d'investiture : à vérifier à l'étape 5 bis) ; axe 6 (« une Europe qui assume sa puissance et protège sa monnaie, ses frontières et sa civilisation »).

### [C-LR-24] Non-participation au gouvernement Lecornu II (11 au 13 octobre 2025)
- Auteur : Les Républicains (BP ; communiqué ; lettre du président aux adhérents)
- Date : 2025-10-11, 2025-10-12, 2025-10-13
- Nature : trois pages : délibération du BP (soutien texte par texte, pas de participation, « large majorité ») ; communiqué (les membres entrés au gouvernement « ne peuvent plus se réclamer » de LR) ; lettre « Pourquoi j'ai décidé de quitter le gouvernement » (pas de censure, consultation des adhérents annoncée)
- URL : https://republicains.fr/actualites/2025/10/11/bureau-politique-des-republicains-du-11-octobre/ ; https://republicains.fr/actualites/2025/10/12/les-republicains-refusent-de-participer-au-gouvernement-lecornu/ ; https://republicains.fr/actualites/2025/10/13/pourquoi-jai-decide-de-quitter-le-gouvernement/
- Archivage : texte archivé, `corpus/C-LR-24-non-participation-gouvernement-lecornu-2025-10-2026-10-27.md`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : chronologie de la participation (`00-perimetre.md`) ; Q6 blocs b et c. Le communiqué du 12 octobre date la délibération du BP du 10 octobre, la page du BP et LCP du 11 octobre (écart de date listé en « Trous »).

### [C-LR-25] « Face à la dette, Les Républicains appellent à une refondation juste et responsable » (16 juillet 2025)
- Auteur : Les Républicains (signé Bruno Retailleau)
- Date : 2025-07-16
- Nature : déclaration du parti en réponse aux orientations budgétaires du Premier ministre (effort à faire porter aussi sur « ceux qui ne cotisent pas », AME, suppressions de postes plus fortes ; groupe de travail commun députés, sénateurs et direction annoncé)
- URL : https://republicains.fr/actualites/2025/07/16/face-a-la-dette-les-republicains-appellent-a-une-refondation-juste-et-responsable/
- Archivage : texte archivé, `corpus/C-LR-25-refondation-face-a-la-dette-2025-07-16-2026-10-27.md`
- Statut : texte du parti, pendant la participation au gouvernement Bayrou
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1 et 3 ; position du parti en coalition (Q4, Q6).

### [C-LR-26] Équipe des porte-parole de la campagne (8 septembre 2026)
- Auteur : Bruno Retailleau, candidat
- Date : 2026-09-08
- Nature : communiqué, 1 page (neuf porte-parole, coordination par Othman Nasrou)
- URL : https://republicains.fr/wp-content/uploads/2026/09/CP_BR_PP_809.pdf
- Archivage : PDF archivé, `corpus/C-LR-26-communique-porte-paroles-2026-09-08-2026-10-27.pdf`
- Statut : texte du candidat
- Étiquette : source du parti, partie prenante
- Utile pour : qui parle pour le candidat.

### [C-LR-27] « Nos secrétaires nationaux 2026 »
- Auteur : Les Républicains
- Date : PDF créé le 2026-01-16 (page « Nomination de nos secrétaires nationaux » du même jour)
- Nature : liste, 1 page
- URL : https://republicains.fr/wp-content/uploads/2026/01/LR_SN_2026_V3.pdf
- Archivage : PDF archivé, `corpus/C-LR-27-secretaires-nationaux-2026-2026-10-27.pdf`
- Statut : texte du parti
- Étiquette : source du parti, partie prenante
- Utile pour : qualité des locuteurs (immigration et intégration, justice, budget, lutte contre l'entrisme, etc.) ; bloc (d) (règle 1 : membres de la direction nationale).

---

## b. Programme des législatives 2024 (priorité 2)

### [C-LR-28] Législatives de juin et juillet 2024 : aucun programme écrit de LR trouvé
- Auteur : sans objet
- Date : campagne du 10 juin au 7 juillet 2024
- Nature : recherche négative. Le site du parti n'a aucune publication entre juin et décembre 2024 (interface publique interrogée le 2026-10-27 : zéro article) ; la capture de la page d'accueil du 25 juin 2024 (Wayback Machine) ne montre aucun programme législatif, seulement des pages des européennes et des pages anciennes (contre-budget, « contre-gouvernement »). Relais : La finance pour tous, « Élections législatives 2024 : propositions économiques des principaux partis ou coalitions », 2024-06-26 (baisse des cotisations des salariés gagnant moins de 4 200 € net, moins de fonctionnaires, baisse des impôts des entreprises, pas de retour sur la réforme de l'assurance chômage, pas de proposition de réforme des retraites ; aucun lien vers un document de LR)
- URL : https://www.lafinancepourtous.com/2024/06/26/elections-legislatives-2024-propositions-economiques-des-principaux-partis-ou-coalitions/ ; capture : https://web.archive.org/web/20240625085224/https://republicains.fr/
- Archivage : lien seul
- Statut : relais (pas de source primaire)
- Étiquette : La finance pour tous (étiquette existante : institut d'éducation financière)
- Utile pour : constat d'absence ; le pacte législatif du 22 juillet 2024 [C-LR-19] et la déclaration du groupe [C-LR-20] sont les premiers textes programmatiques de la législature.

---

## c. Programme présidentiel 2022 (priorité 3)

### [C-LR-29] Valérie Pécresse, « Le courage de faire » (programme, 16 pages)
- Auteur : campagne de Valérie Pécresse, candidate LR
- Date : PDF créé le 2022-03-19
- Nature : programme présidentiel, 16 pages
- URL : https://valeriepecresse.fr/wp-content/uploads/2022/03/16P-VP2022-ok.pdf
- Archivage : PDF archivé, `corpus/C-LR-29-pecresse-le-courage-de-faire-2022-2026-10-27.pdf` (2,4 Mo)
- Statut : programme officiel (document de campagne)
- Étiquette : source du parti, partie prenante
- Utile pour : mesures de 2022 (Q5 : non reprises, insuffisantes seules) ; repère des évolutions de programme (règle 11). Le programme complet en ligne (pages thématiques du site de campagne) et la profession de foi n'ont pas été archivés (voir « Trous »).

---

## d. Contre-budgets, plans d'économies et amendements budgétaires (priorité 4)

### [C-LR-30] Plan de 50 Md€ d'économies du groupe DR sur le budget 2025 (2 octobre 2024)
- Auteur : groupe DR (Laurent Wauquiez)
- Date : 2024-10-02
- Nature : plan d'économies (dossier de presse du groupe selon le relais) : 13 Md€ sur les agences et opérateurs, 12 Md€ sur les aides sociales (dont allocation sociale unique plafonnée), 7 Md€ sur les dépenses liées à l'immigration (AME), près de 18 Md€ d'« année blanche »
- URL : relais LCP, « Face à "la situation catastrophique de nos finances publiques", Laurent Wauquiez présente un plan d'économies de 50 milliards », 2024-10-02, mis à jour le 2024-10-10 : https://lcp.fr/actualites/face-a-la-situation-catastrophique-de-nos-finances-publiques-laurent-wauquiez-presente
- Archivage : lien seul (dossier de presse non trouvé)
- Statut : position du groupe (le groupe soutient alors le gouvernement Barnier)
- Étiquette : source du parti, partie prenante (relais LCP)
- Utile pour : axe 1 ; continuité des plans du groupe.

### [C-LR-31] Plan de « 40 milliards d'euros d'économies » du groupe DR pour le budget 2026 (29 avril 2025)
- Auteur : groupe DR ; page publiée sur le site d'une députée du groupe
- Date : 2025-04-29
- Nature : trois blocs chiffrés sur la page : bureaucratie 10,6 Md€, travail plutôt qu'assistanat 15,6 Md€ (allocation sociale unique plafonnée à 70 % du Smic, arrêts maladie, fraude), immigration 6,2 Md€ (durée minimale de résidence pour les prestations non contributives, AME recentrée sur l'urgence, fin du titre de séjour pour soins, hébergement d'urgence réservé aux étrangers en situation régulière) ; total des blocs 32,4 Md€, l'écart avec 40 Md€ n'est pas expliqué sur la page (calcul par nos soins)
- URL : https://www.annelaureblin.fr/a-l-assemblee/article/budget-2026-la-droite-republicaine-proposition-40-milliards-d-euros-d-economies
- Archivage : lien seul (aucun document du groupe trouvé)
- Statut : position du groupe, connue par la page d'une élue
- Étiquette : source du parti, partie prenante
- Utile pour : axes 1, 2, 3.

### [C-LR-32] Sénat, PLF 2026 : « plus de 30 milliards d'euros d'économies » (entretien de Bruno Retailleau, 24 novembre 2025)
- Auteur : Bruno Retailleau, président du parti (entretien)
- Date : 2025-11-24
- Nature : entretien publié sur le site du parti
- URL : https://republicains.fr/actualites/2025/11/24/bruno-retailleau-ce-budget-cest-le-hold-up-du-siecle/
- Archivage : fiche texte, `corpus/C-LR-32-retailleau-entretien-budget-2026-senat-2025-11-24-2026-10-27.md`
- Statut : position du parti ; le détail des amendements du Sénat n'est pas archivé
- Étiquette : source du parti, partie prenante
- Utile pour : axe 1 (stratégie de la majorité sénatoriale LR sur le PLF 2026).

### [C-LR-33] PLF 2027 : 20 Md€ d'économies supplémentaires demandées par le groupe DR (4 octobre 2026)
- Auteur : groupe DR (Laurent Wauquiez, entretien aux *Échos* relayé par l'AFP)
- Date : 2026-10-04
- Nature : renvoi : la déclaration est archivée en section f, fiche [C-LR-78] (50 000 postes, agences, RSA limité à deux ans pour les personnes aptes, AME en aide d'urgence, aides sociales aux étrangers après deux ans) ; aucun document du groupe trouvé
- URL : voir [C-LR-78]
- Archivage : renvoi
- Statut : position du groupe
- Étiquette : source du parti, partie prenante
- Utile pour : axe 1 ; contre-budget du groupe sur le PLF 2027.

### [C-LR-34] Amendement n° I-618 au PLF 2026 (défiscalisation totale des heures supplémentaires)
- Auteur : Laurent Wauquiez, premier signataire, et 44 députés nommés (président du groupe et liste nominative : 45 signataires du groupe sur 50 à la date du dépôt, 90,0 %, script `lr_textes_du_groupe.py`) : **texte du groupe** (liste d'au moins 90 %, à la limite exacte du seuil ; texte du président du groupe défendu en séance)
- Date : 2025-10-20 ; **adopté** (scrutin gelé 3089 du 2025-10-25, `votes/scrutins.md`)
- Nature : amendement après l'article 2 (suppression du plafond de 7 500 € de l'exonération d'impôt sur le revenu des heures supplémentaires)
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/1906A/AN/618
- Archivage : PDF archivé, `corpus/C-LR-34-amendement-I-618-plf-2026-2026-10-27.pdf`
- Statut : groupe parlementaire ; adopté en première lecture
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (scrutin gelé 3089).

### [C-LR-35] Amendement n° I-269 au PLF 2026 (indexation du barème de l'impôt sur le revenu)
- Auteur : Laurent Wauquiez, premier signataire, et 45 députés nommés (46 signataires du groupe sur 50, 92,0 %) : **texte du groupe**
- Date : 2025-10-20 ; **adopté** (scrutin de réserve 3096 du 2025-10-25)
- Nature : amendement après l'article 2 (revalorisation des seuils et des tranches du barème)
- URL : https://www.assemblee-nationale.fr/dyn/17/amendements/1906A/AN/269
- Archivage : PDF archivé, `corpus/C-LR-35-amendement-I-269-plf-2026-2026-10-27.pdf`
- Statut : groupe parlementaire ; adopté en première lecture
- Étiquette : source du parti, partie prenante
- Utile pour : axe 4 (scrutin de réserve 3096).

---

## e. PPL, PPLC, PPR du groupe DR, par axe, et textes du groupe LR du Sénat (priorité 5)

Sélection : textes **dont le premier signataire était membre du groupe DR à la date du dépôt** (croisement du jeu open data « Dossiers législatifs », téléchargé le 2026-10-27, avec l'historique des mandats de groupe du jeu AMO30), choisis par axe sur leur objet, plus les textes inscrits aux journées réservées du groupe. Le jeu de données compte **413 textes** (343 PPL, PPLO ou PPLC et 70 propositions de résolution) déposés par un premier signataire DR sur la législature au 2026-10-27 (comptage par nos soins). **Auteur vérifié sur le PDF de l'Assemblée** (bloc « présentée par ») et compté en code (`_scripts/calculs/lr_textes_du_groupe.py`, résultats ci-dessous et dans la colonne Auteur) ; un texte est « du groupe » s'il est inscrit à une journée réservée du groupe, s'il est déposé « et les membres du groupe », ou si sa liste nominative réunit au moins 90 % du groupe à la date du dépôt ; sinon c'est un **texte d'élus du groupe**. **Limite constatée** : le PDF diffusé en données ouvertes est régénéré et peut porter des cosignatures postérieures au dépôt (PPL 1550 : une députée entrée au groupe en avril 2026 figure en fin de liste) ; le script écarte les signataires absents du groupe à la date du dépôt, mais le pourcentage reste un plafond. Statuts relevés dans les actes des dossiers au 2026-10-27. PDF : `https://www.assemblee-nationale.fr/dyn/opendata/<identifiant>.pdf`.

**Journées réservées du groupe DR** (relais LCP, dates confirmées par les actes de commission des dossiers) :

### [C-LR-36] Niche du groupe DR du 6 février 2025
- Auteur : groupe DR
- Date : 2025-02-06 (article du 2025-02-03, mis à jour le 2025-03-03)
- Nature : huit PPL inscrites : nationalité à Mayotte (PPL 693, texte de commission 864), titre de séjour pour étranger malade (689), priorité aux travailleurs dans le logement social (687, texte de commission 865), plafonnement du cumul des prestations (765, texte de commission 862), heures supplémentaires hors revenu fiscal de référence (753, texte de commission 863), suspension des allocations familiales des parents de mineurs délinquants (681), importations agricoles (659, texte de commission 861), entraves à la chasse et à l'élevage (579, texte de commission 867)
- URL : relais LCP : https://lcp.fr/actualites/travail-immigration-securite-pour-leur-niche-parlementaire-les-deputes-lr-se-concentrent
- Archivage : lien seul (aucun dossier de presse du groupe trouvé)
- Statut : groupe parlementaire (inscription à la journée réservée : critère « du groupe »)
- Étiquette : relais LCP (pas d'étiquette)
- Utile pour : identification des textes portés par le groupe.

### [C-LR-37] Niche du groupe DR du 22 janvier 2026
- Auteur : groupe DR
- Date : 2026-01-22 (article du 2026-01-12, mis à jour le 2026-01-14)
- Nature : PPL inscrites : voilement des mineures dans l'espace public (2167), suspension des prestations pour exactions (1550), présomption de légitime défense (691), travail le 1er mai (texte du Sénat), déblocage de l'épargne salariale, saisie des amendes sur les minima sociaux, hébergement d'urgence (2229), continuité des transports (texte n° 140, venu du Sénat) ; deux propositions de résolution (Frères musulmans, 1455 ; suspension de nouvelles instances administratives, 2206)
- URL : relais LCP : https://lcp.fr/actualites/voile-des-mineures-ordre-public-travail-a-l-occasion-de-leur-niche-parlementaire-les ; communiqué du groupe sur la résolution adoptée (lien seul) : https://www.deputesdroiterepublicaine.fr/actualite/articles/61-dans-les-medias/5949-resolution-portee-par-la-droite-republicaine-lassemblee-vote-en-faveur-de-linscription-des-freres-musulmans-sur-la-liste-terroriste-europeenne
- Archivage : lien seul
- Statut : groupe parlementaire
- Étiquette : relais LCP (pas d'étiquette)
- Utile pour : identification des textes portés par le groupe.

| ID | Texte | Objet | Auteur (contrôle `lr_textes_du_groupe.py`) | Dépôt | Axe | Statut au 2026-10-27 | Archive |
|---|---|---|---|---|---|---|---|
| C-LR-38 | PPLC 2352 | Principe d'équilibre des finances publiques, norme constitutionnelle contraignante | Véronique Louwagie ; **texte d'élus du groupe** (liste de 20 signataires, tous du groupe, sur 49, 40,8 % ; hors niche) | 2026-01-19 | 1 | Déposée, en commission | PDF |
| C-LR-39 | PPL 765 | Plafonner le cumul de prestations sociales (aide sociale unique) | Yannick Neuder, Laurent Wauquiez et 44 autres ; **groupe** (niche du 6 février 2025 ; liste de 46 sur 47, 97,9 %) | 2024-12-19 | 2 | Rapport et réunions de commission (texte n° 862) ; pas d'acte de séance dans les données ouvertes | PDF |
| C-LR-40 | PPL 2227 | Limiter à deux ans le RSA pour les personnes aptes au travail | Laurent Wauquiez seul ; **texte d'élus du groupe** (président du groupe, seul signataire, hors niche, non examiné en séance) ; mesure reprise dans le plan du groupe sur le PLF 2027 selon un relais [C-LR-78] | 2025-12-09 | 2 | Déposée, en commission | PDF |
| C-LR-41 | PPL 378 | Protéger la société des étrangers clandestins dangereux et faciliter leur expulsion | Laurent Wauquiez et 42 autres ; **groupe** (liste de 43 sur 47, 91,5 %, plafond ; texte du président du groupe ; hors niche) | 2024-10-15 | 3 | Déposée, en commission | PDF |
| C-LR-42 | PPL 693 | Renforcer les conditions d'accès à la nationalité française à Mayotte | Philippe Gosselin et 45 autres ; **groupe** (niche du 6 février 2025 ; 46 sur 47, 97,9 %) | 2024-12-03 | 3 | **Loi promulguée le 12 mai 2025** (CC, décision n° 2025-881 DC du 7 mai 2025, conforme avec une réserve) : texte adopté sous le gouvernement Bayrou | PDF |
| C-LR-43 | PPL 689 | Abroger le titre de séjour pour étranger malade | Véronique Louwagie, Laurent Wauquiez et 42 autres ; **groupe** (niche du 6 février 2025 ; 44 sur 47, 93,6 %) | 2024-12-03 | 3 | Rejetée en commission selon LCP ; pas d'acte de séance dans les données ouvertes | PDF |
| C-LR-44 | PPL 2229 | Interdire le maintien dans l'hébergement d'urgence aux étrangers en situation irrégulière | Fabien Di Filippo et Anne-Laure Blin ; **groupe** (niche du 22 janvier 2026 ; liste de 2 sur 49) | 2025-12-09 | 3 | Réunions de commission (janvier 2026) ; pas d'acte de séance | PDF |
| C-LR-45 | PPL 238 | Mise en œuvre de recommandations sur les soins dispensés aux étrangers en situation irrégulière (AME) | Véronique Louwagie et 22 autres ; **texte d'élus du groupe** (23 sur 47, 48,9 % ; hors niche) | 2024-09-17 | 3 | Déposée, en commission | PDF |
| C-LR-46 | PPL 753 | Exclure les heures supplémentaires du calcul du revenu fiscal de référence | Corentin Le Fur seul ; **groupe** (niche du 6 février 2025, texte de commission 863) | 2024-12-19 | 4 | Adoptée en commission avec un plafond selon LCP ; pas d'acte de séance dans les données ouvertes | PDF |
| C-LR-47 | PPL 3230 | Réformer le droit des successions et des donations | Éric Pauget et 15 autres ; **texte d'élus du groupe** (16 sur 47, 34,0 % ; hors niche) | 2026-10-06 | 4 | Déposée, en commission | PDF |
| C-LR-48 | PPL 691 | Présomption de légitime défense pour les forces de l'ordre | Éric Pauget, Laurent Wauquiez et 43 autres ; **groupe** (niche du 22 janvier 2026 ; 45 sur 47, 95,7 %) | 2024-12-03 | 5 | **Adoptée en première lecture le 7 juillet 2026** (scrutin gelé 7987), transmise au Sénat | PDF |
| C-LR-49 | PPL 1550 | Suspendre les prestations et aides publiques des personnes coupables d'exactions lors de rassemblements | Corentin Le Fur et 49 autres ; **groupe** (niche du 22 janvier 2026 ; 49 du groupe sur 49 à la date, 100 % ; une cosignataire entrée au groupe en avril 2026 écartée) | 2025-06-10 | 5 | Réunions de commission (janvier 2026) ; pas d'acte de séance | PDF |
| C-LR-50 | PPL 3335 | Exécution effective d'une peine minimale dès la première condamnation pour violences volontaires | Patrick Hetzel « et les membres du groupe Droite Républicaine » ; **groupe** (formule de dépôt) | 2026-10-13 | 5 | Déposée, en commission | PDF |
| C-LR-51 | PPL 2167 | Interdire le voilement des mineures dans l'espace public | Laurent Wauquiez et 29 autres ; **groupe** (niche du 22 janvier 2026, rapporteur Patrick Hetzel selon LCP ; liste de 30 sur 49, 61,2 %) | 2025-12-02 | 5 et 6 | Rapport et réunions de commission ; pas d'acte de séance | PDF |
| C-LR-52 | PPLC 1477 | Contre la proportionnelle : scrutin uninominal majoritaire à deux tours inscrit dans la Constitution | Alexandre Portier, Laurent Wauquiez et 49 autres, dont 4 hors du groupe ; **groupe** (47 du groupe sur 49, 95,9 %, plafond ; hors niche) | 2025-05-28 | 6 | Déposée, en commission | PDF |
| C-LR-53 | PPR 1455 | Inscrire la mouvance des Frères musulmans sur la liste européenne des organisations terroristes | Éric Pauget, Michèle Tabarot, Laurent Wauquiez et 22 autres ; **groupe** (niche du 22 janvier 2026, communiqué du groupe ; liste de 25 sur 48, 52,1 %) | 2025-05-23 | 5 et 6 | **Adoptée le 22 janvier 2026** | PDF |

Fichiers : `corpus/C-LR-<nn>-<type>-<numéro>-<objet>-2026-10-27.pdf`.

Résultat du script (`python3 -I _scripts/calculs/lr_textes_du_groupe.py`, 2026-10-27) : sur 18 textes à liste nominative ou à signataire unique contrôlés (dont les deux amendements de la section d), **9 atteignent 90 % par la liste** (amendements I-618 à 90,0 % et I-269 à 92,0 %, PPL 378, 691, 693, 689, 765 et 1550, PPLC 1477), **1 porte la formule « les membres du groupe »** (PPL 3335), **8 sont sous le seuil**, dont **4 restent « du groupe » par leur inscription à une niche** (PPL 753, 2229, 2167 et PPR 1455) et **4 sont requalifiés « textes d'élus du groupe »** (PPLC 2352, PPL 2227, 238 et 3230). Effectif du groupe aux dates de dépôt : 47 à 50 (membres, dont le président, plus apparentés). Fragile : PPL 378, PPLC 1477 et amendement I-618 ne dépassent le seuil que de peu (voir la limite ci-dessus).

### Textes du groupe LR du Sénat (contexte, étiquetés « groupe LR du Sénat »)

### [C-LR-54] PPL sénatoriale « visant à faciliter le maintien en rétention des personnes condamnées pour des faits d'une particulière gravité et présentant de forts risques de récidive »
- Auteur : Jacqueline Eustache-Brinio, Mathieu Darnaud (président du groupe LR du Sénat) et des sénateurs du groupe LR (PPL n° 298, 2024-2025) : groupe LR du Sénat
- Date : dépôt au Sénat en 2025 ; adoptée par l'Assemblée le 2025-07-08 (scrutin gelé 2958) ; **CC, décision n° 2025-895 DC du 7 août 2025 : articles 1er et 2 et 3° de l'article 4 censurés** (allongement de la rétention, effet suspensif de l'appel), autres dispositions conformes sous réserves ; loi n° 2025-796 du 11 août 2025 selon des relais (Légifrance non ouvert)
- Nature : proposition de loi, devenue loi
- URL : https://www.senat.fr/leg/ppl24-298.html ; https://www.conseil-constitutionnel.fr/decision/2025/2025895DC.htm ; texte de reprise de l'allongement à 210 jours étudié au Sénat : rapport n° 611 (2025-2026) de Hervé Reynaud, https://www.senat.fr/rap/l25-611/l25-611_mono.html
- Archivage : lien seul
- Statut : groupe LR du Sénat ; texte adopté pendant la participation au gouvernement Bayrou (ministre de l'Intérieur LR) : aussi acte de coalition
- Étiquette : source du parti, partie prenante (texte) ; décision du CC : niveau 3
- Utile pour : axe 3 (scrutin gelé 2958) ; faisabilité juridique (Q3).

---

## Actes de coalition (septembre 2024 à octobre 2025)

Liste des textes et décisions utiles aux étapes suivantes, sans analyse (`00-perimetre.md`, « Attribution des actes »). Lecture A : actes comptés pleinement à l'échelle C, documentés comme actes d'un gouvernement de coalition.

### [C-LR-55] Circulaire du ministre de l'Intérieur du 23 janvier 2025 sur l'admission exceptionnelle au séjour
- Auteur : Bruno Retailleau, ministre de l'Intérieur (gouvernement Bayrou)
- Date : 2025-01-23 (NOR INTK2435521J, selon la fiche Légifrance vue en résultat de recherche ; abroge la circulaire du 28 novembre 2012)
- Nature : circulaire aux préfets (régularisation au titre de l'article L. 435-1 du code de l'entrée et du séjour des étrangers)
- URL : https://www.legifrance.gouv.fr/circulaire/id/45584 (non ouvert : Légifrance bloque l'outil, `03-sources-et-hierarchie.md` §6) ; recours : Conseil d'État, décision n° 502722 du 21 novembre 2025, https://www.conseil-etat.fr/fr/arianeweb/CE/decision/2025-11-21/502722 (non ouverte à cette étape) ; contexte : note du GISTI, https://www.gisti.org/IMG/pdf/note_circulaire_retailleau.pdf (non ouverte)
- Archivage : lien seul
- Statut : acte de coalition (ministre LR)
- Étiquette : source officielle, partie prenante ; GISTI : étiquette existante
- Utile pour : axe 3 (Q4, actes) ; Q6 bloc b.

### [C-LR-56] Recours à l'article 49.3 par le gouvernement Barnier (PLFSS 2025) et censure du 4 décembre 2024
- Auteur : Michel Barnier, Premier ministre (LR)
- Date : engagement de responsabilité le 2024-12-02 (date connue par le dossier de la motion) ; censure adoptée le 2024-12-04 (scrutin 519)
- Nature : acte de gouvernement ; motion de censure adoptée
- URL : https://www.assemblee-nationale.fr/dyn/17/scrutins/519
- Archivage : lien seul
- Statut : acte de coalition (Premier ministre LR)
- Étiquette : source primaire (scrutin public)
- Utile pour : Q6 bloc b (usage du 49.3 rapporté à la situation de majorité) ; axe 1 (scrutin gelé 519).

### [C-LR-57] Loi sur la nationalité à Mayotte (PPL du groupe DR, promulguée le 12 mai 2025)
- Auteur : groupe DR (PPL 693, [C-LR-42]), adoptée avec le soutien du gouvernement Bayrou
- Date : décision du CC n° 2025-881 DC du 7 mai 2025 (conforme, réserve au paragraphe 22) ; promulgation le 2025-05-12 (actes du dossier)
- Nature : loi
- URL : https://www.conseil-constitutionnel.fr/decision/2025/2025881DC.htm ; dossier : https://www.assemblee-nationale.fr/dyn/17/dossiers/renforcer_conditions_acces_nationalite_francaise_mayotte
- Archivage : lien seul (texte de la proposition : [C-LR-42])
- Statut : texte du groupe adopté pendant la coalition
- Étiquette : décision du CC : niveau 3
- Utile pour : axe 3.

### [C-LR-58] Composition des gouvernements Barnier, Bayrou et Lecornu I (ministres LR)
- Auteur : sans objet (relais de presse)
- Date : 2024-09-21 ; 2024-12-23 ; 2025-10-05
- Nature : listes des ministres ; aucun document officiel ouvert à cette étape (décret de composition et page info.gouv.fr vus en résultat de recherche, non ouverts)
- URL : sources 14 à 19 de `00-perimetre.md`
- Archivage : lien seul
- Statut : contexte
- Étiquette : relais
- Utile pour : identifier les ministres LR dont les actes sont des actes de coalition (à établir nominativement aux étapes suivantes à partir du décret de composition).

Autres actes à réunir aux étapes suivantes (non archivés ici) : loi contre le narcotrafic de 2025 (PPL sénatoriale transpartisane, portée en séance par le ministre de l'Intérieur ; scrutin gelé 1194) ; réponses aux mobilisations sous l'autorité du ministre de l'Intérieur (septembre 2024 à octobre 2025) ; textes budgétaires de 2025 (budgets Bayrou adoptés après le 49.3 de février 2025, `02-partis/ps/01-corpus.md` en cite les recours).

---

## f. Déclarations publiques depuis le 1er janvier 2026 (priorité 6)

23 déclarations. Par locuteur : Bruno Retailleau 15 (2 comme président du parti avant sa déclaration de candidature du 12 février [C-LR-59], [C-LR-60] ; 3 comme président et candidat déclaré [C-LR-62], [C-LR-63], [C-LR-65] ; 10 comme candidat désigné après le 19 avril, dont un communiqué signé comme président du parti [C-LR-73]) ; François-Xavier Bellamy, premier vice-président et député européen, 1 [C-LR-70] ; groupe Droite Républicaine 5 (Laurent Wauquiez, président du groupe, 1 par relais [C-LR-78] ; interventions en séance au nom du groupe 4 : Ian Boucard, Patrick Hetzel, Marie-Christine Dalloz, Nicolas Ray) ; élus LR du Sénat 2 (Jean-François Husson, rapporteur général, et Gérard Larcher, président du Sénat [C-LR-75] ; David Margueritte, corapporteur, et Gérard Larcher [C-LR-81]). Par type de source : 13 pages de republicains.fr (11 reprennent un entretien ou une tribune parus dans la presse : JDD 5, La Tribune Dimanche 1, Le Figaro 1, Valeurs actuelles 1, entretiens dont le média n'est pas indiqué 3 ; 2 sont des textes signés sans média indiqué, [C-LR-59] et [C-LR-72]), 1 communiqué en PDF du parti copié en entier [C-LR-73], 4 comptes rendus intégraux de l'Assemblée, 5 relais de presse ouverts (trois reprises de dépêches AFP : Brut, Fortuneo, La Gazette France ; un article de Public Sénat ; le fil de CNews rapportant un entretien au *Monde*). Chaque déclaration a sa fiche texte dans `corpus/` (date, locuteur, qualité, média, format, axe, URL ouverte, date de consultation, statut, étiquette, position en paraphrase, citations de 15 mots au plus vérifiées en code contre le texte relevé par le second sous-agent). « Site du parti » : texte publié sur republicains.fr (partie prenante). « Compte rendu de l'AN » : source primaire. « Relais » : reprise par un média tiers, le média d'origine est indiqué. Les déclarations du 12 février (candidature), du 2 septembre (réforme constitutionnelle), du 26 août (successions) et la présentation du 12 octobre (plan de 197 Md€) sont en section a ([C-LR-17], [C-LR-15], [C-LR-16], [C-LR-12]) et ne sont pas doublées ici. L'annonce sur les retraites du 22 septembre 2026 (sur LCI, relayée par franceinfo et l'AFP : âge minimal de départ à 63 ans, décote de 7 % par an avant 65 ans, taux plein automatique à 65 ans, capitalisation pour les jeunes à hauteur de 25 à 30 % de leur retraite, 40 Md€ d'économies cumulées sur cinq ans) n'a pas de fiche propre : relais ouvert, https://www.franceinfo.fr/politique/bruno-retailleau/s-il-est-elu-bruno-retailleau-veut-instaurer-un-age-minimal-de-depart-a-la-retraite-a-63-ans-le-taux-plein-a-65_8205254.html (2026-09-22), à archiver en fiche par l'étape 2 si l'axe 2 la retient ; la page du parti du 23 septembre sur ce thème est une vidéo sans texte.

Écart avec la consigne, signalé par le second sous-agent et maintenu : les fiches des pages de republicains.fr ne contiennent pas la copie intégrale du texte quand la page reprend un entretien conduit par un journaliste ou une tribune parue d'abord dans la presse (onze cas) ; la règle de citation (15 mots au plus, pas de reproduction de passages d'articles) l'emporte. Chaque fiche donne un relevé de la structure de la page et l'adresse de l'interface publique du site (`https://republicains.fr/wp-json/wp/v2/posts/<identifiant>`) qui permet de relever le texte. Le communiqué du 31 juillet 2026 est copié en entier ([C-LR-73]) ; les deux textes signés sans média indiqué ([C-LR-59], [C-LR-72]) n'ont pas été copiés par le second sous-agent, par symétrie : copie possible à la relecture.

| ID | Date | Média d'origine | Format | Axe | Position (résumé) | URL |
|---|---|---|---|---|---|---|
| C-LR-59 | 2026-01-05 | republicains.fr (Bruno Retailleau) | communiqué signé | 6 | Refus de la dépendance numérique envers les plateformes américaines ; « voie propre » de la France et de l'Europe fondée sur la souveraineté | https://republicains.fr/actualites/2026/01/05/refuser-la-dependance-numerique-culturelle-defendre-lindependance-europeenne/ (site du parti) |
| C-LR-60 | 2026-01-07 | conférence de presse (Bruno Retailleau) | conférence de presse | 6 | Si le président vote pour l'accord UE-Mercosur, il « prend le risque d'une censure » ; pas d'appel à censurer avant le vote | https://www.brut.media/fr/articles/retailleau-previent-si-macron-vote-pour-le-mercosur-il-prend-le-risque-dune-censure-du-gouvernement (relais AFP par Brut ; date de la page erronée, voir fiche) |
| C-LR-61 | 2026-01-22 | séance de l'AN (Ian Boucard) | intervention en séance | 5 | PPL n° 691 du groupe : présomption simple de légitime défense pour policiers et gendarmes, réécrite avec le gouvernement | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-jeudi-22-janvier-2026 (compte rendu de l'AN) |
| C-LR-62 | 2026-02-18 | Valeurs actuelles, repris sur republicains.fr (Bruno Retailleau) | tribune | 5 et 6 | Cordon sanitaire autour de LFI ; pas de front républicain avec l'extrême gauche, « principale et pire menace » | https://republicains.fr/actualites/2026/02/18/jappelle-a-dresser-un-cordon-sanitaire-autour-de-la-france-insoumise/ (site du parti) |
| C-LR-63 | 2026-03-01 | JDD, repris sur republicains.fr (Bruno Retailleau) | tribune | 6 | Dissuasion strictement nationale, ni partagée ni élargie à l'Europe ; coopérations européennes encadrées dans l'UE et l'Otan | https://republicains.fr/actualites/2026/03/01/la-dissuasion-nucleaire-francaise-ne-se-partage-pas/ (site du parti) |
| C-LR-64 | 2026-04-07 | séance de l'AN (Patrick Hetzel) | intervention en séance | 2 | Le groupe vote le projet de loi contre les fraudes : croisement des données, sanctions des fraudes organisées, « ferme et juste » | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2025-2026/deuxieme-seance-du-mardi-07-avril-2026 (compte rendu de l'AN) |
| C-LR-65 | 2026-04-15 | presse (média non indiqué), republicains.fr (Bruno Retailleau) | interview | 2, 4 et 6 | Seuil « zéro charge », compte social unique plafonné à 70 % du Smic, justice plus ferme ; aucun rapprochement avec le RN | https://republicains.fr/actualites/2026/04/15/je-ne-veux-pas-etre-assimile-au-macronisme/ (site du parti) |
| C-LR-66 | 2026-05-02 | JDD, repris sur republicains.fr (Bruno Retailleau) | interview | 3 et 6 | Algérie : visas proportionnés aux réadmissions, exécution des OQTF, dénonciation de l'accord de 1968 dans les premiers mois | https://republicains.fr/actualites/2026/05/02/bruno-retailleau-interview-algerie-macron/ (site du parti) |
| C-LR-67 | 2026-05-02 | La Tribune Dimanche, repris sur republicains.fr (Bruno Retailleau) | tribune | 2, 3 et 4 | « Priorité Travail » : fin de la référence aux 35 h, zéro cotisation au-delà de 1 623 h, cinq ans d'activité avant les aides pour les étrangers, revenu familial de 240 € par enfant, départ en retraite plus tard | https://republicains.fr/actualites/2026/05/02/priorite-travail-france-35h-salaires-retraites/ (site du parti) |
| C-LR-68 | 2026-05-31 | JDD, repris sur republicains.fr (Bruno Retailleau) | interview | 3, 5 et 6 | Référendum sur une loi immigration après révision constitutionnelle ; règles européennes à modifier (regroupement familial) ; aides aux étrangers après cinq ans ; peines planchers, castration chimique | https://republicains.fr/actualites/2026/05/31/ma-candidature-ira-jusquau-bout/ (site du parti) |
| C-LR-69 | 2026-06-06 | presse (média non indiqué), republicains.fr (Bruno Retailleau) | interview | 5 et 6 | Cour disciplinaire de la magistrature à la place du CSM, avec citoyens tirés au sort ; pas d'indépendance du parquet ; référendum pénal | https://republicains.fr/actualites/2026/06/06/il-faut-creer-une-cour-disciplinaire-de-la-magistrature/ (site du parti) |
| C-LR-70 | 2026-06-16 | Le Figaro, repris sur republicains.fr (François-Xavier Bellamy) | interview | 3 et 6 | Règlement européen « retour » : centres de retour, rétention jusqu'à deux ans, visas refusés aux pays non coopératifs ; États maîtres de leur politique migratoire | https://republicains.fr/actualites/2026/06/16/discussion-sans-filtre-avec-francois-lenglet/ (site du parti) |
| C-LR-71 | 2026-07-01 | presse (média non indiqué), republicains.fr (Bruno Retailleau) | interview | 1 et 2 | Intérêts de la dette ; non-remplacement de fonctionnaires partant en retraite, « à peu près 250 000 postes » | https://republicains.fr/actualites/2026/07/01/je-serai-la-surprise-de-cette-election/ (site du parti) |
| C-LR-72 | 2026-07-14 | republicains.fr (Bruno Retailleau) | tribune | 1 et 6 | Défense : Otan « européanisée » sans en sortir, alliances bilatérales, Union sous impulsion des États, pas de « chimères fédéralistes » ; armées à 100 Md€ en fin de quinquennat | https://republicains.fr/actualites/2026/07/14/lunite-nationale-premiere-de-nos-armes/ (site du parti) |
| C-LR-73 | 2026-07-31 | communiqué du président du parti (PDF sur republicains.fr) | communiqué | 3 et 6 | Suspension de la libre circulation des personnes avec l'Espagne dans l'Union, contrôle à la frontière, visas territorialisés, centres de retour du règlement européen | https://republicains.fr/wp-content/uploads/2026/08/CP_BR_31_07_26.pdf (site du parti ; copie intégrale) |
| C-LR-74 | 2026-08-02 | JDD, repris sur republicains.fr (Bruno Retailleau) | interview | 3 et 6 | « Pas du tout fédéraliste », « double membrane » ; Schengen réservé aux Européens, visas territorialisés, Frontex à Ceuta | https://republicains.fr/actualites/2026/08/02/lespace-schengen-doit-etre-reserve-aux-europeens/ (site du parti) |
| C-LR-75 | 2026-09-04 | Public Sénat (Jean-François Husson ; Gérard Larcher au Parisien) | déclaration rapportée | 1 et 4 | Budget 2027 : redresser les comptes sans hausse de la fiscalité (G. Larcher) ; faire mieux que 5 % de déficit par la dépense (J.-F. Husson) | https://www.publicsenat.fr/actualites/politique/on-est-deja-dans-le-vide-sans-parachute-la-grande-inquietude-de-la-majorite-senatoriale-sur-le-budget-2027 (relais) |
| C-LR-76 | 2026-09-12 | JDD, repris sur republicains.fr (Bruno Retailleau) | interview | 1, 4, 5 et 6 | Baisse des cotisations financée par le plafonnement des aides à 70 % du Smic ; électricité, logement ; 150 Md€ d'économies ; référendums contre les « censures abusives » ; voile interdit dans des lieux ciblés | https://republicains.fr/actualites/2026/09/12/les-pressions-ne-marchent-pas-avec-moi-rien-ne-marretera/ (site du parti) |
| C-LR-77 | 2026-09-30 | Le Monde (Bruno Retailleau) | interview rapportée | 3 et 6 | Droit européen « au-dessus de nos lois mais en dessous de la Constitution », primauté conditionnée au respect des traités et de la Constitution | https://www.cnews.fr/france/2026-09-30/presidentielle-2027-bruno-retailleau-veut-placer-le-droit-europeen-en-dessous-de (relais CNews ; Le Monde non ouvert) |
| C-LR-78 | 2026-10-04 | Les Échos (Laurent Wauquiez) | interview rapportée | 1, 2, 3 et 4 | Pas de censure du budget 2027 ; 20 Md€ d'économies en plus : 50 000 postes, agences, RSA limité à deux ans, AME en aide d'urgence, aides sociales aux étrangers après deux ans | https://bourse.fortuneo.fr/actualites/budget-2027-wauquiez-affirme-que-lr-ne-pratiquera-pas-le-petit-jeu-de-la-censure-9699288 (relais AFP par Fortuneo ; Les Échos non ouvert) |
| C-LR-79 | 2026-10-13 | séance de l'AN (Marie-Christine Dalloz) | intervention en séance | 1 et 4 | Contre la motion de rejet socialiste : contribution sur les hauts revenus reconduite, baisse des dépenses plutôt que des taxes | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-mardi-13-octobre-2026 (compte rendu de l'AN) |
| C-LR-80 | 2026-10-13 | séance de l'AN (Nicolas Ray) | intervention en séance | 1, 2, 3 et 4 | Redressement « intégralement » par la dépense ; soutien à l'indexation du barème de l'IR ; 20 Md€ d'économies (agences, allocation unique à 70 % du Smic, délai de carence pour les étrangers, AME réformée et non supprimée) | https://www.assemblee-nationale.fr/dyn/17/comptes-rendus/seance/session-ordinaire-de-2026-2027/deuxieme-seance-du-mardi-13-octobre-2026 (compte rendu de l'AN) |
| C-LR-81 | 2026-10-21 | Sénat, commission des lois (David Margueritte ; Gérard Larcher au Figaro) | déclaration rapportée | 5 | Projet de loi « casseurs-payeurs » durci en commission (RSA mobilisable, interdiction du territoire) ; soutien du corapporteur LR et du président du Sénat | https://www.lagazettefrance.fr/article/casseurs-payeurs-apres-les-violences-du-17-octobre-la-reponse-legislative-au-senat (relais AFP par La Gazette France) |

Fichiers : `corpus/C-LR-<nn>-<locuteur>-<objet>-<date de la déclaration>-2026-10-27.md`.

Répartition par axe (une déclaration peut compter pour plusieurs) : axe 1 : 7 ; axe 2 : 6 ; axe 3 : 9 ; axe 4 : 7 ; axe 5 : 6 ; axe 6 : 14. L'axe 2 est le plus mince côté parti : hors des textes du candidat, une seule déclaration du groupe porte d'abord sur le travail ou la fraude ([C-LR-64], vote du projet de loi fraudes) ; les mesures sociales du groupe sont dans des déclarations budgétaires ([C-LR-78], [C-LR-80]). L'axe 6 mêle l'Europe ([C-LR-59], [C-LR-60], [C-LR-63], [C-LR-70], [C-LR-72], [C-LR-73], [C-LR-74], [C-LR-77]) et les institutions (référendum, Conseil constitutionnel, magistrature, alliances : [C-LR-62], [C-LR-68], [C-LR-69], [C-LR-76]).

**Appartenance à l'Union européenne (consigne de la page)** : aucune **déclaration** explicite de 2026 sur le maintien ou la sortie n'a été trouvée (voir ci-dessous). Deux **textes du parti** en tiennent lieu et sont à citer en priorité : l'article 2 des statuts de 2025, qui assigne au mouvement de défendre « l'intérêt national au sein de l'Union européenne » [C-LR-22], et l'exposé des motifs du projet de loi constitutionnelle d'août 2026, qui maintient « la participation de la République à l'Union européenne » de l'article 88-1 et la primauté du droit de l'Union sur la loi, sauf contrariété à la Constitution ou méconnaissance de la répartition des compétences [C-LR-13]. Déclarations proches : [C-LR-77] (droit européen « au-dessus de nos lois mais en dessous de la Constitution », relais unique) ; [C-LR-74] (« pas du tout fédéraliste », « double membrane »).

Intégration (2026-10-27, sous-agent de l'étape 1) : identifiants C-LR-59 à C-LR-81 attribués dans l'ordre chronologique du brouillon du second sous-agent (identifiants provisoires C-LR-F01 à C-LR-F22), fichiers renommés en conséquence ; une fiche ajoutée, [C-LR-73] (communiqué du 31 juillet 2026, trouvé dans la médiathèque du site), insérée à sa date ; aucune fiche de la section a ne double une déclaration de la section f.


---

## Actes

Applicable, à part : LR n'a pas exercé le pouvoir national dans la fenêtre comme force dirigeante d'une majorité ; le mandat 2007-2012 (UMP) est hors fenêtre et ne compte pas. Ses actes dans la fenêtre sont ceux de ses ministres et des textes adoptés sous les gouvernements Barnier, Bayrou et Lecornu I (septembre 2024 à octobre 2025), documentés comme **actes de coalition** : section « Actes de coalition » ci-dessus ([C-LR-55] à [C-LR-58], et [C-LR-42], [C-LR-54] pour deux textes adoptés). Renvoi : `00-perimetre.md`, « Attribution des actes » (chronologie datée ; lecture A ; Q6 : blocs a, b, c et d applicables, le bloc b sur la période de coalition). Aucune source sur les actes de 2024-2025 (lois promulguées, circulaires, budgets exécutés) n'est archivée en PDF à cette étape.

---

## Trous

**Non trouvé**
- **Programme présidentiel 2027 complet** : non publié au 2026-10-27 ; aucune date annoncée trouvée. Le site du parti tient lieu de site de campagne ; aucun site distinct du candidat n'a été trouvé (recherches sur le nom du candidat et « 2027 »).
- **Livrets sur l'immigration, la sécurité, la justice, les retraites, les institutions ou l'Europe** : aucun dans la série « Nos propositions pour la France » au 2026-10-27 (huit livrets : travail, production, agriculture, famille, électricité, logement, IA, école).
- **Liste des 13 textes du pacte législatif de juillet 2024** : le document [C-LR-19] annonce « 13 textes législatifs » sans les énumérer ; les relais n'en donnent pas la liste ; les PPL correspondantes n'ont pas été identifiées une à une dans les données ouvertes (à faire aux étapes suivantes en croisant les dépôts DR de septembre à décembre 2024).
- **Programme des législatives 2024** : aucun document écrit de LR [C-LR-28].
- **Programme 2022 complet et profession de foi** de Valérie Pécresse : non archivés (seul le programme de 16 pages l'est) ; le site de campagne n'est plus en ligne et les captures consultées ne donnent pas de PDF complet.
- **Documents du groupe DR pour ses plans d'économies** (50 Md€ en octobre 2024, 40 Md€ en avril 2025, 20 Md€ en octobre 2026) : aucun dossier de presse ni document du groupe trouvé ; plans connus par des relais ou la page d'une élue ([C-LR-30], [C-LR-31], [C-LR-78]). Le site du groupe (deputesdroiterepublicaine.fr) n'a pas de rubrique de documents et ses listes d'actualité ne s'affichent pas en entier.
- **Détail des « plus de 30 milliards » d'économies votées au Sénat** sur le PLF 2026 (amendements, rapport général) : non ouvert [C-LR-32].
- **Texte définitif des statuts de 2025** : seul le projet soumis au congrès (daté du 29 août 2025) est en ligne [C-LR-22].
- **Décision définitive des instances sur les six membres entrés au gouvernement Lecornu II** (annoncée « dans les tout prochains jours » le 12 octobre 2025) et **résultat de la consultation des adhérents** annoncée le 13 octobre 2025 [C-LR-24] : non trouvés.
- **Retrait de Laurent Wauquiez** de la course présidentielle : aucune déclaration datée (`00-perimetre.md`).
- **Statut de Xavier Bertrand à l'égard du parti** au 2026-10-27 : non établi par une source du parti.
- **Composition officielle des gouvernements** (décrets de composition) : non ouverte ; ministres LR établis par la presse seulement [C-LR-58].
- **Délibération d'une instance du parti sur la participation au gouvernement Barnier** (septembre 2024) : aucune trouvée ; seule la réunion des parlementaires du 11 septembre 2024 est rapportée.
- **Site du parti, période juin à décembre 2024** : l'interface publique ne renvoie aucun article ; l'archive du site antérieure à la refonte n'a pas été exploitée au-delà de la page d'accueil du 25 juin 2024.

**Accès refusés ou partiels**
- Légifrance (circulaire du 23 janvier 2025, loi du 11 août 2025) : non ouvert, conformément à `03-sources-et-hierarchie.md` §6 ; références par le Conseil constitutionnel et des relais.
- France 24 (dépêche du 4 octobre 2026) : refus d'accès ; lu sur Fortuneo [C-LR-78].
- *Le Figaro*, *L'Opinion*, *Les Échos*, *Le Monde*, JDD, *La Tribune Dimanche*, *Valeurs actuelles* : non ouverts ; positions lues sur le site du parti ou dans des relais.
- Bourse Direct (dépêche AFP du 1er juillet 2026 sur Laurent Wauquiez) : erreur 404.

### Trous propres à la section f (déclarations)

**Non trouvé**
- Appartenance de la France à l'Union : aucune déclaration explicite de 2026 du parti, du groupe ou du candidat (maintien dans l'Union, refus d'une sortie, révision des traités) n'a été trouvée. Cherché : les 69 publications de republicains.fr datées du 1er janvier au 23 septembre 2026 (liste relevée par l'interface publique du site), les mots « Frexit », « sortir de l'Europe », « sortie de l'Union européenne », « rester dans l'Union » associés au candidat, l'entretien au Monde du 30 septembre (connu par CNews seulement), la réunion du Parti populaire européen à Toulouse fin septembre (aucune page trouvée). Éléments indirects : [C-LR-77] ; [C-LR-74] (« pas du tout fédéraliste », « double membrane ») ; [C-LR-72] (Union à sortir de son « impuissance stratégique » par les États) ; [C-LR-68] (le RN aurait changé d'avis sur « la sortie de l'euro et de l'Europe ») ; [C-LR-70] (« l'Europe peut changer »). Un site d'information non identifié (paris-times.fr, 30 septembre 2026) prête au candidat un rejet de la primauté du droit français sur le droit européen, sans citation et contre la formulation rapportée par CNews : non retenu. Des agrégateurs (ElyséeScope, votons-2027.fr, monvote2027.fr, france-vote.fr) affirment que le projet n'implique pas de sortie de l'Union : vus en résultat de recherche seulement, non ouverts, non retenus.
- Mathieu Darnaud (président du groupe LR du Sénat, reconduit le 30 septembre 2026) : aucune déclaration de 2026 ouverte ; les articles de Public Sénat qui le citent sur le budget portent sur le budget 2026 (fin 2025).
- Porte-parole de la campagne : la page « Bruno Retailleau présente son équipe de porte-paroles » (8 septembre 2026, identifiant 59531) n'a pas de texte ; aucune déclaration de porte-parole recherchée au-delà.
- Groupe LR du Sénat sur l'immigration en 2026 (rétention, prestations) : rien trouvé ; les articles de Public Sénat retrouvés datent de 2023.
- Groupe DR sur l'Europe ou le Mercosur en 2026 : non recherché en séance ; la résolution européenne du groupe sur les Frères musulmans (22 janvier 2026, première séance, Éric Pauget) est au compte rendu, lue, non retenue (objet hors des six axes au sens strict, à reprendre si l'axe 5 la demande).
- Pages vidéo de republicains.fr sans texte, donc non retenues (positions inconnues sans visionnage) : 31 juillet (suspension de la libre circulation pour l'Espagne, 59455 ; le communiqué écrit du même jour a été trouvé ensuite : [C-LR-73]), 1er juin (« Les zones d'émeutes correspondent aux zones d'immigration importante », 59125), 8 juin (« Règlement retour : protéger les Français », 59136), 9 juin (« Mettre fin au corporatisme judiciaire », 59191), 6 septembre (« On est dans un gouvernement des juges », 59528), 15 septembre (« Ce que je veux faire pour le pouvoir d'achat », 59601), 1er juillet (« La prochaine catastrophe sera budgétaire », 59379), 8 juillet (« Je veux rendre la parole aux Français », 59405), 6 mai (« Mais qu'est-ce qu'ils font du pognon ? », 58890), 29 avril (lettre au président sur l'Algérie, 58832), et une vingtaine d'autres.
- Publications de republicains.fr après le 23 septembre 2026 : l'interface du site n'en liste aucune (dernière : 23 septembre) ; le plan d'économies du 12 octobre n'a pas de page d'actualité, mais ses fiches presse sont dans la médiathèque du site (PDF mis en ligne le 15 octobre, [C-LR-12]).
- Page du 2 septembre 2026 (« En France, la seule cour suprême, c'est le peuple », 59515) : texte présent, non retenu car il porte sur la réforme constitutionnelle présentée le 3 septembre (section a) ; à verser en section a si le sous-agent principal le juge utile.
- Page du 23 septembre 2026 (« Je veux sauver notre système de retraite », 59607) : vidéo, et objet couvert par l'annonce du 22 septembre (section a).

**Accès refusés ou partiels**
- France 24 (dépêche AFP du 4 octobre sur Laurent Wauquiez, source 72 de la note de contexte) : refus d'accès ; même dépêche lue sur Fortuneo [C-LR-78].
- Bourse Direct (même dépêche) : texte non extrait.
- Le JDD, Le Figaro, La Tribune Dimanche, Valeurs actuelles, Les Échos, Le Monde, Le Parisien (médias d'origine) : non ouverts ; positions lues sur le site du parti ou dans les relais.
- Public Sénat : texte lisible par téléchargement direct de la page ; l'extraction automatique du corps échoue, le texte a été relevé dans le code de la page.

**Relais uniques**
- [C-LR-78] (Fortuneo seul ouvert), [C-LR-75] (Public Sénat seul), [C-LR-77] (CNews seul), [C-LR-81] (La Gazette France seule, dépêche AFP aussi reprise par Le Petit Journal et Bourse Direct, non ouverts). [C-LR-60] : Brut, recoupé par Ma Commune (reprise AFP du 9 janvier 2026, ouverte) pour la date.


### Écarts apparents entre documents, à instruire aux étapes suivantes (listés, non qualifiés)

Définition du socle (`01-criteres.md` §6) : une divergence est deux positions incompatibles sur le même objet ; un silence, deux instruments pour un même but ou une précision successive n'en sont pas. Les lignes ci-dessous sont des rapprochements à vérifier, pas des divergences établies.

- **Délai d'accès des étrangers aux prestations non contributives** : cinq ans de séjour régulier et d'activité (livret « Famille » [C-LR-07] pour les dispositifs familiaux ; projet de Charte républicaine, article 12 [C-LR-14] ; fiche 9 du plan de 197 Md€, « après la révision constitutionnelle » [C-LR-12] ; candidat [C-LR-67], [C-LR-68]) contre deux ans (plan du groupe DR sur le PLF 2027, [C-LR-78]) et « durée minimale de résidence » sans chiffre (plan du groupe d'avril 2025 [C-LR-31]). À instruire : même objet (toutes prestations ou certaines), même horizon (à droit constant ou après révision constitutionnelle).
- **Montant et horizon du plan d'économies du candidat** : 150 Md€ ([C-LR-76], 12 septembre 2026) contre 197 Md€ en 2032 ([C-LR-12], 12 octobre 2026). Horizon du chiffre de septembre non précisé : peut-être une précision successive.
- **Départs non remplacés dans la fonction publique** : 125 000 départs non remplacés et 250 000 agents « mobilisés » (livret IA, juillet 2026 [C-LR-10]), « à peu près 250 000 postes » ([C-LR-71], 1er juillet 2026), 400 000 départs en retraite non remplacés sur le quinquennat (plan du 12 octobre [C-LR-12]) ; le groupe DR demande 50 000 suppressions de postes pour le seul budget 2027 ([C-LR-78]). Objets et horizons à aligner avant toute qualification.
- **Économies sur les retraites** : 40 Md€ « cumulés sur cinq ans » (annonce du 22 septembre 2026, relais franceinfo) contre 42 Md€ en 2032 (fiche 6 du plan [C-LR-12]) : unités possiblement différentes (cumul contre niveau annuel), à vérifier.
- **Libre circulation et Espagne** : suspension de la libre circulation des personnes avec l'Espagne demandée par communiqué ([C-LR-73], 31 juillet 2026) ; deux jours plus tard, l'entretien du 2 août ([C-LR-74]) demande un Conseil européen extraordinaire, la réservation de Schengen aux Européens et des visas territorialisés, sans redire la suspension. Possible précision successive.
- **Primauté du droit de l'Union** : le projet constitutionnel maintient la primauté du droit de l'Union sur la loi, avec deux limites [C-LR-13] ; l'entretien du 2 septembre parle d'un « bouclier constitutionnel » contre les interprétations des juridictions européennes [C-LR-15] ; Public Sénat le résume comme une primauté du droit français « dans certains cas » ; [C-LR-77] (relais CNews) : droit européen « au-dessus de nos lois mais en dessous de la Constitution ». Compatibles à première lecture ; à confronter au texte des deux projets à l'étape 2.
- **AME** : « transformée en aide d'urgence » (L. Wauquiez, [C-LR-78]), « réformer, et non supprimer » (N. Ray, [C-LR-80]), « réduite aux soins essentiels » (fiche 9 [C-LR-12]), « recentrée sur l'urgence » (plan d'avril 2025 [C-LR-31]) : formulations à comparer sur le même objet.
- **Statut du groupe en juillet 2024** : « opposition responsable » (PDF du 19 juillet 2024) puis soutien au Premier ministre issu de la droite (page actuelle) [C-LR-20] : précision successive liée au changement de gouvernement, listée pour mémoire.
- **Date de la délibération du BP sur le gouvernement Lecornu II** : 10 octobre (communiqué du 12 octobre) contre 11 octobre (page du BP, LCP) [C-LR-24] : écart de fait à vérifier, sans incidence de fond.
- **Date de la confirmation de candidature de Xavier Bertrand** : 26 août (LCP, page de liste) contre 27 août 2026 (LCP, article du jour) : écart de fait.
- **Deux versions du projet de Charte républicaine** (V310826 et V010926) [C-LR-14] : non comparées.

---

## Étiquettes proposées (à inscrire par l'agent principal dans `03-sources/etiquettes.md`)

- [Reporterre : quotidien en ligne consacré à l'écologie, relais] : héberge le PDF du pacte législatif de 2024 [C-LR-19] ; ligne éditoriale revendiquée sur l'écologie ; non inscrit.
- [L'Opinion : quotidien d'information politique et économique, ligne libérale revendiquée] : média d'origine de [C-LR-16], non ouvert ; cité au niveau 5 du socle sans étiquette au registre.
- [La Libre Belgique : quotidien belge généraliste, relais] : composition du gouvernement Bayrou (`00-perimetre.md`, source 17).
- [Fortuneo (bourse.fortuneo.fr) : banque en ligne, relais de dépêches AFP] : [C-LR-78] ; même nature que Boursorama et Bourse Direct, déjà inscrits (proposée par le second sous-agent).
- [La Tribune Dimanche : hebdomadaire d'information générale, pas d'étiquette] : média d'origine de [C-LR-67], non ouvert (proposée par le second sous-agent ; à inscrire seulement si une étape ultérieure le lit).
- Étiquettes existantes utilisées : source du parti, partie prenante ; source officielle, partie prenante ; LCP ; Public Sénat ; Acteurs publics ; Lyon Capitale, LyonMag ; La finance pour tous ; GISTI ; Le Figaro ; JDD ; CNews ; Valeurs actuelles ; Brut ; La Gazette France ; Ma Commune.

---

## Sources secondaires utilisées pour les statuts et le contexte

1. Assemblée nationale, jeu open data « Dossiers législatifs » (documents et dossiers parlementaires), XVIIe législature, téléchargé le 2026-10-27. https://data.assemblee-nationale.fr/static/openData/repository/17/loi/dossiers_legislatifs/Dossiers_Legislatifs.json.zip (413 textes déposés par un premier signataire DR, comptage par nos soins ; statuts des dossiers relevés dans les actes)
2. Assemblée nationale, jeux open data AMO10 et AMO30, XVIIe législature, téléchargés le 2026-10-27 (`00-perimetre.md`, source 1).
3. Les Républicains, interface publique du site (articles, pages, médiathèque de 71 PDF), interrogée le 2026-10-27. https://republicains.fr/wp-json/wp/v2/media?mime_type=application/pdf [source du parti, partie prenante]
4. Groupe Droite Républicaine, site du groupe (déclaration politique, présentation du président, liste des députés), consulté le 2026-10-27. https://www.deputesdroiterepublicaine.fr/ [source du parti, partie prenante]
5. LCP, « Travail, immigration, sécurité : pour leur niche parlementaire, les députés LR se concentrent... », 2025-02-03, mis à jour le 2025-03-03. https://lcp.fr/actualites/travail-immigration-securite-pour-leur-niche-parlementaire-les-deputes-lr-se-concentrent
6. LCP, « Voile des mineures, ordre public, travail : à l'occasion de leur niche parlementaire, les députés Droite républicaine... », 2026-01-12, mis à jour le 2026-01-14. https://lcp.fr/actualites/voile-des-mineures-ordre-public-travail-a-l-occasion-de-leur-niche-parlementaire-les
7. LCP, « Face à une France "quasiment en faillite", Bruno Retailleau présente un plan d'économies de 197 milliards », 2026-10-12. https://lcp.fr/actualites/face-a-une-france-quasiment-en-faillite-bruno-retailleau-presente-un-plan-d-economies-de
8. Public Sénat, « Présidentielle 2027 : Bruno Retailleau veut "renverser la table" avec une profonde réforme constitutionnelle », 2026-09-03. https://www.publicsenat.fr/actualites/politique/presidentielle-2027-bruno-retailleau-veut-renverser-la-table-avec-une-profonde-reforme-constitutionnelle
9. franceinfo (avec l'AFP), « S'il est élu, Bruno Retailleau veut instaurer un âge minimal de départ à la retraite à 63 ans, le taux plein à 65 ans », 2026-09-22. https://www.franceinfo.fr/politique/bruno-retailleau/s-il-est-elu-bruno-retailleau-veut-instaurer-un-age-minimal-de-depart-a-la-retraite-a-63-ans-le-taux-plein-a-65_8205254.html
10. LCP, « Face à "la situation catastrophique de nos finances publiques", Laurent Wauquiez présente un plan d'économies de 50 milliards », 2024-10-02. https://lcp.fr/actualites/face-a-la-situation-catastrophique-de-nos-finances-publiques-laurent-wauquiez-presente
11. Reporterre, « Droite et Macronie pourraient s'entendre sur un "pacte législatif" anti-écolo », 2024-07-24 (hébergeur du PDF du pacte). https://reporterre.net/Droite-et-Macronie-pourraient-s-entendre-sur-un-pacte-legislatif-anti-ecolo [étiquette proposée : quotidien en ligne consacré à l'écologie, relais]
12. La finance pour tous, « Élections législatives 2024 : propositions économiques des principaux partis ou coalitions », 2024-06-26. https://www.lafinancepourtous.com/2024/06/26/elections-legislatives-2024-propositions-economiques-des-principaux-partis-ou-coalitions/
13. Conseil constitutionnel, décision n° 2025-895 DC du 7 août 2025 ; décision n° 2025-881 DC du 7 mai 2025. https://www.conseil-constitutionnel.fr/decision/2025/2025895DC.htm ; https://www.conseil-constitutionnel.fr/decision/2025/2025881DC.htm
14. Sénat, proposition de loi n° 298 (2024-2025) ; rapport n° 611 (2025-2026). https://www.senat.fr/leg/ppl24-298.html ; https://www.senat.fr/rap/l25-611/l25-611_mono.html
15. Wayback Machine, capture de https://republicains.fr/ du 2024-06-25. https://web.archive.org/web/20240625085224/https://republicains.fr/
16. Sources propres à la section f : liste des publications de republicains.fr du 1er janvier au 23 septembre 2026 (https://republicains.fr/wp-json/wp/v2/posts?after=2026-01-01T00:00:00&per_page=100) ; Ma Commune (AFP), « Mercosur : face au risque politique, Emmanuel Macron choisit de dire non malgré des concessions "incontestables" », 2026-01-09, https://www.macommune.info/mercosur-face-au-risque-politique-emmanuel-macron-choisit-de-dire-non-malgre-des-concessions-incontestables/ [presse locale en ligne, relais de dépêches AFP] ; Les Républicains, « Nomination de nos secrétaires nationaux », 2026-01-16, https://republicains.fr/actualites/2026/01/16/nomination-de-nos-secretaires-nationaux/ [source du parti, partie prenante]
