# Ordres de grandeur "calcul par nos soins", effets distributifs v2, Renaissance
# 1. Droit au brut : suppression de la part salariale vieillesse (6,90 % plafonnée + 0,40 % déplafonnée)
PMSS = 4005.0            # plafond mensuel 2026
SMIC = 12.31 * 151.67    # Smic brut mensuel au 1er juin 2026
MED_BRUT = 2200 / 0.795  # brut correspondant à 2 200 € nets (convention de la fiche, taux salarié ~20,5 %)
def gain(b):
    return 0.069 * min(b, PMSS) + 0.004 * b
for nom, b in [("Smic", SMIC), ("median", MED_BRUT), ("plafond", PMSS), ("2 plafonds", 2*PMSS)]:
    g = gain(b)
    print(f"droit au brut {nom}: brut {b:,.0f} gain {g:,.0f} EUR/mois, {12*g:,.0f} EUR/an, {g/b*100:.2f} % du brut")
g_med = gain(MED_BRUT)
print(f"  median apres IR marginal 11 %: {g_med - g_med*0.9*0.11:,.0f} (base imposable = gain x 0,9 abattement 10 %)")
print(f"  Smic, reprise prime d'activite au plus 40 % : gain net >= {gain(SMIC)*(1-0.4015):,.0f}")
# 2. Annee blanche 2028 : perte pour une pension au niveau moyen (1 666 EUR brut fin 2023, Drees 2025)
for infl in (0.01, 0.02, 0.03):
    print(f"annee blanche pension 1 666 brut, revalo evitee {infl:.0%}: {1666*infl*12:,.0f} EUR/an")
print(f"part des pensions dans le rendement OFCE: {3.7/5.0:.0%}")
# 3. Successions : gain maximal par enfant de l'abattement 100 000 -> 150 000 (bareme ligne directe)
tranches = [(8072, .05), (12109, .10), (15932, .15), (552324, .20), (902838, .30), (1805677, .40), (float('inf'), .45)]
def droits(base):
    t, bas = 0.0, 0.0
    for haut, taux in tranches:
        if base > bas:
            t += (min(base, haut) - bas) * taux
        bas = haut
    return t
for part in (120000, 150000, 300000, 1000000, 2000000):
    avant, apres = droits(part - 100000), droits(max(part - 150000, 0))
    print(f"succession part {part:,}: droits {avant:,.0f} -> {apres:,.0f}, gain {avant-apres:,.0f}")
# 4. Plan 150 Md : si proportionnel, part des retraites dans les 100 Md sociaux
print(f"retraites / social = {23.4/57.0:.1%} -> {100*23.4/57.0:.0f} Md")
# 5. Impots de production : poids de l'industrie manufacturiere dans le gain vs economie marchande
print("manufacturier 32 % du gain, environ 2x son poids (France Strategie)")
