#!/usr/bin/env python3
"""build.py — собирает статический сайт coffeebeansstudio.eu в docs/ (GitHub Pages: main, /docs).

  python3 build.py            страницы + картинки (картинки пересобираются, только если их нет)
  python3 build.py --pages    только страницы
  python3 build.py --podlog   самопроверка стража: подложить 6 нарушений в копию docs/ и убедиться, что каждое названо своей строкой
  python3 build.py -h         справка (код 0)

Коды: 0 собрано · 1 собрано, но проверка нашла нарушение · 2 не состоялось (нет исходников, неизвестный ключ).
Проверка после сборки — ссылки целы И страж безопасности (BEZOPASNOST.md): на каждой странице CSP без unsafe-inline и
Referrer-Policy; ни одного style=/on*=/встроенного <script> (кроме ld+json); ни одного голого адреса почты; ни одного
внешнего ресурса (всё self-hosted); security.txt по RFC 9116 и не просрочен.
Все ссылки относительные — сайт работает и на truedba.github.io/coffeebeansstudio-site/, и на домене.
Исключение — 404.html: GitHub отдаёт его на любой глубине, поэтому там ссылки от корня домена.
"""
import html, json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
SRC = ROOT / "src"
DOMAIN = "https://coffeebeansstudio.eu"
SECURITY_EXPIRES = "2027-11-01T00:00:00.000Z"  # security.txt; продлевать раз в год
sys.path.insert(0, str(ROOT))
from content import L, EMAIL, DATE_ISO  # noqa: E402

ARGS = sys.argv[1:]
for a in ARGS:
    if a in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if a not in ("--pages", "--podlog"):
        print(f"неизвестный ключ: {a}\n{__doc__}"); sys.exit(2)
ONLY_PAGES = "--pages" in ARGS or "--podlog" in ARGS

# ───────────────────────────── картинки ─────────────────────────────
# имя → (исходник в src/img, ширины, формат «фото» или «альфа»)
IMAGES = {
    "hero_okno":     ("hero_okno.png",     [960, 1600, 2400, 3200], "photo"),
    "hero_okno_tel": ("hero_okno_tel.png", [480, 828, 1242],        "photo"),
    "studio_kofe":   ("studio_kofe.png",   [800, 1400, 2200],       "photo"),
    "len_lavanda":   ("len_lavanda.png",   [800, 1400, 2200],       "photo"),
    "skoro":         ("skoro.png",         [800, 1400, 2200],       "photo"),
    "svecha_dym":    ("svecha_dym.png",    [800, 1400, 2200],       "photo"),
    "koselig_okno":  ("koselig_okno.png",  [480, 768],              "photo"),
    "koselig_icon":  ("koselig_icon.png",  [160, 320],              "photo"),
    "bonsaj_cvet":   ("bonsaj_cvet.png",   [280, 560],              "alpha"),
    "bonsaj_zel":    ("bonsaj_zel.png",    [280, 560],              "alpha"),
    "logo_zerno":    ("logo_zerno.png",    [64, 128],               "alpha"),
}
for i in range(1, 7):
    IMAGES[f"shot{i}"] = (f"shot{i}.png", [300, 600, 900], "photo")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("ОШИБКА:", " ".join(map(str, cmd)), r.stderr[-400:]); sys.exit(1)


def build_images():
    out = OUT / "assets" / "img"; out.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "work"; tmp.mkdir(exist_ok=True)
    for name, (src, widths, kind) in IMAGES.items():
        s = SRC / "img" / src
        if not s.exists():
            print(f"нет исходника {s} (исходники: ~/lotok/game/assets/sait, nb, en3x — см. README)"); sys.exit(2)
        for w in widths:
            webp, avif = out / f"{name}-{w}.webp", out / f"{name}-{w}.avif"
            if webp.exists() and avif.exists():
                continue
            png = tmp / f"{name}-{w}.png"
            run(["magick", str(s), "-resize", f"{w}x", "-strip", str(png)])
            q = "82" if kind == "alpha" else "74"
            run(["cwebp", "-quiet", "-q", q, "-m", "6"] + (["-exact", "-alpha_q", "90"] if kind == "alpha" else []) + [str(png), "-o", str(webp)])
            run(["avifenc", "-q", "58" if kind == "photo" else "70", "-s", "6", str(png), str(avif)])
    # favicon и иконки
    logo = SRC / "img" / "logo_zerno.png"
    sq = tmp / "logo_sq.png"
    run(["magick", str(logo), "-resize", "880x880", "-gravity", "center", "-background", "none", "-extent", "1024x1024", str(sq)])
    run(["magick", str(sq), "-resize", "32x32", str(OUT / "favicon-32.png")])
    run(["magick", str(sq), "-define", "icon:auto-resize=16,32,48", str(OUT / "favicon.ico")])
    tile = tmp / "apple.png"
    run(["magick", "-size", "180x180", "xc:#1b2530", "(", str(sq), "-resize", "150x150", ")", "-gravity", "center", "-composite", str(OUT / "apple-touch-icon.png")])
    run(["magick", "-size", "512x512", "xc:#1b2530", "(", str(sq), "-resize", "420x420", ")", "-gravity", "center", "-composite", str(OUT / "icon-512.png")])


def dims(name, w):
    p = OUT / "assets" / "img" / f"{name}-{w}.webp"
    r = subprocess.run(["magick", "identify", "-format", "%w %h", str(p)], capture_output=True, text=True)
    a, b = r.stdout.split()
    return int(a), int(b)


def picture(R, name, alt, sizes, cls="", eager=False, mobile=None):
    """<picture> с avif/webp; mobile=(имя, медиа) — другой кадр для узкого экрана."""
    _, widths, _ = IMAGES[name]
    def srcset(n, ext):
        return ", ".join(f"{R}assets/img/{n}-{w}.{ext} {w}w" for w in IMAGES[n][1])
    parts = ["<picture>"]
    if mobile:
        mn, media = mobile
        parts.append(f'<source type="image/avif" media="{media}" srcset="{srcset(mn, "avif")}" sizes="100vw">')
        parts.append(f'<source type="image/webp" media="{media}" srcset="{srcset(mn, "webp")}" sizes="100vw">')
    parts.append(f'<source type="image/avif" srcset="{srcset(name, "avif")}" sizes="{sizes}">')
    parts.append(f'<source type="image/webp" srcset="{srcset(name, "webp")}" sizes="{sizes}">')
    w, h = dims(name, widths[-1])
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    parts.append(f'<img src="{R}assets/img/{name}-{widths[1] if len(widths) > 1 else widths[0]}.webp" alt="{html.escape(alt)}" width="{w}" height="{h}" {load}{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>')
    parts.append("</picture>")
    return "".join(parts)


# ───────────────────────────── страницы ─────────────────────────────
LANGS = ["en", "es", "de", "fr", "it", "pl", "ru"]  # порядок — как список языков игры (k_platforms)
PAGES = {  # ключ → путь без префикса языка
    "home": "", "koselig": "koselig/", "privacy": "privacy/", "kprivacy": "koselig/privacy/",
    "terms": "terms/", "support": "support/", "delete": "koselig/delete-data/",
}


def lp(lang, key):
    return ("" if lang == "en" else f"{lang}/") + PAGES[key]


def rel_root(path):
    return "../" * path.count("/")


# фигуры-«поли­мино» игры для маркеров списка: клетки (x, y) и цвет
POLY = [  # цвет — классом (CSP: style-атрибуты запрещены)
    ([(0, 0), (0, 1), (0, 2), (1, 2)], "cream"),
    ([(0, 0), (1, 0), (2, 0), (1, 1)], "sage"),
    ([(0, 0), (1, 0), (1, 1), (2, 1)], "blue"),
    ([(0, 0), (1, 0), (0, 1), (1, 1)], "cream"),
    ([(0, 0), (0, 1), (1, 1), (2, 1)], "blue"),
    ([(0, 0), (1, 0), (2, 0), (3, 0)], "sage"),
]


def poly_svg(i):
    cells, col = POLY[i % len(POLY)]
    mx = max(x for x, _ in cells) + 1; my = max(y for _, y in cells) + 1
    r = "".join(f'<rect x="{x*10+.6}" y="{y*10+.6}" width="8.8" height="8.8" rx="1.6"/>' for x, y in cells)
    return f'<svg class="poly poly-{col}" viewBox="0 0 {mx*10} {my*10}" width="{mx*10}" height="{my*10}" aria-hidden="true">{r}</svg>'


LOGO_SVG = None

# Почта без голого адреса в HTML: части в data-атрибутах, собирает site.js; без JS видна подпись «support [at] … [dot] eu»
# (читается человеком и читалкой), а ссылка ведёт на страницу поддержки. Сборщики адресов ищут «x@y.z» регуляркой — здесь его нет.
MAIL_U, MAIL_D, MAIL_T = EMAIL.split("@")[0], EMAIL.split("@")[1].rsplit(".", 1)[0], EMAIL.rsplit(".", 1)[1]
MAIL_TEXT = f"{MAIL_U} [at] {MAIL_D} [dot] {MAIL_T}"


def mail_link(R, lang, cls="", subject=""):
    s = f' data-s="{subject}"' if subject else ""
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{R}{lp(lang, "support")}" data-u="{MAIL_U}" data-d="{MAIL_D}" data-t="{MAIL_T}"{s}>{MAIL_TEXT}</a>'


CSP = ("default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; manifest-src 'self'; "
       "base-uri 'none'; form-action 'none'")  # frame-ancestors в <meta> не действует — он в заголовке Cloudflare (BEZOPASNOST.md)


def head(lang, key, title, desc, R, path, og="og-studio", extra_css=""):
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{lp(l, key)}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{lp("en", key)}">'
    canon_key = "kprivacy" if key == "privacy" else key
    canonical = f"{DOMAIN}/{lp(lang, canon_key)}"
    loc = {"en": "en_GB", "es": "es_ES", "de": "de_DE", "fr": "fr_FR", "it": "it_IT", "pl": "pl_PL", "ru": "ru_RU"}[lang]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{canonical}">
{alts}
<meta name="theme-color" content="#1b2530">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Coffee Beans Studio">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{loc}">
<meta property="og:image" content="{DOMAIN}/assets/{og}.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{R}favicon-32.png">
<link rel="apple-touch-icon" href="{R}apple-touch-icon.png">
<link rel="preload" href="{R}assets/fonts/CormorantGaramond-500-{'cyrillic' if lang == 'ru' else 'latin'}.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}assets/site.css">
{extra_css}
</head>
"""


GLOBE_SVG = ('<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2">'
             '<circle cx="8" cy="8" r="6.4"/><path d="M1.6 8h12.8M8 1.6c1.9 1.9 2.8 4 2.8 6.4S9.9 12.5 8 14.4M8 1.6C6.1 3.5 5.2 5.6 5.2 8s.9 4.5 2.8 6.4"/></svg>')


def header(lang, key, R, T, solid=False):
    # Переключатель языков — <details>: 7 языков не встают строкой в шапку телефона 390 px. Без JS раскрывается сам,
    # site.js только закрывает его по клику мимо и Esc. Ссылки — полными именами языков на них самих (как в меню игры).
    items = "".join(
        f'<li><a href="{R}{lp(l, key)}" hreflang="{l}" lang="{l}"{" aria-current=" + chr(34) + "true" + chr(34) if l == lang else ""}>{L[l]["name"]}</a></li>'
        for l in LANGS)
    langs = (f'<details class="langs" data-langs><summary aria-label="{T["lang_label"]}: {L[lang]["name"]}">{GLOBE_SVG}'
             f'<span>{T["short"]}</span></summary><ul>{items}</ul></details>')
    home = R + lp(lang, "home")
    return f"""<a class="skip" href="#main">{T['skip']}</a>
<header class="top{' solid' if solid else ''}" data-top>
  <a class="brand" href="{home}" aria-label="Coffee Beans Studio"><img src="{R}assets/img/logo_zerno-64.webp" alt="" width="22" height="28"><span>Coffee Beans Studio</span></a>
  <nav aria-label="Main">
    <a href="{R}{lp(lang, 'koselig')}"{' aria-current="page"' if key == 'koselig' else ''}>{T['nav_koselig']}</a>
    <a href="{R}{lp(lang, 'support')}"{' aria-current="page"' if key == 'support' else ''}>{T['nav_support']}</a>
    {langs}
  </nav>
</header>
"""


def footer(lang, R, T):
    return f"""<footer class="foot">
  <div class="foot-in">
    <p class="foot-brand"><img src="{R}assets/img/logo_zerno-64.webp" alt="" width="22" height="28" loading="lazy"> Coffee Beans Studio</p>
    <ul class="foot-links">
      <li><a href="{R}{lp(lang, 'kprivacy')}">{T['foot_legal']}</a></li>
      <li><a href="{R}{lp(lang, 'terms')}">{T['foot_terms']}</a></li>
      <li><a href="{R}{lp(lang, 'support')}">{T['foot_support']}</a></li>
      <li><a href="{R}{lp(lang, 'delete')}">{T['foot_delete']}</a></li>
      <li>{mail_link(R, lang)}</li>
    </ul>
    <p class="foot-note">© 2026 Coffee Beans Studio</p>
  </div>
</footer>
<script src="{R}assets/site.js" defer></script>
</body>
</html>
"""


def page_home(lang, R, T):
    k = R + lp(lang, "koselig")
    feats = "".join(f"<li>{poly_svg(i)}<span>{t}</span></li>" for i, (t, _) in enumerate(T["k_feats"][:4]))
    return f"""<body class="home">
{header(lang, 'home', R, T)}
<main id="main">
<section class="hero" data-scene="blue">
  <div class="hero-img">{picture(R, 'hero_okno', '', '100vw', eager=True, mobile=('hero_okno_tel', '(max-aspect-ratio: 4/5)'))}</div>
  <div class="letterbox" aria-hidden="true"><i></i><i></i></div>
  <div class="hero-text">
    <h1>{T['hero_h1']}</h1>
    <p class="lead">{T['hero_p']}</p>
    <a class="btn" href="{k}">{T['hero_cta']}</a>
  </div>
</section>

<section class="scene scene-left" data-scene="brown">
  <div class="scene-img">{picture(R, 'studio_kofe', '', '100vw')}</div>
  <div class="scene-text">
    <h2>{T['ch1_h']}</h2>
    <p>{T['ch1_p']}</p>
  </div>
</section>

<section class="game" data-scene="walnut" aria-labelledby="g-h">
  <div class="game-grid">
    <div class="game-copy">
      <img class="game-icon" src="{R}assets/img/koselig_icon-160.webp" srcset="{R}assets/img/koselig_icon-320.webp 2x" alt="" width="80" height="80" loading="lazy">
      <h2 id="g-h" class="game-title">{T['ch2_h']}</h2>
      <p class="game-sub">{T['ch2_sub']}</p>
      <p>{T['ch2_p']}</p>
      <ul class="polys">{feats}</ul>
      <p class="stores">{T['soon_stores']}</p>
      <a class="btn" href="{k}">{T['ch2_cta']}</a>
    </div>
    <div class="game-phones" aria-hidden="true">
      <figure class="phone p1">{picture(R, 'shot2', '', '(max-width: 700px) 46vw, 300px')}</figure>
      <figure class="phone p2">{picture(R, 'shot3', '', '(max-width: 700px) 46vw, 300px')}</figure>
    </div>
  </div>
</section>

<section class="word" data-scene="linen">
  <div class="word-img">{picture(R, 'len_lavanda', '', '100vw')}</div>
  <blockquote class="word-text"><p class="word-q" lang="no">{T['word_q']}</p><p>{T['word_def']}</p></blockquote>
</section>

<section class="scene scene-right" data-scene="night">
  <div class="scene-img">{picture(R, 'skoro', '', '100vw')}</div>
  <div class="scene-text">
    <h2>{T['soon_h']}</h2>
    <p>{T['soon_p']}</p>
  </div>
</section>

<section class="finale" data-scene="ember">
  <div class="finale-img">{picture(R, 'svecha_dym', '', '100vw')}</div>
  <div class="finale-text">
    <h2>{T['end_h']}</h2>
    <p>{T['end_p']}</p>
    {mail_link(R, lang, "mail")}
  </div>
</section>
</main>
{footer(lang, R, T)}"""


def page_koselig(lang, R, T):
    shots = "".join(
        f'<li><figure class="phone">{picture(R, f"shot{i+1}", alt, "(max-width: 700px) 62vw, 260px")}</figure></li>'
        for i, alt in enumerate(T["k_shot_alts"]))
    feats = "".join(f"<li>{poly_svg(i)}<div><h3>{t}</h3><p>{d}</p></div></li>" for i, (t, d) in enumerate(T["k_feats"]))
    about = "".join(f"<p>{p}</p>" for p in T["k_about_p"])
    links = [("kprivacy", T["foot_legal"]), ("support", T["foot_support"]), ("delete", T["foot_delete"]), ("terms", T["foot_terms"])]
    lk = "".join(f'<li><a href="{R}{lp(lang, k)}">{n}</a></li>' for k, n in links)
    ld = {
        "@context": "https://schema.org", "@type": "VideoGame", "name": "Koselig",
        "description": T["k_desc"], "gamePlatform": ["iOS", "Android"], "genre": "Puzzle",
        "inLanguage": ["en", "es", "de", "fr", "it", "pl", "ru"],
        "publisher": {"@type": "Organization", "name": "Coffee Beans Studio", "url": DOMAIN},
        "url": f"{DOMAIN}/koselig/",
    }
    return f"""<body class="koselig">
{header(lang, 'koselig', R, T)}
<main id="main">
<section class="k-hero" data-scene="blue">
  <div class="k-hero-art">{picture(R, 'koselig_okno', '', '(max-width: 800px) 100vw, 46vw', eager=True)}</div>
  <div class="k-hero-text">
    <img class="game-icon" src="{R}assets/img/koselig_icon-160.webp" srcset="{R}assets/img/koselig_icon-320.webp 2x" alt="" width="96" height="96">
    <p class="kicker">{T['k_eyebrow']}</p>
    <h1 class="game-title">{T['k_h1']}</h1>
    <p class="lead">{T['k_lead']}</p>
    <p class="stores-note">{T['soon_stores']}</p>
  </div>
</section>

<section class="k-about" data-scene="brown">
  <div class="prose wide">
    <h2>{T['k_about_h']}</h2>
    {about}
  </div>
  <div class="bonsai" aria-hidden="true">
    <img class="b-green" src="{R}assets/img/bonsaj_zel-280.webp" srcset="{R}assets/img/bonsaj_zel-560.webp 2x" alt="" width="280" height="{dims('bonsaj_zel', 280)[1]}" loading="lazy">
    <img class="b-bloom" src="{R}assets/img/bonsaj_cvet-280.webp" srcset="{R}assets/img/bonsaj_cvet-560.webp 2x" alt="" width="280" height="{dims('bonsaj_cvet', 280)[1]}" loading="lazy">
  </div>
</section>

<section class="k-shots" data-scene="walnut" aria-labelledby="s-h">
  <h2 id="s-h" class="sr">{T['k_shots_h']}</h2>
  <ul class="strip" tabindex="0" aria-label="{T['k_shots_h']}">{shots}</ul>
</section>

<section class="k-feats" data-scene="linen-dark">
  <div class="prose wide">
    <h2>{T['k_feat_h']}</h2>
    <ul class="feats">{feats}</ul>
  </div>
</section>

<section class="k-ads" data-scene="night">
  <div class="prose">
    <h2>{T['k_ads_h']}</h2>
    <p>{T['k_ads_p']}</p>
    <p class="platforms">{T['k_platforms']}</p>
    <h3>{T['k_links_h']}</h3>
    <ul class="links">{lk}</ul>
  </div>
</section>
</main>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{footer(lang, R, T)}"""


def page_legal(lang, R, T, h1, sub, body, key):
    body = (body.replace('<a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a>', mail_link(R, lang, subject="Delete%20my%20data"))
            .replace('<a href="mailto:{EMAIL}">{EMAIL}</a>', mail_link(R, lang)).replace("{R}", R))
    return f"""<body class="legal">
{header(lang, key, R, T, solid=True)}
<main id="main" class="legal-main">
  <header class="legal-head">
    <h1>{h1}</h1>
    <p class="legal-sub">{sub}</p>
    <p class="legal-date">{T['legal_updated']}: <time datetime="{DATE_ISO}">{T['date']}</time></p>
  </header>
  <article class="prose legal-body">
{body}
  <p class="legal-date end">{T['legal_updated']}: <time datetime="{DATE_ISO}">{T['date']}</time> · {mail_link(R, lang)}</p>
  </article>
</main>
{footer(lang, R, T)}"""


def page_support(lang, R, T):
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in T["faq"])
    body = f"""<section class="mailbox"><h2>{T['s_mail_h']}</h2><p>{mail_link(R, lang, "mail")}</p><p>{T['s_mail_p']}</p></section>
<h2>{T['s_faq_h']}</h2>
<div class="faq">{faq}</div>
<h2 id="delete">{T['s_del_h']}</h2>
<p>{T['s_del_p']}</p>"""
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub("<[^>]+>", "", q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
        for q, a in T["faq"]]}
    out = page_legal(lang, R, T, T["s_h1"], T["s_sub"], body, "support")
    return out.replace("</main>", f'</main>\n<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>', 1)


def page_404(R, T):
    return f"""<body class="nf">
<main id="main" class="nf-main">
  <div class="nf-img">{picture(R, 'svecha_dym', '', '100vw')}</div>
  <div class="nf-text">
    <h1>{T['nf_h1']}</h1>
    <p>{T['nf_p']}</p>
    <p><a class="btn" href="/">{T['nf_cta']}</a></p>
    <p class="nf-langs">{" ".join(f'<a href="/{l}/" hreflang="{l}" lang="{l}">{L[l]["name"]}</a>' for l in LANGS if l != "en")}</p>
  </div>
</main>
</body>
</html>
"""


def write(path, text):
    p = OUT / path / "index.html" if not path.endswith(".html") else OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    text = re.sub(r"\n\s*\n+", "\n", text)
    p.write_text(text, encoding="utf-8")


def build_pages():
    urls = []
    for lang in LANGS:
        T = L[lang]
        for key in PAGES:
            path = lp(lang, key)
            R = rel_root(path)
            if key == "home":
                h = head(lang, key, T["home_title"], T["home_desc"], R, path) + page_home(lang, R, T)
            elif key == "koselig":
                h = head(lang, key, T["k_title"], T["k_desc"], R, path, og="og-koselig") + page_koselig(lang, R, T)
            elif key in ("privacy", "kprivacy"):
                h = head(lang, key, T["p_title"], T["p_desc"], R, path, og="og-koselig") + page_legal(lang, R, T, T["p_h1"], T["p_sub"], T["privacy_html"], key)
            elif key == "terms":
                h = head(lang, key, T["t_title"], T["t_desc"], R, path) + page_legal(lang, R, T, T["t_h1"], T["t_sub"], T["terms_html"], key)
            elif key == "support":
                h = head(lang, key, T["s_title"], T["s_desc"], R, path) + page_support(lang, R, T)
            elif key == "delete":
                h = head(lang, key, T["d_title"], T["d_desc"], R, path, og="og-koselig") + page_legal(lang, R, T, T["d_h1"], T["d_sub"], T["delete_html"], key)
            # header() для правовых страниц получил ключ-заглушку: переписываем ссылки языков на верную страницу
            h = fix_lang_links(h, lang, key, R)
            write(path, h)
            if key != "privacy":
                urls.append(f"{DOMAIN}/{path}")
    # 404 — ссылки от корня
    T = L["en"]
    h = head("en", "home", T["nf_title"], T["nf_p"], "/", "") + page_404("/", T)
    h = h.replace('<link rel="canonical"', '<meta name="robots" content="noindex"><link rel="canonical"')
    write("404.html", h)
    # служебные файлы
    (OUT / "app-ads.txt").write_text("google.com, pub-8167533003532456, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    sm = "".join(f"<url><loc>{u}</loc><lastmod>{DATE_ISO}</lastmod></url>\n" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}</urlset>\n', encoding="utf-8")
    (OUT / "CNAME").write_text("coffeebeansstudio.eu\n", encoding="utf-8")
    # RFC 9116: куда писать о дыре. Срок — меньше года; просрочен → check() код 1 (обновить SECURITY_EXPIRES).
    sec = (f"Contact: mailto:{EMAIL}\nContact: {DOMAIN}/support/\nExpires: {SECURITY_EXPIRES}\n"
           f"Preferred-Languages: en, ru, pl\nCanonical: {DOMAIN}/.well-known/security.txt\n")
    (OUT / ".well-known").mkdir(exist_ok=True)
    (OUT / ".well-known" / "security.txt").write_text(sec, encoding="utf-8")
    (OUT / "security.txt").write_text(sec, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "site.webmanifest").write_text(json.dumps({"name": "Coffee Beans Studio", "short_name": "Coffee Beans", "icons": [{"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}], "theme_color": "#1b2530", "background_color": "#1b2530", "display": "browser"}), encoding="utf-8")
    # css/js/шрифты
    (OUT / "assets" / "fonts").mkdir(parents=True, exist_ok=True)
    for f in (SRC / "fonts").iterdir():
        if f.suffix == ".woff2":
            shutil.copy(f, OUT / "assets" / "fonts" / f.name)
    fonts = (SRC / "fonts" / "fonts.css").read_text().replace("/assets/fonts/", "fonts/")
    (OUT / "assets" / "site.css").write_text(fonts + "\n" + (SRC / "site.css").read_text(), encoding="utf-8")
    shutil.copy(SRC / "site.js", OUT / "assets" / "site.js")


def fix_lang_links(h, lang, key, R):
    for l in LANGS:
        h = re.sub(rf'href="[^"]*" hreflang="{l}" lang="{l}"', f'href="{R}{lp(l, key)}" hreflang="{l}" lang="{l}"', h)
    return h


def check(out=None):
    """Проверка собранного: каждая относительная ссылка и картинка ведёт на файл; страж безопасности. Нарушение → код 1 с перечнем."""
    out = out or OUT
    bad = []
    for p in out.rglob("*.html"):
        if p.name == "404.html":
            continue
        t = p.read_text(encoding="utf-8")
        for m in re.finditer(r'(?:href|src)="([^"#:]+?)"|(?:srcset)="([^"]+)"', t):
            refs = [m.group(1)] if m.group(1) else [s.strip().split(" ")[0] for s in m.group(2).split(",")]
            for ref in refs:
                if not ref or ref.startswith(("mailto", "http", "/")):
                    continue
                tgt = (p.parent / ref).resolve()
                if tgt.is_dir():
                    tgt = tgt / "index.html"
                if not tgt.exists():
                    bad.append(f"{p.relative_to(OUT)} → {ref}")
        if "{EMAIL}" in t or "{R}" in t:
            bad.append(f"{p.relative_to(out)}: неподставленный шаблон")
    if (out / "app-ads.txt").read_text() != "google.com, pub-8167533003532456, DIRECT, f08c47fec0942fa0\n":
        bad.append("app-ads.txt: строка не та")
    bad += check_security(out)
    if bad:
        print("НАРУШЕНИЯ:\n  " + "\n  ".join(sorted(set(bad))[:60])); return 1
    n = len(list(out.rglob("*.html")))
    print(f"ссылки целы, страж безопасности чист: {n} страниц")
    return 0


EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", re.I)


def check_security(out):
    """Страж безопасности собранного сайта. Каждое нарушение — строка с ИМЕНЕМ класса нарушения (по ней узнаётся подлог)."""
    bad = []
    for p in sorted(out.rglob("*.html")):
        rel, t = p.relative_to(out), p.read_text(encoding="utf-8")
        m = re.search(r'<meta http-equiv="Content-Security-Policy" content="([^"]*)"', t)
        if not m:
            bad.append(f"НЕТ CSP: {rel}")
        elif "unsafe-inline" in m.group(1) or "default-src 'none'" not in m.group(1):
            bad.append(f"СЛАБЫЙ CSP: {rel}: {m.group(1)[:60]}")
        if '<meta name="referrer"' not in t:
            bad.append(f"НЕТ REFERRER-POLICY: {rel}")
        for s in re.findall(r'\sstyle="[^"]*"', t):
            bad.append(f"ВСТРОЕННЫЙ СТИЛЬ: {rel}: {s.strip()[:50]}")
        for s in re.findall(r'\son[a-z]+="[^"]*"', t):
            bad.append(f"ОБРАБОТЧИК В АТРИБУТЕ: {rel}: {s.strip()[:50]}")
        for s in re.findall(r"<script\b[^>]*>", t):
            if "src=" not in s and 'type="application/ld+json"' not in s:
                bad.append(f"ВСТРОЕННЫЙ СКРИПТ: {rel}: {s[:50]}")
        for s in set(EMAIL_RE.findall(t)):
            bad.append(f"ГОЛЫЙ АДРЕС ПОЧТЫ: {rel}: {s}")
        # ресурсы — src= и <link href=; обычные ссылки <a href> наружу (политики Google/Apple) — не загрузка, их не трогаем
        for s in re.findall(r'\ssrc="(https?://[^"]+)"', t) + re.findall(r'<link\b[^>]*\shref="(https?://[^"]+)"', t):
            if not s.startswith(DOMAIN + "/"):
                bad.append(f"ВНЕШНИЙ РЕСУРС: {rel}: {s[:60]}")
    css = out / "assets" / "site.css"
    if css.exists():
        for s in re.findall(r"url\(\s*['\"]?(https?:|//)[^)]*\)", css.read_text(encoding="utf-8")):
            bad.append(f"ВНЕШНИЙ РЕСУРС: assets/site.css: {s}")
    for sp in (out / ".well-known" / "security.txt", out / "security.txt"):
        if not sp.exists():
            bad.append(f"НЕТ SECURITY.TXT: {sp.relative_to(out)}"); continue
        st = sp.read_text(encoding="utf-8")
        for f in ("Contact:", "Expires:", "Preferred-Languages:", "Canonical:"):
            if f not in st:
                bad.append(f"SECURITY.TXT БЕЗ ПОЛЯ {f[:-1]}: {sp.relative_to(out)}")
        m = re.search(r"Expires: (\S+)", st)
        if m and m.group(1)[:10] <= DATE_ISO:
            bad.append(f"SECURITY.TXT ПРОСРОЧЕН: {sp.relative_to(out)}: {m.group(1)}")
    return bad


def podlog():
    """Самопроверка стража: 6 подлогов в копию docs/, каждый обязан быть назван СВОЕЙ строкой. Код 0 — все пойманы, 1 — нет."""
    import tempfile
    cases = [  # (имя, правка файла → текст, ожидаемая строка причины)
        ("голый адрес",     "index.html", lambda s: s.replace("</main>", f"<p>{EMAIL}</p></main>", 1), "ГОЛЫЙ АДРЕС ПОЧТЫ: index.html: " + EMAIL),
        ("style-атрибут",   "index.html", lambda s: s.replace("<h1>", '<h1 style="color:red">', 1),       "ВСТРОЕННЫЙ СТИЛЬ: index.html: style=\"color:red\""),
        ("внешний скрипт",  "koselig/index.html", lambda s: s.replace("</body>", '<script src="https://cdn.example.com/x.js"></script></body>', 1), "ВНЕШНИЙ РЕСУРС: koselig/index.html: https://cdn.example.com/x.js"),
        ("снят CSP",        "support/index.html", lambda s: re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>', "", s), "НЕТ CSP: support/index.html"),
        ("встроенный скрипт", "ru/index.html", lambda s: s.replace("</body>", "<script>alert(1)</script></body>", 1), "ВСТРОЕННЫЙ СКРИПТ: ru/index.html: <script>"),
        ("security.txt просрочен", ".well-known/security.txt", lambda s: re.sub(r"Expires: \S+", "Expires: 2020-01-01T00:00:00.000Z", s), "SECURITY.TXT ПРОСРОЧЕН: .well-known/security.txt: 2020-01-01T00:00:00.000Z"),
    ]
    missed = 0
    for name, f, mut, want in cases:
        with tempfile.TemporaryDirectory() as d:
            cp = Path(d) / "docs"; shutil.copytree(OUT, cp)
            p = cp / f; p.write_text(mut(p.read_text(encoding="utf-8")), encoding="utf-8")
            got = check_security(cp)
            hit = any(g.startswith(want) for g in got)
            print(f"{'пойман ' if hit else 'ПРОПУЩЕН'} подлог «{name}» → {want if hit else 'ждали: ' + want + '; получили: ' + '; '.join(got[:3])}")
            missed += not hit
    clean = check_security(OUT)
    if clean:
        print("ПРОВАЛ: страж ругается на чистую сборку: " + "; ".join(clean[:3]))
    print(f"самопроверка стража: {len(cases) - missed} из {len(cases)} подлогов пойманы, чистая сборка {'чиста' if not clean else 'НЕ ЧИСТА'}")
    return 1 if (missed or clean) else 0


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    if not ONLY_PAGES:
        build_images()
    build_pages()
    if "--podlog" in ARGS:
        sys.exit(podlog())
    sys.exit(check())
