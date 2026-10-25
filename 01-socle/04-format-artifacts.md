# Format des pages (artifacts)

- Rédigé le : 2026-10-25
- Statut : brouillon v0, à valider au grill. Hérite du format validé de la série « Vérification d'affirmations » (voir `00-contexte/briefing-serie-verification.md`, section 5) et l'adapte à un objet différent : un parti, pas une affirmation.

## 1. Ce qui ne change pas

- Système visuel : Newsreader (titres), Public Sans (texte), IBM Plex Mono (chiffres). Palette en tokens CSS, thème clair et sombre. Mêmes cinq couleurs de verdict (rouge, orange, ocre, vert, vert foncé). Graphiques en HTML/CSS ou SVG inline, pas d'image externe, pas de librairie.
- Mobile d'abord, vérifié à 390 px en clair et en sombre.
- Ton : lecteur respecté, pas de coaching, pas de bouton de copie, pas de « réponse en 30 secondes ». Le lecteur qui soutient ce parti doit voir ce qui tient dans sa position. Le lecteur qui le combat doit voir ce qui tient aussi.
- Conclusion d'abord, détail replié (« Creuser les données »).
- Sources numérotées en pied de page, étiquetées, note de méthode, date d'arrêt des données.
- Contrôle avant publication : balises, références, ancres, tirets longs, capture 390 px.

## 2. Structure proposée d'une page « parti »

1. **En-tête** : surtitre « Lecture · programme et votes 2022-2026 », titre « <Parti> : que proposent-ils vraiment ? » (forme à trancher), sous-titre d'une phrase qui rappelle la règle du jeu (quatre questions, six axes, mêmes critères pour les cinq forces, lien vers la page de méthode ou vers la synthèse).
2. **La promesse dans leurs mots** : trois à cinq phrases courtes tirées du programme ou du candidat, entre guillemets, sourcées. Pas de commentaire. C'est l'équivalent de « l'affirmation citée » des pages précédentes : on part de ce qu'ils disent.
3. **Illustration SVG** : un motif propre à la série « lecture » (à définir ; proposition : une grille six lignes, trois colonnes, qui se remplit des couleurs de verdict, visible d'un coup d'œil).
4. **La grille en un regard** : tableau six axes × trois verdicts (Diagnostic, Faisabilité, Cohérence), chaque case une pastille colorée avec le libellé, chaque ligne un lien vers le chapitre.
5. **Un chapitre par axe** (six) :
   - pastille hexagonale numérotée, nom de l'axe, titre-conclusion ;
   - « Ce qu'ils constatent » : le diagnostic du parti en une ou deux phrases dans ses mots, puis la pastille Verdict Diagnostic et un paragraphe avec deux ou trois chiffres clés ;
   - « Ce qu'ils proposent » : les mesures principales, chiffrage du parti ;
   - « Est-ce faisable ? » : pastille Verdict Faisabilité, paragraphe, un panneau visuel si pertinent (chiffrage du parti contre chiffrages indépendants sur un axe, par exemple) ;
   - « Disent-ils ce qu'ils votent ? » : pastille Verdict Cohérence, matrice de votes (scrutins en lignes, position du groupe en colonnes) ;
   - encadré vert « Ce qui tient » (obligatoire) ;
   - bloc repliable « Creuser les données ».
6. **Hors grille** : trois lignes qui listent les thèmes majeurs du programme non traités (écologie, santé, école, Europe, défense), pour l'honnêteté du périmètre.
7. **Encadré final sombre « Ce qu'il faut retenir »** : quatre points maximum, sans note globale.
8. **Sources** groupées par axe, étiquetées, puis note de méthode (périmètre retenu, corpus et date d'arrêt, scrutins retenus et règle de sélection, lien vers le repo si Dilhan le rend public).

## 3. Page de synthèse (à la fin)

- Titre « Cinq programmes côte à côte » (à trancher).
- Une matrice interactive cinq forces × six axes, chaque case montrant les trois pastilles (D, F, C) et, au toucher, la phrase de conclusion.
- Une section « Ce qu'ils proposent en commun » par axe, avec les convergences relevées.
- Une section « Les problèmes que personne ne traite » si la vérification des diagnostics a montré des enjeux lourds absents des programmes (exemple possible : l'emploi des 55-64 ans, identifié par la page A).
- Pas de classement, pas de note.

## 4. Page d'accueil de la série (option)

Si la série atteint huit pages, une page d'accueil qui liste les vérifications et les lectures, avec leurs verdicts en miniature. À décider plus tard.

## 5. Points à trancher au grill

- Le titre type des pages parti (question ou affirmation ?).
- Afficher la grille complète en haut (dix-huit pastilles) ou seulement un verdict par axe ?
- La matrice de votes : scrutin par scrutin avec le détail des cinq groupes (le lecteur voit les autres partis dès la page de ce parti) ou seulement le groupe étudié ?
- Longueur cible d'une page parti : les pages de vérification font 50 à 60 Ko de HTML et se lisent en 10 à 15 minutes. Six axes risquent de doubler. Accepter des pages plus longues, ou réduire les panneaux visuels à un par axe ?
