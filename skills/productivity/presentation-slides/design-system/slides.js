(function () {
  var manifest;
  var selected = 'title';
  fetch('../slide-templates/template-manifest.json').then(function (r) { return r.json(); }).then(function (data) { manifest = data; });
  function record() { return (manifest && manifest.layouts || []).find(function (item) { return item.id === selected; }); }
  function update() {
    var item = record(); if (!item) return;
    document.querySelector('#layout-name').textContent = item.label;
    document.querySelectorAll('.layout-option').forEach(function (b) { b.setAttribute('aria-selected', b.dataset.layout === selected); });
    document.querySelectorAll('.inspect-preview .thumb-stage').forEach(function (stage) { stage.hidden = stage.id !== 'inspect-' + selected; });
    document.querySelector('#layout-actions').hidden = true;
    document.querySelector('#apply-layout').textContent = 'Apply ' + item.label + ' layout';
    fitStages();
  }
  function fitStages() {
    document.querySelectorAll('.inspect-preview .thumb-stage').forEach(function (stage) {
      if (stage.hidden) return;
      var frame = stage.parentElement.getBoundingClientRect();
      var scale = Math.min(frame.width / 1920, frame.height / 1080);
      stage.style.transform = 'translate(-50%, -50%) scale(' + scale + ')';
    });
    document.querySelectorAll('.thumb .thumb-stage').forEach(function (stage) {
      var frame = stage.parentElement.getBoundingClientRect();
      var scale = Math.min(frame.width / 1920, frame.height / 1080);
      stage.style.transform = 'translate(-50%, -50%) scale(' + scale + ')';
    });
  }
  document.querySelectorAll('.layout-option').forEach(function (b) { b.addEventListener('click', function () { selected = b.dataset.layout; update(); }); });
  document.querySelector('#apply-layout').addEventListener('click', function () { document.querySelector('#layout-actions').hidden = false; document.querySelector('#layout-status').textContent = 'Outputs ready for ' + record().label + '.'; });
  document.querySelector('#copy-contract').addEventListener('click', function () { navigator.clipboard.writeText(JSON.stringify(record(), null, 2)); document.querySelector('#layout-status').textContent = 'Contract copied.'; });
  document.querySelector('#download-starter').addEventListener('click', function () { var a = document.createElement('a'); a.href = '../slide-templates/starters/' + selected + '.html'; a.download = 'bil-' + selected + '-starter.html'; a.click(); document.querySelector('#layout-status').textContent = 'Starter download requested.'; });
  window.addEventListener('resize', fitStages);
  var ready = window.setInterval(function () { if (manifest) { window.clearInterval(ready); update(); } }, 20);
}());
