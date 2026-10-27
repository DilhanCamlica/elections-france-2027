"""Calculs par nos soins, fiche PS axe 3 (immigration, integration, droits sociaux des etrangers), etapes 3 a 5.
Donnees arretees au 2026-10-27. Chaque bloc cite la source de la fiche (numero entre crochets).
Execution : python3 _scripts/calculs/ps_axe3.py"""

def pct(a, b):
    """Evolution de b vers a, en %."""
    return (a / b - 1) * 100

print("== Q1. Asile 2024 : projet socialiste contre Ofpra [C-PS-01] [23] ==")
projet, ofpra = 130_952, 130_029
print(f"ecart projet / Ofpra = {pct(projet, ofpra):+.2f} %")
print("taux cite par le projet : 38 % ; Ofpra seul 38,9 % [23] ; global avec CNDA 50,1 % [24]")

print("\n== Q1. OQTF prononcees : 2012, 2016, 2022 [28] ==")
oqtf = {2012: 59_998, 2016: 81_656, 2017: 85_268, 2022: 134_280}
print(f"2012 -> 2016 (mandat PS) : {pct(oqtf[2016], oqtf[2012]):+.1f} %")
print(f"2016 -> 2022 : {pct(oqtf[2022], oqtf[2016]):+.1f} %")
print(f"2012 -> 2022 : x{oqtf[2022]/oqtf[2012]:.2f}")
print("taux d'execution : 22,3 % en 2012 [29] ; 10,9 % sur neuf mois 2025 [24]")
print(f"retours forces 2019 -> 2024 : {pct(12_856, 18_906):+.1f} % [24]")

print("\n== Q1. Premiers titres pour 1 000 habitants, 2025 (Eurostat via Euronews [26]) ==")
fr_titres, fr_pop = 377_462, 69.1e6   # population : convention du briefing, par. 3.3
print(f"France : {fr_titres / fr_pop * 1000:.2f} pour 1 000 ; moyenne UE : 9 [26]")

print("\n== Q1/Q3. Volumes de regularisation ==")
ppl, faure, ministere = 300_000, 400_000, 700_000
print(f"400 000 contre 300 000 : {pct(faure, ppl):+.1f} %")
print(f"PPL / estimation ministere des irreguliers : {ppl/ministere*100:.0f} % ; Faure : {faure/ministere*100:.0f} % [18]")
print(f"AES metiers en tension (chiffre de la PPL) : 1 655 / 10 000 = {1655/10000*100:.1f} % [C-PS-42]")

print("\n== Q3. Precedent espagnol 2026 : demandes contre prevision [33] [34] ==")
dem, prev = 1_174_978, 500_000
print(f"demandes / prevision = x{dem/prev:.2f} ; traitees au 2 juillet : {609_737/dem*100:.0f} %")

print("\n== Q3. Recettes d'une regularisation, transposition fragile de l'Espagne 2005 [32] [33] ==")
for n in (300_000, 400_000):
    for par_tete in (4_000, 4_400):
        print(f"{n} personnes x {par_tete} EUR = {n*par_tete/1e9:.2f} Md EUR par an")

print("\n== Q3. 30 000 places d'hebergement pour demandeurs d'asile [C-PS-01] [39] [24] ==")
places, cout_cada, parc = 30_000, 21.91, 111_855
cout = places * cout_cada * 365
print(f"cout annuel au tarif CADA 2026 = {cout/1e6:.0f} M EUR")
print(f"hausse du parc 2026 : {places/parc*100:.1f} %")
print(f"part du cout de l'asile 2025 (1,85 Md EUR [40]) : {cout/1.85e9*100:.1f} %")

print("\n== Q3. AME [41] ==")
print(f"depense 2024 1 387 M EUR ; credits 2026 1 208,3 M EUR ; ecart {pct(1208.3, 1387):+.1f} %")

print("\n== Q4. Actes 2012-2017 : anciennete au 2026-10-27 ==")
from datetime import date
ref = date(2026, 10, 27)
actes = {"suppression du droit d'entree AME (4 juillet 2012)": date(2012, 7, 4),
         "circulaire etudiants (31 mai 2012)": date(2012, 5, 31),
         "circulaire regularisation (28 novembre 2012)": date(2012, 11, 28),
         "abandon du droit de vote (janvier 2013)": date(2013, 1, 31),
         "loi asile (29 juillet 2015)": date(2015, 7, 29),
         "loi droit des etrangers (7 mars 2016)": date(2016, 3, 7),
         "evacuation de Calais (24 octobre 2016)": date(2016, 10, 24)}
for k, d in actes.items():
    print(f"{k} : {(ref - d).days / 365.25:.1f} ans")
