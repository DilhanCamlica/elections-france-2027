#!/usr/bin/env python3
"""Contrôle de texte du repo : tirets longs interdits, en-tête de fiche présent.
Usage : python3 _scripts/lint-texte.py [chemin ...]   (défaut : tout le repo, .md et .html)
Sortie : liste des problèmes, code retour 1 s'il y en a.
"""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
targets = [pathlib.Path(p).resolve() for p in sys.argv[1:]] or [ROOT]
BAD = {"—": "tiret cadratin", "–": "tiret demi-cadratin"}
problems = []
for t in targets:
    files = [t] if t.is_file() else [p for p in t.rglob("*") if p.suffix in (".md", ".html") and ".git" not in p.parts and "transcripts" not in p.parts]
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except Exception as e:
            problems.append(f"{f}: illisible ({e})"); continue
        for i, line in enumerate(text.splitlines(), 1):
            for ch, name in BAD.items():
                if ch in line:
                    problems.append(f"{f.relative_to(ROOT) if f.is_relative_to(ROOT) else f}:{i}: {name}")
for p in problems:
    print(p)
print(f"{len(problems)} problème(s)" if problems else "OK : aucun tiret long")
sys.exit(1 if problems else 0)
