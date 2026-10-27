"""Calculs par nos soins de la fiche PS, axe 2 (travail, protection sociale et fraude).

Fiche : 02-partis/ps/axes/2-travail-protection-sociale.md (étapes 3 à 5, 2026-10-27).
Chaque bloc cite la source des données d'entrée (numéro de la liste des sources de la fiche).
Exécution : python3 _scripts/calculs/ps_axe2.py
"""
from datetime import date


def pct(a, b):
    return 100 * a / b


print("== Q1. Pauvreté (Insee IP 2117, source 32) ==")
pauvres_2024, pauvres_2017 = 9_817_000, 8_572_000
print(f"Hausse 2017-2024 : {pauvres_2024 - pauvres_2017:,} personnes")

print("\n== Q1. Écart de pension de droit direct femmes / hommes (Drees, source 33) ==")
print("Écart publié : 38 % (sans réversion), 25 % (avec) ; le parti écrit « près de 40 % »")

print("\n== Q1. Plus de 75 ans en 2050 (Insee, projections base 2013, source 34) ==")
print(f"74,0 M x 16,3 % = {74.0 * 0.163:.1f} millions")

print("\n== Q1. Part des revenus du travail dans les recettes ROBSS + FSV 2025 (CCSS mai 2026, source 35) ==")
total = 644_392            # M€, total des produits nets 2025
cotis = 315_654            # cotisations sociales
cotis_equilibre = 50_363   # cotisations d'équilibre de l'employeur (fonctions publiques)
cotis_etat = 6_892         # cotisations prises en charge par l'État (exonérations compensées)
csg_robss = 131_001        # CSG affectée aux ROBSS et au FSV
csg_act, csg_brute = 110_670, 157_207  # CSG sur revenus d'activité / CSG brute toutes affectations
csg_act_robss = csg_robss * csg_act / csg_brute  # hypothèse : même part d'activité dans la CSG affectée
travail = cotis + cotis_equilibre + cotis_etat
print(f"Cotisations seules : {pct(travail, total):.1f} %")
print(f"Cotisations + CSG d'activité (hypothèse de prorata) : {pct(travail + csg_act_robss, total):.1f} %")

print("\n== Q1. Fraude (HCFiPS 2026, source 49 ; orateur du groupe [C-PS-76]) ==")
print(f"Détecté / estimé : {pct(2.06, 14):.1f} % ; rapport 100 / 2 = {100 / 2:.0f}")

print("\n== Q1. PLF et PLFSS 2027, effort sur les ménages (OFCE, source 37) ==")
effort, part_aisee = 8.7, 0.64
print(f"Moitié modeste : {effort * (1 - part_aisee):.1f} Md€ sur {effort} Md€ ; avec IJ : 10,2 Md€")

print("\n== Q3. Retour à 62 ans : coût rapporté au PIB ==")
pib_2025 = 152.5 / 0.051  # Md€, déficit 2025 et ratio (briefing §3.3)
print(f"PIB 2025 implicite : {pib_2025:.0f} Md€")
for lib, x in [("Cour, retraites, 2035, retour à 62 ans", 10.4),
               ("Cnav, abrogation, 2032", 16.0),
               ("Cour, finances publiques, 2 x 13,0 (extrapolation)", 26.0)]:
    print(f"{lib} : {x} Md€ = {pct(x, pib_2025):.2f} % du PIB")
print(f"Cohérence Cour : 2 x 5,8 = {2 * 5.8:.1f} Md€ contre 10,4 publiés")

print("\n== Q3. Suspension 2026 : chiffrage du groupe contre gouvernement (source 39) ==")
print(f"0,5 contre 0,4 Md€ : écart {pct(0.5 - 0.4, 0.4):+.0f} %")

print("\n== Q3. ASPA au seuil de pauvreté (PPL n° 3267 ; Drees, sources 42-44) ==")
seuil_seul, seuil_couple = 16_044 / 12, 24_060 / 12
aspa_seul, aspa_couple = 1_043.59, 1_620.18   # montants au 1er janvier 2026
alloc = 752_800                                 # allocataires fin 2024
gain_seul = seuil_seul - aspa_seul
gain_couple_pp = (seuil_couple - aspa_couple) / 2
print(f"Hausse mensuelle : personne seule {gain_seul:.2f} € ; par allocataire en couple {gain_couple_pp:.2f} €")
haut = alloc * gain_seul * 12 / 1e9
bas = alloc * gain_couple_pp * 12 / 1e9
print(f"Coût à effectifs constants : {bas:.2f} à {haut:.2f} Md€ par an, avant nouveaux éligibles et recours accru")

print("\n== Q3. Grande Sécu et fraude ==")
print(f"3,5 Md€ / 7,6 Md€ de frais de gestion des complémentaires (2019) = {pct(3.5, 7.6):.0f} %")
print(f"5,5 Md€ / 11,4 Md€ encaissés par le contrôle fiscal (2024) = {pct(5.5, 11.4):.0f} %")

print("\n== Q4. Actes 2012-2017 : ancienneté au 2026-10-27 ==")
ref = date(2026, 10, 27)
actes = {"Décret carrières longues": date(2012, 7, 2), "Emplois d'avenir (loi)": date(2012, 10, 26),
         "ANI et loi de sécurisation de l'emploi": date(2013, 6, 14), "Contrat de génération (loi)": date(2013, 3, 1),
         "Loi retraites Touraine": date(2014, 1, 20), "Prime d'activité (loi)": date(2015, 8, 17),
         "Loi vieillissement (ASV)": date(2015, 12, 28), "Loi travail": date(2016, 8, 8),
         "Garantie jeunes généralisée": date(2017, 1, 1)}
for k, d in actes.items():
    print(f"{k} : {(ref - d).days / 365.25:.1f} ans")
print(f"Contrat de génération : 40 300 / 220 000 attendus = {pct(40_300, 220_000):.0f} % ; / 500 000 = {pct(40_300, 500_000):.0f} %")

print("\n== Q3. Effets distributifs : deux ans de pension moyenne (Drees, source 33) ==")
print(f"2 x 12 x 1 607 € = {2 * 12 * 1607:,} €")

print("\n== Q4. Cadre entré à 23 ans avec 43 annuités ==")
print(f"Âge de départ au taux plein : {23 + 43} ans")

print("\n== Q4 (arbitrage de l'étape 6). Scrutin de commission du 23 octobre 2024, article 1er ==")
# Compte rendu n° 10 de la commission des affaires sociales, p. 16-17 (liste nominative)
soc_abst = ["Aviragnet", "Bellay", "Califer", "Dombre Coste", "Godard", "Herouin-Léautey", "Runel"]
soc_contre = ["Guedj", "Simion"]
soc_pour = []
n_soc = len(soc_abst) + len(soc_contre) + len(soc_pour)
print(f"Membres SOC présents : {n_soc} ; abstention {len(soc_abst)}, contre {len(soc_contre)}, pour {len(soc_pour)}")
print(f"Part de l'abstention : {pct(len(soc_abst), n_soc):.0f} % (règle des 60 % : position = abstention)")
pour, contre, abst = 17, 28, 19
print(f"Total : {pour + contre + abst} votants (pour {pour}, contre {contre}, abstentions {abst})")
print(f"Si les 19 abstentionnistes avaient voté pour : {pour + abst} pour contre {contre}")
print(f"Texte de séance (scrutin 217) : 7 articles de rapport en commission, 3 restants après la séance "
      f"(2 quinquies, 2 octies, article additionnel de l'amendement n° 6) ; article 3 (gage) non adopté")
print(f"Bourses : 55 000 (2013) + 77 500 (2014) = {55_000 + 77_500:,} nouveaux boursiers à 1 000 €")
