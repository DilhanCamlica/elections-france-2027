# Verticales : état d'avancement et gabarit

## Tableau de bord

| Ordre | Force | Dossier | Étape atteinte | Version du socle appliquée | Page | Dernière révision |
|---|---|---|---|---|---|---|
| 1 | Renaissance | `renaissance/` | 0 (non commencée) | | | |
| 2 | RN | `rn/` | 0 | | | |
| 3 | LFI | `lfi/` | 0 | | | |
| 4 | PS | `ps/` | 0 | | | |
| 5 | LR | `lr/` | 0 | | | |

Étapes (voir `01-socle/00-methodologie.md`) : 1 corpus, 2 extraction par axe, 3 diagnostics, 4 faisabilité, 5 cohérence, 6 revue contradictoire, 7 article long et challenge, 8 page.

Quand le socle change (voir `01-socle/CHANGELOG.md`), la colonne « version du socle appliquée » dit quelles verticales doivent être relues.

## Gabarit d'une verticale

Chaque dossier `02-partis/<parti>/` suit la structure de `_gabarit/` :

```
<parti>/
  00-perimetre.md          périmètre retenu, groupe, candidat (statut), date d'arrêt du corpus
  01-corpus.md             liste des documents qui font foi, avec fiche par document
  corpus/                  PDF et textes archivés (nom explicite + date de téléchargement)
  axes/
    1-finances-publiques.md
    2-travail-protection-sociale.md
    3-immigration.md
    4-pouvoir-achat-fiscalite.md
    5-securite-libertes.md
    6-institutions-democratie-europe.md
  votes/
    scrutins.md            position du groupe sur chaque scrutin gelé, avec lien, et position des quatre autres groupes
  revue/
    defense.md             rapport du relecteur qui défend le parti
    contradiction.md       rapport du relecteur qui défend ses adversaires
    arbitrage.md           arbitrages de l'agent principal
  article-long.md          l'article soumis à Dilhan, avec ses corrections
  hors-grille.md           thèmes majeurs du programme non traités
```

Chaque fiche `axes/<axe>.md` suit `_gabarit/axes/fiche-axe.md`.

## Fichier transversal

`convergences.md` : relevé, axe par axe, des mesures identiques ou très proches entre deux forces ou plus. Alimenté dès l'étape 2 de chaque verticale.
