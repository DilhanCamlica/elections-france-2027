"""RN, axe 3 (immigration) : calculs par nos soins pour la fiche 02-partis/rn/axes/3-immigration.md.

Toutes les entrées sont sourcées dans la fiche (numéros de source entre crochets).
Rien n'est calculé de tête. Lancer : python3 _scripts/calculs/rn_effets_distributifs_axe3.py
"""

def pct(a, b):
    return 100 * a / b

print("== 1. AME : économie annoncée par le RN rapportée à la dépense ==")
eco_amu = 1.3            # Md€, contre-budget 2026 [C-RN-31]
ame_2024 = 1.387         # Md€, dépense réelle 2024 (Sénat, avis PLF 2026)
ame_2025p = 1.385        # Md€, prévision DSS 2025 (même source)
ame_credits_2026 = 1.2083  # Md€, crédits PLF 2026 (même source)
residuel_urgences = 0.071  # Md€, soins urgents, AME humanitaire, garde à vue
print(f"économie / dépense 2024 : {pct(eco_amu, ame_2024):.1f} %")
print(f"économie / prévision 2025 : {pct(eco_amu, ame_2025p):.1f} %")
print(f"économie / crédits 2026 : {pct(eco_amu, ame_credits_2026):.1f} %")
print(f"part de la dépense 2024 laissée par l'économie : {ame_2024 - eco_amu:.3f} Md€ "
      f"({pct(ame_2024 - eco_amu, ame_2024):.1f} %), contre {residuel_urgences} Md€ de soins urgents actuels")
amdt_repli = 0.805533333  # Md€, amendement II-CF1164 (repli RN)
print(f"amendement de repli RN : {pct(amdt_repli, ame_credits_2026):.1f} % des crédits 2026")
eco_2021_q = 4.5 / 5     # Md€/an, chiffrage 2021 sur le quinquennat [C-RN-21]
print(f"chiffrage 2021 ramené à l'année : {eco_2021_q:.2f} Md€")

print("\n== 2. Prestations : chiffrage du RN contre chiffreurs indépendants ==")
rn_solid_2031 = 12.2; rn_solid_2026 = 6.1; rn_solid_2021_an = 21.9 / 5
rn_fam_2031 = 5.9; rn_fam_2021 = 3.9
mont_solid = (0.6, 2.6, 3.1)   # Institut Montaigne 2024 : bas, médian, haut (Md€/an)
mont_fam = (2.6, 3.8, 3.9)     # Institut Montaigne 2024 : bas, médian, haut
for lab, rn in [("solidarité 2031", rn_solid_2031), ("solidarité 2026", rn_solid_2026),
                ("solidarité 2021/an", rn_solid_2021_an)]:
    print(f"{lab} : {rn:.2f} Md€ = x{rn/mont_solid[1]:.2f} la médiane Montaigne "
          f"(x{rn/mont_solid[2]:.2f} le haut de fourchette)")
for lab, rn in [("familiales 2031", rn_fam_2031), ("familiales 2021", rn_fam_2021)]:
    print(f"{lab} : {rn:.2f} Md€ = x{rn/mont_fam[1]:.2f} la médiane Montaigne "
          f"(x{rn/mont_fam[2]:.2f} le haut, x{rn/mont_fam[0]:.2f} le bas)")
ifrap_cnaf_etrangers = 5.3  # Md€, toutes prestations Cnaf versées aux étrangers UE et hors UE (iFRAP, 2023)
ifrap_fam_hors_ue = 1.6     # Md€, prestations familiales des extra-européens (iFRAP, 2023)
rn_prest = rn_solid_2031 + rn_fam_2031
print(f"prestations réservées 2031 (RN) : {rn_prest:.1f} Md€ = x{rn_prest/ifrap_cnaf_etrangers:.2f} "
      f"le total Cnaf versé à tous les étrangers selon l'iFRAP")
print(f"familiales 2031 (RN) / familiales hors UE (iFRAP) : x{rn_fam_2031/ifrap_fam_hors_ue:.2f}")

print("\n== 3. Borne haute tirée de l'Insee (revenus 2021) ==")
pauvres_immigres = 1.925e6   # personnes immigrées pauvres
taux_pauvrete_imm = 0.306
prest_moy_imm = 2410         # € par personne et par an, prestations hors pensions et chômage
prest_moy_non_imm = 1530
pop_imm = pauvres_immigres / taux_pauvrete_imm
total_prest_imm = pop_imm * prest_moy_imm / 1e9
print(f"immigrés dans le champ de l'enquête : {pop_imm/1e6:.2f} millions")
print(f"prestations (hors pensions, chômage) reçues par tous les immigrés : {total_prest_imm:.1f} Md€ (2021)")
print(f"prestations réservées RN 2031 / ce total : {pct(rn_prest, total_prest_imm):.0f} %")
print(f"écart moyen immigrés / non-immigrés : +{pct(prest_moy_imm - prest_moy_non_imm, prest_moy_non_imm):.1f} %")
print(f"part des immigrés sous D1 : 21,9 % soit x{21.9/10:.2f} leur poids attendu ; sous D2 : {21.9+17.7:.1f} %")

print("\n== 4. Total de l'axe contre l'OID (classé à droite) ==")
oid_net = 6.9
for lab, v in [("2027", 15.1), ("2031", 29.0), ("2026 (contre-budget)", 11.91), ("2021/an", 16.1)]:
    print(f"RN {lab} : {v} Md€ = x{v/oid_net:.2f} l'économie nette OID après cinq ans")
pib = 152.5 / 0.051
print(f"PIB implicite 2025 : {pib:.0f} Md€ ; 29 Md€ = {pct(29, pib):.2f} % du PIB")

print("\n== 5. Asile : chiffrage 2021 contre la mission budgétaire ==")
rn_asile_an = 30.7 / 5
mission_iai_2026 = 2.16
ada_2026 = 0.3134
print(f"asile + MNA (RN 2021) : {rn_asile_an:.2f} Md€/an = x{rn_asile_an/mission_iai_2026:.2f} "
      f"les crédits de la mission Immigration, asile, intégration 2026 ; ADA 2026 = {ada_2026} Md€")

print("\n== 6. Droit du sol, Algérie, logement, Espagne ==")
decl_ant, sans_formalite, total_acq = 32923, 1981, 98139
print(f"acquisitions liées au droit du sol 2025 : {decl_ant+sans_formalite} soit "
      f"{pct(decl_ant+sans_formalite, total_acq):.1f} % des acquisitions")
print(f"OQTF Algériens 2019-2022 exécutées : {pct(2600, 58700):.1f} %")
for part in (0.15, 0.16):
    print(f"titres valides totaux si 649 991 = {part:.0%} : {649991/part/1e6:.2f} millions")
print(f"620 000 logements sociaux / 5,3 millions de ménages du parc social : {pct(620000, 5.3e6):.1f} %")
print(f"Espagne : demandes / prévision gouvernementale : x{1174978/500000:.2f}")
print(f"scrutin 3260 : marge {185-184} voix")

print("\n== 7. Cas-types (barèmes au 1er avril 2026, par an) ==")
af2, af3 = 152.25, 347.32
rsa_seul, rsa_couple2 = 651.69, 1368.55
print(f"couple étranger, 2 enfants, aucun parent français : allocations familiales perdues {af2*12:.0f} €/an")
print(f"idem, 3 enfants : {af3*12:.0f} €/an")
print(f"adulte seul étranger, moins de cinq ans de travail à temps plein : RSA forfaitaire perdu {rsa_seul*12:.0f} €/an")
print(f"couple étranger avec 2 enfants au RSA : {rsa_couple2*12:.0f} €/an (montant forfaitaire, avant forfait logement)")
print(f"RSA seul / niveau de vie médian des immigrés (18 060 €, 2021) : {pct(rsa_seul*12, 18060):.0f} %")
