#!/usr/bin/env python3
"""Pose la marque « base du verdict C » (socle v2.3) sur une page « parti ».

Usage :
  python3 _scripts/marque-base-c.py --page <fichier .src.html ou .html> --parti "Le RN" --base votes
  python3 _scripts/marque-base-c.py --page ... --parti "Les Républicains" --base actes --periode 2024-2025 \
      --phrase "ont gouverné de septembre 2024 à octobre 2025 (Premier ministre et ministre de l'Intérieur)"

Ce que le script fait, dans l'ordre, et exactement une fois chacun :
  1. grille : la pastille « Votent ? » de chaque ligne reçoit la classe base-votes ou base-actes et une ligne de base ;
  2. sous la grille, avant la ligne « Comment ils gouvernent », un encadré « Lire la colonne » avec un bouton « Pourquoi ? » ;
  3. chapitres : une seconde puce (« Votes seuls » / « Votes + actes <période> ») à côté de la puce de verdict C ;
  4. note de méthode : un paragraphe « La base du verdict de cohérence » avant le paragraphe « Même grille… » ;
  5. CSS : les règles de la marque, insérées après la règle .verdict-chip (page assemblée) ; sur un fichier .src.html
     qui porte le jeton {{CSS}}, le CSS n'est pas touché (il vient du gabarit, qui doit déjà porter la marque).
L'encadré final (« Ce qu'il faut retenir ») n'est pas modifié par le script : son point sur la base est écrit à la main,
parce qu'il nomme l'acte quand la règle v2.3 a joué.
Le script refuse de tourner deux fois sur la même page (marqueur base-note présent).
"""
import argparse, pathlib, re, sys

CSS = """
/* Base du verdict C (socle v2.3) */
.pill .pb{font-family:var(--mono);font-size:.56rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);line-height:1.2;margin-top:.15rem}
.pill.base-votes{border:1.5px dashed color-mix(in srgb,var(--muted) 75%,transparent)}
.pill.base-votes.c1{background:color-mix(in srgb,var(--v1s) 45%,var(--card))}
.pill.base-votes.c2{background:color-mix(in srgb,var(--v2s) 45%,var(--card))}
.pill.base-votes.c3{background:color-mix(in srgb,var(--v3s) 45%,var(--card))}
.pill.base-votes.c4{background:color-mix(in srgb,var(--v4s) 45%,var(--card))}
.pill.base-votes.c5{background:color-mix(in srgb,var(--v5s) 45%,var(--card))}
.pill.base-actes{border:1.5px solid color-mix(in srgb,var(--muted) 45%,transparent)}
.base-note{margin:.9rem 0 0;padding:.8rem .95rem;border:1.5px dashed color-mix(in srgb,var(--muted) 75%,transparent);border-radius:10px;font-size:.84rem;color:var(--ink);background:var(--card)}
.base-note p{margin:0}
.base-note details{margin-top:.45rem}
.base-note summary{cursor:pointer;list-style:none;font-family:var(--mono);font-size:.72rem;color:var(--accent);display:inline-flex;gap:.35rem;align-items:center}
.base-note summary::-webkit-details-marker{display:none}
.base-note summary .chev{transition:transform .2s ease}
.base-note details[open] summary .chev{transform:rotate(90deg)}
.base-note .body{margin-top:.5rem;color:var(--muted);font-size:.82rem}
.base-note .body p{margin:0 0 .4rem}
.base-sw{width:16px;height:10px;border-radius:3px;display:inline-block;vertical-align:-1px;margin:0 .3rem 0 .1rem;border:1.5px dashed var(--muted);background:color-mix(in srgb,var(--v3s) 45%,var(--card))}
.base-sw.actes{border-style:solid;background:var(--v3s)}
.base-chip{display:inline-block;font-family:var(--mono);font-size:.62rem;letter-spacing:.04em;padding:.2rem .5rem;border-radius:999px;border:1.5px dashed var(--muted);color:var(--muted);white-space:nowrap}
.base-chip.actes{border-style:solid}
@media (max-width:420px){.pill .pb{font-size:.5rem;letter-spacing:.03em}}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--page", required=True)
    ap.add_argument("--parti", default="", help="sujet de la phrase, par exemple « Le RN », « Les Républicains »")
    ap.add_argument("--base", choices=["votes", "actes"])
    ap.add_argument("--periode", default="", help="pour --base actes : 2024-2025, 2017-2026, 2012-2017")
    ap.add_argument("--phrase", default="", help="pour --base actes : « ont gouverné de … à … (postes) »")
    ap.add_argument("--regle", default="", help="pour --base actes : une phrase sur l'acte qui a fait jouer la règle v2.3, ou vide")
    ap.add_argument("--css-seulement", action="store_true", help="n'insère que le CSS de la marque dans une page assemblée (après assemblage depuis un gabarit qui ne l'a pas)")
    a = ap.parse_args()
    p = pathlib.Path(a.page); t = p.read_text()
    if a.css_seulement:
        if "Base du verdict C (socle v2.3)" in t:
            sys.exit("CSS déjà présent : " + a.page)
        m = re.search(r"\.verdict-chip\{[^}]*\}", t); assert m, "règle .verdict-chip absente"
        p.write_text(t[:m.end()] + CSS + t[m.end():]); print("CSS inséré : " + a.page); return
    if not (a.parti and a.base):
        sys.exit("--parti et --base sont requis hors --css-seulement")
    if "base-note" in t:
        sys.exit("déjà marquée : " + a.page)
    if a.base == "actes" and not (a.periode and a.phrase):
        sys.exit("--periode et --phrase sont requis avec --base actes")

    cls = "base-" + a.base
    court = "votes seuls" if a.base == "votes" else f"votes + actes {a.periode}"
    puce = "Votes seuls" if a.base == "votes" else f"Votes + actes {a.periode}"

    # 1. grille
    n = 0
    def rep_pill(m):
        nonlocal n; n += 1
        return f'<div class="pill {m.group(1)} {cls}"><span class="pq">Votent&nbsp;?</span>{m.group(2)}<span class="pb">{court}</span></div>'
    t = re.sub(r'<div class="pill (c[1-5])"><span class="pq">Votent&nbsp;\?</span>(<span class="pv">.*?</span>)</div>', rep_pill, t)
    assert n == 6, f"pastilles Votent trouvées : {n}"

    # 2. encadré sous la grille
    if a.base == "votes":
        detail = (f"<p>{a.parti} n'a pas gouverné au niveau national depuis 2012. Ses six verdicts de cohérence sont marqués "
                  f"<span class=\"base-sw\"></span>« votes seuls »&nbsp;: ils reposent sur les scrutins retenus, les textes et les amendements de son groupe, "
                  f"et sur rien d'autre, parce qu'il n'y a rien d'autre.</p>"
                  f"<p>Pour une force qui a gouverné, le même verdict est marqué <span class=\"base-sw actes\"></span>« votes + actes » et compte en plus ses décisions de gouvernement&nbsp;: "
                  f"une décision contraire à une promesse que le parti maintient aujourd'hui vaut à elle seule le cran « écart important ». "
                  f"Un verdict « votes seuls » ne se compare donc qu'à un autre verdict « votes seuls ».</p>")
    else:
        regle = (" " + a.regle.strip()) if a.regle.strip() else ""
        detail = (f"<p>{a.parti} {a.phrase}. Ses verdicts de cohérence sont marqués <span class=\"base-sw actes\"></span>« votes + actes {a.periode} »&nbsp;: "
                  f"ils comptent les scrutins retenus, les textes de son groupe, et ses décisions de gouvernement de cette période.</p>"
                  f"<p>Une décision de gouvernement contraire à une promesse que le parti maintient aujourd'hui vaut à elle seule le cran « écart important », "
                  f"même expliquée, même prise sous contrainte&nbsp;; la contrainte est écrite dans le chapitre, pas dans le verdict.{regle} "
                  f"Les forces qui n'ont pas gouverné portent la marque <span class=\"base-sw\"></span>« votes seuls »&nbsp;: leur verdict n'est pas plus favorable, il est moins testé, "
                  f"et ne se compare pas à celui-ci.</p>")
    note = ('\n    <div class="base-note" role="note">\n'
            '      <p><b>Lire la colonne « Votent-ils ce qu\'ils disent&nbsp;? »</b> Elle compare la parole aux votes pour les cinq forces et, pour celles qui ont gouverné depuis 2012, à leurs décisions de gouvernement. '
            'Une force qui n\'a pas gouverné n\'est pas plus cohérente&nbsp;: elle est moins testée.</p>\n'
            '      <details><summary>Pourquoi cette marque&nbsp;? <span class="chev">›</span></summary><div class="body">' + detail +
            '<p>La règle et ses quatre conditions sont dans la <a href="#note-methode">note de méthode</a>.</p></div></details>\n'
            '    </div>\n')
    k = t.count('<div class="mline">'); assert k == 1, f"mline : {k}"
    t = t.replace('<div class="mline">', note + '\n    <div class="mline">', 1)

    # 3. chapitres
    n = 0
    def rep_chip(m):
        nonlocal n; n += 1
        return m.group(0) + f'<span class="base-chip {a.base}">{puce}</span>'
    t = re.sub(r"Votent-ils ce qu'ils disent&nbsp;\?</h3><span class=\"verdict-chip c[1-5]\">[^<]*</span>", rep_chip, t)
    assert n == 6, f"puces de chapitre : {n}"

    # 4. note de méthode
    if a.base == "votes":
        meth = (f"<p><b>La base du verdict de cohérence.</b> Pour les cinq forces, la parole est confrontée aux votes du groupe sur les mêmes scrutins et à ses textes. "
                f"Pour celles qui ont gouverné depuis 2012, elle est aussi confrontée à leurs décisions de gouvernement, et une décision contraire à une promesse que le parti maintient dans la campagne actuelle vaut à elle seule le cran « écart important » (règle v2.3 du socle, 28 octobre 2026&nbsp;; quatre conditions&nbsp;: une décision et non un résultat manqué, un Premier ministre ou un ministre du parti compétent, la même promesse reprise en 2026, pas de renoncement écrit entre-temps). "
                f"{a.parti} n'a pas gouverné&nbsp;: ses verdicts portent la marque « votes seuls ». Ils ne sont pas plus favorables, ils sont moins testés, et la synthèse ne les comparera qu'à ceux des forces dans le même cas.</p>\n  ")
    else:
        meth = (f"<p><b>La base du verdict de cohérence.</b> Pour les cinq forces, la parole est confrontée aux votes du groupe sur les mêmes scrutins et à ses textes. "
                f"{a.parti} {a.phrase}&nbsp;: ses verdicts portent la marque « votes + actes {a.periode} » et comptent aussi ses décisions de gouvernement de cette période. "
                f"Une décision contraire à une promesse que le parti maintient dans la campagne actuelle vaut à elle seule le cran « écart important » (règle v2.3 du socle, 28 octobre 2026&nbsp;; quatre conditions&nbsp;: une décision et non un résultat manqué, un Premier ministre ou un ministre du parti compétent, la même promesse reprise en 2026, pas de renoncement écrit entre-temps). "
                f"Les forces qui n'ont pas gouverné portent la marque « votes seuls »&nbsp;: leurs verdicts sont moins testés, pas plus favorables, et la synthèse ne comparera les deux familles qu'entre elles.</p>\n  ")
    k = t.count("<p>Même grille, mêmes scrutins"); assert k == 1, f"paragraphe Même grille : {k}"
    t = t.replace("<p>Même grille, mêmes scrutins", meth + "<p>Même grille, mêmes scrutins", 1)

    # 5. CSS
    if "{{CSS}}" not in t and "Base du verdict C (socle v2.3)" not in t:
        m = re.search(r"\.verdict-chip\{[^}]*\}", t); assert m, "règle .verdict-chip absente"
        t = t[:m.end()] + CSS + t[m.end():]
    p.write_text(t)
    print(f"marquée : {a.page} ({court})")

if __name__ == "__main__":
    main()
