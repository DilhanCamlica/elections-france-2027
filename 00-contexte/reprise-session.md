# Reprise de session : état au 2026-10-25, soir

Ce fichier est le point d'entrée d'une session qui reprend le travail après un compactage ou un redémarrage. Il complète `CLAUDE.md` (règles) et `README.md` (structure) par ce qu'aucun fichier ne dit : où on en est exactement, ce qui est décidé mais pas encore fait, les pièges rencontrés. Il est réécrit à chaque fin de session.

## Ordre de lecture pour reprendre

1. `CLAUDE.md`, puis `README.md`.
2. Ce fichier.
3. `01-socle/01-criteres.md` (v2) et `01-socle/04-format-artifacts.md` (v2) en entier ; `01-socle/CHANGELOG.md` pour l'historique des décisions.
4. Pour produire la page Renaissance : `02-partis/renaissance/article-long.md` (y compris le complément v2), les six fiches `02-partis/renaissance/axes/*.md` (lire au moins les verdicts, « Ce qui tient », les matrices de votes et les sections Q5), `methode.md`, `tendances.md`, `hors-grille.md`.
5. Le gabarit HTML : la page « Immigration : vrai ou faux ? » (https://claude.ai/artifact/V1w68c2LjyuVbLEgFnuan4), à relire avec l'outil Artifact (`action: "read"`) ; son HTML complet est sauvegardé par l'outil dans un fichier local indiqué dans le résultat. La page « Qui paie pour qui ? » (https://claude.ai/artifact/95kD4VLYrjVh3kH9rZXxfc) utilise le même système (composants : barres, barres empilées, tuiles, matrice de points, ticket de caisse, axe d'estimations, blocs repliables, échelle de verdict à cinq crans, thème clair et sombre, Newsreader, Public Sans, IBM Plex Mono).

## État exact

- **Socle : v2**, validé par Dilhan en deux grills le 2026-10-25. Six questions (Diagnostic, Mesures, Faisabilité avec effets distributifs, Cohérence, Écoute, Méthode) et une carte des tendances. Deux inventaires gelés dans `03-sources/` : `demandes-exprimees.md` (47 demandes) et `tendances-lourdes.md` (14 tendances). Liste de 23 scrutins gelée plus un complément (4758) dans `03-sources/scrutins-selectionnes.md`, positions des cinq groupes dans `scrutins-positions.md`.
- **Verticale 1, Renaissance : étapes 1 à 7 faites en v2.** Verdicts finaux après deux revues contradictoires et deux arbitrages (`revue/arbitrage.md`, `revue/arbitrage-v2.md`) :

| Axe | D | F | C | E |
|---|---|---|---|---|
| 1 Finances publiques et dette | 4 Plutôt fondé | 3 Conditionnelle | 2 Écart important | 3 Répond en partie |
| 2 Travail, protection sociale, fraude | 3 Partiellement fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 3 Immigration | 4 Plutôt fondé | 3 Conditionnelle | 3 Écart partiel | 3 Répond en partie |
| 4 Pouvoir d'achat et fiscalité | 4 Plutôt fondé | 2 Très incertaine | 2 Écart important | 3 Répond en partie |
| 5 Sécurité, ordre public, libertés | 3 Partiellement fondé | 3 Conditionnelle | 3 Écart partiel | 4 Répond |
| 6 Institutions, démocratie, Europe | 4 Plutôt fondé | 2 Très incertaine | 3 Écart partiel | 3 Répond en partie |
| Méthode (M) | 2 Écart important de méthode | | | |
| Carte des tendances | 8 traitées, 6 en partie, 0 nommée, 0 absente | | | |

- **Article long soumis à Dilhan** (`article-long.md`, v1 puis complément v2). Il ne l'a pas encore challengé ligne par ligne ; sa remarque de fond (analyse « lisse ») a été traitée par le passage en v2. Statut : il a dit vouloir produire la page après compactage.
- **Prochaine étape : étape 8, la page Renaissance.** Puis boucle de révision (déjà largement faite par la v2), puis verticale 2 : RN.
- Git : repo local `~/Documents/Politique/elections-france-2027`, branche `main`, 31 commits environ, **rien n'est poussé, aucun remote**. Publication GitHub décidée « après la première verticale, sur feu vert explicite de Dilhan » : pas encore demandée.

## Marche à suivre pour la page (étape 8)

1. Lire `01-socle/04-format-artifacts.md` v2 : titre « Renaissance : ce qu'elle propose, ce qu'elle vote », surtitre « Lecture · programme et votes 2022-2026 », grille 6 × 4 (24 pastilles) plus une ligne « Comment ils gouvernent » et la carte des tendances en tuiles, six chapitres courts (3 à 4 lignes par question, un panneau visuel maximum, encadré « Ce qui tient », bloc « Creuser »), chapitre « Comment ils gouvernent », chapitre court « Ce qui vient », « Hors grille », « Ce qu'il faut retenir » (quatre points, pas de note globale), sources par axe étiquetées, note de méthode avec dates de gel.
2. Repartir du HTML de la page immigration (relue via l'outil Artifact), garder le CSS, remplacer le contenu. Charger les skills `artifact-design` puis `dataviz` avant d'écrire (règle de l'outil Artifact).
3. Matrices de votes : scrutins de l'axe en lignes, cinq groupes en colonnes (LFI, SOC, EPR, DR, RN), positions dans `03-sources/scrutins-positions.md` ; le 4758 figure en complément pondéré à part aux axes 1, 2 et 4.
4. Les 18 + 6 + 1 verdicts et leurs phrases de conclusion sont dans les fiches (`**Verdict …**`) ; les « Ce qui tient » sont à reprendre tels quels, condensés.
5. Écrire le fichier dans `05-artifacts/renaissance.html`, le passer au contrôle : `_scripts/lint-texte.py` (tirets), plus un script à écrire dans `_scripts/` qui vérifie balises fermées, références `#sN` existantes et toutes citées, ancres valides (la série précédente en avait un, non versionné ici). Capture à 390 px en clair et en sombre : Playwright n'a pas été vérifié sur ce Mac ; le navigateur intégré (`mcp__Claude_Browser__*`, `resize_window` 390 × 844, `colorScheme`) peut servir.
6. Publier avec l'outil Artifact (`icon` sur la première publication, `description` d'une phrase). Une nouvelle page est privée : le dire à Dilhan. Inscrire l'URL dans `05-artifacts/README.md` et `README.md`, archiver le HTML, commiter `🖼️ artifact: renaissance v1`.
7. Dans la note de méthode de la page : périmètre (Renaissance seul, groupe EPR, candidat Attal), corpus arrêté au 2026-10-25, 23 scrutins gelés plus 4758, inventaire des demandes et liste des tendances gelés le 2026-10-25, lien vers le repo quand il sera public.

## Décisions prises, non dérivables des fichiers de contenu

- Sous-agents : Opus pour recherche, vérification, revue ; Sonnet pour extraction, transcripts, scripts, carte des tendances. L'agent principal seul sur Fable. Toujours passer `model` explicitement.
- Les sous-agents ne commitent pas ; l'agent principal commite par étape (`CLAUDE.md`).
- Grill-me (une question à la fois, recommandation à chaque fois) dès qu'un choix de forme, de compréhension ou d'expérience de lecture se présente ; sinon on fait, on ne demande pas.
- Dilhan veut qu'on lui renvoie en sparring les cadrages de ses remarques que les données ne soutiennent pas (« guerre civile », « sans du tout s'adapter »), tout en retenant les critères de fond. Mémoire Claude : `analyse-politique-pas-seulement-les-faits.md`.
- Ordre des verticales : Renaissance, RN, LFI, PS, LR.
- Date d'arrêt du corpus : fixée au début de chaque verticale (Renaissance : 2026-10-25), réalignée à la fin des cinq.

## En suspens (à exécuter quand c'est possible)

- **Scrutin Smic** : la PPL LFI n° 3176 (Smic à 1 700 € net) est en niche le 29 octobre 2026. Si un scrutin a lieu, il remplace le n° 881 dans la liste gelée (décision écrite avant tout vote), et la matrice de l'axe 4 est à refaire pour les cinq forces ; la ligne Smic de Q5 axe 4 peut changer.
- **Transcript Manon Bril** (France Inter) : aucun sous-titre, aucun outil de transcription audio installé (ni whisper, ni mlx_whisper). Sans effet sur l'étude.
- **Publication GitHub** du repo : décidée après la première verticale relue ; à demander à Dilhan au moment de la page.
- **Programme 2017** et discours au Congrès de 2017 : à archiver dans `02-partis/renaissance/corpus/` (règle v2 du corpus), reconstitués pour l'instant par sources secondaires.
- **Retours du socle** : tous traités (`02-partis/renaissance/revue/retours-socle.md`), sauf la ligne 6 (Smic) qui attend le 29 octobre.

## Pièges rencontrés

- Accès refusés (403) : Légifrance, résultats électoraux du ministère de l'Intérieur, pages DGEF, Interstats, JDD, CNews, Europe 1 ; Mediapart payant. Contournements dans `01-socle/03-sources-et-hierarchie.md` §6.
- Le champ « position majoritaire » de l'open data de l'Assemblée est faux une fois sur deux : recalcul par la règle des 60 % (`03-sources/scrutins-positions.md`).
- Les agents d'extraction inventent des « divergences » qui n'en sont pas : définition stricte dans le brief d'étape 2.
- Les relecteurs lisent la ligne 2 du registre des biais et la notion de contre-pied « assumé » de façons opposées : règles écrites en v2 (`01-criteres.md`, échelles C, E, M).
- Deux rédacteurs sur un même fichier : ne jamais lancer en parallèle deux agents qui écrivent dans la même fiche (effets distributifs puis Q5 ont été séquencés pour ça).
- La carte des tendances tend au « tout traité » : statut « traitée en partie » ajouté pour ça.

## Contexte familial d'origine

`00-contexte/echange-famille-2026-10-25.md`. Les deux pages déjà partagées à la famille sont les deux artifacts cités plus haut. Le point C-D-E de l'échange (violences, interdiction de manifester, Mediapart) est documenté dans `00-contexte/contexte-actualite-octobre-2026.md` et, pour la méthode de gouvernement, dans `02-partis/renaissance/methode.md`. Les affirmations de la vidéo longue de Viktorovitch sont triées (confirmées, inexactes, non vérifiables) dans ce même fichier.
