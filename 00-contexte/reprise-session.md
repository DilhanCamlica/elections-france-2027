# Reprise de session : état au 2026-10-26, page RN publiée en privé, boucle de révision Renaissance faite (page v1.2 republiée)

Ce fichier est le point d'entrée d'une session qui reprend le travail après un compactage ou un redémarrage. Il complète `CLAUDE.md` (règles) et `README.md` (structure) par ce qu'aucun fichier ne dit : où on en est exactement, ce qui est décidé mais pas encore fait, les pièges rencontrés. Il est réécrit à chaque fin de session.

## Ordre de lecture pour reprendre

1. `CLAUDE.md`, puis `README.md`.
2. Ce fichier.
3. `01-socle/01-criteres.md` (v2) et `01-socle/04-format-artifacts.md` (v2) en entier ; `01-socle/CHANGELOG.md` pour l'historique des décisions.
4. Pour produire la page RN : `02-partis/rn/article-long.md` (avec les corrections de Dilhan quand il l'aura challengé), `02-partis/rn/revue/arbitrage.md` (grille finale et règles appliquées), les six fiches `02-partis/rn/axes/*.md` (verdicts, « Ce qui tient », matrices de votes, tableaux Q5 complets), `methode.md`, `tendances.md`, `hors-grille.md`, `votes/scrutins.md` (divergences UDR).
5. Le gabarit HTML : `05-artifacts/renaissance.html` (v1.1), à reprendre tel quel pour le CSS et la structure ; les URL des pages « Immigration : vrai ou faux ? » et « Qui paie pour qui ? » sont dans `05-artifacts/README.md`.

## État exact

- **Socle : v2.2** depuis le 2026-10-26 : l'échelle C est pondérée par la mesure structurante de l'axe (v2.1) et la question Méthode a un bloc (d) « valeurs affichées et discipline interne » pour les cinq forces (v2.2), tous deux décidés par Dilhan au challenge de l'article RN (`01-socle/CHANGELOG.md`). La question « pour qui » (bénéficiaires des mesures) a été écartée ; les effets distributifs restent décrits et la page les montre sous « Qui gagne, qui perd » (axes 1, 2, 4). Appliqués au RN et à Renaissance (boucle de révision du 2026-10-26 : `02-partis/rn/revue/retours-socle.md`, lignes 1, 4, 5, 6, 7, 9, 10 faites ; 3 et 8 en suspens). Précisions du même jour au socle : échelle F (le niveau 4 ne décide pas du cran), échelle C (l'explication publique distingue les crans 1 et 2, pas 3 et 4 ; un vote global expliqué ne fait pas un objet), bloc (d) (texte statutaire = principe ; périmètre matériel de la loi de 1881 ; acte public du parti = cas admis), registre ligne 18, Unédic au niveau 2.
- **Verticale 1, Renaissance : étape 8 faite et boucle de révision faite (2026-10-26)**, page v1.2 republiée à la même URL (partagée) : https://claude.ai/artifact/DvTLMrSY4DesQbiNN1NkW2. Grille après la boucle : D 4/3/4/4/3/4, F 3/3/3/2/**2**/2, C 2/3/3/2/3/**2**, E 3/3/3/3/4/3, M 2, carte 8/6/0/0. **Deux crans déplacés, confirmés par Dilhan le 2026-10-26** (`02-partis/renaissance/revue/arbitrage-v3.md`) : F axe 5 de 3 à 2 (le verdict suit la mesure structurante, la fin de l'excuse de minorité, qui exige une révision constitutionnelle ; même règle que l'axe 3 du RN) ; C axe 6 de 3 à 2 (le paquet de révision de 2018-2019 bloqué par le Sénat est un objet, expliqué ou non : trois objets avec la proportionnelle et les retraits de 2026). Bloc (d) instruit (4 cas 2017-2019, aucun engagement explicite rompu, M 2 confirmé). Dilhan n'a pas relu la page v1.2 ; ses retours restent attendus.
- **Verticale 2, RN : étapes 1 à 8 faites (socle v2.2).** Page publiée en privé le 2026-10-26 : https://claude.ai/artifact/K4r1V5pr5MTEYm6XHd1Y6b (HTML archivé dans `05-artifacts/rn.html`, 158 sources, contrôle `verifie-page.py` sans problème, rendu vérifié à 390 px en clair et en sombre). Dilhan n'a pas encore partagé ni relu la page. Corpus (45 archives, `01-corpus.md`, 83 identifiants C-RN), six fiches extraites puis contrôlées (54 corrections), étapes 3 à 5 et Q5 par six agents, chapitre Méthode, carte des tendances, revue contradictoire (défense, contradiction), arbitrage appliqué, article long écrit par l'agent principal et **soumis à Dilhan le 2026-10-26**. Grille finale :

| Axe | D | F | C | E |
|---|---|---|---|---|
| 1 Finances publiques et dette | 4 Plutôt fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 2 Travail, protection sociale, fraude | 3 Partiellement fondé | 3 Conditionnelle | 4 Plutôt cohérent | 3 Répond en partie |
| 3 Immigration | 3 Partiellement fondé | 2 Très incertaine | 2 Écart important (pondération v2.1) | 3 Répond en partie |
| 4 Pouvoir d'achat et fiscalité | 4 Plutôt fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 5 Sécurité, ordre public, libertés | 3 Partiellement fondé | 3 Conditionnelle | 4 Plutôt cohérent | 4 Répond |
| 6 Institutions, démocratie, Europe | 4 Plutôt fondé | 2 Très incertaine | 4 Plutôt cohérent | 3 Répond en partie |
| Méthode (M) | 3 Écart partiel (parole, comportement parlementaire et discipline interne ; deux manquements : motion de rejet Duplomb, discipline revendiquée contre maintiens ; pas d'actes de gouvernement) | | | |
| Carte des tendances | 5 traitées, 9 en partie, 0 nommée, 0 absente | | | |

- **Prochaine étape : les retours de Dilhan sur la page RN (privée) ; puis la question GitHub (publication du repo, « sur feu vert explicite ») ; puis la verticale 3 (LFI)** selon la marche à suivre ci-dessous, avec les règles v2.2 et les précisions du 2026-10-26 dès l'étape 1. Titre prévu au socle : « Le RN : ce qu'il propose, ce qu'il vote ». La page doit lister les 47 demandes avec intensité et statut (règle « l'inventaire entier, pas un extrait ») : les tableaux Q5 des fiches 1, 2, 4, 5, 6 ont le statut en deuxième colonne ; **la fiche 3 a un tableau à colonnes différentes (mesure puis statut dans le texte)** : lire le verdict E et le tableau ensemble pour fixer les six statuts.
- Git : repo local `~/Documents/Politique/elections-france-2027`, branche `main`, environ 45 commits, **rien n'est poussé, aucun remote**. Publication GitHub : décidée « après la première verticale relue, sur feu vert explicite de Dilhan » ; pas encore demandée.

## Boucle de révision du socle après deux verticales : faite le 2026-10-26

Six chantiers exécutés dans l'ordre (commits `ed6c5b9` socle, `e404ac0` bloc (d), `a07ae2f` fiches et arbitrage v3, `40ed1fb` page v1.2 et registres) : précisions au socle ; bloc (d) Renaissance (sous-agent Opus) relu et arbitré ; six fiches relues par un sous-agent Opus (mesures structurantes nommées, « Poids de la concordance », écarts de montant reclassés en écarts de chiffrage, motif D de l'axe 6 sans le Cevipof, phrase « le niveau 4 ne décide pas ») ; `revue/arbitrage-v3.md` (sept doutes du sous-agent tranchés, deux fondés) ; `article-long.md` (section « Ce que la boucle de révision a changé ») ; page republiée à la même URL par un sous-agent Sonnet (lecture puis publication, pour ne pas charger le contexte principal avec le HTML en ligne ; version 5 en ligne), vérifiée à 390 px en clair et en sombre. Reste à faire à la réception des retours de Dilhan : rien de planifié ; si un cran déplacé est contesté, le remettre dans la fiche, l'arbitrage, l'article, la page (pastille, chip, paragraphe, note « Relecture ») et les registres.

Pour les verticales suivantes : la synthèse devra repasser, pour les cinq forces, des requêtes complémentaires sur les propos visés au titre du sexe et de l'orientation sexuelle (périmètre de la loi de 1881 fixé après l'instruction RN) ; les scrutins de la XVIe législature (3213 et autres) restent à traiter de façon commune.

## Marche à suivre pour une page (étape 8, suivie pour Renaissance et le RN ; à reprendre pour les trois suivantes)

1. Lire `01-socle/04-format-artifacts.md` v2 : titre, surtitre « Lecture · programme et votes 2022-2026 », grille 6 × 4 (24 pastilles) plus une ligne « Comment ils gouvernent » et la carte des tendances en tuiles, six chapitres courts (3 à 4 lignes par question, un panneau visuel maximum, encadré « Ce qui tient », bloc « Creuser » avec la matrice de votes et **toutes les demandes de l'axe** avec intensité et statut), chapitre « Comment ils gouvernent », « Hors grille », « Ce qu'il faut retenir » (quatre points, pas de note globale), sources par axe étiquetées, note de méthode avec dates de gel.
2. Écrire la page avec des jetons de sources et l'assembler avec `_scripts/assemble-sources.py` (voir `05-artifacts/README.md`) : le CSS et le dessin d'en-tête se recopient depuis `05-artifacts/renaissance.html` (`{{CSS}}`, `{{HERO_SVG}}` dans le fichier source, épissure faite par un petit script avant l'assemblage). Repartir de `05-artifacts/renaissance.html` et `rn.html` : garder le CSS et les composants (`.grid`, `.pill`, `.mline`, `.tend`, `.qb`, `.panel`, `.votes`, `.true`, `details.dig`, `ul.dem` avec `.st` et `.ti`), remplacer le contenu. Charger les skills `artifact-design` puis `dataviz` avant d'écrire (règle de l'outil Artifact).
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

- **Retours de Dilhan sur la page RN** (privée, pas encore partagée). Les deux crans Renaissance déplacés le 2026-10-26 sont confirmés.
- **Lignes 3 et 8 de `02-partis/rn/revue/retours-socle.md`** (scrutin 3213 à la synthèse ; plafond de 64 ans d'Orléans le 17 novembre 2026). Chaque modification du socle passe par `01-socle/CHANGELOG.md`.
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
