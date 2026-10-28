# Format des pages (artifacts)

- Rédigé le : 2026-10-25
- Statut : **v2**, validée au second grill du 2026-10-25 (grille 6 × 4 plus une ligne Méthode et une carte des tendances). Hérite du format validé de la série « Vérification d'affirmations » (voir `00-contexte/briefing-serie-verification.md`, section 5).

## 1. Ce qui ne change pas par rapport à la série

- Système visuel : Newsreader (titres), Public Sans (texte), IBM Plex Mono (chiffres). Palette en tokens CSS, thème clair et sombre. Mêmes cinq couleurs de verdict (rouge, orange, ocre, vert, vert foncé). Graphiques en HTML/CSS ou SVG inline, pas d'image externe, pas de librairie.
- Mobile d'abord, vérifié à 390 px en clair et en sombre, sans défilement horizontal.
- Ton : lecteur respecté, pas de coaching, pas de bouton de copie. Le lecteur qui soutient ce parti doit voir ce qui tient dans sa position ; celui qui le combat aussi.
- Conclusion d'abord, détail replié (« Creuser les données »).
- Sources numérotées, étiquetées, note de méthode, date d'arrêt.
- Contrôle avant publication : balises, références, ancres, tirets longs, capture 390 px.

## 2. Structure d'une page « parti » (v2)

**Titre** : « Le RN : ce qu'il propose, ce qu'il vote » (patron identique pour les cinq). **Surtitre** : « Lecture · programme et votes 2022-2026 ».

1. **En-tête** : surtitre, titre, une phrase de règle du jeu (six axes, quatre verdicts par axe, un verdict de méthode, mêmes critères et mêmes scrutins pour les cinq forces, lien vers la méthode).
2. **La promesse dans leurs mots** : trois à cinq phrases courtes du programme ou du candidat, entre guillemets (15 mots maximum), sourcées.
3. **Illustration SVG** : motif de la série « lecture », défini à la première page.
4. **La grille en un regard** : six lignes (axes) × **quatre colonnes** : « Le problème est-il réel ? », « Est-ce faisable ? », « Votent-ils ce qu'ils disent ? », « Répondent-ils aux demandes ? ». Vingt-quatre pastilles colorées avec libellé court. Sous la grille, **une ligne à part « Comment ils gouvernent »** avec son verdict unique (échelle M), et **la carte des tendances lourdes** : une tuile par tendance en trois couleurs (traite, nomme sans mesure, absent). Testé à 390 px : quatre colonnes étroites, libellés sur deux lignes si besoin. **Ajout v2.3 (2026-10-28) : la base du verdict C est visible dans la grille.** Chaque pastille de la colonne « Votent-ils ce qu'ils disent ? » porte sous son libellé une ligne en petites capitales mono : « votes seuls » pour une force qui n'a pas gouverné depuis 2012, « votes + actes 2024-2025 » (LR), « votes + actes 2017-2026 » (Renaissance), « votes + actes 2012-2017 » (PS) pour les autres. Les pastilles « votes seuls » ont un contour en pointillé et une couleur de fond atténuée (même teinte, saturation réduite), pour que la colonne se lise comme deux familles de verdicts, pas une seule. Sous la grille, une **légende d'une phrase**, toujours présente : « La colonne "Votent-ils ce qu'ils disent ?" compare la parole aux votes pour les cinq forces et, pour celles qui ont gouverné depuis 2012, à leurs actes. Une force qui n'a pas gouverné n'est pas plus cohérente : elle est moins testée. » Un bouton « Pourquoi ? » déplie trois lignes : ce qu'un acte fait au verdict (règle v2.3), quelles forces ont des actes, et le renvoi à la note de méthode. Testé à 390 px : la ligne de base tient sur une ligne ou passe en abrégé (« votes », « votes + actes »).
5. **Six chapitres, un par axe, courts** (12 à 15 minutes de lecture pour la page dépliée). Par chapitre :
   - pastille hexagonale, nom de l'axe, titre-conclusion ;
   - **Ce qu'ils constatent** : pastille D, 3 à 4 lignes ;
   - **Ce qu'ils proposent** : 3 à 4 lignes ; au chapitre 6, une phrase explicite et sourcée sur l'appartenance à l'Union européenne (sortie, maintien, renégociation des traités, désobéissance, intégration), qui dit ce que le programme propose et ce qu'il ne propose pas (ajout du 2026-10-27 : la question est posée au lecteur pour chaque force, le silence de la page laissait l'idée reçue intacte) ;
   - **Est-ce faisable ?** : pastille F, 3 à 4 lignes, effets distributifs en une phrase quand ils sont connus ;
   - **Disent-ils ce qu'ils votent ?** : pastille C, 3 à 4 lignes ; **ajout v2.3** : à côté de la puce de verdict, une seconde puce neutre (gris, contour) donne la base : « Votes seuls » ou « Votes + actes <période> » ; pour une force sans actes, la première phrase du paragraphe le dit (« Aucun acte de gouvernement à confronter : ce verdict ne porte que sur les votes et les textes du groupe ») ; pour une force avec actes, quand la règle v2.3 a joué, le paragraphe nomme l'acte, le poste, la promesse maintenue et la contrainte du moment en une phrase chacune ;
   - **Répondent-ils aux demandes ?** : pastille E, 3 à 4 lignes : les demandes larges de l'axe (inventaire gelé), ce que le programme en fait, et s'il assume ce qu'il écarte ;
   - **un panneau visuel maximum** : la matrice de votes (scrutins en lignes, cinq groupes en colonnes) ou un graphique de chiffrage ;
   - encadré vert **« Ce qui tient »** ;
   - bloc repliable **« Creuser les données »**.
6. **Chapitre « Comment ils gouvernent »** (nouveau) : pastille M, titre-conclusion, 3 blocs courts (la parole de méthode du programme ; les actes de méthode depuis 2012 avec leur date, pondérés par l'ancienneté ; le comportement parlementaire), un panneau visuel (par exemple une frise des consultations promises et de leurs suites, ou le nombre de 49.3 par législature rapporté à la situation de majorité), encadré « Ce qui tient », bloc « Creuser ». Pour une force sans passé gouvernemental, le chapitre le dit en première ligne. **Ajout v2.2** : un quatrième bloc court « Valeurs affichées et discipline interne » (ce que le parti dit de ses valeurs, combien de cas publics documentés sur la fenêtre, combien avec réaction du parti et en quel délai, avec les mêmes colonnes pour les cinq forces), sans pastille à part. **Effets distributifs** (décision du 2026-10-26, question « pour qui » écartée) : ils restent décrits sans verdict, mais chaque chapitre d'axe qui en a (axes 1, 2, 4) les montre dans son panneau « Creuser » sous le titre « Qui gagne, qui perd », par décile ou par catégorie, avec la source.
7. **Chapitre « Ce qui vient »** (nouveau, court) : la carte des tendances lourdes commentée en une phrase par tendance « absente » ; pas de verdict.
8. **Hors grille** : trois lignes.
9. **Encadré final « Ce qu'il faut retenir »** : quatre points maximum, sans note globale. **Ajout v2.3** : quand la force n'a pas gouverné, l'un des quatre points est réservé à la base du verdict C (« Ses verdicts de cohérence ne portent que sur ses votes : l'exercice du pouvoir ne les a pas testés ») ; quand elle a gouverné et qu'un acte a fait jouer la règle v2.3, un point le dit avec l'acte et la promesse.
10. **Sources** par axe, puis note de méthode (périmètre, corpus, scrutins, inventaire des demandes et liste des tendances avec leur date de gel, lien vers le repo public une fois publié).

## 3. Page de synthèse (à la fin)

- Matrice cinq forces × six axes, chaque case avec les quatre pastilles (D, F, C, E) ; une ligne « Comment ils gouvernent » (M) pour les cinq ; la carte des tendances pour les cinq côte à côte.
- « Ce qu'ils proposent en commun » par axe ; « Les demandes que personne ne traite » (inventaire contre les cinq programmes) ; « Les problèmes que personne ne regarde » (tendances absentes des cinq).
- **Ajout v2.3** : la ligne C de la matrice est séparée visuellement en deux familles par la même marque que sur les pages (pointillé et fond atténué pour « votes seuls », ligne de base sous chaque pastille) ; un encadré « Lire la colonne cohérence » dit que les verdicts ne se comparent qu'au sein d'une même famille et donne le compte des crans 2 par famille ; aucun total, aucune moyenne.
- Pas de classement, pas de note.

## 4. Publication

Une nouvelle page est privée tant que Dilhan ne l'a pas partagée. Le HTML est archivé dans `05-artifacts/`, l'URL dans `05-artifacts/README.md` et `README.md`. Une page mise à jour garde la même URL.
