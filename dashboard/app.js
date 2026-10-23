// MagangHub Batch 2 2026 - Main Application Logic
import { OVERALL_STATS, PROVINCES_DATA, SCATTER_POINTS, OPPORTUNITY_LISTINGS, METHODOLOGY_STEPS } from './data.js';

// Application State
const state = {
  currentMapMetric: 'postings', // 'postings', 'quota', 'applicants', 'ratio'
  selectedProvince: PROVINCES_DATA[0], // default DKI Jakarta
  scatterCategory: 'All', // 'All', 'BUMN', 'Tech', 'Government', 'Corporate'
  searchQuery: '',
  filterProvince: 'All',
  filterField: 'All',
  filterEducation: 'All',
  filterCompetition: 'All',
  sortBy: 'ratio-desc',
  page: 1,
  pageSize: 8,
  activeMethodologyIndex: 0
};

// DOM References
const elements = {
  // Stats
  statPostings: document.getElementById('stat-postings'),
  statPositions: document.getElementById('stat-positions'),
  statApplicants: document.getElementById('stat-applicants'),
  statRatio: document.getElementById('stat-ratio'),

  // Map
  mapMetricButtons: document.querySelectorAll('.map-metric-btn'),
  mapSvgContainer: document.getElementById('indonesia-map-container'),
  provinceDetailCard: document.getElementById('province-detail-card'),
  provinceLeaderboard: document.getElementById('province-leaderboard'),
  mapTooltip: document.getElementById('map-tooltip'),

  // Scatter Plot
  scatterSvg: document.getElementById('scatter-plot-svg'),
  scatterCategoryPills: document.querySelectorAll('.scatter-cat-pill'),
  chartTooltip: document.getElementById('chart-tooltip'),

  // Explorer
  searchInput: document.getElementById('explorer-search'),
  provinceSelect: document.getElementById('explorer-province'),
  fieldSelect: document.getElementById('explorer-field'),
  educationSelect: document.getElementById('explorer-education'),
  competitionSelect: document.getElementById('explorer-competition'),
  sortSelect: document.getElementById('explorer-sort'),
  resetFiltersBtn: document.getElementById('explorer-reset'),
  listingsContainer: document.getElementById('listings-container'),
  resultsCount: document.getElementById('explorer-results-count'),
  paginationContainer: document.getElementById('explorer-pagination'),

  // Modal
  modalBackdrop: document.getElementById('detail-modal'),
  modalTitle: document.getElementById('modal-title'),
  modalInstitution: document.getElementById('modal-institution'),
  modalBadge: document.getElementById('modal-badge'),
  modalLocation: document.getElementById('modal-location'),
  modalQuota: document.getElementById('modal-quota'),
  modalApplicants: document.getElementById('modal-applicants'),
  modalRatio: document.getElementById('modal-ratio'),
  modalWorkMode: document.getElementById('modal-workmode'),
  modalStipend: document.getElementById('modal-stipend'),
  modalDuration: document.getElementById('modal-duration'),
  modalMajors: document.getElementById('modal-majors'),
  modalDescription: document.getElementById('modal-description'),
  modalCloseBtn: document.getElementById('modal-close-btn'),

  // Methodology
  methodologyStepsContainer: document.getElementById('methodology-steps-container'),
  methodologyDetailContainer: document.getElementById('methodology-detail-container')
};

// Formatting utilities
function formatNumber(num) {
  return new Intl.NumberFormat('id-ID').format(num);
}

function formatRatio(num) {
  return `${num.toFixed(1)}×`;
}

// -------------------------------------------------------------
// 1. INITIALIZE HERO & OVERVIEW STATS
// -------------------------------------------------------------
function initOverviewStats() {
  if (elements.statPostings) elements.statPostings.textContent = formatNumber(OVERALL_STATS.postings);
  if (elements.statPositions) elements.statPositions.textContent = formatNumber(OVERALL_STATS.positions);
  if (elements.statApplicants) elements.statApplicants.textContent = "418K";
  if (elements.statRatio) elements.statRatio.textContent = `${OVERALL_STATS.competitionRatio}×`;
}

// -------------------------------------------------------------
// 2. INDONESIA MAP VISUALIZATION (SVG Choropleth)
// -------------------------------------------------------------
function getMetricValue(province, metric) {
  switch (metric) {
    case 'postings': return province.postings;
    case 'quota': return province.quota;
    case 'applicants': return province.applicants;
    case 'ratio': return province.ratio;
    default: return province.postings;
  }
}

function getMetricLabel(metric) {
  switch (metric) {
    case 'postings': return 'Lowongan';
    case 'quota': return 'Kuota (Kursi)';
    case 'applicants': return 'Pelamar';
    case 'ratio': return 'Competition Ratio';
    default: return 'Nilai';
  }
}

function getMetricColor(value, min, max, metric) {
  // Editorial restrained sequential slate scale
  const norm = Math.max(0, Math.min(1, (value - min) / (max - min || 1)));
  if (metric === 'ratio') {
    // Subtle rust tint for high competition
    if (norm > 0.8) return '#C2410C';
    if (norm > 0.6) return '#EA580C';
    if (norm > 0.4) return '#78716C';
    if (norm > 0.2) return '#A8A29E';
    return '#D6D3D1';
  } else {
    // Deep slate tones
    if (norm > 0.8) return '#1E293B';
    if (norm > 0.5) return '#334155';
    if (norm > 0.25) return '#64748B';
    if (norm > 0.1) return '#94A3B8';
    return '#CBD5E1';
  }
}

function renderIndonesiaMap() {
  const metric = state.currentMapMetric;
  const values = PROVINCES_DATA.map(p => getMetricValue(p, metric));
  const minVal = Math.min(...values);
  const maxVal = Math.max(...values);

  // SVG dimensions for Indonesia projection (approx aspect ratio 900x380)
  const svg = `
    <svg viewBox="0 0 940 400" class="w-full h-auto select-none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <pattern id="grid-pattern" width="30" height="30" patternUnits="userSpaceOnUse">
          <path d="M 30 0 L 0 0 0 30" fill="none" stroke="#F0EFEA" stroke-width="0.8"/>
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill="url(#grid-pattern)" />
      
      <!-- Coordinate Graticules Subtle -->
      <line x1="0" y1="200" x2="940" y2="200" stroke="#E7E5E4" stroke-dasharray="3,3" stroke-width="0.8"/>
      <text x="16" y="196" fill="#A8A29E" font-size="10" font-family="'JetBrains Mono', monospace">0° Equator</text>

      <!-- SUMATERA -->
      <g id="sumatera-group" class="map-island-group">
        <!-- Aceh & Sumut -->
        <path id="prov-sumatera-utara" class="province-path" data-id="sumatera-utara"
          d="M 120 70 L 150 95 L 175 140 L 150 160 L 125 125 L 100 85 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='sumatera-utara').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- Sumbar & Riau -->
        <path id="prov-riau" class="province-path" data-id="riau"
          d="M 150 160 L 195 165 L 220 200 L 180 205 L 150 175 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='riau').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <path id="prov-sumatera-barat" class="province-path" data-id="sumatera-barat"
          d="M 150 175 L 180 205 L 165 240 L 140 215 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='sumatera-barat').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- Sumsel & Lampung -->
        <path id="prov-lampung" class="province-path" data-id="lampung"
          d="M 195 210 L 240 220 L 260 270 L 225 285 L 190 240 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='lampung').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
      </g>

      <!-- KALIMANTAN -->
      <g id="kalimantan-group" class="map-island-group">
        <!-- Kalbar / Kalteng / Kalsel / Kaltim -->
        <path id="prov-kalimantan-timur" class="province-path" data-id="kalimantan-timur"
          d="M 380 120 L 450 110 L 485 160 L 480 230 L 435 240 L 390 220 L 370 170 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='kalimantan-timur').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <circle cx="430" cy="180" r="3" fill="#1E293B"/>
        <text x="438" y="184" fill="#57534E" font-size="10" font-family="'Plus Jakarta Sans', sans-serif">Kalimantan</text>
      </g>

      <!-- JAWA -->
      <g id="jawa-group" class="map-island-group">
        <!-- Banten -->
        <path id="prov-banten" class="province-path" data-id="banten"
          d="M 245 300 L 275 300 L 270 325 L 240 325 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='banten').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- DKI Jakarta -->
        <path id="prov-dki-jakarta" class="province-path" data-id="dki-jakarta"
          d="M 275 298 L 295 298 L 295 315 L 275 315 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='dki-jakarta').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.5"/>
        <!-- Jawa Barat -->
        <path id="prov-jawa-barat" class="province-path" data-id="jawa-barat"
          d="M 275 315 L 330 310 L 325 340 L 265 338 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='jawa-barat').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- Jawa Tengah -->
        <path id="prov-jawa-tengah" class="province-path" data-id="jawa-tengah"
          d="M 330 310 L 385 315 L 380 345 L 325 340 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='jawa-tengah').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- DI Yogyakarta -->
        <path id="prov-di-yogyakarta" class="province-path" data-id="di-yogyakarta"
          d="M 350 335 L 372 335 L 370 350 L 348 350 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='di-yogyakarta').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- Jawa Timur -->
        <path id="prov-jawa-timur" class="province-path" data-id="jawa-timur"
          d="M 385 315 L 450 320 L 440 355 L 380 345 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='jawa-timur').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
      </g>

      <!-- BALI & NUSA TENGGARA -->
      <g id="bali-group" class="map-island-group">
        <!-- Bali -->
        <path id="prov-bali" class="province-path" data-id="bali"
          d="M 460 338 L 485 336 L 485 352 L 460 350 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='bali').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <!-- NTB -->
        <path id="prov-nusa-tenggara-barat" class="province-path" data-id="nusa-tenggara-barat"
          d="M 495 338 L 540 336 L 538 355 L 493 352 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='nusa-tenggara-barat').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
      </g>

      <!-- SULAWESI -->
      <g id="sulawesi-group" class="map-island-group">
        <path id="prov-sulawesi-selatan" class="province-path" data-id="sulawesi-selatan"
          d="M 540 180 L 585 180 L 600 230 L 565 290 L 535 250 L 560 220 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='sulawesi-selatan').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <text x="560" y="240" fill="#57534E" font-size="10" font-family="'Plus Jakarta Sans', sans-serif">Sulawesi</text>
      </g>

      <!-- PAPUA & MALUKU -->
      <g id="papua-group" class="map-island-group">
        <path id="prov-papua" class="province-path" data-id="papua"
          d="M 760 170 L 830 160 L 910 180 L 910 280 L 820 280 L 780 230 Z"
          fill="${getMetricColor(PROVINCES_DATA.find(p=>p.id==='papua').postings, minVal, maxVal, metric)}"
          stroke="#FFFFFF" stroke-width="1.2"/>
        <text x="825" y="220" fill="#57534E" font-size="10" font-family="'Plus Jakarta Sans', sans-serif">Papua</text>
      </g>

      <!-- Callout annotations on the map -->
      <!-- Jakarta Hub Indicator -->
      <line x1="285" y1="298" x2="285" y2="250" stroke="#1E293B" stroke-width="1"/>
      <circle cx="285" cy="250" r="3" fill="#1E293B"/>
      <rect x="250" y="225" width="90" height="20" fill="#FFFFFF" stroke="#E7E5E4" rx="2"/>
      <text x="256" y="239" font-size="10" font-family="'JetBrains Mono', monospace" fill="#1A1A1A" font-weight="600">Jakarta (37.5%)</text>
    </svg>
  `;

  elements.mapSvgContainer.innerHTML = svg;

  // Add click & hover listeners to province paths
  const paths = elements.mapSvgContainer.querySelectorAll('.province-path');
  paths.forEach(p => {
    const provId = p.getAttribute('data-id');
    const province = PROVINCES_DATA.find(item => item.id === provId);
    if (!province) return;

    if (province.id === state.selectedProvince.id) {
      p.classList.add('active');
    }

    p.addEventListener('mouseenter', (e) => {
      showMapTooltip(e, province);
    });

    p.addEventListener('mousemove', (e) => {
      moveMapTooltip(e);
    });

    p.addEventListener('mouseleave', () => {
      hideMapTooltip();
    });

    p.addEventListener('click', () => {
      paths.forEach(el => el.classList.remove('active'));
      p.classList.add('active');
      state.selectedProvince = province;
      renderProvinceDetailCard(province);
    });
  });

  renderProvinceDetailCard(state.selectedProvince);
  renderProvinceLeaderboard();
}

function showMapTooltip(e, province) {
  const metric = state.currentMapMetric;
  const val = getMetricValue(province, metric);
  const formattedVal = metric === 'ratio' ? formatRatio(val) : formatNumber(val);

  elements.mapTooltip.innerHTML = `
    <div class="font-mono text-xs uppercase tracking-wider text-stone-500">${province.island}</div>
    <div class="font-serif text-base font-semibold text-stone-900">${province.name}</div>
    <div class="mt-1 flex items-baseline gap-2">
      <span class="font-mono text-sm font-bold text-stone-900">${formattedVal}</span>
      <span class="text-xs text-stone-500">${getMetricLabel(metric)}</span>
    </div>
    <div class="mt-1 text-xs text-stone-400 font-mono">Porsi Nasional: ${province.sharePostings}%</div>
  `;
  elements.mapTooltip.style.opacity = '1';
  moveMapTooltip(e);
}

function moveMapTooltip(e) {
  const x = e.clientX + 14;
  const y = e.clientY + 14;
  elements.mapTooltip.style.left = `${x}px`;
  elements.mapTooltip.style.top = `${y}px`;
}

function hideMapTooltip() {
  elements.mapTooltip.style.opacity = '0';
}

function renderProvinceDetailCard(province) {
  if (!elements.provinceDetailCard) return;

  elements.provinceDetailCard.innerHTML = `
    <div class="editorial-border-b pb-4 mb-4">
      <div class="flex items-center justify-between">
        <span class="editorial-tag">${province.island}</span>
        <span class="font-mono text-xs text-stone-500 font-medium">Rank #${PROVINCES_DATA.indexOf(province) + 1} of 15 Focus Regions</span>
      </div>
      <h3 class="font-serif text-3xl font-semibold text-stone-900 mt-2">${province.name}</h3>
      <p class="text-sm text-stone-600 mt-1 leading-relaxed">${province.highlight}</p>
    </div>

    <div class="grid grid-cols-2 gap-4 py-2">
      <div>
        <div class="font-mono text-xs text-stone-500 uppercase">Total Lowongan</div>
        <div class="font-mono text-2xl font-semibold text-stone-900 mt-0.5">${formatNumber(province.postings)}</div>
        <div class="text-xs text-stone-500 mt-0.5">${province.sharePostings}% pangsa nasional</div>
      </div>
      <div>
        <div class="font-mono text-xs text-stone-500 uppercase">Kuota Kursi</div>
        <div class="font-mono text-2xl font-semibold text-stone-900 mt-0.5">${formatNumber(province.quota)}</div>
        <div class="text-xs text-stone-500 mt-0.5">Total posisi terbuka</div>
      </div>
      <div>
        <div class="font-mono text-xs text-stone-500 uppercase">Pelamar Terdaftar</div>
        <div class="font-mono text-2xl font-semibold text-stone-900 mt-0.5">${formatNumber(province.applicants)}</div>
        <div class="text-xs text-stone-500 mt-0.5">Permintaan calon peserta</div>
      </div>
      <div>
        <div class="font-mono text-xs text-stone-500 uppercase">Keketatan (Ratio)</div>
        <div class="font-mono text-2xl font-semibold ${province.ratio >= 9 ? 'text-amber-700' : 'text-stone-900'} mt-0.5">${province.ratio}×</div>
        <div class="text-xs text-stone-500 mt-0.5">pelamar per 1 kursi</div>
      </div>
    </div>

    <div class="editorial-border-t pt-3 mt-4 flex items-center justify-between text-xs text-stone-500">
      <span>Klaster Unggulan:</span>
      <span class="font-medium text-stone-800">${province.topSector}</span>
    </div>
  `;
}

function renderProvinceLeaderboard() {
  if (!elements.provinceLeaderboard) return;
  const sorted = [...PROVINCES_DATA].sort((a, b) => b.postings - a.postings).slice(0, 5);

  elements.provinceLeaderboard.innerHTML = sorted.map((p, idx) => `
    <div class="py-2.5 flex items-center justify-between text-sm cursor-pointer hover:bg-stone-100 px-2 rounded transition-colors ${p.id === state.selectedProvince.id ? 'bg-stone-100 font-semibold' : ''}" data-id="${p.id}">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs text-stone-400 w-4">${idx + 1}</span>
        <span class="text-stone-800">${p.name}</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="font-mono text-xs text-stone-600">${formatNumber(p.postings)} post</span>
        <span class="font-mono text-xs font-semibold text-stone-900 w-12 text-right">${p.ratio}×</span>
      </div>
    </div>
  `).join('');

  elements.provinceLeaderboard.querySelectorAll('[data-id]').forEach(el => {
    el.addEventListener('click', () => {
      const id = el.getAttribute('data-id');
      const prov = PROVINCES_DATA.find(p => p.id === id);
      if (prov) {
        state.selectedProvince = prov;
        renderIndonesiaMap();
      }
    });
  });
}

// -------------------------------------------------------------
// 3. COMPETITION SCATTER PLOT (Quota vs Applicants with Regression)
// -------------------------------------------------------------
function renderScatterPlot() {
  if (!elements.scatterSvg) return;

  const width = 860;
  const height = 480;
  const margin = { top: 30, right: 40, bottom: 60, left: 65 };
  const innerW = width - margin.left - margin.right;
  const innerH = height - margin.top - margin.bottom;

  // Filter data based on category
  const filtered = state.scatterCategory === 'All'
    ? SCATTER_POINTS
    : SCATTER_POINTS.filter(p => p.category === state.scatterCategory);

  const maxQuota = 35;
  const maxApplicants = 400;

  const xScale = (val) => margin.left + (val / maxQuota) * innerW;
  const yScale = (val) => margin.top + innerH - (val / maxApplicants) * innerH;

  // Linear Regression Calculation (y = mx + b)
  let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
  const n = SCATTER_POINTS.length;
  SCATTER_POINTS.forEach(d => {
    sumX += d.quota;
    sumY += d.applicants;
    sumXY += d.quota * d.applicants;
    sumX2 += d.quota * d.quota;
  });
  const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
  const intercept = (sumY - slope * sumX) / n;

  // Regression endpoints
  const regX1 = 0;
  const regY1 = intercept;
  const regX2 = 35;
  const regY2 = slope * regX2 + intercept;

  let svgHtml = `
    <defs>
      <!-- Subtle Grid Pattern -->
      <pattern id="scatter-grid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#F5F5F0" stroke-width="1"/>
      </pattern>
    </defs>

    <rect width="${width}" height="${height}" fill="#FAFAF8" rx="4"/>
    <rect x="${margin.left}" y="${margin.top}" width="${innerW}" height="${innerH}" fill="url(#scatter-grid)"/>

    <!-- Axis Grid Lines & Ticks -->
  `;

  // X-Axis Grid & Labels (Quota)
  [0, 5, 10, 15, 20, 25, 30, 35].forEach(q => {
    const x = xScale(q);
    svgHtml += `
      <line x1="${x}" y1="${margin.top}" x2="${x}" y2="${margin.top + innerH}" stroke="#E7E5E4" stroke-width="0.8" stroke-dasharray="2,2"/>
      <text x="${x}" y="${margin.top + innerH + 22}" font-size="11" font-family="'JetBrains Mono', monospace" fill="#78716C" text-anchor="middle">${q}</text>
    `;
  });

  // Y-Axis Grid & Labels (Applicants)
  [0, 50, 100, 150, 200, 250, 300, 350, 400].forEach(a => {
    const y = yScale(a);
    svgHtml += `
      <line x1="${margin.left}" y1="${y}" x2="${margin.left + innerW}" y2="${y}" stroke="#E7E5E4" stroke-width="0.8" stroke-dasharray="2,2"/>
      <text x="${margin.left - 12}" y="${y + 4}" font-size="11" font-family="'JetBrains Mono', monospace" fill="#78716C" text-anchor="end">${a}</text>
    `;
  });

  // Axis Labels
  svgHtml += `
    <text x="${margin.left + innerW / 2}" y="${height - 15}" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" fill="#1A1A1A" text-anchor="middle">
      Kuota Posisi Terbuka (Seats per Posting) →
    </text>
    <text x="${- (margin.top + innerH / 2)}" y="20" transform="rotate(-90)" font-size="12" font-family="'Plus Jakarta Sans', sans-serif" font-weight="600" fill="#1A1A1A" text-anchor="middle">
      Jumlah Pelamar Terdaftar (Applicants) →
    </text>
  `;

  // Regression Confidence Band Ribbon (± 30 applicants)
  const bandUpper1 = yScale(regY1 + 35);
  const bandLower1 = yScale(regY1 - 25);
  const bandUpper2 = yScale(regY2 + 35);
  const bandLower2 = yScale(regY2 - 25);
  svgHtml += `
    <polygon points="${xScale(regX1)},${bandUpper1} ${xScale(regX2)},${bandUpper2} ${xScale(regX2)},${bandLower2} ${xScale(regX1)},${bandLower1}"
      fill="#E7E5E4" opacity="0.45"/>
  `;

  // Linear Regression Line (Solid Dark Slate)
  svgHtml += `
    <line x1="${xScale(regX1)}" y1="${yScale(regY1)}" x2="${xScale(regX2)}" y2="${yScale(regY2)}"
      stroke="#1E293B" stroke-width="2.2" stroke-linecap="round"/>
    <text x="${xScale(31)}" y="${yScale(slope * 31 + intercept) - 12}" font-size="11" font-family="'Newsreader', serif" font-style="italic" fill="#1E293B" font-weight="600">
      Garis Tren Regresi (r = 0.743)
    </text>
  `;

  // Scatter Dots
  filtered.forEach(d => {
    const cx = xScale(d.quota);
    const cy = yScale(d.applicants);

    let fill = '#475569'; // default slate
    if (d.category === 'BUMN') fill = '#1E3A4B'; // deep navy
    else if (d.category === 'Tech') fill = '#C2410C'; // editorial rust
    else if (d.category === 'Government') fill = '#0F766E'; // teal
    else if (d.category === 'Corporate') fill = '#57534E'; // stone

    svgHtml += `
      <circle class="scatter-dot" data-id="${d.id}" cx="${cx}" cy="${cy}" r="5"
        fill="${fill}" stroke="#FFFFFF" stroke-width="1.2" opacity="0.85"/>
    `;
  });

  elements.scatterSvg.innerHTML = svgHtml;

  // Tooltip listeners on scatter dots
  elements.scatterSvg.querySelectorAll('.scatter-dot').forEach(dot => {
    const id = parseInt(dot.getAttribute('data-id'), 10);
    const item = SCATTER_POINTS.find(p => p.id === id);
    if (!item) return;

    dot.addEventListener('mouseenter', (e) => {
      showScatterTooltip(e, item);
    });

    dot.addEventListener('mousemove', (e) => {
      moveScatterTooltip(e);
    });

    dot.addEventListener('mouseleave', () => {
      hideScatterTooltip();
    });
  });
}

function showScatterTooltip(e, d) {
  elements.chartTooltip.innerHTML = `
    <div class="flex items-center justify-between gap-4">
      <span class="editorial-tag">${d.category}</span>
      <span class="text-xs font-mono text-stone-400">${d.province}</span>
    </div>
    <div class="font-serif text-sm font-semibold text-stone-900 mt-1">${d.position}</div>
    <div class="text-xs text-stone-500">${d.company}</div>
    <div class="mt-2 grid grid-cols-3 gap-2 border-t border-stone-200 pt-2 text-center">
      <div>
        <div class="text-[10px] uppercase font-mono text-stone-400">Kuota</div>
        <div class="font-mono text-xs font-bold text-stone-900">${d.quota}</div>
      </div>
      <div>
        <div class="text-[10px] uppercase font-mono text-stone-400">Pelamar</div>
        <div class="font-mono text-xs font-bold text-stone-900">${d.applicants}</div>
      </div>
      <div>
        <div class="text-[10px] uppercase font-mono text-stone-400">Ratio</div>
        <div class="font-mono text-xs font-bold ${d.ratio >= 15 ? 'text-amber-700' : 'text-stone-900'}">${d.ratio}×</div>
      </div>
    </div>
  `;
  elements.chartTooltip.style.opacity = '1';
  moveScatterTooltip(e);
}

function moveScatterTooltip(e) {
  const x = e.clientX + 16;
  const y = e.clientY - 20;
  elements.chartTooltip.style.left = `${x}px`;
  elements.chartTooltip.style.top = `${y}px`;
}

function hideScatterTooltip() {
  elements.chartTooltip.style.opacity = '0';
}

// -------------------------------------------------------------
// 4. OPPORTUNITY EXPLORER (Search, Filters, Listings Table)
// -------------------------------------------------------------
function filterAndSortListings() {
  let result = [...OPPORTUNITY_LISTINGS];

  // 1. Search Query
  if (state.searchQuery.trim()) {
    const q = state.searchQuery.toLowerCase().trim();
    result = result.filter(item =>
      item.position.toLowerCase().includes(q) ||
      item.institution.toLowerCase().includes(q) ||
      item.city.toLowerCase().includes(q) ||
      item.majors.toLowerCase().includes(q)
    );
  }

  // 2. Province Filter
  if (state.filterProvince !== 'All') {
    result = result.filter(item => item.province === state.filterProvince);
  }

  // 3. Field Filter
  if (state.filterField !== 'All') {
    result = result.filter(item => item.field === state.filterField);
  }

  // 4. Education Filter
  if (state.filterEducation !== 'All') {
    result = result.filter(item => item.education === state.filterEducation);
  }

  // 5. Competition Filter
  if (state.filterCompetition !== 'All') {
    if (state.filterCompetition === 'low') {
      result = result.filter(item => item.ratio < 8);
    } else if (state.filterCompetition === 'moderate') {
      result = result.filter(item => item.ratio >= 8 && item.ratio <= 14);
    } else if (state.filterCompetition === 'fierce') {
      result = result.filter(item => item.ratio > 14);
    }
  }

  // 6. Sort
  switch (state.sortBy) {
    case 'ratio-desc':
      result.sort((a, b) => b.ratio - a.ratio);
      break;
    case 'ratio-asc':
      result.sort((a, b) => a.ratio - b.ratio);
      break;
    case 'quota-desc':
      result.sort((a, b) => b.quota - a.quota);
      break;
    case 'quota-asc':
      result.sort((a, b) => a.quota - b.quota);
      break;
    case 'applicants-desc':
      result.sort((a, b) => b.applicants - a.applicants);
      break;
    default:
      result.sort((a, b) => b.ratio - a.ratio);
  }

  return result;
}

function renderOpportunityListings() {
  if (!elements.listingsContainer) return;

  const filtered = filterAndSortListings();
  const total = filtered.length;
  elements.resultsCount.textContent = `Menampilkan ${Math.min(total, state.pageSize * state.page)} dari ${total} lowongan terkurasi`;

  // Pagination calculation
  const startIndex = (state.page - 1) * state.pageSize;
  const pageItems = filtered.slice(startIndex, startIndex + state.pageSize);

  if (pageItems.length === 0) {
    elements.listingsContainer.innerHTML = `
      <div class="py-16 text-center text-stone-500 font-serif text-lg">
        Tidak ditemukan lowongan dengan kriteria filter tersebut. Coba sesuaikan kata kunci atau bersihkan filter.
      </div>
    `;
    elements.paginationContainer.innerHTML = '';
    return;
  }

  elements.listingsContainer.innerHTML = pageItems.map(item => `
    <div class="listing-row editorial-border-b py-4 px-3 flex flex-col md:flex-row md:items-center justify-between gap-4 cursor-pointer" data-listing-id="${item.id}">
      <div class="flex-1 min-w-0">
        <div class="flex items-center gap-2 mb-1">
          <span class="editorial-tag">${item.category}</span>
          <span class="text-xs font-mono text-stone-400">${item.field}</span>
          <span class="text-xs font-mono text-stone-400">·</span>
          <span class="text-xs font-mono text-stone-500">${item.education}</span>
        </div>
        <h4 class="font-serif text-lg font-semibold text-stone-900 truncate hover:text-amber-800 transition-colors">${item.position}</h4>
        <div class="flex items-center gap-2 text-xs text-stone-600 mt-0.5">
          <span class="font-medium text-stone-800">${item.institution}</span>
          <span>·</span>
          <span>${item.city}, ${item.province}</span>
        </div>
      </div>

      <div class="flex items-center gap-6 shrink-0">
        <div class="text-right">
          <div class="text-[11px] uppercase font-mono text-stone-400">Kuota</div>
          <div class="font-mono text-sm font-semibold text-stone-800">${item.quota} kursi</div>
        </div>
        <div class="text-right">
          <div class="text-[11px] uppercase font-mono text-stone-400">Pelamar</div>
          <div class="font-mono text-sm font-semibold text-stone-800">${item.applicants}</div>
        </div>
        <div class="text-right min-w-[70px]">
          <div class="text-[11px] uppercase font-mono text-stone-400">Keketatan</div>
          <div class="font-mono text-base font-bold ${item.ratio >= 15 ? 'text-amber-700' : 'text-stone-900'}">${item.ratio}×</div>
        </div>
        <div>
          <button class="px-3 py-1.5 text-xs font-mono border border-stone-300 rounded hover:bg-stone-900 hover:text-white transition-colors" data-inspect-id="${item.id}">
            Rincian →
          </button>
        </div>
      </div>
    </div>
  `).join('');

  // Attach click listeners to row or inspect button
  elements.listingsContainer.querySelectorAll('[data-listing-id]').forEach(row => {
    row.addEventListener('click', () => {
      const id = row.getAttribute('data-listing-id');
      const item = OPPORTUNITY_LISTINGS.find(it => it.id === id);
      if (item) openListingModal(item);
    });
  });

  // Render pagination
  renderPagination(total);
}

function renderPagination(total) {
  const totalPages = Math.ceil(total / state.pageSize);
  if (totalPages <= 1) {
    elements.paginationContainer.innerHTML = '';
    return;
  }

  let html = `<div class="flex items-center gap-2 font-mono text-xs">`;
  for (let i = 1; i <= totalPages; i++) {
    html += `
      <button class="w-8 h-8 rounded border ${i === state.page ? 'border-stone-900 bg-stone-900 text-white font-bold' : 'border-stone-200 text-stone-700 hover:bg-stone-100'} transition-colors" data-page="${i}">
        ${i}
      </button>
    `;
  }
  html += `</div>`;
  elements.paginationContainer.innerHTML = html;

  elements.paginationContainer.querySelectorAll('[data-page]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      state.page = parseInt(btn.getAttribute('data-page'), 10);
      renderOpportunityListings();
      const el = document.getElementById('opportunity-explorer');
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

function openListingModal(item) {
  if (!elements.modalBackdrop) return;

  elements.modalTitle.textContent = item.position;
  elements.modalInstitution.textContent = item.institution;
  elements.modalBadge.textContent = item.category;
  elements.modalLocation.textContent = `${item.city}, ${item.province}`;
  elements.modalQuota.textContent = `${item.quota} Kursi`;
  elements.modalApplicants.textContent = `${item.applicants} Pelamar`;
  elements.modalRatio.textContent = `${item.ratio}× (Pelamar / Kursi)`;
  elements.modalWorkMode.textContent = item.workMode;
  elements.modalStipend.textContent = item.stipend;
  elements.modalDuration.textContent = item.duration;
  elements.modalMajors.textContent = item.majors;
  elements.modalDescription.textContent = item.description;

  elements.modalBackdrop.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

function closeListingModal() {
  if (!elements.modalBackdrop) return;
  elements.modalBackdrop.classList.add('hidden');
  document.body.style.overflow = 'auto';
}

// -------------------------------------------------------------
// 5. METHODOLOGY VISUALIZATION
// -------------------------------------------------------------
function renderMethodology() {
  if (!elements.methodologyStepsContainer) return;

  elements.methodologyStepsContainer.innerHTML = METHODOLOGY_STEPS.map((step, idx) => `
    <div class="methodology-step-card p-4 rounded border cursor-pointer transition-all ${idx === state.activeMethodologyIndex ? 'border-stone-900 bg-stone-50 shadow-sm' : 'border-stone-200 hover:border-stone-400 bg-white'}" data-step-index="${idx}">
      <div class="flex items-center justify-between">
        <span class="font-mono text-xs font-bold text-stone-400">${step.number}</span>
        <span class="editorial-tag">${step.badge}</span>
      </div>
      <h4 class="font-serif text-lg font-semibold text-stone-900 mt-2">${step.title}</h4>
      <div class="text-xs text-stone-500 font-mono mt-0.5">${step.subtitle}</div>
    </div>
  `).join('');

  elements.methodologyStepsContainer.querySelectorAll('[data-step-index]').forEach(card => {
    card.addEventListener('click', () => {
      const idx = parseInt(card.getAttribute('data-step-index'), 10);
      state.activeMethodologyIndex = idx;
      renderMethodology();
    });
  });

  const activeStep = METHODOLOGY_STEPS[state.activeMethodologyIndex];
  elements.methodologyDetailContainer.innerHTML = `
    <div class="bg-stone-50 border border-stone-200 p-6 rounded-lg">
      <div class="flex items-center gap-3">
        <span class="font-mono text-xs font-bold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded">Fase ${activeStep.number}</span>
        <span class="font-mono text-xs text-stone-500">${activeStep.subtitle}</span>
      </div>
      <h3 class="font-serif text-2xl font-bold text-stone-900 mt-2">${activeStep.title}</h3>
      <p class="text-stone-700 text-sm mt-3 leading-relaxed">${activeStep.description}</p>
      <div class="editorial-border-t pt-4 mt-6 flex items-center justify-between text-xs font-mono text-stone-500">
        <span>Karakteristik Data:</span>
        <span class="text-stone-800 font-medium">${activeStep.meta}</span>
      </div>
    </div>
  `;
}

// -------------------------------------------------------------
// 6. SETUP EVENT LISTENERS
// -------------------------------------------------------------
function setupEventListeners() {
  // Map Metric Switchers
  elements.mapMetricButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      elements.mapMetricButtons.forEach(b => {
        b.classList.remove('bg-stone-900', 'text-white', 'border-stone-900');
        b.classList.add('bg-white', 'text-stone-700', 'border-stone-200');
      });
      btn.classList.remove('bg-white', 'text-stone-700', 'border-stone-200');
      btn.classList.add('bg-stone-900', 'text-white', 'border-stone-900');

      state.currentMapMetric = btn.getAttribute('data-metric');
      renderIndonesiaMap();
    });
  });

  // Scatter Category Pills
  elements.scatterCategoryPills.forEach(pill => {
    pill.addEventListener('click', () => {
      elements.scatterCategoryPills.forEach(p => {
        p.classList.remove('bg-stone-900', 'text-white', 'border-stone-900');
        p.classList.add('bg-white', 'text-stone-700', 'border-stone-200');
      });
      pill.classList.remove('bg-white', 'text-stone-700', 'border-stone-200');
      pill.classList.add('bg-stone-900', 'text-white', 'border-stone-900');

      state.scatterCategory = pill.getAttribute('data-cat');
      renderScatterPlot();
    });
  });

  // Explorer Search & Filters
  if (elements.searchInput) {
    elements.searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      state.page = 1;
      renderOpportunityListings();
    });
  }

  if (elements.provinceSelect) {
    elements.provinceSelect.addEventListener('change', (e) => {
      state.filterProvince = e.target.value;
      state.page = 1;
      renderOpportunityListings();
    });
  }

  if (elements.fieldSelect) {
    elements.fieldSelect.addEventListener('change', (e) => {
      state.filterField = e.target.value;
      state.page = 1;
      renderOpportunityListings();
    });
  }

  if (elements.educationSelect) {
    elements.educationSelect.addEventListener('change', (e) => {
      state.filterEducation = e.target.value;
      state.page = 1;
      renderOpportunityListings();
    });
  }

  if (elements.competitionSelect) {
    elements.competitionSelect.addEventListener('change', (e) => {
      state.filterCompetition = e.target.value;
      state.page = 1;
      renderOpportunityListings();
    });
  }

  if (elements.sortSelect) {
    elements.sortSelect.addEventListener('change', (e) => {
      state.sortBy = e.target.value;
      renderOpportunityListings();
    });
  }

  if (elements.resetFiltersBtn) {
    elements.resetFiltersBtn.addEventListener('click', () => {
      state.searchQuery = '';
      state.filterProvince = 'All';
      state.filterField = 'All';
      state.filterEducation = 'All';
      state.filterCompetition = 'All';
      state.sortBy = 'ratio-desc';
      state.page = 1;

      if (elements.searchInput) elements.searchInput.value = '';
      if (elements.provinceSelect) elements.provinceSelect.value = 'All';
      if (elements.fieldSelect) elements.fieldSelect.value = 'All';
      if (elements.educationSelect) elements.educationSelect.value = 'All';
      if (elements.competitionSelect) elements.competitionSelect.value = 'All';
      if (elements.sortSelect) elements.sortSelect.value = 'ratio-desc';

      renderOpportunityListings();
    });
  }

  // Modal Close
  if (elements.modalCloseBtn) {
    elements.modalCloseBtn.addEventListener('click', closeListingModal);
  }
  if (elements.modalBackdrop) {
    elements.modalBackdrop.addEventListener('click', (e) => {
      if (e.target === elements.modalBackdrop) closeListingModal();
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeListingModal();
  });
}

// -------------------------------------------------------------
// 7. BOOTSTRAP APPLICATION
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  initOverviewStats();
  renderIndonesiaMap();
  renderScatterPlot();
  renderOpportunityListings();
  renderMethodology();
  setupEventListeners();

  // Resize listener for scatter plot responsive redraw
  window.addEventListener('resize', () => {
    renderScatterPlot();
  });
});
