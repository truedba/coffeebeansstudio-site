# Безопасность coffeebeansstudio.eu

Задача заказчика (13.11.2026): «чтобы никто не смог его взломать и спамить остальных; всё было максимально безопасно».
Сайт статический (GitHub Pages), форм, логинов и бэкенда нет — поэтому «взлом» здесь означает три вещи:
перехват домена/аккаунтов, подделка писем от нашего имени и подмена содержимого по дороге к читателю.

## Угрозы и меры

| Угроза | Чем закрыта | Где |
|---|---|---|
| Перехват домена GitHub Pages (чужой репозиторий публикуется на наш домен, если наш отвязан) | подтверждение домена на аккаунте truedba: TXT `_github-pages-challenge-truedba` | GitHub Settings → Pages → Add a domain; TXT в Cloudflare |
| Подмена репозитория: force-push, удаление `main` | ruleset «main: без удаления и force-push» (id 27192336), Actions выключены, Dependabot alerts + security updates, secret scanning + push protection, private vulnerability reporting | GitHub, сделано 13.11 |
| Спам «от support@coffeebeansstudio.eu» | SPF `-all`, DKIM (есть, `cf2024-1`), DMARC `p=reject` + `sp=reject` — домен ничего не отправляет, любое письмо «от нас» законно отвергается | Cloudflare DNS (список ниже) |
| Сбор нашей почты ботами | в HTML адреса нет: части в `data-u/data-d/data-t`, собирает `site.js`; без JS — «support [at] … [dot] eu» + ссылка на страницу поддержки; из JSON-LD адрес убран; страж `build.py` — «ГОЛЫЙ АДРЕС ПОЧТЫ» | `build.py` (`mail_link`), `src/site.js` |
| XSS / внедрение скрипта | CSP `default-src 'none'; script-src 'self'; style-src 'self'; …; base-uri 'none'; form-action 'none'` без `unsafe-inline`; style-атрибуты и встроенные скрипты запрещены стражем | `<meta http-equiv>` на каждой странице; тот же CSP заголовком у Cloudflare |
| Кликджекинг (сайт в чужом iframe) | `frame-ancestors 'none'` + `X-Frame-Options: DENY` заголовком (в `<meta>` не действуют); запасной путь — `site.js` выводит из фрейма | Cloudflare Transform Rule |
| MITM, подмена по дороге | HTTPS (сертификат GitHub, выпуск ждём), Always Use HTTPS, HSTS, TLS ≥ 1.2, `upgrade-insecure-requests` в CSP после выпуска | GitHub (enforce HTTPS), Cloudflare |
| Подмена DNS-ответов | DNSSEC (Cloudflare подписывает, DS у реестра через OVH) | Cloudflare + OVH |
| Выпуск сертификата чужим УЦ | CAA: только Let's Encrypt (GitHub) и УЦ Cloudflare, `iodef` на support@ | Cloudflare DNS |
| Захват аккаунтов GitHub / Cloudflare / OVH / Google | 2FA приложением или passkey, резервные коды — PDF `Bezopasnost_2FA.pdf`; OVH: transfer lock | заказчик, по PDF |
| Поставка (чужие CDN, шрифты, скрипты) | всё self-hosted: шрифты, CSS, JS, картинки в репозитории; страж — «ВНЕШНИЙ РЕСУРС» | `build.py` check |
| DoS | GitHub Pages за Fastly; после прокси — Cloudflare, rate limiting (1 правило бесплатно) | Cloudflare |
| Кто и куда сообщать о дыре | `/.well-known/security.txt` (RFC 9116), срок до 2027-11-01, просрочка ловится стражем | `build.py` |
| Утечка адресов переходов | `Referrer-Policy: no-referrer` (meta + заголовок) | `build.py`, Cloudflare |

**Страж в сборке:** `python3 build.py` после каждой сборки проверяет ссылки И безопасность (CSP на каждой странице и без
`unsafe-inline`, Referrer-Policy, нет `style=`/`on*=`/встроенных скриптов, нет голых адресов, нет внешних ресурсов, security.txt
целый и не просрочен); нарушение → код 1 со строкой класса. **Самопроверка:** `python3 build.py --podlog` подкладывает 6 подлогов
в копию `docs/` и требует, чтобы каждый был назван СВОЕЙ строкой (6 из 6 — условие). Заголовки живого сайта: глобальный предмет
`web-headers` (`python3 ~/tooling/web-headers/webheaders.py https://coffeebeansstudio.eu/`).

Чего НЕ делаем и почему: `upgrade-insecure-requests` в CSP пока не стоит — до выпуска сертификата он сломал бы загрузку
ресурсов по http. Bot Fight Mode — см. риск в п. 10.

## Что делает заказчик в дашбордах (по порядку)

Статус ДО (замер 13.11, `dig @1.1.1.1`): SPF `~all`, DMARC нет, CAA нет, DS нет, DNSSEC выключен, HTTPS не отвечает
(сертификат GitHub не выпущен), заголовков безопасности нет (только то, что отдаёт GitHub: `Access-Control-Allow-Origin: *`).

### Сейчас, не дожидаясь сертификата

**1. GitHub — подтвердить домен** (защита от перехвата; API для этого нет, только сайт).
GitHub → аватар → Settings → слева **Pages** → **Add a domain** → `coffeebeansstudio.eu` → **Add domain**.
GitHub покажет TXT: имя `_github-pages-challenge-truedba` и значение (случайная строка). Cloudflare → coffeebeansstudio.eu →
**DNS → Records → Add record**: Type `TXT`, Name `_github-pages-challenge-truedba`, Content — строка из GitHub, TTL Auto →
Save. Через 1–2 минуты в GitHub нажать **Verify**. Должно стать «Verified».

**2. Cloudflare DNS — DMARC** (DNS → Records → Add record):
Type `TXT` · Name `_dmarc` · Content:
`v=DMARC1; p=reject; sp=reject; adkim=s; aspf=s; rua=mailto:support@coffeebeansstudio.eu; fo=1`
Почему `reject`, а не `quarantine`: домен не отправляет писем вообще (Email Routing только принимает и пересылает; ответы идут
из Gmail от dikur86@gmail.com). Законного отправителя нет — значит, любое письмо «от @coffeebeansstudio.eu» подделка, и его
надо отвергать, а не класть в спам. Пересылку это не ломает: DMARC проверяется по домену в поле From ПИСЬМА ОТПРАВИТЕЛЯ
(gmail.com, outlook.com…), а не по нашему. `rua` — сводки приёмников, 1–2 письма в сутки, прилетят на support@ → Gmail.
Если когда-нибудь появится отправка от support@ (Gmail «send as» через SMTP) — сначала DKIM того сервиса, потом `p=`.

**3. Cloudflare DNS — SPF на `-all`:** открыть существующий TXT `v=spf1 include:_spf.mx.cloudflare.net ~all` → Edit →
`v=spf1 include:_spf.mx.cloudflare.net -all` → Save.
Не сломает ли пересылку: нет. Cloudflare Email Routing переписывает обратный адрес (SRS) на наш домен и отправляет со
своих серверов, которые и перечислены в `_spf.mx.cloudflare.net` — они проходят. `-all` бьёт только по чужим серверам.

**4. Cloudflare DNS — CAA** (три-четыре записи Add record, Type `CAA`):
- Tag `Only allow specific hostnames` (issue) · CA domain name `letsencrypt.org` — сертификаты GitHub Pages;
- issue `pki.goog` — Google Trust Services, его выдаёт Cloudflare для прокси;
- issue `ssl.com` и issue `sectigo.com` — запасные УЦ Cloudflare (Universal SSL может выбрать их);
- Tag `Send violation reports to URL` (iodef) · `mailto:support@coffeebeansstudio.eu`.
Flags 0. **`issuewild` не добавлять**: сертификат Cloudflare покрывает `*.coffeebeansstudio.eu`, запрет wildcard его сломает.

**5. Cloudflare — DNSSEC:** DNS → **Settings** → DNSSEC → **Enable DNSSEC**. Cloudflare покажет DS-запись: **Key Tag**,
**Algorithm** (13), **Digest Type** (2), **Digest**, и ниже **Public Key** (DNSKEY). Все четыре поля + ключ переписать (копировать).
OVH → **Web Cloud → Domain names → coffeebeansstudio.eu → вкладка DNSSEC** → Add a DNSSEC key (или «Manage DS records»):
Key Tag — из Cloudflare; Flag — `257 (KSK)`; Algorithm — `13 — ECDSAP256SHA256`; **Public key** — Public Key из Cloudflare
(OVH спрашивает ключ, не digest). Save. У EURid DS появится в течение часа–суток; Cloudflare в разделе DNSSEC напишет «Success».
Проверка: `dig +short DS coffeebeansstudio.eu @1.1.1.1` (должна появиться строка) и https://dnsviz.net/d/coffeebeansstudio.eu/.
Риск: если ввести ключ с ошибкой, домен перестанет резолвиться у проверяющих резолверов (~половина мира) — поэтому после
сохранения в OVH сразу смотреть dnsviz; при красном — удалить DS в OVH, резолвинг вернётся за TTL.

**6. Cloudflare — Email Routing:** Email → Email Routing → **Settings** (или Routing rules) → **Catch-all address** →
Action `Drop` → Save. Правило `support@ → dikur86@gmail.com` остаётся. Смысл: письма на выдуманные адреса (info@, admin@,
abuse-боты) не доходят до Gmail. Исключение, если захочется: добавить `postmaster@` и `abuse@` → тот же Gmail.

**7. OVH — замок переноса:** Web Cloud → Domain names → coffeebeansstudio.eu → **General information** → блок
**Protection against transfer** (Transfer lock) → Enable/Activate. Там же: **Anti-hijacking / Authorization code** не
запрашивать без нужды. Сам аккаунт OVH — 2FA по PDF.

### После того, как GitHub выпустит сертификат

Признак: `gh api repos/truedba/coffeebeansstudio-site/pages --jq .https_enforced` → `true` (фоновая проверка в сессии
включит его сама) или в GitHub → репозиторий → Settings → Pages галка **Enforce HTTPS** доступна и стоит.

**8. Cloudflare — прокси + TLS.** DNS → Records: у четырёх A-записей `@` и CNAME `www` переключить облако на оранжевое
(**Proxied**). Затем SSL/TLS → **Overview** → режим **Full (strict)**. Edge Certificates: **Always Use HTTPS** — On;
**Minimum TLS Version** — `TLS 1.2`; **TLS 1.3** — On; **Automatic HTTPS Rewrites** — On; **Opportunistic Encryption** — On.
Проверка через 10 минут: `gh api repos/truedba/coffeebeansstudio-site/pages/health --jq '.domain|{is_proxied,responds_to_https,https_error}'`
и `curl -sI https://coffeebeansstudio.eu/ | head -3` (должен быть `server: cloudflare`, 200).
Риск: Full (strict) требует, чтобы сертификат GitHub продлевался через прокси (Let's Encrypt приходит по http на
`/.well-known/acme-challenge/`). Если через ~60 дней `https_error` станет не null — переключить на **Full** (не strict):
связь браузер↔Cloudflare остаётся строгой, а Cloudflare↔GitHub проверяет шифрование, но не имя в сертификате.

**9. Cloudflare — HSTS.** SSL/TLS → Edge Certificates → **HSTS** → Enable → читаем предупреждение → Next:
Enable HSTS — On; **Max Age** — `6 months`; **Apply HSTS policy to subdomains** — On (у нас только www, тоже на прокси);
**Preload** — ВЫКЛ пока; **No-Sniff Header** — On (это X-Content-Type-Options). Save.
Preload — это список, зашитый в браузеры: попасть туда недели, выйти — месяцы, и всё это время любой поддомен без HTTPS
(в том числе будущие) будет недоступен. Включать preload через месяц работы HTTPS, с Max Age `12 months`, затем подать на
hstspreload.org. До этого — ничего не теряем: браузер запоминает HSTS после первого захода.

**10. Cloudflare — заголовки безопасности.** Rules → **Transform Rules** → **Modify Response Header** → Create rule:
имя `security headers`, When incoming requests match: **All incoming requests**. Then: **Set static** — по строке на заголовок:
- `Content-Security-Policy` = `default-src 'none'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; manifest-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'; upgrade-insecure-requests`
- `X-Frame-Options` = `DENY`
- `X-Content-Type-Options` = `nosniff`
- `Referrer-Policy` = `no-referrer`
- `Permissions-Policy` = `camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=(), browsing-topics=()`
- `Cross-Origin-Opener-Policy` = `same-origin`
Deploy. (Бесплатно до 10 правил; одно правило держит несколько заголовков.) Проверка: `python3 ~/tooling/web-headers/webheaders.py https://coffeebeansstudio.eu/` → оценка A.
После этого `upgrade-insecure-requests` можно добавить и в `CSP` в `build.py` — заголовок и meta должны совпадать.

**11. Cloudflare — rate limiting (DoS).** Security → **WAF → Rate limiting rules** → Create rule: имя `flood`,
If incoming requests match: Field `URI Path` · Operator `contains` · Value `/` ; With the same **IP**; Rate `100` requests per
`10` seconds; Then **Block** for `10 seconds` (на Free — фиксированно). Deploy. Обычному читателю 100 запросов за 10 с не
нужны (вся главная — ~40 запросов).

**Bot Fight Mode (Security → Bots) — НЕ включать без нужды.** Он выдаёт JS-проверку «подозрительным» клиентам, и на Free его
нельзя обойти правилом WAF. Под раздачу могут попасть робот Let's Encrypt (продление сертификата GitHub → п. 8 ломается) и
роботы магазинов, которые проверяют адрес политики конфиденциальности при ревью (Apple/Google). Для статического сайта за
Cloudflare выгода от него — нулевая; DoS закрывают прокси и п. 11. Если всё же включить — после этого проверить п. 8 через
две недели и перед каждой подачей в магазин.

### Через месяц
- HSTS: Max Age → 12 months, Preload → On, заявка на hstspreload.org.
- Cloudflare → Security → Events: посмотреть, не режет ли rate limiting настоящих людей.
- Письма `rua` DMARC на support@: если там нет чужих отправителей — всё работает; если есть — кто-то пробовал подделывать.
- `security.txt` живёт до 2027-11-01: за месяц до — поправить `SECURITY_EXPIRES` в `build.py` и пересобрать.
