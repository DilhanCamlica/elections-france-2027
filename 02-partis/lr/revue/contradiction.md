# LR : revue contradictoire, rôle « contradiction » (étape 6)

- Date : 2026-10-27
- Données arrêtées au : 2026-10-27
- Corpus arrêté au : 2026-10-27
- Auteur : sous-agent Opus, relecteur contradiction (défendre les adversaires des Républicains : chercher les complaisances, les écarts minimisés, les crans trop favorables au regard de la définition littérale)
- Statut : brouillon, pour arbitrage de l'agent principal
- Version du socle : v2.2 (pondération v2.1 de l'échelle C, bloc d de l'échelle M, précisions du 2026-10-26 et du 2026-10-27, dont la lecture A)
- Fichiers lus : `CLAUDE.md` ; `02-partis/_gabarit/briefs/etape-6-revue.md` ; `01-socle/01-criteres.md` (en entier), `02-registre-biais.md` ; `02-partis/lr/` : les six fiches `axes/*.md` (verdicts, Q4, Q5, « Ce qui tient », divergences), `methode.md`, `tendances.md`, `revue/retours-socle.md` ; corpus relu en texte : [C-LR-12] (fiches 1, 2 et 6, extraction `pdftotext`), [C-LR-03] (note « seuil zéro cotisation », p. 13 à 16), [C-LR-20] (PDF de juillet 2024 et page actuelle), [C-LR-69], [C-LR-72], [C-LR-73], [C-LR-74] ; pour la symétrie : `ps/revue/arbitrage.md` (lignes 1, 7, 10, 11, 13, 14), `rn/revue/arbitrage.md` (règles et table), `rn/axes/3-immigration.md` (verdict C), verdicts E de l'axe 5 du RN et de Renaissance, verdicts D de l'axe 1 de LFI et de Renaissance, `renaissance/revue/arbitrage-v3.md` ; modèles : `ps/revue/contradiction.md`.
- Aucune fiche n'a été modifiée. Ce rapport est le seul fichier écrit dans le dépôt (deux extractions de texte dans le répertoire temporaire de la session, hors dépôt). Calculs refaits en code (`python3`, une ligne, résultats donnés dans le texte).

Sigles : LR (Les Républicains), DR (groupe Droite républicaine), PM (Premier ministre), PLF et PLFSS (projets de loi de finances et de financement de la sécurité sociale), CDHR (contribution différentielle sur les hauts revenus), COR (Conseil d'orientation des retraites), ASSO (administrations de sécurité sociale), LPM (loi de programmation militaire), CSU (compte social unique), ASU (allocation sociale unique), RAFP (retraite additionnelle de la fonction publique), CNCDH (Commission nationale consultative des droits de l'homme), CSM (Conseil supérieur de la magistrature), PJLC (projet de loi constitutionnelle), PIB (produit intérieur brut), Md€ (milliard d'euros).

Convention : « fiche n » renvoie à `axes/n-*.md` au 2026-10-27 ; « [C-LR-nn] » au corpus ; « [Ax-n] » à la source n de la liste de l'axe x en fin de fichier ; « [M-n] » et « [T-n] » aux sources des sections Méthode et Carte.

## Table de synthèse

| Objet | Verdict actuel | Proposition | Force de la preuve |
|---|---|---|---|
| Axe 1, D | 4 | **3** | Moyenne à forte : la « poudrière sociale » est l'une des deux « poudrières » du titre de la fiche 1 du plan ; deux de ses quatre chiffres sont faux ou hors convention d'un facteur 7 et 7,8 ; la fiche 2 compte le même « 60 % » pour descendre au cran 3 (règle 4) |
| Axe 1, F | 3 | Maintien ; motif à compléter (défense hors plan) | Plausible : 100 Md€ de budget des armées promis par le candidat, 76,3 Md€ prévus par la LPM actualisée en 2030 ; le plan ne dit rien de l'écart |
| Axe 1, C | 3 | **2** | Forte par la lettre de la règle v2.1 : « pas d'impôt nouveau » est la promesse centrale nommée par la fiche elle-même ; l'acte de coalition contraire (PLF 2025 d'un PM LR) compte à plein sous la lecture A, quel que soit son âge |
| Axe 1, E | 3 | Maintien | Aucune |
| Axe 2, D, F, E | 3, 3, 3 | Maintien ; F au bord bas du cran 3 | Aucune pour un déplacement |
| Axe 2, C | 3 | **2** | Moyenne : troisième objet, les règles de chômage de juin 2024 non appliquées par la coalition puis promises en 2026 comme « jamais appliquées », même configuration que le récépissé du PS (arbitrage PS, ligne 10, compté en lecture A) |
| Axe 3, D, F, E | 4, 2, 3 | Maintien | Aucune |
| Axe 3, C | 3 | **2** | Moyenne : la « loi immigration » du pacte portait la durée de présence pour les aides, objet principal de la mesure structurante (v2.1, « son objet principal ») ; l'initiative des lois appartenait au PM LR de septembre à décembre 2024 (Constitution, article 39) |
| Axe 4, D, F, E | 4, 3, 3 | Maintien | Aucune |
| Axe 4, C | 3 | **2** | Moyenne : (a) l'autofinancement du seuil repose en entier sur une recette (1,4 Md€) que le livret exclut : sans elle, solde de - 0,05 Md€ ; (b) règle 4 : les hausses d'impôts de 2025 sont comptées à l'axe 1 seulement, alors que la sous-indexation des pensions l'est aux axes 1 et 2 |
| Axe 5, D, F | 3, 2 | Maintien | Aucune |
| Axe 5, C | 3 | **2** | Moyenne à forte par la lettre : la fiche écrit que l'objet « touche l'objet de la mesure structurante » ; v2.1 range « son objet principal » dans le cœur ; la compétence n'était pas seulement celle d'un garde des Sceaux non LR (article 39) |
| Axe 5, E | 4 | Maintien | Lettre du cran 4, symétrie RN et Renaissance |
| Axe 6, D, F, E | 4, 2, 3 | Maintien | Aucune |
| Axe 6, C | 4 | **3** | Plausible : la cour disciplinaire de la magistrature, annoncée par le candidat comme partie de « sa révision constitutionnelle », est absente des deux projets publiés, sans explication |
| Méthode | 3 | Maintien ; **un point à retirer** et un manquement à ajouter | Le « non vérifiable » sur la consultation d'octobre 2025 tombe dans le sens favorable au parti (consultation tenue, 74 % contre, relais unique) ; l'entrée au gouvernement en septembre 2024, deux mois après une déclaration contre les « coalitions », est un second acte de méthode : deux manquements, toujours le cran 3 ; cran 2 seulement si les 49.3 sont lus comme actes contraires à la parole « dernier mot au peuple » (faible) |
| Méthode, bloc (d) | 0 cas | Maintien du compte, réserve sur la collecte | Deux requêtes supplémentaires sans résultat ; Poligraph inaccessible : la comparaison « 0 contre 12 » ne doit pas être publiée sans cette réserve |
| Carte | 8 / 6 / 0 / 0 | **7 / 7 / 0 / 0** (tendance 13 en partie) | Moyenne : le cœur (montant de la dépense de défense) ne figure que dans la couche candidat, et le seul chiffrage du parti (plan de 197 Md€) ne le reprend pas |

Effet si tout était retenu : C 2/2/2/2/2/3 au lieu de 3/3/3/3/3/4 ; D axe 1 à 3 ; M inchangé (3). Tous les déplacements proposés vont contre le parti, sauf la consultation d'octobre 2025, signalée par honnêteté. Trois propositions (axes 1, 3, 5) reposent sur la seule lecture littérale de la règle v2.1 et du retour au socle n° 4 ; elles tombent ensemble si l'arbitrage décide que v2.1 ne vise que les actes postérieurs à la promesse actuelle.

## Question préalable : la règle v2.1 et les actes de coalition (retours au socle n° 2, 4 et 7)

La règle v2.1 (`01-criteres.md` §4) écrit : un décalage documenté qui porte sur « le cœur de cette mesure (son objet principal, son périmètre, son montant global ou son calendrier central) ou sur la promesse centrale de la campagne vaut à lui seul le cran 2 ». La lecture A (précision du 2026-10-27, retour 1) écrit que les actes du mandat exercé comptent « pleinement », « un objet par objet, quel que soit leur âge », et nomme expressément les actes de coalition de LR en 2024-2026. Aucune des deux phrases ne restreint la règle v2.1 aux actes postérieurs à la promesse actuelle. Les fiches 1, 3 et 5 appliquent pourtant une restriction non écrite, de trois façons :

- fiche 1 : la promesse centrale est identique en 2024 et en 2026, mais l'acte contraire « porte sur le programme de 2024 », donc compte comme un objet ;
- fiche 3 : la loi promise « porte sur un instrument de droit constant, pas sur la Charte », alors que l'objet (durée de présence pour les aides) est le même ;
- fiche 5 : l'objet « touche l'objet de la mesure structurante mais pas son cœur », alors que v2.1 définit le cœur par « son objet principal ».

Lecture littérale : les trois actes portent sur la promesse centrale ou sur l'objet principal de la mesure structurante, donc cran 2 aux trois axes. Lecture la plus favorable au parti : la règle ne viserait que les décalages entre le programme actuel et des actes ou textes actuels ; elle n'est écrite nulle part, et les arbitrages PS et Renaissance n'ont pas eu à la trancher (aucune de leurs promesses centrales actuelles n'avait été contredite par un acte de leur mandat). La décision de principe revient à Dilhan (point d'arrêt 2) ; ce rapport montre que, si elle n'est pas prise, la lettre du socle donne le cran 2.

Deuxième point de principe, propre aux axes 3 et 5 : les fiches excusent la non-présentation des lois promises par la position minoritaire de LR dans la coalition. C'est inexact pour la période du gouvernement Barnier (21 septembre au 13 décembre 2024) : « L'initiative des lois appartient concurremment au Premier ministre et aux membres du Parlement » (Constitution, article 39, alinéa 1) et « Le Premier ministre dirige l'action du Gouvernement » (article 21) [A5-1, page ouverte]. Pendant ces trois mois, le PM LR avait seul l'initiative des projets de loi ; le groupe DR avait en outre l'initiative des propositions pendant toute la période. L'explication « compétence d'un ministre non LR » ne vaut que pour la période Bayrou.

## Axe 1 : Finances publiques et dette

**D, cran 4, proposé 3.** Définition du cran 3 : « le constat est exact sur une partie du périmètre et faux ou non établi sur une autre ». La fiche 1 du plan s'intitule « deux poudrières » [C-LR-12, p. 3] : la poudrière budgétaire (dette, déficit, intérêts, taux) et « la poudrière sociale », quatre chiffres en une puce. Deux de ces quatre sont faux ou reposent sur une convention que la statistique de niveau 2 ne retient pas : « 60 % de la dette est de la dette sociale » contre 8,6 % (Insee, facteur 6,98) ; « au moins 40 Md€ par an » manquent aux retraites contre 5,1 Md€ (COR, facteur 7,84) ; le troisième (16 Md€ de déficit de l'assurance maladie) n'est pas vérifié par la fiche (calculs par nos soins, sources de la fiche 1, [23], [24], [42]). La fiche juge ce volet « secondaire (une phrase de la fiche 1, sans chiffrage qui en dépende) ». C'est inexact sur le second point : les 40 Md€ sont le « Pourquoi » de la fiche 6 du plan, la réforme des retraites de 42 Md€ [C-LR-12, p. 8], mesure structurante de l'axe 2. Règle 4 (le même fait se lit de la même façon sur deux axes) : la fiche 2 descend au cran 3 en écrivant que le cran 4 est écarté parce que « 60 % de la dette » est faux d'un facteur 7 ; la phrase est la même, dans le même document. Le précédent LFI (arbitrage LFI, axe 1, D 4) ne s'applique pas : le chiffre de fraude contesté y était étranger au diagnostic de l'axe et au plan ; ici, la poudrière sociale est la moitié du titre du diagnostic. Le précédent Renaissance (« deux tiers de la dette », cran 4) portait sur une **cause** tirée d'un essai, non vérifiable ; ici il s'agit de **constats** chiffrés, vérifiés et faux. La poudrière budgétaire reste exacte : pas de cran 2.

**F, cran 3, maintien ; motif à compléter.** Le candidat porte le budget des armées à « 100 milliards d'euros à la fin du quinquennat » [C-LR-72] ; la LPM actualisée (loi n° 2026-791 du 16 août 2026) prévoit 76,3 Md€ en 2030, 63,4 Md€ au PLF 2027 [A1-1, page ouverte ; A1-2, vue en résultat]. Écart en fin de trajectoire : environ 23,7 Md€ (calcul par nos soins, horizons 2030 et 2032 mêlés), du même ordre que la marge du plan sur l'effort que la DG Trésor juge nécessaire (146 contre 125 Md€, soit 21 Md€). Le plan ne mentionne pas la défense [C-LR-12, extraction complète : une seule occurrence, au diagnostic]. On ignore si le tendanciel repris de la mission Jaravel-Ragot-Tavernier-Valla inclut la LPM actualisée : non tranché, d'où « plausible ». Sous 1 % du PIB, le cran 1 n'est pas atteint ; le motif doit dire qu'une promesse du candidat de l'ordre de 0,6 % du PIB n'est pas dans la trajectoire, et la fiche 1 (« Q3 ») doit cesser d'écrire que la ligne 97 est un simple « coût du rattrapage non chiffré ».

**C, cran 3, proposé 2.** Définition du cran 2, étendue par v2.1 : un décalage documenté sur « la promesse centrale de la campagne vaut à lui seul le cran 2 ». La fiche nomme elle-même cette promesse : refus de toute hausse d'impôt, « constant de juillet 2025 à octobre 2026 », et « Il n'y aura pas d'impôt nouveau » à la présentation du plan (fiche 1, Q4). Le pacte de juillet 2024 écrit la même ligne rouge, « aucune augmentation des impôts » [C-LR-20, PDF, p. 1 ; C-LR-19, p. 6]. L'acte : un PLF déposé par un PM LR, dont un tiers de l'effort par des hausses d'impôts, puis une loi de finances qui en institue 23 Md€ (Cour des comptes, fiche 1 [27]) ; le groupe s'abstient sur la CDHR (scrutin 21, 3 pour, 1 contre, 9 abstentions). Sous la lecture A, cet acte compte « pleinement », sans pondération par l'âge. Il porte sur le contenu même de la promesse centrale, pas sur une ligne secondaire. Par la lettre, cran 2, sans même compter le second objet (pensions). La fiche le reconnaît comme cas limite (a) et retour n° 4 ; elle retient la lecture favorable sans base écrite (voir la question préalable).

**Cas limite (d) de la fiche, à requalifier en constat.** Le plan compte 6,0 Md€ de « cotisation dédiée de 1 % du salaire brut », assise sur la « masse salariale privée ≈ 600 Md€ », et 4,3 Md€ de RAFP doublée, parmi les « économies » [C-LR-12, p. 8]. Une cotisation de 1 % sur toute la masse salariale privée est obligatoire par construction (sinon l'assiette serait moindre) : c'est un prélèvement obligatoire nouveau au sens de l'Insee, même si ce n'est pas un « impôt » au sens juridique. Pas proposé comme objet (la promesse dit « impôt »), mais « Ce qui tient » ne peut pas écrire « cap sans impôt nouveau » sans ajouter « avec 10,3 Md€ de cotisations nouvelles ».

**« Ce qui tient » à resserrer.** (1) « La troisième ligne rouge, l'arrêt de la dégradation des comptes, a été tenue en 2025 » : la fiche écrit elle-même en Q4 qu'elle l'a été « par l'impôt (objet n° 1) », la Cour disant « exclusivement ». Tenue contre la première ligne rouge : à écrire dans la même phrase. (2) « Ses hypothèses de croissance sont prudentes » : vrai, mais la même phrase doit citer les deux hypothèses favorables que la fiche relève en Q3 (ajustement stock-flux nul, soit 2,3 points de dette en 2032 ; trajectoire 0,9 point au-dessus de l'engagement européen de 2029).

## Axe 2 : Travail, protection sociale et fraude

**F, cran 3, maintien.** L'écart établi va de 12 % à 31 % ; la borne basse est sous la bande du cran 3 (30 % à 100 %), la borne haute dedans. Le cran 3 tient par la définition, sans marge. À noter pour le motif : la ligne « produits financiers des réserves » (7,5 Md€) suppose environ 179 Md€ placés en plus ; les réserves nouvelles que le plan crée (cotisation de 6,0 Md€ par an) n'en accumulent qu'une trentaine en cinq ans, d'où une ligne surévaluée d'un facteur proche de 5 si elles sont la seule source (ordre de grandeur par nos soins, à refaire en code par l'agent d'application). Un non vérifiable n'est pas faux (règle 3) : les 19 Md€ ne déplacent pas le cran.

**C, cran 3, proposé 2.** Définition du cran 2 : « décalage net sur plusieurs objets (trois ou plus) ». La fiche compte deux objets (ASU du groupe contre CSU du parti ; pensions sous l'inflation au 49.3 de décembre 2024). Troisième objet proposé : la fiche décrit elle-même que le programme de 2026 demande d'appliquer les règles d'assurance chômage de juin 2024, « jamais appliquées » [C-LR-02, p. 31], règles que le gouvernement de coalition « a choisi de ne pas appliquer, sans le dire » (fiche 2, actes de coalition, ligne 2). La fiche l'écarte faute de promesse de l'époque et le renvoie à la Méthode. Or l'arbitrage PS compte, sous la lecture A, le récépissé de contrôle d'identité : « refusé par le gouvernement [...] en février 2016, promis à nouveau en 2026 sans explication du changement : sous la lecture A, un objet » (`ps/revue/arbitrage.md`, ligne 10). La configuration est la même : acte de gouvernement contraire à la position actuelle, sans explication du changement. Précision factuelle : la réforme de juin 2024 avait été suspendue par le gouvernement Attal le 30 juin 2024 ; le PM LR a ensuite rendu la main aux partenaires sociaux dans sa déclaration de politique générale, et l'arrêté d'agrément de décembre 2024 a validé une convention différente [A2-1, vu en résultat ; fiche 2, [32], [33]]. L'acte de coalition est donc la non-reprise et l'agrément d'autres règles, pas la suspension. Trois objets, aucun au cœur de la réforme des retraites : cran 2 par le nombre. Force moyenne : la réponse attendue est que le parti a changé d'avis (règle 11) ; mais la règle 11 vise une évolution entre deux textes du parti, pas un acte de gouvernement contraire.

**Second point sur l'ASU (règle 11).** La fiche a raison de compter l'objet ; la lecture alternative (« étiquette du plafond ») ne tient pas, puisque le parti écrit en janvier 2026 que l'ASU « n'est pas la bonne réponse » [C-LR-03, note CSU, p. 12] et que l'orateur du groupe défend en séance « notre proposition d'une allocation sociale unique » [C-LR-80]. Position du groupe tenue en même temps que celle du parti : objet, lettre de la règle 11.

**E, cran 3, maintien ; une ligne à corriger.** « Garder des retraites et une assurance maladie essentiellement publiques » est classée « traitée » alors que le plan ajoute un pilier de capitalisation qui ferait un quart de la retraite des jeunes (relais [C-LR-82]). Statut juste : « traitée en partie, va contre en partie en l'assumant ». Sans effet sur le cran.

**« Ce qui tient » à resserrer.** « Une réforme qui avantage nommément les carrières incomplètes à 65 ans » : à mettre en regard, dans la même phrase, de la décote de 7 % par année avant 65 ans, qui recule le départ sans décote pour les autres.

## Axe 3 : Immigration

**C, cran 3, proposé 2.** Définition v2.1 : un décalage documenté sur « son objet principal » vaut le cran 2. Mesure structurante : la Charte républicaine, dont l'article 12 permet de subordonner les prestations à cinq ans de résidence [C-LR-14, art. 12]. La « loi immigration » du pacte de 2024, annoncée par le gouvernement Barnier le 14 octobre 2024 et jamais déposée, comprenait « durée de présence pour certaines aides » (fiche 3, Q4, actes de coalition, ligne 5 ; [C-LR-19, p. 3, 7]) : c'est l'objet principal de la mesure structurante, à droit constant. La fiche l'écarte du cœur parce qu'il s'agit « d'un instrument de droit constant, pas [de] la Charte » ; v2.1 parle de l'objet, pas de l'instrument. L'explication par le refus du PM Bayrou ne couvre pas la période Barnier : de l'annonce (14 octobre) à la censure (4 décembre), le PM LR avait l'initiative (article 39) [A5-1]. Le texte sénatorial de deux ans, adopté le 18 mars 2025, n'a pas été inscrit à l'Assemblée pendant la participation, ni sur une journée réservée du groupe [C-LR-84] (recherche sur l'inscription non faite ici : point non vérifiable). Force moyenne : le calendrier annoncé (« début 2025 ») dépassait la durée du gouvernement Barnier.

**Cinq ans contre deux ans : maintien de la lecture « nuance », avec une réserve.** Le livret « Famille » pose cinq ans d'activité pour le revenu familial sans mentionner de révision [C-LR-07, p. 4, 11] ; le président du groupe demande deux ans au PLF 2027 [C-LR-78]. Lus tous deux à droit constant, ce seraient deux positions tenues en même temps sur un même objet (règle 11). La fiche lit le livret comme un silence sur la voie ; c'est défendable, mais le cas limite doit rester écrit.

**Asile « hors des frontières ».** Le plan compte 0,9 Md€ « après la révision constitutionnelle » ; la révision publiée ne le prévoit pas. La fiche lit un silence (C) et un cran 1 (F, mesure secondaire). Cohérent avec la règle du silence ; « Ce qui tient » (« Le parti nomme l'obstacle et écrit la voie ») doit ajouter que ce n'est pas vrai pour l'asile.

**Q3, chiffrage.** Les deux bases du chiffrage de 10 Md€ sont de niveau 4 et d'un seul bord (OID, classé à droite ; Institut Montaigne, classé libéral) ; la fiche le dit et ne leur fait pas décider du cran. Conforme (registre, ligne 8) ; « Ce qui tient » (« sourcé ligne à ligne ») doit garder la mention « base surtout un think tank engagé », déjà présente.

## Axe 4 : Pouvoir d'achat et fiscalité

**C, cran 3, proposé 2.** Deux arguments indépendants.

(a) **L'autofinancement de la mesure structurante repose sur une recette que le programme exclut.** La note chiffre un coût brut de 3 649 M€ et trois recettes : 2,6 Md€ (heures nouvelles des salariés qui n'en font pas), 1,4 Md€ par « la suppression de l'exonération fiscale » des heures supplémentaires, 1,0 Md€ (cotisations sur les 16 heures intégrées) [C-LR-03, note seuil, p. 14-15, relue]. Le livret maintient cette exonération « intégralement » [C-LR-02, p. 21]. Solde affiché : + 1,351 Md€ ; sans la recette exclue : - 0,049 Md€ ; sans elle et sans l'hypothèse de comportement : - 2,649 Md€ (calculs par nos soins). Le plan classe la mesure parmi les 14 Md€ « autofinancés » [C-LR-12, p. 16]. Le décalage entre deux textes du programme porte donc sur le montant global (le financement) de la mesure structurante, que v2.1 range dans le cœur. La fiche le traite en cas limite (b), « non tranché », et le range en F parce que « la comparaison 1 oppose le discours au programme ». Le candidat présente la mesure dans les mêmes termes que le livret [C-LR-67 ; C-LR-76] : c'est bien un écart entre discours et programme chiffré. Réserve honnête (registre, ligne 18) : l'argument utilise la transparence de la note ; il ne compte pas des lignes contestables, il oppose deux textes du parti sur une même recette.

(b) **Règle 4.** La sous-indexation des pensions est comptée à l'axe 1 (objet n° 2) et à l'axe 2 (objet n° 2). Les hausses d'impôts de la loi de finances pour 2025 (CDHR, surtaxe sur les bénéfices, TVA des abonnements d'électricité) relèvent pourtant de l'axe 4 (« impôt sur le revenu, TVA [...] énergie », `01-criteres.md` §2) et n'y sont « pas comptées une seconde fois » (fiche 4, actes de coalition). Un même acte se lit de la même façon sur deux axes : soit les deux actes sont comptés sur leurs deux axes (axe 4 : trois objets, cran 2), soit aucun (axe 2 : un objet de moins). La lecture qui compte l'un et pas l'autre favorise le parti sur l'axe où il est le plus exposé.

Avec (a) seul, l'axe passe au cran 2 par v2.1 ; avec (b) seul, au cran 2 par le nombre. L'objet 8854 (quatre votants) peut tomber sans changer ce résultat.

**« Ce qui tient » à resserrer.** « Le groupe [...] a voté contre la réduction des allègements de cotisations voulue par un gouvernement dirigé par un Premier ministre LR, ce qui montre une ligne tenue contre son propre camp » : le même groupe s'abstient sur la CDHR (scrutin 21) et ne s'oppose pas à la loi finale ; la phrase doit le dire. « Transparence rare » : à garder.

## Axe 5 : Sécurité, ordre public et libertés

**C, cran 3, proposé 2.** Définition v2.1 : le cœur comprend « son objet principal ». Mesure structurante : les peines minimales obligatoires. La « loi sécurité justice », première des treize lois du pacte, avait les peines planchers « en tête » (fiche 5, Q4). La fiche écrit que l'objet d'écart « touche l'objet de la mesure structurante mais pas son cœur », en définissant le cœur par trois critères absents du socle : « ni le périmètre ni le contenu de la promesse n'ont changé », « le parti ne l'a contredite par aucun vote ni acte », « la compétence était celle d'un ministre non LR ». Le premier critère confond cœur et changement de position ; le deuxième ferait de toute promesse non réalisée un non-écart ; le troisième est inexact pour la période Barnier (article 39 [A5-1]). Le groupe, lui, n'a déposé sa PPL sur les peines minimales (n° 3335) que le 13 octobre 2026, deux ans après le pacte et un an après la sortie du gouvernement, alors qu'il déposait dès décembre 2024 celle sur la présomption de légitime défense (fiche 5, actes de coalition). Lettre de v2.1 : cran 2. La fiche signale elle-même cette lecture (retour n° 7). Force moyenne à forte par la lettre ; elle tombe avec la question préalable si l'arbitrage restreint v2.1.

**Dissolution de LFI et état d'urgence.** La fiche les lit comme « ajouts sans poids propre ». Le socle range les positions sur le pluralisme à l'axe 6 et en Méthode (a) (`01-criteres.md`, bloc d, règle 5, dernière phrase). La recommandation par le candidat de dissoudre le premier groupe d'opposition de gauche [C-LR-88] doit être documentée à l'axe 6 (Q2 et angles morts) et en Méthode (a), pas seulement à l'axe 5. Sans effet de cran : une parole, pas un acte, et aucun engagement contraire.

**E, cran 4, maintien.** Une seule demande de premier rang, traitée ; les demandes « fortes » ne comptent pas pour le cran (Renaissance et RN, même lecture). Le retrait sans explication, le 1er septembre 2026, de la sanction des agents ayant fait un usage « manifestement abusif » de leurs prérogatives [C-LR-14, V310826, p. 3] est déjà écrit ; il pèse sur la lecture, pas sur le cran.

**« Ce qui tient » à resserrer.** « La ligne est constante depuis 2022 » : à compléter par « sans que le gouvernement dirigé par un PM LR, puis le groupe pendant la coalition, ne dépose de texte sur les peines minimales ».

## Axe 6 : Institutions, démocratie et Europe

**C, cran 4, proposé 3.** Définition du cran 3 : « décalage documenté sur un ou deux objets » ; le cran 4 est « réservé aux nuances de calendrier ou d'ampleur, sans décalage sur un objet » (précision du 2026-10-26). Le 6 juin 2026, le candidat propose de remplacer le CSM, pour la discipline, par une cour disciplinaire avec des citoyens tirés au sort, et dit que cela ferait partie de sa révision constitutionnelle [C-LR-69, paraphrase de la fiche ; citation : « créer une cour disciplinaire de la magistrature à la place du CSM »]. Les deux projets publiés fin août et début septembre n'en contiennent rien [C-LR-13 ; C-LR-14]. La fiche lit un « silence du texte écrit ». Or l'objet n'est pas une mesure que le texte tait : c'est le contenu de la mesure structurante elle-même (la révision), que le candidat décrit d'une façon et que le texte écrit d'une autre, sans explication. Décalage sur le périmètre de la révision. Force plausible : la règle du silence est la lecture concurrente, et le candidat n'a pas réitéré la mesure après la publication (recherche non faite). Cran 2 non proposé : la révision publiée garde son objet principal (dernier mot au peuple, primauté).

**Espagne : maintien de la lecture de la fiche.** Le communiqué du 31 juillet demande « la suspension de la libre circulation des personnes avec l'Espagne » et le rattache à la position italienne sur Schengen [C-LR-73] ; l'entretien du 2 août réserve la libre circulation de Schengen aux Européens [C-LR-74]. Relus en entier, les deux textes parlent de Schengen et du contrôle aux frontières ; le communiqué ne vise pas expressément le droit au séjour des citoyens de l'Union. Pas d'objet établi.

**49.3 Barnier : formulation à corriger, pas le cran.** La fiche écrit « Concorde » en s'appuyant sur une demande de 49.3 postérieure d'un an à l'acte [C-LR-85]. Une position postérieure ne peut pas établir la concordance d'un acte antérieur (retour n° 6) ; sans engagement, l'acte est « sans objet » à l'échelle C. Même cran.

**« Ce qui tient » à resserrer.** « Les votes du groupe [...] concordent » : sur les trois scrutins exploitables, le groupe vote à 11 sur 48 (4244), à 15 sur 48 et « divisé » par la règle (8611), à 4 sur 48 (5313) ; la phrase doit donner ces participations (registre, ligne 12).

## Méthode (`methode.md`)

**Un « non vérifiable » tombe, en faveur du parti.** La consultation des adhérents annoncée le 13 octobre 2025 a eu lieu selon Europe 1 : « pas moins de 74% des encartés LR se sont prononcés contre cette participation », consultation tenue « en début de semaine », article du 16 octobre 2025 [M-1, page ouverte] ; le parti n'a pas participé au gouvernement Lecornu II, et les six membres entrés au gouvernement ont été déclarés hors du parti [C-LR-24]. Relais unique, sans taux de participation : règle 5, le chiffre ne déplace rien, mais l'engagement « votre choix devra être respecté » paraît tenu. Le chapitre doit retirer la phrase « Si l'étape 6 établit qu'elle n'a pas eu lieu, c'est un second manquement » et classer la consultation en « tenue (relais unique) ».

**Un manquement à ajouter : l'entrée au gouvernement de septembre 2024.** La déclaration du groupe de juillet 2024 écrit que « les coalitions contre nature » ne représentent « une quelconque solution » et se définit comme « groupe d'opposition responsable » [C-LR-20, PDF, p. 1, relu]. Deux mois plus tard, les députés DR « ont validé le principe » d'une participation, sans délibération d'instance du parti trouvée (méthode, bloc b, ligne 1), et le groupe a réécrit sa déclaration (version actuelle du site : soutien à « un Premier ministre issu de la droite républicaine ») [C-LR-20, page]. Ce n'est pas un engagement explicite au sens du socle (pas de « nous ne participerons pas ») ; c'est une formule d'intention, et « les actes de méthode qui la contredisent comptent pour eux-mêmes » (`01-criteres.md`, échelle M, précision du 2026-10-25). Le chapitre range le changement en « précision successive » (fiche 6) : la définition de la précision successive vaut pour les divergences de programme, pas pour un acte de méthode. Proposé comme second manquement, expliqué (« une vraie politique de droite »).

**Effet : maintien du cran 3.** Deux manquements documentés et expliqués : lettre du cran 3. Le cran 2 supposerait un troisième objet ; seul candidat, les cinq 49.3 de la coalition lus comme contraires à la parole de « dernier mot au peuple » : c'est une formule d'intention, et les 49.3 ont porté sur des textes financiers en majorité relative ; pour le PS, les 49.3 de 2016 n'ont pas été comptés comme manquements (contexte, plus de dix ans) ; le traitement des 49.3 dans les six objets de Renaissance n'a pas été relu ici. Argument faible, signalé sans proposition.

**Bloc (d), maintien du compte (0 cas), réserve à écrire.** Deux requêtes supplémentaires en mode approfondi (« élu Les Républicains condamné provocation à la haine raciale définitivement conseiller municipal LR » ; « Les Républicains suspend OR exclut élu propos [...] 2021 OR 2022 OR 2023 OR 2025 ») ne renvoient à aucun cas LR admissible ; le seul cas de 2024 relevé (Meurthe-et-Moselle, et une seconde investiture de l'alliance Ciotti) est déjà traité comme hors périmètre [M-2, vu en résultat]. La base Poligraph, qui a une page des condamnations d'élus locaux LR, n'a pas répondu (erreur 429, chapitre) : la collecte ne peut pas être dite complète. Le chapitre écrit déjà que comparer 0 à 12 (RN) reviendrait à comparer l'attention de la presse ; la page ne doit publier aucun chiffre comparatif sans cette réserve et sans la mention « Poligraph non interrogé ». Cas limite des propos de juillet 2023 (retour n° 11) : la précision ii inclut les propos visant un groupe « à raison de l'origine » ; « régression vers les origines ethniques » attribue un comportement à un groupe défini par l'origine. Admis comme maintien, ce serait un fait au tableau, sans objet de rupture (aucun engagement explicite) : sans effet de cran, mais la lecture « hors périmètre » est la plus favorable des deux et doit être arbitrée pour les cinq forces.

**« Ce qui tient » à resserrer.** « Une démocratie interne pratiquée » : à compléter par la consultation d'octobre 2025 (relais unique) et, dans la même phrase, par l'entrée au gouvernement de 2024 décidée par les parlementaires sans vote d'instance trouvé.

## Carte des tendances (`tendances.md`)

**Tendance 13 (défense), « traitée », proposé « traitée en partie ».** Règle de l'arbitrage (« traitée » exige le cœur de la tendance et une pièce de 2024 ou plus récente) et règle des couches (« le parti d'abord », fiche). Le cœur de la tendance est la hausse des dépenses de défense ; la seule mesure qui le chiffre (100 Md€ en fin de quinquennat) est dans la tribune du candidat [C-LR-72] ; les pièces du parti disent « préserver » la LPM (pacte, 2024) et multiplier par cinq les moyens de l'IA de défense (livret IA) ; le plan de 197 Md€, seul chiffrage du parti pour le quinquennat, ne mentionne pas la défense [C-LR-12]. Le président du parti étant le candidat, la couche candidat est forte ; mais une mesure absente du seul document chiffré du parti, et sans effet dans sa trajectoire, ne répond pas au cœur au niveau du parti. Force moyenne : la fiche signale elle-même le rattachement comme discutable.

**Tendance 6 (IA), maintien « traitée ».** Une seule pièce, mais un livret dédié de 2026 qui répond au cœur (formation, reconversion, observatoire) : la règle n'exige pas deux pièces.

**Tendance 2 (démographie), maintien** par symétrie avec le RN, comme le dit la fiche.

## Q5 transversal

- Aucune ligne « traitée » ne repose sur une mesure de 2022 seule : la règle des mesures vivantes est appliquée (axe 5, moyens).
- Contre-pieds « assumés » : chacun est adossé à une déclaration datée (axes 1, 2, 4) ou à un vote du groupe ; conforme.
- Une ligne à corriger : axe 2, « retraites essentiellement publiques » (voir plus haut), sans effet de cran.
- Les crans E (3, 3, 3, 3, 4, 3) sont ceux des autres forces, sans asymétrie trouvée.

## Registre des biais, lignes surveillées

| Ligne | Constat pour LR |
|---|---|
| 1 Sélection des scrutins | 8854 est un scrutin de réserve à quatre votants ; il porte un objet d'écart à l'axe 4. Sans lui, la proposition de cran 2 à l'axe 4 tient (arguments a et b) |
| 2 Pouvoir et opposition | LR a treize mois d'actes, dont trois à Matignon. Les fiches excusent plusieurs actes par la position minoritaire de LR ; c'est inexact pour la période Barnier (article 39) |
| 3 Textes globaux | Appliqué |
| 4 Biais des modèles | Les restrictions non écrites de v2.1 (question préalable) jouent toutes dans le même sens |
| 8 Chiffrage à sens unique | Immigration : les deux bases du parti sont de droite ou libérales ; présentées comme telles |
| 10 Parti et candidat | Président du parti et candidat confondus : la carte attribue au parti une mesure de défense que seule la couche candidat porte |
| 12 Généralisation à partir d'un vote | Axe 6 : trois scrutins exploitables à 4, 11 et 15 votants |
| 17 Cas individuels | Collecte du bloc (d) incomplète (Poligraph) : réserve à écrire |
| 18 Transparence pénalisée | L'argument (a) de l'axe 4 utilise la note du parti ; il oppose deux textes sur une même recette, il ne compte pas des lignes |

## Cherché sans trouver

- Un texte du parti ou du groupe réitérant, après septembre 2026, la cour disciplinaire de la magistrature (non cherché sur pièce : recherche à faire par l'agent d'application).
- Une source officielle du parti publiant le résultat de la consultation d'octobre 2025 (seul Europe 1 trouvé ; une recherche sur « 74 % » n'a pas trouvé de second relais).
- Une décision formelle du gouvernement Barnier écartant les règles de chômage de juin 2024 (la suspension date du gouvernement Attal ; le retour à la négociation, de la déclaration de politique générale du PM LR).
- Un cas LR admissible au bloc (d) sur 2017-2026 (deux requêtes supplémentaires).
- L'hypothèse de défense du tendanciel de la mission Jaravel-Ragot-Tavernier-Valla (rapport non ouvert, comme pour la fiche 1).

## Points non vérifiables

- Taux de participation et chiffre exact de la consultation des adhérents d'octobre 2025 (relais unique).
- Inscription ou non de la PPL sénatoriale de deux ans (n° 299) à l'ordre du jour de l'Assemblée et refus éventuel d'une journée réservée du groupe pendant la coalition.
- Écart exact entre la défense promise par le candidat (100 Md€ en 2032) et le tendanciel du plan : horizons différents (LPM à 2030).
- Montant des réserves que le plan suppose pour la ligne de 7,5 Md€ (ordre de grandeur seulement).

## Sources

### Axe 1

1. Ministère des Armées, « Actualisation de la loi de programmation militaire : aller plus vite, plus loin », 2026-04-09. https://www.defense.gouv.fr/actualites/actualisation-loi-programmation-militaire-aller-plus-vite-plus-loin [page ouverte le 2026-10-27 ; 57,1 Md€ en 2026, 63,4 Md€ au PLF 2027, 76,3 Md€ en 2030]
2. Légifrance, loi n° 2026-791 du 16 août 2026 actualisant la programmation militaire pour les années 2024 à 2030. https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054694832 [vue en résultat, page non ouverte]
3. Les Républicains, « Rétablir l'ordre dans les comptes publics », fiches presse, 2026-10-12 [C-LR-12], fiches 1, 2 et 6, texte extrait par `pdftotext`. [source du parti, partie prenante]
4. Calculs par nos soins (`python3`) : 60 / 8,6 = 6,98 ; 40 / 5,1 = 7,84 ; 100 - 76,3 = 23,7 ; 146 - 125 = 21.

### Axe 2

1. LégiSocial, « Assurance chômage : le projet de décret a été dévoilé par le Gouvernement ». https://www.legisocial.fr/actualites-sociales/6748-assurance-chomage-projet-decret-devoile-gouvernement.html [vue en résultat, page non ouverte ; suspension de la réforme annoncée le 30 juin 2024]
2. `02-partis/ps/revue/arbitrage.md`, ligne 10 (récépissé, lecture A).

### Axe 3 et axe 5

1. Conseil constitutionnel, texte intégral de la Constitution du 4 octobre 1958 en vigueur, articles 20, 21 et 39. https://www.conseil-constitutionnel.fr/le-bloc-de-constitutionnalite/texte-integral-de-la-constitution-du-4-octobre-1958-en-vigueur [page ouverte le 2026-10-27]

### Axe 4

1. Les Républicains, note technique « Seuil zéro cotisation », janvier 2026 [C-LR-03], p. 13 à 16, texte extrait par `pdftotext`. [source du parti, partie prenante]
2. Calculs par nos soins (`python3`) : 2,6 + 1,4 + 1,0 - 3,649 = 1,351 ; sans 1,4 : - 0,049 ; sans 1,4 ni 2,6 : - 2,649.

### Méthode

1. Europe 1, « Avec la non-censure actée du gouvernement Lecornu, Les Républicains sont plus divisés que jamais », 2025-10-16. https://www.europe1.fr/politique/avec-la-non-censure-actee-du-gouvernement-lecornu-les-republicains-sont-plus-divises-que-jamais-792907 [page ouverte le 2026-10-27 ; radio du groupe Lagardère, classée à droite]
2. Wikipédia, « Crise de 2024 au parti Les Républicains ». https://fr.wikipedia.org/wiki/Crise_de_2024_au_parti_Les_R%C3%A9publicains [vue en résultat, page non ouverte ; pointeur seulement]
3. Groupe Droite républicaine, déclaration politique, 2024-07-19 [C-LR-20], PDF relu le 2026-10-27, et version actuelle du site. [source du parti, partie prenante]
4. Les Républicains, « Les Républicains refusent de participer au gouvernement Lecornu », 2025-10-12. https://republicains.fr/actualites/2025/10/12/les-republicains-refusent-de-participer-au-gouvernement-lecornu/ [vue en résultat, page non ouverte ; source du parti]

### Carte

1. Bruno Retailleau, tribune du 2026-07-14 [C-LR-72], fiche relue. [source du parti, partie prenante]
2. [C-LR-12], extraction complète : aucune occurrence de la défense hors du diagnostic (fiche 1).
