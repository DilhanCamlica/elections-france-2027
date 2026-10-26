"""Calculs par nos soins, fiche LFI axe 4 (pouvoir d'achat et fiscalite), etapes 3 a 5.
Donnees arretees au 2026-10-26. Chaque entree cite la source de la fiche (numero entre crochets)."""

def pct(a, b):
    return (a / b - 1) * 100

print("== Smic : conversion brut / net (sources 18, 32 de la fiche) ==")
smic_net, smic_brut = 1477.93, 1867.02
ratio = smic_net / smic_brut
print(f"ratio net/brut = {ratio:.4f}")
print(f"1700 net / 1477,93 = +{pct(1700, smic_net):.2f} %")
print(f"2176 brut / 1867,02 = +{pct(2176, smic_brut):.2f} %")
print(f"2176 brut en net = {2176*ratio:.2f} EUR ; 1700 net en brut = {1700/ratio:.2f} EUR")
print(f"hausse brute mensuelle = {2176-smic_brut:.2f} EUR")

print("\n== Smic et seuil de pauvrete 2024 (Insee [34]) ==")
seuil = 1337
print(f"ecart Smic net - seuil = {smic_net-seuil:.2f} EUR ; Smic/seuil = {smic_net/seuil:.3f}")
print(f"1722 net - seuil = {2176*ratio-seuil:.0f} EUR")

print("\n== Inflation cumulee 2021 a 2026 (Insee [36] [37], Eurostat [38]) ==")
ipc = [1.6, 5.2, 4.9, 2.0, 0.9]
ipch = [2.1, 5.9, 5.7, 2.3, 0.9]
def cum(l):
    x = 1.0
    for v in l:
        x *= 1 + v / 100
    return (x - 1) * 100
for h in (1.8, 2.0, 2.4):
    print(f"IPC 2021-2025 + 2026 a {h} % : {cum(ipc+[h]):.1f} %")
for h in (1.8, 2.0, 2.4):
    print(f"IPCH 2021-2025 + 2026 a {h} % : {cum(ipch+[h]):.1f} %")
print(f"IPC 2021-2025 seul : {cum(ipc):.1f} % ; IPCH 2021-2025 seul : {cum(ipch):.1f} %")
# niveau IPCH 2026 qui donnerait 20,9 %
x = 1.0
for v in ipch:
    x *= 1 + v/100
print(f"IPCH 2026 implicite pour 20,9 % cumules : {(1.209/x-1)*100:.2f} %")

print("\n== Indice de Kaitz apres la hausse (groupe d'experts [40]) ==")
kaitz = 62.5
print(f"Kaitz 2024 {kaitz} % -> {kaitz*2176/smic_brut:.1f} % si le salaire median ne bouge pas (approximation, Smic brut 2026 rapporte au median 2024)")

print("\n== Echelle mobile : plafond de deux fois le salaire median (Insee [39]) ==")
med, d9 = 2190, 4334
print(f"2 x median net EQTP 2024 = {2*med} EUR, au-dessus du 9e decile ({d9} EUR) de {2*med-d9} EUR")

print("\n== Branches sous le Smic (ministere du Travail, relais [44]) ==")
print(f"126 / 179 = {126/179*100:.1f} %")

print("\n== CAC 40 (Vernimmen, relais [45]) ==")
div, rachats = 72.8, 34.8
print(f"dividendes + rachats = {div+rachats:.1f} Md EUR ; part des dividendes = {div/(div+rachats)*100:.0f} %")

print("\n== Successions : 20 Md EUR de recettes nouvelles (C-LFI-03, p. 14) ==")
for nom, base in (("DMTG 2024 (20,8)", 20.8), ("DMTG 2025 (20,7)", 20.7), ("successions 2025 (16,2)", 16.2), ("successions 2023 (16,6)", 16.6), ("successions 2022 (15,3, axe 1)", 15.3)):
    print(f"+20 sur {nom} = +{20/base*100:.0f} %")

print("\n== Imposition minimale des patrimoines > 100 M EUR ==")
lfi = 15
for nom, v in (("Senat, IS deduit, bas", 2), ("Senat, IS deduit, haut", 3), ("Zucman, bas", 15), ("Zucman, central", 20), ("Zucman, haut", 25), ("Institut de l'Entreprise, avant comportements (axe 1)", 5.5)):
    print(f"LFI 15 / {nom} {v} = facteur {lfi/v:.2f}")

print("\n== Smic : chiffrages du cout public (niveau 4, ne decident pas) ==")
print(f"Institut Montaigne 19 (17-21) / chiffrage LFI 2025 1,6 = facteur {19/1.6:.1f} ({17/1.6:.1f} a {21/1.6:.1f})")
print(f"Institut Montaigne 19 Md EUR = {19/3138*100:.2f} % du PIB 2027 (PIB implicite 3 138 Md EUR, HCFP, axe 1)")
print(f"Allegements generaux 75 Md EUR en 2024 = {75/3138*100:.1f} % du PIB 2027 (ordre de grandeur)")

print("\n== Taux marginal IR + CSG de 90 % (plan 2022) contre taux censures en 2012 (CC 2012-662 DC) ==")
for nom, t in (("rentes 2013", 75.34), ("stock-options", 77), ("plus-values terrains", 82)):
    print(f"90 % - {nom} {t} % = +{90-t:.1f} points")

print("\n== Dares : beneficiaires de la revalorisation du 1er janvier 2026 (relais [43]) ==")
print(f"2,1 M a 11,8 % -> effectif salarie implicite {2.1/0.118:.1f} M")

print("\n== Inflation : variante sans 2021 (2022 a 2026) ==")
print(f"IPC 2022-2025 + 2026 a 1,8 % : {cum(ipc[1:]+[1.8]):.1f} % ; IPCH idem : {cum(ipch[1:]+[1.8]):.1f} %")

print("\n== ASPA portee au seuil de pauvrete (C-LFI-53 ; rapport 3350 [41]) ==")
aspa = 1043.59
print(f"1337 / 1043,59 = +{pct(1337, aspa):.1f} %")
print(f"application statique a 5,2 Md EUR de depenses ASV et ASPA 2025 : +{5.2*(1337/aspa-1):.2f} Md EUR (borne grossiere, sans nouveaux entrants ni allocataires partiels)")

print("\n== Point d'indice (repris de l'axe 1) ==")
print(f"17 contre 21,3 Md EUR : sous-estimation de {(1-17/21.3)*100:.0f} %")
