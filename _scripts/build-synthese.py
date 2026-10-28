#!/usr/bin/env python3
"""Construit 05-artifacts/synthese.html depuis 05-artifacts/sources/synthese.src.html :
{{CSS}} recopié depuis le gabarit (rn.html), {{DEMANDES}} depuis synthese_ecoute.py,
{{VEILLE}} depuis le fichier 04-synthese/travail/veille-phrase.txt s'il existe.
Usage : python3 _scripts/build-synthese.py
"""
import re, subprocess, html, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "05-artifacts/sources/synthese.src.html").read_text(encoding="utf-8")
css = re.search(r"<style>\n(.*?)</style>", (ROOT / "05-artifacts/rn.html").read_text(encoding="utf-8"), re.S).group(1)
src = src.replace("{{CSS}}\n", css)
out = subprocess.run([sys.executable, "-I", str(ROOT / "_scripts/calculs/synthese_ecoute.py")], capture_output=True, text=True).stdout
rows = [l for l in out.splitlines() if l.startswith("| ") and not l.startswith("| Axe")]
cls = {"T": "c4", "TC": "c4", "TP": "c3", "TPC": "c3", "NT": "c0", "C": "c2"}
trs = []
for l in rows:
    cells = [c.strip() for c in l.strip("|").split("|")]
    axe, dem, st = cells[0], cells[1], cells[2:]
    tds = []
    for s_ in st:
        code = s_.split(":")[0]
        if code == "P":
            tds.append(f'<td><span class="st c0" style="font-family:var(--mono);font-size:.64rem;padding:.15rem .4rem;border-radius:4px;background:var(--accent-soft)">P&nbsp;: {html.escape(s_.split(":", 1)[1])}</span></td>')
        else:
            tds.append(f'<td><span class="st {cls[code]}" style="font-family:var(--mono);font-size:.64rem;padding:.15rem .4rem;border-radius:4px">{code}</span></td>')
    trs.append(f'        <tr><td class="n">{axe}</td><td>{html.escape(dem)}</td>{"".join(tds)}</tr>')
src = src.replace("{{DEMANDES}}", "\n".join(trs))
veille_p = ROOT / "04-synthese/travail/veille-phrase.txt"
src = src.replace("{{VEILLE}}", veille_p.read_text(encoding="utf-8").strip() if veille_p.exists() else "")
assert "{{" not in src, "jeton non remplacé"
(ROOT / "05-artifacts/synthese.html").write_text(src, encoding="utf-8")
print("05-artifacts/synthese.html écrit,", len(trs), "demandes")
