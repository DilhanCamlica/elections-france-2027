"""Calculs de la fiche LR, axe 6 (Institutions, démocratie et Europe), étapes 3 à 5.

Rédigé le 2026-10-27, sous-agent Opus. Chaque bloc renvoie à la source de la fiche
`02-partis/lr/axes/6-institutions-democratie-europe.md` (numéros entre crochets).
Calculs par nos soins ; aucune donnée n'est inventée ici.
"""
from datetime import date

ARRET = date(2026, 10, 27)


def pct(a, b):
    return 100 * a / b


print("1. Règle des 60 % sur les scrutins de l'axe, groupe DR (03-sources/scrutins-positions.md)")
scrutins = {
    "7454 Corse": (1, 34, 10),
    "4244 Mercosur": (11, 0, 0),
    "8611 Schengen": (9, 1, 5),
    "5313 UE-États-Unis": (4, 0, 0),
    "3182 Nouvelle-Calédonie (réserve)": (43, 0, 0),
}
EFFECTIF_DR = 48  # 00-perimetre.md, au 2026-10-27
for nom, (p, c, a) in scrutins.items():
    v = p + c + a
    maxi = max(p, c, a)
    pos = ["pour", "contre", "abstention"][[p, c, a].index(maxi)]
    regle = pos if maxi / v > 0.60 else "divisé"
    print(f"  {nom}: {v} votants, part majoritaire {pct(maxi, v):.1f} % ({pos}) -> {regle} ; "
          f"votants / effectif d'octobre 2026 = {pct(v, EFFECTIF_DR):.1f} %")

print("\n2. Dernier référendum national (29 mai 2005) : « plus de vingt ans » [C-LR-13, p. 1]")
d = (ARRET - date(2005, 5, 29)).days
print(f"  {d} jours, soit {d / 365.25:.1f} ans au {ARRET}")

print("\n3. Seuil du RIP : un dixième puis un vingtième des inscrits (Insee, 11 février 2026) [8]")
INSCRITS = 50_187_093
print(f"  1/10 = {INSCRITS / 10:,.0f} ; 1/20 = {INSCRITS / 20:,.0f} "
      f"(le projet écrit environ 4,8 et 2,4 millions ; écart {pct(INSCRITS / 10 - 4.8e6, 4.8e6):.1f} %)")

print("\n4. Conseil constitutionnel, bilan statistique au 30 juin 2026 [4]")
DC = dict(conformite=464, ncp=407, nct=20, autres=10)
tot_dc = sum(DC.values())
print(f"  DC depuis 1959 : {tot_dc} décisions ; au moins une censure (partielle ou totale) : "
      f"{DC['ncp'] + DC['nct']} = {pct(DC['ncp'] + DC['nct'], tot_dc):.1f} % ; totale : {pct(DC['nct'], tot_dc):.1f} %")
# Solutions QPC (onglet « Solutions DC_QPC ») : 1075 solutions pour 1091 décisions
qpc_nct = 143 + 74 + 1 + 40 + 1 + 1
qpc_ncp = 41 + 18 + 1 + 5 + 1 + 2 + 9
qpc_date = 3 + 1 + 1
qpc_sol = 1075
print(f"  QPC 2010-30/06/2026 : {qpc_sol} solutions ; non-conformité totale {qpc_nct} ({pct(qpc_nct, qpc_sol):.1f} %), "
      f"partielle {qpc_ncp} ({pct(qpc_ncp, qpc_sol):.1f} %), de date à date {qpc_date} ; "
      f"ensemble {pct(qpc_nct + qpc_ncp + qpc_date, qpc_sol):.1f} %")
dc_par_an = {2017: 14, 2018: 19, 2019: 19, 2020: 16, 2021: 21, 2022: 13, 2023: 15, 2024: 12, 2025: 26, "S1 2026": 6}
qpc_par_an = {2017: 75, 2018: 64, 2019: 61, 2020: 46, 2021: 75, 2022: 67, 2023: 45, 2024: 42, 2025: 55, "S1 2026": 31}
print(f"  2017 à juin 2026 : {sum(dc_par_an.values())} décisions DC, {sum(qpc_par_an.values())} décisions QPC")

print("\n5. Loi immigration du 26 janvier 2024 (2023-863 DC, communiqué) [6]")
print(f"  35 articles censurés, dont 32 pour la procédure : {pct(32, 35):.1f} % ; 3 au fond : {pct(3, 35):.1f} %")

print("\n6. Révision par l'article 89 : Sénat et Congrès")
SENAT, LR_SEN, LR_CENTRISTES = 348, 124, 187  # 00-perimetre.md ; fiche axe 3, source 68
maj_sen = SENAT // 2 + 1
print(f"  Sénat : majorité absolue {maj_sen} ; groupe LR {LR_SEN} = {pct(LR_SEN, SENAT):.1f} % ; "
      f"LR et centristes {LR_CENTRISTES} = {pct(LR_CENTRISTES, SENAT):.1f} %")
CONGRES = 577 + 348
seuil = -(-3 * CONGRES // 5)
lr_cong = EFFECTIF_DR + LR_SEN
print(f"  Congrès {CONGRES}, trois cinquièmes = {seuil} ; DR + LR = {lr_cong} = {pct(lr_cong, CONGRES):.1f} % "
      f"du Congrès, {pct(lr_cong, seuil):.1f} % du seuil")
maj_an = 577 // 2 + 1
print(f"  Assemblée : majorité absolue {maj_an} ; groupe DR {EFFECTIF_DR} = {pct(EFFECTIF_DR, 577):.1f} %")
print("  Rejet du PJLC Corse par le Sénat le 26-27 octobre 2026 : 181 contre 134 ; "
      f"part des contre parmi les exprimés {pct(181, 181 + 134):.1f} %")

print("\n7. Calendrier « rentrée 2027 » [C-LR-15] (dates officielles : 18 avril et 2 mai 2027 ; fin du mandat le 14 mai) [9]")
prise = date(2027, 5, 14)
for ref in (date(2027, 9, 19), date(2027, 10, 3)):
    print(f"  du {prise} au référendum hypothétique du {ref} : {(ref - prise).days} jours")
print(f"  délais de l'article 42 (six semaines puis quatre semaines) : {6 * 7 + 4 * 7} jours au minimum, "
      "hors procédure accélérée")

print("\n8. Scrutin 8611 : groupe DR, 9 pour sur 15 votants")
print(f"  {pct(9, 15):.1f} % : la règle exige plus de 60 % -> divisé ; le groupe avait annoncé un vote pour")

print("\n9. RIP Aéroports de Paris (fiche Renaissance) : 1 093 030 soutiens, 4 717 396 requis")
print(f"  vingtième de l'époque = {4_717_396 / 2:,.0f} ; soutiens / vingtième = {pct(1_093_030, 4_717_396 / 2):.1f} %")
