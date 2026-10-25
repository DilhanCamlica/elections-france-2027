# Élections France 2027 : lecture neutre et sourcée des programmes

Ce repo documente une étude indépendante de ce que proposent cinq forces politiques françaises en vue de la présidentielle de 2027, et de la distance entre ce qu'elles disent, ce qu'elles écrivent et ce qu'elles votent.

Il est la matière probante. Les produits finaux sont des pages web (artifacts) destinées à être partagées directement avec des lecteurs qui ne sont pas d'accord entre eux. Chaque chiffre d'un artifact doit pouvoir être retrouvé ici, avec sa source.

## Pourquoi ce travail existe

Il prolonge une série de pages de vérification d'affirmations politiques (« Qui paie pour qui ? », « Immigration : vrai ou faux ? »), partagées dans un cadre familial avant les élections. La discussion a glissé des affirmations vers les solutions : que proposent les partis, est-ce faisable, et traitent-ils de vrais problèmes ?

## Ce qu'on étudie

Cinq forces : La France insoumise (LFI), Parti socialiste (PS), le parti présidentiel (Renaissance, ex-LREM), Les Républicains (LR), Rassemblement national (RN). Le périmètre exact de chaque force (parti seul ou coalition) est fixé dans `01-socle/01-criteres.md`.

Pour chacune, sur des axes thématiques communs, six questions (socle v2) :

1. **Diagnostic** : le problème que le parti dit vouloir régler est-il fondé dans les données ?
2. **Mesures** : que propose-t-il précisément, dans ses propres mots ?
3. **Faisabilité** : juridique, budgétaire, opérationnelle, avec les effets distributifs quand ils sont connus.
4. **Cohérence** : ce qu'il dit en public, ce qu'il écrit dans son programme, ce qu'il vote à l'Assemblée et au Sénat, et ce qu'il a fait quand il était au pouvoir.
5. **Écoute** : le programme traite-t-il les demandes les plus exprimées par la population (inventaire commun, gelé avant lecture des programmes) ? Quand il va contre, le dit-il ?
6. **Méthode** : comment le parti gouverne ou gouvernerait (49.3, consultations et leurs suites, réponses aux mobilisations, référendums), fenêtre depuis 2012.

Plus une carte des tendances lourdes identifiées par les institutions (vieillissement, IA, climat, dette, patrimoine, défense), pour voir ce que chaque programme regarde ou ignore.

Puis une synthèse comparative qui met les cinq forces côte à côte et fait ressortir les convergences.

## Ce qu'on ne fait pas

- Pas de verdict sur des valeurs ou sur ce qui est souhaitable. On tranche des faits, des ordres de grandeur et des cohérences.
- Pas de note globale par parti. Les verdicts sont par axe et par question.
- Pas de « debunk » : chaque fiche contient une partie « ce qui tient » rédigée sincèrement.
- Pas de personne privée citée, pas de citation inventée, pas d'imitation visuelle d'une institution.

## Méthode en bref

Le socle (`01-socle/`) est écrit avant toute lecture de parti : critères, échelles, hiérarchie des sources, registre des biais, format des pages. Puis les partis sont traités un par un (une « verticale »). Après chaque verticale, le socle est relu et corrigé, et les verticales déjà faites sont révisées si nécessaire. Le tableau comparatif est produit en dernier. Le détail est dans `01-socle/00-methodologie.md`.

Toute modification du socle est tracée dans `01-socle/CHANGELOG.md`.

## Transparence sur les biais

Le registre `01-socle/02-registre-biais.md` liste les biais identifiés (sélection des scrutins, asymétrie entre partis au pouvoir et d'opposition, biais des modèles de langage, disponibilité inégale des sources, position de l'auteur) et la parade prévue pour chacun. Si un lecteur en identifie un autre, il a sa place dans ce fichier.

## Structure du repo

| Dossier | Contenu |
|---|---|
| `00-contexte/` | Ce qui a déclenché l'étude : l'échange familial, le briefing de la série précédente, les transcripts des vidéos partagées, les notes de contexte sur l'actualité et le paysage politique d'octobre 2026 |
| `01-socle/` | Méthode, critères et échelles, registre des biais, hiérarchie des sources, format des pages, changelog |
| `02-partis/<parti>/` | Une verticale par force : corpus, fiches par axe, scrutins analysés, article long, revue contradictoire |
| `03-sources/` | Registre des sources communes à plusieurs verticales (chiffrages, bases de scrutins, statistique publique) |
| `04-synthese/` | Le tableau comparatif et sa note de méthode |
| `05-artifacts/` | Code HTML des pages publiées et registre des URL |
| `_scripts/` | Scripts de contrôle (liens, sources citées, tirets longs, cohérence) |

## Outils et exécution

Travail réalisé avec Claude Code (agent principal et sous-agents). Les sous-agents font la collecte, la vérification et la revue contradictoire ; l'agent principal arbitre et rédige. Les règles pour tout agent qui reprend ce repo sont dans `CLAUDE.md`.

## État d'avancement

Voir `01-socle/CHANGELOG.md` et le tableau de bord en tête de `02-partis/README.md`.

## Pages publiées

| Page | Statut | URL |
|---|---|---|
| Qui paie pour qui ? (série précédente) | publiée, partagée | https://claude.ai/artifact/95kD4VLYrjVh3kH9rZXxfc |
| Immigration : vrai ou faux ? (série précédente) | publiée, partagée | https://claude.ai/artifact/V1w68c2LjyuVbLEgFnuan4 |
| Renaissance : ce qu'elle propose, ce qu'elle vote | à faire (verticale 1) | |
| Le RN : ce qu'il propose, ce qu'il vote | à faire (verticale 2) | |
| LFI : ce qu'elle propose, ce qu'elle vote | à faire (verticale 3) | |
| Le PS : ce qu'il propose, ce qu'il vote | à faire (verticale 4) | |
| LR : ce qu'ils proposent, ce qu'ils votent | à faire (verticale 5) | |
| Cinq programmes côte à côte (synthèse) | à faire | |

## Licence et réutilisation

Les textes de ce repo sont réutilisables avec mention de la source. Les documents de tiers (programmes, rapports, articles) restent la propriété de leurs auteurs et ne sont cités que par extraits courts et par lien. Le dossier `00-contexte/` contient un échange privé : il n'est pas destiné à être publié tel quel.
