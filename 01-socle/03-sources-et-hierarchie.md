# Sources : hiérarchie, étiquetage, registre

- Rédigé le : 2026-10-25
- Statut : v2 (2026-10-25)

## 1. Hiérarchie

Du plus fort au plus faible. Un verdict s'appuie en priorité sur les niveaux 1 à 3. Les niveaux 4 et 5 servent à pointer vers une source plus forte ou à documenter un débat.

| Niveau | Type | Exemples | Usage |
|---|---|---|---|
| 1 | **Sources primaires du parti** | Programme officiel (PDF archivé), contre-budget déposé, proposition de loi (texte sur le site de l'Assemblée ou du Sénat), compte rendu intégral des débats, scrutin public | Seules sources admises pour Q2 (mesures) et pour les votes de Q4 |
| 2 | **Statistique publique et institutions de contrôle** | Insee, Drees, Dares, Eurostat, OCDE, Banque de France, Cour des comptes, Haut Conseil des finances publiques, HCFiPS, Conseil d'orientation des retraites, France Stratégie, Conseil d'analyse économique, Défenseur des droits, Sénat et Assemblée (rapports) | Base de Q1 (diagnostic) et des contraintes budgétaires de Q3 |
| 3 | **Juridictions et autorités** | Conseil constitutionnel, Conseil d'État, Cour de justice de l'Union européenne, Cour européenne des droits de l'homme, Commission européenne (avis budgétaires) | Base des contraintes juridiques de Q3 |
| 4 | **Chiffrages et analyses engagés ou académiques** | Institut Montaigne (classé libéral), iFRAP (think tank libéral), Fondapol (classée à droite), Fondation Jean-Jaurès (proche du PS), Terra Nova (centre gauche), OFCE (centre de recherche de Sciences Po, souvent classé keynésien), Institut des politiques publiques (académique), CEPII, Attac (classée à gauche), Observatoire de l'immigration et de la démographie (classé à droite), Contribuables associés (engagé) | Toujours étiquetés ; cités par paire quand ils divergent ; jamais seuls à l'appui d'un verdict |
| 5 | **Presse et fact-checking** | AFP Factuel, Les Décodeurs (Le Monde), CheckNews (Libération), Vrai ou Faux (France Info), Le Figaro, Les Échos, Public Sénat, Mediapart, Contexte, Alternatives économiques, Valeurs actuelles, L'Opinion | Relais vers une source primaire, documentation des déclarations publiques, chronologie. Le média est étiqueté s'il a une ligne éditoriale marquée |

## 2. Règles d'étiquetage

- Tout organisme de niveau 4 et tout média de niveau 5 à ligne marquée reçoit une étiquette courte et factuelle, identique dans tous les fichiers et toutes les pages. La liste des étiquettes est tenue dans `03-sources/etiquettes.md` et s'enrichit. Une étiquette se justifie par un élément public (statuts, financements, autodéfinition, classement par la presse), noté dans ce fichier.
- Les sources de niveau 1 émanant d'un parti sont étiquetées « source du parti, partie prenante ». Les sources gouvernementales sur un sujet où le gouvernement est partie prenante (ministère de l'Intérieur sur une manifestation, par exemple) sont étiquetées « source officielle, partie prenante ».
- On n'étiquette pas la statistique publique (niveau 2), sauf si une controverse documentée existe sur une publication précise.

## 2 bis. Enquêtes d'opinion et revendications (v2)

Les baromètres d'opinion (Cevipof, Ipsos, Elabe, Eurobaromètre), le baromètre d'opinion de la Drees (statistique publique, mais mesure d'opinion) et les revendications écrites des mobilisations sont admis pour un seul usage : construire l'inventaire des demandes exprimées (`03-sources/demandes-exprimees.md`) qui sert à la question Écoute. Ils ne servent jamais à un verdict de fait (Diagnostic, Faisabilité, Cohérence). Chaque enquête est étiquetée « enquête d'opinion », chaque revendication porte son auteur et sa date.

## 2 ter. Processus d'étiquetage (v2)

Un sous-agent qui a besoin d'une étiquette absente la propose dans sa fiche, entre crochets, avec sa justification ; l'agent principal l'inscrit dans `03-sources/etiquettes.md` à la relecture. Le sous-agent ne modifie pas le registre.

## 3. Ce qui ne compte pas comme source

- Un message sur un réseau social sans reprise par un média identifié ou sans archive.
- Un sondage d'opinion, pour un verdict (il peut figurer en contexte).
- Une vidéo d'opinion (y compris celles de `00-contexte/transcripts/`), pour un verdict. Elles servent à repérer des affirmations à vérifier et des sources à remonter.
- La connaissance interne du modèle, pour tout chiffre décrivant le monde actuel.

## 4. Format d'une référence

Dans les fichiers du repo :

```
n. Éditeur, « Titre », date de publication. URL. [étiquette si engagé] [relais : si l'URL est un média qui cite une source primaire non accessible, le dire]
```

Dans les pages : numéro en exposant, liste groupée par thème en pied de page, même format.

## 5. Archivage

Les PDF de programmes, contre-budgets et rapports sont téléchargés dans `02-partis/<parti>/corpus/` ou `03-sources/pdf/` avec un nom explicite et la date de téléchargement, pour que la preuve survive à un changement d'URL. Les pages web importantes sont sauvegardées en texte (`.md`) avec URL et date de consultation. Les fichiers de plus de 20 Mo ne sont pas versionnés : lien et somme de contrôle seulement.

## 5 bis. Positions de vote (v2)

Le champ « position majoritaire » du jeu open data de l'Assemblée est peu fiable (22 écarts sur 27 scrutins constatés). La position d'un groupe est recalculée : position la plus fréquente parmi les votants du groupe, « divisé » si aucune position ne dépasse 60 % des votants. Les déclarations publiques retenues au corpus sont archivées en texte (`.md`) au moment de l'étape 1, pas seulement par leur lien.

## 6. Ce qui marche et ce qui bloque (hérité de la série précédente)

Lecture directe possible : pages et PDF Insee, PDF Drees, rapports du Sénat et de l'Assemblée, Banque de France, Unédic, strategie-plan.gouv.fr (HCFiPS, France Stratégie), vie-publique.fr, legifrance, conseil-constitutionnel.fr.

Bloque ou partiel (constaté jusqu'au 25 octobre 2026) : Légifrance (erreur 403 : passer par le Sénat, Vie publique, le Conseil constitutionnel ou les archives web), sites de résultats du ministère de l'Intérieur (403), Interstats, PDF de l'OCDE (passer par le Trésor ou la presse), pages de la DGEF (403, recouper avec Eurostat), Statista, articles payants (Mediapart, Le Monde au-delà du chapô, Les Échos, JDD, CNews, Europe 1). Pour un article payant, on cite le chapô accessible et les reprises par d'autres médias, et on le dit.

## 7. Registre commun

`03-sources/registre.md` liste les sources utilisées dans plusieurs verticales (chiffrages transversaux, bases de scrutins, séries statistiques), avec un identifiant stable réutilisable dans les fiches (`[S-INSEE-IP2106]`, par exemple). Les sources propres à une verticale restent dans son dossier.
