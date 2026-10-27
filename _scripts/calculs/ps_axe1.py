"""PS, axe 1 (finances publiques et dette) : calculs des étapes 3 à 5.

Rédigé le 2026-10-27 par un sous-agent Opus. Chaque bloc imprime un résultat
repris dans 02-partis/ps/axes/1-finances-publiques.md avec la mention
« calcul par nos soins ». Sources entre crochets : numéros de la liste des
sources de la fiche.
"""

# --- Données publiques -------------------------------------------------------
# Insee, comptes nationaux base 2020, tableaux 3.101 (dette) et 3.106 (déficit)
dette_md = {2012: 1915.8, 2016: 2190.5, 2017: 2263.3, 2025: 3460.5}
dette_t2_2026 = 3595.5                      # Insee, Informations rapides n° 239
deficit_pct_b2020 = {2012: 5.2, 2013: 4.9, 2014: 4.6, 2015: 3.9, 2016: 3.8, 2017: 3.4}
dette_pct_b2020 = {2012: 91.7, 2016: 98.2, 2017: 98.8}
deficit_apu_2025, deficit_apul_2025 = 152.5, 15.6   # Md€, tableau 3.106
deficit_apu_2024, deficit_apul_2024 = 169.1, 17.8
# Insee, publications de l'époque (bases 2010 et 2014)
deficit_epoque = {2012: 4.8, 2013: 4.2, 2017: 2.6}  # IP 1500 (2014) ; IP 1698 (2018)
dette_epoque_2017 = 96.8
pib_2013 = 2117.2                             # base 2020
# Engagements 2012 [C-PS-69, p. 22]
promesse_deficit = {2012: 4.5, 2013: 3.0, 2014: 2.3, 2015: 1.6, 2016: 0.8, 2017: 0.0}
promesse_dette_2017 = 80.2
# HCFP, avis 2026-5 : PIB 2026 et 2027, dette 2026 et 2027, croissance nominale
pib_2026, pib_2027 = 3051.4, 3135.0
dette_pct_2026, dette_pct_2027 = 119.3, 121.7
g_nominal_2027 = 0.027
sfa = (0.0, 0.5)                              # ajustement stock-flux, point de PIB
# Contre-budget 2027 [C-PS-33]
recettes, soutien, economies, fraude, depenses = 39.5, 11.0, 12.1, 5.5, 22.0
postes_chiffres = [5, 1, 2.5, 1.5, 1, 1, 3, 1, 3, 1]   # priorités 02 à 05
lcp = {"Zucman": 15, "héritages": 10, "numérique": 10, "exonérations": 4}
# Autres bases
cae_heritage = 12.0        # CAE, note 69 (2021), recettes supplémentaires simulées
dmtg_2024 = 20.8           # Md€, question écrite n° 11677 (chiffre de la question)
fraude_loi_2026 = 2.3      # Md€ attendus de la loi contre les fraudes (relais)
arcep_tbits = 56.0         # trafic entrant fin 2025, Arcep
tarif_go = 0.055           # €/Go, amendement I-CF365

print("=== Q1 Diagnostic ===")
print("dette 2017 -> T2 2026 :", round(dette_t2_2026 - dette_md[2017], 1), "Md€")
print("dette 2016 -> T2 2026 (dix ans) :", round(dette_t2_2026 - dette_md[2016], 1), "Md€")
dette_fin_2026 = dette_pct_2026 / 100 * pib_2026
print("dette fin 2026 prévue (HCFP) :", round(dette_fin_2026, 1), "Md€ ; hausse depuis 2017 :",
      round(dette_fin_2026 - dette_md[2017], 1))
print("part des APUL dans le déficit 2025 :", round(deficit_apul_2025 / deficit_apu_2025 * 100, 1), "%",
      "; 2024 :", round(deficit_apul_2024 / deficit_apu_2024 * 100, 1), "%")
rec = {2017: 54.3, 2025: 52.2}; dep = {2017: 57.7, 2025: 57.3}   # Insee IP 2106
print("variation 2017-2025 : recettes", round(rec[2025] - rec[2017], 1), "pt ; dépenses",
      round(dep[2025] - dep[2017], 1), "pt ; déficit", round(5.1 - 3.4, 1), "pt")

print("\n=== Q3 Faisabilité ===")
solde = recettes - soutien + (economies + fraude) - depenses
print("effort net (texte, 12,1 + 5,5) :", round(solde, 1), "Md€ ; avec 17,5 au tableau :",
      round(recettes - soutien + 17.5 - depenses, 1))
print("effort net en % du PIB 2027 :", round(24 / pib_2027 * 100, 2))
print("recettes brutes en % du PIB 2027 :", round(recettes / pib_2027 * 100, 2),
      "; rapport aux 17 Md€ de mesures nouvelles du PLF :", round(recettes / 17, 2))
print("postes de dépenses chiffrés :", sum(postes_chiffres), "; non ventilé :", depenses - sum(postes_chiffres))
print("ventilation LCP :", sum(lcp.values()), "contre 39,5")
print("Zucman + numérique :", lcp["Zucman"] + lcp["numérique"], "Md€ soit",
      round((lcp["Zucman"] + lcp["numérique"]) / recettes * 100, 1), "% des recettes")
print("CSG héritages 10 contre CAE 12 :", round((10 - cae_heritage) / cae_heritage * 100, 1), "%",
      "; rapport aux DMTG 2024 :", round(10 / dmtg_2024 * 100, 1), "%")
print("fraude 5,5 contre 2,3 attendus de la loi de 2026 :", round(5.5 / fraude_loi_2026, 2), "fois")
secondes = 365.25 * 24 * 3600
go_an = arcep_tbits * 1e12 / 8 * secondes / 1e9
print("volume annuel si 56 Tbit/s constants :", round(go_an / 1e9, 1), "milliards de Go ;",
      "taxe avant plafond :", round(go_an * tarif_go / 1e9, 1), "Md€")
print("volume nécessaire pour 10 Md€ :", round(10e9 / tarif_go / 1e9, 1), "milliards de Go")
for g in (g_nominal_2027, 0.03):
    for s in sfa:
        d = dette_pct_2027 * g / (1 + g) - s
        print(f"déficit stabilisant (g={g}, sfa={s}) : {d:.2f} % du PIB")
for base, lib in ((5.0, "cible du PLF 2027"), (5.4, "prévision 2026")):
    print(f"déficit 2027 si -0,77 pt depuis {lib} ({base} %) :", round(base - 24 / pib_2027 * 100, 2))
annule = 21 + 6.5
print("si le contre-budget remplace les 27,5 Md€ de mesures du PLF critiquées en séance :",
      round(24 - annule, 1), "Md€ par rapport au PLF")

print("\n=== Q4 Actes 2012-2017 ===")
for y in sorted(promesse_deficit):
    print(y, "promis", promesse_deficit[y], "exécuté base 2020", deficit_pct_b2020[y],
          "écart", round(deficit_pct_b2020[y] - promesse_deficit[y], 1))
print("2013 base de l'époque :", deficit_epoque[2013], "écart", round(deficit_epoque[2013] - 3.0, 1))
print("2017 base de l'époque :", deficit_epoque[2017], "écart", round(deficit_epoque[2017] - 0.0, 1))
print("dette 2017 : promis", promesse_dette_2017, "; époque", dette_epoque_2017,
      "(écart", round(dette_epoque_2017 - promesse_dette_2017, 1), ") ; base 2020", dette_pct_b2020[2017],
      "(écart", round(dette_pct_b2020[2017] - promesse_dette_2017, 1), ")")
print("hausse de la dette 2012-2017 :", round(dette_md[2017] - dette_md[2012], 1), "Md€ ;",
      round(dette_pct_b2020[2017] - dette_pct_b2020[2012], 1), "pt de PIB")
print("mesures nouvelles 2013 (1,4 pt de PIB) :", round(0.014 * pib_2013, 1), "Md€ contre 29 Md€ promis")

print("\n=== Q3 (arbitrage de l'étape 6) : mesures du Projet non chiffrées au contre-budget ===")
# Estimations de niveau 2 reprises de la fiche 2 (tableau Q3), horizons différents (2016 à 2035)
mesures = {  # (bas, haut) en Md€
    "retour à 62 ans (Cour 2035 ; Cnav 2032)": (10.4, 16.0),
    "abrogation des réformes de l'assurance chômage (Unédic)": (6.5, 6.5),
    "ASPA au seuil de pauvreté (calcul fiche 2)": (1.7, 2.7),
    "RSA automatique (non-recours, Drees)": (2.5, 2.5),
    "revenu d'autonomie (RSA dès 21 ou 18 ans, Trésor 2016)": (3.1, 6.6),
}
bas = sum(v[0] for v in mesures.values()); haut = sum(v[1] for v in mesures.values())
print(f"somme : {bas:.1f} à {haut:.1f} Md€, soit {bas / pib_2027 * 100:.2f} à {haut / pib_2027 * 100:.2f} % du PIB 2027")
