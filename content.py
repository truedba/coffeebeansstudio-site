# Тексты сайта coffeebeansstudio.eu на трёх языках. Факты об игре — только из кода ~/lotok (см. README.md, раздел «Откуда факты»).
# Правило отбора: фраза проходит, если её можно проверить в коде игры или в магазине; «красивое, но непроверяемое» — нет.

DATE_ISO = "2026-11-12"
EMAIL = "support@coffeebeansstudio.eu"

L = {}

# ─────────────────────────────── ENGLISH ───────────────────────────────
L["en"] = dict(
    name="English", short="EN", date="12 November 2026",
    nav_koselig="Koselig", nav_support="Support", skip="Skip to content",
    foot_legal="Privacy", foot_terms="Terms", foot_support="Support", foot_delete="Delete data",
    foot_note="Coffee Beans Studio is the trading name of Dzmitry Kurtsikau, Poland.",
    soon_stores="Coming soon to the App Store and Google Play",
    home_title="Coffee Beans Studio — cozy, clever games",
    home_desc="Coffee Beans Studio is a small independent studio making cozy, clever games. Our first game, Koselig, is a wooden tray puzzle for iPhone and Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Quiet games<br>for warm evenings",
    hero_p="We make cozy, clever games — the kind you play slowly, with a cup of tea, by candlelight.",
    hero_cta="Meet Koselig",
    ch1_h="Brewed slowly",
    ch1_p="Coffee Beans Studio is a small independent studio. We care about calm puzzles, warm materials and honest design: things you can touch with your eyes — wood, linen, candlelight — and rules you can learn in a minute.",
    ch2_h="Koselig",
    ch2_sub="A wooden tray puzzle",
    ch2_p="Fit every piece into the wooden tray. Change the table, the tray and the pieces to suit your mood: oak or linen, walnut or brass, paint or stone. When you are stuck, a small bonsai can tell you whether the position can still be solved.",
    ch2_cta="About the game",
    word_q="koselig",
    word_def="<em>Norwegian</em> — cozy, warm, pleasantly intimate. The feeling of a candle, a blanket and good company.",
    soon_h="Almost wrapped",
    soon_p="Koselig is getting ready for the App Store and Google Play. This page will have the links on release day.",
    end_h="Say hello",
    end_p="Questions, ideas or a bug in a puzzle? We read every letter.",
    # Koselig
    k_title="Koselig — a cozy wooden tray puzzle for iPhone and Android",
    k_desc="Koselig is a calm wooden tray puzzle: fit every piece into the tray, choose your table, tray and pieces, and let a small bonsai blossom when you solve it. Coming soon to the App Store and Google Play.",
    k_eyebrow="A game by Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="A cozy wooden tray puzzle. Fit every piece into the tray — and take your time.",
    k_about_h="Puzzle, unhurried",
    k_about_p=[
        "Koselig is a digital wooden tray puzzle. Pieces lie on the table around the tray; you pick them up, turn them and fit them in until every cell is filled.",
        "The levels lead you along a map, from small trays to the full one. There is more than one way to fill a tray — and a perfect solution, where no two pieces of the same colour touch.",
        "When you are not sure a position can still work, tap <em>Stuck?</em>. The bonsai checks it for you after a short video you choose to watch — or straight away if you have bought <em>No ads</em>.",
    ],
    k_feat_h="What is inside",
    k_feats=[
        ("Three tables", "Oak, linen and walnut — each with its own quiet life: a candle, steam over tea, lavender in the breeze."),
        ("Trays and pieces", "Trays in pine, walnut, stone, steel, brass, olive and cherry. Pieces in paint, wood, stone, metal and terrazzo."),
        ("A map of levels", "Gentle first steps on smaller trays, then the full puzzle."),
        ("The bonsai", "Your helper for the <em>Stuck?</em> check — and it blossoms when you solve a level."),
        ("Saves", "Three save slots for positions you want to come back to."),
        ("Seven languages", "English, Español, Deutsch, Français, Italiano, Polski and Русский."),
    ],
    k_ads_h="Fair about ads",
    k_ads_p="No banners and no pop-ups. A short video plays only when you ask for a <em>Stuck?</em> check and choose to watch it. One optional purchase, <em>No ads</em>, lets the check work without videos.",
    k_shots_h="Screenshots",
    k_shot_alts=[
        "A small tray on the linen table with a few pieces around it",
        "The walnut table with the wooden tray and pieces above and below it",
        "The Stuck? card with a bonsai in a pot",
        "The Solved! screen with the bonsai and the level time",
        "The map of levels: a path through autumn hills to a house on a hill",
        "Settings: pieces, tray, table, saves, sound, language and No ads",
    ],
    k_platforms="iPhone and Android · English, Español, Deutsch, Français, Italiano, Polski, Русский",
    k_links_h="Good to know",
    # legal common
    legal_updated="Last updated",
    # privacy
    p_title="Privacy Policy — Koselig",
    p_desc="How the Koselig game and coffeebeansstudio.eu handle your data: no accounts, progress on your device, Google AdMob for optional rewarded videos, purchases via Apple and Google.",
    p_h1="Privacy Policy",
    p_sub="Koselig and coffeebeansstudio.eu",
    privacy_html="""
<p>This policy explains what happens to your data when you play <strong>Koselig</strong> on iPhone or Android and when you visit <strong>coffeebeansstudio.eu</strong>. We wrote it to match what the app actually does.</p>

<h2 id="who">Who we are</h2>
<p>Koselig is published by <strong>Coffee Beans Studio</strong>, the trading name of <strong>Dzmitry Kurtsikau</strong>, a private individual based in Poland (“we”, “us”). For any question about privacy, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">In short</h2>
<ul>
<li>There are <strong>no accounts</strong> and no sign-in. We never ask for your name, email or phone number.</li>
<li>Your progress and settings are <strong>stored only on your device</strong>. We do not receive them.</li>
<li>The game shows ads <strong>only when you choose</strong> to watch a short rewarded video for the <em>Stuck?</em> check. There are no banners and no interstitial ads. The ads come from <strong>Google AdMob</strong>, which processes device data and identifiers.</li>
<li>Where the law requires it (for example in the EEA, the UK and Switzerland), you are asked for <strong>consent</strong> through Google’s consent form before personalised ads are shown.</li>
<li>The optional <strong>“No ads”</strong> purchase is handled by Apple or Google. We never see your payment details.</li>
<li>Koselig contains <strong>no analytics</strong> and no crash-reporting service. We do not sell personal data.</li>
</ul>

<h2 id="device">1. Data stored on your device</h2>
<p>Koselig saves the following on your phone so you can continue where you left off:</p>
<ul>
<li>game progress: opened levels, the current position of the pieces and your three save slots;</li>
<li>settings: sound, language, the chosen table, tray and pieces;</li>
<li>whether you own the “No ads” purchase;</li>
<li>your advertising consent choice, which is stored on the device by Google’s consent SDK.</li>
</ul>
<p>This data stays on your device and is not sent to us. It is deleted when you delete the app. If you reinstall the game, the “No ads” purchase can be restored from Apple or Google (Settings → <em>Restore</em>); progress starts again.</p>

<h2 id="ads">2. Advertising: Google AdMob</h2>
<p>Koselig uses the <strong>Google Mobile Ads SDK</strong> (Google AdMob) to show rewarded videos. To have a video ready when you ask for one, the app starts the SDK at launch and loads one video in the background. This means Google may receive data from your device <strong>even if you never watch a video</strong>.</p>
<p>Data that Google may collect and process through the SDK includes:</p>
<ul>
<li>device identifiers: on Android the <strong>Advertising ID</strong>; on iPhone the identifier for vendors and other device signals;</li>
<li>your <strong>IP address</strong>, which can be used to estimate an approximate location (country or city);</li>
<li>device and app information: model, operating system and version, language, screen size, app version;</li>
<li>interactions with ads: which ads were loaded, shown, watched to the end or tapped.</li>
</ul>
<p>Google uses this data to deliver and measure ads, to prevent fraud and abuse and — <strong>only with your consent where consent is required</strong> — to personalise ads. Without consent, Google may still show non-personalised or limited ads, which still use some device data for frequency capping, measurement and fraud prevention.</p>
<p><strong>On iPhone</strong>, Koselig does not ask for permission to track you (App Tracking Transparency). Because of that, the Apple advertising identifier (IDFA) is not available to the app or to Google.</p>
<p><strong>Ad networks.</strong> We use Google AdMob only and have not enabled ad mediation with other networks. The Android version currently contains software adapters that AdMob can use for mediation with Meta Audience Network and AppLovin; they are not enabled in our AdMob account, and we plan to remove them. If we ever enable another network, we will update this policy first.</p>
<p>Learn more from Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">How Google uses information from sites or apps that use its services</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Google Privacy Policy</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Google EU User Consent Policy</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Google’s consent tools for apps (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">My Ad Center — manage ad personalisation in your Google account</a></li>
</ul>

<h2 id="consent">3. Your consent and how to change it</h2>
<p>In regions where consent is required, Koselig shows Google’s consent form (User Messaging Platform) before ads are requested. You can accept, refuse or choose purposes. You can change your choice at any time in the game: <strong>Settings → Ads &amp; data</strong> (this item appears where the consent rules apply). Deleting and reinstalling the app also resets your choice.</p>
<p>You can also limit ads on your device: on Android in <em>Settings → Google → Ads</em> (reset or delete the Advertising ID); on iPhone in <em>Settings → Privacy &amp; Security → Apple Advertising</em>.</p>

<h2 id="purchases">4. The “No ads” purchase</h2>
<p>Koselig offers one optional in-app purchase, <strong>“No ads”</strong> (product <code>koselig.no_ads</code>). It is processed entirely by the <strong>Apple App Store</strong> or <strong>Google Play</strong>. We do not receive your name, card or payment details. The app only receives confirmation from the store that the purchase is owned and stores that fact on your device. See the <a href="https://www.apple.com/legal/privacy/" rel="noopener">Apple Privacy Policy</a> and the <a href="https://policies.google.com/privacy" rel="noopener">Google Privacy Policy</a>.</p>

<h2 id="no">5. What we do not do</h2>
<ul>
<li>No accounts, no sign-in, no social features.</li>
<li>No analytics, no crash reporting, no tracking by us.</li>
<li>No access to your contacts, photos, camera, microphone or precise location.</li>
<li>We do not sell personal data and we do not use it for anything except what is described here.</li>
</ul>
<p>The app uses internet access (for ads and the purchase) and, on Android, vibration for haptic feedback.</p>

<h2 id="children">6. Children</h2>
<p>Koselig is a general-audience puzzle game. It is not directed at children under 13 and is not part of a children’s category. Ads in Koselig are not configured as child-directed. We do not knowingly collect personal information from children. If you believe a child has provided us with personal data, contact us and we will delete it.</p>

<h2 id="legal">7. Legal bases (GDPR)</h2>
<ul>
<li><strong>Consent</strong> (Art. 6(1)(a) GDPR) — personalised advertising and storing or accessing information on your device where consent is required.</li>
<li><strong>Legitimate interests</strong> (Art. 6(1)(f)) — showing non-personalised ads to fund a free game, ad measurement and fraud prevention.</li>
<li><strong>Contract</strong> (Art. 6(1)(b)) — delivering and restoring the “No ads” purchase.</li>
</ul>
<p>Google acts as an independent controller for the data it collects through its SDK. Google and Apple may process data outside the European Economic Area under their own safeguards.</p>

<h2 id="retention">8. How long data is kept</h2>
<p>Data on your device stays there until you delete the app. Data collected by Google is kept according to Google’s policies. If you write to us, we keep your email only as long as needed to answer and solve your request.</p>

<h2 id="rights">9. Your rights</h2>
<p>You have the right to access, correct and delete your personal data, to restrict or object to processing, to data portability and to withdraw consent at any time. Because we do not hold game data on our servers, most requests are answered by deleting the app; requests about advertising data can be made to Google through the links above. You can always write to us at <a href="mailto:{EMAIL}">{EMAIL}</a>. You also have the right to lodge a complaint with a supervisory authority — in Poland the <a href="https://uodo.gov.pl/" rel="noopener">President of the Personal Data Protection Office (UODO)</a> — or with the authority in your country.</p>

<h2 id="website">10. This website</h2>
<p>coffeebeansstudio.eu is a static website. It uses <strong>no cookies, no analytics and no third-party fonts or scripts</strong>. It is hosted on <strong>GitHub Pages</strong> (GitHub, Inc.), and its domain name service is provided by <strong>Cloudflare</strong>. These providers may process your IP address and technical request data in server logs for security and delivery. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a> and the <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare Privacy Policy</a>.</p>

<h2 id="changes">11. Changes</h2>
<p>If the app starts doing something new with data — for example a new ad network or analytics — we will update this page before the change reaches the app, and change the date below.</p>
""",
    # terms
    t_title="Terms of Use — Coffee Beans Studio",
    t_desc="Short and honest terms for Koselig and other games by Coffee Beans Studio.",
    t_h1="Terms of Use",
    t_sub="Koselig and other games by Coffee Beans Studio",
    terms_html="""
<p>These terms apply when you use <strong>Koselig</strong> or another game by <strong>Coffee Beans Studio</strong> (the trading name of Dzmitry Kurtsikau, Poland). By playing, you agree to them. They are short on purpose.</p>

<h2>1. Playing the game</h2>
<p>We give you a personal, non-exclusive, non-transferable right to install and play our games on devices you own or control, for your own non-commercial use. Please do not copy, resell, reverse engineer or redistribute the game or its art, except where the law allows it.</p>

<h2>2. The stores</h2>
<p>You download our games from the Apple App Store or Google Play, and their terms apply too. For apps downloaded from the App Store, Apple’s <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Standard End User License Agreement</a> applies in addition to these terms. Apple and Google are not responsible for the game or for support.</p>

<h2>3. Ads and the “No ads” purchase</h2>
<p>Koselig is free. It can show a short rewarded video when you ask for a <em>Stuck?</em> check. The ads are provided by Google AdMob; we do not control their content and are not responsible for third-party products advertised in them.</p>
<p>“No ads” is a one-time, non-consumable purchase. It lets the <em>Stuck?</em> check work without videos; the number of checks per level stays the same. The price is shown by the store before you pay. Payment, refunds and cancellations are handled by Apple or Google under their policies. The purchase is tied to your Apple ID or Google account and can be restored after reinstalling (Settings → <em>Restore</em>).</p>

<h2>4. Your progress</h2>
<p>Progress is stored only on your device. If you delete the app or lose the device, progress cannot be recovered by us.</p>

<h2>5. Changes and availability</h2>
<p>We may update the game — add, change or remove levels and features — and may stop offering it. We will try to keep it working, but we cannot promise it will always be available or free of bugs.</p>

<h2>6. Liability</h2>
<p>The game is provided “as is”. To the extent the law allows, we are not liable for indirect damages or loss of data. Nothing in these terms limits liability that cannot be limited by law, or your rights as a consumer under the laws of your country.</p>

<h2>7. Law</h2>
<p>These terms are governed by the law of Poland. If you are a consumer, you also keep the protection of the mandatory laws of the country where you live.</p>

<h2>8. Contact</h2>
<p>Questions or complaints: <a href="mailto:{EMAIL}">{EMAIL}</a>. Our privacy practices are described in the <a href="{R}privacy/">Privacy Policy</a>.</p>
""",
    # support
    s_title="Support — Coffee Beans Studio",
    s_desc="Help with Koselig: restore the No ads purchase, start a level over, change the language, ad consent and deleting your data.",
    s_h1="Support",
    s_sub="We read every letter",
    s_mail_h="Write to us",
    s_mail_p="Tell us your phone model, the game version and what happened. A screenshot helps a lot.",
    s_faq_h="Questions",
    faq=[
        ("How do I restore the “No ads” purchase?",
         "Open the menu (☰ in the top right corner) → Settings → next to <em>No ads</em> tap <em>Restore</em>. Use the same Apple ID or Google account you bought it with. The purchase is checked with the store every time the game starts, so it also comes back by itself after a reinstall once the store answers."),
        ("How do I start a level over?",
         "Open Settings and tap <em>Start over</em>, then tap again to confirm. This resets the current level. To erase everything — all progress and settings — delete the app."),
        ("How do I change the language?",
         "Settings → <em>Language</em>. Koselig speaks English, Español, Deutsch, Français, Italiano, Polski and Русский. <em>System</em> follows the language of your phone."),
        ("When does the game show ads?",
         "Only when you tap <em>Stuck?</em> and choose <em>Watch video</em>. There are no banners and no pop-up ads. With <em>No ads</em> the check works straight away."),
        ("How do I change my ad consent?",
         "Settings → <em>Ads &amp; data</em> opens Google’s consent form again. The item appears in regions where consent rules apply."),
        ("Can I keep a position and come back to it?",
         "Yes. Settings → <em>Saves</em> has three slots: <em>Save</em> stores the current position, <em>Load</em> brings it back."),
    ],
    s_del_h="Deleting your data",
    s_del_p="Koselig has no accounts and keeps your progress only on your device. Deleting the app deletes everything it stored. Ad data is handled by Google — see the <a href=\"{R}koselig/delete-data/\">data deletion page</a>.",
    # delete data
    d_title="Delete your data — Koselig",
    d_desc="How to delete data related to the Koselig game: everything is stored on your device; delete the app. Ad data is managed by Google.",
    d_h1="Delete your data",
    d_sub="Koselig by Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> has no accounts, so there is no account to delete. We do not keep your game data on any server.</p>

<h2>Data on your device</h2>
<p>Progress, saves, settings, the “No ads” purchase status and your ad consent choice are stored only on your phone. <strong>To delete all of it, delete the app</strong>:</p>
<ul>
<li><strong>iPhone:</strong> touch and hold the Koselig icon → <em>Remove App</em> → <em>Delete App</em>.</li>
<li><strong>Android:</strong> touch and hold the Koselig icon → <em>App info</em> → <em>Uninstall</em> (or <em>Storage → Clear storage</em> to keep the app but erase its data).</li>
</ul>
<p>Deleting the app does not cancel or remove the “No ads” purchase — it belongs to your Apple ID or Google account and can be restored later.</p>

<h2>Advertising data</h2>
<p>Ads in Koselig are provided by Google AdMob. Data collected by Google is controlled by Google. You can:</p>
<ul>
<li>reset or delete your Android Advertising ID: <em>Settings → Google → Ads</em>;</li>
<li>change your consent in the game: <em>Settings → Ads &amp; data</em>;</li>
<li>manage or delete data in your Google account: <a href="https://myadcenter.google.com/" rel="noopener">My Ad Center</a> and <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Google Data &amp; privacy</a>;</li>
<li>read how Google uses data from apps: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>

<h2>Emails to us</h2>
<p>If you wrote to us and want your messages deleted, send a request to <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> from the same address. We will delete them within 30 days and confirm.</p>
<p>More details: <a href="{R}koselig/privacy/">Privacy Policy</a>.</p>
""",
    nf_title="Page not found — Coffee Beans Studio",
    nf_h1="This page blew out like a candle",
    nf_p="The address may be wrong or the page has moved.",
    nf_cta="Back to the studio",
)

# ─────────────────────────────── РУССКИЙ ───────────────────────────────
L["ru"] = dict(
    name="Русский", short="RU", date="12 ноября 2026",
    nav_koselig="Koselig", nav_support="Поддержка", skip="К содержанию",
    foot_legal="Конфиденциальность", foot_terms="Условия", foot_support="Поддержка", foot_delete="Удаление данных",
    foot_note="Coffee Beans Studio — торговое название Дмитрия Курцикова (Dzmitry Kurtsikau), Польша.",
    soon_stores="Скоро в App Store и Google Play",
    home_title="Coffee Beans Studio — уютные умные игры",
    home_desc="Coffee Beans Studio — маленькая независимая студия уютных умных игр. Первая игра — Koselig, деревянный лоток-головоломка для iPhone и Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Тихие игры<br>для тёплых вечеров",
    hero_p="Мы делаем уютные умные игры — в такие играют не спеша, с чашкой чая, при свече.",
    hero_cta="Знакомьтесь: Koselig",
    ch1_h="Завариваем не спеша",
    ch1_p="Coffee Beans Studio — маленькая независимая студия. Нам важны спокойные головоломки, тёплые материалы и честный дизайн: то, что хочется потрогать глазами — дерево, лён, свет свечи, — и правила, которые понятны за минуту.",
    ch2_h="Koselig",
    ch2_sub="Деревянный лоток-головоломка",
    ch2_p="Уложите все фигуры в деревянный лоток. Стол, лоток и фигуры — под настроение: дуб или лён, орех или латунь, краска или камень. А если зашли в тупик, маленький бонсай подскажет, можно ли ещё собрать.",
    ch2_cta="Об игре",
    word_q="koselig",
    word_def="<em>норв.</em> — уютный, тёплый, душевный. Чувство свечи, пледа и хорошей компании.",
    soon_h="Почти упаковано",
    soon_p="Koselig готовится к выходу в App Store и Google Play. В день выхода здесь появятся ссылки.",
    end_h="Напишите нам",
    end_p="Вопрос, идея или ошибка в головоломке? Мы читаем каждое письмо.",
    k_title="Koselig — уютная деревянная головоломка для iPhone и Android",
    k_desc="Koselig — спокойная головоломка с деревянным лотком: уложите все фигуры, выберите стол, лоток и фигуры, и бонсай зацветёт, когда соберёте. Скоро в App Store и Google Play.",
    k_eyebrow="Игра Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Уютная деревянная головоломка. Уложите все фигуры в лоток — и не торопитесь.",
    k_about_h="Головоломка без спешки",
    k_about_p=[
        "Koselig — цифровой деревянный лоток-головоломка. Фигуры лежат на столе вокруг лотка: берёте, поворачиваете, укладываете — пока не заполнится каждая клетка.",
        "Уровни ведут по карте — от маленьких лотков к полному. Уложить можно по-разному, а есть и идеальное решение, где фигуры одного цвета не касаются друг друга.",
        "Не уверены, что позиция ещё сходится? Нажмите <em>«Тупик?»</em>. Бонсай проверит её после короткого ролика, который вы сами решите посмотреть, — или сразу, если куплено <em>«Без рекламы»</em>.",
    ],
    k_feat_h="Что внутри",
    k_feats=[
        ("Три стола", "Дуб, лён и орех — у каждого своя тихая жизнь: горит свеча, пар над чаем, лаванда на ветру."),
        ("Лотки и фигуры", "Лотки из сосны, ореха, камня, стали, латуни, оливы и вишни. Фигуры — краска, дерево, камень, металл и терраццо."),
        ("Карта уровней", "Лёгкие первые шаги на малых лотках, потом — полная головоломка."),
        ("Бонсай", "Помощник в проверке «Тупик?» — и цветёт, когда уровень собран."),
        ("Позиции", "Три ячейки, чтобы сохранить позицию и вернуться к ней."),
        ("Семь языков", "Русский, English, Español, Deutsch, Français, Italiano и Polski."),
    ],
    k_ads_h="Честно о рекламе",
    k_ads_p="Ни баннеров, ни всплывающей рекламы. Короткий ролик — только когда вы просите проверку «Тупик?» и сами соглашаетесь его посмотреть. Одна необязательная покупка, «Без рекламы», — и проверка работает без роликов.",
    k_shots_h="Кадры из игры",
    k_shot_alts=[
        "Малый лоток на льняном столе, вокруг несколько фигур",
        "Ореховый стол: деревянный лоток, фигуры над ним и под ним",
        "Карточка «Тупик?» с бонсаем в горшке",
        "Экран «Собрано!» с бонсаем и временем уровня",
        "Карта уровней: тропа через осенние холмы к дому на холме",
        "Настройки: фигуры, лоток, стол, позиции, звук, язык и «Без рекламы»",
    ],
    k_platforms="iPhone и Android · русский, English, Español, Deutsch, Français, Italiano, Polski",
    k_links_h="Полезно знать",
    legal_updated="Обновлено",
    p_title="Политика конфиденциальности — Koselig",
    p_desc="Как игра Koselig и сайт coffeebeansstudio.eu обращаются с данными: без аккаунтов, прогресс на устройстве, Google AdMob для роликов по желанию, покупки через Apple и Google.",
    p_h1="Политика конфиденциальности",
    p_sub="Koselig и coffeebeansstudio.eu",
    privacy_html="""
<p class="note">Юридически обязывающая версия — <a href="{R}koselig/privacy/">английская</a>. Это её точный перевод для удобства.</p>
<p>Здесь описано, что происходит с вашими данными, когда вы играете в <strong>Koselig</strong> на iPhone или Android и когда заходите на <strong>coffeebeansstudio.eu</strong>. Текст написан по тому, что приложение делает на самом деле.</p>

<h2 id="who">Кто мы</h2>
<p>Koselig выпускает <strong>Coffee Beans Studio</strong> — торговое название <strong>Dzmitry Kurtsikau</strong>, частного лица в Польше («мы»). По любым вопросам о данных пишите на <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">Коротко</h2>
<ul>
<li><strong>Аккаунтов нет</strong>, входа нет. Мы не спрашиваем имя, почту или телефон.</li>
<li>Прогресс и настройки <strong>хранятся только на вашем устройстве</strong>. Мы их не получаем.</li>
<li>Реклама — <strong>только по вашему выбору</strong>: короткий ролик за награду для проверки «Тупик?». Баннеров и межстраничной рекламы нет. Ролики показывает <strong>Google AdMob</strong>, он обрабатывает данные устройства и идентификаторы.</li>
<li>Где этого требует закон (например, ЕЭЗ, Великобритания, Швейцария), перед персонализированной рекламой у вас спрашивают <strong>согласие</strong> через форму Google.</li>
<li>Необязательную покупку <strong>«Без рекламы»</strong> проводят Apple или Google. Платёжных данных мы не видим.</li>
<li>В Koselig <strong>нет аналитики</strong> и нет сервиса отчётов о сбоях. Мы не продаём персональные данные.</li>
</ul>

<h2 id="device">1. Данные на вашем устройстве</h2>
<p>Чтобы вы могли продолжить с того же места, Koselig сохраняет на телефоне:</p>
<ul>
<li>прогресс: открытые уровни, текущую позицию фигур и три ячейки сохранений;</li>
<li>настройки: звук, язык, выбранные стол, лоток и фигуры;</li>
<li>куплено ли «Без рекламы»;</li>
<li>ваш выбор по согласию на рекламу — его хранит на устройстве SDK согласия Google.</li>
</ul>
<p>Эти данные остаются на устройстве и нам не отправляются. Они удаляются вместе с приложением. После переустановки покупку «Без рекламы» можно восстановить у Apple или Google (Настройки → <em>Восстановить</em>); прогресс начнётся заново.</p>

<h2 id="ads">2. Реклама: Google AdMob</h2>
<p>Для роликов за награду Koselig использует <strong>Google Mobile Ads SDK</strong> (Google AdMob). Чтобы ролик был готов, когда вы его попросите, приложение запускает SDK при старте и заранее загружает один ролик. Поэтому Google может получать данные с устройства, <strong>даже если вы ни разу не смотрели ролик</strong>.</p>
<p>Через SDK Google может собирать и обрабатывать:</p>
<ul>
<li>идентификаторы устройства: на Android — <strong>рекламный идентификатор</strong>; на iPhone — идентификатор для разработчика (IDFV) и другие сигналы устройства;</li>
<li><strong>IP-адрес</strong>, по которому можно определить приблизительное местоположение (страну или город);</li>
<li>сведения об устройстве и приложении: модель, система и её версия, язык, размер экрана, версия приложения;</li>
<li>действия с рекламой: какие ролики загружены, показаны, досмотрены или нажаты.</li>
</ul>
<p>Google использует эти данные, чтобы показывать и измерять рекламу, бороться с мошенничеством и — <strong>только с вашего согласия, где оно требуется</strong> — персонализировать рекламу. Без согласия Google может показывать неперсонализированную или ограниченную рекламу; она тоже использует часть данных устройства для ограничения частоты показов, измерений и защиты от мошенничества.</p>
<p><strong>На iPhone</strong> Koselig не запрашивает разрешение на отслеживание (App Tracking Transparency). Поэтому рекламный идентификатор Apple (IDFA) недоступен ни приложению, ни Google.</p>
<p><strong>Рекламные сети.</strong> Мы используем только Google AdMob и не включали медиацию с другими сетями. В Android-версии пока есть программные адаптеры, через которые AdMob может работать с Meta Audience Network и AppLovin; в нашем аккаунте AdMob они не включены, и мы планируем их убрать. Если когда-нибудь подключим другую сеть, сначала обновим эту политику.</p>
<p>Подробнее у Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Как Google использует данные сайтов и приложений, где работают его сервисы</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Политика конфиденциальности Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Политика Google о согласии пользователей из ЕС</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Инструменты согласия Google для приложений (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Мой рекламный центр — персонализация рекламы в аккаунте Google</a></li>
</ul>

<h2 id="consent">3. Согласие и как его изменить</h2>
<p>Там, где согласие обязательно, Koselig показывает форму согласия Google (User Messaging Platform) до запроса рекламы. Можно согласиться, отказаться или выбрать цели. Изменить выбор можно в любой момент: <strong>Настройки → Реклама и данные</strong> (пункт виден там, где действуют правила о согласии). Удаление и переустановка приложения тоже сбрасывают выбор.</p>
<p>Ограничить рекламу можно и в самом телефоне: на Android — <em>Настройки → Google → Реклама</em> (сбросить или удалить рекламный идентификатор); на iPhone — <em>Настройки → Конфиденциальность и безопасность → Реклама от Apple</em>.</p>

<h2 id="purchases">4. Покупка «Без рекламы»</h2>
<p>В Koselig одна необязательная покупка — <strong>«Без рекламы»</strong> (товар <code>koselig.no_ads</code>). Её целиком проводят <strong>Apple App Store</strong> или <strong>Google Play</strong>. Мы не получаем ни имени, ни карты, ни платёжных данных. Приложение получает от магазина только подтверждение, что покупка есть, и запоминает это на устройстве. См. <a href="https://www.apple.com/legal/privacy/" rel="noopener">политику Apple</a> и <a href="https://policies.google.com/privacy" rel="noopener">политику Google</a>.</p>

<h2 id="no">5. Чего мы не делаем</h2>
<ul>
<li>Нет аккаунтов, входа и социальных функций.</li>
<li>Нет аналитики, отчётов о сбоях и отслеживания с нашей стороны.</li>
<li>Нет доступа к контактам, фото, камере, микрофону и точному местоположению.</li>
<li>Мы не продаём персональные данные и не используем их ни для чего, кроме описанного здесь.</li>
</ul>
<p>Приложению нужен интернет (для рекламы и покупки) и, на Android, вибрация для тактильного отклика.</p>

<h2 id="children">6. Дети</h2>
<p>Koselig — головоломка для широкой аудитории. Она не предназначена для детей младше 13 лет и не входит в детские категории. Реклама в Koselig не настроена как реклама для детей. Мы сознательно не собираем персональные данные детей. Если вы считаете, что ребёнок передал нам такие данные, напишите нам — мы их удалим.</p>

<h2 id="legal">7. Правовые основания (GDPR)</h2>
<ul>
<li><strong>Согласие</strong> (ст. 6(1)(a) GDPR) — персонализированная реклама, а также хранение и чтение данных на устройстве, где требуется согласие.</li>
<li><strong>Законный интерес</strong> (ст. 6(1)(f)) — неперсонализированная реклама, на которую живёт бесплатная игра, измерение рекламы и защита от мошенничества.</li>
<li><strong>Договор</strong> (ст. 6(1)(b)) — выдача и восстановление покупки «Без рекламы».</li>
</ul>
<p>Google — самостоятельный контролёр данных, которые собирает через свой SDK. Google и Apple могут обрабатывать данные за пределами ЕЭЗ со своими гарантиями защиты.</p>

<h2 id="retention">8. Сроки хранения</h2>
<p>Данные на устройстве хранятся, пока вы не удалите приложение. Данные Google хранятся по правилам Google. Если вы нам написали, мы храним вашу почту, пока это нужно для ответа и решения вопроса.</p>

<h2 id="rights">9. Ваши права</h2>
<p>Вы вправе получить доступ к своим данным, исправить и удалить их, ограничить обработку или возразить против неё, получить данные в переносимом виде и в любой момент отозвать согласие. Игровых данных на наших серверах нет, поэтому большинство запросов решается удалением приложения; запросы о рекламных данных — к Google по ссылкам выше. Нам всегда можно написать: <a href="mailto:{EMAIL}">{EMAIL}</a>. Вы также вправе подать жалобу в надзорный орган — в Польше это <a href="https://uodo.gov.pl/" rel="noopener">Председатель Управления по защите персональных данных (UODO)</a> — или в орган своей страны.</p>

<h2 id="website">10. Этот сайт</h2>
<p>coffeebeansstudio.eu — статический сайт. На нём <strong>нет cookie, аналитики, сторонних шрифтов и скриптов</strong>. Он размещён на <strong>GitHub Pages</strong> (GitHub, Inc.), DNS домена обслуживает <strong>Cloudflare</strong>. Эти провайдеры могут обрабатывать ваш IP-адрес и технические данные запросов в журналах серверов для безопасности и доставки. См. <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">заявление GitHub о конфиденциальности</a> и <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">политику Cloudflare</a>.</p>

<h2 id="changes">11. Изменения</h2>
<p>Если приложение начнёт делать с данными что-то новое — например, появится другая рекламная сеть или аналитика, — мы обновим эту страницу до того, как изменение попадёт в приложение, и поменяем дату ниже.</p>
""",
    t_title="Условия использования — Coffee Beans Studio",
    t_desc="Короткие и честные условия для Koselig и других игр Coffee Beans Studio.",
    t_h1="Условия использования",
    t_sub="Koselig и другие игры Coffee Beans Studio",
    terms_html="""
<p class="note">Юридически обязывающая версия — <a href="{R}terms/">английская</a>. Это перевод для удобства.</p>
<p>Эти условия действуют, когда вы пользуетесь <strong>Koselig</strong> или другой игрой <strong>Coffee Beans Studio</strong> (торговое название Dzmitry Kurtsikau, Польша). Играя, вы с ними соглашаетесь. Они короткие нарочно.</p>
<h2>1. Игра</h2>
<p>Мы даём вам личное, неисключительное и непередаваемое право устанавливать наши игры на свои устройства и играть в них для некоммерческих целей. Пожалуйста, не копируйте, не перепродавайте, не декомпилируйте и не распространяйте игру и её графику, кроме случаев, разрешённых законом.</p>
<h2>2. Магазины</h2>
<p>Игры скачиваются из Apple App Store или Google Play, и их условия тоже действуют. Для приложений из App Store дополнительно действует <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">стандартное лицензионное соглашение Apple</a>. Apple и Google не отвечают за игру и её поддержку.</p>
<h2>3. Реклама и покупка «Без рекламы»</h2>
<p>Koselig бесплатна. Она может показать короткий ролик за награду, когда вы просите проверку «Тупик?». Рекламу показывает Google AdMob; мы не управляем её содержанием и не отвечаем за рекламируемые товары третьих лиц.</p>
<p>«Без рекламы» — разовая постоянная покупка. С ней проверка «Тупик?» работает без роликов; число проверок на уровне не меняется. Цену показывает магазин до оплаты. Оплату, возвраты и отмены проводят Apple или Google по своим правилам. Покупка привязана к вашему Apple ID или аккаунту Google и восстанавливается после переустановки (Настройки → <em>Восстановить</em>).</p>
<h2>4. Прогресс</h2>
<p>Прогресс хранится только на вашем устройстве. Если удалить приложение или потерять устройство, восстановить прогресс мы не сможем.</p>
<h2>5. Изменения и доступность</h2>
<p>Мы можем обновлять игру — добавлять, менять и убирать уровни и функции — и можем прекратить её распространение. Мы стараемся, чтобы всё работало, но не обещаем, что игра всегда будет доступна и без ошибок.</p>
<h2>6. Ответственность</h2>
<p>Игра предоставляется «как есть». В пределах, разрешённых законом, мы не отвечаем за косвенный ущерб и потерю данных. Ничто здесь не ограничивает ответственность, которую нельзя ограничить по закону, и ваши права потребителя по законам вашей страны.</p>
<h2>7. Право</h2>
<p>Условия регулируются правом Польши. Если вы потребитель, за вами сохраняется защита обязательных норм страны, где вы живёте.</p>
<h2>8. Связь</h2>
<p>Вопросы и жалобы: <a href="mailto:{EMAIL}">{EMAIL}</a>. Как мы обращаемся с данными — в <a href="{R}ru/privacy/">политике конфиденциальности</a>.</p>
""",
    s_title="Поддержка — Coffee Beans Studio",
    s_desc="Помощь по Koselig: восстановить покупку «Без рекламы», начать уровень сначала, сменить язык, согласие на рекламу и удаление данных.",
    s_h1="Поддержка",
    s_sub="Мы читаем каждое письмо",
    s_mail_h="Напишите нам",
    s_mail_p="Укажите модель телефона, версию игры и что случилось. Скриншот очень помогает.",
    s_faq_h="Вопросы",
    faq=[
        ("Как восстановить покупку «Без рекламы»?",
         "Откройте меню (☰ в правом верхнем углу) → Настройки → рядом с <em>«Без рекламы»</em> нажмите <em>«Восстановить»</em>. Нужен тот же Apple ID или аккаунт Google, с которого была покупка. Игра сверяется с магазином при каждом запуске, так что после переустановки покупка вернётся и сама, как только магазин ответит."),
        ("Как начать уровень сначала?",
         "В настройках нажмите <em>«Начать сначала»</em> и ещё раз для подтверждения. Сбросится текущий уровень. Чтобы стереть всё — прогресс и настройки — удалите приложение."),
        ("Как сменить язык?",
         "Настройки → <em>«Язык»</em>. Koselig говорит по-русски, по-английски, по-испански, по-немецки, по-французски, по-итальянски и по-польски. <em>«Как в системе»</em> — язык телефона."),
        ("Когда игра показывает рекламу?",
         "Только когда вы нажимаете <em>«Тупик?»</em> и выбираете <em>«Смотреть ролик»</em>. Баннеров и всплывающей рекламы нет. С покупкой «Без рекламы» проверка срабатывает сразу."),
        ("Как изменить согласие на рекламу?",
         "Настройки → <em>«Реклама и данные»</em> снова открывает форму согласия Google. Пункт виден там, где действуют правила о согласии."),
        ("Можно сохранить позицию и вернуться к ней?",
         "Да. В настройках, в разделе <em>«Позиции»</em>, три ячейки: <em>«Записать»</em> сохраняет текущую позицию, <em>«Открыть»</em> возвращает её."),
    ],
    s_del_h="Удаление данных",
    s_del_p="В Koselig нет аккаунтов, прогресс хранится только на устройстве. Удалите приложение — удалится всё, что оно хранило. Рекламными данными распоряжается Google — см. <a href=\"{R}ru/koselig/delete-data/\">страницу об удалении данных</a>.",
    d_title="Удаление данных — Koselig",
    d_desc="Как удалить данные игры Koselig: всё хранится на устройстве — удалите приложение. Рекламными данными распоряжается Google.",
    d_h1="Удаление данных",
    d_sub="Koselig, Coffee Beans Studio",
    delete_html="""
<p>В <strong>Koselig</strong> нет аккаунтов, поэтому удалять аккаунт не нужно. Игровых данных на серверах мы не храним.</p>
<h2>Данные на устройстве</h2>
<p>Прогресс, сохранения, настройки, статус покупки «Без рекламы» и выбор по согласию на рекламу хранятся только на телефоне. <strong>Чтобы удалить всё, удалите приложение</strong>:</p>
<ul>
<li><strong>iPhone:</strong> нажмите и удерживайте значок Koselig → <em>Удалить приложение</em> → <em>Удалить приложение</em>.</li>
<li><strong>Android:</strong> нажмите и удерживайте значок Koselig → <em>О приложении</em> → <em>Удалить</em> (или <em>Хранилище → Очистить хранилище</em>, чтобы оставить приложение, но стереть его данные).</li>
</ul>
<p>Удаление приложения не отменяет покупку «Без рекламы» — она принадлежит вашему Apple ID или аккаунту Google и восстанавливается позже.</p>
<h2>Рекламные данные</h2>
<p>Рекламу в Koselig показывает Google AdMob, собранными данными распоряжается Google. Вы можете:</p>
<ul>
<li>сбросить или удалить рекламный идентификатор Android: <em>Настройки → Google → Реклама</em>;</li>
<li>изменить согласие в игре: <em>Настройки → Реклама и данные</em>;</li>
<li>управлять данными в аккаунте Google: <a href="https://myadcenter.google.com/" rel="noopener">Мой рекламный центр</a> и <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Данные и конфиденциальность</a>;</li>
<li>прочитать, как Google использует данные приложений: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>
<h2>Письма нам</h2>
<p>Если вы нам писали и хотите, чтобы переписку удалили, отправьте запрос на <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> с того же адреса. Удалим в течение 30 дней и подтвердим.</p>
<p>Подробнее — в <a href="{R}ru/koselig/privacy/">политике конфиденциальности</a>.</p>
""",
    nf_title="Страница не найдена — Coffee Beans Studio",
    nf_h1="Эта страница погасла, как свеча",
    nf_p="Возможно, адрес набран с ошибкой или страница переехала.",
    nf_cta="Вернуться в студию",
)

# ─────────────────────────────── POLSKI ───────────────────────────────
L["pl"] = dict(
    name="Polski", short="PL", date="12 listopada 2026",
    nav_koselig="Koselig", nav_support="Pomoc", skip="Przejdź do treści",
    foot_legal="Prywatność", foot_terms="Warunki", foot_support="Pomoc", foot_delete="Usuwanie danych",
    foot_note="Coffee Beans Studio to nazwa handlowa Dzmitry Kurtsikau, Polska.",
    soon_stores="Wkrótce w App Store i Google Play",
    home_title="Coffee Beans Studio — przytulne, mądre gry",
    home_desc="Coffee Beans Studio to małe niezależne studio, które tworzy przytulne, mądre gry. Nasza pierwsza gra, Koselig, to drewniana łamigłówka z tacką na iPhone’a i Androida.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Ciche gry<br>na ciepłe wieczory",
    hero_p="Tworzymy przytulne, mądre gry — takie, w które gra się powoli, z kubkiem herbaty, przy świecy.",
    hero_cta="Poznaj Koselig",
    ch1_h="Parzone powoli",
    ch1_p="Coffee Beans Studio to małe niezależne studio. Zależy nam na spokojnych łamigłówkach, ciepłych materiałach i uczciwym projektowaniu: na tym, czego chce się dotknąć wzrokiem — drewno, len, światło świecy — i na zasadach, które da się zrozumieć w minutę.",
    ch2_h="Koselig",
    ch2_sub="Drewniana łamigłówka z tacką",
    ch2_p="Ułóż wszystkie klocki w drewnianej tacce. Stół, tackę i klocki dobierz do nastroju: dąb albo len, orzech albo mosiądz, farba albo kamień. A gdy utkniesz, małe bonsai podpowie, czy da się to jeszcze ułożyć.",
    ch2_cta="O grze",
    word_q="koselig",
    word_def="<em>norw.</em> — przytulny, ciepły, swojski. Uczucie świecy, koca i dobrego towarzystwa.",
    soon_h="Prawie zapakowane",
    soon_p="Koselig szykuje się do premiery w App Store i Google Play. W dniu premiery pojawią się tu linki.",
    end_h="Napisz do nas",
    end_p="Pytanie, pomysł albo błąd w łamigłówce? Czytamy każdą wiadomość.",
    k_title="Koselig — przytulna drewniana łamigłówka na iPhone’a i Androida",
    k_desc="Koselig to spokojna łamigłówka z drewnianą tacką: ułóż wszystkie klocki, wybierz stół, tackę i klocki, a bonsai zakwitnie, gdy ułożysz poziom. Wkrótce w App Store i Google Play.",
    k_eyebrow="Gra Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Przytulna drewniana łamigłówka. Ułóż wszystkie klocki w tacce — i nie spiesz się.",
    k_about_h="Łamigłówka bez pośpiechu",
    k_about_p=[
        "Koselig to cyfrowa drewniana łamigłówka z tacką. Klocki leżą na stole wokół tacki: bierzesz je, obracasz i układasz, aż zapełnisz każde pole.",
        "Poziomy prowadzą przez mapę — od małych tacek do pełnej. Tackę można ułożyć na różne sposoby, a jest też rozwiązanie idealne, w którym klocki tego samego koloru się nie stykają.",
        "Nie masz pewności, czy układ jeszcze się zepnie? Stuknij <em>„Impas?”</em>. Bonsai sprawdzi go po krótkim filmie, który sam zdecydujesz się obejrzeć — albo od razu, jeśli kupisz <em>„Bez reklam”</em>.",
    ],
    k_feat_h="Co w środku",
    k_feats=[
        ("Trzy stoły", "Dąb, len i orzech — każdy z własnym cichym życiem: płonie świeca, nad herbatą unosi się para, lawenda kołysze się na wietrze."),
        ("Tacki i klocki", "Tacki z sosny, orzecha, kamienia, stali, mosiądzu, oliwki i wiśni. Klocki: farba, drewno, kamień, metal i lastryko."),
        ("Mapa poziomów", "Łagodne pierwsze kroki na mniejszych tackach, potem pełna łamigłówka."),
        ("Bonsai", "Pomocnik przy sprawdzaniu „Impas?” — i zakwita, gdy ułożysz poziom."),
        ("Zapisy", "Trzy miejsca na układy, do których chcesz wrócić."),
        ("Siedem języków", "Polski, English, Español, Deutsch, Français, Italiano i Русский."),
    ],
    k_ads_h="Uczciwie o reklamach",
    k_ads_p="Bez banerów i wyskakujących reklam. Krótki film pojawia się tylko wtedy, gdy prosisz o sprawdzenie „Impas?” i zgadzasz się go obejrzeć. Jeden opcjonalny zakup, „Bez reklam”, sprawia, że sprawdzanie działa bez filmów.",
    k_shots_h="Zrzuty ekranu",
    k_shot_alts=[
        "Mała tacka na lnianym stole, wokół kilka klocków",
        "Stół z orzecha: drewniana tacka i klocki nad nią i pod nią",
        "Karta „Impas?” z bonsai w doniczce",
        "Ekran „Ułożone!” z bonsai i czasem poziomu",
        "Mapa poziomów: ścieżka przez jesienne wzgórza do domu na wzgórzu",
        "Ustawienia: klocki, tacka, stół, zapisy, dźwięk, język i „Bez reklam”",
    ],
    k_platforms="iPhone i Android · polski, English, Español, Deutsch, Français, Italiano, Русский",
    k_links_h="Warto wiedzieć",
    legal_updated="Ostatnia aktualizacja",
    p_title="Polityka prywatności — Koselig",
    p_desc="Jak gra Koselig i strona coffeebeansstudio.eu traktują Twoje dane: bez kont, postęp na urządzeniu, Google AdMob dla filmów na życzenie, zakupy przez Apple i Google.",
    p_h1="Polityka prywatności",
    p_sub="Koselig i coffeebeansstudio.eu",
    privacy_html="""
<p class="note">Wiążąca jest wersja <a href="{R}koselig/privacy/">angielska</a>. To jej tłumaczenie dla wygody.</p>
<p>Ta polityka wyjaśnia, co dzieje się z Twoimi danymi, gdy grasz w <strong>Koselig</strong> na iPhonie lub Androidzie i gdy odwiedzasz <strong>coffeebeansstudio.eu</strong>. Opisuje to, co aplikacja faktycznie robi.</p>

<h2 id="who">Kim jesteśmy</h2>
<p>Koselig wydaje <strong>Coffee Beans Studio</strong> — nazwa handlowa <strong>Dzmitry Kurtsikau</strong>, osoby prywatnej z Polski („my”). W sprawach prywatności pisz na <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">W skrócie</h2>
<ul>
<li><strong>Nie ma kont</strong> ani logowania. Nie pytamy o imię, e-mail ani numer telefonu.</li>
<li>Postęp i ustawienia <strong>są zapisywane tylko na Twoim urządzeniu</strong>. Nie otrzymujemy ich.</li>
<li>Reklamy pojawiają się <strong>tylko wtedy, gdy sam wybierzesz</strong> krótki film z nagrodą przy sprawdzaniu „Impas?”. Nie ma banerów ani reklam pełnoekranowych. Reklamy dostarcza <strong>Google AdMob</strong>, który przetwarza dane urządzenia i identyfikatory.</li>
<li>Tam, gdzie wymaga tego prawo (np. w EOG, Wielkiej Brytanii i Szwajcarii), przed reklamami spersonalizowanymi prosimy o <strong>zgodę</strong> w formularzu Google.</li>
<li>Opcjonalny zakup <strong>„Bez reklam”</strong> obsługuje Apple lub Google. Nie widzimy Twoich danych płatniczych.</li>
<li>Koselig <strong>nie zawiera analityki</strong> ani usługi raportowania awarii. Nie sprzedajemy danych osobowych.</li>
</ul>

<h2 id="device">1. Dane na Twoim urządzeniu</h2>
<p>Aby można było kontynuować grę, Koselig zapisuje na telefonie:</p>
<ul>
<li>postęp: odblokowane poziomy, bieżący układ klocków i trzy miejsca zapisu;</li>
<li>ustawienia: dźwięk, język, wybrany stół, tackę i klocki;</li>
<li>informację, czy masz zakup „Bez reklam”;</li>
<li>Twój wybór dotyczący zgody na reklamy, zapisywany na urządzeniu przez SDK zgody Google.</li>
</ul>
<p>Te dane zostają na urządzeniu i nie są do nas wysyłane. Usuwasz je razem z aplikacją. Po ponownej instalacji zakup „Bez reklam” można przywrócić z Apple lub Google (Ustawienia → <em>Przywróć</em>); postęp zaczyna się od nowa.</p>

<h2 id="ads">2. Reklamy: Google AdMob</h2>
<p>Koselig korzysta z <strong>Google Mobile Ads SDK</strong> (Google AdMob), aby wyświetlać filmy z nagrodą. Żeby film był gotowy, gdy o niego poprosisz, aplikacja uruchamia SDK przy starcie i wczytuje jeden film w tle. Dlatego Google może otrzymywać dane z urządzenia <strong>nawet wtedy, gdy nie obejrzysz żadnego filmu</strong>.</p>
<p>Google może zbierać i przetwarzać przez SDK m.in.:</p>
<ul>
<li>identyfikatory urządzenia: na Androidzie <strong>identyfikator wyświetlania reklam</strong>; na iPhonie identyfikator dostawcy (IDFV) i inne sygnały urządzenia;</li>
<li><strong>adres IP</strong>, na podstawie którego można określić przybliżoną lokalizację (kraj lub miasto);</li>
<li>informacje o urządzeniu i aplikacji: model, system i jego wersja, język, rozmiar ekranu, wersja aplikacji;</li>
<li>interakcje z reklamami: które reklamy zostały wczytane, wyświetlone, obejrzane do końca lub kliknięte.</li>
</ul>
<p>Google używa tych danych do wyświetlania i pomiaru reklam, zapobiegania oszustwom oraz — <strong>wyłącznie za Twoją zgodą tam, gdzie jest wymagana</strong> — do personalizacji reklam. Bez zgody Google może wyświetlać reklamy niespersonalizowane lub ograniczone, które również wykorzystują część danych urządzenia do limitu wyświetleń, pomiaru i ochrony przed oszustwami.</p>
<p><strong>Na iPhonie</strong> Koselig nie prosi o zgodę na śledzenie (App Tracking Transparency). Dlatego identyfikator reklamowy Apple (IDFA) nie jest dostępny ani dla aplikacji, ani dla Google.</p>
<p><strong>Sieci reklamowe.</strong> Korzystamy wyłącznie z Google AdMob i nie włączyliśmy mediacji z innymi sieciami. Wersja na Androida zawiera obecnie adaptery, przez które AdMob mógłby współpracować z Meta Audience Network i AppLovin; nie są one włączone na naszym koncie AdMob i planujemy je usunąć. Jeśli kiedykolwiek włączymy inną sieć, najpierw zaktualizujemy tę politykę.</p>
<p>Więcej u Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Jak Google wykorzystuje informacje z witryn i aplikacji korzystających z jego usług</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Polityka prywatności Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Polityka Google dotycząca zgody użytkowników z UE</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Narzędzia zgody Google dla aplikacji (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Moje centrum reklam — personalizacja reklam na koncie Google</a></li>
</ul>

<h2 id="consent">3. Zgoda i jak ją zmienić</h2>
<p>W regionach, w których zgoda jest wymagana, Koselig pokazuje formularz zgody Google (User Messaging Platform) przed pobraniem reklam. Możesz się zgodzić, odmówić lub wybrać cele. Wybór zmienisz w każdej chwili w grze: <strong>Ustawienia → Reklamy i dane</strong> (pozycja jest widoczna tam, gdzie obowiązują zasady zgody). Usunięcie i ponowna instalacja aplikacji również resetuje wybór.</p>
<p>Reklamy możesz też ograniczyć w telefonie: na Androidzie w <em>Ustawienia → Google → Reklamy</em> (zresetuj lub usuń identyfikator); na iPhonie w <em>Ustawienia → Prywatność i ochrona → Reklamy Apple</em>.</p>

<h2 id="purchases">4. Zakup „Bez reklam”</h2>
<p>Koselig oferuje jeden opcjonalny zakup w aplikacji — <strong>„Bez reklam”</strong> (produkt <code>koselig.no_ads</code>). Obsługuje go w całości <strong>Apple App Store</strong> lub <strong>Google Play</strong>. Nie otrzymujemy Twojego imienia, karty ani danych płatniczych. Aplikacja dostaje od sklepu tylko potwierdzenie, że zakup jest Twój, i zapisuje to na urządzeniu. Zobacz <a href="https://www.apple.com/legal/privacy/" rel="noopener">politykę prywatności Apple</a> i <a href="https://policies.google.com/privacy" rel="noopener">politykę prywatności Google</a>.</p>

<h2 id="no">5. Czego nie robimy</h2>
<ul>
<li>Nie ma kont, logowania ani funkcji społecznościowych.</li>
<li>Nie ma analityki, raportów awarii ani śledzenia z naszej strony.</li>
<li>Nie ma dostępu do kontaktów, zdjęć, aparatu, mikrofonu ani dokładnej lokalizacji.</li>
<li>Nie sprzedajemy danych osobowych i nie używamy ich do niczego poza tym, co tu opisano.</li>
</ul>
<p>Aplikacja korzysta z internetu (reklamy i zakup) oraz, na Androidzie, z wibracji jako informacji dotykowej.</p>

<h2 id="children">6. Dzieci</h2>
<p>Koselig to łamigłówka dla ogólnej publiczności. Nie jest skierowana do dzieci poniżej 13 lat i nie należy do kategorii dziecięcych. Reklamy w Koselig nie są skonfigurowane jako skierowane do dzieci. Świadomie nie zbieramy danych osobowych dzieci. Jeśli uważasz, że dziecko przekazało nam takie dane, napisz — usuniemy je.</p>

<h2 id="legal">7. Podstawy prawne (RODO)</h2>
<ul>
<li><strong>Zgoda</strong> (art. 6 ust. 1 lit. a RODO) — reklamy spersonalizowane oraz przechowywanie i odczyt informacji na urządzeniu tam, gdzie wymagana jest zgoda.</li>
<li><strong>Prawnie uzasadniony interes</strong> (art. 6 ust. 1 lit. f) — reklamy niespersonalizowane finansujące darmową grę, pomiar reklam i zapobieganie oszustwom.</li>
<li><strong>Umowa</strong> (art. 6 ust. 1 lit. b) — dostarczenie i przywrócenie zakupu „Bez reklam”.</li>
</ul>
<p>Google jest niezależnym administratorem danych zbieranych przez swój SDK. Google i Apple mogą przetwarzać dane poza Europejskim Obszarem Gospodarczym na podstawie własnych zabezpieczeń.</p>

<h2 id="retention">8. Jak długo przechowujemy dane</h2>
<p>Dane na urządzeniu pozostają tam do usunięcia aplikacji. Dane zebrane przez Google są przechowywane zgodnie z zasadami Google. Jeśli do nas napiszesz, przechowujemy Twój e-mail tak długo, jak to potrzebne do odpowiedzi i rozwiązania sprawy.</p>

<h2 id="rights">9. Twoje prawa</h2>
<p>Masz prawo dostępu do swoich danych, ich sprostowania i usunięcia, ograniczenia przetwarzania, sprzeciwu, przenoszenia danych oraz wycofania zgody w dowolnym momencie. Nie przechowujemy danych gry na serwerach, więc większość żądań realizuje usunięcie aplikacji; żądania dotyczące danych reklamowych kieruj do Google przez powyższe linki. Zawsze możesz napisać do nas: <a href="mailto:{EMAIL}">{EMAIL}</a>. Masz też prawo wnieść skargę do <a href="https://uodo.gov.pl/" rel="noopener">Prezesa Urzędu Ochrony Danych Osobowych (UODO)</a> lub do organu nadzorczego w swoim kraju.</p>

<h2 id="website">10. Ta strona</h2>
<p>coffeebeansstudio.eu to strona statyczna. Nie używa <strong>plików cookie, analityki ani zewnętrznych czcionek i skryptów</strong>. Jest hostowana w <strong>GitHub Pages</strong> (GitHub, Inc.), a DNS domeny obsługuje <strong>Cloudflare</strong>. Ci dostawcy mogą przetwarzać Twój adres IP i dane techniczne żądań w logach serwerów w celach bezpieczeństwa i dostarczania strony. Zobacz <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">oświadczenie GitHub o prywatności</a> i <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">politykę prywatności Cloudflare</a>.</p>

<h2 id="changes">11. Zmiany</h2>
<p>Jeśli aplikacja zacznie robić z danymi coś nowego — np. pojawi się inna sieć reklamowa lub analityka — zaktualizujemy tę stronę, zanim zmiana trafi do aplikacji, i zmienimy datę poniżej.</p>
""",
    t_title="Warunki korzystania — Coffee Beans Studio",
    t_desc="Krótkie i uczciwe warunki dla Koselig i innych gier Coffee Beans Studio.",
    t_h1="Warunki korzystania",
    t_sub="Koselig i inne gry Coffee Beans Studio",
    terms_html="""
<p class="note">Wiążąca jest wersja <a href="{R}terms/">angielska</a>. To tłumaczenie dla wygody.</p>
<p>Te warunki obowiązują, gdy korzystasz z <strong>Koselig</strong> lub innej gry <strong>Coffee Beans Studio</strong> (nazwa handlowa Dzmitry Kurtsikau, Polska). Grając, akceptujesz je. Są krótkie celowo.</p>
<h2>1. Gra</h2>
<p>Udzielamy Ci osobistego, niewyłącznego i nieprzenoszalnego prawa do instalowania naszych gier na swoich urządzeniach i grania w nie do celów niekomercyjnych. Prosimy nie kopiować, nie odsprzedawać, nie dekompilować i nie rozpowszechniać gry ani jej grafiki, poza przypadkami dozwolonymi przez prawo.</p>
<h2>2. Sklepy</h2>
<p>Gry pobierasz z Apple App Store lub Google Play i obowiązują też ich warunki. Dla aplikacji z App Store dodatkowo obowiązuje <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">standardowa umowa licencyjna Apple</a>. Apple i Google nie odpowiadają za grę ani jej wsparcie.</p>
<h2>3. Reklamy i zakup „Bez reklam”</h2>
<p>Koselig jest darmowa. Może pokazać krótki film z nagrodą, gdy prosisz o sprawdzenie „Impas?”. Reklamy dostarcza Google AdMob; nie kontrolujemy ich treści i nie odpowiadamy za reklamowane produkty osób trzecich.</p>
<p>„Bez reklam” to jednorazowy, trwały zakup. Dzięki niemu sprawdzanie „Impas?” działa bez filmów; liczba sprawdzeń na poziom się nie zmienia. Cenę pokazuje sklep przed zapłatą. Płatności, zwroty i anulowania obsługuje Apple lub Google na swoich zasadach. Zakup jest przypisany do Twojego Apple ID lub konta Google i można go przywrócić po ponownej instalacji (Ustawienia → <em>Przywróć</em>).</p>
<h2>4. Postęp</h2>
<p>Postęp jest zapisywany tylko na Twoim urządzeniu. Jeśli usuniesz aplikację lub stracisz urządzenie, nie odzyskamy go.</p>
<h2>5. Zmiany i dostępność</h2>
<p>Możemy aktualizować grę — dodawać, zmieniać i usuwać poziomy i funkcje — i możemy przestać ją oferować. Staramy się, żeby wszystko działało, ale nie obiecujemy, że gra zawsze będzie dostępna i wolna od błędów.</p>
<h2>6. Odpowiedzialność</h2>
<p>Gra jest udostępniana „tak jak jest”. W granicach dozwolonych przez prawo nie odpowiadamy za szkody pośrednie ani utratę danych. Nic tutaj nie ogranicza odpowiedzialności, której prawo nie pozwala ograniczyć, ani Twoich praw konsumenta wynikających z prawa Twojego kraju.</p>
<h2>7. Prawo</h2>
<p>Warunki podlegają prawu polskiemu. Jeśli jesteś konsumentem, zachowujesz ochronę bezwzględnie obowiązujących przepisów kraju, w którym mieszkasz.</p>
<h2>8. Kontakt</h2>
<p>Pytania i reklamacje: <a href="mailto:{EMAIL}">{EMAIL}</a>. Jak traktujemy dane — w <a href="{R}pl/privacy/">polityce prywatności</a>.</p>
""",
    s_title="Pomoc — Coffee Beans Studio",
    s_desc="Pomoc w Koselig: przywracanie zakupu „Bez reklam”, zaczynanie poziomu od nowa, zmiana języka, zgoda na reklamy i usuwanie danych.",
    s_h1="Pomoc",
    s_sub="Czytamy każdą wiadomość",
    s_mail_h="Napisz do nas",
    s_mail_p="Podaj model telefonu, wersję gry i co się stało. Zrzut ekranu bardzo pomaga.",
    s_faq_h="Pytania",
    faq=[
        ("Jak przywrócić zakup „Bez reklam”?",
         "Otwórz menu (☰ w prawym górnym rogu) → Ustawienia → przy <em>„Bez reklam”</em> stuknij <em>„Przywróć”</em>. Użyj tego samego Apple ID lub konta Google, na którym kupiłeś. Gra sprawdza zakup w sklepie przy każdym uruchomieniu, więc po ponownej instalacji wraca on sam, gdy tylko sklep odpowie."),
        ("Jak zacząć poziom od nowa?",
         "W Ustawieniach stuknij <em>„Zacznij od nowa”</em> i jeszcze raz, aby potwierdzić. Zresetuje to bieżący poziom. Aby skasować wszystko — postęp i ustawienia — usuń aplikację."),
        ("Jak zmienić język?",
         "Ustawienia → <em>„Język”</em>. Koselig mówi po polsku, angielsku, hiszpańsku, niemiecku, francusku, włosku i rosyjsku. <em>„Systemowy”</em> to język telefonu."),
        ("Kiedy gra pokazuje reklamy?",
         "Tylko gdy stukniesz <em>„Impas?”</em> i wybierzesz <em>„Obejrzyj filmik”</em>. Nie ma banerów ani wyskakujących reklam. Z „Bez reklam” sprawdzanie działa od razu."),
        ("Jak zmienić zgodę na reklamy?",
         "Ustawienia → <em>„Reklamy i dane”</em> ponownie otwiera formularz zgody Google. Pozycja jest widoczna tam, gdzie obowiązują zasady zgody."),
        ("Czy mogę zapisać układ i do niego wrócić?",
         "Tak. W Ustawieniach, w sekcji <em>„Zapisy”</em>, są trzy miejsca: <em>„Zapisz”</em> zachowuje bieżący układ, <em>„Wczytaj”</em> go przywraca."),
    ],
    s_del_h="Usuwanie danych",
    s_del_p="Koselig nie ma kont i przechowuje postęp tylko na urządzeniu. Usunięcie aplikacji usuwa wszystko, co zapisała. Danymi reklamowymi zarządza Google — zobacz <a href=\"{R}pl/koselig/delete-data/\">stronę o usuwaniu danych</a>.",
    d_title="Usuwanie danych — Koselig",
    d_desc="Jak usunąć dane gry Koselig: wszystko jest na urządzeniu — usuń aplikację. Danymi reklamowymi zarządza Google.",
    d_h1="Usuwanie danych",
    d_sub="Koselig, Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> nie ma kont, więc nie ma konta do usunięcia. Nie przechowujemy danych gry na serwerach.</p>
<h2>Dane na urządzeniu</h2>
<p>Postęp, zapisy, ustawienia, status zakupu „Bez reklam” i wybór dotyczący zgody na reklamy są zapisane tylko na telefonie. <strong>Aby usunąć wszystko, usuń aplikację</strong>:</p>
<ul>
<li><strong>iPhone:</strong> przytrzymaj ikonę Koselig → <em>Usuń aplikację</em> → <em>Usuń aplikację</em>.</li>
<li><strong>Android:</strong> przytrzymaj ikonę Koselig → <em>Informacje o aplikacji</em> → <em>Odinstaluj</em> (albo <em>Pamięć → Wyczyść pamięć</em>, aby zostawić aplikację, ale skasować jej dane).</li>
</ul>
<p>Usunięcie aplikacji nie anuluje zakupu „Bez reklam” — należy on do Twojego Apple ID lub konta Google i można go później przywrócić.</p>
<h2>Dane reklamowe</h2>
<p>Reklamy w Koselig dostarcza Google AdMob, a zebranymi danymi zarządza Google. Możesz:</p>
<ul>
<li>zresetować lub usunąć identyfikator wyświetlania reklam na Androidzie: <em>Ustawienia → Google → Reklamy</em>;</li>
<li>zmienić zgodę w grze: <em>Ustawienia → Reklamy i dane</em>;</li>
<li>zarządzać danymi na koncie Google: <a href="https://myadcenter.google.com/" rel="noopener">Moje centrum reklam</a> i <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Dane i prywatność</a>;</li>
<li>przeczytać, jak Google wykorzystuje dane z aplikacji: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>
<h2>Wiadomości do nas</h2>
<p>Jeśli do nas pisałeś i chcesz, abyśmy usunęli korespondencję, wyślij prośbę na <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> z tego samego adresu. Usuniemy ją w ciągu 30 dni i potwierdzimy.</p>
<p>Więcej: <a href="{R}pl/koselig/privacy/">polityka prywatności</a>.</p>
""",
    nf_title="Nie znaleziono strony — Coffee Beans Studio",
    nf_h1="Ta strona zgasła jak świeca",
    nf_p="Adres może być błędny albo strona została przeniesiona.",
    nf_cta="Wróć do studia",
)
