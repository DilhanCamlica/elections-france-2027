"""LR, axe 1 (finances publiques et dette) : calculs des étapes 3 à 5.

Rédigé le 2026-10-27 par un sous-agent Opus. Chaque bloc imprime un résultat
repris dans 02-partis/lr/axes/1-finances-publiques.md avec la mention
« calcul par nos soins ». Sources entre crochets : numéros de la liste des
sources de la fiche (section « Sources ajoutées aux étapes 3 à 5 »).
Exécution : python3 -I _scripts/calculs/lr_axe1.py
"""

# --- Données publiques -------------------------------------------------------
# Insee, tableau 3.101 (dette, base 2020) [24] et Informations rapides n° 239 [23]
dette = {2017: 2263.2858, 2019: 2387.399, 2021: 2828.7813, 2025: 3460.465}
dette_asso_2025 = 293.065
dette_t2_2026, dette_asso_t2_2026 = 3595.5, 309.4
# Insee, tableau 3.106 (déficit, base 2020) [25]
deficit_2017_pct = 3.4
deficit_2025_md = 152.511
pib_2025_md = 2995.0                       # série du PIB du tableau 3.101
# HCFP, avis 2026-5 [26] : PIB, intérêts, LPM, effort
pib_2026, pib_2027_plf = 3051.4, 3135.0
interets = {2025: 66, 2026: 79, 2027: 91}
lpm = {2026: 57, 2027: 63}
# PLF 2027 [29] : impôt sur le revenu, charge de la dette de l'État
ir_2027, charge_dette_etat_2027 = 102.5, 72.373 + 0.561
# Eurostat gov_10a_main, dépense publique en % du PIB, 2025 [28]
te_2025 = {"FI": 57.5, "FR": 57.3, "EA20": 49.8}
# Cour des comptes, RSPFP juin 2026 [27] : effort (méthode de la Cour)
cour_effort_2029, cour_effort_2031 = 85, 135
# DG Trésor, Trésor-Éco n° 403 [31] : effort à l'horizon 2032, politique inchangée
tresor_effort_2032 = 125
# Sénat, commission d'enquête sur les agences (2025) [32]
senat_agences = 0.54
# DGAFP [34] : pensions de droit direct attribuées en 2024 (fonction publique)
departs_fp_2024 = 136_700
# Sénat, rapport sur le PLF 2011 citant la Cour (2010) [35] : RGPP
rgpp_postes_2007_2010 = 100_000
# Fraude : rendement attendu de la loi de 2026 selon le gouvernement (relais, fiche PS)
fraude_loi_2026 = 2.3

# --- Plan du 12 octobre 2026 [C-LR-12] ----------------------------------------
annees = [2027, 2028, 2029, 2030, 2031, 2032]
eco_tot = [12, 58, 95, 131, 169, 197]
def_sans = [5.2, 5.5, 5.9, 6.3, 6.7, 7.1]
def_avec = [4.8, 4.2, 3.9, 3.6, 2.8, 2.2]
dette_avec = [121.1, 122.2, 123.2, 123.8, 123.6, 122.7]
dette_sans_pub = {2027: 121.5, 2029: 126.8, 2031: 133.5, 2032: 137.4}
croiss = [0.008, 0.010, 0.010, 0.010, 0.010, 0.010]
defl = [0.017, 0.016, 0.015, 0.015, 0.015, 0.015]
fiches = {"3": 56, "4": 32, "5": 8, "6": 42, "7": 4, "8": 30, "9": 7, "10": 4,
          "11": 4, "12": 10}
eco_deficit_2032, rendus = 146, 51
lignes_fp = 400_000
cout_poste = 62_000
agences_structures = 4.0
fraude_plan = 9.0
cotisation_1pct, rafp = 6.0, 4.3
immig_revision = 3.6 + 0.9

print("=== Q1 Diagnostic ===")
print(f"Hausse de la dette fin 2017 à fin T2 2026 : {dette_t2_2026 - dette[2017]:.1f} Md€")
covid = dette[2021] - dette[2019]
print(f"Hausse 2020-2021 : {covid:.1f} Md€ ; hors Covid : {dette_t2_2026 - dette[2017] - covid:.1f} Md€")
print(f"Part de la dette des ASSO : fin 2025 {100*dette_asso_2025/dette[2025]:.1f} % ; "
      f"fin T2 2026 {100*dette_asso_t2_2026/dette_t2_2026:.1f} %")
print(f"Déficit 2025 : {100*deficit_2025_md/pib_2025_md:.2f} % du PIB")
print(f"Intérêts APU 2027 / IR 2027 : {100*interets[2027]/ir_2027:.0f} % ; "
      f"charge de la dette de l'État / IR : {100*charge_dette_etat_2027/ir_2027:.0f} %")
print(f"Écart de dépense France - zone euro 2025 : {te_2025['FR']-te_2025['EA20']:.1f} points ; "
      f"France - Finlande : {te_2025['FR']-te_2025['FI']:.1f}")
print(f"Intérêts 2027 (91) contre LPM 2027 ({lpm[2027]}) : x{interets[2027]/lpm[2027]:.2f}")

print("\n=== Q3 Arithmétique interne du plan ===")
print("Somme des fiches 3 à 12 :", sum(fiches.values()), "; 146 + 51 =", eco_deficit_2032 + rendus)
# PIB nominal selon les hypothèses du plan, à partir du PIB 2026 du HCFP
pib = {}
p, prix = pib_2026, 1.0
for a, g, d in zip(annees, croiss, defl):
    p *= (1 + g) * (1 + d)
    prix *= (1 + d)
    pib[a] = p
print("PIB nominal (Md€) :", {a: round(v) for a, v in pib.items()})
print(f"Indice des prix 2032 / 2026 : {prix:.4f}")
eco_nominal = eco_deficit_2032 * prix
print(f"146 Md€ (euros 2026) en euros courants 2032 : {eco_nominal:.1f} Md€, "
      f"soit {100*eco_nominal/pib[2032]:.2f} point de PIB")
ecart_dette = 137.4 - 122.7
interets_evites = ecart_dette / 100 * pib[2032] * 0.036
print(f"Dette évitée en 2032 : {ecart_dette:.1f} points, {ecart_dette/100*pib[2032]:.0f} Md€ ; "
      f"intérêts évités à 3,6 % : {interets_evites:.1f} Md€ ({100*interets_evites/pib[2032]:.2f} point)")
print(f"Réduction du déficit expliquée : {100*(eco_nominal+interets_evites)/pib[2032]:.2f} point "
      f"contre {def_sans[-1]-def_avec[-1]:.1f} affiché")
# Dynamique de la dette, ajustement stock-flux nul puis 0,5 point (valeur du HCFP 2026-2027)
for sfa in (0.0, 0.5):
    d = dette_avec[0]
    serie = [d]
    for i in range(1, len(annees)):
        g = (1 + croiss[i]) * (1 + defl[i]) - 1
        d = d / (1 + g) + def_avec[i] + sfa
        serie.append(round(d, 1))
    print(f"Dette recalculée, ajustement stock-flux {sfa} : {serie} (affiché {dette_avec})")
d = dette_sans_pub[2027]
for i in range(1, len(annees)):
    g = (1 + croiss[i]) * (1 + defl[i]) - 1
    d = d / (1 + g) + def_sans[i]
print(f"Dette sans réforme recalculée 2032 : {d:.1f} (affiché 137,4)")
print("Réduction annuelle du déficit avec le plan (points) :",
      [round(def_avec[i-1]-def_avec[i], 1) for i in range(1, len(annees))])

print("\n=== Q3 Confrontation aux niveaux 2 et 3 ===")
print(f"Enveloppe déficit 146 contre DG Trésor 125 : {100*(146/tresor_effort_2032-1):+.0f} %")
print(f"146 contre Cour des comptes 135 (2031, autre méthode) : {100*(146/cour_effort_2031-1):+.0f} %")
print(f"Agences, structures : {agences_structures} contre Sénat {senat_agences} : "
      f"x{agences_structures/senat_agences:.1f}, écart {agences_structures-senat_agences:.2f} Md€")
print(f"Postes : 400 000 x 62 000 € = {lignes_fp*cout_poste/1e9:.1f} Md€")
cinq_ans = 5 * departs_fp_2024
print(f"Départs en retraite sur cinq ans au rythme de 2024 : {cinq_ans} ; "
      f"part non remplacée : {100*lignes_fp/cinq_ans:.0f} %")
print(f"Rythme annuel du plan : {lignes_fp/5:.0f} ; RGPP 2007-2010 : {rgpp_postes_2007_2010/4:.0f} par an ; "
      f"rapport x{(lignes_fp/5)/(rgpp_postes_2007_2010/4):.1f}")
print(f"Fraude 9 Md€ contre loi de 2026 (2,3 Md€ attendus) : x{fraude_plan/fraude_loi_2026:.1f}")
print(f"Lignes conditionnées à la révision constitutionnelle : {immig_revision:.1f} Md€, "
      f"{100*immig_revision/197:.1f} % du plan")
print(f"Cotisation dédiée et RAFP : {cotisation_1pct+rafp:.1f} Md€, {100*(cotisation_1pct+rafp)/197:.1f} % du plan")
bas = agences_structures - senat_agences
haut = bas + immig_revision
print(f"Écart établi sur pièces de niveau 2 et 3 : {bas:.2f} Md€ ({100*bas/197:.1f} %) ; "
      f"avec les lignes conditionnées : {haut:.2f} Md€ ({100*haut/197:.1f} %)")
print("Déficit 2029 du plan (3,9 %) contre l'engagement de PDE (sous 3 % en 2029) : écart 0,9 point")
print("Trajectoire PSMT 2030 (2,2 %) contre plan 2030 (3,6 %) : écart 1,4 point")

# --- Étape 6 (arbitrage, 2026-10-27) ------------------------------------------
# Cotisations nouvelles et rendement de réserves comptés parmi les « économies »
# des retraites [C-LR-12, p. 8] ; budget des armées promis par le candidat
# [C-LR-72] contre LPM actualisée pour 2030 [66, page ouverte par la contradiction]
reserves_rendement = 7.5
non_depense = cotisation_1pct + rafp + reserves_rendement
print(f"Étape 6 : cotisations nouvelles et rendement de réserves : {non_depense:.1f} Md€, "
      f"{100*non_depense/197:.1f} % du plan de 197 Md€")
armees_candidat, lpm_2030 = 100.0, 76.3
print(f"Étape 6 : armées, 100 Md€ promis (fin de quinquennat) contre LPM 2030 {lpm_2030} Md€ : "
      f"écart {armees_candidat-lpm_2030:.1f} Md€ (horizons 2030 et 2032 mêlés)")
