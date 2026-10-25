#!/usr/bin/env python3
"""Contrôle d'une page HTML avant publication.
Usage : python3 _scripts/verifie-page.py 05-artifacts/<slug>.html
Vérifie : balises ouvertes et fermées (hors éléments vides), ancres internes
qui pointent vers un id existant, références de sources (#sN) toutes citées
au moins une fois dans le texte, numérotation continue des sources,
absence de tirets longs. Code retour 1 s'il y a un problème.
"""
import re
import sys
import pathlib
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr", "path", "circle", "rect", "line", "polygon", "polyline", "ellipse", "use", "stop"}


class Check(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.ids = set()
        self.hrefs = []
        self.problems = []
        self.dup = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            if d["id"] in self.ids:
                self.problems.append(f"id en double : {d['id']} (ligne {self.getpos()[0]})")
            self.ids.add(d["id"])
        if tag == "a" and d.get("href", "").startswith("#"):
            self.hrefs.append((d["href"][1:], self.getpos()[0]))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.problems.append(f"fermeture sans ouverture : </{tag}> ligne {self.getpos()[0]}")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        # cherche plus haut dans la pile
        names = [t for t, _ in self.stack]
        if tag in names:
            idx = len(names) - 1 - names[::-1].index(tag)
            for t, l in self.stack[idx + 1:]:
                self.problems.append(f"balise non fermée : <{t}> ouverte ligne {l}, fermée par </{tag}> ligne {self.getpos()[0]}")
            del self.stack[idx:]
        else:
            self.problems.append(f"fermeture inattendue : </{tag}> ligne {self.getpos()[0]}")


def main(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    p = Check()
    p.feed(text)
    p.close()
    for t, l in p.stack:
        p.problems.append(f"balise jamais fermée : <{t}> ligne {l}")
    # ancres
    for h, l in p.hrefs:
        if h not in p.ids:
            p.problems.append(f"ancre sans cible : #{h} ligne {l}")
    # sources
    src_ids = sorted(int(i[1:]) for i in p.ids if re.fullmatch(r"s\d+", i))
    if src_ids:
        expected = list(range(1, max(src_ids) + 1))
        if src_ids != expected:
            missing = sorted(set(expected) - set(src_ids))
            p.problems.append(f"numérotation des sources discontinue, manquent : {missing}")
    cited = {int(h[1:]) for h, _ in p.hrefs if re.fullmatch(r"s\d+", h)}
    for n in src_ids:
        if n not in cited:
            p.problems.append(f"source jamais citée dans le texte : s{n}")
    # tirets longs
    for i, line in enumerate(text.splitlines(), 1):
        if "—" in line or "–" in line:
            p.problems.append(f"tiret long ligne {i}")
    # interdits de la plateforme
    for bad in ("<!doctype", "<html", "<head>", "<body"):
        if bad in text.lower():
            p.problems.append(f"balise de squelette interdite : {bad}")
    for pr in p.problems:
        print(pr)
    n_src = len(src_ids)
    print(f"{len(p.problems)} problème(s) ; {n_src} sources, {len(p.hrefs)} liens internes, {len(p.ids)} ids, {len(text.encode('utf-8')) // 1024} Ko")
    return 1 if p.problems else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
