# Verticales : état d'avancement et gabarit

## Tableau de bord

| Ordre | Force | Dossier | Étape atteinte | Version du socle appliquée | Page | Dernière révision |
|---|---|---|---|---|---|---|
| 1 | Renaissance | `renaissance/` | 8 en v2.2 (boucle de révision du 2026-10-26 faite : v2.1 et v2.2 appliquées, F axe 5 et C axe 6 déplacés, M 2 confirmé, page v1.2 republiée à la même URL ; boucle après LFI du 2026-10-27 : bloc (d) relu sans changement, page v1.4 ; boucle après le PS du 2026-10-27 : fiche 2 annotée (vote de commission du 23 octobre 2024), bloc (d) repassé sans cas de plus, trois textes d'élus du groupe au corpus, page v1.5) | v2.2 (précisions du 2026-10-27 appliquées) | publiée v1.4, partagée : https://claude.ai/artifact/DvTLMrSY4DesQbiNN1NkW2 | 2026-10-26 |
| 2 | RN | `rn/` | 8 en v2.2 (page produite le 2026-10-26, partagée par Dilhan ; boucle après LFI du 2026-10-27 : fiche 4 conforme à la règle du véhicule refusé, page v1.2 ; boucle après le PS du 2026-10-27 : fiche 2 annotée (217 vidé, vote de commission), bloc (d) repassé sans cas de plus, cinq PPL lues comme textes d'élus du groupe, page v1.3) | v2.2 (précisions du 2026-10-27 appliquées) | publiée v1.2, partagée : https://claude.ai/artifact/K4r1V5pr5MTEYm6XHd1Y6b | 2026-10-26 |
| 3 | LFI | `lfi/` | 6 (revue contradictoire et arbitrage faits le 2026-10-26, appliqués : grille D 4/3/3/4/4/4, F 3/3/3/3/3/2, C 4/3/4/3/4/4, E 3/3/3/3/3/3, M 4, carte 8 / 6 / 0 / 0 ; corpus arrêté au 2026-10-26, programme 2027 attendu le 6 novembre 2026, boucle de révision prévue) ; étape 7 : article long écrit le 2026-10-26, revu par Dilhan le 2026-10-27 sans correction ; étape 8 : page produite et publiée le 2026-10-27 (212 sources), partagée par Dilhan ; boucle de révision du socle faite le 2026-10-27 (retours 2, 4, 5 écrits au socle et à l'inventaire, page v1.2) ; relecture de la verticale à la parution du programme (6 novembre 2026 ; boucle après le PS du 2026-10-27 : fiche 2, arbitrage, article et page corrigés (refus de véhicule lu au vote de commission du 23 octobre 2024), bloc (d) repassé, un cas admis de plus (4 cas, M 4 inchangé), motion de mai 2025 lue comme texte d'élus, page v1.3) | v2.2 (précisions du 2026-10-27 appliquées) | publiée v1.2, partagée : https://claude.ai/artifact/Y5vhGKqsBcXhtgtzBpGq6i | 2026-10-27 |
| 4 | PS | `ps/` | 8 (corpus arrêté au 2026-10-27, 94 fiches ; étapes 2 à 6 faites le 2026-10-27 ; lecture A confirmée par Dilhan le 2026-10-27 (actes 2012-2017 comptés pleinement à l'échelle C) : grille D 4/3/4/3/3/4, F 3/3/3/3/3/2, C 3/3/3/2/3/2, E 3/3/3/3/3/3, M 3, carte 11 / 3 / 0 / 0 ; article long écrit le 2026-10-27 (`ps/article-long.md`, 7064 mots, décompte de l'écoute `_scripts/calculs/ps_ecoute_decompte.py`), considéré relu par Dilhan le 2026-10-27 sans correction ; étape 8 : page produite et publiée en privé le 2026-10-27 (`05-artifacts/ps.html` depuis `sources/ps.src.html`, 248 sources, https://claude.ai/artifact/NRgowSK65vkZ99HWXb1Bj3), à partager par Dilhan après relecture ; boucle de révision du socle à faire ; boucle de révision du socle faite le 2026-10-27 (règles 11 à 13, lecture A, texte du groupe, scrutin de commission, dirigeants fédéraux, requêtes élargies : `01-socle/CHANGELOG.md`), `revue/retours-socle.md` clos, page v1.1 republiée (partagée par Dilhan)) | v2.2 (précisions du 2026-10-27) | | 2026-10-27 |
| 5 | LR | `lr/` | 6 (corpus arrêté au 2026-10-27, 92 fiches ; étapes 2 à 6 faites le 2026-10-27 ; revue contradictoire, arbitrage et application faits : grille D 3/3/4/4/3/4, F 3/3/2/3/2/2, C 3/3/3/3/4/4, E 3/3/3/3/4/3, M 3, carte 8 / 6 / 0 / 0 ; deux crans déplacés par la revue, D axe 1 et C axe 5 ; point d'arrêt 2 soumis à Dilhan : lecture des actes de coalition d'un partenaire minoritaire, `lr/revue/arbitrage.md`) | v2.2 (précisions du 2026-10-27) | | 2026-10-27 |

Étapes (voir `01-socle/00-methodologie.md`) : 1 corpus, 2 extraction par axe, 3 diagnostics, 4 faisabilité, 5 cohérence, 5 bis écoute, méthode et tendances (v2), 6 revue contradictoire, 7 article long et challenge, 8 page.

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
    scrutins.md            position du groupe sur chaque scrutin gelé, avec lien, et divergences du groupe hors périmètre cité au socle (produit par `_scripts/votes-parti.py` depuis `03-sources/scrutins-positions.md`)
  revue/
    defense.md             rapport du relecteur qui défend le parti
    contradiction.md       rapport du relecteur qui défend ses adversaires
    arbitrage.md           arbitrages de l'agent principal
  methode.md               chapitre Méthode (Q6), gabarit _gabarit/methode.md (v2)
  tendances.md             carte des tendances lourdes : traite / nomme / absent (v2)
  article-long.md          l'article soumis à Dilhan, avec ses corrections
  hors-grille.md           thèmes majeurs du programme non traités
```

Chaque fiche `axes/<axe>.md` suit `_gabarit/axes/fiche-axe.md`.

## Fichier transversal

`convergences.md` : relevé, axe par axe, des mesures identiques ou très proches entre deux forces ou plus. Alimenté dès l'étape 2 de chaque verticale.
