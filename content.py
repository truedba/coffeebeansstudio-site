# Тексты сайта coffeebeansstudio.eu на семи языках (как в игре). Факты об игре — только из кода ~/lotok (см. README.md, раздел «Откуда факты»).
# Правило отбора: фраза проходит, если её можно проверить в коде игры или в магазине; «красивое, но непроверяемое» — нет.

DATE_ISO = "2026-11-17"
EMAIL = "support@coffeebeansstudio.eu"

L = {}

# ─────────────────────────────── ENGLISH ───────────────────────────────
L["en"] = dict(
    name="English", short="EN", date="17 November 2026",
    nav_koselig="Koselig", nav_support="Support", skip="Skip to content", lang_label="Language",
    foot_legal="Privacy", foot_terms="Terms", foot_support="Support", foot_delete="Delete data",
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
<p>Koselig is published by <strong>Coffee Beans Studio</strong>. The controller of your personal data under the GDPR is <strong>Dzmitry Kurtsikau</strong>, a private individual based in Poland (“we”, “us”). For any question about privacy, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">In short</h2>
<ul>
<li>There are <strong>no accounts</strong> and no sign-in. We never ask for your name, email or phone number.</li>
<li>Your progress and settings are <strong>stored on your device</strong>; on iPhone they are also copied to your own iCloud account. We do not receive them.</li>
<li>The game shows ads <strong>only when you choose</strong> to watch a short rewarded video for the <em>Stuck?</em> check. There are no banners and no interstitial ads. The ads come from <strong>Google AdMob</strong>, which processes device data and identifiers.</li>
<li>Where the law requires it (for example in the EEA, the UK and Switzerland), you are asked for <strong>consent</strong> through Google’s consent form before personalised ads are shown.</li>
<li>The optional <strong>“No ads”</strong> purchase is handled by Apple or Google. We never see your payment details.</li>
<li>Koselig uses <strong>Google Firebase</strong> for game analytics and crash reports. They do not include your name, email or contacts. We do not sell personal data.</li>
</ul>

<h2 id="device">1. Data stored on your device</h2>
<p>Koselig saves the following on your phone so you can continue where you left off:</p>
<ul>
<li>game progress: opened levels, the current position of the pieces and your three save slots;</li>
<li>settings: sound, language, the chosen table, tray and pieces;</li>
<li>whether you own the “No ads” purchase;</li>
<li>your advertising consent choice, which is stored on the device by Google’s consent SDK.</li>
</ul>
<p>This data stays on your device and is not sent to us. It is deleted when you delete the app. <strong>On iPhone</strong>, progress and save slots are also copied to <strong>your own iCloud account</strong> (iCloud key-value storage), so you can continue on another device or after reinstalling. This copy is stored by Apple under your Apple ID; we cannot read it. You can stop it in iOS Settings → [your name] → iCloud. On Android the game does not use cloud saves, so after reinstalling progress starts again. The “No ads” purchase can always be restored from Apple or Google (Settings → <em>Restore</em>).</p>

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
<p><strong>On iPhone</strong>, Koselig asks once for permission to track (App Tracking Transparency) before ads are loaded. If you allow it, Google may use the Apple advertising identifier (IDFA) to personalise and measure ads. If you refuse, the IDFA is not available to the app or to Google, and the game works the same. You can change this at any time in iOS Settings → Privacy &amp; Security → Tracking.</p>
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

<h2 id="firebase">4. Game analytics and crash reports: Google Firebase</h2>
<p>Koselig uses <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> and <strong>Firebase Remote Config</strong> (Google). We use them to see which levels are too hard, to find and fix crashes and to adjust game settings without an app update.</p>
<ul>
<li><strong>Analytics</strong> receives an app-instance identifier generated by Firebase and events about how the game is used: levels started, finished or reset, hints and the <em>Stuck?</em> check, settings opened, language changed, the “No ads” purchase started, completed or failed. We do not link it to your name, email or advertising ID.</li>
<li><strong>Crashlytics</strong>, after a crash, receives a crash report: the technical state of the app, the stack trace, device model and OS version, and a Crashlytics installation identifier.</li>
<li><strong>Remote Config</strong> downloads game settings and sends your country, language, time zone, app and OS version.</li>
</ul>
<p>Google processes this data on our behalf. Analytics event data is kept for no longer than 14 months, crash reports for 90 days. See <a href="https://firebase.google.com/support/privacy" rel="noopener">Privacy and security in Firebase</a>.</p>
<h2 id="purchases">5. The “No ads” purchase</h2>
<p>Koselig offers one optional in-app purchase, <strong>“No ads”</strong> (product <code>koselig.no_ads</code>). It is processed entirely by the <strong>Apple App Store</strong> or <strong>Google Play</strong>. We do not receive your name, card or payment details. The app only receives confirmation from the store that the purchase is owned and stores that fact on your device. See the <a href="https://www.apple.com/legal/privacy/" rel="noopener">Apple Privacy Policy</a> and the <a href="https://policies.google.com/privacy" rel="noopener">Google Privacy Policy</a>.</p>

<h2 id="no">6. What we do not do</h2>
<ul>
<li>No accounts, no sign-in, no social features.</li>
<li>No tracking by us across other companies’ apps or websites.</li>
<li>No access to your contacts, photos, camera, microphone or precise location.</li>
<li>We do not sell personal data and we do not use it for anything except what is described here.</li>
</ul>
<p>The app uses internet access (for ads, analytics and crash reports, the purchase and, on iPhone, iCloud saves) and, on Android, vibration for haptic feedback.</p>

<h2 id="children">7. Children</h2>
<p>Koselig is a general-audience puzzle game. It is not directed at children under 13 and is not part of a children’s category. Ads in Koselig are not configured as child-directed. We do not knowingly collect personal information from children. If you believe a child has provided us with personal data, contact us and we will delete it.</p>

<h2 id="legal">8. Legal bases (GDPR)</h2>
<ul>
<li><strong>Consent</strong> (Art. 6(1)(a) GDPR) — personalised advertising and storing or accessing information on your device where consent is required.</li>
<li><strong>Legitimate interests</strong> (Art. 6(1)(f)) — showing non-personalised ads to fund a free game, ad measurement and fraud prevention.</li>
<li><strong>Legitimate interests</strong> (Art. 6(1)(f)) — game analytics and crash reports to fix and improve the game.</li>
<li><strong>Contract</strong> (Art. 6(1)(b)) — delivering and restoring the “No ads” purchase.</li>
</ul>
<p>Google acts as an independent controller for the data it collects through its SDK. Google and Apple may process data outside the European Economic Area under their own safeguards.</p>

<h2 id="retention">9. How long data is kept</h2>
<p>Data on your device stays there until you delete the app. The iCloud copy of your progress stays in your iCloud account. Analytics event data is kept for no longer than 14 months and crash reports for 90 days. Data collected by Google for ads is kept according to Google’s policies. If you write to us, we keep your email only as long as needed to answer and solve your request.</p>

<h2 id="rights">10. Your rights</h2>
<p>You have the right to access, correct and delete your personal data, to restrict or object to processing, to data portability and to withdraw consent at any time. Because we do not hold game data on our servers, most requests are answered by deleting the app; requests about advertising data can be made to Google through the links above. You can always write to us at <a href="mailto:{EMAIL}">{EMAIL}</a>. You also have the right to lodge a complaint with a supervisory authority — in Poland the <a href="https://uodo.gov.pl/" rel="noopener">President of the Personal Data Protection Office (UODO)</a> — or with the authority in your country.</p>

<h2 id="website">11. This website</h2>
<p>coffeebeansstudio.eu is a static website. It uses <strong>no cookies, no analytics and no third-party fonts or scripts</strong>. It is hosted on <strong>GitHub Pages</strong> (GitHub, Inc.), and its domain name service is provided by <strong>Cloudflare</strong>. These providers may process your IP address and technical request data in server logs for security and delivery. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a> and the <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Cloudflare Privacy Policy</a>.</p>

<h2 id="changes">12. Changes</h2>
<p>If the app starts doing something new with data — for example a new ad network or analytics — we will update this page before the change reaches the app, and change the date below.</p>
""",
    # terms
    t_title="Terms of Use — Coffee Beans Studio",
    t_desc="Short and honest terms for Koselig and other games by Coffee Beans Studio.",
    t_h1="Terms of Use",
    t_sub="Koselig and other games by Coffee Beans Studio",
    terms_html="""
<p>These terms apply when you use <strong>Koselig</strong> or another game by <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Poland). By playing, you agree to them. They are short on purpose.</p>

<h2>1. Playing the game</h2>
<p>We give you a personal, non-exclusive, non-transferable right to install and play our games on devices you own or control, for your own non-commercial use. Please do not copy, resell, reverse engineer or redistribute the game or its art, except where the law allows it.</p>

<h2>2. The stores</h2>
<p>You download our games from the Apple App Store or Google Play, and their terms apply too. For apps downloaded from the App Store, Apple’s <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Standard End User License Agreement</a> applies in addition to these terms. Apple and Google are not responsible for the game or for support.</p>

<h2>3. Ads and the “No ads” purchase</h2>
<p>Koselig is free. It can show a short rewarded video when you ask for a <em>Stuck?</em> check. The ads are provided by Google AdMob; we do not control their content and are not responsible for third-party products advertised in them.</p>
<p>“No ads” is a one-time, non-consumable purchase. It lets the <em>Stuck?</em> check work without videos; the number of checks per level stays the same. The price is shown by the store before you pay. Payment, refunds and cancellations are handled by Apple or Google under their policies. The purchase is tied to your Apple ID or Google account and can be restored after reinstalling (Settings → <em>Restore</em>).</p>

<h2>4. Your progress</h2>
<p>Progress is stored on your device and, on iPhone, also in your own iCloud account. If you delete the app or lose the device, we cannot recover progress for you; on iPhone it can come back from iCloud.</p>

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
         "Tap ☰ in the top right corner to open Settings, then tap <em>Restore</em> next to <em>No ads</em>. Use the same Apple ID or Google account you bought it with. The purchase is checked with the store every time the game starts, so it also comes back by itself after a reinstall once the store answers."),
        ("How do I start a level over?",
         "Open Settings and tap <em>Start over</em>, then tap again to confirm. This resets the current level. To erase everything — all progress and settings — delete the app."),
        ("How do I change the language?",
         "Settings → <em>Language</em>. Koselig speaks English, Español, Deutsch, Français, Italiano, Polski and Русский. <em>System</em> follows the language of your phone."),
        ("When does the game show ads?",
         "Only when you tap <em>Stuck?</em> and choose <em>Watch video</em>. There are no banners and no pop-up ads. With <em>No ads</em> the check works straight away."),
        ("How do I change my ad consent?",
         "In Settings, tap <em>Change</em> next to <em>Ads &amp; data</em> — Google’s consent form opens again. The item appears in regions where consent rules apply."),
        ("Can I keep a position and come back to it?",
         "Yes. Settings → <em>Saves</em> has three slots: <em>Save</em> stores the current position, <em>Load</em> brings it back."),
    ],
    s_del_h="Deleting your data",
    s_del_p="Koselig has no accounts. Progress is kept on your device and, on iPhone, in your own iCloud account. Deleting the app deletes everything it stored on the device. About ad, analytics and iCloud data — see the <a href=\"{R}koselig/delete-data/\">data deletion page</a>.",
    # delete data
    d_title="Delete your data — Koselig",
    d_desc="How to delete data related to the Koselig game: delete the app; the iCloud copy is managed by Apple; ad data is managed by Google.",
    d_h1="Delete your data",
    d_sub="Koselig by Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> has no accounts, so there is no account to delete. We do not keep your progress on our servers.</p>

<h2>Data on your device</h2>
<p>Progress, saves, settings, the “No ads” purchase status and your ad consent choice are stored on your phone. <strong>To delete all of it, delete the app</strong>:</p>
<ul>
<li><strong>iPhone:</strong> touch and hold the Koselig icon → <em>Remove App</em> → <em>Delete App</em>.</li>
<li><strong>Android:</strong> touch and hold the Koselig icon → <em>App info</em> → <em>Uninstall</em> (or <em>Storage → Clear storage</em> to keep the app but erase its data).</li>
</ul>
<p>Deleting the app does not cancel or remove the “No ads” purchase — it belongs to your Apple ID or Google account and can be restored later.</p>

<h2>iCloud copy (iPhone)</h2>
<p>On iPhone, progress and save slots are also copied to your own iCloud account. It is stored by Apple under your Apple ID. To stop it, turn off iCloud for Koselig in <em>Settings → [your name] → iCloud</em>.</p>
<h2>Analytics and crash reports</h2>
<p>Analytics events and crash reports (Google Firebase) are not linked to your name or email, so we cannot find one person’s records. They are deleted automatically: analytics events after no more than 14 months, crash reports after 90 days.</p>
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
    name="Русский", short="RU", date="17 ноября 2026",
    nav_koselig="Koselig", nav_support="Поддержка", skip="К содержанию", lang_label="Язык",
    foot_legal="Конфиденциальность", foot_terms="Условия", foot_support="Поддержка", foot_delete="Удаление данных",
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
<p>Koselig выпускает <strong>Coffee Beans Studio</strong>. Ответственный за ваши персональные данные (контролёр по GDPR) — <strong>Dzmitry Kurtsikau</strong>, частное лицо в Польше («мы»). По любым вопросам о данных пишите на <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">Коротко</h2>
<ul>
<li><strong>Аккаунтов нет</strong>, входа нет. Мы не спрашиваем имя, почту или телефон.</li>
<li>Прогресс и настройки <strong>хранятся на вашем устройстве</strong>; на iPhone они ещё копируются в ваш собственный iCloud. Мы их не получаем.</li>
<li>Реклама — <strong>только по вашему выбору</strong>: короткий ролик за награду для проверки «Тупик?». Баннеров и межстраничной рекламы нет. Ролики показывает <strong>Google AdMob</strong>, он обрабатывает данные устройства и идентификаторы.</li>
<li>Где этого требует закон (например, ЕЭЗ, Великобритания, Швейцария), перед персонализированной рекламой у вас спрашивают <strong>согласие</strong> через форму Google.</li>
<li>Необязательную покупку <strong>«Без рекламы»</strong> проводят Apple или Google. Платёжных данных мы не видим.</li>
<li>Koselig использует <strong>Google Firebase</strong> для игровой аналитики и отчётов о сбоях. В них нет вашего имени, почты и контактов. Мы не продаём персональные данные.</li>
</ul>

<h2 id="device">1. Данные на вашем устройстве</h2>
<p>Чтобы вы могли продолжить с того же места, Koselig сохраняет на телефоне:</p>
<ul>
<li>прогресс: открытые уровни, текущую позицию фигур и три ячейки сохранений;</li>
<li>настройки: звук, язык, выбранные стол, лоток и фигуры;</li>
<li>куплено ли «Без рекламы»;</li>
<li>ваш выбор по согласию на рекламу — его хранит на устройстве SDK согласия Google.</li>
</ul>
<p>Эти данные остаются на устройстве и нам не отправляются. Они удаляются вместе с приложением. <strong>На iPhone</strong> прогресс и сохранения ещё копируются в <strong>ваш собственный iCloud</strong> (хранилище «ключ–значение» iCloud), чтобы продолжить на другом устройстве или после переустановки. Эту копию хранит Apple под вашим Apple ID; прочитать её мы не можем. Отключить можно в Настройках iOS → [ваше имя] → iCloud. На Android облачных сохранений нет: после переустановки прогресс начнётся заново. Покупку «Без рекламы» всегда можно восстановить у Apple или Google (Настройки → <em>Восстановить</em>).</p>

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
<p><strong>На iPhone</strong> Koselig один раз спрашивает разрешение на отслеживание (App Tracking Transparency) перед загрузкой рекламы. Если вы разрешите, Google может использовать рекламный идентификатор Apple (IDFA), чтобы подбирать и измерять рекламу. Если откажете, IDFA недоступен ни приложению, ни Google, а игра работает так же. Изменить выбор можно в любой момент: Настройки iOS → Конфиденциальность и безопасность → Отслеживание.</p>
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

<h2 id="firebase">4. Игровая аналитика и отчёты о сбоях: Google Firebase</h2>
<p>Koselig использует <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> и <strong>Firebase Remote Config</strong> (Google). С их помощью мы видим, какие уровни слишком трудные, находим и чиним сбои и меняем настройки игры без обновления приложения.</p>
<ul>
<li><strong>Аналитика</strong> получает идентификатор экземпляра приложения, созданный Firebase, и события об игре: уровень начат, пройден или сброшен, подсказки и проверка <em>Тупик?</em>, открыты настройки, сменён язык, покупка «Без рекламы» начата, завершена или не удалась. Мы не связываем это с вашим именем, почтой или рекламным идентификатором.</li>
<li><strong>Crashlytics</strong> после сбоя получает отчёт: техническое состояние приложения, трассировку стека, модель устройства и версию ОС, идентификатор установки Crashlytics.</li>
<li><strong>Remote Config</strong> скачивает настройки игры и передаёт страну, язык, часовой пояс, версию приложения и ОС.</li>
</ul>
<p>Google обрабатывает эти данные по нашему поручению. События аналитики хранятся не дольше 14 месяцев, отчёты о сбоях — 90 дней. См. <a href="https://firebase.google.com/support/privacy" rel="noopener">Конфиденциальность и безопасность в Firebase</a>.</p>
<h2 id="purchases">5. Покупка «Без рекламы»</h2>
<p>В Koselig одна необязательная покупка — <strong>«Без рекламы»</strong> (товар <code>koselig.no_ads</code>). Её целиком проводят <strong>Apple App Store</strong> или <strong>Google Play</strong>. Мы не получаем ни имени, ни карты, ни платёжных данных. Приложение получает от магазина только подтверждение, что покупка есть, и запоминает это на устройстве. См. <a href="https://www.apple.com/legal/privacy/" rel="noopener">политику Apple</a> и <a href="https://policies.google.com/privacy" rel="noopener">политику Google</a>.</p>

<h2 id="no">6. Чего мы не делаем</h2>
<ul>
<li>Нет аккаунтов, входа и социальных функций.</li>
<li>Мы не отслеживаем вас в чужих приложениях и на чужих сайтах.</li>
<li>Нет доступа к контактам, фото, камере, микрофону и точному местоположению.</li>
<li>Мы не продаём персональные данные и не используем их ни для чего, кроме описанного здесь.</li>
</ul>
<p>Приложению нужен интернет (для рекламы, аналитики и отчётов о сбоях, покупки и, на iPhone, сохранений в iCloud) и, на Android, вибрация для тактильного отклика.</p>

<h2 id="children">7. Дети</h2>
<p>Koselig — головоломка для широкой аудитории. Она не предназначена для детей младше 13 лет и не входит в детские категории. Реклама в Koselig не настроена как реклама для детей. Мы сознательно не собираем персональные данные детей. Если вы считаете, что ребёнок передал нам такие данные, напишите нам — мы их удалим.</p>

<h2 id="legal">8. Правовые основания (GDPR)</h2>
<ul>
<li><strong>Согласие</strong> (ст. 6(1)(a) GDPR) — персонализированная реклама, а также хранение и чтение данных на устройстве, где требуется согласие.</li>
<li><strong>Законный интерес</strong> (ст. 6(1)(f)) — неперсонализированная реклама, на которую живёт бесплатная игра, измерение рекламы и защита от мошенничества.</li>
<li><strong>Законный интерес</strong> (ст. 6(1)(f)) — игровая аналитика и отчёты о сбоях, чтобы чинить и улучшать игру.</li>
<li><strong>Договор</strong> (ст. 6(1)(b)) — выдача и восстановление покупки «Без рекламы».</li>
</ul>
<p>Google — самостоятельный контролёр данных, которые собирает через свой SDK. Google и Apple могут обрабатывать данные за пределами ЕЭЗ со своими гарантиями защиты.</p>

<h2 id="retention">9. Сроки хранения</h2>
<p>Данные на устройстве хранятся, пока вы не удалите приложение. Копия прогресса в iCloud остаётся в вашем iCloud. События аналитики хранятся не дольше 14 месяцев, отчёты о сбоях — 90 дней. Рекламные данные Google хранятся по правилам Google. Если вы нам написали, мы храним вашу почту, пока это нужно для ответа и решения вопроса.</p>

<h2 id="rights">10. Ваши права</h2>
<p>Вы вправе получить доступ к своим данным, исправить и удалить их, ограничить обработку или возразить против неё, получить данные в переносимом виде и в любой момент отозвать согласие. Игровых данных на наших серверах нет, поэтому большинство запросов решается удалением приложения; запросы о рекламных данных — к Google по ссылкам выше. Нам всегда можно написать: <a href="mailto:{EMAIL}">{EMAIL}</a>. Вы также вправе подать жалобу в надзорный орган — в Польше это <a href="https://uodo.gov.pl/" rel="noopener">Председатель Управления по защите персональных данных (UODO)</a> — или в орган своей страны.</p>

<h2 id="website">11. Этот сайт</h2>
<p>coffeebeansstudio.eu — статический сайт. На нём <strong>нет cookie, аналитики, сторонних шрифтов и скриптов</strong>. Он размещён на <strong>GitHub Pages</strong> (GitHub, Inc.), DNS домена обслуживает <strong>Cloudflare</strong>. Эти провайдеры могут обрабатывать ваш IP-адрес и технические данные запросов в журналах серверов для безопасности и доставки. См. <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">заявление GitHub о конфиденциальности</a> и <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">политику Cloudflare</a>.</p>

<h2 id="changes">12. Изменения</h2>
<p>Если приложение начнёт делать с данными что-то новое — например, появится другая рекламная сеть или аналитика, — мы обновим эту страницу до того, как изменение попадёт в приложение, и поменяем дату ниже.</p>
""",
    t_title="Условия использования — Coffee Beans Studio",
    t_desc="Короткие и честные условия для Koselig и других игр Coffee Beans Studio.",
    t_h1="Условия использования",
    t_sub="Koselig и другие игры Coffee Beans Studio",
    terms_html="""
<p class="note">Юридически обязывающая версия — <a href="{R}terms/">английская</a>. Это перевод для удобства.</p>
<p>Эти условия действуют, когда вы пользуетесь <strong>Koselig</strong> или другой игрой <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Польша). Играя, вы с ними соглашаетесь. Они короткие нарочно.</p>
<h2>1. Игра</h2>
<p>Мы даём вам личное, неисключительное и непередаваемое право устанавливать наши игры на свои устройства и играть в них для некоммерческих целей. Пожалуйста, не копируйте, не перепродавайте, не декомпилируйте и не распространяйте игру и её графику, кроме случаев, разрешённых законом.</p>
<h2>2. Магазины</h2>
<p>Игры скачиваются из Apple App Store или Google Play, и их условия тоже действуют. Для приложений из App Store дополнительно действует <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">стандартное лицензионное соглашение Apple</a>. Apple и Google не отвечают за игру и её поддержку.</p>
<h2>3. Реклама и покупка «Без рекламы»</h2>
<p>Koselig бесплатна. Она может показать короткий ролик за награду, когда вы просите проверку «Тупик?». Рекламу показывает Google AdMob; мы не управляем её содержанием и не отвечаем за рекламируемые товары третьих лиц.</p>
<p>«Без рекламы» — разовая постоянная покупка. С ней проверка «Тупик?» работает без роликов; число проверок на уровне не меняется. Цену показывает магазин до оплаты. Оплату, возвраты и отмены проводят Apple или Google по своим правилам. Покупка привязана к вашему Apple ID или аккаунту Google и восстанавливается после переустановки (Настройки → <em>Восстановить</em>).</p>
<h2>4. Прогресс</h2>
<p>Прогресс хранится на вашем устройстве, а на iPhone ещё и в вашем собственном iCloud. Если удалить приложение или потерять устройство, мы восстановить прогресс не сможем; на iPhone он может вернуться из iCloud.</p>
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
         "Нажмите ☰ в правом верхнем углу, чтобы открыть Настройки, затем — <em>«Восстановить»</em> рядом с <em>«Без рекламы»</em>. Нужен тот же Apple ID или аккаунт Google, с которого была покупка. Игра сверяется с магазином при каждом запуске, так что после переустановки покупка вернётся и сама, как только магазин ответит."),
        ("Как начать уровень сначала?",
         "В настройках нажмите <em>«Начать сначала»</em> и ещё раз для подтверждения. Сбросится текущий уровень. Чтобы стереть всё — прогресс и настройки — удалите приложение."),
        ("Как сменить язык?",
         "Настройки → <em>«Язык»</em>. Koselig говорит по-русски, по-английски, по-испански, по-немецки, по-французски, по-итальянски и по-польски. <em>«Как в системе»</em> — язык телефона."),
        ("Когда игра показывает рекламу?",
         "Только когда вы нажимаете <em>«Тупик?»</em> и выбираете <em>«Смотреть ролик»</em>. Баннеров и всплывающей рекламы нет. С покупкой «Без рекламы» проверка срабатывает сразу."),
        ("Как изменить согласие на рекламу?",
         "В Настройках нажмите <em>«Изменить»</em> рядом с <em>«Реклама и данные»</em> — снова откроется форма согласия Google. Пункт виден там, где действуют правила о согласии."),
        ("Можно сохранить позицию и вернуться к ней?",
         "Да. В настройках, в разделе <em>«Позиции»</em>, три ячейки: <em>«Записать»</em> сохраняет текущую позицию, <em>«Открыть»</em> возвращает её."),
    ],
    s_del_h="Удаление данных",
    s_del_p="В Koselig нет аккаунтов. Прогресс хранится на устройстве, а на iPhone — ещё и в вашем iCloud. Удалите приложение — удалится всё, что оно хранило на устройстве. О рекламных данных, аналитике и iCloud — <a href=\"{R}ru/koselig/delete-data/\">страница об удалении данных</a>.",
    d_title="Удаление данных — Koselig",
    d_desc="Как удалить данные игры Koselig: удалите приложение; копией в iCloud распоряжается Apple, рекламными данными — Google.",
    d_h1="Удаление данных",
    d_sub="Koselig, Coffee Beans Studio",
    delete_html="""
<p>В <strong>Koselig</strong> нет аккаунтов, поэтому удалять аккаунт не нужно. Ваш прогресс на наших серверах мы не храним.</p>
<h2>Данные на устройстве</h2>
<p>Прогресс, сохранения, настройки, статус покупки «Без рекламы» и выбор по согласию на рекламу хранятся на телефоне. <strong>Чтобы удалить всё, удалите приложение</strong>:</p>
<ul>
<li><strong>iPhone:</strong> нажмите и удерживайте значок Koselig → <em>Удалить приложение</em> → <em>Удалить приложение</em>.</li>
<li><strong>Android:</strong> нажмите и удерживайте значок Koselig → <em>О приложении</em> → <em>Удалить</em> (или <em>Хранилище → Очистить хранилище</em>, чтобы оставить приложение, но стереть его данные).</li>
</ul>
<p>Удаление приложения не отменяет покупку «Без рекламы» — она принадлежит вашему Apple ID или аккаунту Google и восстанавливается позже.</p>
<h2>Копия в iCloud (iPhone)</h2>
<p>На iPhone прогресс и сохранения ещё копируются в ваш собственный iCloud. Эту копию хранит Apple под вашим Apple ID. Чтобы отключить, выключите iCloud для Koselig: <em>Настройки → [ваше имя] → iCloud</em>.</p>
<h2>Аналитика и отчёты о сбоях</h2>
<p>События аналитики и отчёты о сбоях (Google Firebase) не связаны с вашим именем или почтой, поэтому найти записи одного человека мы не можем. Они удаляются сами: события аналитики — не позже чем через 14 месяцев, отчёты о сбоях — через 90 дней.</p>
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
    name="Polski", short="PL", date="17 listopada 2026",
    nav_koselig="Koselig", nav_support="Pomoc", skip="Przejdź do treści", lang_label="Język",
    foot_legal="Prywatność", foot_terms="Warunki", foot_support="Pomoc", foot_delete="Usuwanie danych",
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
<p>Koselig wydaje <strong>Coffee Beans Studio</strong>. Administratorem Twoich danych osobowych w rozumieniu RODO jest <strong>Dzmitry Kurtsikau</strong>, osoba prywatna z Polski („my”). W sprawach prywatności pisz na <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">W skrócie</h2>
<ul>
<li><strong>Nie ma kont</strong> ani logowania. Nie pytamy o imię, e-mail ani numer telefonu.</li>
<li>Postęp i ustawienia <strong>są zapisywane na Twoim urządzeniu</strong>; na iPhonie są też kopiowane do Twojego własnego iCloud. Nie otrzymujemy ich.</li>
<li>Reklamy pojawiają się <strong>tylko wtedy, gdy sam wybierzesz</strong> krótki film z nagrodą przy sprawdzaniu „Impas?”. Nie ma banerów ani reklam pełnoekranowych. Reklamy dostarcza <strong>Google AdMob</strong>, który przetwarza dane urządzenia i identyfikatory.</li>
<li>Tam, gdzie wymaga tego prawo (np. w EOG, Wielkiej Brytanii i Szwajcarii), przed reklamami spersonalizowanymi prosimy o <strong>zgodę</strong> w formularzu Google.</li>
<li>Opcjonalny zakup <strong>„Bez reklam”</strong> obsługuje Apple lub Google. Nie widzimy Twoich danych płatniczych.</li>
<li>Koselig korzysta z <strong>Google Firebase</strong> do analityki gry i raportów awarii. Nie zawierają one Twojego imienia, e-maila ani kontaktów. Nie sprzedajemy danych osobowych.</li>
</ul>

<h2 id="device">1. Dane na Twoim urządzeniu</h2>
<p>Aby można było kontynuować grę, Koselig zapisuje na telefonie:</p>
<ul>
<li>postęp: odblokowane poziomy, bieżący układ klocków i trzy miejsca zapisu;</li>
<li>ustawienia: dźwięk, język, wybrany stół, tackę i klocki;</li>
<li>informację, czy masz zakup „Bez reklam”;</li>
<li>Twój wybór dotyczący zgody na reklamy, zapisywany na urządzeniu przez SDK zgody Google.</li>
</ul>
<p>Te dane zostają na urządzeniu i nie są do nas wysyłane. Usuwasz je razem z aplikacją. <strong>Na iPhonie</strong> postęp i zapisy są też kopiowane do <strong>Twojego własnego iCloud</strong> (magazyn klucz–wartość iCloud), aby można było grać dalej na innym urządzeniu lub po ponownej instalacji. Tę kopię przechowuje Apple w ramach Twojego Apple ID; nie możemy jej odczytać. Możesz to wyłączyć w Ustawieniach iOS → [Twoje imię] → iCloud. Na Androidzie gra nie korzysta z zapisów w chmurze, więc po ponownej instalacji postęp zaczyna się od nowa. Zakup „Bez reklam” zawsze można przywrócić z Apple lub Google (Ustawienia → <em>Przywróć</em>).</p>

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
<p><strong>Na iPhonie</strong> Koselig raz prosi o zgodę na śledzenie (App Tracking Transparency) przed wczytaniem reklam. Jeśli się zgodzisz, Google może używać identyfikatora reklamowego Apple (IDFA) do personalizacji i pomiaru reklam. Jeśli odmówisz, IDFA nie jest dostępny ani dla aplikacji, ani dla Google, a gra działa tak samo. Możesz to zmienić w każdej chwili: Ustawienia iOS → Prywatność i ochrona → Śledzenie.</p>
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

<h2 id="firebase">4. Analityka gry i raporty awarii: Google Firebase</h2>
<p>Koselig korzysta z <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> i <strong>Firebase Remote Config</strong> (Google). Dzięki nim widzimy, które poziomy są za trudne, znajdujemy i naprawiamy awarie oraz zmieniamy ustawienia gry bez aktualizacji aplikacji.</p>
<ul>
<li><strong>Analityka</strong> otrzymuje identyfikator instancji aplikacji utworzony przez Firebase i zdarzenia o grze: poziom rozpoczęty, ukończony lub zresetowany, podpowiedzi i sprawdzenie <em>Impas?</em>, otwarte ustawienia, zmiana języka, zakup „Bez reklam” rozpoczęty, zakończony lub nieudany. Nie łączymy tego z Twoim imieniem, e-mailem ani identyfikatorem reklamowym.</li>
<li><strong>Crashlytics</strong> po awarii otrzymuje raport: stan techniczny aplikacji, ślad stosu, model urządzenia i wersję systemu oraz identyfikator instalacji Crashlytics.</li>
<li><strong>Remote Config</strong> pobiera ustawienia gry i wysyła kraj, język, strefę czasową, wersję aplikacji i systemu.</li>
</ul>
<p>Google przetwarza te dane w naszym imieniu. Zdarzenia analityki są przechowywane nie dłużej niż 14 miesięcy, raporty awarii — 90 dni. Zobacz <a href="https://firebase.google.com/support/privacy" rel="noopener">Prywatność i bezpieczeństwo w Firebase</a>.</p>
<h2 id="purchases">5. Zakup „Bez reklam”</h2>
<p>Koselig oferuje jeden opcjonalny zakup w aplikacji — <strong>„Bez reklam”</strong> (produkt <code>koselig.no_ads</code>). Obsługuje go w całości <strong>Apple App Store</strong> lub <strong>Google Play</strong>. Nie otrzymujemy Twojego imienia, karty ani danych płatniczych. Aplikacja dostaje od sklepu tylko potwierdzenie, że zakup jest Twój, i zapisuje to na urządzeniu. Zobacz <a href="https://www.apple.com/legal/privacy/" rel="noopener">politykę prywatności Apple</a> i <a href="https://policies.google.com/privacy" rel="noopener">politykę prywatności Google</a>.</p>

<h2 id="no">6. Czego nie robimy</h2>
<ul>
<li>Nie ma kont, logowania ani funkcji społecznościowych.</li>
<li>Nie śledzimy Cię w aplikacjach ani na stronach innych firm.</li>
<li>Nie ma dostępu do kontaktów, zdjęć, aparatu, mikrofonu ani dokładnej lokalizacji.</li>
<li>Nie sprzedajemy danych osobowych i nie używamy ich do niczego poza tym, co tu opisano.</li>
</ul>
<p>Aplikacja korzysta z internetu (reklamy, analityka i raporty awarii, zakup oraz, na iPhonie, zapisy w iCloud) oraz, na Androidzie, z wibracji jako informacji dotykowej.</p>

<h2 id="children">7. Dzieci</h2>
<p>Koselig to łamigłówka dla ogólnej publiczności. Nie jest skierowana do dzieci poniżej 13 lat i nie należy do kategorii dziecięcych. Reklamy w Koselig nie są skonfigurowane jako skierowane do dzieci. Świadomie nie zbieramy danych osobowych dzieci. Jeśli uważasz, że dziecko przekazało nam takie dane, napisz — usuniemy je.</p>

<h2 id="legal">8. Podstawy prawne (RODO)</h2>
<ul>
<li><strong>Zgoda</strong> (art. 6 ust. 1 lit. a RODO) — reklamy spersonalizowane oraz przechowywanie i odczyt informacji na urządzeniu tam, gdzie wymagana jest zgoda.</li>
<li><strong>Prawnie uzasadniony interes</strong> (art. 6 ust. 1 lit. f) — reklamy niespersonalizowane finansujące darmową grę, pomiar reklam i zapobieganie oszustwom.</li>
<li><strong>Prawnie uzasadniony interes</strong> (art. 6 ust. 1 lit. f) — analityka gry i raporty awarii, aby naprawiać i ulepszać grę.</li>
<li><strong>Umowa</strong> (art. 6 ust. 1 lit. b) — dostarczenie i przywrócenie zakupu „Bez reklam”.</li>
</ul>
<p>Google jest niezależnym administratorem danych zbieranych przez swój SDK. Google i Apple mogą przetwarzać dane poza Europejskim Obszarem Gospodarczym na podstawie własnych zabezpieczeń.</p>

<h2 id="retention">9. Jak długo przechowujemy dane</h2>
<p>Dane na urządzeniu pozostają tam do usunięcia aplikacji. Kopia postępu w iCloud pozostaje na Twoim koncie iCloud. Zdarzenia analityki są przechowywane nie dłużej niż 14 miesięcy, raporty awarii — 90 dni. Dane reklamowe zebrane przez Google są przechowywane zgodnie z zasadami Google. Jeśli do nas napiszesz, przechowujemy Twój e-mail tak długo, jak to potrzebne do odpowiedzi i rozwiązania sprawy.</p>

<h2 id="rights">10. Twoje prawa</h2>
<p>Masz prawo dostępu do swoich danych, ich sprostowania i usunięcia, ograniczenia przetwarzania, sprzeciwu, przenoszenia danych oraz wycofania zgody w dowolnym momencie. Nie przechowujemy danych gry na serwerach, więc większość żądań realizuje usunięcie aplikacji; żądania dotyczące danych reklamowych kieruj do Google przez powyższe linki. Zawsze możesz napisać do nas: <a href="mailto:{EMAIL}">{EMAIL}</a>. Masz też prawo wnieść skargę do <a href="https://uodo.gov.pl/" rel="noopener">Prezesa Urzędu Ochrony Danych Osobowych (UODO)</a> lub do organu nadzorczego w swoim kraju.</p>

<h2 id="website">11. Ta strona</h2>
<p>coffeebeansstudio.eu to strona statyczna. Nie używa <strong>plików cookie, analityki ani zewnętrznych czcionek i skryptów</strong>. Jest hostowana w <strong>GitHub Pages</strong> (GitHub, Inc.), a DNS domeny obsługuje <strong>Cloudflare</strong>. Ci dostawcy mogą przetwarzać Twój adres IP i dane techniczne żądań w logach serwerów w celach bezpieczeństwa i dostarczania strony. Zobacz <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">oświadczenie GitHub o prywatności</a> i <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">politykę prywatności Cloudflare</a>.</p>

<h2 id="changes">12. Zmiany</h2>
<p>Jeśli aplikacja zacznie robić z danymi coś nowego — np. pojawi się inna sieć reklamowa lub analityka — zaktualizujemy tę stronę, zanim zmiana trafi do aplikacji, i zmienimy datę poniżej.</p>
""",
    t_title="Warunki korzystania — Coffee Beans Studio",
    t_desc="Krótkie i uczciwe warunki dla Koselig i innych gier Coffee Beans Studio.",
    t_h1="Warunki korzystania",
    t_sub="Koselig i inne gry Coffee Beans Studio",
    terms_html="""
<p class="note">Wiążąca jest wersja <a href="{R}terms/">angielska</a>. To tłumaczenie dla wygody.</p>
<p>Te warunki obowiązują, gdy korzystasz z <strong>Koselig</strong> lub innej gry <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Polska). Grając, akceptujesz je. Są krótkie celowo.</p>
<h2>1. Gra</h2>
<p>Udzielamy Ci osobistego, niewyłącznego i nieprzenoszalnego prawa do instalowania naszych gier na swoich urządzeniach i grania w nie do celów niekomercyjnych. Prosimy nie kopiować, nie odsprzedawać, nie dekompilować i nie rozpowszechniać gry ani jej grafiki, poza przypadkami dozwolonymi przez prawo.</p>
<h2>2. Sklepy</h2>
<p>Gry pobierasz z Apple App Store lub Google Play i obowiązują też ich warunki. Dla aplikacji z App Store dodatkowo obowiązuje <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">standardowa umowa licencyjna Apple</a>. Apple i Google nie odpowiadają za grę ani jej wsparcie.</p>
<h2>3. Reklamy i zakup „Bez reklam”</h2>
<p>Koselig jest darmowa. Może pokazać krótki film z nagrodą, gdy prosisz o sprawdzenie „Impas?”. Reklamy dostarcza Google AdMob; nie kontrolujemy ich treści i nie odpowiadamy za reklamowane produkty osób trzecich.</p>
<p>„Bez reklam” to jednorazowy, trwały zakup. Dzięki niemu sprawdzanie „Impas?” działa bez filmów; liczba sprawdzeń na poziom się nie zmienia. Cenę pokazuje sklep przed zapłatą. Płatności, zwroty i anulowania obsługuje Apple lub Google na swoich zasadach. Zakup jest przypisany do Twojego Apple ID lub konta Google i można go przywrócić po ponownej instalacji (Ustawienia → <em>Przywróć</em>).</p>
<h2>4. Postęp</h2>
<p>Postęp jest zapisywany na Twoim urządzeniu, a na iPhonie także w Twoim własnym iCloud. Jeśli usuniesz aplikację lub stracisz urządzenie, nie odzyskamy go; na iPhonie może wrócić z iCloud.</p>
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
         "Stuknij ☰ w prawym górnym rogu, aby otworzyć Ustawienia, a potem stuknij <em>„Przywróć”</em> przy <em>„Bez reklam”</em>. Użyj tego samego Apple ID lub konta Google, na którym kupiłeś. Gra sprawdza zakup w sklepie przy każdym uruchomieniu, więc po ponownej instalacji wraca on sam, gdy tylko sklep odpowie."),
        ("Jak zacząć poziom od nowa?",
         "W Ustawieniach stuknij <em>„Zacznij od nowa”</em> i jeszcze raz, aby potwierdzić. Zresetuje to bieżący poziom. Aby skasować wszystko — postęp i ustawienia — usuń aplikację."),
        ("Jak zmienić język?",
         "Ustawienia → <em>„Język”</em>. Koselig mówi po polsku, angielsku, hiszpańsku, niemiecku, francusku, włosku i rosyjsku. <em>„Systemowy”</em> to język telefonu."),
        ("Kiedy gra pokazuje reklamy?",
         "Tylko gdy stukniesz <em>„Impas?”</em> i wybierzesz <em>„Obejrzyj filmik”</em>. Nie ma banerów ani wyskakujących reklam. Z „Bez reklam” sprawdzanie działa od razu."),
        ("Jak zmienić zgodę na reklamy?",
         "W Ustawieniach dotknij <em>„Zmień”</em> obok <em>„Reklamy i dane”</em> — formularz zgody Google otworzy się ponownie. Pozycja jest widoczna tam, gdzie obowiązują zasady zgody."),
        ("Czy mogę zapisać układ i do niego wrócić?",
         "Tak. W Ustawieniach, w sekcji <em>„Zapisy”</em>, są trzy miejsca: <em>„Zapisz”</em> zachowuje bieżący układ, <em>„Wczytaj”</em> go przywraca."),
    ],
    s_del_h="Usuwanie danych",
    s_del_p="Koselig nie ma kont. Postęp jest zapisany na urządzeniu, a na iPhonie także w Twoim iCloud. Usunięcie aplikacji usuwa wszystko, co zapisała na urządzeniu. O danych reklamowych, analityce i iCloud — <a href=\"{R}pl/koselig/delete-data/\">strona o usuwaniu danych</a>.",
    d_title="Usuwanie danych — Koselig",
    d_desc="Jak usunąć dane gry Koselig: usuń aplikację; kopią w iCloud zarządza Apple, danymi reklamowymi — Google.",
    d_h1="Usuwanie danych",
    d_sub="Koselig, Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> nie ma kont, więc nie ma konta do usunięcia. Nie przechowujemy Twojego postępu na naszych serwerach.</p>
<h2>Dane na urządzeniu</h2>
<p>Postęp, zapisy, ustawienia, status zakupu „Bez reklam” i wybór dotyczący zgody na reklamy są zapisane na telefonie. <strong>Aby usunąć wszystko, usuń aplikację</strong>:</p>
<ul>
<li><strong>iPhone:</strong> przytrzymaj ikonę Koselig → <em>Usuń aplikację</em> → <em>Usuń aplikację</em>.</li>
<li><strong>Android:</strong> przytrzymaj ikonę Koselig → <em>Informacje o aplikacji</em> → <em>Odinstaluj</em> (albo <em>Pamięć → Wyczyść pamięć</em>, aby zostawić aplikację, ale skasować jej dane).</li>
</ul>
<p>Usunięcie aplikacji nie anuluje zakupu „Bez reklam” — należy on do Twojego Apple ID lub konta Google i można go później przywrócić.</p>
<h2>Kopia w iCloud (iPhone)</h2>
<p>Na iPhonie postęp i zapisy są też kopiowane do Twojego własnego iCloud. Przechowuje je Apple w ramach Twojego Apple ID. Aby to wyłączyć, wyłącz iCloud dla Koselig: <em>Ustawienia → [Twoje imię] → iCloud</em>.</p>
<h2>Analityka i raporty awarii</h2>
<p>Zdarzenia analityki i raporty awarii (Google Firebase) nie są powiązane z Twoim imieniem ani e-mailem, więc nie możemy znaleźć zapisów jednej osoby. Usuwają się same: zdarzenia analityki najpóźniej po 14 miesiącach, raporty awarii po 90 dniach.</p>
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

# ─────────────────────────────── ESPAÑOL ───────────────────────────────
# Термины игры — колонка «es» ~/lotok/tools/teksty_gen.py; правовые тексты — смысл английских без изменений.
L["es"] = dict(
    name="Español", short="ES", date="17 de noviembre de 2026",
    nav_koselig="Koselig", nav_support="Soporte", skip="Saltar al contenido", lang_label="Idioma",
    foot_legal="Privacidad", foot_terms="Condiciones", foot_support="Soporte", foot_delete="Eliminar datos",
    soon_stores="Próximamente en el App Store y Google Play",
    home_title="Coffee Beans Studio — juegos acogedores e ingeniosos",
    home_desc="Coffee Beans Studio es un pequeño estudio independiente que hace juegos acogedores e ingeniosos. Nuestro primer juego, Koselig, es un rompecabezas con bandeja de madera para iPhone y Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Juegos tranquilos<br>para veladas cálidas",
    hero_p="Hacemos juegos acogedores e ingeniosos, de esos que se juegan despacio, con una taza de té y a la luz de una vela.",
    hero_cta="Conoce Koselig",
    ch1_h="A fuego lento",
    ch1_p="Coffee Beans Studio es un pequeño estudio independiente. Nos importan los rompecabezas tranquilos, los materiales cálidos y el diseño honesto: las cosas que se acarician con la mirada —madera, lino, luz de vela— y las reglas que se aprenden en un minuto.",
    ch2_h="Koselig",
    ch2_sub="Un rompecabezas con bandeja de madera",
    ch2_p="Encaja todas las piezas en la bandeja de madera. Cambia la mesa, la bandeja y las piezas según tu estado de ánimo: roble o lino, nogal o latón, pintura o piedra. Y si te atascas, un pequeño bonsái puede decirte si la posición aún tiene solución.",
    ch2_cta="Sobre el juego",
    word_q="koselig",
    word_def="<em>noruego</em> — acogedor, cálido, entrañable. La sensación de una vela, una manta y buena compañía.",
    soon_h="Casi a punto",
    soon_p="Koselig se prepara para llegar al App Store y a Google Play. El día del lanzamiento encontrarás aquí los enlaces.",
    end_h="Escríbenos",
    end_p="¿Preguntas, ideas o un fallo en algún rompecabezas? Leemos todos los mensajes.",
    # Koselig
    k_title="Koselig — un acogedor rompecabezas con bandeja de madera para iPhone y Android",
    k_desc="Koselig es un rompecabezas tranquilo con bandeja de madera: encaja todas las piezas, elige tu mesa, tu bandeja y tus piezas, y deja que un pequeño bonsái florezca cuando lo resuelvas. Próximamente en el App Store y Google Play.",
    k_eyebrow="Un juego de Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Un acogedor rompecabezas con bandeja de madera. Encaja todas las piezas en la bandeja y tómate tu tiempo.",
    k_about_h="Un rompecabezas sin prisas",
    k_about_p=[
        "Koselig es un rompecabezas digital con bandeja de madera. Las piezas están sobre la mesa, alrededor de la bandeja: las tomas, las giras y las encajas hasta llenar todas las casillas.",
        "Los niveles te llevan por un mapa, desde bandejas pequeñas hasta la bandeja completa. Hay más de una forma de llenar una bandeja, y también una solución más estricta, en la que no se tocan piezas del mismo color.",
        "Cuando no tengas claro si una posición aún tiene solución, toca <em>¿Atascado?</em> y el bonsái la comprobará por ti tras un video corto que eliges ver, o al instante si has comprado <em>Sin anuncios</em>.",
    ],
    k_feat_h="Qué hay dentro",
    k_feats=[
        ("Tres mesas", "Roble, lino y nogal, cada una con su propia vida tranquila: una vela, el vapor sobre el té, lavanda mecida por la brisa."),
        ("Bandejas y piezas", "Bandejas de pino, nogal, piedra, acero, latón, olivo y cerezo. Piezas: pintura, madera, piedra, metal y terrazo."),
        ("Un mapa de niveles", "Primeros pasos suaves en bandejas más pequeñas y, después, el rompecabezas completo."),
        ("El bonsái", "Te ayuda con la comprobación <em>¿Atascado?</em> y florece cuando resuelves un nivel."),
        ("Partidas", "Tres espacios de guardado para las posiciones a las que quieras volver."),
        ("Siete idiomas", "Español, English, Deutsch, Français, Italiano, Polski y Русский."),
    ],
    k_ads_h="Juego limpio con los anuncios",
    k_ads_p="Ni banners ni anuncios emergentes. Un video corto solo se reproduce cuando pides una comprobación <em>¿Atascado?</em> y decides verlo. Una compra opcional, <em>Sin anuncios</em>, hace que la comprobación funcione sin videos.",
    k_shots_h="Capturas de pantalla",
    k_shot_alts=[
        "Una bandeja pequeña sobre la mesa de lino, con algunas piezas alrededor",
        "La mesa de nogal con la bandeja de madera y piezas arriba y abajo",
        "La tarjeta «¿Atascado?» con un bonsái en su maceta",
        "La pantalla «¡Resuelto!» con el bonsái y el tiempo del nivel",
        "El mapa de niveles: un sendero entre colinas otoñales hasta una casa en lo alto",
        "Ajustes: piezas, bandeja, mesa, partidas, sonido, idioma y «Sin anuncios»",
    ],
    k_platforms="iPhone y Android · español, English, Deutsch, Français, Italiano, Polski, Русский",
    k_links_h="Conviene saber",
    # legal common
    legal_updated="Última actualización",
    # privacy
    p_title="Política de privacidad — Koselig",
    p_desc="Cómo tratan tus datos el juego Koselig y coffeebeansstudio.eu: sin cuentas, el progreso en tu dispositivo, Google AdMob para videos con recompensa opcionales y compras a través de Apple y Google.",
    p_h1="Política de privacidad",
    p_sub="Koselig y coffeebeansstudio.eu",
    privacy_html="""
<p class="note">La versión jurídicamente vinculante es la <a href="{R}koselig/privacy/">inglesa</a>. Esta es su traducción fiel, para tu comodidad.</p>
<p>Esta política explica qué ocurre con tus datos cuando juegas a <strong>Koselig</strong> en iPhone o Android y cuando visitas <strong>coffeebeansstudio.eu</strong>. La redactamos para que se ajuste a lo que la aplicación hace realmente.</p>

<h2 id="who">Quiénes somos</h2>
<p>Koselig lo publica <strong>Coffee Beans Studio</strong>. El responsable del tratamiento de tus datos personales según el RGPD es <strong>Dzmitry Kurtsikau</strong>, persona física establecida en Polonia («nosotros»). Para cualquier pregunta sobre privacidad, escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">En resumen</h2>
<ul>
<li><strong>No hay cuentas</strong> ni inicio de sesión. Nunca te pedimos tu nombre, tu correo electrónico ni tu número de teléfono.</li>
<li>Tu progreso y tus ajustes <strong>se guardan en tu dispositivo</strong>; en iPhone también se copian a tu propia cuenta de iCloud. Nosotros no los recibimos.</li>
<li>El juego muestra anuncios <strong>solo cuando tú decides</strong> ver un video corto con recompensa a cambio de la comprobación <em>¿Atascado?</em>; no hay banners ni anuncios intersticiales. Los anuncios los proporciona <strong>Google AdMob</strong>, que trata datos e identificadores del dispositivo.</li>
<li>Donde la ley lo exige (por ejemplo, en el EEE, el Reino Unido y Suiza), se te pide el <strong>consentimiento</strong> mediante el formulario de consentimiento de Google antes de mostrarte anuncios personalizados.</li>
<li>La compra opcional <strong>«Sin anuncios»</strong> la gestionan Apple o Google. Nunca vemos tus datos de pago.</li>
<li>Koselig usa <strong>Google Firebase</strong> para la analítica del juego y los informes de fallos. No incluyen tu nombre, tu correo ni tus contactos. No vendemos datos personales.</li>
</ul>

<h2 id="device">1. Datos guardados en tu dispositivo</h2>
<p>Koselig guarda lo siguiente en tu teléfono para que puedas seguir donde lo dejaste:</p>
<ul>
<li>el progreso del juego: los niveles desbloqueados, la posición actual de las piezas y tus tres espacios de guardado;</li>
<li>los ajustes: sonido, idioma y la mesa, la bandeja y las piezas que hayas elegido;</li>
<li>si tienes la compra «Sin anuncios»;</li>
<li>tu elección sobre el consentimiento publicitario, que el SDK de consentimiento de Google guarda en el dispositivo.</li>
</ul>
<p>Estos datos permanecen en tu dispositivo y no se nos envían. Se borran al eliminar la aplicación. <strong>En iPhone</strong>, el progreso y las partidas guardadas también se copian a <strong>tu propia cuenta de iCloud</strong> (almacenamiento clave-valor de iCloud), para que puedas seguir en otro dispositivo o tras reinstalar. Esa copia la guarda Apple con tu Apple ID; nosotros no podemos leerla. Puedes desactivarla en Ajustes de iOS → [tu nombre] → iCloud. En Android el juego no usa guardado en la nube, así que tras reinstalar el progreso empieza de cero. La compra «Sin anuncios» siempre se puede restaurar desde Apple o Google (Ajustes → <em>Restaurar</em>).</p>

<h2 id="ads">2. Publicidad: Google AdMob</h2>
<p>Koselig usa el <strong>Google Mobile Ads SDK</strong> (Google AdMob) para mostrar videos con recompensa. Para tener un video listo cuando lo pidas, la aplicación inicia el SDK al abrirse y carga un video en segundo plano. Esto significa que Google puede recibir datos de tu dispositivo <strong>aunque nunca llegues a ver un video</strong>.</p>
<p>Entre los datos que Google puede recopilar y tratar a través del SDK están:</p>
<ul>
<li>identificadores del dispositivo: en Android, el <strong>ID de publicidad</strong>; en iPhone, el identificador del proveedor (IDFV) y otras señales del dispositivo;</li>
<li>tu <strong>dirección IP</strong>, que puede usarse para estimar una ubicación aproximada (país o ciudad);</li>
<li>información del dispositivo y de la aplicación: modelo, sistema operativo y su versión, idioma, tamaño de pantalla y versión de la aplicación;</li>
<li>interacciones con los anuncios: qué anuncios se cargaron, se mostraron, se vieron hasta el final o se tocaron.</li>
</ul>
<p>Google usa estos datos para publicar y medir anuncios, prevenir el fraude y el abuso y —<strong>solo con tu consentimiento, donde este sea obligatorio</strong>— personalizar los anuncios. Sin consentimiento, Google puede seguir mostrando anuncios no personalizados o limitados, que aun así usan algunos datos del dispositivo para la limitación de frecuencia, la medición y la prevención del fraude.</p>
<p><strong>En iPhone</strong>, Koselig te pide una vez permiso para rastrearte (App Tracking Transparency) antes de cargar anuncios. Si lo permites, Google puede usar el identificador publicitario de Apple (IDFA) para personalizar y medir los anuncios. Si lo rechazas, el IDFA no está disponible ni para la aplicación ni para Google, y el juego funciona igual. Puedes cambiarlo cuando quieras en Ajustes de iOS → Privacidad y seguridad → Rastreo.</p>
<p><strong>Redes publicitarias.</strong> Solo usamos Google AdMob y no hemos activado la mediación con otras redes. La versión para Android incluye por ahora adaptadores de software que AdMob puede usar para la mediación con Meta Audience Network y AppLovin; no están activados en nuestra cuenta de AdMob y tenemos previsto eliminarlos. Si algún día activamos otra red, primero actualizaremos esta política.</p>
<p>Más información en los sitios de Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Cómo utiliza Google la información de sitios web o aplicaciones que utilizan sus servicios</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Política de privacidad de Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Política de consentimiento de usuarios de la UE de Google</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Herramientas de consentimiento de Google para aplicaciones (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Mi Centro de Anuncios: gestiona la personalización de anuncios en tu cuenta de Google</a></li>
</ul>

<h2 id="consent">3. Tu consentimiento y cómo cambiarlo</h2>
<p>En las regiones donde se requiere consentimiento, Koselig muestra el formulario de consentimiento de Google (User Messaging Platform) antes de solicitar anuncios. Puedes aceptar, rechazar o elegir finalidades, y cambiar tu elección en cualquier momento dentro del juego: <strong>Ajustes → Anuncios y datos</strong> (esta opción aparece donde se aplican las normas de consentimiento). Eliminar y volver a instalar la aplicación también restablece tu elección.</p>
<p>También puedes limitar los anuncios en tu dispositivo: en Android, en <em>Ajustes → Google → Anuncios</em> (restablecer o eliminar el ID de publicidad); en iPhone, en <em>Ajustes → Privacidad y seguridad → Publicidad de Apple</em>.</p>

<h2 id="firebase">4. Analítica del juego e informes de fallos: Google Firebase</h2>
<p>Koselig usa <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> y <strong>Firebase Remote Config</strong> (Google). Con ellos vemos qué niveles son demasiado difíciles, encontramos y corregimos fallos y ajustamos el juego sin actualizar la aplicación.</p>
<ul>
<li><strong>Analytics</strong> recibe un identificador de instancia de la aplicación generado por Firebase y eventos sobre el uso del juego: nivel empezado, completado o reiniciado, pistas y la comprobación <em>¿Atascado?</em>, ajustes abiertos, idioma cambiado, compra «Sin anuncios» iniciada, completada o fallida. No lo vinculamos con tu nombre, tu correo ni tu identificador publicitario.</li>
<li><strong>Crashlytics</strong>, tras un fallo, recibe un informe: el estado técnico de la aplicación, el seguimiento de la pila, el modelo del dispositivo y la versión del sistema, y un identificador de instalación de Crashlytics.</li>
<li><strong>Remote Config</strong> descarga los ajustes del juego y envía tu país, idioma, zona horaria y versiones de la aplicación y del sistema.</li>
</ul>
<p>Google trata estos datos por encargo nuestro. Los eventos de analítica se conservan como máximo 14 meses y los informes de fallos, 90 días. Consulta <a href="https://firebase.google.com/support/privacy" rel="noopener">Privacidad y seguridad en Firebase</a>.</p>
<h2 id="purchases">5. La compra «Sin anuncios»</h2>
<p>Koselig ofrece una única compra opcional dentro de la aplicación, <strong>«Sin anuncios»</strong> (producto <code>koselig.no_ads</code>). La procesan íntegramente el <strong>Apple App Store</strong> o <strong>Google Play</strong>. No recibimos tu nombre, tu tarjeta ni tus datos de pago. La aplicación solo recibe de la tienda la confirmación de que tienes la compra y guarda ese dato en tu dispositivo. Consulta la <a href="https://www.apple.com/legal/privacy/" rel="noopener">Política de privacidad de Apple</a> y la <a href="https://policies.google.com/privacy" rel="noopener">Política de privacidad de Google</a>.</p>

<h2 id="no">6. Lo que no hacemos</h2>
<ul>
<li>Sin cuentas, sin inicio de sesión, sin funciones sociales.</li>
<li>No te rastreamos en aplicaciones ni sitios web de otras empresas.</li>
<li>Sin acceso a tus contactos, fotos, cámara, micrófono ni ubicación precisa.</li>
<li>No vendemos datos personales ni los usamos para nada más que lo descrito aquí.</li>
</ul>
<p>La aplicación usa el acceso a internet (para los anuncios, la analítica y los informes de fallos, la compra y, en iPhone, el guardado en iCloud) y, en Android, la vibración para la respuesta háptica.</p>

<h2 id="children">7. Niños</h2>
<p>Koselig es un juego de rompecabezas para el público general. No está dirigido a niños menores de 13 años ni forma parte de ninguna categoría infantil. Los anuncios de Koselig no están configurados como dirigidos a niños. No recopilamos a sabiendas información personal de niños. Si crees que un niño nos ha facilitado datos personales, contáctanos y los eliminaremos.</p>

<h2 id="legal">8. Bases jurídicas (RGPD)</h2>
<ul>
<li><strong>Consentimiento</strong> (art. 6.1.a) del RGPD): publicidad personalizada y almacenamiento de información en tu dispositivo o acceso a ella, cuando se requiera consentimiento.</li>
<li><strong>Interés legítimo</strong> (art. 6.1.f) del RGPD): mostrar anuncios no personalizados para financiar un juego gratuito, medir los anuncios y prevenir el fraude.</li>
<li><strong>Interés legítimo</strong> (art. 6.1.f) del RGPD): analítica del juego e informes de fallos para corregir y mejorar el juego.</li>
<li><strong>Contrato</strong> (art. 6.1.b) del RGPD): proporcionar y restaurar la compra «Sin anuncios».</li>
</ul>
<p>Google actúa como responsable del tratamiento independiente respecto de los datos que recopila a través de su SDK. Google y Apple pueden tratar datos fuera del Espacio Económico Europeo con sus propias garantías.</p>

<h2 id="retention">9. Cuánto tiempo se conservan los datos</h2>
<p>Los datos de tu dispositivo permanecen allí hasta que eliminas la aplicación. La copia del progreso en iCloud permanece en tu cuenta de iCloud. Los eventos de analítica se conservan como máximo 14 meses y los informes de fallos, 90 días. Los datos publicitarios recopilados por Google se conservan según las políticas de Google. Si nos escribes, conservamos tu correo electrónico solo el tiempo necesario para responderte y resolver tu solicitud.</p>

<h2 id="rights">10. Tus derechos</h2>
<p>Tienes derecho a acceder a tus datos personales, rectificarlos y suprimirlos, a limitar su tratamiento u oponerte a él, a la portabilidad de los datos y a retirar tu consentimiento en cualquier momento. Como no guardamos datos del juego en nuestros servidores, la mayoría de las solicitudes se resuelven eliminando la aplicación; las solicitudes sobre datos publicitarios pueden dirigirse a Google a través de los enlaces anteriores. Siempre puedes escribirnos a <a href="mailto:{EMAIL}">{EMAIL}</a>. También tienes derecho a presentar una reclamación ante una autoridad de control —en Polonia, el <a href="https://uodo.gov.pl/" rel="noopener">Presidente de la Oficina de Protección de Datos Personales (UODO)</a>— o ante la autoridad de tu país.</p>

<h2 id="website">11. Este sitio web</h2>
<p>coffeebeansstudio.eu es un sitio web estático. No usa <strong>cookies, analítica ni fuentes o scripts de terceros</strong>. Está alojado en <strong>GitHub Pages</strong> (GitHub, Inc.), y el servicio de nombres de dominio lo presta <strong>Cloudflare</strong>. Estos proveedores pueden tratar tu dirección IP y datos técnicos de las solicitudes en los registros de sus servidores, por motivos de seguridad y para servir el sitio. Consulta la <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Declaración de privacidad de GitHub</a> y la <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Política de privacidad de Cloudflare</a>.</p>

<h2 id="changes">12. Cambios</h2>
<p>Si la aplicación empieza a hacer algo nuevo con los datos —por ejemplo, una nueva red publicitaria o analítica—, actualizaremos esta página antes de que el cambio llegue a la aplicación y cambiaremos la fecha que figura abajo.</p>
""",
    # terms
    t_title="Condiciones de uso — Coffee Beans Studio",
    t_desc="Condiciones breves y honestas para Koselig y otros juegos de Coffee Beans Studio.",
    t_h1="Condiciones de uso",
    t_sub="Koselig y otros juegos de Coffee Beans Studio",
    terms_html="""
<p class="note">La versión jurídicamente vinculante es la <a href="{R}terms/">inglesa</a>. Esta traducción se ofrece para tu comodidad.</p>
<p>Estas condiciones se aplican cuando usas <strong>Koselig</strong> u otro juego de <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Polonia). Al jugar, las aceptas. Son breves a propósito.</p>

<h2>1. Jugar</h2>
<p>Te concedemos un derecho personal, no exclusivo e intransferible a instalar nuestros juegos y jugar a ellos en dispositivos de tu propiedad o bajo tu control, para tu propio uso no comercial. Te pedimos que no copies, revendas, apliques ingeniería inversa ni redistribuyas el juego o sus gráficos, salvo en la medida en que la ley lo permita.</p>

<h2>2. Las tiendas</h2>
<p>Descargas nuestros juegos del Apple App Store o de Google Play, y sus condiciones también se aplican. A las aplicaciones descargadas del App Store se les aplica, además de estas condiciones, el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Contrato de licencia de usuario final estándar</a> de Apple. Apple y Google no son responsables del juego ni de su soporte.</p>

<h2>3. Anuncios y la compra «Sin anuncios»</h2>
<p>Koselig es gratuito. Cuando pides una comprobación <em>¿Atascado?</em>, puede mostrar un video corto con recompensa. Los anuncios los proporciona Google AdMob; no controlamos su contenido ni somos responsables de los productos de terceros que se anuncian en ellos.</p>
<p>«Sin anuncios» es una compra no consumible de pago único. Hace que la comprobación <em>¿Atascado?</em> funcione sin videos; el número de comprobaciones por nivel no cambia. La tienda muestra el precio antes del pago. Los pagos, reembolsos y cancelaciones los gestionan Apple o Google según sus políticas. La compra está vinculada a tu ID de Apple o a tu cuenta de Google y puede restaurarse después de reinstalar el juego (Ajustes → <em>Restaurar</em>).</p>

<h2>4. Tu progreso</h2>
<p>El progreso se guarda en tu dispositivo y, en iPhone, también en tu propia cuenta de iCloud. Si eliminas la aplicación o pierdes el dispositivo, no podremos recuperarlo; en iPhone puede volver desde iCloud.</p>

<h2>5. Cambios y disponibilidad</h2>
<p>Podemos actualizar el juego —añadir, cambiar o quitar niveles y funciones— y podemos dejar de ofrecerlo. Haremos lo posible por que siga funcionando, pero no podemos prometer que esté siempre disponible ni libre de errores.</p>

<h2>6. Responsabilidad</h2>
<p>El juego se ofrece «tal cual». En la medida en que la ley lo permita, no somos responsables de daños indirectos ni de la pérdida de datos. Nada de lo dispuesto en estas condiciones limita la responsabilidad que la ley no permite limitar, ni tus derechos como consumidor conforme a las leyes de tu país.</p>

<h2>7. Legislación aplicable</h2>
<p>Estas condiciones se rigen por la legislación de Polonia. Si eres consumidor, conservas además la protección de las normas imperativas del país donde vives.</p>

<h2>8. Contacto</h2>
<p>Preguntas o reclamaciones: <a href="mailto:{EMAIL}">{EMAIL}</a>. Cómo tratamos los datos se explica en la <a href="{R}es/privacy/">Política de privacidad</a>.</p>
""",
    # support
    s_title="Soporte — Coffee Beans Studio",
    s_desc="Ayuda con Koselig: restaurar la compra «Sin anuncios», empezar de nuevo un nivel, cambiar el idioma o el consentimiento para los anuncios, y eliminar tus datos.",
    s_h1="Soporte",
    s_sub="Leemos todos los mensajes",
    s_mail_h="Escríbenos",
    s_mail_p="Cuéntanos el modelo de tu teléfono, la versión del juego y qué ocurrió. Una captura de pantalla ayuda mucho.",
    s_faq_h="Preguntas",
    faq=[
        ("¿Cómo restauro la compra «Sin anuncios»?",
         "Toca ☰ en la esquina superior derecha para abrir los Ajustes y luego toca <em>Restaurar</em> junto a <em>Sin anuncios</em>. Usa el mismo ID de Apple o la misma cuenta de Google con los que la compraste. Cada vez que se inicia, el juego comprueba la compra con la tienda, así que tras una reinstalación también vuelve sola en cuanto la tienda responde."),
        ("¿Cómo vuelvo a empezar un nivel?",
         "Abre Ajustes y toca <em>Empezar de nuevo</em>; luego vuelve a tocar para confirmar. Así se reinicia el nivel actual. Para borrarlo todo —todo el progreso y los ajustes—, elimina la aplicación."),
        ("¿Cómo cambio el idioma?",
         "Ajustes → <em>Idioma</em>. Koselig está disponible en español, English, Deutsch, Français, Italiano, Polski y Русский. <em>Del sistema</em> sigue el idioma de tu teléfono."),
        ("¿Cuándo muestra anuncios el juego?",
         "Solo cuando tocas <em>¿Atascado?</em> y eliges <em>Ver video</em>. No hay banners ni anuncios emergentes. Con <em>Sin anuncios</em>, la comprobación funciona al instante."),
        ("¿Cómo cambio mi consentimiento para los anuncios?",
         "En Ajustes, toca <em>Cambiar</em> junto a <em>Anuncios y datos</em>: se vuelve a abrir el formulario de consentimiento de Google. Esta opción aparece en las regiones donde se aplican las normas de consentimiento."),
        ("¿Puedo guardar una posición y volver a ella?",
         "Sí. En Ajustes → <em>Partidas</em> hay tres espacios: <em>Guardar</em> almacena la posición actual y <em>Cargar</em> la recupera."),
    ],
    s_del_h="Eliminar tus datos",
    s_del_p="Koselig no tiene cuentas. El progreso se guarda en tu dispositivo y, en iPhone, también en tu iCloud. Al eliminar la aplicación se borra todo lo que guardó en el dispositivo. Sobre los datos publicitarios, la analítica y iCloud, consulta la <a href=\"{R}es/koselig/delete-data/\">página sobre la eliminación de datos</a>.",
    # delete data
    d_title="Eliminar tus datos — Koselig",
    d_desc="Cómo eliminar los datos del juego Koselig: elimina la aplicación; la copia en iCloud la gestiona Apple y los datos publicitarios, Google.",
    d_h1="Eliminar tus datos",
    d_sub="Koselig, de Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> no tiene cuentas, así que no hay ninguna cuenta que eliminar. No guardamos tu progreso en nuestros servidores.</p>

<h2>Datos en tu dispositivo</h2>
<p>El progreso, las partidas guardadas, los ajustes, el estado de la compra «Sin anuncios» y tu elección sobre el consentimiento publicitario se guardan en tu teléfono. <strong>Para borrarlo todo, elimina la aplicación</strong>:</p>
<ul>
<li><strong>iPhone:</strong> mantén el dedo sobre el icono de Koselig → <em>Eliminar app</em> → <em>Eliminar app</em>.</li>
<li><strong>Android:</strong> mantén el dedo sobre el icono de Koselig → <em>Información de la app</em> → <em>Desinstalar</em> (o <em>Almacenamiento → Borrar almacenamiento</em> para conservar la aplicación y borrar sus datos).</li>
</ul>
<p>Eliminar la aplicación no cancela ni elimina la compra «Sin anuncios»: está vinculada a tu ID de Apple o a tu cuenta de Google y puedes restaurarla más adelante.</p>

<h2>Copia en iCloud (iPhone)</h2>
<p>En iPhone, el progreso y las partidas guardadas también se copian a tu propia cuenta de iCloud. La guarda Apple con tu Apple ID. Para detenerlo, desactiva iCloud para Koselig en <em>Ajustes → [tu nombre] → iCloud</em>.</p>
<h2>Analítica e informes de fallos</h2>
<p>Los eventos de analítica y los informes de fallos (Google Firebase) no están vinculados a tu nombre ni a tu correo, así que no podemos encontrar los registros de una persona. Se borran solos: los eventos de analítica en un máximo de 14 meses y los informes de fallos a los 90 días.</p>
<h2>Datos publicitarios</h2>
<p>Los anuncios de Koselig los proporciona Google AdMob. Los datos que recopila Google están bajo el control de Google. Puedes:</p>
<ul>
<li>restablecer o eliminar el ID de publicidad de Android: <em>Ajustes → Google → Anuncios</em>;</li>
<li>cambiar tu consentimiento en el juego: <em>Ajustes → Anuncios y datos</em>;</li>
<li>gestionar o eliminar los datos de tu cuenta de Google: <a href="https://myadcenter.google.com/" rel="noopener">Mi Centro de Anuncios</a> y <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Datos y privacidad de Google</a>;</li>
<li>leer cómo usa Google los datos de las aplicaciones: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>

<h2>Correos que nos enviaste</h2>
<p>Si nos escribiste y quieres que borremos tus mensajes, envía una solicitud a <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> desde la misma dirección. Los borraremos en un plazo de 30 días y te lo confirmaremos.</p>
<p>Más información: <a href="{R}es/koselig/privacy/">Política de privacidad</a>.</p>
""",
    nf_title="Página no encontrada — Coffee Beans Studio",
    nf_h1="Esta página se apagó como una vela",
    nf_p="Puede que la dirección esté mal escrita o que la página se haya movido.",
    nf_cta="Volver al estudio",
)

# ─────────────────────────────── DEUTSCH ───────────────────────────────
# Термины игры — колонка «de» ~/lotok/tools/teksty_gen.py; правовые тексты — смысл английских без изменений.
L["de"] = dict(
    name="Deutsch", short="DE", date="17. November 2026",
    nav_koselig="Koselig", nav_support="Hilfe", skip="Zum Inhalt springen", lang_label="Sprache",
    foot_legal="Datenschutz", foot_terms="Nutzungsbedingungen", foot_support="Hilfe", foot_delete="Daten löschen",
    soon_stores="Bald im App Store und bei Google Play",
    home_title="Coffee Beans Studio – gemütliche, kluge Spiele",
    home_desc="Coffee Beans Studio ist ein kleines unabhängiges Studio für gemütliche, kluge Spiele. Unser erstes Spiel, Koselig, ist ein Legespiel im Holzrahmen für iPhone und Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Ruhige Spiele<br>für warme Abende",
    hero_p="Wir machen gemütliche, kluge Spiele – solche, die man in aller Ruhe spielt, bei einer Tasse Tee und Kerzenschein.",
    hero_cta="Koselig kennenlernen",
    ch1_h="In Ruhe aufgebrüht",
    ch1_p="Coffee Beans Studio ist ein kleines unabhängiges Studio. Uns liegen ruhige Rätsel, warme Materialien und ehrliches Design am Herzen: Dinge, die man mit den Augen berühren kann – Holz, Leinen, Kerzenschein – und Regeln, die man in einer Minute versteht.",
    ch2_h="Koselig",
    ch2_sub="Ein Legespiel im Holzrahmen",
    ch2_p="Lege jedes Teil in den Holzrahmen. Tisch, Rahmen und Teile wählst du nach Lust und Laune: Eiche oder Leinen, Nuss oder Messing, Lack oder Stein. Und wenn du nicht weiterkommst, verrät dir ein kleiner Bonsai, ob es von hier aus noch eine Lösung gibt.",
    ch2_cta="Mehr zum Spiel",
    word_q="koselig",
    word_def="<em>Norwegisch</em> – gemütlich, warm, angenehm vertraut. Das Gefühl von Kerzenlicht, einer Wolldecke und guter Gesellschaft.",
    soon_h="Fast eingepackt",
    soon_p="Koselig wird gerade für den App Store und Google Play vorbereitet. Am Tag der Veröffentlichung findest du hier die Links.",
    end_h="Schreib uns",
    end_p="Fragen, Ideen oder ein Fehler in einem Rätsel? Wir lesen jede Nachricht.",
    # Koselig
    k_title="Koselig – ein gemütliches Legespiel im Holzrahmen für iPhone und Android",
    k_desc="Koselig ist ein ruhiges Legespiel im Holzrahmen: Lege jedes Teil in den Rahmen, wähle Tisch, Rahmen und Teile – und ist das Level gelöst, blüht ein kleiner Bonsai auf. Bald im App Store und bei Google Play.",
    k_eyebrow="Ein Spiel von Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Ein gemütliches Legespiel im Holzrahmen. Lege jedes Teil in den Rahmen – und lass dir Zeit.",
    k_about_h="Rätseln ohne Eile",
    k_about_p=[
        "Koselig ist ein digitales Legespiel im Holzrahmen. Die Teile liegen auf dem Tisch rund um den Rahmen: Du nimmst sie, drehst sie und legst sie ein, bis jedes Feld belegt ist.",
        "Die Level führen dich über eine Karte – von kleinen Rahmen bis zum großen. Jeder Rahmen lässt sich auf mehr als eine Art füllen, und es gibt eine perfekte Lösung, bei der sich keine zwei gleichfarbigen Teile berühren.",
        "Du bist nicht sicher, ob es noch eine Lösung gibt? Tippe auf <em>Verrannt?</em>, und der Bonsai prüft es für dich – nach einem kurzen Video, das du dir freiwillig ansiehst, oder sofort, wenn du <em>Werbefrei</em> gekauft hast.",
    ],
    k_feat_h="Was drinsteckt",
    k_feats=[
        ("Drei Tische", "Eiche, Leinen und Nuss – auf jedem regt sich leise etwas: eine Kerze, Dampf über dem Tee, Lavendel im Wind."),
        ("Rahmen und Teile", "Rahmen aus Kiefer, Nuss, Stein, Stahl, Messing, Olive und Kirsche. Teile in Lack, Holz, Stein, Metall und Terrazzo."),
        ("Eine Levelkarte", "Sanfte erste Schritte in kleineren Rahmen, dann das ganze Rätsel."),
        ("Der Bonsai", "Dein Helfer bei <em>Verrannt?</em> – und er blüht auf, wenn du ein Level löst."),
        ("Spielstände", "Drei Speicherplätze für Zwischenstände, zu denen du zurückkehren möchtest."),
        ("Sieben Sprachen", "Deutsch, English, Español, Français, Italiano, Polski und Русский."),
    ],
    k_ads_h="Fair in Sachen Werbung",
    k_ads_p="Keine Banner, keine Pop-ups. Ein kurzes Video läuft nur, wenn du über <em>Verrannt?</em> prüfen lassen möchtest und dich für das Video entscheidest. Dazu gibt es einen optionalen Kauf: Mit <em>Werbefrei</em> funktioniert die Prüfung ohne Videos.",
    k_shots_h="Screenshots",
    k_shot_alts=[
        "Ein kleiner Rahmen auf dem Leinentisch, ringsum ein paar Teile",
        "Der Nusstisch mit dem Holzrahmen, Teile darüber und darunter",
        "Das Fenster „Verrannt?“ mit einem Bonsai im Topf",
        "Der Bildschirm „Geschafft!“ mit dem Bonsai und der Levelzeit",
        "Die Levelkarte: ein Weg durch herbstliche Hügel zu einem Haus auf einer Anhöhe",
        "Einstellungen: Teile, Rahmen, Tisch, Spielstände, Ton, Sprache und „Werbefrei“",
    ],
    k_platforms="iPhone und Android · Deutsch, English, Español, Français, Italiano, Polski, Русский",
    k_links_h="Gut zu wissen",
    # legal common
    legal_updated="Stand",
    # privacy
    p_title="Datenschutzerklärung – Koselig",
    p_desc="Wie das Spiel Koselig und coffeebeansstudio.eu mit deinen Daten umgehen: keine Konten, Fortschritt auf deinem Gerät, Google AdMob für freiwillige Belohnungsvideos, Käufe über Apple und Google.",
    p_h1="Datenschutzerklärung",
    p_sub="Koselig und coffeebeansstudio.eu",
    privacy_html="""
<p class="note">Rechtlich verbindlich ist die <a href="{R}koselig/privacy/">englische Fassung</a>. Dies ist eine genaue Übersetzung zur leichteren Orientierung.</p>
<p>Diese Erklärung beschreibt, was mit deinen Daten passiert, wenn du <strong>Koselig</strong> auf dem iPhone oder unter Android spielst und wenn du <strong>coffeebeansstudio.eu</strong> besuchst. Wir haben sie so geschrieben, dass sie dem entspricht, was die App tatsächlich tut.</p>

<h2 id="who">Wer wir sind</h2>
<p>Koselig wird von <strong>Coffee Beans Studio</strong> veröffentlicht. Verantwortlicher für deine personenbezogenen Daten im Sinne der DSGVO ist <strong>Dzmitry Kurtsikau</strong>, eine in Polen ansässige Privatperson („wir“, „uns“). Wenn du Fragen zum Datenschutz hast, schreib an <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">Das Wichtigste in Kürze</h2>
<ul>
<li>Es gibt <strong>keine Konten</strong> und keine Anmeldung. Wir fragen nie nach deinem Namen, deiner E-Mail-Adresse oder deiner Telefonnummer.</li>
<li>Dein Fortschritt und deine Einstellungen werden <strong>auf deinem Gerät gespeichert</strong>; auf dem iPhone zusätzlich in deinem eigenen iCloud. Wir erhalten sie nicht.</li>
<li>Das Spiel zeigt Werbung <strong>nur, wenn du dich dafür entscheidest</strong>, für die Prüfung mit <em>Verrannt?</em> ein kurzes Belohnungsvideo anzusehen. Es gibt keine Banner und keine Interstitial-Anzeigen. Die Werbung stammt von <strong>Google AdMob</strong>; Google verarbeitet dabei Gerätedaten und Kennungen.</li>
<li>Wo das Gesetz es verlangt (zum Beispiel im EWR, im Vereinigten Königreich und in der Schweiz), wirst du über das Einwilligungsformular von Google um deine <strong>Einwilligung</strong> gebeten, bevor personalisierte Werbung angezeigt wird.</li>
<li>Den optionalen Kauf <strong>„Werbefrei“</strong> wickeln Apple oder Google ab. Deine Zahlungsdaten sehen wir nie.</li>
<li>Koselig nutzt <strong>Google Firebase</strong> für Spielanalysen und Absturzberichte. Sie enthalten weder deinen Namen noch deine E-Mail oder Kontakte. Wir verkaufen keine personenbezogenen Daten.</li>
</ul>

<h2 id="device">1. Daten auf deinem Gerät</h2>
<p>Damit du dort weitermachen kannst, wo du aufgehört hast, speichert Koselig auf deinem Smartphone:</p>
<ul>
<li>Spielfortschritt: freigeschaltete Level, die aktuelle Position der Teile und deine drei Speicherplätze;</li>
<li>Einstellungen: Ton, Sprache sowie die Wahl von Tisch, Rahmen und Teilen;</li>
<li>ob du den Kauf „Werbefrei“ besitzt;</li>
<li>deine Entscheidung zur Werbeeinwilligung, die das Einwilligungs-SDK von Google auf dem Gerät speichert.</li>
</ul>
<p>Diese Daten bleiben auf deinem Gerät und werden nicht an uns gesendet. Sie werden gelöscht, wenn du die App löschst. <strong>Auf dem iPhone</strong> werden Fortschritt und Spielstände zusätzlich in <strong>dein eigenes iCloud</strong> kopiert (iCloud-Schlüssel-Wert-Speicher), damit du auf einem anderen Gerät oder nach einer Neuinstallation weiterspielen kannst. Diese Kopie speichert Apple unter deiner Apple-ID; wir können sie nicht lesen. Du kannst das in den iOS-Einstellungen → [dein Name] → iCloud ausschalten. Unter Android nutzt das Spiel keine Cloud-Spielstände, nach einer Neuinstallation beginnt der Fortschritt also von vorn. Der Kauf „Werbefrei“ lässt sich jederzeit über Apple oder Google wiederherstellen (Einstellungen → <em>Wiederherstellen</em>).</p>

<h2 id="ads">2. Werbung: Google AdMob</h2>
<p>Koselig nutzt das <strong>Google Mobile Ads SDK</strong> (Google AdMob), um Belohnungsvideos anzuzeigen. Damit ein Video bereitsteht, wenn du eines anforderst, startet die App das SDK gleich beim Öffnen und lädt im Hintergrund ein Video vor. Google kann daher Daten von deinem Gerät erhalten, <strong>auch wenn du nie ein Video ansiehst</strong>.</p>
<p>Zu den Daten, die Google über das SDK erheben und verarbeiten kann, gehören:</p>
<ul>
<li>Gerätekennungen: unter Android die <strong>Werbe-ID</strong>; auf dem iPhone die Anbieter-Kennung (IDFV) und weitere Gerätesignale;</li>
<li>deine <strong>IP-Adresse</strong>, aus der sich ein ungefährer Standort (Land oder Stadt) ableiten lässt;</li>
<li>Geräte- und App-Informationen: Modell, Betriebssystem und Version, Sprache, Bildschirmgröße, App-Version;</li>
<li>Interaktionen mit Anzeigen: welche Anzeigen geladen, angezeigt, bis zum Ende angesehen oder angetippt wurden.</li>
</ul>
<p>Google nutzt diese Daten, um Werbung auszuliefern und zu messen, um Betrug und Missbrauch zu verhindern und – <strong>nur mit deiner Einwilligung, wo diese erforderlich ist</strong> – um Werbung zu personalisieren. Ohne Einwilligung kann Google weiterhin nicht personalisierte oder eingeschränkte Anzeigen ausliefern; auch diese nutzen einige Gerätedaten, um die Häufigkeit zu begrenzen, Anzeigen zu messen und Betrug vorzubeugen.</p>
<p><strong>Auf dem iPhone</strong> bittet Koselig einmal um die Erlaubnis zum Tracking (App Tracking Transparency), bevor Werbung geladen wird. Erlaubst du es, kann Google die Werbekennung von Apple (IDFA) nutzen, um Werbung zu personalisieren und zu messen. Lehnst du ab, steht die IDFA weder der App noch Google zur Verfügung, und das Spiel funktioniert genauso. Du kannst das jederzeit ändern: iOS-Einstellungen → Datenschutz &amp; Sicherheit → Tracking.</p>
<p><strong>Werbenetzwerke.</strong> Wir nutzen nur Google AdMob und haben keine Mediation mit anderen Netzwerken aktiviert. Die Android-Version enthält derzeit Software-Adapter, die AdMob für eine Mediation mit Meta Audience Network und AppLovin nutzen kann; in unserem AdMob-Konto sind sie nicht aktiviert, und wir planen, sie zu entfernen. Sollten wir jemals ein weiteres Netzwerk aktivieren, aktualisieren wir zuerst diese Erklärung.</p>
<p>Mehr dazu bei Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Wie Google Daten von Websites und Apps verwendet, die Google-Dienste nutzen</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Datenschutzerklärung von Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Google-Richtlinie zur Einwilligung der Nutzer in der EU</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Einwilligungstools von Google für Apps (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Mein Werbecenter – Personalisierung von Werbung in deinem Google-Konto verwalten</a></li>
</ul>

<h2 id="consent">3. Deine Einwilligung und wie du sie änderst</h2>
<p>In Regionen, in denen eine Einwilligung erforderlich ist, zeigt Koselig das Einwilligungsformular von Google (User Messaging Platform), bevor Anzeigen angefordert werden. Du kannst zustimmen, ablehnen oder Zwecke auswählen. Deine Entscheidung kannst du im Spiel jederzeit ändern: <strong>Einstellungen → Werbung &amp; Daten</strong> (dieser Punkt erscheint dort, wo die Einwilligungsregeln gelten). Löschst du die App und installierst sie neu, wird deine Entscheidung ebenfalls zurückgesetzt.</p>
<p>Du kannst Werbung auch auf deinem Gerät einschränken: unter Android in <em>Einstellungen → Google → Anzeigen</em> (Werbe-ID zurücksetzen oder löschen); auf dem iPhone in <em>Einstellungen → Datenschutz &amp; Sicherheit → Apple-Werbung</em>.</p>

<h2 id="firebase">4. Spielanalyse und Absturzberichte: Google Firebase</h2>
<p>Koselig nutzt <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> und <strong>Firebase Remote Config</strong> (Google). Damit sehen wir, welche Level zu schwer sind, finden und beheben Abstürze und passen Spieleinstellungen ohne App-Update an.</p>
<ul>
<li><strong>Analytics</strong> erhält eine von Firebase erzeugte App-Instanz-ID und Ereignisse zur Nutzung des Spiels: Level gestartet, geschafft oder zurückgesetzt, Hinweise und die Prüfung <em>Verrannt?</em>, Einstellungen geöffnet, Sprache gewechselt, Kauf „Werbefrei“ gestartet, abgeschlossen oder fehlgeschlagen. Wir verknüpfen das nicht mit deinem Namen, deiner E-Mail oder deiner Werbekennung.</li>
<li><strong>Crashlytics</strong> erhält nach einem Absturz einen Bericht: den technischen Zustand der App, den Stacktrace, Gerätemodell und Systemversion sowie eine Crashlytics-Installations-ID.</li>
<li><strong>Remote Config</strong> lädt Spieleinstellungen herunter und übermittelt Land, Sprache, Zeitzone, App- und Systemversion.</li>
</ul>
<p>Google verarbeitet diese Daten in unserem Auftrag. Analyse-Ereignisse werden höchstens 14 Monate aufbewahrt, Absturzberichte 90 Tage. Siehe <a href="https://firebase.google.com/support/privacy" rel="noopener">Datenschutz und Sicherheit in Firebase</a>.</p>
<h2 id="purchases">5. Der Kauf „Werbefrei“</h2>
<p>Koselig bietet einen optionalen In-App-Kauf an: <strong>„Werbefrei“</strong> (Produkt <code>koselig.no_ads</code>). Er wird vollständig über den <strong>Apple App Store</strong> oder <strong>Google Play</strong> abgewickelt. Wir erhalten weder deinen Namen noch deine Karten- oder Zahlungsdaten. Die App erhält vom Store nur die Bestätigung, dass du den Kauf besitzt, und speichert diese Information auf deinem Gerät. Siehe die <a href="https://www.apple.com/legal/privacy/" rel="noopener">Datenschutzrichtlinie von Apple</a> und die <a href="https://policies.google.com/privacy" rel="noopener">Datenschutzerklärung von Google</a>.</p>

<h2 id="no">6. Was wir nicht tun</h2>
<ul>
<li>Keine Konten, keine Anmeldung, keine sozialen Funktionen.</li>
<li>Kein Tracking durch uns über Apps oder Websites anderer Unternehmen hinweg.</li>
<li>Kein Zugriff auf Kontakte, Fotos, Kamera, Mikrofon oder deinen genauen Standort.</li>
<li>Wir verkaufen keine personenbezogenen Daten und verwenden sie für nichts anderes als das hier Beschriebene.</li>
</ul>
<p>Die App nutzt den Internetzugang (für Werbung, Analyse und Absturzberichte, den Kauf und auf dem iPhone für iCloud-Spielstände) und unter Android die Vibration für haptisches Feedback.</p>

<h2 id="children">7. Kinder</h2>
<p>Koselig ist ein Rätselspiel für ein allgemeines Publikum. Es richtet sich nicht an Kinder unter 13 Jahren und gehört keiner Kinderkategorie an. Die Werbung in Koselig ist nicht als kindgerichtet konfiguriert. Wir erheben nicht wissentlich personenbezogene Daten von Kindern. Wenn du glaubst, dass ein Kind uns personenbezogene Daten übermittelt hat, melde dich bei uns – wir löschen sie dann.</p>

<h2 id="legal">8. Rechtsgrundlagen (DSGVO)</h2>
<ul>
<li><strong>Einwilligung</strong> (Art. 6 Abs. 1 lit. a DSGVO) – personalisierte Werbung sowie das Speichern von Informationen auf deinem Gerät oder der Zugriff darauf, wo eine Einwilligung erforderlich ist.</li>
<li><strong>Berechtigte Interessen</strong> (Art. 6 Abs. 1 lit. f) – das Ausspielen nicht personalisierter Werbung zur Finanzierung eines kostenlosen Spiels, Anzeigenmessung und Betrugsprävention.</li>
<li><strong>Berechtigte Interessen</strong> (Art. 6 Abs. 1 lit. f) – Spielanalyse und Absturzberichte, um das Spiel zu reparieren und zu verbessern.</li>
<li><strong>Vertrag</strong> (Art. 6 Abs. 1 lit. b) – Bereitstellung und Wiederherstellung des Kaufs „Werbefrei“.</li>
</ul>
<p>Für die Daten, die Google über sein SDK erhebt, ist Google eigenständiger Verantwortlicher. Google und Apple können Daten außerhalb des Europäischen Wirtschaftsraums verarbeiten und stützen sich dabei auf eigene Garantien.</p>

<h2 id="retention">9. Speicherdauer</h2>
<p>Daten auf deinem Gerät bleiben dort, bis du die App löschst. Die iCloud-Kopie deines Fortschritts bleibt in deinem iCloud. Analyse-Ereignisse werden höchstens 14 Monate aufbewahrt, Absturzberichte 90 Tage. Von Google für Werbung erhobene Daten werden nach den Richtlinien von Google aufbewahrt. Wenn du uns schreibst, bewahren wir deine E-Mail nur so lange auf, wie es nötig ist, um dir zu antworten und dein Anliegen zu klären.</p>

<h2 id="rights">10. Deine Rechte</h2>
<p>Du hast das Recht auf Auskunft über deine personenbezogenen Daten, auf ihre Berichtigung und Löschung, auf Einschränkung der Verarbeitung und Widerspruch gegen sie, auf Datenübertragbarkeit sowie das Recht, deine Einwilligung jederzeit zu widerrufen. Da wir keine Spieldaten auf unseren Servern speichern, lassen sich die meisten Anfragen durch das Löschen der App erledigen; Anfragen zu Werbedaten kannst du über die oben genannten Links an Google richten. Du kannst uns jederzeit unter <a href="mailto:{EMAIL}">{EMAIL}</a> schreiben. Außerdem hast du das Recht, dich bei einer Aufsichtsbehörde zu beschweren – in Polen beim <a href="https://uodo.gov.pl/" rel="noopener">Präsidenten des Amtes für den Schutz personenbezogener Daten (UODO)</a> – oder bei der Behörde in deinem Land.</p>

<h2 id="website">11. Diese Website</h2>
<p>coffeebeansstudio.eu ist eine statische Website. Sie verwendet <strong>keine Cookies, keine Analysedienste und keine Schriften oder Skripte von Dritten</strong>. Sie wird bei <strong>GitHub Pages</strong> (GitHub, Inc.) gehostet, den DNS-Dienst der Domain stellt <strong>Cloudflare</strong> bereit. Diese Anbieter können deine IP-Adresse und technische Daten deiner Anfragen zu Sicherheits- und Auslieferungszwecken in Serverprotokollen verarbeiten. Siehe die <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Datenschutzerklärung von GitHub</a> und die <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Datenschutzrichtlinie von Cloudflare</a>.</p>

<h2 id="changes">12. Änderungen</h2>
<p>Sollte die App künftig etwas Neues mit Daten tun – etwa ein neues Werbenetzwerk oder Analysedienste nutzen –, aktualisieren wir diese Seite, bevor die Änderung in der App ankommt, und ändern das Datum unten.</p>
""",
    # terms
    t_title="Nutzungsbedingungen – Coffee Beans Studio",
    t_desc="Kurze, ehrliche Nutzungsbedingungen für Koselig und andere Spiele von Coffee Beans Studio.",
    t_h1="Nutzungsbedingungen",
    t_sub="Koselig und andere Spiele von Coffee Beans Studio",
    terms_html="""
<p class="note">Rechtlich verbindlich ist die <a href="{R}terms/">englische Fassung</a>. Diese Übersetzung ist zur leichteren Orientierung gedacht.</p>
<p>Diese Bedingungen gelten, wenn du <strong>Koselig</strong> oder ein anderes Spiel von <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Polen) nutzt. Indem du spielst, stimmst du ihnen zu. Sie sind bewusst kurz gehalten.</p>

<h2>1. Das Spiel nutzen</h2>
<p>Wir räumen dir ein persönliches, nicht ausschließliches und nicht übertragbares Recht ein, unsere Spiele auf Geräten zu installieren und zu spielen, die dir gehören oder über die du verfügst – für deine eigene, nicht kommerzielle Nutzung. Bitte kopiere das Spiel und seine Grafiken nicht, verkaufe oder verbreite sie nicht weiter und betreibe kein Reverse Engineering – es sei denn, das Gesetz erlaubt es.</p>

<h2>2. Die Stores</h2>
<p>Du lädst unsere Spiele aus dem Apple App Store oder von Google Play herunter; deren Bedingungen gelten ebenfalls. Für Apps aus dem App Store gilt zusätzlich zu diesen Bedingungen Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Standard-Endbenutzer-Lizenzvertrag</a>. Apple und Google sind weder für das Spiel noch für den Support verantwortlich.</p>

<h2>3. Werbung und der Kauf „Werbefrei“</h2>
<p>Koselig ist kostenlos. Das Spiel kann ein kurzes Belohnungsvideo zeigen, wenn du über <em>Verrannt?</em> eine Prüfung anforderst. Die Werbung stellt Google AdMob bereit; wir haben keinen Einfluss auf ihren Inhalt und sind nicht für Produkte Dritter verantwortlich, die darin beworben werden.</p>
<p>„Werbefrei“ ist ein einmaliger Kauf, der sich nicht verbraucht. Damit funktioniert die Prüfung mit <em>Verrannt?</em> ohne Videos; die Zahl der Prüfungen pro Level bleibt gleich. Den Preis zeigt dir der Store, bevor du bezahlst. Zahlung, Erstattungen und Stornierungen wickeln Apple oder Google nach ihren eigenen Richtlinien ab. Der Kauf ist an deine Apple-ID oder dein Google-Konto gebunden und lässt sich nach einer Neuinstallation wiederherstellen (Einstellungen → <em>Wiederherstellen</em>).</p>

<h2>4. Dein Fortschritt</h2>
<p>Der Fortschritt wird auf deinem Gerät gespeichert und auf dem iPhone zusätzlich in deinem eigenen iCloud. Wenn du die App löschst oder das Gerät verlierst, können wir ihn nicht wiederherstellen; auf dem iPhone kann er aus iCloud zurückkommen.</p>

<h2>5. Änderungen und Verfügbarkeit</h2>
<p>Wir können das Spiel aktualisieren – Level und Funktionen hinzufügen, ändern oder entfernen – und das Angebot auch einstellen. Wir bemühen uns, es am Laufen zu halten, können aber nicht versprechen, dass es immer verfügbar oder fehlerfrei ist.</p>

<h2>6. Haftung</h2>
<p>Das Spiel wird „wie besehen“ bereitgestellt. Soweit gesetzlich zulässig, haften wir nicht für mittelbare Schäden oder Datenverlust. Nichts in diesen Bedingungen beschränkt eine Haftung, die gesetzlich nicht beschränkt werden kann, oder deine Rechte als Verbraucher nach dem Recht deines Landes.</p>

<h2>7. Anwendbares Recht</h2>
<p>Für diese Bedingungen gilt polnisches Recht. Wenn du Verbraucher bist, behältst du außerdem den Schutz der zwingenden Vorschriften des Landes, in dem du lebst.</p>

<h2>8. Kontakt</h2>
<p>Fragen oder Beschwerden: <a href="mailto:{EMAIL}">{EMAIL}</a>. Wie wir mit Daten umgehen, steht in der <a href="{R}de/privacy/">Datenschutzerklärung</a>.</p>
""",
    # support
    s_title="Hilfe – Coffee Beans Studio",
    s_desc="Hilfe zu Koselig: den Kauf „Werbefrei“ wiederherstellen, ein Level neu beginnen, die Sprache wechseln, die Werbeeinwilligung ändern und deine Daten löschen.",
    s_h1="Hilfe",
    s_sub="Wir lesen jede Nachricht",
    s_mail_h="Schreib uns",
    s_mail_p="Nenn uns dein Handymodell, die Spielversion und was passiert ist. Ein Screenshot hilft sehr.",
    s_faq_h="Fragen",
    faq=[
        ("Wie stelle ich den Kauf „Werbefrei“ wieder her?",
         "Tippe oben rechts auf ☰, um die Einstellungen zu öffnen, und dann neben <em>Werbefrei</em> auf <em>Wiederherstellen</em>. Verwende dieselbe Apple-ID bzw. dasselbe Google-Konto wie beim Kauf. Das Spiel gleicht den Kauf bei jedem Start mit dem Store ab – nach einer Neuinstallation kommt er also auch von selbst zurück, sobald der Store antwortet."),
        ("Wie beginne ich ein Level neu?",
         "Öffne die Einstellungen, tippe auf <em>Neu beginnen</em> und zur Bestätigung noch einmal. Dadurch wird das aktuelle Level zurückgesetzt. Um alles zu löschen – den gesamten Fortschritt und alle Einstellungen –, lösche die App."),
        ("Wie ändere ich die Sprache?",
         "Einstellungen → <em>Sprache</em>. Koselig spricht Deutsch, English, Español, Français, Italiano, Polski und Русский. Mit <em>System</em> richtet sich das Spiel nach der Sprache deines Handys."),
        ("Wann zeigt das Spiel Werbung?",
         "Nur wenn du auf <em>Verrannt?</em> tippst und <em>Video ansehen</em> wählst. Es gibt keine Banner und keine Pop-up-Werbung. Mit <em>Werbefrei</em> funktioniert die Prüfung sofort."),
        ("Wie ändere ich meine Werbeeinwilligung?",
         "Tippe in den Einstellungen neben <em>Werbung &amp; Daten</em> auf <em>Ändern</em> – das Einwilligungsformular von Google öffnet sich erneut. Der Punkt erscheint in Regionen, in denen Einwilligungsregeln gelten."),
        ("Kann ich einen Zwischenstand speichern und später weitermachen?",
         "Ja. Unter Einstellungen → <em>Spielstände</em> gibt es drei Plätze: <em>Speichern</em> sichert den aktuellen Stand, <em>Öffnen</em> holt ihn zurück."),
    ],
    s_del_h="Daten löschen",
    s_del_p="Koselig hat keine Konten. Der Fortschritt liegt auf deinem Gerät und auf dem iPhone zusätzlich in deinem iCloud. Löschst du die App, wird alles entfernt, was sie auf dem Gerät gespeichert hat. Zu Werbe-, Analyse- und iCloud-Daten siehe die <a href=\"{R}de/koselig/delete-data/\">Seite zum Löschen von Daten</a>.",
    # delete data
    d_title="Deine Daten löschen – Koselig",
    d_desc="So löschst du Daten zum Spiel Koselig: Lösche die App; die iCloud-Kopie verwaltet Apple, Werbedaten verwaltet Google.",
    d_h1="Deine Daten löschen",
    d_sub="Koselig von Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> hat keine Konten – es gibt also kein Konto, das gelöscht werden müsste. Deinen Fortschritt speichern wir auf keinem unserer Server.</p>

<h2>Daten auf deinem Gerät</h2>
<p>Fortschritt, Spielstände, Einstellungen, der Status des Kaufs „Werbefrei“ und deine Entscheidung zur Werbeeinwilligung werden auf deinem Smartphone gespeichert. <strong>Um all das zu löschen, lösche die App</strong>:</p>
<ul>
<li><strong>iPhone:</strong> Halte das Koselig-Symbol gedrückt → <em>App entfernen</em> → <em>App löschen</em>.</li>
<li><strong>Android:</strong> Halte das Koselig-Symbol gedrückt → <em>App-Info</em> → <em>Deinstallieren</em> (oder <em>Speicher → Speicherinhalt löschen</em>, um die App zu behalten und nur ihre Daten zu löschen).</li>
</ul>
<p>Das Löschen der App storniert oder entfernt den Kauf „Werbefrei“ nicht – er gehört zu deiner Apple-ID oder deinem Google-Konto und lässt sich später wiederherstellen.</p>

<h2>iCloud-Kopie (iPhone)</h2>
<p>Auf dem iPhone werden Fortschritt und Spielstände zusätzlich in dein eigenes iCloud kopiert. Apple speichert sie unter deiner Apple-ID. Zum Abschalten deaktiviere iCloud für Koselig: <em>Einstellungen → [dein Name] → iCloud</em>.</p>
<h2>Analyse und Absturzberichte</h2>
<p>Analyse-Ereignisse und Absturzberichte (Google Firebase) sind nicht mit deinem Namen oder deiner E-Mail verknüpft, daher können wir die Einträge einer einzelnen Person nicht finden. Sie werden automatisch gelöscht: Analyse-Ereignisse spätestens nach 14 Monaten, Absturzberichte nach 90 Tagen.</p>
<h2>Werbedaten</h2>
<p>Die Werbung in Koselig stellt Google AdMob bereit. Für die von Google erhobenen Daten ist Google verantwortlich. Du kannst:</p>
<ul>
<li>deine Android-Werbe-ID zurücksetzen oder löschen: <em>Einstellungen → Google → Anzeigen</em>;</li>
<li>deine Einwilligung im Spiel ändern: <em>Einstellungen → Werbung &amp; Daten</em>;</li>
<li>Daten in deinem Google-Konto verwalten oder löschen: <a href="https://myadcenter.google.com/" rel="noopener">Mein Werbecenter</a> und <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Daten und Datenschutz</a>;</li>
<li>nachlesen, wie Google Daten aus Apps verwendet: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>

<h2>E-Mails an uns</h2>
<p>Wenn du uns geschrieben hast und deine Nachrichten gelöscht haben möchtest, schick von derselben Adresse eine Anfrage an <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a>. Wir löschen sie innerhalb von 30 Tagen und bestätigen dir das.</p>
<p>Mehr dazu: <a href="{R}de/koselig/privacy/">Datenschutzerklärung</a>.</p>
""",
    nf_title="Seite nicht gefunden – Coffee Beans Studio",
    nf_h1="Diese Seite ist erloschen wie eine Kerze",
    nf_p="Vielleicht stimmt die Adresse nicht, oder die Seite ist umgezogen.",
    nf_cta="Zurück zum Studio",
)

# ─────────────────────────────── FRANÇAIS ───────────────────────────────
# Термины игры — колонка «fr» ~/lotok/tools/teksty_gen.py; правовые тексты — смысл английских без изменений.
L["fr"] = dict(
    name="Français", short="FR", date="17 novembre 2026",
    nav_koselig="Koselig", nav_support="Aide", skip="Aller au contenu", lang_label="Langue",
    foot_legal="Confidentialité", foot_terms="Conditions", foot_support="Aide", foot_delete="Suppression des données",
    soon_stores="Bientôt sur l’App Store et Google Play",
    home_title="Coffee Beans Studio — des jeux douillets et malins",
    home_desc="Coffee Beans Studio est un petit studio indépendant qui crée des jeux douillets et malins. Notre premier jeu, Koselig, est un casse-tête sur plateau de bois pour iPhone et Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Des jeux paisibles<br>pour les soirées au chaud",
    hero_p="Nous créons des jeux douillets et malins — de ceux auxquels on joue sans se presser, une tasse de thé à la main, à la lueur d’une bougie.",
    hero_cta="Découvrir Koselig",
    ch1_h="Infusé sans hâte",
    ch1_p="Coffee Beans Studio est un petit studio indépendant. Ce qui compte pour nous : des casse-tête paisibles, des matières chaleureuses et un design honnête — des choses qu’on touche du regard (le bois, le lin, la lueur d’une bougie) et des règles qu’on apprend en une minute.",
    ch2_h="Koselig",
    ch2_sub="Un casse-tête sur plateau de bois",
    ch2_p="Placez toutes les pièces sur le plateau de bois. Changez de table, de plateau et de pièces selon votre humeur : chêne ou lin, noyer ou laiton, peinture ou pierre. Et si vous ne voyez plus d’issue, un petit bonsaï peut vous dire si la position a encore une solution.",
    ch2_cta="À propos du jeu",
    word_q="koselig",
    word_def="<em>norvégien</em> — douillet, chaleureux, d’une intimité agréable. Ce que l’on ressent près d’une bougie, sous un plaid, en bonne compagnie.",
    soon_h="Presque dans la boîte",
    soon_p="Koselig se prépare pour l’App Store et Google Play. Les liens apparaîtront ici le jour de la sortie.",
    end_h="Un petit mot ?",
    end_p="Une question, une idée, un bug dans un casse-tête ? Nous lisons chaque message.",
    # Koselig
    k_title="Koselig — un casse-tête douillet sur plateau de bois pour iPhone et Android",
    k_desc="Koselig est un casse-tête paisible sur plateau de bois : placez toutes les pièces sur le plateau, choisissez votre table, votre plateau et vos pièces, et un petit bonsaï fleurit quand vous réussissez. Bientôt sur l’App Store et Google Play.",
    k_eyebrow="Un jeu de Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Un casse-tête douillet sur plateau de bois. Placez toutes les pièces sur le plateau — et prenez votre temps.",
    k_about_h="Un casse-tête, sans se presser",
    k_about_p=[
        "Koselig est un casse-tête numérique sur plateau de bois. Les pièces sont posées sur la table autour du plateau : vous les prenez, les tournez et les placez jusqu’à ce que chaque case soit remplie.",
        "Les niveaux vous guident le long d’une carte, des petits plateaux jusqu’au plateau complet. Il y a plus d’une façon de remplir un plateau — et la plus stricte de toutes, où deux pièces de même couleur ne se touchent jamais.",
        "Vous doutez que la position ait encore une issue ? Touchez <em>Sans issue ?</em> : le bonsaï vérifie pour vous, après une courte vidéo que vous choisissez de regarder — ou tout de suite si vous avez acheté <em>Sans pub</em>.",
    ],
    k_feat_h="Ce que vous y trouverez",
    k_feats=[
        ("Trois tables", "Chêne, lin et noyer — chacune avec sa petite vie tranquille : une bougie, le thé qui fume, la lavande dans la brise."),
        ("Plateaux et pièces", "Plateaux en pin, noyer, pierre, acier, laiton, olivier et cerisier. Pièces : peinture, bois, pierre, métal et terrazzo."),
        ("Une carte des niveaux", "Des premiers pas en douceur sur de petits plateaux, puis le casse-tête complet."),
        ("Le bonsaï", "Votre allié pour la vérification <em>Sans issue ?</em> — et il fleurit quand vous réussissez un niveau."),
        ("Sauvegardes", "Trois emplacements pour les positions auxquelles vous voulez revenir."),
        ("Sept langues", "Français, English, Español, Deutsch, Italiano, Polski et Русский."),
    ],
    k_ads_h="Franc jeu sur la pub",
    k_ads_p="Ni bannière ni publicité qui surgit à l’écran. Une courte vidéo n’est diffusée que si vous demandez une vérification <em>Sans issue ?</em> et choisissez de la regarder. Un seul achat facultatif, <em>Sans pub</em>, permet de vérifier sans vidéo.",
    k_shots_h="Captures d’écran",
    k_shot_alts=[
        "Un petit plateau sur la table en lin, entouré de quelques pièces",
        "La table en noyer, avec le plateau de bois et des pièces au-dessus et en dessous",
        "La fenêtre « Sans issue ? » avec un bonsaï en pot",
        "L’écran « Réussi ! » avec le bonsaï et le temps réalisé",
        "La carte des niveaux : un chemin à travers les collines d’automne, jusqu’à une maison tout en haut",
        "Réglages : pièces, plateau, table, sauvegardes, son, langue et « Sans pub »",
    ],
    k_platforms="iPhone et Android · Français, English, Español, Deutsch, Italiano, Polski, Русский",
    k_links_h="Bon à savoir",
    # legal common
    legal_updated="Dernière mise à jour",
    # privacy
    p_title="Politique de confidentialité — Koselig",
    p_desc="Ce que le jeu Koselig et le site coffeebeansstudio.eu font de vos données : pas de compte, progression sur votre appareil, Google AdMob pour des vidéos avec récompense facultatives, achats via Apple et Google.",
    p_h1="Politique de confidentialité",
    p_sub="Koselig et coffeebeansstudio.eu",
    privacy_html="""
<p class="note">Seule la version <a href="{R}koselig/privacy/">anglaise</a> fait foi. Ce texte en est une traduction, fournie pour votre commodité.</p>
<p>Cette politique explique ce que deviennent vos données lorsque vous jouez à <strong>Koselig</strong> sur iPhone ou Android et lorsque vous consultez <strong>coffeebeansstudio.eu</strong>. Nous l’avons rédigée pour qu’elle corresponde à ce que fait réellement l’application.</p>

<h2 id="who">Qui sommes-nous ?</h2>
<p>Koselig est publié par <strong>Coffee Beans Studio</strong>. Le responsable du traitement de vos données personnelles au sens du RGPD est <strong>Dzmitry Kurtsikau</strong>, particulier établi en Pologne (« nous »). Pour toute question relative à la confidentialité, écrivez à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">En bref</h2>
<ul>
<li>Il n’y a <strong>aucun compte</strong>, et aucune connexion n’est requise. Nous ne vous demandons jamais votre nom, votre adresse e-mail ni votre numéro de téléphone.</li>
<li>Votre progression et vos réglages sont <strong>enregistrés sur votre appareil</strong> ; sur iPhone, ils sont aussi copiés dans votre propre iCloud. Nous ne les recevons pas.</li>
<li>Le jeu n’affiche de publicité <strong>que si vous choisissez</strong> de regarder une courte vidéo avec récompense pour la vérification <em>Sans issue ?</em> Il n’y a ni bannière ni publicité interstitielle. Les publicités sont fournies par <strong>Google AdMob</strong>, qui traite des données et des identifiants de l’appareil.</li>
<li>Lorsque la loi l’exige (par exemple dans l’EEE, au Royaume-Uni et en Suisse), votre <strong>consentement</strong> vous est demandé via le formulaire de consentement de Google avant l’affichage de publicités personnalisées.</li>
<li>L’achat facultatif <strong>« Sans pub »</strong> est géré par Apple ou Google. Nous ne voyons jamais vos informations de paiement.</li>
<li>Koselig utilise <strong>Google Firebase</strong> pour l’analyse du jeu et les rapports de plantage. Ils ne contiennent ni votre nom, ni votre e-mail, ni vos contacts. Nous ne vendons pas de données personnelles.</li>
</ul>

<h2 id="device">1. Données stockées sur votre appareil</h2>
<p>Koselig enregistre les éléments suivants sur votre téléphone, pour que vous puissiez reprendre la partie là où vous l’aviez laissée :</p>
<ul>
<li>la progression : niveaux débloqués, position actuelle des pièces et vos trois emplacements de sauvegarde ;</li>
<li>les réglages : son, langue, table, plateau et pièces choisis ;</li>
<li>le fait que vous possédiez ou non l’achat « Sans pub » ;</li>
<li>votre choix en matière de consentement publicitaire, enregistré sur l’appareil par le SDK de consentement de Google.</li>
</ul>
<p>Ces données restent sur votre appareil et ne nous sont pas transmises. Elles sont effacées lorsque vous supprimez l’application. <strong>Sur iPhone</strong>, la progression et les sauvegardes sont aussi copiées dans <strong>votre propre iCloud</strong> (stockage clé-valeur iCloud), pour continuer sur un autre appareil ou après une réinstallation. Cette copie est conservée par Apple sous votre identifiant Apple ; nous ne pouvons pas la lire. Vous pouvez la désactiver dans Réglages iOS → [votre nom] → iCloud. Sur Android, le jeu n’utilise pas de sauvegarde dans le cloud : après une réinstallation, la progression repart de zéro. L’achat « Sans pub » peut toujours être restauré auprès d’Apple ou de Google (Réglages → <em>Restaurer</em>).</p>

<h2 id="ads">2. Publicité : Google AdMob</h2>
<p>Koselig utilise le <strong>Google Mobile Ads SDK</strong> (Google AdMob) pour afficher des vidéos avec récompense. Pour qu’une vidéo soit prête au moment où vous la demandez, l’application initialise le SDK au lancement et charge une vidéo en arrière-plan. Google peut donc recevoir des données de votre appareil <strong>même si vous ne regardez jamais de vidéo</strong>.</p>
<p>Parmi les données que Google peut collecter et traiter via le SDK :</p>
<ul>
<li>des identifiants de l’appareil : sur Android, l’<strong>identifiant publicitaire</strong> ; sur iPhone, l’identifiant pour les fournisseurs (IDFV) et d’autres signaux de l’appareil ;</li>
<li>votre <strong>adresse IP</strong>, qui peut servir à estimer une localisation approximative (pays ou ville) ;</li>
<li>des informations sur l’appareil et l’application : modèle, système d’exploitation et sa version, langue, taille de l’écran, version de l’application ;</li>
<li>les interactions avec les publicités : quelles publicités ont été chargées, affichées, regardées jusqu’au bout ou touchées.</li>
</ul>
<p>Google utilise ces données pour diffuser et mesurer les publicités, pour prévenir la fraude et les abus et — <strong>uniquement avec votre consentement lorsque celui-ci est requis</strong> — pour personnaliser les publicités. Sans consentement, Google peut tout de même afficher des publicités non personnalisées ou limitées, qui utilisent néanmoins certaines données de l’appareil à des fins de limitation de la fréquence d’affichage, de mesure et de prévention de la fraude.</p>
<p><strong>Sur iPhone</strong>, Koselig vous demande une fois l’autorisation de vous suivre (App Tracking Transparency) avant de charger des publicités. Si vous l’acceptez, Google peut utiliser l’identifiant publicitaire d’Apple (IDFA) pour personnaliser et mesurer les publicités. Si vous refusez, l’IDFA n’est accessible ni à l’application ni à Google, et le jeu fonctionne de la même façon. Vous pouvez changer ce choix à tout moment : Réglages iOS → Confidentialité et sécurité → Suivi.</p>
<p><strong>Réseaux publicitaires.</strong> Nous utilisons uniquement Google AdMob et n’avons pas activé de médiation avec d’autres réseaux. La version Android contient actuellement des adaptateurs logiciels qu’AdMob peut utiliser pour la médiation avec Meta Audience Network et AppLovin ; ils ne sont pas activés dans notre compte AdMob, et nous prévoyons de les retirer. Si nous activons un jour un autre réseau, nous mettrons d’abord cette politique à jour.</p>
<p>En savoir plus auprès de Google :</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Comment Google utilise les informations des sites ou applications qui utilisent ses services</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Règles de confidentialité de Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Règles de Google relatives au consentement de l’utilisateur dans l’UE</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Outils de consentement de Google pour les applications (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Mon Centre publicitaire — gérer la personnalisation des annonces dans votre compte Google</a></li>
</ul>

<h2 id="consent">3. Votre consentement et comment le modifier</h2>
<p>Dans les régions où le consentement est requis, Koselig affiche le formulaire de consentement de Google (User Messaging Platform) avant toute demande de publicité. Vous pouvez accepter, refuser ou choisir les finalités. Votre choix peut être modifié à tout moment dans le jeu : <strong>Réglages → Publicité et données</strong> (cette option apparaît là où les règles de consentement s’appliquent). Supprimer puis réinstaller l’application réinitialise aussi votre choix.</p>
<p>Vous pouvez également limiter la publicité sur votre appareil : sur Android, dans <em>Paramètres → Google → Annonces</em> (réinitialiser ou supprimer l’identifiant publicitaire) ; sur iPhone, dans <em>Réglages → Confidentialité et sécurité → Publicité Apple</em>.</p>

<h2 id="firebase">4. Analyse du jeu et rapports de plantage : Google Firebase</h2>
<p>Koselig utilise <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> et <strong>Firebase Remote Config</strong> (Google). Ils nous permettent de voir quels niveaux sont trop difficiles, de trouver et corriger les plantages et d’ajuster les réglages du jeu sans mise à jour de l’application.</p>
<ul>
<li><strong>Analytics</strong> reçoit un identifiant d’instance de l’application créé par Firebase et des événements sur l’utilisation du jeu : niveau commencé, terminé ou réinitialisé, indices et vérification <em>Sans issue ?</em>, réglages ouverts, langue changée, achat « Sans pub » commencé, réussi ou échoué. Nous ne le relions ni à votre nom, ni à votre e-mail, ni à votre identifiant publicitaire.</li>
<li><strong>Crashlytics</strong>, après un plantage, reçoit un rapport : l’état technique de l’application, la trace de la pile, le modèle de l’appareil et la version du système, ainsi qu’un identifiant d’installation Crashlytics.</li>
<li><strong>Remote Config</strong> télécharge les réglages du jeu et transmet votre pays, votre langue, votre fuseau horaire, les versions de l’application et du système.</li>
</ul>
<p>Google traite ces données pour notre compte. Les événements d’analyse sont conservés 14 mois au maximum, les rapports de plantage 90 jours. Voir <a href="https://firebase.google.com/support/privacy" rel="noopener">Confidentialité et sécurité dans Firebase</a>.</p>
<h2 id="purchases">5. L’achat « Sans pub »</h2>
<p>Koselig propose un seul achat intégré facultatif, <strong>« Sans pub »</strong> (produit <code>koselig.no_ads</code>). Il est entièrement traité par l’<strong>App Store d’Apple</strong> ou par <strong>Google Play</strong>. Nous ne recevons ni votre nom, ni votre carte, ni vos informations de paiement. L’application reçoit seulement de la boutique la confirmation que l’achat vous appartient, et elle enregistre cette information sur votre appareil. Voir la <a href="https://www.apple.com/legal/privacy/" rel="noopener">Politique de confidentialité d’Apple</a> et les <a href="https://policies.google.com/privacy" rel="noopener">Règles de confidentialité de Google</a>.</p>

<h2 id="no">6. Ce que nous ne faisons pas</h2>
<ul>
<li>Pas de compte, pas de connexion, pas de fonctions sociales.</li>
<li>Aucun suivi de notre part dans les applications ou sites web d’autres entreprises.</li>
<li>Aucun accès à vos contacts, à vos photos, à l’appareil photo, au micro ni à votre localisation précise.</li>
<li>Nous ne vendons pas de données personnelles et ne les utilisons à aucune autre fin que celles décrites ici.</li>
</ul>
<p>L’application utilise l’accès à Internet (pour la publicité, l’analyse et les rapports de plantage, l’achat et, sur iPhone, les sauvegardes iCloud) et, sur Android, le vibreur pour le retour haptique.</p>

<h2 id="children">7. Enfants</h2>
<p>Koselig est un jeu de casse-tête tout public. Il ne s’adresse pas aux enfants de moins de 13 ans et ne figure dans aucune catégorie destinée aux enfants. Les publicités de Koselig ne sont pas configurées comme destinées aux enfants. Nous ne collectons pas sciemment d’informations personnelles auprès d’enfants. Si vous pensez qu’un enfant nous a communiqué des données personnelles, contactez-nous et nous les supprimerons.</p>

<h2 id="legal">8. Bases légales (RGPD)</h2>
<ul>
<li><strong>Consentement</strong> (art. 6.1.a du RGPD) — publicité personnalisée, ainsi que stockage d’informations sur votre appareil ou accès à celles-ci lorsque le consentement est requis.</li>
<li><strong>Intérêts légitimes</strong> (art. 6.1.f) — affichage de publicités non personnalisées pour financer un jeu gratuit, mesure des publicités et prévention de la fraude.</li>
<li><strong>Intérêts légitimes</strong> (art. 6.1.f) — analyse du jeu et rapports de plantage pour corriger et améliorer le jeu.</li>
<li><strong>Contrat</strong> (art. 6.1.b) — fourniture et restauration de l’achat « Sans pub ».</li>
</ul>
<p>Google agit en qualité de responsable du traitement indépendant pour les données qu’il collecte via son SDK. Google et Apple peuvent traiter des données en dehors de l’Espace économique européen, dans le cadre de leurs propres garanties.</p>

<h2 id="retention">9. Durée de conservation</h2>
<p>Les données stockées sur votre appareil y restent jusqu’à ce que vous supprimiez l’application. La copie de votre progression dans iCloud reste dans votre iCloud. Les événements d’analyse sont conservés 14 mois au maximum, les rapports de plantage 90 jours. Les données publicitaires collectées par Google sont conservées conformément aux règles de Google. Si vous nous écrivez, nous ne conservons votre adresse e-mail que le temps nécessaire pour vous répondre et traiter votre demande.</p>

<h2 id="rights">10. Vos droits</h2>
<p>Vous disposez d’un droit d’accès, de rectification et d’effacement de vos données personnelles, du droit de demander la limitation du traitement ou de vous y opposer, du droit à la portabilité des données et du droit de retirer votre consentement à tout moment. Comme nous ne conservons pas de données de jeu sur nos serveurs, la plupart des demandes se règlent en supprimant l’application ; les demandes concernant les données publicitaires peuvent être adressées à Google via les liens ci-dessus. Vous pouvez toujours nous écrire à <a href="mailto:{EMAIL}">{EMAIL}</a>. Vous avez également le droit d’introduire une réclamation auprès d’une autorité de contrôle — en Pologne, le <a href="https://uodo.gov.pl/" rel="noopener">Président de l’Office de protection des données personnelles (UODO)</a> — ou auprès de l’autorité de votre pays.</p>

<h2 id="website">11. Ce site</h2>
<p>Le site coffeebeansstudio.eu est statique. Il n’utilise <strong>ni cookies, ni outil d’analyse, ni polices ou scripts tiers</strong>. Il est hébergé sur <strong>GitHub Pages</strong> (GitHub, Inc.), et son service de noms de domaine (DNS) est assuré par <strong>Cloudflare</strong>. Ces prestataires peuvent traiter votre adresse IP et des données techniques relatives aux requêtes dans les journaux de leurs serveurs, à des fins de sécurité et d’acheminement. Voir la <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Déclaration de confidentialité de GitHub</a> et la <a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Politique de confidentialité de Cloudflare</a>.</p>

<h2 id="changes">12. Modifications</h2>
<p>Si l’application se met à faire quelque chose de nouveau avec les données — par exemple un nouveau réseau publicitaire ou un outil d’analyse —, nous mettrons cette page à jour avant que le changement n’arrive dans l’application, et nous modifierons la date ci-dessous.</p>
""",
    # terms
    t_title="Conditions d’utilisation — Coffee Beans Studio",
    t_desc="Des conditions courtes et honnêtes pour Koselig et les autres jeux de Coffee Beans Studio.",
    t_h1="Conditions d’utilisation",
    t_sub="Koselig et les autres jeux de Coffee Beans Studio",
    terms_html="""
<p class="note">Seule la version <a href="{R}terms/">anglaise</a> fait foi. Ce texte en est une traduction, fournie pour votre commodité.</p>
<p>Ces conditions s’appliquent lorsque vous utilisez <strong>Koselig</strong> ou un autre jeu de <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Pologne). En jouant, vous les acceptez. Elles sont courtes, et c’est voulu.</p>

<h2>1. Utilisation du jeu</h2>
<p>Nous vous accordons un droit personnel, non exclusif et non cessible d’installer nos jeux et d’y jouer sur les appareils que vous possédez ou contrôlez, pour votre propre usage non commercial. Merci de ne pas copier, revendre ni redistribuer le jeu ou ses graphismes, et de ne pas en faire l’ingénierie inverse, sauf dans la mesure où la loi l’autorise.</p>

<h2>2. Les boutiques</h2>
<p>Vous téléchargez nos jeux sur l’App Store d’Apple ou sur Google Play, dont les conditions s’appliquent également. Pour les applications téléchargées sur l’App Store, le <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">contrat de licence d’utilisateur final standard</a> d’Apple s’applique en plus des présentes conditions. Apple et Google ne sont responsables ni du jeu ni de son assistance.</p>

<h2>3. La publicité et l’achat « Sans pub »</h2>
<p>Koselig est gratuit. Il peut afficher une courte vidéo avec récompense lorsque vous demandez une vérification <em>Sans issue ?</em> Les publicités sont fournies par Google AdMob ; nous n’en contrôlons pas le contenu et ne sommes pas responsables des produits de tiers qui y sont présentés.</p>
<p>« Sans pub » est un achat unique et non consommable. Il permet à la vérification <em>Sans issue ?</em> de fonctionner sans vidéo ; le nombre de vérifications par niveau reste le même. Le prix est indiqué par la boutique avant le paiement. Le paiement, les remboursements et les annulations sont gérés par Apple ou Google selon leurs propres règles. L’achat est lié à votre identifiant Apple ou à votre compte Google et peut être restauré après une réinstallation (Réglages → <em>Restaurer</em>).</p>

<h2>4. Votre progression</h2>
<p>La progression est enregistrée sur votre appareil et, sur iPhone, aussi dans votre propre iCloud. Si vous supprimez l’application ou perdez l’appareil, nous ne pouvons pas la récupérer ; sur iPhone, elle peut revenir depuis iCloud.</p>

<h2>5. Évolutions et disponibilité</h2>
<p>Nous pouvons mettre le jeu à jour — ajouter, modifier ou retirer des niveaux et des fonctionnalités — et nous pouvons cesser de le proposer. Nous nous efforcerons de le maintenir en état de marche, mais nous ne pouvons pas promettre qu’il sera toujours disponible ni exempt de bugs.</p>

<h2>6. Responsabilité</h2>
<p>Le jeu est fourni « en l’état ». Dans la mesure permise par la loi, nous ne sommes pas responsables des dommages indirects ni de la perte de données. Rien dans les présentes conditions ne limite une responsabilité que la loi ne permet pas de limiter, ni vos droits de consommateur au titre du droit de votre pays.</p>

<h2>7. Droit applicable</h2>
<p>Les présentes conditions sont régies par le droit polonais. Si vous êtes un consommateur, vous conservez en outre la protection des dispositions impératives du droit du pays où vous résidez.</p>

<h2>8. Contact</h2>
<p>Questions ou réclamations : <a href="mailto:{EMAIL}">{EMAIL}</a>. La façon dont nous traitons les données est décrite dans la <a href="{R}fr/privacy/">Politique de confidentialité</a>.</p>
""",
    # support
    s_title="Aide — Coffee Beans Studio",
    s_desc="Aide pour Koselig : restaurer l’achat « Sans pub », recommencer un niveau, changer de langue, consentement publicitaire et suppression de vos données.",
    s_h1="Aide",
    s_sub="Nous lisons chaque message",
    s_mail_h="Écrivez-nous",
    s_mail_p="Indiquez le modèle de votre téléphone, la version du jeu et ce qui s’est passé. Une capture d’écran nous aide beaucoup.",
    s_faq_h="Questions",
    faq=[
        ("Comment restaurer l’achat « Sans pub » ?",
         "Touchez ☰ en haut à droite pour ouvrir les Réglages, puis touchez <em>Restaurer</em> à côté de <em>Sans pub</em>. Utilisez le même identifiant Apple ou compte Google que pour l’achat. Le jeu vérifie l’achat auprès de la boutique à chaque lancement : après une réinstallation, l’achat revient donc aussi de lui-même dès que la boutique a répondu."),
        ("Comment recommencer un niveau ?",
         "Ouvrez les Réglages et touchez <em>Recommencer</em>, puis touchez à nouveau pour confirmer. Le niveau en cours repart de zéro. Pour tout effacer — progression et réglages —, supprimez l’application."),
        ("Comment changer de langue ?",
         "Réglages → <em>Langue</em>. Koselig parle français, anglais, espagnol, allemand, italien, polonais et russe. <em>Système</em> suit la langue de votre téléphone."),
        ("Quand le jeu affiche-t-il des publicités ?",
         "Uniquement quand vous touchez <em>Sans issue ?</em> et choisissez <em>Voir la vidéo</em>. Ni bannière ni publicité qui surgit à l’écran. Avec <em>Sans pub</em>, la vérification se fait tout de suite."),
        ("Comment modifier mon consentement publicitaire ?",
         "Dans Réglages, touchez <em>Modifier</em> à côté de <em>Publicité et données</em> : le formulaire de consentement de Google s’ouvre à nouveau. Cette option apparaît dans les régions où les règles de consentement s’appliquent."),
        ("Puis-je garder une position pour y revenir plus tard ?",
         "Oui. Réglages → <em>Sauvegardes</em> propose trois emplacements : <em>Sauver</em> enregistre la position actuelle, <em>Charger</em> la rétablit."),
    ],
    s_del_h="Supprimer vos données",
    s_del_p="Koselig fonctionne sans compte. La progression est conservée sur votre appareil et, sur iPhone, aussi dans votre iCloud. Supprimer l’application efface tout ce qu’elle a enregistré sur l’appareil. Pour les données publicitaires, d’analyse et iCloud, voir la <a href=\"{R}fr/koselig/delete-data/\">page sur la suppression des données</a>.",
    # delete data
    d_title="Supprimer vos données — Koselig",
    d_desc="Comment supprimer les données du jeu Koselig : supprimez l’application ; la copie iCloud est gérée par Apple, les données publicitaires par Google.",
    d_h1="Supprimer vos données",
    d_sub="Koselig, un jeu de Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> fonctionne sans compte : il n’y a donc aucun compte à supprimer. Nous ne conservons pas votre progression sur nos serveurs.</p>

<h2>Données sur votre appareil</h2>
<p>La progression, les sauvegardes, les réglages, l’état de l’achat « Sans pub » et votre choix de consentement publicitaire sont enregistrés sur votre téléphone. <strong>Pour tout effacer, supprimez l’application</strong> :</p>
<ul>
<li><strong>iPhone :</strong> maintenez le doigt sur l’icône de Koselig → <em>Supprimer l’app</em> → <em>Supprimer l’app</em>.</li>
<li><strong>Android :</strong> maintenez le doigt sur l’icône de Koselig → <em>Infos sur l’appli</em> → <em>Désinstaller</em> (ou <em>Stockage → Vider l’espace de stockage</em> pour garder l’application mais effacer ses données).</li>
</ul>
<p>Supprimer l’application n’annule pas et ne retire pas l’achat « Sans pub » : il est rattaché à votre identifiant Apple ou à votre compte Google et pourra être restauré plus tard.</p>

<h2>Copie iCloud (iPhone)</h2>
<p>Sur iPhone, la progression et les sauvegardes sont aussi copiées dans votre propre iCloud. Apple la conserve sous votre identifiant Apple. Pour l’arrêter, désactivez iCloud pour Koselig : <em>Réglages → [votre nom] → iCloud</em>.</p>
<h2>Analyse et rapports de plantage</h2>
<p>Les événements d’analyse et les rapports de plantage (Google Firebase) ne sont liés ni à votre nom ni à votre e-mail : nous ne pouvons donc pas retrouver les données d’une personne. Ils sont supprimés automatiquement : les événements d’analyse au plus tard après 14 mois, les rapports de plantage après 90 jours.</p>
<h2>Données publicitaires</h2>
<p>Les publicités de Koselig sont fournies par Google AdMob. Google est responsable du traitement des données qu’il collecte. Vous pouvez :</p>
<ul>
<li>réinitialiser ou supprimer votre identifiant publicitaire Android : <em>Paramètres → Google → Annonces</em> ;</li>
<li>modifier votre consentement dans le jeu : <em>Réglages → Publicité et données</em> ;</li>
<li>gérer ou supprimer des données dans votre compte Google : <a href="https://myadcenter.google.com/" rel="noopener">Mon Centre publicitaire</a> et <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Données et confidentialité</a> ;</li>
<li>découvrir comment Google utilise les données des applications : <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>

<h2>Vos e-mails</h2>
<p>Si vous nous avez écrit et souhaitez que vos messages soient supprimés, envoyez une demande à <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> depuis la même adresse. Nous les supprimerons sous 30 jours et vous le confirmerons.</p>
<p>Plus de détails : <a href="{R}fr/koselig/privacy/">Politique de confidentialité</a>.</p>
""",
    nf_title="Page introuvable — Coffee Beans Studio",
    nf_h1="Cette page s’est éteinte comme une bougie",
    nf_p="L’adresse est peut-être erronée, ou la page a été déplacée.",
    nf_cta="Retour au studio",
)

# ─────────────────────────────── ITALIANO ───────────────────────────────
# Термины игры — колонка «it» ~/lotok/tools/teksty_gen.py; правовые тексты — смысл английских без изменений.
L["it"] = dict(
    name="Italiano", short="IT", date="17 novembre 2026",
    nav_koselig="Koselig", nav_support="Assistenza", skip="Vai al contenuto", lang_label="Lingua",
    foot_legal="Privacy", foot_terms="Termini", foot_support="Assistenza", foot_delete="Elimina dati",
    soon_stores="Presto su App Store e Google Play",
    home_title="Coffee Beans Studio — giochi accoglienti e ingegnosi",
    home_desc="Coffee Beans Studio è un piccolo studio indipendente che crea giochi accoglienti e ingegnosi. Il nostro primo gioco, Koselig, è un rompicapo a incastro in un vassoio di legno, per iPhone e Android.",
    hero_eyebrow="Coffee Beans Studio",
    hero_h1="Giochi tranquilli<br>per serate al calduccio",
    hero_p="Creiamo giochi accoglienti e ingegnosi, di quelli da giocare con calma, con una tazza di tè, a lume di candela.",
    hero_cta="Scopri Koselig",
    ch1_h="A fuoco lento",
    ch1_p="Coffee Beans Studio è un piccolo studio indipendente. Ci stanno a cuore i rompicapi tranquilli, i materiali caldi e un design onesto: cose da toccare con gli occhi — legno, lino, luce di candela — e regole che si imparano in un minuto.",
    ch2_h="Koselig",
    ch2_sub="Un rompicapo a incastro in un vassoio di legno",
    ch2_p="Sistema tutti i pezzi nel vassoio di legno. Tavolo, vassoio e pezzi li scegli a seconda dell’umore: rovere o lino, noce o ottone, vernice o pietra. E quando sei bloccato, un piccolo bonsai può dirti se c’è ancora una soluzione.",
    ch2_cta="Tutto sul gioco",
    word_q="koselig",
    word_def="<em>norvegese</em> — accogliente, caldo, piacevolmente intimo. La sensazione di una candela, di una coperta e di buona compagnia.",
    soon_h="Il pacchetto è quasi pronto",
    soon_p="Koselig si prepara al debutto su App Store e Google Play. Il giorno dell’uscita troverai qui i link.",
    end_h="Passa a salutarci",
    end_p="Domande, idee o un bug in un rompicapo? Leggiamo ogni messaggio.",
    # Koselig
    k_title="Koselig — un rompicapo accogliente in un vassoio di legno, per iPhone e Android",
    k_desc="Koselig è un rompicapo tranquillo a incastro: sistema tutti i pezzi nel vassoio di legno, scegli tavolo, vassoio e pezzi e, quando lo completi, guarda fiorire un piccolo bonsai. Presto su App Store e Google Play.",
    k_eyebrow="Un gioco di Coffee Beans Studio",
    k_h1="Koselig",
    k_lead="Un rompicapo accogliente in un vassoio di legno. Sistema tutti i pezzi nel vassoio — e prenditi il tuo tempo.",
    k_about_h="Un rompicapo senza fretta",
    k_about_p=[
        "Koselig è la versione digitale di un rompicapo a incastro in un vassoio di legno. I pezzi sono sul tavolo, intorno al vassoio: li prendi, li ruoti e li sistemi finché non riempi ogni casella.",
        "I livelli ti guidano lungo una mappa, dai vassoi piccoli fino a quello completo. Un vassoio si può riempire in più di un modo, e c’è anche la soluzione più rigorosa, in cui due pezzi dello stesso colore non si toccano mai.",
        "Quando non sei sicuro che una disposizione abbia ancora una soluzione, tocca <em>Bloccato?</em>. Il bonsai la controlla per te dopo un breve video che scegli tu di guardare, oppure subito, se hai acquistato <em>Senza annunci</em>.",
    ],
    k_feat_h="Cosa c’è dentro",
    k_feats=[
        ("Tre tavoli", "Rovere, lino e noce, ognuno con la sua vita quieta: una candela, il vapore del tè, la lavanda mossa dalla brezza."),
        ("Vassoi e pezzi", "Vassoi in pino, noce, pietra, acciaio, ottone, ulivo e ciliegio. Pezzi: vernice, legno, pietra, metallo e terrazzo."),
        ("La mappa dei livelli", "Si comincia piano, con vassoi più piccoli, poi arriva il rompicapo completo."),
        ("Il bonsai", "Ti aiuta nel controllo <em>Bloccato?</em> e fiorisce quando completi un livello."),
        ("Salvataggi", "Tre slot di salvataggio per le disposizioni a cui vuoi tornare."),
        ("Sette lingue", "Italiano, English, Español, Deutsch, Français, Polski e Русский."),
    ],
    k_ads_h="Pubblicità onesta",
    k_ads_p="Niente banner e niente pop-up. Un breve video parte solo quando chiedi il controllo <em>Bloccato?</em> e scegli di guardarlo. Un unico acquisto facoltativo, <em>Senza annunci</em>, fa funzionare il controllo senza video.",
    k_shots_h="Screenshot",
    k_shot_alts=[
        "Un vassoio piccolo sul tavolo in lino, con alcuni pezzi intorno",
        "Il tavolo in noce con il vassoio di legno e i pezzi sopra e sotto",
        "Il riquadro «Bloccato?» con un bonsai in vaso",
        "La schermata «Completato!» con il bonsai e il tempo del livello",
        "La mappa dei livelli: un sentiero tra colline autunnali fino a una casa in cima a un colle",
        "Impostazioni: pezzi, vassoio, tavolo, salvataggi, audio, lingua e «Senza annunci»",
    ],
    k_platforms="iPhone e Android · Italiano, English, Español, Deutsch, Français, Polski, Русский",
    k_links_h="Buono a sapersi",
    # legal common
    legal_updated="Ultimo aggiornamento",
    # privacy
    p_title="Informativa sulla privacy — Koselig",
    p_desc="Come il gioco Koselig e coffeebeansstudio.eu trattano i tuoi dati: nessun account, progressi sul tuo dispositivo, Google AdMob per i video con premio facoltativi, acquisti tramite Apple e Google.",
    p_h1="Informativa sulla privacy",
    p_sub="Koselig e coffeebeansstudio.eu",
    privacy_html="""
<p class="note">La versione vincolante è quella <a href="{R}koselig/privacy/">inglese</a>; questa è una traduzione per comodità.</p>
<p>Questa informativa spiega che cosa succede ai tuoi dati quando giochi a <strong>Koselig</strong> su iPhone o Android e quando visiti <strong>coffeebeansstudio.eu</strong>. L’abbiamo scritta in base a ciò che l’app fa davvero.</p>

<h2 id="who">Chi siamo</h2>
<p>Koselig è pubblicato da <strong>Coffee Beans Studio</strong>. Il titolare del trattamento dei tuoi dati personali ai sensi del GDPR è <strong>Dzmitry Kurtsikau</strong>, persona fisica residente in Polonia («noi»). Per qualsiasi domanda sulla privacy, scrivi a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="short">In breve</h2>
<ul>
<li><strong>Nessun account</strong> e nessun login. Non ti chiediamo mai nome, email o numero di telefono.</li>
<li>Progressi e impostazioni sono <strong>salvati sul tuo dispositivo</strong>; su iPhone vengono anche copiati nel tuo iCloud personale. Noi non li riceviamo.</li>
<li>Il gioco mostra annunci <strong>solo quando scegli tu</strong> di guardare un breve video con premio per il controllo <em>Bloccato?</em>. Non ci sono banner né annunci interstitial. Gli annunci sono forniti da <strong>Google AdMob</strong>, che tratta dati e identificatori del dispositivo.</li>
<li>Dove la legge lo richiede (ad esempio nel SEE, nel Regno Unito e in Svizzera), prima di mostrarti annunci personalizzati ti viene chiesto il <strong>consenso</strong> tramite il modulo di Google.</li>
<li>L’acquisto facoltativo <strong>«Senza annunci»</strong> è gestito da Apple o da Google. Non vediamo mai i tuoi dati di pagamento.</li>
<li>Koselig usa <strong>Google Firebase</strong> per l’analisi del gioco e le segnalazioni degli arresti anomali. Non contengono il tuo nome, la tua email o i tuoi contatti. Non vendiamo dati personali.</li>
</ul>

<h2 id="device">1. Dati salvati sul tuo dispositivo</h2>
<p>Koselig salva sul tuo telefono quanto segue, così puoi riprendere da dove avevi lasciato:</p>
<ul>
<li>progressi di gioco: livelli sbloccati, posizione attuale dei pezzi e i tuoi tre slot di salvataggio;</li>
<li>impostazioni: audio, lingua, tavolo, vassoio e pezzi scelti;</li>
<li>se possiedi l’acquisto «Senza annunci»;</li>
<li>la tua scelta sul consenso pubblicitario, che l’SDK di consenso di Google salva sul dispositivo.</li>
</ul>
<p>Questi dati restano sul tuo dispositivo e non ci vengono inviati. Vengono cancellati quando elimini l’app. <strong>Su iPhone</strong> progressi e salvataggi vengono anche copiati nel <strong>tuo iCloud personale</strong> (archivio chiave-valore di iCloud), per continuare su un altro dispositivo o dopo la reinstallazione. Questa copia è conservata da Apple con il tuo ID Apple; noi non possiamo leggerla. Puoi disattivarla in Impostazioni di iOS → [il tuo nome] → iCloud. Su Android il gioco non usa salvataggi nel cloud, quindi dopo la reinstallazione i progressi ripartono da zero. L’acquisto «Senza annunci» si può sempre ripristinare tramite Apple o Google (Impostazioni → <em>Ripristina</em>).</p>

<h2 id="ads">2. Pubblicità: Google AdMob</h2>
<p>Koselig usa il <strong>Google Mobile Ads SDK</strong> (Google AdMob) per mostrare video con premio. Per avere un video pronto quando lo chiedi, l’app avvia l’SDK all’apertura e carica un video in background. Ciò significa che Google può ricevere dati dal tuo dispositivo <strong>anche se non guardi mai un video</strong>.</p>
<p>Tra i dati che Google può raccogliere e trattare tramite l’SDK ci sono:</p>
<ul>
<li>identificatori del dispositivo: su Android l’<strong>ID pubblicità</strong>; su iPhone l’identificatore per il fornitore e altri segnali del dispositivo;</li>
<li>il tuo <strong>indirizzo IP</strong>, che può servire a stimare una posizione approssimativa (paese o città);</li>
<li>informazioni sul dispositivo e sull’app: modello, sistema operativo e relativa versione, lingua, dimensioni dello schermo, versione dell’app;</li>
<li>interazioni con gli annunci: quali annunci sono stati caricati, mostrati, guardati fino alla fine o toccati.</li>
</ul>
<p>Google usa questi dati per pubblicare e misurare gli annunci, per prevenire frodi e abusi e — <strong>solo con il tuo consenso, dove il consenso è richiesto</strong> — per personalizzare gli annunci. Senza consenso, Google può comunque mostrare annunci non personalizzati o limitati, che usano pur sempre alcuni dati del dispositivo per il limite di frequenza, la misurazione e la prevenzione delle frodi.</p>
<p><strong>Su iPhone</strong> Koselig ti chiede una volta il permesso di tracciarti (App Tracking Transparency) prima di caricare gli annunci. Se lo consenti, Google può usare l’identificatore pubblicitario di Apple (IDFA) per personalizzare e misurare gli annunci. Se rifiuti, l’IDFA non è disponibile né per l’app né per Google, e il gioco funziona allo stesso modo. Puoi cambiare scelta in qualsiasi momento: Impostazioni di iOS → Privacy e sicurezza → Tracciamento.</p>
<p><strong>Reti pubblicitarie.</strong> Usiamo solo Google AdMob e non abbiamo attivato la mediazione con altre reti. La versione Android contiene al momento adattatori software che AdMob può usare per la mediazione con Meta Audience Network e AppLovin; non sono attivati nel nostro account AdMob e prevediamo di rimuoverli. Se mai attiveremo un’altra rete, prima aggiorneremo questa informativa.</p>
<p>Maggiori informazioni da Google:</p>
<ul>
<li><a href="https://policies.google.com/technologies/partner-sites" rel="noopener">Come Google utilizza le informazioni dei siti o delle app che usano i suoi servizi</a></li>
<li><a href="https://policies.google.com/privacy" rel="noopener">Norme sulla privacy di Google</a></li>
<li><a href="https://www.google.com/about/company/user-consent-policy/" rel="noopener">Norme di Google relative al consenso degli utenti dell’UE</a></li>
<li><a href="https://support.google.com/admob/answer/10113207" rel="noopener">Strumenti di Google per il consenso nelle app (UMP)</a></li>
<li><a href="https://myadcenter.google.com/" rel="noopener">Il mio Centro annunci — gestisci la personalizzazione degli annunci nel tuo account Google</a></li>
</ul>

<h2 id="consent">3. Il tuo consenso e come modificarlo</h2>
<p>Nelle regioni in cui il consenso è richiesto, Koselig mostra il modulo di consenso di Google (User Messaging Platform) prima di richiedere annunci. Puoi accettare, rifiutare o scegliere le finalità. Puoi cambiare la tua scelta in qualsiasi momento nel gioco: <strong>Impostazioni → Annunci e dati</strong> (la voce compare dove si applicano le regole sul consenso). Anche eliminare e reinstallare l’app azzera la tua scelta.</p>
<p>Puoi anche limitare gli annunci sul tuo dispositivo: su Android in <em>Impostazioni → Google → Annunci</em> (reimposta o elimina l’ID pubblicità); su iPhone in <em>Impostazioni → Privacy e sicurezza → Pubblicità di Apple</em>.</p>

<h2 id="firebase">4. Analisi del gioco e segnalazioni degli arresti anomali: Google Firebase</h2>
<p>Koselig usa <strong>Google Analytics for Firebase</strong>, <strong>Firebase Crashlytics</strong> e <strong>Firebase Remote Config</strong> (Google). Ci servono per capire quali livelli sono troppo difficili, trovare e correggere gli arresti anomali e regolare le impostazioni del gioco senza aggiornare l’app.</p>
<ul>
<li><strong>Analytics</strong> riceve un identificatore dell’istanza dell’app generato da Firebase ed eventi sull’uso del gioco: livello iniziato, completato o azzerato, suggerimenti e controllo <em>Bloccato?</em>, impostazioni aperte, lingua cambiata, acquisto «Senza annunci» avviato, completato o non riuscito. Non lo colleghiamo al tuo nome, alla tua email o al tuo identificatore pubblicitario.</li>
<li><strong>Crashlytics</strong>, dopo un arresto anomalo, riceve una segnalazione: lo stato tecnico dell’app, lo stack trace, il modello del dispositivo e la versione del sistema, e un identificatore di installazione Crashlytics.</li>
<li><strong>Remote Config</strong> scarica le impostazioni del gioco e invia paese, lingua, fuso orario, versioni dell’app e del sistema.</li>
</ul>
<p>Google tratta questi dati per nostro conto. Gli eventi di analisi sono conservati al massimo 14 mesi, le segnalazioni degli arresti anomali 90 giorni. Vedi <a href="https://firebase.google.com/support/privacy" rel="noopener">Privacy e sicurezza in Firebase</a>.</p>
<h2 id="purchases">5. L’acquisto «Senza annunci»</h2>
<p>Koselig offre un solo acquisto in-app facoltativo, <strong>«Senza annunci»</strong> (prodotto <code>koselig.no_ads</code>). È gestito interamente da <strong>Apple App Store</strong> o <strong>Google Play</strong>. Non riceviamo il tuo nome, la tua carta né i tuoi dati di pagamento. L’app riceve dallo store soltanto la conferma che possiedi l’acquisto e salva questa informazione sul tuo dispositivo. Consulta l’<a href="https://www.apple.com/legal/privacy/" rel="noopener">Informativa sulla privacy di Apple</a> e le <a href="https://policies.google.com/privacy" rel="noopener">Norme sulla privacy di Google</a>.</p>

<h2 id="no">6. Cosa non facciamo</h2>
<ul>
<li>Nessun account, nessun login, nessuna funzione social.</li>
<li>Nessun tracciamento da parte nostra nelle app o nei siti di altre aziende.</li>
<li>Nessun accesso a contatti, foto, fotocamera, microfono o posizione precisa.</li>
<li>Non vendiamo dati personali e non li usiamo per scopi diversi da quelli descritti qui.</li>
</ul>
<p>L’app usa l’accesso a internet (per gli annunci, l’analisi e le segnalazioni degli arresti anomali, l’acquisto e, su iPhone, i salvataggi iCloud) e, su Android, la vibrazione per il feedback aptico.</p>

<h2 id="children">7. Bambini</h2>
<p>Koselig è un rompicapo per un pubblico generale. Non è rivolto ai bambini sotto i 13 anni e non fa parte di una categoria per bambini. Gli annunci in Koselig non sono configurati come destinati ai bambini. Non raccogliamo consapevolmente informazioni personali dai bambini. Se ritieni che un bambino ci abbia fornito dati personali, contattaci e li elimineremo.</p>

<h2 id="legal">8. Basi giuridiche (GDPR)</h2>
<ul>
<li><strong>Consenso</strong> (art. 6, par. 1, lett. a, GDPR) — pubblicità personalizzata e archiviazione di informazioni o accesso a informazioni sul tuo dispositivo, dove è richiesto il consenso.</li>
<li><strong>Legittimo interesse</strong> (art. 6, par. 1, lett. f) — visualizzazione di annunci non personalizzati per finanziare un gioco gratuito, misurazione degli annunci e prevenzione delle frodi.</li>
<li><strong>Legittimo interesse</strong> (art. 6, par. 1, lett. f) — analisi del gioco e segnalazioni degli arresti anomali per correggere e migliorare il gioco.</li>
<li><strong>Contratto</strong> (art. 6, par. 1, lett. b) — fornitura e ripristino dell’acquisto «Senza annunci».</li>
</ul>
<p>Google agisce come titolare autonomo del trattamento per i dati che raccoglie tramite il suo SDK. Google e Apple possono trattare dati al di fuori dello Spazio economico europeo, con garanzie proprie.</p>

<h2 id="retention">9. Per quanto tempo vengono conservati i dati</h2>
<p>I dati sul tuo dispositivo restano lì finché non elimini l’app. La copia dei progressi in iCloud resta nel tuo iCloud. Gli eventi di analisi sono conservati al massimo 14 mesi, le segnalazioni degli arresti anomali 90 giorni. I dati pubblicitari raccolti da Google vengono conservati secondo le norme di Google. Se ci scrivi, conserviamo il tuo indirizzo email solo per il tempo necessario a risponderti e a risolvere la tua richiesta.</p>

<h2 id="rights">10. I tuoi diritti</h2>
<p>Hai il diritto di accesso, di rettifica e di cancellazione dei tuoi dati personali, di limitazione del trattamento, di opposizione al trattamento, alla portabilità dei dati e di revocare il consenso in qualsiasi momento. Poiché non conserviamo dati di gioco sui nostri server, la maggior parte delle richieste si risolve eliminando l’app; le richieste sui dati pubblicitari si possono rivolgere a Google tramite i link qui sopra. Puoi sempre scriverci a <a href="mailto:{EMAIL}">{EMAIL}</a>. Hai anche il diritto di proporre reclamo a un’autorità di controllo — in Polonia il <a href="https://uodo.gov.pl/" rel="noopener">Presidente dell’Ufficio per la protezione dei dati personali (UODO)</a> — o all’autorità del tuo Paese.</p>

<h2 id="website">11. Questo sito</h2>
<p>coffeebeansstudio.eu è un sito statico. Non usa <strong>né cookie, né strumenti di analisi, né font o script di terze parti</strong>. È ospitato su <strong>GitHub Pages</strong> (GitHub, Inc.) e il servizio DNS del dominio è fornito da <strong>Cloudflare</strong>. Questi fornitori possono trattare il tuo indirizzo IP e i dati tecnici delle richieste nei log dei server, per la sicurezza e per l’erogazione del sito. Consulta l’<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">Informativa sulla privacy di GitHub</a> e l’<a href="https://www.cloudflare.com/privacypolicy/" rel="noopener">Informativa sulla privacy di Cloudflare</a>.</p>

<h2 id="changes">12. Modifiche</h2>
<p>Se l’app inizierà a fare qualcosa di nuovo con i dati — ad esempio una nuova rete pubblicitaria o strumenti di analisi — aggiorneremo questa pagina prima che la modifica arrivi nell’app e cambieremo la data qui sotto.</p>
""",
    # terms
    t_title="Termini di utilizzo — Coffee Beans Studio",
    t_desc="Termini brevi e onesti per Koselig e gli altri giochi di Coffee Beans Studio.",
    t_h1="Termini di utilizzo",
    t_sub="Koselig e gli altri giochi di Coffee Beans Studio",
    terms_html="""
<p class="note">La versione vincolante è quella <a href="{R}terms/">inglese</a>; questa è una traduzione per comodità.</p>
<p>Questi termini si applicano quando usi <strong>Koselig</strong> o un altro gioco di <strong>Coffee Beans Studio</strong> (Dzmitry Kurtsikau, Polonia). Giocando, li accetti. Sono brevi di proposito.</p>

<h2>1. Il gioco</h2>
<p>Ti concediamo un diritto personale, non esclusivo e non trasferibile di installare i nostri giochi e di giocarci su dispositivi di tua proprietà o sotto il tuo controllo, per uso personale e non commerciale. Ti chiediamo di non copiare, rivendere, sottoporre a reverse engineering né ridistribuire il gioco o la sua grafica, salvo nei casi consentiti dalla legge.</p>

<h2>2. Gli store</h2>
<p>Scarichi i nostri giochi da Apple App Store o da Google Play, e si applicano anche i loro termini. Per le app scaricate da App Store, oltre a questi termini si applica il <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Contratto di licenza standard per l’utente finale</a> di Apple. Apple e Google non sono responsabili del gioco né dell’assistenza.</p>

<h2>3. Pubblicità e acquisto «Senza annunci»</h2>
<p>Koselig è gratuito. Può mostrare un breve video con premio quando chiedi il controllo <em>Bloccato?</em>. Gli annunci sono forniti da Google AdMob; non ne controlliamo il contenuto e non siamo responsabili dei prodotti di terzi che vi vengono pubblicizzati.</p>
<p>«Senza annunci» è un acquisto una tantum, non consumabile. Permette al controllo <em>Bloccato?</em> di funzionare senza video; il numero di controlli per livello resta lo stesso. Il prezzo viene indicato dallo store prima del pagamento. Pagamenti, rimborsi e annullamenti sono gestiti da Apple o da Google secondo le rispettive regole. L’acquisto è legato al tuo ID Apple o al tuo account Google e si può ripristinare dopo una reinstallazione (Impostazioni → <em>Ripristina</em>).</p>

<h2>4. I tuoi progressi</h2>
<p>I progressi sono salvati sul tuo dispositivo e, su iPhone, anche nel tuo iCloud personale. Se elimini l’app o perdi il dispositivo, non possiamo recuperarli; su iPhone possono tornare da iCloud.</p>

<h2>5. Modifiche e disponibilità</h2>
<p>Possiamo aggiornare il gioco — aggiungere, modificare o rimuovere livelli e funzioni — e possiamo smettere di offrirlo. Cercheremo di mantenerlo funzionante, ma non possiamo promettere che sarà sempre disponibile o privo di bug.</p>

<h2>6. Responsabilità</h2>
<p>Il gioco è fornito «così com’è». Nei limiti consentiti dalla legge, non siamo responsabili di danni indiretti o della perdita di dati. Nulla in questi termini limita la responsabilità che per legge non può essere limitata, né i tuoi diritti di consumatore previsti dalle leggi del tuo Paese.</p>

<h2>7. Legge applicabile</h2>
<p>Questi termini sono regolati dalla legge polacca. Se sei un consumatore, conservi anche la tutela delle norme imperative del Paese in cui vivi.</p>

<h2>8. Contatti</h2>
<p>Domande o reclami: <a href="mailto:{EMAIL}">{EMAIL}</a>. Come trattiamo i dati è spiegato nell’<a href="{R}it/privacy/">Informativa sulla privacy</a>.</p>
""",
    # support
    s_title="Assistenza — Coffee Beans Studio",
    s_desc="Aiuto con Koselig: ripristinare l’acquisto «Senza annunci», ricominciare un livello, cambiare lingua, consenso agli annunci ed eliminazione dei dati.",
    s_h1="Assistenza",
    s_sub="Leggiamo ogni messaggio",
    s_mail_h="Scrivici",
    s_mail_p="Indicaci il modello del telefono, la versione del gioco e che cosa è successo. Uno screenshot aiuta molto.",
    s_faq_h="Domande",
    faq=[
        ("Come ripristino l’acquisto «Senza annunci»?",
         "Tocca ☰ in alto a destra per aprire le Impostazioni, poi tocca <em>Ripristina</em> accanto a <em>Senza annunci</em>. Usa lo stesso ID Apple o account Google con cui l’hai acquistato. Il gioco verifica l’acquisto presso lo store a ogni avvio, quindi dopo una reinstallazione si ripristina anche da solo, appena lo store risponde."),
        ("Come ricomincio un livello?",
         "Apri Impostazioni e tocca <em>Ricomincia da capo</em>, poi tocca di nuovo per confermare. Così il livello in corso riparte da zero. Per cancellare tutto — tutti i progressi e le impostazioni — elimina l’app."),
        ("Come cambio lingua?",
         "Impostazioni → <em>Lingua</em>. Le lingue di Koselig sono Italiano, English, Español, Deutsch, Français, Polski e Русский. <em>Di sistema</em> segue la lingua del telefono."),
        ("Quando il gioco mostra annunci?",
         "Solo quando tocchi <em>Bloccato?</em> e scegli <em>Guarda il video</em>. Niente banner e niente annunci pop-up. Con <em>Senza annunci</em> il controllo funziona subito."),
        ("Come cambio il consenso agli annunci?",
         "In Impostazioni, tocca <em>Modifica</em> accanto a <em>Annunci e dati</em>: si riapre il modulo di consenso di Google. La voce compare nelle regioni in cui si applicano le regole sul consenso."),
        ("Posso salvare una disposizione e tornarci più tardi?",
         "Sì. In Impostazioni, <em>Salvataggi</em> ha tre slot: <em>Salva</em> memorizza la disposizione attuale, <em>Apri</em> la ricarica."),
    ],
    s_del_h="Eliminare i tuoi dati",
    s_del_p="Koselig non ha account. I progressi sono salvati sul dispositivo e, su iPhone, anche nel tuo iCloud. Eliminando l’app elimini tutto ciò che aveva salvato sul dispositivo. Per i dati pubblicitari, di analisi e iCloud vedi la <a href=\"{R}it/koselig/delete-data/\">pagina sull’eliminazione dei dati</a>.",
    # delete data
    d_title="Elimina i tuoi dati — Koselig",
    d_desc="Come eliminare i dati del gioco Koselig: elimina l’app; la copia in iCloud è gestita da Apple, i dati pubblicitari da Google.",
    d_h1="Elimina i tuoi dati",
    d_sub="Koselig di Coffee Beans Studio",
    delete_html="""
<p><strong>Koselig</strong> non ha account, quindi non c’è nessun account da eliminare. Non conserviamo i tuoi progressi sui nostri server.</p>

<h2>Dati sul tuo dispositivo</h2>
<p>Progressi, salvataggi, impostazioni, stato dell’acquisto «Senza annunci» e la tua scelta sul consenso pubblicitario sono salvati sul tuo telefono. <strong>Per eliminare tutto, elimina l’app</strong>:</p>
<ul>
<li><strong>iPhone:</strong> tieni premuta l’icona di Koselig → <em>Rimuovi app</em> → <em>Elimina app</em>.</li>
<li><strong>Android:</strong> tieni premuta l’icona di Koselig → <em>Informazioni app</em> → <em>Disinstalla</em> (oppure <em>Spazio di archiviazione → Cancella spazio di archiviazione</em> per tenere l’app ma cancellarne i dati).</li>
</ul>
<p>Eliminare l’app non annulla né rimuove l’acquisto «Senza annunci»: appartiene al tuo ID Apple o al tuo account Google e puoi ripristinarlo in seguito.</p>

<h2>Copia in iCloud (iPhone)</h2>
<p>Su iPhone progressi e salvataggi vengono anche copiati nel tuo iCloud personale. La conserva Apple con il tuo ID Apple. Per interromperla, disattiva iCloud per Koselig: <em>Impostazioni → [il tuo nome] → iCloud</em>.</p>
<h2>Analisi e segnalazioni degli arresti anomali</h2>
<p>Gli eventi di analisi e le segnalazioni degli arresti anomali (Google Firebase) non sono collegati al tuo nome o alla tua email, quindi non possiamo trovare i dati di una singola persona. Vengono cancellati automaticamente: gli eventi di analisi entro 14 mesi, le segnalazioni degli arresti anomali dopo 90 giorni.</p>
<h2>Dati pubblicitari</h2>
<p>Gli annunci in Koselig sono forniti da Google AdMob. I dati raccolti da Google sono sotto il controllo di Google. Puoi:</p>
<ul>
<li>reimpostare o eliminare l’ID pubblicità di Android: <em>Impostazioni → Google → Annunci</em>;</li>
<li>cambiare il consenso nel gioco: <em>Impostazioni → Annunci e dati</em>;</li>
<li>gestire o eliminare i dati nel tuo account Google: <a href="https://myadcenter.google.com/" rel="noopener">Il mio Centro annunci</a> e <a href="https://myaccount.google.com/data-and-privacy" rel="noopener">Dati e privacy di Google</a>;</li>
<li>leggere come Google usa i dati delle app: <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">policies.google.com</a>.</li>
</ul>

<h2>Email che ci hai inviato</h2>
<p>Se ci hai scritto e vuoi che i tuoi messaggi vengano eliminati, invia una richiesta a <a href="mailto:{EMAIL}?subject=Delete%20my%20data">{EMAIL}</a> dallo stesso indirizzo. Li elimineremo entro 30 giorni e te lo confermeremo.</p>
<p>Maggiori dettagli: <a href="{R}it/koselig/privacy/">Informativa sulla privacy</a>.</p>
""",
    nf_title="Pagina non trovata — Coffee Beans Studio",
    nf_h1="Questa pagina si è spenta come una candela",
    nf_p="Forse l’indirizzo è sbagliato, o la pagina è stata spostata.",
    nf_cta="Torna allo studio",
)
