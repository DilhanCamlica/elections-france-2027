"""Règle 18 (arbitrage LR, 2026-10-28) : participation des groupes suivis aux
scrutins de `03-sources/scrutins-positions.md`.

Rédigé le 2026-10-28 par un sous-agent Opus (boucle de révision LR, contrôle
d'impact sur les verticales faites). Résultats repris dans les fiches `axes/`
des verticales concernées, avec la mention « calcul par nos soins ».
Règle : un scrutin où moins de 10 % des membres du groupe ont voté (pour +
contre + abstention), sans explication de vote au nom du groupe, est « non
exploitable » pour un objet d'écart (`02-partis/lr/revue/arbitrage.md`, règle 18).
Les non votants (présents qui ne prennent pas part au vote) ne comptent pas
parmi les votants. Le scrutin 519 (motion de censure, seuls les pour sont
décomptés) est signalé à part : la règle ne s'y applique pas.
Source des chiffres : jeu open data « Scrutins » de l'Assemblée nationale,
tel que recopié dans `03-sources/scrutins-positions.md` (sections « Détail par
scrutin », colonnes Membres, Pour, Contre, Abst.).
Exécution : python3 -I _scripts/calculs/regle18_participation.py
"""
import pathlib, re

FICHIER = pathlib.Path(__file__).resolve().parents[2] / "03-sources" / "scrutins-positions.md"
SUIVIS = ["LFI-NFP", "SOC", "EPR", "DR", "RN"]
SEUIL = 0.10

texte = FICHIER.read_text(encoding="utf-8")
detail = texte.split("## Détail par scrutin")[1].split("## Anomalies")[0]
sections = re.split(r"^### Scrutin (\d+) ", detail, flags=re.M)[1:]

lignes, sous_seuil, limites = [], [], []
for num, corps in zip(sections[::2], sections[1::2]):
    for g in SUIVIS:
        m = re.search(rf"^\| {re.escape(g)} \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|", corps, flags=re.M)
        if not m:
            continue
        membres, p, c, a, nv = map(int, m.groups())
        votants = p + c + a
        part = votants / membres
        lignes.append((num, g, votants, membres, part))
        if num == "519":
            continue
        if part < SEUIL:
            sous_seuil.append((num, g, votants, membres, part))
        elif part < 0.12:
            limites.append((num, g, votants, membres, part))

print(f"{len(sections) // 2} scrutins lus, {len(lignes)} couples scrutin x groupe.")
print("\nSous le seuil de 10 % (non exploitables pour un objet d'écart) :")
for num, g, v, m, part in sous_seuil:
    print(f"  {num:>5} {g:<8} {v:>3} votants sur {m:>3} : {part * 100:5.1f} %")
print("\nEntre 10 et 12 % (à la limite, exploitables) :")
for num, g, v, m, part in limites:
    print(f"  {num:>5} {g:<8} {v:>3} votants sur {m:>3} : {part * 100:5.1f} %")
print("\nScrutin 519 (censure, pour seuls) : règle non applicable.")
