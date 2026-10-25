# Pages publiées

Le code HTML de chaque page publiée est archivé ici (`<slug>.html`), à l'identique de la version en ligne. L'URL ne change jamais pour une page donnée ; une mise à jour republie à la même URL et remplace le fichier.

| Slug | Titre | URL | Série | Dernière publication | Statut de partage |
|---|---|---|---|---|---|
| qui-paie-pour-qui | Qui paie pour qui ? | https://claude.ai/artifact/95kD4VLYrjVh3kH9rZXxfc | Vérification | 2026-10-24 (v2) | partagée, toute personne avec le lien |
| immigration-vrai-ou-faux | Immigration : vrai ou faux ? | https://claude.ai/artifact/V1w68c2LjyuVbLEgFnuan4 | Vérification | 2026-10-24 (v1) | partagée, toute personne avec le lien |
| renaissance | Renaissance : ce qu'elle propose, ce qu'elle vote | https://claude.ai/artifact/DvTLMrSY4DesQbiNN1NkW2 | Lecture | 2026-10-25 (v1) | privée, non partagée |

Les deux pages de la série « Vérification » ont été produites avant la création de ce repo. Leur HTML n'est pas archivé ici ; la version publiée fait foi et peut être relue avec l'outil Artifact (action `read`).

Les pages de la série « Lecture » (une par force, puis la synthèse) sont ajoutées au fil des verticales. Contrôle avant publication : `python3 _scripts/verifie-page.py 05-artifacts/<slug>.html` (balises, ancres, sources citées et numérotées, tirets longs, squelette interdit), puis `_scripts/lint-texte.py`, puis capture à 390 px en clair et en sombre dans le navigateur intégré, sur la page publiée (le navigateur intégré ne lit pas les fichiers locaux).
