# Ordres de grandeur "calcul par nos soins", RN, axe 4 (pouvoir d'achat et fiscalite).
# Etapes 3 a 5 (Q1, Q3 dont effets distributifs v2, Q4). Sources citees dans la fiche
# 02-partis/rn/axes/4-pouvoir-achat-fiscalite.md (numeros entre crochets).

def p(*a):
    print(*a)

p("=== Q1 : verification ===")
# Insee, comptes de la Nation 2025 [29] : pouvoir d'achat du RDB par UC, evolution annuelle en %
pa = {2017: 1.2, 2018: 0.3, 2019: 2.0, 2020: -0.3, 2021: 2.8, 2022: -0.3, 2023: 0.4, 2024: 2.2, 2025: -0.7}
def cumul(a, b):
    x = 1.0
    for y in range(a, b + 1):
        x *= 1 + pa[y] / 100
    return (x - 1) * 100
p(f"PA par UC cumule 2018-2025 : {cumul(2018, 2025):.1f} % ; 2022-2025 : {cumul(2022, 2025):.1f} % ; 2023-2025 : {cumul(2023, 2025):.1f} %")
# Eurostat nrg_pc_204, menages 2 500-5 000 kWh, EUR/kWh, toutes taxes (I_TAX) et hors taxes (X_TAX) [30]
elec = {"FR": {"2017-S2": (0.1756, 0.1132), "2022-S2": (0.2204, 0.1723), "2024-S2": (0.2926, 0.2223), "2025-S2": (0.2561, 0.1785)},
        "EU": {"2017-S2": (0.2089, 0.1271), "2025-S2": (0.2896, 0.2059)},
        "DE": {"2025-S2": (0.3869, 0.2625)}, "IT": {"2025-S2": (0.2966, 0.2190)}, "ES": {"2025-S2": (0.2669, 0.1840)}}
for g, d in elec.items():
    for t, (ttc, ht) in d.items():
        p(f"  elec {g} {t} : TTC {ttc} ; part taxes {(1-ht/ttc)*100:.1f} %")
fr = elec["FR"]
p(f"elec FR TTC 2017-S2 -> 2025-S2 : {(fr['2025-S2'][0]/fr['2017-S2'][0]-1)*100:.1f} % ; 2022-S2 -> 2025-S2 : {(fr['2025-S2'][0]/fr['2022-S2'][0]-1)*100:.1f} %")
p(f"elec FR / UE 2025-S2 : {(fr['2025-S2'][0]/elec['EU']['2025-S2'][0]-1)*100:.1f} %")
# Gazole, decomposition DGEC au 16/10/2026 (relais) [32] : prix 234,6 ct ; accise 60,7 ; TVA 39,1
prix, accise, tva = 234.6, 60.7, 39.1
p(f"gazole : part des taxes {(accise+tva)/prix*100:.1f} % ; TVA implicite 20 % de {prix-tva:.1f} = {(prix-tva)*0.2:.1f}")
# Prelevements obligatoires Insee [33] : 45,0 % en 2022, 45,3 % en 2017 ; OCDE 46,1 % en 2022 (relais)
p(f"impots de production FR/UE (Eurostat 2024 via FIPECO) : {4.4/2.4:.2f} ; parti 2024 : {4.7/2.5:.2f}")

p("=== Q3 : C3S et impots de production ===")
c3s = {"2023 (prev. PLFSS 2024)": 4.800, "2024 (prev. PLFSS 2025)": 5.195, "2025 (prev. PLFSS 2026)": 5.337, "2026 (prev. PLFSS 2026)": 5.452}
for k, v in c3s.items():
    p(f"  C3S {k} : {v} Md ; 4,8 / rendement = {4.8/v*100:.0f} %")
# CVAE : PLF 2026, baisse du taux maximal de 0,28 a 0,19 % = 1,1 Md (relais) => rendement proportionnel
cvae = 1.1 / (0.28 - 0.19) * 0.28
p(f"CVAE implicite au taux de 0,28 % (hypothese de proportionnalite) : {cvae:.1f} Md")
cfe = 8.0
tot_ind = cfe + cvae + c3s["2026 (prev. PLFSS 2026)"]
p(f"CFE 2024 {cfe} + CVAE {cvae:.1f} + C3S 2026 {c3s['2026 (prev. PLFSS 2026)']} = {tot_ind:.1f} Md ; RN 2026 16,2 ({(16.2/tot_ind-1)*100:.0f} %) ; RN 2027 17,1 ({(17.1/tot_ind-1)*100:.0f} %)")

p("=== Q3 : TVA a 5,5 % sur l'energie ===")
k = 1 - 1.055 / 1.20
p(f"part de la depense TTC perdue en TVA si 20 % -> 5,5 % : {k*100:.2f} %")
# SDES : depense des menages 2023, logement 58 Md (relais) + carburants 54,5 Md (relais) [34]
dep = 58.0 + 54.5
p(f"perte statique sur la depense 2023 ({dep} Md TTC, tout suppose a 20 %) : {dep*k:.1f} Md")
# Parti 2022 : 95 Md de depenses dont 16 Md de TVA a 20 %
p(f"2022 : 95 Md TTC x {k:.3f} = {95*k:.1f} Md ; TVA implicite a 20 % : {95/1.2*0.2:.1f} Md (parti : 16)")
rn = {"2022": 12.0, "2025 brut": 12.0, "2025 net": 10.0, "2026": 10.96, "2026 net du retour TVA 1,82": 10.96 - 1.82, "2027": 12.2}
for kk, v in rn.items():
    p(f"  RN {kk} : {v:.2f} ; ecart a Montaigne 11,3 : {(v/11.3-1)*100:+.0f} % ; a Bercy 16,8 : {(v/16.8-1)*100:+.0f} %")
p(f"Bercy 2024 : 10 + 4,5 + 2,3 = {10+4.5+2.3:.1f} ; part carburants : {10/16.8*100:.0f} %")
p(f"carburants : TVA totale 8 Md (ministre, 2026) x {k/(0.2/1.2):.3f} = perte {8*k/(0.2/1.2):.1f} Md")

p("=== Q3 : ecarts de chiffrage du contre-budget 2026 ===")
spec_slide = 8.4 + 3.0 + 1.3
spec_tab = 8.4 + 3.0 + 0.75
p(f"bloc speculation : avec 1,3 = {spec_slide:.2f} ; avec 0,75 = {spec_tab:.2f} ; sous-total affiche 12,2 (diapositive) et 12,150 (tableau)")
baisses = 24.919 + 18.490 + 0.002 + 1.997
p(f"baisses d'impots et de cotisations du tableau : {baisses:.1f} Md (affiche : 45)")
p(f"recettes nouvelles du tableau : 88,274 - economies ; solde affiche -35,6")
p(f"15 Md par an x 5 ans = {15*5} Md cumules ; 30 Md nets sur le quinquennat = {30/5:.0f} Md par an en moyenne")

p("=== Q3 : rachats d'actions, IFF ===")
p(f"33 % x 34,8 Md (rachats CAC 40 2025, IDEP) = {0.33*34.8:.2f} Md ; base necessaire pour 8,4 Md par an : {8.4/0.33:.1f} Md")
ifi, ifi_isf_perte = 2.3, 4.5
p(f"IFF : si +4 Md est un gain net apres suppression de l'IFI ({ifi}), produit brut >= {4+ifi:.1f} Md, soit {((4+ifi)/ifi_isf_perte-1)*100:.0f} % de plus que la perte ISF->IFI estimee par France Strategie ({ifi_isf_perte})")

p("=== Q3 : IR des moins de 30 ans ===")
p(f"Montaigne 3,6-3,7 contre RN 2,0 : ecart {(3.6/2.0-1)*100:.0f} a {(3.7/2.0-1)*100:.0f} %")
def ir_seul(rni):
    tr = [(11600, 0.0), (29579, 0.11), (84577, 0.30), (181917, 0.41), (1e12, 0.45)]
    imp, bas = 0.0, 0.0
    for haut, t in tr:
        if rni > bas:
            imp += (min(rni, haut) - bas) * t
        bas = haut
    if imp < 1982:
        imp = max(0.0, imp - (897 - 0.4525 * imp))
    return imp
smic_brut_an = 1801.80 * 12  # Smic 2025 (hypothese), revenus 2025
for m in (1, 1.5, 2, 3, 4):
    brut = smic_brut_an * m
    net_imp = brut * 0.80          # hypothese simplificatrice : net imposable = 80 % du brut
    rni = net_imp * 0.90           # abattement de 10 %
    g = ir_seul(rni)
    p(f"  celibataire a {m} Smic : brut {brut:,.0f} ; RNI {rni:,.0f} ; IR evite {g:,.0f} EUR/an ({g/net_imp*100:.1f} % du net imposable)")

p("=== Q3 : successions, exoneration de 300 000 EUR d'immeubles ===")
bareme = [(8072, 0.05), (12109, 0.10), (15932, 0.15), (552324, 0.20), (902838, 0.30), (1805677, 0.40), (1e12, 0.45)]
def droits(part):
    tax = max(0.0, part - 100000)
    d, bas = 0.0, 0.0
    for haut, t in bareme:
        if tax > bas:
            d += (min(tax, haut) - bas) * t
        bas = haut
    return d
cas = [("maison 300 000, 2 enfants", 300000, 0, 2), ("maison 200 000, 1 enfant", 200000, 0, 1),
       ("maison 500 000, 2 enfants", 500000, 0, 2), ("maison 300 000 + 300 000 financier, 2 enfants", 300000, 300000, 2),
       ("maison 180 000, 2 enfants", 180000, 0, 2)]
for nom, immo, autre, n in cas:
    avant = n * droits((immo + autre) / n)
    exo = min(immo, 300000)
    apres = n * droits((immo + autre - exo) / n)
    p(f"  {nom} : droits {avant:,.0f} -> {apres:,.0f} ; gain {avant-apres:,.0f} EUR")

p("=== Effets distributifs : TVA energie ===")
r_d1, r_d10 = 19 / 30, 45 / 30   # Insee, note de conjoncture dec. 2021 (Budget de famille 2017)
for n in (30.0e6, 32.3e6):
    moy = 12.2e9 / n
    p(f"  {n/1e6:.1f} M menages : moyen {moy:.0f} ; D1 ~{moy*r_d1:.0f} ; D10 ~{moy*r_d10:.0f} EUR/an")
p(f"Cour des comptes (relais FJJ) : D10 130 EUR contre 82 EUR pour D1-D3 reunis, soit {130/(82/3):.1f} fois un decile modeste moyen")
p(f"cheque energie exceptionnel 2022 : 174 EUR au premier decile, contre {82/3:.0f} EUR par decile modeste avec la baisse de TVA")

p("=== Hausse de 10 % des salaires exoneree : effet d'aubaine ===")
p("Insee 2020 (PEPA 2019) : aubaine 15 % (micro) a 40 % (macro) de l'effet sur les salaires")
