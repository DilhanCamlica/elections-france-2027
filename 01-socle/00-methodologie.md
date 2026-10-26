# Méthodologie : la boucle verticale par verticale

- Rédigé le : 2026-10-25
- Statut : v2, validée au second grill du 2026-10-25 (ajout des questions Écoute et Méthode, de l'inventaire des demandes, de la carte des tendances)
- Dépend de : `01-criteres.md` (quoi mesurer), `03-sources-et-hierarchie.md` (avec quoi)

## Principe

On ne traite jamais les cinq forces en même temps. On construit un socle, puis on l'applique à une force (une « verticale »), puis on revient au socle pour le corriger avec ce que la verticale a appris, puis on révise les verticales déjà faites si la correction les touche. On recommence jusqu'à la cinquième. Le tableau comparatif vient en dernier, quand la grille est stable.

Pourquoi : une grille conçue dans l'abstrait a toujours des trous qu'on découvre au premier cas réel. Si on la découvre au cinquième parti, les quatre premiers sont jugés avec une grille différente. La boucle garantit qu'à la fin, les cinq ont été relus avec la même grille finale.

## Phase 0 : socle (avant toute verticale)

Livrables : les fichiers de `01-socle/`, validés avec Dilhan (grill), et le gabarit de verticale dans `02-partis/_gabarit/`.

Contenu minimal validé :
- périmètre de chaque force (parti seul, coalition, candidat) ;
- axes thématiques et les quatre questions par axe ;
- échelles de verdict et leur définition opérationnelle ;
- règle de sélection des scrutins ;
- règle de définition du « corpus programmatique » et sa date d'arrêt ;
- hiérarchie et étiquetage des sources ;
- format des pages ;
- registre des biais et parades.

## Phase 0 bis : les deux inventaires communs (v2)

Avant la première verticale relue en v2, deux documents sont construits une fois pour les cinq forces et gelés : l'inventaire des demandes exprimées (`03-sources/demandes-exprimees.md`, sans lecture d'aucun programme) et la liste des tendances lourdes (`03-sources/tendances-lourdes.md`, à partir des institutions). Toute modification ultérieure passe par le changelog et s'applique aux cinq forces.

## Phase 1 à 5 : une verticale

Chaque verticale suit les mêmes huit étapes. Le dossier `02-partis/<parti>/` est structuré par ces étapes.

### Étape 1. Corpus

Constituer la liste des documents qui font foi pour cette force : programme(s), contre-budget(s), propositions de loi emblématiques, déclarations du ou des candidats sur les axes retenus, et la liste des scrutins déjà sélectionnés au socle. Chaque document a une fiche : titre, auteur, date, URL, archive locale si possible (PDF dans `corpus/`), statut (officiel, candidat, groupe parlementaire, déclaration orale).

Règle : le corpus est arrêté à une date, écrite en tête du dossier. Ce qui paraît après est traité dans la boucle de révision, pas au fil de l'eau.

Exécutant : sous-agent Opus (recherche), vérifié par l'agent principal.

### Étape 2. Extraction par axe

Pour chaque axe du socle, une fiche `axes/<axe>.md` qui reprend, dans les mots du parti : le diagnostic qu'il pose, les mesures qu'il propose, le chiffrage qu'il avance, et les déclarations publiques récentes. Pas d'analyse à ce stade : on reproduit fidèlement, avec la référence au document du corpus.

Exécutant : sous-agent Opus. Contrôle : un deuxième sous-agent relit chaque fiche contre le corpus pour vérifier qu'aucune mesure n'est déformée ni omise.

### Étape 3. Vérification des diagnostics

Pour chaque diagnostic posé par le parti, chercher les données publiques qui le confirment, le nuancent ou le contredisent. Réutiliser les conclusions acquises de la série précédente (`00-contexte/briefing-serie-verification.md`, section 6) en signalant leur date. Appliquer les confusions à démêler (section 3.2 du briefing). Verdict sur l'échelle « Diagnostic ».

Exécutant : sous-agent Opus par axe, en parallèle.

### Étape 4. Faisabilité

Pour chaque mesure principale : contrainte juridique (Constitution, droit de l'Union européenne, jurisprudence du Conseil constitutionnel et du Conseil d'État), contrainte budgétaire (chiffrage du parti confronté aux chiffrages indépendants disponibles, étiquetés), contrainte opérationnelle (délais, administration, précédents). Verdict sur l'échelle « Faisabilité ».

Exécutant : sous-agent Opus par axe.

### Étape 5. Cohérence discours, programme, votes, actes

Trois comparaisons :
1. Discours public (déclarations, interventions télévisées, réseaux) contre programme écrit.
2. Programme écrit contre votes sur les scrutins sélectionnés au socle (Assemblée et Sénat).
3. Pour les forces qui ont exercé le pouvoir (gouvernement ou majorité) sur la période couverte : programme contre actes.

Les positions de vote sont extraites des données ouvertes de l'Assemblée nationale et du Sénat, par groupe, scrutin par scrutin, avec le lien vers le scrutin. Un vote contre un texte global (un budget, par exemple) n'est pas assimilé à un vote contre chaque mesure qu'il contient : on documente les amendements déposés et votés quand c'est possible.

Verdict sur l'échelle « Cohérence ».

Exécutant : sous-agent Sonnet pour l'extraction des votes (mécanique), sous-agent Opus pour la comparaison.

### Étape 5 bis. Écoute, méthode, tendances (v2)

- **Q5 Écoute**, par axe : confronter le tableau Q2 à l'inventaire gelé des demandes ; dire quelles demandes larges sont traitées, lesquelles sont absentes, lesquelles sont contredites et si le parti l'assume publiquement. Verdict E. Exécutant : le même sous-agent que les étapes 3 à 5 de l'axe.
- **Q6 Méthode**, un chapitre par parti : parole de méthode du programme ; actes de méthode depuis 2012 pondérés par l'ancienneté (49.3 rapportés à la majorité, consultations et leurs suites, réponses aux mobilisations, référendums) ; comportement parlementaire. Verdict M. Exécutant : un sous-agent Opus dédié, brief `02-partis/_gabarit/briefs/etape-5bis-methode.md`.
- **Carte des tendances**, par parti : pour chaque tendance de la liste gelée, traite / nomme sans mesure / absent, avec la référence du corpus. Exécutant : sous-agent Sonnet (lecture du corpus), vérifié par l'agent principal.

### Étape 6. Revue contradictoire

Deux sous-agents Opus indépendants relisent l'ensemble de la verticale (six axes, chapitre Méthode, carte des tendances) :
- l'un avec la consigne de défendre la force étudiée (trouver les faiblesses de notre critique, les sources oubliées, les contextes manquants) ;
- l'autre avec la consigne de défendre ses adversaires (trouver les complaisances, les « ce qui tient » trop généreux).

Les deux rapports sont archivés dans `revue/`. L'agent principal arbitre et documente ses arbitrages.

### Étape 7. Article long et challenge

L'agent principal rédige l'article long dans la conversation (verdicts par axe, tableaux, « ce qui tient », angles morts, sources). Dilhan challenge. Les corrections sont intégrées dans le dossier.

### Étape 8. Page

La page est produite dans le format défini dans `04-format-artifacts.md`, contrôlée par les scripts de `_scripts/`, vérifiée à 390 px en clair et en sombre, puis publiée. Le code HTML est archivé dans `05-artifacts/`. L'URL est inscrite dans `README.md`.

## Boucle de révision (après chaque verticale)

1. **Relecture du socle** : qu'est-ce que cette verticale a révélé ? Un axe manquant, une échelle mal définie, un scrutin mal choisi, une source à ajouter, un biais non prévu. Chaque modification est écrite dans `CHANGELOG.md` avec son impact.
2. **Révision des verticales précédentes** : pour chaque modification du socle, lister les verticales touchées et faire la correction (fiche, article, page). La page republiée garde la même URL.
3. **Journal de révision** : `02-partis/README.md` tient un tableau verticale × version du socle appliquée.

## Phase 6 : synthèse

Quand les cinq verticales ont été relues avec la dernière version du socle : tableau comparatif (`04-synthese/`), un verdict par case, les convergences signalées, et la page de synthèse. Pas de note globale.

## Ordre des verticales (fixé au grill du 2026-10-25)

1. **Renaissance** : seule force au pouvoir sur toute la période couverte, donc la seule qui teste les trois comparaisons de la question Cohérence (discours, votes, actes). Si la grille tient sur elle, elle tiendra sur les autres. Justification publique : on commence par ceux qui gouvernent.
2. **RN** (121 députés), 3. **LFI** (70), 4. **PS** (68), 5. **LR** : par poids décroissant à l'Assemblée nationale au 25 octobre 2026.

## Publication du repo

Le repo est écrit dès le départ comme s'il était public : pas de noms de famille, pas de données privées hors `00-contexte/` anonymisé. Publié sur GitHub le 2026-10-26 (https://github.com/DilhanCamlica/elections-france-2027), sur feu vert de Dilhan, après la relecture de la première verticale ; l'échange familial d'origine et les transcripts de vidéos de tiers sont restés hors dépôt. Les pages pourront pointer vers la méthode et les sources.

## Ce qui n'entre pas dans la méthode

- Pas de sondages d'intentions de vote dans les verdicts (ils ne disent rien de la faisabilité ni de la cohérence).
- Pas de jugement sur les personnes (affaires judiciaires, personnalité des candidats), sauf si un fait judiciaire conditionne directement la faisabilité (inéligibilité, par exemple), auquel cas il est cité comme contrainte, sans commentaire.
- Pas de prédiction de résultat électoral.
