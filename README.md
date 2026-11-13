# coffeebeansstudio.eu — сайт студии Coffee Beans Studio

**Цель одной фразой:** дать человеку, который нашёл Koselig в магазине (или магазину, который проверяет разработчика), тёплое
первое впечатление о студии и честные ответы — что за игра, что она делает с данными, куда писать.
**Правило отбора текста:** фраза проходит, только если её можно проверить в коде игры (`~/lotok/game`) или в магазине.

- Прод: https://coffeebeansstudio.eu (GitHub Pages, ветка `main`, папка `/docs`, файл `docs/CNAME`)
- Репозиторий: https://github.com/truedba/coffeebeansstudio-site · локально `~/coffeebeansstudio-site`
- Обязательные адреса для магазинов: `/privacy/`, `/koselig/privacy/`, `/terms/`, `/support/`, `/koselig/delete-data/`,
  `/app-ads.txt` (строка AdMob `pub-8167533003532456`). Те же страницы на `/es/…`, `/de/…`, `/fr/…`, `/it/…`, `/pl/…`, `/ru/…` (переводы, обязывает английская).

## Сборка
```
python3 build.py          # картинки (если их нет) + страницы → docs/, в конце проверка ссылок: 0 цело · 1 битые · 2 нет исходников
python3 build.py --pages  # только страницы
python3 build.py --podlog # самопроверка стража безопасности: 6 подлогов в копию docs/, каждый назван своей строкой (условие: 6 из 6)
```
Проверка после сборки — ссылки И **страж безопасности** (`BEZOPASNOST.md`: CSP без unsafe-inline, Referrer-Policy, нет
style=/встроенных скриптов/голых адресов/внешних ресурсов, security.txt не просрочен). Почта на страницах собирается в `site.js`
из `data-u/data-d/data-t` — в HTML адреса нет. Заголовки живого сайта: `python3 ~/tooling/web-headers/webheaders.py URL`.
Тексты — `content.py` (7 языков, как в игре: en es de fr it pl ru; порядок — `LANGS` в `build.py`), вёрстка — `src/site.css`, `src/site.js`, шаблоны — функции `page_*` в `build.py`.
Картинки-исходники в `src/img/` в git не лежат (сотни МБ): откуда они —
- кадры Nano Banana 4K: `~/lotok/game/assets/sait/*.png`, промпты — `~/lotok/art/NB_SAIT.tsv`, учёт — `~/lotok/art/GEN-LEDGER.md`;
- бонсай и логотип с пурпура: `bash ~/tooling/claude-rig/rig.sh prep_key.py <src> <out> [--no-crop]` (розовые лепестки сохраняются);
- иконка и заставка игры: `~/lotok/game/assets/icon.png`, `nb/zs_fon_a.png`;
- кадры игры 1170×2084 (англ.): `SHOT_TOLKO=yazyki SHOT_YAZYKI=en … engine.sh run --resolution 1170x2532 --script tools/shot.gd` в `~/lotok/game`.
OG-картинки: `src/og.html` + `work/og.mjs` (Playwright, Chrome) → `docs/assets/og-*.jpg`.

## Языки
Семь — ровно языки игры. Названия кнопок и терминов (Тупик?/Stuck?/¿Atascado?/Sackgasse?/Impasse ?/Bloccato?, «Без рекламы»,
Настройки, Позиции, материалы столов, лотков и фигур) берутся из `~/lotok/tools/teksty_gen.py` — единого источника строк игры:
сайт обязан называть то, что игрок видит на экране. Правовые страницы переводятся без изменения смысла; на каждой — пометка,
что обязывает английская версия. Новый язык: словарь `L["xx"]` в `content.py` с теми же ключами, что `L["en"]` (включая
`lang_label`), + `LANGS` и `og:locale` в `build.py`. Переключатель — `<details class="langs">` (не встаёт строкой в шапку
телефона 390 px); без JS раскрывается сам, `site.js` только закрывает его по клику мимо и Esc.
Кадр с раскрытым меню: `node ~/tooling/web-shot/webshot.mjs shot URL out.png 390 844 --click='.langs summary'`.

## Проверки
Глобальный предмет **web-shot** (`~/tooling/web-shot`, ID `web-shot`, граф: `python3 ~/tooling/graph.py show web-shot`):
- `node ~/tooling/web-shot/webshot.mjs shot URL out.png 390 844 --full` — кадр страницы;
- `… weight URL 390 844` — вес; `… idle URL 1440 900` — страница замирает (код 1 «ЖИВЁТ В ПОКОЕ» — нельзя выкладывать);
- до переключения DNS: `PAGES_IP=185.199.108.153 node … shot http://coffeebeansstudio.eu/ out.png`;
- Lighthouse: `npx lighthouse@12.2.1 URL --only-categories=performance,accessibility,best-practices,seo`.
`work/` (не в git) — черновики, из которых вынесен web-shot; OG-картинки — `work/og.mjs` + `src/og.html`.

## Движение (правило владельца: живёт, только пока смотрят)
Одно оркестрованное движение — открытие кадра на первом экране (шторки + наезд, конечные). Таймеров нет; параллакс — rAF только по
событию прокрутки; `visibilitychange` ставит CSS на паузу; `prefers-reduced-motion` убирает всё движение.

## Откуда факты политики (сверено 12.11.2026)
- реклама: `game/scripts/reklama.gd`, `reklama_poing.gd` (только rewarded, UMP до запуска SDK, ролик грузится заранее);
  `foundation/ads/ad_service_v2.gd` + `addons/admob/src/utils/AdMobSettings.gd`: `is_for_child_directed_treatment=false`, `max_ad_content_rating=PG`;
- адаптеры медиации Meta/AppLovin есть в Android-сборке (`addons/admob/admob_export_plugin.gd`), в AdMob не включены (BACKLOG P2);
- Firebase: плагины закомментированы (`android/overlay/build.gradle`), аналитика — заглушка `DummyAnalytics`;
- iOS: нет `NSUserTrackingUsageDescription` → ATT не спрашивается; `PrivacyInfo.xcprivacy`: `NSPrivacyTracking=false`;
- покупка: `scripts/pokupka.gd`, товар `koselig.no_ads`, состояние `user://pokupki.json`; сохранения `user://lotok.json`.
**Включили Firebase, медиацию или новую сеть — СНАЧАЛА правка `content.py` (раздел ads/no) и дата, потом сборка игры.**
