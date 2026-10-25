# Ordres de grandeur "calcul par nos soins", RN, axe 1 (finances publiques et dette).
# Etapes 3 a 5 (Q1, Q3 dont effets distributifs v2, Q4). Sources citees dans la fiche
# 02-partis/rn/axes/1-finances-publiques.md (numeros entre crochets).
# Section ajoutee par le sous-agent axe 1 ; d'autres axes peuvent ajouter leur section a la suite.

print("=== AXE 1 : Q1 verification ===")
# Insee, tableau 3.101 (base 2020), dette de Maastricht en Md EUR
apu = {2000: 880.0, 2017: 2263.3, 2023: 3103.2, 2024: 3306.1, 2025: 3460.5}
etat = {2000: 660.3, 2017: 1768.0, 2023: 2516.2, 2024: 2686.5, 2025: 2822.7}
print(f"hausse dette APU 2017-2025 : {apu[2025]-apu[2017]:.1f} Md ({(apu[2025]/apu[2017]-1)*100:.1f} %)")
d_etat = etat[2023] - etat[2017]
print(f"hausse dette Etat 2017-2023 : {d_etat:.1f} Md ; dette Etat 2000 : {etat[2000]} ; dette APU 2000 : {apu[2000]}")
print(f"  rapport hausse Etat / dette APU 2000 : {d_etat/apu[2000]:.2f} ; / dette Etat 2000 : {d_etat/etat[2000]:.2f}")
# Programme 2022 : 2 834,3 Md (T3 2021, Insee IR 328), +597 Md et +27 % sur le quinquennat
base = 2834.3 - 597
print(f"programme 2022 : base implicite {base:.1f} Md ; hausse {597/base*100:.1f} %")
# Deficits consecutifs du budget de l'Etat : dernier budget en equilibre 1974
print(f"nombre de lois de finances en deficit de 1975 a 2024 : {2024-1975+1}")
# Bardella : 15 Md = "a peine 1 % de la depense publique annuelle de l'Etat"
pde_2027, dep_apu_2025 = 511.6, 1714.2
print(f"15 Md / perimetre depenses Etat 2027 (511,6) : {15/pde_2027*100:.1f} % ; / depense APU 2025 (1714,2) : {15/dep_apu_2025*100:.2f} %")
# Contre-budget 2026 : cout de la dette 74 Md ; HCFP : 79,2 Md en 2026, soit 4,5 Md de plus que la LFI 2026
print(f"charge d'interets APU attendue en LFI 2026 : {79.2-4.5:.1f} Md")

print("=== AXE 1 : Q3 faisabilite ===")
# PIB implicite : PO 2026 = 1338,5 Md = 43,9 % ; PO 2027 = 1386,3 Md = 44,2 % (HCFP)
pib26, pib27 = 1338.5/0.439, 1386.3/0.442
print(f"PIB implicite 2026 : {pib26:.0f} Md ; 2027 : {pib27:.0f} Md")
print(f"4 % du PIB 2026 (tribune du 1er octobre) : {0.04*pib26:.0f} Md")
print(f"140 Md en points de PIB 2027 : {140/pib27*100:.1f} pts")
print(f"baisse du deficit 5,4 -> 3,7 en 2027 : 1,7 pt = {0.017*pib27:.0f} Md ; PLF 2027 : 5,4 -> 5,0 = {0.004*pib27:.0f} Md")
# Ecart du chiffrage du parti avec l'IDEP (2031)
rn31, idep31, idep_bas, idep_haut = 141.7, 7.5, -25.0, 50.0
print(f"facteur RN / IDEP central : {rn31/idep31:.1f} ; RN / IDEP haut : {rn31/idep_haut:.1f}")
rn27, idep27 = 71.6, 2.9
print(f"2027 : facteur RN / IDEP : {rn27/idep27:.1f}")
# Lignes de l'annexe 2031 se heurtant a une contrainte documentee par une source de niveau 2 ou 3
lignes = {
    "contribution UE (decision ressources propres, unanimite)": 13.1,
    "prestations de solidarite apres 5 ans de travail (CC 2024-6 RIP)": 12.2,
    "prestations familiales, un parent francais (egalite, CEDH)": 5.9,
    "BTF precomptes (interets en droits constates, SEC 2010)": 4.2,
    "ecretement TVA collectivites (transfert entre APU)": 3.4,
    "cotisation CNRACL (transfert entre APU)": 3.2,
    "economie sur le cout de la dette (double emploi avec le module d'interets)": 3.0,
    "TVA a la source : exces sur l'ecart total de TVA 2023 (18,0 - 12,1)": 18.0 - 12.1,
}
tot = sum(lignes.values())
for k, v in lignes.items():
    print(f"  {k}: {v:.1f}")
print(f"total : {tot:.1f} Md, soit {tot/rn31*100:.0f} % de l'amelioration nette affichee en 2031 ; reste {rn31-tot:.1f} Md")
print(f"TVA a la source / ecart de TVA 2023 : {18.0/12.1:.2f}")
# Contribution UE : amendement I-746 (PLF 2027) -11,1 Md sur 30,9 Md pour une contribution nette de 5 Md
psr27, amdt = 30.9055, 11.1
print(f"contribution nette implicite selon le RN en 2027 : {amdt+5:.1f} Md ; baisse en % du PSR : {amdt/psr27*100:.0f} %")
print(f"13,1 Md (2031) / solde net 2023 (Senat, 9,333) : {13.1/9.333:.2f}")
print(f"hausse PSR 2026 (28,8) -> 2027 (30,9) : {(30.9/28.8-1)*100:.1f} %")
# Taux : refinancement 4,0 % des 2028 contre TEC 10 de 4,90 % le 2 octobre 2026 ; sensibilite HCFP
print(f"ecart hypothese RN / TEC10 du 2 oct. : {(4.90-4.0)*100:.0f} pb ; sensibilite +1 pt : +3,4 Md an 1, +8,1 Md an 2 (HCFP)")
print(f"variante RN 5 % : +{135-121} Md en 2031, +{146-127} Md en 2032")
# Rachats d'actions 11,35 Md en 2027 rapportes aux rachats du CAC 40 en 2025 (34,8 Md, IDEP)
print(f"rachats d'actions : 11,35 / 34,8 = {11.35/34.8*100:.0f} %")
# Ecart interne contre-budget 2026
print(f"besoin d'emprunt 1,51 vs 1,454 : ecart {(1.51/1.454-1)*100:.1f} %")

print("=== AXE 1 : effets distributifs ===")
# TVA energie a 5,5 % : cout 12,2 Md en 2027 (RN). Hypothese de repercussion integrale.
gain_part_ttc = 1 - 1.055/1.20
print(f"baisse du prix TTC si repercussion integrale : {gain_part_ttc*100:.1f} %")
# Ratios Insee (note de conjoncture dec. 2021, structure Budget de famille 2017) : surcout d'energie
# pour une meme hausse de prix : D1 ~19 EUR, menage moyen ~30 EUR, D10 ~45 EUR par mois.
r_d1, r_d10 = 19/30, 45/30
for n in (30.0e6, 32.3e6):
    moy = 12.2e9/n
    print(f"menages {n/1e6:.1f} M : gain moyen {moy:.0f} EUR/an ; D1 ~{moy*r_d1:.0f} ; D10 ~{moy*r_d10:.0f} ; rapport D10/D1 {r_d10/r_d1:.1f}")
# Cour des comptes (relais Fondation Jean-Jaures) : baisse de TVA gaz et electricite, 130 EUR pour le
# dernier decile contre 82 EUR pour les trois premiers deciles reunis
print(f"rapport D10 / (D1+D2+D3) Cour des comptes : {130/82:.2f} ; D10 / decile moyen des trois premiers : {130/(82/3):.1f}")
# IDEP : menages -24,7 Md nets en 2027 ; grandes entreprises +13,1 ; ensemble des entreprises -12,0
print(f"conditions de prestations 2031 : {12.2+5.9:.1f} Md")
