"""LR, axe 5 (sécurité, ordre public et libertés) : calculs de la fiche.

- Auteur : sous-agent Opus, étapes 3 à 5
- Statut : brouillon (étapes 3 à 5)
- Données arrêtées au : 2026-10-27
- Fiche : 02-partis/lr/axes/5-securite-libertes.md
Chaque valeur d'entrée renvoie au numéro de source de la fiche (« s. n »). Calculs par nos soins.
Lancer avec : python3 -I _scripts/calculs/lr_axe5.py
"""

def pct(a, b):
    return 100 * (a / b - 1)

# 1. Série SSMSI 2016-2025, faits enregistrés (bilan 2025, annexe 1) [s. 20]
ans = list(range(2016, 2026))
tentatives = [2259, 2284, 2482, 2718, 3115, 3136, 3584, 4015, 4290, 4477]
homicides = [911, 826, 831, 857, 823, 882, 959, 996, 976, 975]
violences = [277300, 289600, 312200, 334200, 332400, 371200, 417200, 444100, 449800, 472400]
vv_sans_arme = [94800, 89500, 83000, 80900, 65600, 62100, 59500, 54300, 48300, 49200]
vols_armes = [10900, 10000, 9000, 9100, 8600, 8500, 8600, 8700, 8600, 7900]
cambriolages = [248900, 253000, 236800, 236700, 189300, 189900, 211500, 217100, 218200, 211600]
vols_vehicules = [164800, 154800, 142600, 140000, 121800, 122200, 133100, 139900, 137600, 124800]

baisses = [ans[i] for i in range(1, len(ans)) if tentatives[i] <= tentatives[i - 1]]
print(f"1a. Tentatives d'homicide 2016-2025 : années sans hausse = {baisses or 'aucune'} ; x{tentatives[-1] / tentatives[0]:.2f} ({pct(tentatives[-1], tentatives[0]):+.0f} %)")
print(f"1b. Homicides 2016-2025 : {pct(homicides[-1], homicides[0]):+.0f} % ; maximum {max(homicides)} en {ans[homicides.index(max(homicides))]}")
print(f"1c. Violences physiques 2016-2025 : {pct(violences[-1], violences[0]):+.0f} % ; 2025 : {violences[-1]} contre « 473 000 » de la PPL n° 3335 ({pct(473000, violences[-1]):+.2f} %)")
for nom, s in [("vols violents sans arme", vv_sans_arme), ("vols avec armes", vols_armes), ("cambriolages", cambriolages), ("vols de véhicules", vols_vehicules)]:
    print(f"1d. {nom} 2016-2025 : {pct(s[-1], s[0]):+.0f} %")

# 2. Mineurs mis en cause, IGJ juillet 2025 (repris de la fiche RN, source 27) [s. 23]
print(f"2. Mineurs mis en cause 2016-2024 : {pct(131572, 165638):+.1f} %")

# 3. Ifop pour Écran de veille, 2025 [s. 27] : moins de 25 ans voilées 45 % (2025) contre 16 % (2003) ; PPL n° 2167 : 44 % des 15-24 ans
print(f"3. Voile chez les moins de 25 ans : x{45 / 16:.1f} ; écart avec le chiffre de la PPL : {45 - 44} point")

# 4. PPL n° 3335 : seuils rapportés à la peine encourue [C-LR-50, p. 6-7] ; loi de 2007 : mêmes seuils pour les délits et crimes [s. 30]
for seuil, encourue in [(1, 3), (2, 5), (3, 7), (4, 10), (5, 15), (7, 20), (10, 30)]:
    print(f"4. Seuil {seuil} an(s) pour {encourue} ans encourus : {100 * seuil / encourue:.0f} %")

# 5. Ordre de grandeur de l'effet carcéral de la PPL n° 3335 (hypothèses explicites, pas une prévision)
#    Condamnations 2024 pour coups et violences volontaires (délits) : 80 724, dont 5 316 par des juridictions pour mineurs [s. 22]
#    Récidivistes légaux parmi les condamnés pour violence volontaire : 21,7 % [s. 22]
adultes = 80724 - 5316
primo = adultes * (1 - 0.217)
places, detenus = 63348, 89400  # [s. 25] et [s. 26]
print(f"5a. Condamnés majeurs pour violences volontaires (délits) 2024 : {adultes} ; non récidivistes légaux : {primo:.0f}")
for part in (0.10, 0.25, 0.50):
    sup = primo * part  # un an de détention en plus par condamné = une place occupée un an
    print(f"5b. Si {part:.0%} des non-récidivistes reçoivent une année de détention de plus : {sup:.0f} places-années, soit {100 * sup / places:.0f} % des places opérationnelles")
print(f"5c. Densité actuelle : {100 * detenus / places:.1f} % (détenus du 1er oct. 2026 sur places du 1er sept. 2026, périmètres non identiques)")

# 6. Coût de construction, Cour des comptes plan 15 000 : 5,7 Md€ pour 15 471 places [s. 29]
print(f"6. Coût moyen par place : {5.7e9 / 15471 / 1e3:.0f} k€ ; 10 000 places : {10000 * 5.7e9 / 15471 / 1e9:.1f} Md€")

# 7. Participation du groupe DR au scrutin 805 (13/02/2025) : 4 votants ; effectif 47 (périmètre, 47 à 50 sur la législature) [s. 11]
for eff in (47, 50):
    print(f"7. Scrutin 805 : 4 votants sur {eff} = {100 * 4 / eff:.1f} %")
print(f"7b. Scrutin 7987 : 48 votants sur 48 = 100 % ; 8279 : 48 sur 48 (46 pour, 2 abst.) ; 1194 : 46 votants")

# 8. Victoire du PSG (31 mai 2025) : 559 interpellations, 2 morts, environ 190 à 200 blessés selon la presse [s. 28]
print("8. PPL n° 1550 : « plus de 500 interpellations » contre 559 ; « centaines de blessés » contre 190 à 200 selon la presse")

# 9. Délai entre la promesse de 2024 (pacte, 22/07/2024) et le dépôt de la PPL n° 3335 (13/10/2026)
from datetime import date
print(f"9. Pacte -> PPL n° 3335 : {(date(2026, 10, 13) - date(2024, 7, 22)).days} jours ; sortie du gouvernement -> dépôt : {(date(2026, 10, 13) - date(2025, 10, 12)).days} jours")
