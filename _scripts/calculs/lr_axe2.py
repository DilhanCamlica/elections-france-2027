"""Calculs par nos soins de la fiche LR, axe 2 (travail, protection sociale et fraude).

Fiche : 02-partis/lr/axes/2-travail-protection-sociale.md (étapes 3 à 5, 2026-10-27).
Chaque bloc cite la source des données d'entrée (numéro de la liste des sources de la fiche,
ou identifiant du corpus [C-LR-nn]).
Exécution : python3 -I _scripts/calculs/lr_axe2.py
"""


def pct(a, b):
    return 100 * a / b


print("== Mesure structurante : poids des retraites dans la sphère sociale du plan [C-LR-12, p. 2] ==")
sphere = {"retraites": 42, "arrets_maladie": 4, "travail_gagnant": 30, "fraude_sociale": 4, "gestion": 4}
tot = sum(sphere.values())
print(f"Total sphère sociale : {tot} Md€ ; retraites {pct(42, tot):.0f} % ; CSU (10 Md€) {pct(10, tot):.0f} %")

print("\n== Q1. « + 30,8 % » : périmètres (note CSU [C-LR-03] ; Drees, sources 41 à 43) ==")
print(f"Dépense moyenne par allocataire des minima : 5 600 -> 7 300 € : {pct(7300 - 5600, 5600):+.1f} % (arrondis)")
print(f"Dépense des minima sociaux : 21,5 -> 30,6 Md€ : {pct(30.6 - 21.5, 21.5):+.1f} %")
print(f"Prestations de protection sociale : 652,9 (2012) -> 848,9 Md€ (2022) : {pct(848.9 - 652.9, 652.9):+.1f} % (euros courants, deux bases comptables)")
print(f"Minima sociaux / prestations de protection sociale 2022 : {pct(30.6, 848.9):.1f} %")

print("\n== Q1. « 60 % de la dette est de la dette sociale » (Insee, dette fin 2025, source 44) ==")
dette, asso = 3460.5, 293.1
print(f"Dette des administrations de sécurité sociale : {asso} / {dette} Md€ = {pct(asso, dette):.1f} %")

print("\n== Q1. Fraude sociale (HCFiPS, note du 13 janvier 2026, source 38) ==")
print(f"Recouvré / estimé : 0,681 / 14 = {pct(0.681, 14):.1f} % ; détecté / estimé : 2,06 / 14 = {pct(2.06, 14):.1f} %")
print(f"Chiffres du parti : 0,6 / 13 = {pct(0.6, 13):.1f} % (« moins d'un vingtième » : seuil 5 %)")

print("\n== Q1. Assurance chômage (Unédic, panorama de février 2026, source 29) ==")
rc, part = 9.4, 0.261
alloc = rc / part
print(f"Dépenses totales d'allocation 2024 déduites : {rc} / {part} = {alloc:.1f} Md€ ; « 45 Md€ » du plan : {pct(45 - alloc, alloc):+.0f} %")

print("\n== Q1. Seniors 60-64 ans (Dares 2025 via Previssima, source 45) ==")
print(f"Écart revendiqué : 60 - 36 = 24 points ; écart 2025 : 55,0 - 44,4 = {55.0 - 44.4:.1f} points")

print("\n== Q1. Heures (Rexecode via iFRAP, source 47) ==")
ecart_h = 1786 - 1664
print(f"Écart France-Allemagne : {ecart_h} h, soit {ecart_h / 39:.1f} à {ecart_h / 35:.1f} semaines de 39 h ou 35 h")

print("\n== Q1. Retraites : besoin de « 40 Md€ » contre le solde du COR (sources 25, 26) ==")
print(f"40 / 5,1 (COR 2026, 2025) = {40 / 5.1:.1f} ; 40 / 6,6 (Cour, 2025) = {40 / 6.6:.1f}")
print(f"Subventions et contributions d'équilibre 1,9 % du PIB 2025 : {0.019 * 422 / 0.141:.0f} Md€ (PIB déduit de 422 Md€ = 14,1 % du PIB)")

print("\n== Q1. Cas type de Tours [C-LR-02, p. 30 ; C-LR-04] ==")
smic24, smic25 = 1398.69, 1426.30   # Smic net mensuel au 1er janvier 2024 et au 1er novembre 2024 (source 57)
total, legal = 2374.66, 1705.96
print(f"Total / (2 x Smic net 2024) = {pct(total, 2 * smic24):.1f} % ; avec le Smic net de novembre 2024 : {pct(total, 2 * smic25):.1f} %")
print(f"Aides légales (I + II) / (2 x Smic net 2024) = {pct(legal, 2 * smic24):.1f} %")
print(f"Total après plafonnement de 410 € : {total - 410:.2f} € (le livret écrit 1 865 €)")
print(f"Plafond 70 % x 2 adultes : Smic 2024 {0.7 * 2 * smic24:.2f} € (baisse {total - 0.7 * 2 * smic24:.0f} €) ; Smic nov. 2024 {0.7 * 2 * smic25:.2f} € (baisse {total - 0.7 * 2 * smic25:.0f} €)")
seul = 1157.04
print(f"Foyer 1 (personne seule) : {seul} € ; plafond {0.7 * smic25:.2f} € ; écrêtement {seul - 0.7 * smic25:.0f} € par mois ; aides légales seules 874,94 € = {pct(874.94, smic25):.0f} % du Smic net")

print("\n== Q3. Retraites : fiche 6 [C-LR-12, p. 8] ==")
lignes = {"ages": 12.0, "reserves": 7.5, "agirc": 7.2, "cotis1": 6.0, "rafp": 4.3, "regimes_speciaux": 3.0, "fraude": 2.0}
print(f"Somme des lignes : {sum(lignes.values()):.1f} Md€")
print(f"Réserves nécessaires pour 7,5 Md€ à 4,2 % : {7.5 / 0.042:.0f} Md€")
print("Réserves fin 2023 (Cour, source 25) : Agirc-Arrco 101,7 ; RAFP 43,3 ; FRR 21,2 Md€ ; somme",
      f"{101.7 + 43.3 + 21.2:.1f} Md€")
rafp25 = 2.23   # cotisations RAFP enregistrées en 2025 (source 28)
for g in (0.0, 0.02, 0.03):
    v = rafp25 * (1 + g) ** 7
    print(f"Doublement des cotisations RAFP en 2032 (masse +{g:.0%}/an) : +{v:.2f} Md€ ; 4,3 / {v:.2f} = {4.3 / v:.2f}")
print(f"Cotisation de 1 % sur 600 Md€ de masse salariale privée : {600 * 0.01:.1f} Md€")
print(f"Régimes spéciaux : 3,0 Md€ / 6,0 Md€ de subventions 2026 (source 27) = {pct(3.0, 6.0):.0f} %")

print("\n== Q3. 40 Md€ cumulés sur cinq ans [C-LR-82] contre 42 Md€ en 2032 [C-LR-12] ==")
for niveau in (12.0, 42.0):
    cumul = sum(niveau * k / 5 for k in range(1, 6))
    print(f"Montée linéaire sur 5 ans jusqu'à {niveau} Md€ : cumul {cumul:.0f} Md€")

print("\n== Q3. Décote de 7 % par an (calcul illustratif) ==")
pension = 1666   # pension moyenne brute de droit direct, Drees (repris de la fiche RN)
for ans in (1, 2):
    print(f"{ans} an(s) avant 65 ans : -{7 * ans} % = -{pension * 0.07 * ans:.0f} € bruts par mois sur {pension} €")

print("\n== Q3. Ruptures conventionnelles (Unédic, source 29 ; Sénat, source 30) ==")
print(f"7 à 8 Md€ / 9,4 Md€ de dépenses liées : {pct(7, 9.4):.0f} % à {pct(8, 9.4):.0f} %")
borne = 9.4 * (15 - 6) / 15
print(f"Borne statique d'une limite à 6 mois (15 mois indemnisés en moyenne) : {borne:.1f} Md€ (hypothèse uniforme)")
print(f"Avenant n° 3 (15 mois au lieu de 18) : 0,94 Md€ en croisière ; 7 / 0,94 = {7 / 0.94:.1f}")

print("\n== Q3. Règles de juin 2024 : 4 à 5 Md€ contre 3,6 Md€ (ministère du Travail, source 31) ==")
print(f"Écart : {pct(4 - 3.6, 3.6):+.0f} % à {pct(5 - 3.6, 3.6):+.0f} %")

print("\n== Q3. Fonction publique : trois jours de carence (inspections, source 50) ==")
print(f"3,0 Md€ (plan) / 0,289 Md€ (trois jours) = {3.0 / 0.289:.1f} ; / 1,2 Md€ (trois jours + 90 %) = {3.0 / 1.2:.1f}")

print("\n== Q3. Plafond britannique (GOV.UK, novembre 2025, source 48) ==")
uk = 111_000 * 241 * 12 / 1e9
print(f"111 000 foyers x 241 £ x 12 = {uk:.2f} Md£ par an ; CSU 10 Md€ ; ratio pour 1 £ = 1,15 à 1,20 € : {10 / (uk * 1.20):.0f} à {10 / (uk * 1.15):.0f}")

print("\n== Q3. RSA limité à deux ans : 7 Md€ [C-LR-78] contre ≈ 12 Md€ de RSA (Drees 2022, source 41) ==")
print(f"7 / 12 = {pct(7, 12):.0f} %")

print("\n== Effets distributifs : RIA contre RSA 2025 (note RIA [C-LR-03] ; note CSU, montants RSA 2025) ==")
rsa1, fl1 = 646.52, 77.58
rsa2 = rsa1 * 1.5
fl2 = 0.16 * rsa2
print(f"Personne seule avec aide au logement : RSA {rsa1 - fl1:.2f} € ; RIA socle 300 € : {300 - (rsa1 - fl1):+.2f} € ; RIA avec activité 550 € : {550 - (rsa1 - fl1):+.2f} €")
print(f"Couple sans enfant avec aide au logement : RSA {rsa2 - fl2:.2f} € ; 2 x 300 € : {600 - (rsa2 - fl2):+.2f} € ; 2 x 550 € : {1100 - (rsa2 - fl2):+.2f} €")
print("(Hypothèse : aucun forfait logement déduit du RIA, non précisé par la note.)")
