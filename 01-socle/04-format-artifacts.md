# Format des pages (artifacts)

- Rédigé le : 2026-10-25
- Statut : v1, validé avec Dilhan au grill du 2026-10-25. Hérite du format validé de la série « Vérification d'affirmations » (voir `00-contexte/briefing-serie-verification.md`, section 5) et l'adapte à un objet différent : un parti, pas une affirmation.

## 1. Ce qui ne change pas par rapport à la série

- Système visuel : Newsreader (titres), Public Sans (texte), IBM Plex Mono (chiffres). Palette en tokens CSS, thème clair et sombre. Mêmes cinq couleurs de verdict (rouge, orange, ocre, vert, vert foncé). Graphiques en HTML/CSS ou SVG inline, pas d'image externe, pas de librairie.
- Mobile d'abord, vérifié à 390 px en clair et en sombre, sans défilement horizontal.
- Ton : lecteur respecté, pas de coaching, pas de bouton de copie, pas de « réponse en 30 secondes ». Le lecteur qui soutient ce parti doit voir ce qui tient dans sa position. Le lecteur qui le combat doit le voir aussi.
- Conclusion d'abord, détail replié (« Creuser les données »).
- Sources numérotées en pied de page, étiquetées, note de méthode, date d'arrêt des données.
- Contrôle avant publication : balises, références, ancres, tirets longs, capture 390 px.

## 2. Structure d'une page « parti »

**Titre** : « Le RN : ce qu'il propose, ce qu'il vote » (patron identique pour les cinq : « Renaissance : ce qu'elle propose, ce qu'elle vote », « LFI : ce qu'elle propose, ce qu'elle vote », « Le PS : ce qu'il propose, ce qu'il vote », « LR : ce qu'ils proposent, ce qu'ils votent »). Descriptif, sans jugement, il annonce la mécanique de la page.
**Surtitre** : « Lecture · programme et votes 2022-2026 », pour distinguer de la série « Vérification ».

1. **En-tête** : surtitre, titre, une phrase qui rappelle la règle du jeu (six axes, trois verdicts, mêmes critères et mêmes scrutins pour les cinq forces, lien vers la méthode).
2. **La promesse dans leurs mots** : trois à cinq phrases courtes tirées du programme ou du chef de parti, entre guillemets (15 mots maximum chacune), sourcées. Pas de commentaire. Équivalent de « l'affirmation citée » : on part de ce qu'ils disent.
3. **Illustration SVG** : motif de la série « lecture », à définir à la première page (proposition : une grille six lignes × trois colonnes qui se remplit des couleurs de verdict).
4. **La grille en un regard** : tableau six axes × trois verdicts (Diagnostic, Faisabilité, Cohérence), **dix-huit pastilles** colorées avec libellé court, une ligne par axe, chaque ligne lien vers son chapitre. Testé à 390 px : trois colonnes étroites, libellés sur deux lignes si besoin. C'est le produit : en dix secondes, le lecteur voit qu'un diagnostic peut être juste et la mesure infaisable, ou l'inverse.
5. **Six chapitres, un par axe, courts.** Cible : page dépliée lisible en 12 à 15 minutes. Par chapitre :
   - pastille hexagonale numérotée, nom de l'axe, titre-conclusion ;
   - **Ce qu'ils constatent** : le diagnostic du parti en une ou deux phrases dans ses mots, pastille Verdict Diagnostic, un paragraphe de 3 à 4 lignes avec deux ou trois chiffres clés sourcés ;
   - **Ce qu'ils proposent** : les mesures principales et le chiffrage du parti, 3 à 4 lignes ;
   - **Est-ce faisable ?** : pastille Verdict Faisabilité, 3 à 4 lignes ;
   - **Disent-ils ce qu'ils votent ?** : pastille Verdict Cohérence, 3 à 4 lignes ;
   - **un panneau visuel maximum** par chapitre : en priorité la **matrice de votes** (scrutins en lignes, **les cinq groupes en colonnes**, pour / contre / abstention / non votant), sinon un graphique de chiffrage (parti contre estimations indépendantes) ;
   - encadré vert **« Ce qui tient »** (obligatoire) ;
   - bloc repliable **« Creuser les données »** : tableaux détaillés, nuances juridiques, chiffrages concurrents étiquetés, amendements, divergences parti/candidat.
6. **Hors grille** : trois lignes qui listent les grands thèmes du programme non traités (écologie et énergie, santé, école, défense, etc.).
7. **Encadré final sombre « Ce qu'il faut retenir »** : quatre points maximum, sans note globale.
8. **Sources** groupées par axe, étiquetées, puis note de méthode : périmètre retenu, corpus et date d'arrêt, scrutins retenus et règle de sélection, lien vers le repo public une fois publié.

Pourquoi les cinq groupes dans la matrice : le lecteur voit tout de suite si « tout le monde a voté pareil » ou si ce parti est seul ; ça empêche de faire passer pour un travers propre à un parti ce qui est général ; et ça construit la synthèse au fil de l'eau, puisque les scrutins sont les mêmes pour les cinq pages.

## 3. Page de synthèse (à la fin)

- Titre proposé : « Cinq programmes côte à côte » (à confirmer au moment venu).
- Une matrice cinq forces × six axes, chaque case montrant les trois pastilles (D, F, C) et, au toucher, la phrase de conclusion.
- Une section « Ce qu'ils proposent en commun » par axe, avec les convergences relevées.
- Une section « Les problèmes que personne ne traite » si la vérification des diagnostics a montré des enjeux lourds absents des programmes (exemple possible : l'emploi des 55-64 ans, identifié par la page A).
- Pas de classement, pas de note.

## 4. Page d'accueil de la série (option)

Si la série atteint huit pages, une page d'accueil qui liste les vérifications et les lectures, avec leurs verdicts en miniature. À décider plus tard.

## 5. Publication

Une nouvelle page est privée tant que Dilhan ne l'a pas partagée. Le code HTML de chaque page publiée est archivé dans `05-artifacts/<slug>.html` et son URL inscrite dans `05-artifacts/README.md` et dans `README.md`. Une page mise à jour garde la même URL.
