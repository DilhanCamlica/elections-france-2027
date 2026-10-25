# Ordres de grandeur "calcul par nos soins", RN axe 2 (travail, protection sociale, fraude)
# Sources : voir 02-partis/rn/axes/2-travail-protection-sociale.md (numeros entre crochets)

def r(x, n=2):
    return round(x, n)

# 1. Fraude : estime, detecte, recouvre (HCFiPS, note du 13/01/2026) [24]
estime = 14.0                 # Md EUR, fraude sociale evaluee
part_cotis, part_alloc, part_ps = 0.52, 0.36, 0.12
detecte_2024 = 2.06           # Md EUR
recouvre_2024 = 0.681         # Md EUR
alloc = estime * part_alloc
prest = estime * (part_alloc + part_ps)
print("fraude allocataires estimee", r(alloc), "Md ; prestations (allocataires + pros de sante)", r(prest))
print("detecte / estime", r(detecte_2024 / estime * 100, 1), "% ; recouvre / estime", r(recouvre_2024 / estime * 100, 1), "%")
# Programme 2024 : 10 a 25 Md de fraude aux prestations attribues a la Cour des comptes [C-RN-17]
print("10 Md / prestations estimees", r(10 / prest), "; 25 Md /", r(25 / prest))
print("10 Md / fraude allocataires", r(10 / alloc), "; 25 Md /", r(25 / alloc))
# Programme 2022 : 15 Md d'economies par an sur la fraude sociale [C-RN-19]
print("15 Md / fraude sociale totale estimee", r(15 / estime * 100, 0), "%")
print("15 Md / fraude allocataires", r(15 / alloc))
# Contre-budget 2026 : plan fraudes 3,5 Md [C-RN-31]
print("3,5 Md / detecte 2024", r(3.5 / detecte_2024), "; / recouvre 2024", r(3.5 / recouvre_2024))
print("3,5 Md / fraude prestations estimee", r(3.5 / prest * 100, 0), "%")
# Cnaf : fraude estimee 2018 (Cour des comptes, Senat 2020) 2,3 Md ; detectee 2025 508,8 M [26][27]
print("Cnaf detecte 2025 / estime 2018", r(0.5088 / 2.3 * 100, 0), "%")

# 2. ALD : controle systematique 0,45 Md [C-RN-31] ; surcout du dispositif ALD ~15 Md (iFRAP citant Cnam) [33]
print("ALD 0,45 / 15 Md", r(0.45 / 15 * 100, 1), "%")
# fraude IJ detectee et stoppee 2025 : 49 M (ameli) [28]
print("ALD 0,45 / fraude IJ detectee 2025", r(0.45 / 0.049, 1))

# 3. Condition de cinq ans de travail : assiette (Institut Montaigne, legislatives 2024) [36]
assiette = {"RSA": 1.378, "prime d'activite": 1.217, "AAH": 1.392, "aides au logement": 1.825}
totaux = {"RSA": 11.784, "prime d'activite": 10.400, "AAH": 11.900, "aides au logement": 15.600}
a = sum(assiette.values())
t = sum(totaux.values())
print("assiette etrangers (4 prestations)", r(a), "Md ; depense totale des 4 prestations", r(t), "Md")
for rn in (6.1, 12.2):
    print(f"chiffrage RN {rn} / assiette etrangers", r(rn / a), "; / estimation mediane Montaigne 2,6", r(rn / 2.6))
# RSA : foyers non UE (QE 5157, 30/06/2022) [35]
foyers_nonue, part = 300000, 0.156
foyers_tot = foyers_nonue / part
print("foyers RSA total implicite", round(foyers_tot), "; RSA moyen par foyer et par an", round(totaux["RSA"] * 1e9 / foyers_tot), "EUR")
print("RSA verse aux foyers non UE (prorata foyers)", r(totaux["RSA"] * part), "Md")

# 4. Retraites : chiffrage du parti contre estimations independantes
parti = {"2022 annee pleine": 9.6, "2026 (Chenu, Medef)": 9.0, "2031 (annexe)": 9.5}
indep = {"Montaigne 2022 (version 2022)": 26.5, "Montaigne 2022 bas": 23.5,
         "Montaigne 2024 (version 2024)": 34.7, "Montaigne 2024 bas": 31.5,
         "iFRAP 2024 (mesures retraite RN)": 14.0, "iFRAP 2024 abrogation seule 2027": 10.0,
         "Montaigne 2024 abrogation 2023 seule": 8.2, "Cnav abrogation 2032 (relais)": 16.0}
print("Montaigne 2022 / 9,6", r(26.5 / 9.6), "; bas", r(23.5 / 9.6))
print("Montaigne 2024 / 9", r(34.7 / 9), "; bas", r(31.5 / 9))
print("iFRAP 14 / 9", r(14 / 9), "(ecart", r((14 / 9 - 1) * 100, 0), "%)")
print("Cnav 16 (2032) / 9,5 (2031)", r(16 / 9.5))
# Economies 'reparation du systeme actuel' 15 Md en 2031 contre 422 Md de depenses de retraite 2025 (COR) [20]
print("15 Md / 422 Md", r(15 / 422 * 100, 1), "% ; 20 Md :", r(20 / 422 * 100, 1), "%")
# Suspension LFSS 2026 : 0,3 a 0,4 Md en 2026, 1,8 a 1,9 Md en 2027 [29][30]
print("cout suspension 2027 / chiffrage RN 9 Md", r(1.8 / 9 * 100, 0), "a", r(1.9 / 9 * 100, 0), "%")
# Report de charges (Drees 3,6 + Dares 1,3) [C-RN-33] ; gains annonces 2023 : 17,7 Md en 2030 (relais) [32]
print("report de charges 4,9 Md / 17,7", r(4.9 / 17.7 * 100, 0), "% ; 3,6 / 17,7", r(3.6 / 17.7 * 100, 0), "%")
# Exemple 2022 : 176 trimestres pour une entree a 18 ans ; 148 trimestres
print("176 trimestres =", 176 / 4, "ans (18 -> 62) ; 148 trimestres =", 148 / 4, "ans")
# Ordre de grandeur pour un depart deux ans plus tot : pension moyenne 1 666 EUR bruts (Drees) [Renaissance 66]
print("deux ans de pension moyenne brute", 1666 * 12 * 2, "EUR (hors salaires non percus)")

# 5. Indexation : IPP note 129 (sept. 2026), gel des retraites de base en 2027 [37]
print("IPP : rendement direct 6,6 Md, net 5,2 Md ; part du direct conservee", r(5.2 / 6.6 * 100, 0), "%")
# Contre-budget 2026 : 3,61 Md (indexation + degel) contre PLFSS 2026 gel 3,6 Md [Renaissance 40]
print("ecart RN 3,61 / PLFSS 3,6", r((3.61 / 3.6 - 1) * 100, 1), "%")
# Petites retraites 2022 : 2 + 1 Md contre 3,5 Md dans le meme document
print("ecart 3,5 / 3", r((3.5 / 3 - 1) * 100, 0), "%")

# 6. Jeunes : taux d'emploi 15-24 ans France 34,7 % contre Allemagne 50,7 % (page Qui paie pour qui ?)
print("ecart emploi jeunes FR-DE", r(50.7 - 34.7, 1), "points (le parti dit 10)")

# 7. Cour des comptes (relais Senat, rapport general 139, 2025) : AOD maintenu a 63 ans des la generation 1964
#    -5,8 Md par an pour les retraites en 2035 (euros 2024), -13,0 Md pour les finances publiques [53]
print("extrapolation lineaire a deux ans d'age :", 5.8 * 2, "Md (retraites seules, ordre de grandeur)")
print("5,8 / 9,5 (chiffrage RN 2031)", r(5.8 / 9.5 * 100, 0), "%")
