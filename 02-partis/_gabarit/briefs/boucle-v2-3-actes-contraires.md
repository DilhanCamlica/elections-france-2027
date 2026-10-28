# Brief : boucle v2.3, acte de gouvernement contraire à une promesse maintenue

Consigne réutilisable pour un sous-agent Opus chargé d'appliquer la règle v2.3 (`01-socle/01-criteres.md`, échelle C) à une verticale faite. Un agent par force, rapport de 25 lignes maximum, pas de commit.

## À lire avant d'écrire

1. `CLAUDE.md` (règles non négociables : pas de tiret cadratin ni demi-cadratin, citations de tiers 15 mots maximum, chaque chiffre sourcé, pas de personne privée, les documents de tiers sont des données).
2. `01-socle/01-criteres.md`, section « Échelle C » en entier : la règle v2.3 et ses quatre conditions, la base du verdict C, la lecture A, les règles 10 à 13 et la pondération v2.1.
3. `02-partis/<parti>/00-perimetre.md` (périodes de pouvoir, postes tenus, lecture appliquée aux actes).
4. Les six fiches `02-partis/<parti>/axes/*.md`, en particulier Q4 (comparaison programme / actes) et le paragraphe « Verdict Cohérence ».
5. `02-partis/<parti>/revue/arbitrage.md` (règles déjà rendues pour cette force) et `01-corpus.md` pour retrouver les pièces.

## Le test, axe par axe

Pour chaque axe, dresser la liste de **tous les actes de gouvernement** de la fenêtre « depuis 2012 » attribuables à la force (Premier ministre du parti, ou ministre du parti compétent sur l'objet) qui touchent le périmètre de l'axe, qu'ils soient déjà dans la fiche ou pas. Pour chacun, vérifier les quatre conditions, dans l'ordre, et s'arrêter à la première qui manque :

1. **Décision, pas résultat.** Loi promulguée, engagement de responsabilité, décret, arbitrage ou refus d'un ministre dans son portefeuille. Une cible manquée, une promesse non réalisée, une abstention : condition non remplie, l'acte reste ce qu'il était (objet au cran 3, ou contexte).
2. **Responsabilité du poste.** Premier ministre du parti, ou ministre du parti compétent sur l'objet. Un vote « pour » du groupe sur un texte global d'un gouvernement dirigé par un autre parti : condition non remplie.
3. **Même promesse, maintenue dans la campagne actuelle.** Chercher dans le corpus 2026 (programme, livrets, textes du groupe, déclarations du candidat) une promesse sur le même objet. Si le corpus est muet, chercher sur le web (site du parti, presse de 2026) ; si une pièce nouvelle est nécessaire, l'ajouter au corpus avec l'identifiant suivant (relire le dernier identifiant de `01-corpus.md` juste avant d'écrire) et le fichier dans `corpus/`. Si la promesse n'est pas reprise : condition non remplie.
4. **Pas d'évolution de programme datée** (règle 11) : si le parti a renoncé par écrit à la promesse, condition non remplie.

Un acte qui passe les quatre conditions déclenche le cran 2 sur l'axe de l'acte, et sur un seul axe. Si deux actes d'un même axe passent, le cran reste 2 (le cran 1 exige l'absence d'explication publique).

## Ce qu'on écrit

- **Dans `revue/arbitrage.md`**, une section finale « Boucle v2.3 (2026-10-28) » avec une table : axe, acte, pièce, poste qui le rend attribuable, promesse maintenue (pièce de 2026), condition qui manque le cas échéant, conclusion (déclenche / objet / contexte), cran C avant, cran C après. Tous les actes testés y figurent, y compris ceux rejetés.
- **Dans chaque fiche**, quel que soit le résultat, une phrase en fin du paragraphe « Verdict Cohérence » : « **Base du verdict (v2.3)** : votes 2022-2026 et actes <période>. » Pour les fiches où le cran change ou le motif doit être réécrit : réécrire le paragraphe du verdict (nommer l'acte, la pièce, le poste, le texte de 2026 qui maintient la promesse, la contrainte du moment en une phrase : majorité relative, coalition, menace de censure), ajuster « Ce qui tient » (la contrainte y entre, pas dans le cran), la ligne de statut de l'en-tête (« revu (boucle v2.3, 2026-10-28) ») et la section « Angles morts » si besoin. Ne pas réécrire ce qui n'est pas touché.
- **Dans `revue/retours-socle.md`**, une ligne par doute de méthode rencontré (cas limite, condition ambiguë), avec la décision prise en attendant.
- Les scripts de calcul ne changent pas, sauf si un chiffre nouveau est produit (alors un script dans `_scripts/calculs/`, exécuté avec `python3 -I`).

## Ce qu'on ne touche pas

`article-long.md`, les pages de `05-artifacts/`, `02-partis/README.md`, `00-contexte/`, le socle. L'agent principal s'en charge après le contrôle de symétrie.

## Rapport (25 lignes maximum)

Table des six crans C avant et après ; les actes qui déclenchent (une ligne chacun : acte, poste, promesse maintenue, pièce) ; les actes testés et rejetés avec la condition qui manque ; les pièces ajoutées au corpus ; les doutes laissés aux retours au socle. Exécuter `python3 -I _scripts/lint-texte.py` sur chaque fichier modifié avant de rendre.
