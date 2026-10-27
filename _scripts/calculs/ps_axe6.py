"""Calculs de la fiche PS, axe 6 (Institutions, démocratie et Europe), étapes 3 à 5.

Rédigé le 2026-10-27, sous-agent Opus. Chaque bloc renvoie à la source de la fiche
`02-partis/ps/axes/6-institutions-democratie-europe.md` (numéros entre crochets).
Calculs par nos soins ; aucune donnée n'est inventée ici.
"""
from datetime import date

ARRET = date(2026, 10, 27)


def pct(a, b):
    return 100 * a / b


print("1. Règle des 60 % sur les scrutins de l'axe (03-sources/scrutins-positions.md)")
scrutins = {
    "7454 Corse": (41, 5, 19),
    "4244 Mercosur": (29, 1, 0),
    "8611 Schengen": (0, 37, 0),
    "5313 UE-États-Unis": (16, 0, 0),
    "3182 Nouvelle-Calédonie (réserve)": (56, 4, 6),
}
EFFECTIF_SOC = 69  # 00-perimetre.md, au 2026-10-27
for nom, (p, c, a) in scrutins.items():
    v = p + c + a
    maxi = max(p, c, a)
    pos = ["pour", "contre", "abstention"][[p, c, a].index(maxi)]
    regle = pos if maxi / v > 0.60 else "divisé"
    print(f"  {nom}: {v} votants, part majoritaire {pct(maxi, v):.1f} % ({pos}) -> {regle} ; "
          f"votants / effectif d'octobre 2026 = {pct(v, EFFECTIF_SOC):.1f} %")

print("\n2. Congrès (article 89) : majorité des trois cinquièmes")
CONGRES = 577 + 348
seuil = -(-3 * CONGRES // 5)
gauche_soc = 69 + 62  # SOC (Assemblée) + SER (Sénat), 00-perimetre.md
print(f"  {CONGRES} parlementaires, seuil {seuil} ; SOC + SER = {gauche_soc}, "
      f"soit {pct(gauche_soc, CONGRES):.1f} % du Congrès et {pct(gauche_soc, seuil):.1f} % du seuil")

print("\n3. Homicides UE / États-Unis (Projet : « près de 3 fois moins nombreux »)")
hom_ue_2023 = 3930          # Eurostat, 2025-04-23 [S]
pop_ue_2023 = 448.4e6       # Eurostat, 2023-07-11 (première estimation)
taux_ue = hom_ue_2023 / pop_ue_2023 * 1e5
taux_us_2023 = 5.7          # FBI 2023, relais presse
print(f"  UE 2023 : {taux_ue:.2f} pour 100 000 ; États-Unis 2023 : {taux_us_2023} ; "
      f"rapport {taux_us_2023 / taux_ue:.1f}")
print(f"  Avec la population révisée 447,6 M : rapport {taux_us_2023 / (hom_ue_2023 / 447.6e6 * 1e5):.1f}")

print("\n4. Espérance de vie 2024")
ev_ue, ev_us = 81.5, 79.0
print(f"  écart UE - États-Unis : {ev_ue - ev_us:.1f} an(s) (81,7 en estimation provisoire : {81.7 - ev_us:.1f})")

print("\n5. Budget de l'UE à 3 % du PIB européen (ordre de grandeur)")
pib_ue_2025 = 18_800        # Md€, Eurostat relayé, 2026-08-06
cfp_actuel_pct = 1.13       # % du RNB, CFP 2021-2027 (Sénat, rapport n° 532)
cfp_propose_pct = 1.26      # % du RNB, proposition 2028-2034
part_france_pib = 15.8      # % du PIB de l'UE, Eurostat relayé
b3 = pib_ue_2025 * 0.03
bact = pib_ue_2025 * cfp_actuel_pct / 100
print(f"  3 % de {pib_ue_2025} Md€ = {b3:.0f} Md€ par an ; niveau actuel ≈ {bact:.0f} Md€ "
      f"(RNB assimilé au PIB) ; multiplicateur {3 / cfp_actuel_pct:.2f} (proposition de la Commission : "
      f"{3 / cfp_propose_pct:.2f})")
print(f"  hausse ≈ {b3 - bact:.0f} Md€ par an ; si elle était financée au prorata du PIB, part française "
      f"≈ {(b3 - bact) * part_france_pib / 100:.0f} Md€ par an (hypothèse, le Projet prévoit des ressources propres)")

print("\n6. Emprunt commun de 500 Md€ rapporté aux précédents")
for nom, m in {"NextGenerationEU (prix 2018)": 750, "SAFE (2025, prêts)": 150, "prêt Ukraine (déc. 2025)": 90}.items():
    print(f"  500 / {m} ({nom}) = {500 / m:.2f}")

print("\n7. Participation et abstention")
print(f"  municipales 2020, 1er tour : abstention {100 - 44.66:.2f} %")
print(f"  législatives 2022 -> 2024 : {66.71 - 47.51:+.2f} points ; européennes 2019 -> 2024 : {51.49 - 50.1:+.2f} points")
print(f"  abstention systématique (Insee) 2002 -> 2022 : {16 - 12:+d} points ; 2007 -> 2022 : {16 - 9:+d} points")
print(f"  Cevipof : 22 % en février 2026, « moins 4 points sur un an » -> {22 + 4} % en 2025 (concorde avec les 26 % de la PPL n° 2031)")

print("\n8. Recours au 49.3 par législature (Assemblée nationale)")
leg = {"IXe (1988-1993)": 39, "XIVe (2012-2017)": 6, "XVe (2017-2022)": 1, "XVIe (2022-2024)": 23}
for k, v in leg.items():
    print(f"  {k}: {v}")
print(f"  XIVe : 6 recours sur 2 textes, soit {6 / 2:.0f} par texte")

print("\n9. Ancienneté des actes au 2026-10-27 (règle des dix ans)")
actes = {
    "4 projets de révision déposés (14/03/2013)": date(2013, 3, 14),
    "réponse ministérielle laïcité (13/05/2014)": date(2014, 5, 13),
    "1er 49.3 loi Macron (février 2015)": date(2015, 2, 17),
    "dernier 49.3 loi Macron (09/07/2015)": date(2015, 7, 9),
    "rejet de la Charte des langues au Sénat (27/10/2015)": date(2015, 10, 27),
    "abandon de la révision « protection de la Nation » (30/03/2016)": date(2016, 3, 30),
    "CSM adopté dans les mêmes termes (avril 2016)": date(2016, 4, 30),
    "49.3 loi travail, 2e lecture (05/07/2016)": date(2016, 7, 5),
    "adoption définitive loi travail (20/07/2016)": date(2016, 7, 20),
    "fin du mandat (14/05/2017)": date(2017, 5, 14),
}
for k, d in actes.items():
    ans = (ARRET - d).days / 365.25
    print(f"  {k}: {ans:.1f} ans -> {'plus de dix ans' if ans > 10 else 'moins de dix ans'}")

print("\n10. Dotations aux collectivités")
print("  part forfaitaire de la DGF réduite de 11,2 Md€ entre 2013 et 2017 (Cour des comptes, relais) : "
      "engagement 54 de 2012, dotations « à leur niveau actuel »")

print("\n11. Financement des associations (Tchernonog, relais RTES)")
print(f"  subventions : 34 % -> 20 % ({20 - 34:+d} points) ; commande publique : 17 % -> 29 % ({29 - 17:+d} points), 2005 -> 2020")
