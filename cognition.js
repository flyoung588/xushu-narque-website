const DATA_ROOT='generated/public-cognition/';

async function load(name){
  const response=await fetch(DATA_ROOT+name,{cache:'no-store'});
  if(!response.ok)throw new Error(`Public cognition unavailable: ${name}`);
  return response.json();
}
const esc=value=>String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const status=value=>`<span class="status status-${String(value).toLowerCase().replaceAll('_','-')}">${esc(value)}</span>`;
const list=items=>items?.length?`<ul>${items.map(item=>`<li>${esc(item)}</li>`).join('')}</ul>`:'<p class="empty">None recorded in the public view.</p>';

function missionCard(m,detail=true){
  const detailId=m.mission_id.includes('SOLAR')?'solar':m.mission_id.includes('BATTERY')?'battery':'aging';
  return `<article class="mission-card">
    <header><div><p class="kicker">OPEN MISSION</p><h2>${esc(m.name_zh)}<small>${esc(m.name_en)}</small></h2></div>${status(m.mission_status)}</header>
    <p class="mission-text">${esc(m.open_mission_zh)}</p>
    <div class="mission-grid">
      <div><b>CURRENT LOCAL GAME</b><p>${esc(m.current_local_game_public)}</p></div>
      <div><b>CURRENT NODE</b><p>${esc(m.current_node)}</p></div>
      <div><b>CURRENT BLOCKER</b><p>${esc(m.current_blocker)}</p></div>
      <div><b>NEXT REALITY GATE</b><p>${esc(m.next_reality_gate)}</p></div>
    </div>
    ${detail?`<details><summary>Evidence boundary</summary><div class="detail-grid"><section><b>WHAT HAS BEEN FALSIFIED</b>${list(m.falsified_public)}</section><section><b>WHAT IS STILL UNKNOWN</b>${list(m.unknowns_public)}</section><section><b>NOT YET PROVEN</b>${list(m.not_proven)}</section></div></details>`:''}
    <footer><span>Evidence cutoff ${esc(m.evidence_cutoff)}</span><span>${esc(m.disclosure_note)}</span>${detail?`<a href="mission.html?id=${detailId}">OPEN DETAIL →</a>`:''}</footer>
  </article>`;
}

async function renderMissions(){
  const data=await load('xrem_missions.json');
  const target=document.querySelector('[data-missions]');if(!target.children.length)target.innerHTML=data.missions.map(m=>missionCard(m)).join('');
  document.querySelectorAll('[data-cutoff]').forEach(el=>el.textContent=data.evidence_cutoff);
}

async function renderCurrent(){
  const data=await load('current_state.json');
  if(document.querySelector('[data-current]').children.length){document.querySelector('[data-cutoff]').textContent=data.evidence_cutoff;return}
  const group=(title,items)=>`<section class="state-group"><h2>${title}</h2>${items.length?items.map(p=>`<article><div>${status(p.status)}<h3>${esc(p.name)}</h3></div><p>${esc(p.current_node)}</p><small>Next gate — ${esc(p.next_gate)}</small></article>`).join(''):'<p class="empty">No public objects in this state.</p>'}</section>`;
  const p=data.project_state;
  document.querySelector('[data-current]').innerHTML=`<section class="proof-grid"><div><h2>PROCESS STATE</h2><p>${esc(data.process_state.summary)}</p></div><div><h2>THEORY STATE</h2><p>${esc(data.theory_state.status)}</p></div><div><h2>CAPABILITY STATE</h2><p>${esc(data.capability_state.status)}</p><small>Mission progress ≠ Capability progress</small></div></section>`+group('WHAT IS ACTIVE',p.active)+group('WHAT IS FROZEN',p.frozen)+group('WHAT IS WAITING',p.waiting)+group('WHAT IS CLOSED / HISTORICAL',p.closed_historical)+`<section class="proof-grid"><div><h2>WHAT IS PROVEN</h2>${list(data.proven)}</div><div><h2>WHAT IS NOT PROVEN</h2>${list(data.not_proven)}</div></section>`;
  document.querySelector('[data-cutoff]').textContent=data.evidence_cutoff;
}

async function renderChanges(){
  const data=await load('what_changed.json');
  if(document.querySelector('[data-changes]').children.length)return;
  document.querySelector('[data-changes]').innerHTML=data.entries.map(e=>`<article class="change"><header><time>${esc(e.date)}</time>${status(e.materiality)}${status(e.delta_type)}</header><h2>${esc(e.affected)}</h2><dl><dt>WHAT CHANGED</dt><dd>${esc(e.what_changed)}</dd><dt>WHAT DID NOT CHANGE</dt><dd>${esc(e.what_did_not_change)}</dd><dt>WHY IT MATTERS</dt><dd>${esc(e.why_it_matters)}</dd><dt>NEXT GATE</dt><dd>${esc(e.next_gate)}</dd></dl><footer>Evidence cutoff ${esc(data.evidence_cutoff)} · ${esc(data.payload_hash)}</footer></article>`).join('');
}

async function renderWorld(){
 const d=await load('world_model.json'), en=document.documentElement.lang.startsWith('en');
 const txt=o=>esc(en?o.canonical_text_en:o.canonical_text_zh);
 document.querySelectorAll('[data-world-model]').forEach(el=>{if(!el.children.length)el.innerHTML=`<article><p>${txt(d.definition)}</p></article><div class="capital-grid">${d.theories.map(t=>`<article><h3>${esc(t.object_id.replace('THEORY-','').replaceAll('-',' '))}</h3><p>${txt(t)}</p><small>${esc(t.epistemic_status)}</small></article>`).join('')}</div>`});
}
async function renderProcess(){
 const d=await load('xrem_process.json'), en=document.documentElement.lang.startsWith('en');
 const p=d.process;
 document.querySelectorAll('[data-xrem-definition]').forEach(el=>{if(!el.textContent.trim())el.textContent=en?d.xrem_definition.canonical_text_en:d.xrem_definition.canonical_text_zh});
 document.querySelectorAll('[data-xrem-process]').forEach(el=>{if(!el.children.length)el.innerHTML=p.steps.map((s,i)=>`<li><b>${String(i+1).padStart(2,'0')}</b><span>${esc(s)}</span></li>`).join('')});
}
async function renderCapitals(){
 const d=await load('three_capitals.json'), en=document.documentElement.lang.startsWith('en');
 document.querySelectorAll('[data-capitals]').forEach(el=>{if(!el.children.length)el.innerHTML=d.items.map(x=>`<article><h3>${esc(x.object_id.replace('CAPITAL-',''))}</h3><p>${esc(en?x.canonical_text_en:x.canonical_text_zh)}</p></article>`).join('')});
}
async function renderVerification(){
 const d=await load('verification_capital.json'), en=document.documentElement.lang.startsWith('en'), b=d.base;
 document.querySelectorAll('[data-verification]').forEach(el=>{if(!el.children.length)el.innerHTML=`<p>${esc(en?b.canonical_text_en:b.canonical_text_zh)}</p><div class="layer-grid">${b.layers.map(x=>`<article><b>${esc(x.id)}</b><h3>${esc(x.name)}</h3><small>${esc(x.class)}</small></article>`).join('')}</div><p class="boundary">${esc(b.north_star)}</p>`});
}

async function renderNow(){
  const data=await load('now_at_narque.json');
  if(document.querySelector('[data-now]').children.length){document.querySelector('[data-now-cutoff]')?.textContent=data.evidence_cutoff;return}
  const en=document.documentElement.lang.startsWith('en');
  document.querySelector('[data-now]').innerHTML=data.items.map(item=>`<a href="${esc(item.href)}"><h3>${esc(en?item.title_en:item.title_zh)}<small>${esc(en?item.title_zh:item.title_en)}</small></h3><p>${esc(en?item.summary_en:item.summary_zh)}</p><span>VIEW CURRENT STATE →</span></a>`).join('');
  document.querySelector('[data-now-cutoff]')?.textContent=data.evidence_cutoff;
}

async function renderHomeMissions(){
  const data=await load('xrem_missions.json');
  if(document.querySelector('[data-home-missions]').children.length)return;
  const en=document.documentElement.lang.startsWith('en');
  document.querySelector('[data-home-missions]').innerHTML=data.missions.map(m=>{
    const id=m.mission_id.includes('SOLAR')?'solar':m.mission_id.includes('BATTERY')?'battery':'aging';
    return `<a href="mission.html?id=${id}"><header>${status(m.mission_status)}<span>${esc(m.current_local_game_public==='NONE'?'LOCAL GAME · NONE':'LOCAL GAME · QUALIFICATION')}</span></header><h3>${esc(en?m.name_en:m.name_zh)}<small>${esc(en?m.name_zh:m.name_en)}</small></h3><b>${esc(m.current_node)}</b><p>${esc(m.current_blocker)}</p><footer>${en?'NEXT GATE':'下一 REALITY GATE'} →</footer></a>`;
  }).join('');
}

async function renderMissionDetail(){
  const id=new URLSearchParams(location.search).get('id')||'solar';
  const files={solar:'mission-xrem-solar-001.json',battery:'mission-xrem-battery-001.json',aging:'mission-xrem-aging-reversal-open-mission.json'};
  if(!files[id])throw new Error('Unknown public mission');
  const mission=await load(files[id]);
  document.querySelector('[data-mission-detail]').innerHTML=missionCard(mission);
  document.title=`${mission.name_en} · XREM · NARQUE`;
}

const jobs=[];
if(document.querySelector('[data-missions]'))jobs.push(renderMissions());
if(document.querySelector('[data-current]'))jobs.push(renderCurrent());
if(document.querySelector('[data-changes]'))jobs.push(renderChanges());
if(document.querySelector('[data-now]'))jobs.push(renderNow());
if(document.querySelector('[data-mission-detail]'))jobs.push(renderMissionDetail());
if(document.querySelector('[data-home-missions]'))jobs.push(renderHomeMissions());
if(document.querySelector('[data-world-model]'))jobs.push(renderWorld());
if(document.querySelector('[data-xrem-process]')||document.querySelector('[data-xrem-definition]'))jobs.push(renderProcess());
if(document.querySelector('[data-capitals]'))jobs.push(renderCapitals());
if(document.querySelector('[data-verification]'))jobs.push(renderVerification());
Promise.all(jobs).catch(error=>{document.querySelectorAll('[data-cognition-root]').forEach(el=>el.innerHTML=`<p class="projection-error">Public projection failed closed. ${esc(error.message)}</p>`)});
