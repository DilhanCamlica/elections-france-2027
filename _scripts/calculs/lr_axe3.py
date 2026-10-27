"""Calculs par nos soins, fiche LR axe 3 (immigration, integration, droits sociaux des etrangers), etapes 3 a 5.
Donnees arretees au 2026-10-27. Chaque bloc cite la source de la fiche (numero entre crochets).
Execution : python3 -I _scripts/calculs/lr_axe3.py"""

def fmt(x):
    """Entier avec espace comme separateur de milliers."""
    return f"{x:,.0f}".replace(",", " ")

def pct(a, b):
    """Evolution de b vers a, en %."""
    return (a / b - 1) * 100

print("== Q1. Stock de titres valides : 4,5 M (fin 2025) contre 3,1 M (2017, chiffre du parti) [C-LR-12] [33] [34] ==")
fin2025 = 4.5e6                     # ministere de l'Interieur, fin 2025, champ non precise par les relais [33]
insee = {2017: 2_965_310, 2018: 3_122_834, 2021: 3_451_804}   # metropole, pays tiers hors Britanniques, documents provisoires inclus [34]
print(f"hausse selon le parti (3,1 -> 4,5) : {pct(4.5, 3.1):+.1f} %")
print(f"hausse 2017 Insee -> fin 2025 ministere : {pct(fin2025, insee[2017]):+.1f} % (champs differents)")
print(f"ecart chiffre 2017 du parti / serie Insee 2017 : {pct(3.1e6, insee[2017]):+.1f} % ; / 2018 : {pct(3.1e6, insee[2018]):+.1f} %")

print("\n== Q1. Cout net : OID 41 Md EUR contre convention OCDE -0,85 point de PIB [C-LR-12] [35] [36] ==")
deficit, deficit_pib = 152.5, 5.1          # briefing par. 3.3 (Insee) [36]
pib = deficit / deficit_pib * 100
ocde = 0.0085 * pib
print(f"PIB 2025 implicite = {pib:.0f} Md EUR ; -0,85 pt de PIB = {ocde:.1f} Md EUR")
print(f"OID 41 Md EUR / equivalent OCDE = x{41/ocde:.2f} ; OID en % du PIB = {41/pib*100:.2f} %")

print("\n== Q1. OQTF : execution et Algerie [38] [40] ==")
print("taux d'execution 9 premiers mois 2025 : 10,9 % (Senat) ; 'moins d'une sur dix' = 10,0 %")
visas_dz_2025, visas_dz_2024 = 204_250, 250_000
print(f"visas aux Algeriens 2025 / 2024 : {pct(visas_dz_2025, visas_dz_2024):+.1f} % (relais DGEF) [40]")

print("\n== Q1. Hebergement d'urgence : part des etrangers en situation irreguliere (Cour des comptes) [41] ==")
for p in (0.40, 0.60):
    print(f"{p:.0%} de 203 000 places = {p*203_000:,.0f} personnes".replace(",", " "))

print("\n== Q1. AME : beneficiaires et mineurs (PPL 238) [C-LR-45] ==")
benef, mineurs = 446_532, 98_926
print(f"part des ayants droit mineurs : {mineurs/benef*100:.1f} %")

print("\n== Q2/Q3. Fiche 9 : total et part conditionnee par la revision [C-LR-12] ==")
postes = {"prestations 5 ans": 3.6, "famille": 1.5, "etudiants": 1.5, "asile": 0.9, "AME": 0.7,
          "titres": 0.5, "hebergement": 0.5, "MNA soins contentieux": 0.8}
tot = sum(postes.values())
apres_revision = postes["prestations 5 ans"] + postes["asile"]
print(f"total = {tot:.1f} Md EUR ; apres revision (prestations + asile) = {apres_revision:.1f} Md EUR, soit {apres_revision/tot*100:.0f} %")
print(f"part de la mesure structurante (prestations 5 ans) = {postes['prestations 5 ans']/tot*100:.0f} %")

print("\n== Q3. Fiche 9 contre l'OID (fevrier 2025) [35] ==")
oid_brut, oid_surcout, oid_net = 9.8, 2.9, 6.9
print(f"OID net verifie : {oid_brut - oid_surcout:.1f} Md EUR")
print(f"LR 10,0 / OID brut 9,8 : {pct(10.0, oid_brut):+.1f} % ; LR 10,0 / OID net 6,9 : {pct(10.0, oid_net):+.1f} %")
lignes_oid = {"etudiants": (1.5, 2.25), "asile": (0.9, 0.93), "AME": (0.7, 0.66),
              "hebergement": (0.5, 0.19), "MNA soins contentieux": (0.8, 0.34 + 0.26 + 0.23)}
for k, (lr, oid) in lignes_oid.items():
    print(f"  {k} : LR {lr} contre OID {oid:.2f} -> {pct(lr, oid):+.0f} %")

print("\n== Q3. Prestations apres cinq ans : 3,6 Md EUR contre Institut Montaigne [C-LR-12] [57] [58] ==")
lr = 3.6
for nom, v in {"Montaigne 2022 (Pecresse, central)": 2.1, "Montaigne 2022 (haut)": 2.7,
               "Montaigne 2024 (RN, 5 ans ETP, central)": 2.6, "Montaigne 2024 (RN, haut)": 3.1,
               "Montaigne cite par le parti": 2.8}.items():
    print(f"  LR / {nom} {v} = x{lr/v:.2f}")

print("\n== Q3. AME reduite aux soins essentiels : 0,7 Md EUR [C-LR-12] [42] ==")
dep2024, credits2026 = 1.387, 1.2083
print(f"0,7 / depense 2024 = {0.7/dep2024*100:.1f} % ; 0,7 / credits 2026 = {0.7/credits2026*100:.1f} %")

print("\n== Q3. Regroupement familial divise par deux : 1,5 Md EUR selon le perimetre [C-LR-12] [59] [60] ==")
rf_strict, familial_2025 = 12_885, 91_100     # Ined 2023 ; DGEF 2025 (motif familial, ordre de grandeur)
for nom, flux in {"regroupement familial strict (Ined 2023)": rf_strict, "motif familial (2025)": familial_2025}.items():
    moins = flux / 2
    stock5 = moins * 5          # personnes en moins apres cinq ans de flux reduit, sans departs
    print(f"  {nom} : {fmt(moins)} titres de moins par an ; apres cinq ans {fmt(stock5)} ; 1,5 Md EUR / personne = {fmt(1.5e9/stock5)} EUR par an")

print("\n== Q3. Titres au cout complet : 0,5 Md EUR [C-LR-12] [33] ==")
premiers, renouv = 384_230, 955_000
for n, lab in ((1_000_000, "1 million (fiche 9)"), (premiers + renouv, "premiers + renouvellements 2025")):
    print(f"  {lab} : {0.5e9/n:,.0f} EUR de plus par titre".replace(",", " "))

print("\n== Q3. Effets distributifs : cas-types [C-LR-07] [61] [C-LR-09] ==")
rf = 240 * 12
print(f"Revenu familial : 240 EUR x 12 = {rf} EUR par enfant et par an ; deux enfants {2*rf} EUR, trois {3*rf} EUR")
print("allocations familiales actuelles, deux enfants : 1 827 EUR par an (bareme avril 2026, fiche RN) [61]")
print(f"APL etudiants hors UE non boursiers : 200 M EUR / 100 000 = {200e6/100_000:,.0f} EUR par etudiant et par an".replace(",", " "))

print("\n== Q3. Calendrier de l'article 89 : election -> referendum de rentree 2027 [C-LR-15] ==")
from datetime import date
print(f"second tour 2027-05-09 (hypothese) -> 2027-09-15 : {(date(2027,9,15)-date(2027,5,9)).days} jours")
print("Senat : LR 124 sieges, LR + centristes 187 sur 348 ; majorite absolue 175 [68]")

print("\n== Q4. Actes de coalition : regularisations et eloignements 2025 [39] [38] ==")
reg2025 = 28_610
print(f"regularisations 2024 implicites : {reg2025/(1-0.101):,.0f}".replace(",", " "))
print(f"eloignements forces 2025 : 15 569 (+21 %) ; 2024 implicite {15_569/1.21:,.0f}".replace(",", " "))
print(f"retours forces 2024 / 2019 (Senat) : {pct(12_856, 18_906):+.1f} %")
print(f"part du mandat de ministre LR dans 2025 : {(date(2025,10,12)-date(2025,1,1)).days/365*100:.0f} %")
