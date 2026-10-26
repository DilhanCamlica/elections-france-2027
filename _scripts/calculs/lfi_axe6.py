"""LFI, axe 6 (institutions, démocratie et Europe) : calculs des étapes 3 à 5.

- Rédigé le : 2026-10-26
- Données arrêtées au : 2026-10-26
- Auteur : sous-agent Opus, étapes 3 à 5
- Statut : brouillon (étapes 3 à 5)
Sources des valeurs : voir la fiche 02-partis/lfi/axes/6-institutions-democratie-europe.md (numéros entre crochets).
"""
from datetime import date

def pct(a, b):
    return 100 * a / b

# 1. Article 49.3 : 23 recours sous la XVIe législature, 1 sous Barnier (déc. 2024), 4 sous Bayrou, 3 sous Lecornu [fiche Renaissance, 27 à 29]
xvie, barnier, bayrou, lecornu = 23, 1, 4, 3
print("49.3 depuis 2022 au 1er janvier 2025 :", xvie + barnier)
print("49.3 depuis 2022 au 26 octobre 2026 :", xvie + barnier + bayrou + lecornu)
print("49.3 depuis juillet 2024 :", barnier + bayrou + lecornu)

# 2. Gouvernement démissionnaire en 2024 : démission acceptée le 16 juillet, Barnier nommé le 5 septembre, gouvernement nommé le 21 septembre
d0 = date(2024, 7, 16)
print("Jours jusqu'à la nomination du Premier ministre :", (date(2024, 9, 5) - d0).days)
print("Jours jusqu'à la nomination du gouvernement :", (date(2024, 9, 21) - d0).days)

# 3. Participation aux municipales, premier tour : 2026 57,17 ; 2020 44,66 ; 2014 63,55 [banque des territoires]
print("Écart 2026 - 2014 (points) :", round(57.17 - 63.55, 2))
print("Écart 2026 - 2020 (points) :", round(57.17 - 44.66, 2))

# 4. Non-inscrits et mal-inscrits (Insee, 2022) : 2,9 M et 7,7 M
print("Non-inscrits + mal-inscrits (M) :", 2.9 + 7.7)

# 5. Sièges 2024 et seuils de l'article 68
for nfp in (182, 193):
    print(f"NFP {nfp} sièges : {pct(nfp, 577):.1f} % des 577 ; manque pour 289 : {289 - nfp}")
deux_tiers_an = -(-2 * 577 // 3)
deux_tiers_senat = -(-2 * 348 // 3)
print("Deux tiers de l'Assemblée (577) :", deux_tiers_an, "; du Sénat (348) :", deux_tiers_senat)
print("Part du groupe LFI-NFP (70 députés) dans ce seuil :", round(pct(70, deux_tiers_an), 1), "%")
print("Commission des lois, 2 octobre 2024 : 15 pour sur 69, soit", round(pct(15, 69), 1), "%")

# 6. Exploitations agricoles (France entière, recensements 2010 et 2020) : 514 964 et 416 054 ; parti : 520 000 et 416 000
print("Baisse 2010-2020 (recensement) :", round(pct(416054 - 514964, 514964), 1), "%")
print("Baisse selon le parti :", round(pct(416000 - 520000, 520000), 1), "%")
print("Écart sur le point de départ 2010 :", round(pct(520000 - 514964, 514964), 1), "%")

# 7. Dépenses de défense de la France (OTAN, part du PIB réel) : 1,82 % en 2014, 2,05 % en 2025 (estimation)
print("Hausse 2014-2025 (points de PIB) :", round(2.05 - 1.82, 2))

# 8. Contribution nette : 9 Md€ (parti) contre 9,333 Md€ (Sénat, 2023)
print("9 / 9,333 :", round(pct(9, 9.333), 1), "%")

# 9. Constituante : chiffrage de 2022 (300 M€ puis 500 M€ par an en 2023 et 2024)
print("Coût total chiffré en 2022 (M€) :", 300 + 500 * 2)
# Calendrier de 2022 transposé à 2027 : élection présidentielle (avril-mai), référendum de l'article 11 puis élection de la constituante
# dans l'année, entrée en fonction au 1er janvier de l'année suivante, deux ans de travaux (LAEC 2025)
print("Référendum sur le projet de Constitution, hypothèse : au plus tôt début", 2027 + 1 + 2)

# 10. RIP Aéroports de Paris : 1 093 030 soutiens pour 4 717 396 requis
print("RIP ADP, part du seuil :", round(pct(1093030, 4717396), 1), "%")

# 11. Participation du groupe LFI-NFP (70 députés au 26 octobre 2026 ; effectif à la date du scrutin non recalculé) aux scrutins de l'axe
for num, votants in (("7454", 62), ("4244", 68), ("8611", 57), ("5313", 17), ("3182", 66)):
    print(f"Scrutin {num} : {votants} votants LFI-NFP, {pct(votants, 70):.1f} % de 70")
