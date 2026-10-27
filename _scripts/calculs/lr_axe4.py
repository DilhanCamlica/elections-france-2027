"""LR, axe 4 (pouvoir d'achat et fiscalité) : calculs des étapes 3 à 5.

Rédigé le 2026-10-27 par un sous-agent Opus. Chaque bloc imprime un résultat
repris dans 02-partis/lr/axes/4-pouvoir-achat-fiscalite.md avec la mention
« calcul par nos soins ». Les numéros entre crochets renvoient à la liste
« Sources ajoutées aux étapes 3 à 5 » de la fiche ; [C-LR-nn] au corpus.
Exécution : python3 -I _scripts/calculs/lr_axe4.py
"""

def p(label, value, unit=""):
    print(f"{label} : {value}{unit}")

# --- 1. Prix de l'électricité des ménages (Eurostat nrg_pc_204, tranche DC) [S1]
# c€/kWh toutes taxes (I_TAX) et hors taxes (X_TAX), extraction du 2026-10-27
fr_ttc = {"2009-S1": 0.1206, "2009-S2": 0.1207, "2025-S1": 0.2671,
          "2025-S2": 0.2561, "2026-S1": 0.2485}
fr_ht_2026s1, ue_ttc_2026s1 = 0.1726, 0.2832
hicp = {2009: 92.44, 2025: 124.43}          # Eurostat prc_hicp_aind, France [S2]
moy09 = (fr_ttc["2009-S1"] + fr_ttc["2009-S2"]) / 2
moy25 = (fr_ttc["2025-S1"] + fr_ttc["2025-S2"]) / 2
ratio = moy25 / moy09
reel = ratio / (hicp[2025] / hicp[2009])
print("1. Électricité")
p("  prix moyen 2009 (€/kWh TTC)", round(moy09, 4))
p("  prix moyen 2025 (€/kWh TTC)", round(moy25, 4))
p("  rapport 2025 / 2009", round(ratio, 2))
p("  hausse hors inflation (IPCH)", round((reel - 1) * 100, 1), " %")
p("  France contre UE, 1er semestre 2026", round((fr_ttc["2026-S1"] / ue_ttc_2026s1 - 1) * 100, 1), " %")
p("  part des taxes dans le prix, France 2026-S1", round((1 - fr_ht_2026s1 / fr_ttc["2026-S1"]) * 100, 1), " %")

# --- 2. Poids des CEE dans le tarif réglementé (CRE, délibération 2026-06) [S3]
cee_res = 9.80                      # €/MWh, consommateurs résidentiels, HT
baisse_ttc_eur, baisse_ttc_pct = 1.99, 0.83    # moyenne des TRVE bleus
baisse_ht_eur, baisse_ht_pct = 0.59, 0.36
ttc_moy = baisse_ttc_eur / (baisse_ttc_pct / 100)
ht_moy = baisse_ht_eur / (baisse_ht_pct / 100)
print("2. CEE dans le tarif bleu 2026")
p("  tarif moyen TTC déduit (€/MWh)", round(ttc_moy, 1))
p("  tarif moyen HT déduit (€/MWh)", round(ht_moy, 1))
p("  part des CEE, TVA de 20 % comprise, dans le TTC", round(cee_res * 1.2 / ttc_moy * 100, 1), " %")
p("  part des CEE dans le HT", round(cee_res / ht_moy * 100, 1), " %")
facture_moy = 1042.0                # € TTC par an pour 4,5 MWh, communiqué CRE du 2026-01-20 (relais [S3])
p("  gain annuel sur une facture moyenne (€)", round(facture_moy * cee_res * 1.2 / ttc_moy))
# Enveloppe totale des CEE : 8 Md€ en 2026 selon le gouvernement (relais [S4])
p("  8 Md€ par an sur 2026-2030 (Md€)", 8 * 5, "")
p("  9,5 Md€ du livret rapportés à cette enveloppe", round(9.5 / 40 * 100, 1), " %")

# --- 3. Prélèvements sur le travail et la production (Eurostat gov_10a_taxag) [S5]
d611 = {"FR": 10.0, "EA20": 7.7}    # cotisations sociales effectives des employeurs, % PIB 2024
d613 = {"FR": 4.7, "EA20": 6.0}     # cotisations des ménages (salariés et indépendants), % PIB 2024
d29 = {"FR": 4.4, "EA20": 2.2, "UE": 2.4}   # autres impôts sur la production, % PIB 2024
pib_2025 = 2995.0                   # Insee, base 2020 (fiche LR axe 1, source 24)
print("3. Prélèvements sur le travail")
ecart = d611["FR"] - d611["EA20"]
p("  écart de cotisations employeurs avec la zone euro (points)", round(ecart, 1))
p("  en Md€ au PIB 2025", round(ecart / 100 * pib_2025, 1))
p("  écart de cotisations des ménages (points)", round(d613["FR"] - d613["EA20"], 1))
p("  impôts de production : 95 Md€ du livret en % du PIB 2025", round(95 / pib_2025 * 100, 2), " %")

# --- 4. Propriétaires (Eurostat ilc_lvho02, part de la population, 2025) [S6]
own = {"FR": 61.4, "UE": 68.5}
print("4. Propriétaires")
p("  écart France / UE, même mesure (points)", round(own["UE"] - own["FR"], 1))
p("  écart avancé par le livret, 57 contre 70 (points)", 70 - 57)

# --- 5. Seuil zéro cotisation : note technique [C-LR-03] et livret [C-LR-02]
print("5. Seuil zéro cotisation")
perte_patronale = [-70, -529, -1174, -2060]     # M€, tableau 5
gain_salarial = [37, 40, 45, 62]
brut = sum(perte_patronale) + sum(gain_salarial)
p("  coût brut (M€)", brut)
compens = 2.6 + 1.4 + 1.0
p("  compensations (Md€)", round(compens, 1))
p("  solde (Md€)", round(compens + brut / 1000, 2))
# Arbitrage de l'étape 6 (n° 13) : la recette de 1,4 Md€ (« suppression de
# l'exonération fiscale » des heures supplémentaires) est exclue par le livret,
# qui maintient l'exonération « intégralement » [C-LR-02, p. 21].
p("  solde sans la recette de 1,4 Md€ exclue par le livret (Md€)", round(compens - 1.4 + brut / 1000, 3))
p("  solde sans 1,4 Md€ ni les 2,6 Md€ d'heures nouvelles (Md€)", round(compens - 1.4 - 2.6 + brut / 1000, 3))
p("  part de la perte patronale portée par le quartile supérieur", round(perte_patronale[3] / sum(perte_patronale) * 100, 1), " %")
gain_employeur = [6, 24, 50, 84]                 # €/mois, tableau 4
p("  gain employeur mensuel, rapport Q4 / Q1", round(gain_employeur[3] / gain_employeur[0], 1))
p("  perte annuelle des salariés déjà en heures supplémentaires (€)", 6 * 12)
p("  écart livret (4,3 Md€ rendus) contre note (3,83 Md€)", round(4.3 - 3.833, 2), " Md€")
rem_hs = [1054, 1787, 2315, 2965]                # Dares via la note, tableau 3
p("  rémunération des heures supplémentaires, rapport Q4 / Q1", round(rem_hs[3] / rem_hs[0], 1))

# Exemple « François » [C-LR-02, p. 22], hypothèses signalées :
net_mensuel = 2115.0
h_mois = 151.67
taux_net_brut = 0.78     # hypothèse : rapport net / brut d'un salarié non cadre du privé
csg_crds = (0.092 + 0.005) * 0.9825   # CSG et CRDS sur 98,25 % du brut
net_h = net_mensuel / h_mois
brut_h = net_h / taux_net_brut
h_annuelles_375 = 1607 * 37.5 / 35
h_au_dela = h_annuelles_375 - 1623
gain = 16 * net_h + h_au_dela * brut_h * 1.25 * (1 - csg_crds)
print("  exemple du livret (37,5 heures par semaine)")
p("    heures au-delà de 1 623", round(h_au_dela, 1))
p("    gain annuel recalculé (€)", round(gain))
p("    gain annoncé (230 € x 12)", 230 * 12)
p("    écart", round((2760 - gain) / 2760 * 100, 1), " %")
p("    16 heures au taux net (livret : environ 230 €)", round(16 * net_h))
p("  gain au salaire médian : 500 + 2 800 contre 3 500 (€)", 500 + 2800)

# --- 6. Restitution de 15 Md€ de cotisations salariales « dès le premier euro »
print("6. 15 Md€ de cotisations salariales")
gain_median = 500.0                     # € par an au salaire médian [C-LR-02, p. 16]
brut_median_annuel = net_mensuel / taux_net_brut * 12
taux = gain_median / brut_median_annuel
assiette = 15e9 / taux / 1e9
p("  baisse de taux implicite (uniforme)", round(taux * 100, 2), " % du brut")
p("  assiette implicite (Md€ de salaires bruts)", round(assiette))
masse_privee = 185 * 4                  # Urssaf, Stat'ur n° 415 : environ 185 Md€ au T4 2025 [S7]
p("  masse salariale privée annualisée (Md€)", masse_privee)
p("  gain médian si la baisse portait sur le seul privé (€)", round(15e9 / (masse_privee * 1e9) * brut_median_annuel))
deciles = {"D1": 1492, "médiane": 2190, "D9": 4334}   # Insee, net EQTP privé 2024 [S8]
for k, v in deciles.items():
    p(f"  gain annuel au {k} (taux uniforme)", round(v / taux_net_brut * 12 * taux))

# --- 7. Revenu familial [C-LR-07, p. 12-13]
print("7. Revenu familial")
rf = 14e6 * 240 * 12 / 1e9
p("  coût du RF (Md€)", round(rf, 2))
p("  solde avant troisième enfant (Md€)", round(41 - rf, 2))
t3 = 8e6 * 0.17 * 240 * 12 * 14 / 18 / 1e9
p("  troisième enfant, formule de la note (Md€)", round(t3, 2))
p("  solde avec 1,5 Md€", round(41 - rf - 1.5, 2))
p("  solde avec la formule", round(41 - rf - t3, 2))

# --- 8. Impôts de production [C-LR-05, p. 20] contre sources de niveau 2
print("8. Impôts de production")
c3s_lr, c3s_plfss = 5.3, 5.452          # PLFSS 2026, annexe 3 (fiche RN, source 27)
cvae_lr, cvae_recon = 4.3, 3.4          # reconstitution de la fiche RN (PLF 2026)
p("  C3S : écart du livret", round((c3s_lr / c3s_plfss - 1) * 100, 1), " %")
p("  CVAE : écart du livret", round((cvae_lr / cvae_recon - 1) * 100, 1), " %")
p("  total du livret", round(5.3 + 4.3 + 2.8 + 1.9, 1), " Md€")

# --- 9. Successions : seuil de la tranche à 45 % (service-public.fr) [S9]
print("9. Successions")
seuil45 = 1_805_677
p("  part nette taxable à 45 % (€)", seuil45)
p("  part brute correspondante avec l'abattement de 100 000 € (€)", seuil45 + 100_000)

# --- 10. Poids des mesures tenues constantes dans la fiche 14 du plan [C-LR-12, p. 16]
print("10. Fiche 14 du plan")
rendu = {"cotisations salariales": 15, "familles et transmission": 3,
         "MaPrimeRénov' et TVA sur les certificats": 3, "cotisations patronales": 15,
         "impôts de production": 15, "seuil zéro cotisation": 10, "fin des CEE": 4}
total = sum(rendu.values())
tenu = sum(rendu[k] for k in ["cotisations salariales", "cotisations patronales",
                               "impôts de production", "seuil zéro cotisation", "fin des CEE"])
p("  total rendu et autofinancé (Md€)", total)
p("  seuil, cotisations, impôts de production, CEE (Md€)", tenu)
p("  part", round(tenu / total * 100, 1), " %")
