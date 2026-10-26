"""LFI, axe 5 (sécurité, ordre public et libertés) : calculs de la fiche.

- Auteur : sous-agent Opus, étapes 3 à 5
- Statut : brouillon (étapes 3 à 5)
- Données arrêtées au : 2026-10-26
- Fiche : 02-partis/lfi/axes/5-securite-libertes.md
Chaque valeur d'entrée renvoie au numéro de source de la fiche.
"""
from datetime import date

def mois(d1, d2):
    return (d2.year - d1.year) * 12 + (d2.month - d1.month) + 1

# 1. Décès après tirs sur véhicules (refus d'obtempérer), étude Esprit 2022 relayée par la QE n° 549 [s. 31]
avant = 4; p_avant = mois(date(2011, 7, 1), date(2017, 2, 1))
apres = 25; p_apres = mois(date(2017, 3, 1), date(2022, 10, 1))
t_av = avant / p_avant * 12; t_ap = apres / p_apres * 12
print(f"1. Périodes : {p_avant} et {p_apres} mois ; taux annuels {t_av:.2f} et {t_ap:.2f} ; rapport {t_ap / t_av:.1f}")
# Prolongation jusqu'à fin 2025, sources mêlées : 3 décès liés à un refus d'obtempérer en 2023, 0 en 2024, 0 en 2025 [s. 32, 33]
# (hypothèse : aucun décès de novembre à décembre 2022 hors du décompte de l'étude ; hypothèse favorable au rapport)
apres_2025 = apres + 3 + 0 + 0; p_2025 = mois(date(2017, 3, 1), date(2025, 12, 1))
t_2025 = apres_2025 / p_2025 * 12
print(f"   Jusqu'à fin 2025 : {apres_2025} décès sur {p_2025} mois, {t_2025:.2f} par an, rapport {t_2025 / t_av:.1f}")

# 2. Tirs de la police nationale sur véhicules en mouvement [s. 31]
tirs = {2012: 116, 2016: 137, 2017: 202, 2020: 153, 2021: 157, 2022: 138, 2023: 79}
print(f"2. 2016-2017 : {100*(tirs[2017]/tirs[2016]-1):+.0f} % ; 2017-2023 : {100*(tirs[2023]/tirs[2017]-1):+.0f} % ; 2012-2022 : {100*(tirs[2022]/tirs[2012]-1):+.0f} %")

# 3. Enquêtes IGPN pour usage de la force [s. 33]
ens = {2019: 868, 2023: 519, 2024: 428, 2025: 322}
print(f"3. Usage de la force 2019-2025 : {100*(ens[2025]/ens[2019]-1):+.0f} % ; 2024-2025 : {100*(ens[2025]/ens[2024]-1):+.0f} %")
bles = {2023: 108, 2024: 72, 2025: 86}
print(f"   Blessés graves 2024-2025 : {100*(bles[2025]/bles[2024]-1):+.0f} %")

# 4. Amendement II-3202 : part de l'action 01 du programme 176 [C-LFI-61 ; s. 46]
transfert = 1.2e9; action01_2025 = 1_831_861_889
print(f"4. Transfert / action 01 (LFI 2025) : {100*transfert/action01_2025:.1f} %")
redeploy = 7000 + 24000 + 10000
print(f"   Agents redéployés selon l'amendement : {redeploy} pour une cible de 40 000")

# 5. CEPEJ 2024 (données 2022) [s. 39]
print(f"5. Juges : 11,3 contre moyenne 21,9 : {11.3/21.9:.2f} ; contre médiane 17,6 : {11.3/17.6:.2f}")
print(f"   Budget par habitant : 77,20 contre 85,40 : {100*(77.20/85.40-1):+.1f} %")

# 6. Magistrats : rythme de la programmation [s. 58]
print(f"6. Postes de magistrats pourvus au 1er déc. 2025 : 489 sur 1 500, soit {100*489/1500:.0f} %")

# 7. Participation et unanimité du groupe LFI-NFP [s. 65]
print(f"7. Scrutin 805 : 26 votants sur 71, {100*26/71:.0f} % ; scrutin 7987 : 69 contre sur 69 votants")
