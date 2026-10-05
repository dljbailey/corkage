'use strict';
(() => {
  const form = document.querySelector('#filters');
  if (!form) return;
  const grid = document.querySelector('#restaurant-grid');
  const dialog = document.querySelector('#restaurant-dialog');
  const content = document.querySelector('#detail-content');
  const fields = Object.fromEntries(['search', 'area', 'scope', 'sort', 'free'].map(id => [id, document.getElementById(id)]));
  const labels = { public: 'Public dining', events: 'Private / group events', members: 'Members only', discretion: 'Ask management first', clarify: 'Policy needs clarification' };
  let records = [];
  let lastOpener = null;
  const escape = value => String(value).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const safeLink = value => { const u = new URL(value, location.href); if (u.protocol !== 'https:') throw new Error('Unsafe source URL'); return escape(u.href); };
  const normalise = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function updateURL(restaurant) {
    const url = new URL(location.href);
    for (const [key, value, fallback] of [['q', fields.search.value, ''], ['area', fields.area.value, 'all'], ['scope', fields.scope.value, 'public'], ['sort', fields.sort.value, 'name'], ['free', fields.free.checked ? '1' : '', '']]) {
      if (value === fallback) url.searchParams.delete(key); else url.searchParams.set(key, value);
    }
    if (restaurant) url.searchParams.set('restaurant', restaurant); else url.searchParams.delete('restaurant');
    history.replaceState(null, '', url);
  }
  function render() {
    const query = normalise(fields.search.value.trim());
    const matches = records.filter(r => (fields.area.value === 'all' || r.area === fields.area.value) && (fields.scope.value === 'all' || r.scope === fields.scope.value) && (!fields.free.checked || Boolean(r.freeOffer)) && normalise([r.name, r.neighbourhood, r.cuisine].join(' ')).includes(query));
    matches.sort((a, b) => (fields.sort.value === 'area' ? a.area.localeCompare(b.area) : 0) || a.name.localeCompare(b.name, 'en'));
    const positions = new Map(matches.map((r, i) => [r.id, i]));
    const cards = [...grid.children].sort((a, b) => (positions.get(a.dataset.id) ?? Infinity) - (positions.get(b.dataset.id) ?? Infinity));
    for (const card of cards) { card.hidden = !positions.has(card.dataset.id); grid.append(card); }
    document.querySelector('#result-count').textContent = `${matches.length} ${matches.length === 1 ? 'restaurant' : 'restaurants'} · ${fields.scope.value === 'all' ? 'all arrangements' : labels[fields.scope.value].toLowerCase()}`;
    document.querySelector('#empty').hidden = matches.length > 0;
    document.querySelector('#scope-note').textContent = fields.scope.value === 'public' ? 'Public dining includes day-specific offers and conditions. See each policy before booking.' : 'Special arrangements are not general BYO permission. Check the scope and contact the restaurant before bringing wine.';
    updateURL(dialog.open ? dialog.dataset.restaurant : null);
  }
  function openRestaurant(id, opener) {
    const r = records.find(item => item.id === id);
    if (!r) return;
    lastOpener = opener || document.querySelector('#search');
    content.innerHTML = `<p class="eyebrow">${escape(r.neighbourhood)} · ${escape(r.area)} London</p><h2 id="detail-title">${escape(r.name)}</h2><p class="cuisine">${escape(r.cuisine)}</p><span class="status ${r.scope === 'public' ? '' : 'special'}">${escape(labels[r.scope])}</span><p class="detail-fee">${escape(r.fee)}</p><div class="detail-policy"><p>${escape(r.policy)}</p></div><div class="detail-source"><a class="button small" href="${safeLink(r.website)}" target="_blank" rel="noopener noreferrer">Restaurant website ↗</a><a class="text-link" href="${safeLink(r.source)}" target="_blank" rel="noopener noreferrer">Read the official policy source ↗</a><span>Source checked 13 September 2026</span></div><p class="small-note">Website evidence, not a personal confirmation. Source links may open a PDF. Rates and availability can change; agree the full charge before your visit.</p><section class="detail-section"><h3>A bottle to consider</h3>${r.pairings.length ? `<ul>${r.pairings.map(p => `<li>${escape(p)}</li>`).join('')}</ul><p class="small-note">Editorial wine-style suggestions, conditional on the menu you choose. Not restaurant recommendations or merchant stock.</p>` : '<p>We have not verified enough menu detail to suggest a pairing. Ask the restaurant about the current food before choosing your bottle.</p>'}</section><section class="detail-section"><h3>Wine shops to plan around</h3><p class="small-note">Wider-area options, not a nearest-shop ranking. Some require a separate journey. Check current hours, branch stock and collection before travelling.</p><ul class="merchant-list">${r.merchants.map(m => `<li><a href="${safeLink(m.url)}" target="_blank" rel="noopener noreferrer">${escape(m.name)} ↗</a><br>${escape(m.address)}</li>`).join('')}</ul></section><section class="detail-section"><a class="text-link" href="policies.html#${escape(r.id)}">Open the text policy listing →</a></section>`;
    dialog.dataset.restaurant = id;
    if (!dialog.open) dialog.showModal();
    document.body.classList.add('dialog-open');
    dialog.scrollTop = 0;
    updateURL(id);
  }
  dialog.querySelector('.close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', e => { if (e.target === dialog) { const rect = dialog.getBoundingClientRect(); if (e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom) dialog.close(); } });
  dialog.addEventListener('close', () => { document.body.classList.remove('dialog-open'); updateURL(); if (lastOpener?.isConnected && !lastOpener.closest('[hidden]')) lastOpener.focus({ preventScroll: true }); });
  grid.addEventListener('click', e => { const button = e.target.closest('[data-restaurant]'); if (button) openRestaurant(button.dataset.restaurant, button); });
  form.addEventListener('submit', e => e.preventDefault());
  form.addEventListener('input', render);
  form.addEventListener('change', render);
  form.addEventListener('reset', () => setTimeout(render, 0));
  document.querySelector('#clear-search').addEventListener('click', () => { form.reset(); fields.search.focus(); });
  function readURL() {
    const params = new URLSearchParams(location.search);
    fields.search.value = params.get('q') || '';
    for (const [key, fallback] of [['area', 'all'], ['scope', 'public'], ['sort', 'name']]) fields[key].value = [...fields[key].options].some(o => o.value === params.get(key)) ? params.get(key) : fallback;
    fields.free.checked = params.get('free') === '1';
    const id = params.get('restaurant');
    render();
    if (id) openRestaurant(id);
  }
  fetch('data.json').then(response => { if (!response.ok) throw new Error('Data unavailable'); return response.json(); }).then(data => {
    if (!Array.isArray(data) || data.length !== 42) throw new Error('Invalid directory');
    records = data;
    for (const button of grid.querySelectorAll('button')) button.disabled = false;
    readURL();
    document.documentElement.dataset.directoryReady = 'true';
    window.addEventListener('popstate', readURL);
  }).catch(() => {
    document.querySelector('#result-count').textContent = 'Interactive details could not load. Use the complete text policy list below.';
    form.hidden = true;
    for (const card of grid.children) card.hidden = false;
    document.querySelector('#scope-note').textContent = 'All arrangements shown below. Special-scope listings are not general BYO permission.';
    const fallback = document.createElement('p'); fallback.innerHTML = '<a class="button" href="policies.html">Read all restaurant policies →</a>'; grid.before(fallback);
    for (const button of grid.querySelectorAll('button')) { const link = document.createElement('a'); link.href = `policies.html#${button.dataset.restaurant}`; link.className = 'card-open'; link.textContent = button.textContent; button.replaceWith(link); }
  });
})();
