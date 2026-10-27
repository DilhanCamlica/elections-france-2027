"""PS, axe 4 (pouvoir d'achat et fiscalité) : calculs des étapes 3 à 5.

Rédigé le 2026-10-27 par un sous-agent Opus ; complété le 2026-10-27 à l'application
de l'arbitrage de l'étape 6 (taux de CSG au Smic, taille relative des groupes IPP). Chaque bloc imprime un résultat
repris dans 02-partis/ps/axes/4-pouvoir-achat-fiscalite.md avec la mention
« calcul par nos soins ». Les numéros entre crochets renvoient à la liste des
sources de la fiche. Les montants du parti viennent de la PPL n° 3252 [C-PS-48].

Limites assumées : le gain de CSG est un gain brut de CSG ; il ne modélise ni
la prime d'activité (qui baisse quand le revenu d'activité monte), ni l'impôt
sur le revenu (la part déductible de la CSG baisse), ni le décalage de deux ans
du revenu fiscal de référence (RFR) ; c'est un contrôle d'ordre de grandeur.
"""

# --- Données publiques ----------------------------------------------------
smic_brut_jan26, smic_net_jan26 = 1823.03, 1443.11   # info.gouv, 1er janvier 2026 [38]
smic_brut_jun26, smic_net_jun26 = 1867.02, 1477.93   # info.gouv, 1er juin 2026 [39]
csg_actuelle, csg_non_deduc, crds, assiette = 0.092, 0.024, 0.005, 0.9825  # Urssaf [40]

# --- Barème de la PPL n° 3252, article 1er (RFR pour une part) ----------
# (borne haute du RFR, taux) ; au-dessus de 32 004 € et jusqu'à 50 004 € : 9,2 % ;
# au-delà de 50 004 € : 10,2 %. Seuils majorés de 2 971 € par demi-part.
bareme = [(8196, .0025), (14004, .0040), (18000, .0055), (21000, .0070),
          (23004, .0085), (24996, .0100), (26496, .0200), (27996, .0425),
          (29256, .0650), (32004, .0875)]
MAJ_DEMI_PART = 2971


def taux_csg(rfr, parts):
    maj = (parts - 1) * 2 * MAJ_DEMI_PART
    for borne, t in bareme:
        if rfr < borne + maj:
            return t
    if rfr <= 50004 + maj:
        return csg_actuelle
    return 0.102


ratio_net = smic_net_jun26 / smic_brut_jun26          # net / brut au Smic


def rfr_annuel(brut_mensuel):
    """RFR approché : net imposable (net + CSG non déductible + CRDS) x 12, moins 10 %."""
    net = brut_mensuel * ratio_net
    net_imposable = net + (csg_non_deduc + crds) * assiette * brut_mensuel
    return net_imposable * 12 * 0.9


def gain_mensuel(brut_mensuel, t):
    return (csg_actuelle - t) * assiette * brut_mensuel


print("=== Smic : montants du parti contre Smic actuel ===")
for cible in (1690, 1700, 1600):
    print(f"{cible} € net : +{cible - smic_net_jan26:.2f} € / +{(cible / smic_net_jan26 - 1) * 100:.1f} % "
          f"(janv. 2026) ; +{cible - smic_net_jun26:.2f} € / +{(cible / smic_net_jun26 - 1) * 100:.1f} % (juin 2026)")
print("écart 1 690 / 1 700 :", round((1700 - 1690) / 1690 * 100, 2), "%")

print("\n=== CSG progressive : contrôle des cas types de la PPL ===")
brut_1700 = 1700 / ratio_net
cas = [
    ("célibataire au Smic", [smic_brut_jun26], 1, 125),
    ("couple, deux Smic, sans enfant", [smic_brut_jun26] * 2, 2, None),
    ("couple, deux Smic, un enfant", [smic_brut_jun26] * 2, 2.5, 230),
    ("couple, deux salaires de 1 700 € net, sans enfant", [brut_1700] * 2, 2, 200),
]
for nom, bruts, parts, annonce in cas:
    rfr = sum(rfr_annuel(b) for b in bruts)
    t = taux_csg(rfr, parts)
    gain = sum(gain_mensuel(b, t) for b in bruts)
    print(f"{nom} : RFR approché {rfr:,.0f} € pour {parts} parts -> taux {t * 100:.2f} % ; "
          f"gain de CSG {gain:.0f} € par mois" + (f" (annoncé : {annonce} €)" if annonce else ""))
# taux annoncé au Smic : 0,85 % (tranche e, RFR de 21 000 à 23 004 € pour une part)
print("gain au Smic au taux annoncé de 0,85 % :", round(gain_mensuel(smic_brut_jun26, .0085)), "€ par mois")
print("brut mensuel qui place un célibataire à 21 000 € de RFR :", round(21000 / 12 / 0.9 /
      (ratio_net + (csg_non_deduc + crds) * assiette)), "€")

print("\n=== Smic à 1 700 € net : part de la CSG et part du salaire brut ===")
ratio_sans_csg = ratio_net + csg_actuelle * assiette      # net hors CSG / brut
for t in (.0055, .0085):
    ratio_t = ratio_sans_csg - t * assiette
    net_avec_csg_seule = smic_brut_jun26 * ratio_t
    brut_requis = 1700 / ratio_t
    print(f"CSG à {t * 100:.2f} % : net au Smic actuel {net_avec_csg_seule:.2f} € ; brut requis pour 1 700 € net "
          f"{brut_requis:.2f} €, soit +{(brut_requis / smic_brut_jun26 - 1) * 100:.1f} % de Smic brut")
print("hausse de Smic brut sans baisse de CSG pour 1 700 € net :",
      round((1700 / ratio_net / smic_brut_jun26 - 1) * 100, 1), "%")

print("\n=== Successions (IGS) ===")
igs, annees = 400, 2040 - 2025 + 1
dmtg_2024, succ_2023, cae = 20.8, 16.6, 12.0
print("rendement annuel moyen de l'IGS :", round(igs / annees, 1), "Md€ sur", annees, "ans")
print("rapport aux DMTG 2024 :", round(igs / annees / dmtg_2024, 2), "; aux successions 2023 :",
      round(igs / annees / succ_2023, 2))
print("si supplément : rapport au supplément du CAE (12 Md€) :", round(igs / annees / cae, 2))
print("cumul 2025-2040 au niveau des DMTG 2024 :", round(dmtg_2024 * annees), "Md€ ; avec +12 Md€ CAE :",
      round((dmtg_2024 + cae) * annees), "Md€")

print("\n=== Diagnostic ===")
print("500 fortunes : 2005-2025", round(1128 / 170, 1), "fois ; 2003-2024", round((1128 + 100) / 124, 1), "fois")
print("hausse de TVA dans 70 c de hausse TTC du gazole :", round(0.70 / 6, 3), "€ (TVA = TTC / 6)")
dens = 0.845   # densité du gazole, kg/L (valeur usuelle, hypothèse)
print("marge de raffinage (relais DGEC) : février", round(40 * dens / 10, 1), "c/L ; septembre",
      round(235 * dens / 10, 1), "c/L ; rapport", round(235 / 40, 1))
print("taux implicite IS : PME/GE", round(21.4 / 14.3, 2), "; ETI/GE", round(17.8 / 14.3, 2))

print("\n=== Effets distributifs ===")
foyers = 40700 / 0.001
print("foyers fiscaux 2022 (0,1 % = 40 700) :", round(foyers / 1e6, 1), "millions ; 1 800 foyers =",
      round(1800 / foyers * 100, 4), "% des foyers")

print("\n=== Compléments ===")
pib_2025 = 3460.5 / 1.157          # Insee : dette 3 460,5 Md€ = 115,7 % du PIB (fiche 1, sources 34 et 40)
print("PIB 2025 déduit :", round(pib_2025), "Md€ ; 500 fortunes 2025 / PIB 2025 :", round(1128 / pib_2025 * 100, 1), "%")
print("PPL n° 3252, 10 Md€ par an sur 16 ans :", 10 * annees, "Md€ contre 400 Md€ (IGS du Projet)")
for annonce, recalc in ((125, 159), (230, 301), (200, 0)):
    print(f"exemple annoncé {annonce} € contre {recalc} € reconstitués : écart {(recalc - annonce) / annonce * 100:+.0f} %")

print("\n=== Étape 6 (arbitrage n° 6) : taux de CSG au Smic, RFR contre brut annuel ===")
# Repris du contrôle sur pièces fait pour l'arbitrage (2026-10-27), calcul par nos soins.
# Cas : célibataire à une part. Smic brut au 1er janvier 2026 : 1 823,03 € (décret
# n° 2025-1228) [38 ; 85] ; au 1er juin 2026 : 1 867,02 € [39 ; 86]. RFR approché :
# net imposable (net + CSG non déductible 2,4 % + CRDS 0,5 % sur 98,25 % du brut),
# moins l'abattement forfaitaire de 10 %. Le barème lit le RFR par part (art. 1er
# de la PPL n° 3252 [C-PS-48]).
for nom, brut_m, net_m in (("Smic janvier 2026", smic_brut_jan26, smic_net_jan26),
                           ("Smic juin 2026", smic_brut_jun26, smic_net_jun26)):
    brut_a, net_a = 12 * brut_m, 12 * net_m
    net_imp = net_a + (csg_non_deduc + crds) * assiette * brut_a
    rfr = 0.9 * net_imp
    print(f"{nom} : RFR {rfr:,.0f} € -> {taux_csg(rfr, 1) * 100:.2f} % ; "
          f"brut annuel pris pour RFR {brut_a:,.0f} € -> {taux_csg(brut_a, 1) * 100:.2f} %")
print("Lecture : 0,55 % sur la base légale (RFR) ; 0,85 %, taux de l'exposé, seulement si le "
      "brut annuel tient lieu de RFR (inférence : la méthode de l'exposé n'est pas publiée).")

print("\n=== Étape 6 (arbitrage n° 5) : taille des groupes de la note IPP n° 92 ===")
# 0,1 % des foyers en 2016 : environ 37 800 ; sommet de la note : 75 foyers [87] (chiffres du relecteur).
print("0,1 % (37 800 foyers) / 75 foyers :", round(37800 / 75), "fois")
