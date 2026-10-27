"""PS, axe 5 (sécurité, ordre public et libertés) : calculs de la fiche.

- Auteur : sous-agent Opus, étapes 3 à 5
- Statut : brouillon (étapes 3 à 5)
- Données arrêtées au : 2026-10-27
- Fiche : 02-partis/ps/axes/5-securite-libertes.md
Chaque valeur d'entrée renvoie au numéro de source de la fiche (« s. n »). Calculs par nos soins.
"""
from datetime import date

# 1. Contrôles d'identité, Cour des comptes 2023 (données 2021) [s. 31]
total, police_route, gendarmerie_route = 47.0, 6.6, 8.3  # millions
print(f"1. Contrôles hors routier : {total - police_route - gendarmerie_route:.1f} M (PPL n° 1841 : 32 M)")

# 2. Cannabis : « 8 millions en consomment régulièrement » [C-PS-01] contre OFDT 2025 (données 2023) [s. 35]
projet, reguliers, annee, quotidiens = 8.0, 1.4, 5.0, 0.9
print(f"2. Rapport 8 M / usagers réguliers : {projet / reguliers:.1f} ; / usagers dans l'année : {projet / annee:.1f} ; / quotidiens : {projet / quotidiens:.1f}")

# 3. Justice, Cepej 2024 (données 2022), note USM [s. 28] et relais Actu-Juridique pour l'Espagne [s. 30]
fr, de, es, moy, med, grp_c = 77.2, 136.1, 96.8, 85.40, 74.80, 92.1
for nom, v in [("Allemagne", de), ("Espagne", es), ("moyenne", moy), ("médiane", med), ("moyenne groupe C", grp_c)]:
    print(f"3. France contre {nom} ({v} €) : {100 * (fr / v - 1):+.1f} %")
print(f"   Juges : 11,3 contre moyenne 21,9 : {11.3 / 21.9:.2f} ; contre médiane 17,6 : {11.3 / 17.6:.2f}")

# 4. Engagement 52 de 2012 : 1 000 postes par an (police, gendarmerie, justice) [C-PS-69] ; rapport IGA-IGF [s. 27]
promis = 1000 * 5
realises_pg = 8837  # police et gendarmerie, 2013-2017, dont 2 286 prévus en loi de finances 2017
print(f"4. Promis sur 5 ans (trois administrations) : {promis} ; police et gendarmerie seules : {realises_pg}, soit {realises_pg / promis:.2f} fois, {realises_pg / 5:.0f} par an")
print(f"   Part de 2017 (prévisionnelle) : {100 * 2286 / realises_pg:.0f} %")

# 5. Effectifs police et gendarmerie, Cour des comptes 2026 [s. 25]
fin_2024, hausse = 252_300, 10_600
print(f"5. Hausse 2016-2024 : {100 * hausse / (fin_2024 - hausse):.1f} % (Cour : 4,4 %)")

# 6. Magistrats, programmation 2023-2027 [s. 42]
print(f"6. Magistrats arrivés au 1er déc. 2025 : 489 / 1 500 = {100 * 489 / 1500:.1f} % ; PLF 2027 : +287 [s. 43]")

# 7. Sécurité civile : contre-budget 2027 « doubler » pour 1 Md€ [C-PS-33] ; 1 Md€ ajouté est du même ordre que le budget actuel, donc le double ; programme 161, PLF 2026 [s. 46]
cp_2026, ae_2026 = 882.7, 994.9
print(f"7. 1 Md€ contre {cp_2026} M€ de CP : {100 * (1000 / cp_2026 - 1):+.0f} % ; contre {ae_2026} M€ d'AE : {100 * (1000 / ae_2026 - 1):+.0f} %")

# 8. Violences sexuelles et sexistes : 3 Md€ par an (PPL n° 3106, art. 68) ; 1,5 Md€ annoncés par le gouvernement (relais unique) [s. 45] ; adoption [s. 44] ; coût CIIVISE 9,7 Md€ [s. 37]
print(f"8. Écart programmation / annonce : {3.0 - 1.5:.1f} Md€ par an ; 3 Md€ = {100 * 3.0 / 9.7:.0f} % du coût annuel estimé par la CIIVISE")

# 9. Refus d'obtempérer routiers [C-PS-54, p. 3] contre SSMSI (relais) [s. 39]
print(f"9. 28 200 (2025) contre « environ 30 000 » : {100 * (28200 / 30000 - 1):+.0f} % ; moyenne 2016-2023 de 25 700 : {100 * (25700 / 30000 - 1):+.0f} %")

# 10. Tirs de LBD, IGPN 2025 (relais) [s. 40] : 5 065, +25 % sur un an
print(f"10. Tirs de LBD 2024 déduits : {5065 / 1.25:.0f}")

# 11. Ancienneté des actes 2012-2017 au 2026-10-27 (règle du socle : plus de dix ans = contexte)
ref = date(2026, 10, 27)
actes = {
    "abandon du récépissé (discours du 19 sept. 2012)": date(2012, 9, 19),
    "interdiction des grenades offensives (13 nov. 2014)": date(2014, 11, 13),
    "loi renseignement (24 juil. 2015)": date(2015, 7, 24),
    "déclaration de l'état d'urgence (14 nov. 2015)": date(2015, 11, 14),
    "amendement récépissé rejeté (25 fév. 2016)": date(2016, 2, 25),
    "loi du 3 juin 2016": date(2016, 6, 3),
    "loi du 21 juil. 2016 (4e prorogation)": date(2016, 7, 21),
    "loi du 19 déc. 2016 (5e prorogation)": date(2016, 12, 19),
    "loi du 28 fév. 2017 (article L. 435-1)": date(2017, 2, 28),
}
for nom, d in actes.items():
    ans = (ref - d).days / 365.25
    print(f"11. {nom} : {ans:.1f} ans, {'plus' if ans > 10 else 'moins'} de dix ans")

# 12. CEDH, Seydi et autres c. France, 26 juin 2025 [s. 33] : 1 violation sur 6 contrôles examinés
print(f"12. Contrôles jugés discriminatoires : 1 sur 6, {100 / 6:.0f} %")

# 13. Participation du groupe SOC au scrutin 805 : 10 votants ; groupe de 66 députés selon le parti (nov. 2024) [C-PS-34]
print(f"13. Scrutin 805 : 10 votants sur 66, {100 * 10 / 66:.0f} %")

# 14. Crimes et délits racistes, xénophobes ou antireligieux 2024 (SSMSI, relais) [s. 38] : 9 350 contre « plus de 9 300 »
print(f"14. Écart : {100 * (9350 / 9300 - 1):+.1f} %")
