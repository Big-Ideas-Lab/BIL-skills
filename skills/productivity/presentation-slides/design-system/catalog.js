(function () {
  function replay(name) {
    var stage = document.querySelector('[data-motion="' + name + '"]');
    if (!stage) return;
    stage.classList.remove('play');
    void stage.offsetWidth;
    stage.classList.add('play');
  }
  var bookmarks = document.querySelectorAll('.bookmark-strip a[href^="#"]');
  var sections = Array.prototype.map.call(bookmarks, function (link) { return document.querySelector(link.getAttribute('href')); }).filter(Boolean);
  function setCurrent(id) { bookmarks.forEach(function (link) { link.toggleAttribute('aria-current', link.getAttribute('href') === '#' + id); }); }
  bookmarks.forEach(function (link) { link.addEventListener('click', function () { setCurrent(link.getAttribute('href').slice(1)); }); });
  if (window.location.hash) setCurrent(window.location.hash.slice(1));
  if ('IntersectionObserver' in window && sections.length) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) setCurrent(entry.target.id);
      });
    }, {rootMargin:'-18% 0px -65% 0px', threshold:0});
    sections.forEach(function (section) { observer.observe(section); });
  }
  document.querySelectorAll('[data-replay]').forEach(function (button) {
    button.addEventListener('click', function () { replay(button.dataset.replay); });
  });
  function legacyCopy(text) {
    var area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.top = '-1000px';
    document.body.appendChild(area);
    area.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (error) { ok = false; }
    document.body.removeChild(area);
    return ok;
  }
  function copyText(button, text, label) {
    var status = button.parentNode.querySelector('.copy-status');
    function settle(ok) {
      button.textContent = ok ? 'Copied' : 'Select and copy';
      if (status) status.textContent = ok ? 'Copied to clipboard' : 'Automatic copy is blocked here - the path is selectable above';
      setTimeout(function () { button.textContent = label; if (status) status.textContent = ''; }, 2200);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { settle(true); }, function () { settle(legacyCopy(text)); });
    } else {
      settle(legacyCopy(text));
    }
  }
  document.querySelectorAll('[data-copy]').forEach(function (button) {
    button.addEventListener('click', function () {
      var source = document.querySelector(button.dataset.copy);
      copyText(button, source.value || source.textContent, 'Copy HTML');
    });
  });
  document.querySelectorAll('[data-copy-text]').forEach(function (button) {
    button.addEventListener('click', function () { copyText(button, button.dataset.copyText, 'Copy agent instruction'); });
  });
  document.querySelectorAll('.component-card .fragment').forEach(function (fragment) {
    var details = document.createElement('details');
    var summary = document.createElement('summary');
    summary.textContent = 'View HTML';
    details.appendChild(summary);
    fragment.parentNode.insertBefore(details, fragment);
    details.appendChild(fragment);
  });
  document.querySelectorAll('[data-page-turner-demo]').forEach(function (nav) {
    var current = Math.max(1, parseInt(nav.dataset.current, 10) || 1);
    var total = Math.max(current, parseInt(nav.dataset.total, 10) || current);
    var previous = nav.querySelector('[data-page-previous]');
    var next = nav.querySelector('[data-page-next]');
    var output = nav.querySelector('.bil-page-tracker');
    function render() { output.textContent = current + ' / ' + total; output.setAttribute('aria-label', 'Page ' + current + ' of ' + total); previous.disabled = current === 1; next.disabled = current === total; }
    previous.addEventListener('click', function () { if (current > 1) { current -= 1; render(); } });
    next.addEventListener('click', function () { if (current < total) { current += 1; render(); } });
    render();
  });
}());
