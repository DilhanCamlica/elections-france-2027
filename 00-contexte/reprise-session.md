# Reprise de session : état au 2026-10-26, après le premier challenge de l'article RN

Ce fichier est le point d'entrée d'une session qui reprend le travail après un compactage ou un redémarrage. Il complète `CLAUDE.md` (règles) et `README.md` (structure) par ce qu'aucun fichier ne dit : où on en est exactement, ce qui est décidé mais pas encore fait, les pièges rencontrés. Il est réécrit à chaque fin de session.

## Ordre de lecture pour reprendre

1. `CLAUDE.md`, puis `README.md`.
2. Ce fichier.
3. `01-socle/01-criteres.md` (v2) et `01-socle/04-format-artifacts.md` (v2) en entier ; `01-socle/CHANGELOG.md` pour l'historique des décisions.
4. Pour produire la page RN : `02-partis/rn/article-long.md` (avec les corrections de Dilhan quand il l'aura challengé), `02-partis/rn/revue/arbitrage.md` (grille finale et règles appliquées), les six fiches `02-partis/rn/axes/*.md` (verdicts, « Ce qui tient », matrices de votes, tableaux Q5 complets), `methode.md`, `tendances.md`, `hors-grille.md`, `votes/scrutins.md` (divergences UDR).
5. Le gabarit HTML : `05-artifacts/renaissance.html` (v1.1), à reprendre tel quel pour le CSS et la structure ; les URL des pages « Immigration : vrai ou faux ? » et « Qui paie pour qui ? » sont dans `05-artifacts/README.md`.

## État exact

- **Socle : v2.1** depuis le 2026-10-26 : l'échelle C est pondérée par la mesure structurante de l'axe (décision de Dilhan au challenge de l'article RN, `01-socle/CHANGELOG.md`). Appliquée au RN ; Renaissance à relire à la boucle de révision. Les retours de la verticale RN pour la boucle de révision sont dans `02-partis/rn/revue/retours-socle.md` (9 lignes) : aucun n'a encore été appliqué aux fiches Renaissance.
- **Verticale 1, Renaissance : étape 8 faite**, page publiée et partagée (v1.1), URL dans `05-artifacts/README.md`. Dilhan n'a pas fini sa relecture de la page ; ses retours restent attendus.
- **Verticale 2, RN : étapes 1 à 7 faites en v2 le 2026-10-25 et le 2026-10-26.** Corpus (45 archives, `01-corpus.md`, 83 identifiants C-RN), six fiches extraites puis contrôlées (54 corrections), étapes 3 à 5 et Q5 par six agents, chapitre Méthode, carte des tendances, revue contradictoire (défense, contradiction), arbitrage appliqué, article long écrit par l'agent principal et **soumis à Dilhan le 2026-10-26**. Grille finale :

| Axe | D | F | C | E |
|---|---|---|---|---|
| 1 Finances publiques et dette | 4 Plutôt fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 2 Travail, protection sociale, fraude | 3 Partiellement fondé | 3 Conditionnelle | 4 Plutôt cohérent | 3 Répond en partie |
| 3 Immigration | 3 Partiellement fondé | 2 Très incertaine | 2 Écart important (pondération v2.1) | 3 Répond en partie |
| 4 Pouvoir d'achat et fiscalité | 4 Plutôt fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 5 Sécurité, ordre public, libertés | 3 Partiellement fondé | 3 Conditionnelle | 4 Plutôt cohérent | 4 Répond |
| 6 Institutions, démocratie, Europe | 4 Plutôt fondé | 2 Très incertaine | 4 Plutôt cohérent | 3 Répond en partie |
| Méthode (M) | 3 Écart partiel (parole et comportement parlementaire seulement, pas d'actes de gouvernement) | | | |
| Carte des tendances | 5 traitées, 9 en partie, 0 nommée, 0 absente | | | |

- **Challenge en cours** : premier retour de Dilhan traité le 2026-10-26 (six affirmations vérifiées, pondération C adoptée) ; question suivante posée à Dilhan : une septième question « pour qui » (public revendiqué contre bénéficiaires des mesures chiffrées). **Prochaine étape : la suite du challenge, puis la page RN (étape 8)** selon la marche à suivre ci-dessous. Titre prévu au socle : « Le RN : ce qu'il propose, ce qu'il vote ». La page doit lister les 47 demandes avec intensité et statut (règle « l'inventaire entier, pas un extrait ») : les tableaux Q5 des fiches 1, 2, 4, 5, 6 ont le statut en deuxième colonne ; **la fiche 3 a un tableau à colonnes différentes (mesure puis statut dans le texte)** : lire le verdict E et le tableau ensemble pour fixer les six statuts.
- Git : repo local `~/Documents/Politique/elections-france-2027`, branche `main`, environ 45 commits, **rien n'est poussé, aucun remote**. Publication GitHub : décidée « après la première verticale relue, sur feu vert explicite de Dilhan » ; pas encore demandée.

## Marche à suivre pour une page (étape 8, suivie pour Renaissance ; à reprendre pour le RN)

1. Lire `01-socle/04-format-artifacts.md` v2 : titre, surtitre « Lecture · programme et votes 2022-2026 », grille 6 × 4 (24 pastilles) plus une ligne « Comment ils gouvernent » et la carte des tendances en tuiles, six chapitres courts (3 à 4 lignes par question, un panneau visuel maximum, encadré « Ce qui tient », bloc « Creuser » avec la matrice de votes et **toutes les demandes de l'axe** avec intensité et statut), chapitre « Comment ils gouvernent », « Hors grille », « Ce qu'il faut retenir » (quatre points, pas de note globale), sources par axe étiquetées, note de méthode avec dates de gel.
2. Repartir de `05-artifacts/renaissance.html` : garder le CSS et les composants (`.grid`, `.pill`, `.mline`, `.tend`, `.qb`, `.panel`, `.votes`, `.true`, `details.dig`, `ul.dem` avec `.st` et `.ti`), remplacer le contenu. Charger les skills `artifact-design` puis `dataviz` avant d'écrire (règle de l'outil Artifact).
3. Matrices de votes : scrutins de l'axe en lignes, cinq groupes en colonnes (LFI, SOC, EPR, DR, RN), positions dans `03-sources/scrutins-positions.md` ; le 4758 en complément pondéré à part aux axes 1, 2 et 4 ; pour le RN, une ligne ou une note sur les divergences de l'UDR (217, 468, 3684, 881, 3182) depuis `02-partis/rn/votes/scrutins.md`.
4. Les 24 + 1 verdicts et leurs phrases de conclusion sont dans les fiches (`**Verdict …**`) ; les « Ce qui tient » sont à reprendre condensés ; la note de méthode dit que le RN n'a pas d'actes de gouvernement à confronter et que son verdict M ne se compare pas à celui de Renaissance (registre des biais, lignes 2 et 14).
5. Écrire `05-artifacts/rn.html`, contrôler : `python3 _scripts/verifie-page.py 05-artifacts/rn.html` puis `_scripts/lint-texte.py`. Publier d'abord en privé (icône « ballot », description d'une phrase), vérifier à 390 px en clair et en sombre dans le navigateur intégré sur la page publiée (il ne lit ni `file://` ni un serveur local ; le contenu est dans un iframe : défilement et clics par coordonnées), corriger en une passe, republier.
6. Inscrire l'URL dans `05-artifacts/README.md` et `README.md`, dire à Dilhan que la page est privée, commiter `🖼️ artifact: rn v1`.
7. Note de méthode de la page : périmètre (RN seul, groupe RN, candidate Marine Le Pen, UDR cité quand il diverge), corpus arrêté au 2026-10-25, 23 scrutins gelés plus 4758, inventaire des demandes et liste des tendances gelés le 2026-10-25, pas de programme 2027 publié, réforme des retraites du 17 novembre 2026 hors corpus.

## Décisions prises, non dérivables des fichiers de contenu

- Sous-agents : Opus pour recherche, vérification, revue ; Sonnet pour extraction mécanique, scripts, carte des tendances. L'agent principal seul sur Fable. Toujours passer `model` explicitement. Les lancer par vagues (trois axes à la fois) pour garder la relecture digeste, chaque rapport limité à 15 ou 25 lignes.
- Les sous-agents ne commitent pas ; l'agent principal commite par étape (`CLAUDE.md`).
- Grill-me (une question à la fois, recommandation à chaque fois) dès qu'un choix de forme, de compréhension ou d'expérience de lecture se présente ; sinon on fait, on ne demande pas.
- Ordre des verticales : Renaissance, RN, LFI, PS, LR. Date d'arrêt du corpus : fixée au début de chaque verticale (Renaissance et RN : 2026-10-25), réalignée à la fin des cinq.
- Règles d'arbitrage appliquées aux deux verticales et à reprendre pour les suivantes (`02-partis/rn/revue/arbitrage.md`, « Règles appliquées ») : une source de niveau 4 ne décide jamais seule d'un cran ; en C, un décalage documenté sur un objet vaut cran 3 même expliqué, le cran 4 est réservé aux nuances ; un énoncé non vérifiable n'est pas faux ; un même refus se lit de la même façon sur deux axes ; un relais de presse unique ne déplace pas un cran ; mesures de 2024 vivantes en Q5, mesures de 2022 non reprises insuffisantes ; carte : « traitée » exige le cœur de la tendance et une pièce de 2024 ou plus récente.

## En suspens (à exécuter quand c'est possible)

- **Challenge de l'article RN par Dilhan**, puis page RN.
- **Boucle de révision après le RN** : les 8 lignes de `02-partis/rn/revue/retours-socle.md` (lecture de §6 pour les divergences Renaissance ; scrutin 3213 ; Cevipof dans les motifs D ; règle du niveau 4 en F ; transparence du chiffrage ; lecture de l'échelle C ; plafond de 64 ans d'Orléans), plus les retours Renaissance déjà traités. Chaque modification du socle passe par `01-socle/CHANGELOG.md`.
- **17 novembre 2026** : réforme des retraites du RN ; réexaminer F et C de l'axe 2 et la divergence de corpus sur l'âge.
- **Scrutin Smic** : PPL LFI n° 3176 en niche le 29 octobre 2026 ; si un scrutin a lieu, il remplace le 881 dans la liste gelée et les matrices de l'axe 4 des deux verticales sont à refaire.
- **Publication GitHub** du repo : à demander à Dilhan.
- **Programme 2017** de Renaissance : à archiver dans `02-partis/renaissance/corpus/`.
- Pour la synthèse : les scrutins de la XVIe législature (3213, 1662, 909, 831) sont cités en contexte dans les fiches RN ; décider d'un traitement commun aux cinq forces.

## Pièges rencontrés

- Accès refusés (403) : Légifrance, résultats électoraux du ministère de l'Intérieur, pages DGEF, Interstats, EUR-Lex (arrêts de la CJUE et directives lus par relais), NORMLEX, JDD, CNews, Europe 1 ; Mediapart payant. Contournements dans `01-socle/03-sources-et-hierarchie.md` §6.
- Le champ « position majoritaire » de l'open data de l'Assemblée est faux une fois sur deux : recalcul par la règle des 60 % (`03-sources/scrutins-positions.md`). Le script `_scripts/votes-parti.py` produit `votes/scrutins.md` pour un groupe et ses alliés hors périmètre.
- Les agents d'extraction inventent des « divergences » qui n'en sont pas ; les agents de vérification lisent parfois des résumés de moteur de recherche au lieu d'ouvrir les pages : exiger « page ouverte ou le dire », et un chiffreur de chaque bord ou le dire.
- Les sous-agents de vérification classent facilement au cran 2 en F sur un seul think tank : rappeler la règle du niveau 4.
- Deux rédacteurs sur un même fichier : jamais en parallèle. Un sous-agent qui ajoute une fiche au corpus peut réutiliser un identifiant déjà pris (doublon C-RN-82 corrigé en C-RN-83) : vérifier le dernier identifiant avant d'ajouter.
- Les documents de plus de 20 Mo (programmes RN 2024 et 2022) ne sont pas versionnés : copie texte plus somme de contrôle.
- La carte des tendances tend au « tout traité » ; la revue l'a ramenée de 6 à 5 traitées.

## Contexte familial d'origine

`00-contexte/echange-famille-2026-10-25.md`. Les pages déjà partagées à la famille sont les trois artifacts cités dans `05-artifacts/README.md`.
