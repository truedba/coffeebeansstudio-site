// Coffee Beans Studio — всё живое страницы. Правило владельца: движение живёт, только пока на него смотрят.
// Таймеров нет вовсе: параллакс считается в requestAnimationFrame ТОЛЬКО в ответ на прокрутку
// (вкладка в фоне не прокручивается — значит, ни такта), смена тона фона и цветение бонсая — IntersectionObserver.
(() => {
  const body = document.body;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');

  // свёрнутая вкладка: CSS-анимации на паузу
  document.addEventListener('visibilitychange', () => body.classList.toggle('paused', document.hidden));

  // тон фона по сцене, которая занимает середину экрана
  const scenes = document.querySelectorAll('[data-scene]');
  if (scenes.length) {
    const io = new IntersectionObserver((es) => {
      for (const e of es) if (e.isIntersecting) body.dataset.scene = e.target.dataset.scene;
    }, { rootMargin: '-45% 0px -45% 0px' });
    scenes.forEach((s) => io.observe(s));
  }

  // шапка становится плотной, когда первый экран ушёл
  const top = document.querySelector('[data-top]');
  const hero = document.querySelector('.hero, .k-hero');
  if (top && hero) {
    new IntersectionObserver(([e]) => top.classList.toggle('solid', !e.isIntersecting), { rootMargin: '-72px 0px 0px 0px' }).observe(hero);
  }

  // бонсай зацветает, когда его видно (как в игре после сборки) — один раз
  const bonsai = document.querySelector('.bonsai');
  if (bonsai) {
    const bo = new IntersectionObserver(([e]) => { if (e.isIntersecting) { bonsai.classList.add('in'); bo.disconnect(); } }, { threshold: 0.6 });
    bo.observe(bonsai);
  }

  // параллакс картинок сцен: только видимые, только по прокрутке
  const layers = [...document.querySelectorAll('.scene-img img, .word-img img, .finale-img img')];
  if (!layers.length) return;
  // наблюдаем секции, двигаем их картинки
  const secOf = new Map(layers.map((l) => [l.closest('section'), l]));
  const vis = new Set();
  const so = new IntersectionObserver((es) => es.forEach((e) => e.isIntersecting ? vis.add(e.target) : vis.delete(e.target)));
  secOf.forEach((_, s) => so.observe(s));
  let queued = false;
  const step = () => {
    queued = false;
    if (reduce.matches || document.hidden) return;
    const vh = innerHeight;
    vis.forEach((s) => {
      const r = s.getBoundingClientRect();
      const k = (r.top + r.height / 2 - vh / 2) / (vh + r.height); // -0.5…0.5
      secOf.get(s).style.transform = `translate3d(0, ${(k * -12).toFixed(2)}%, 0)`;
    });
  };
  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(step); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  onScroll();
})();
