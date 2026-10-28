"""LR, boucle v2.3 (2026-10-28) : signataires des deux amendements du groupe
DR au PLFSS 2027 versés au corpus ([C-LR-93], [C-LR-94]) et part du groupe.

Rédigé le 2026-10-28 par un sous-agent Opus (boucle v2.3). Résultats repris
dans 02-partis/lr/revue/arbitrage.md (section « Boucle v2.3 ») et dans les
fiches 2 et 4, avec la mention « calcul par nos soins ».
Règle : `01-socle/01-criteres.md` §6 (texte « du groupe » : 90 % des membres).
Effectif du groupe : 48 au 2026-10-27 (`00-perimetre.md`, source 1) ; le
maximum de la législature relevé par lr_textes_du_groupe.py est 50, testé aussi.
Exécution : python3 -I _scripts/calculs/lr_boucle_v23.py (requiert pdftotext)
"""
import pathlib, re, subprocess

CORPUS = pathlib.Path(__file__).resolve().parents[2] / "02-partis" / "lr" / "corpus"
PIECES = {"C-LR-93 (n° 7, article 35)": "C-LR-93-*.pdf",
          "C-LR-94 (n° 350, article 7)": "C-LR-94-*.pdf"}

for label, motif in PIECES.items():
    pdf = sorted(CORPUS.glob(motif))[0]
    texte = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                           capture_output=True, text=True, check=True).stdout
    bloc = texte.split("présenté par")[1].split("----------")[0]
    bloc = re.sub(r"\s+", " ", bloc).replace(" et ", ", ")
    noms = [n.strip() for n in bloc.split(",") if n.strip()]
    print(f"{label} : {len(noms)} signataires ; "
          f"{len(noms) / 48 * 100:.1f} % de 48 ; {len(noms) / 50 * 100:.1f} % de 50 ; "
          f"M. Barnier signataire : {'M. Barnier' in noms}")

# Scrutin 8976 (22 octobre 2026, amendement n° 350 et identiques) : DR 7 pour
# sur 48 (Datan), part des votants du groupe (règle 18 : seuil de 10 %)
print(f"Scrutin 8976 : {7 / 48 * 100:.1f} % des membres du groupe ont voté")
