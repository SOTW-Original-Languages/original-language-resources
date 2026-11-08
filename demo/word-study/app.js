'use strict';
/* SOTW public-safe limited Word Study viewer. No private corpus or inferred links. */
const $=id=>document.getElementById(id);
const editionLabels={BSB:'Berean Standard Bible',KJV1769:'King James Version 1769',WEBSTER1833:'Webster Bible 1833',ASV1901:'American Standard Version 1901'};
const asvBase='https://raw.githubusercontent.com/SOTW-ASV-1901/asv-1901-resources/';
let sample=null,book='GEN',edition='ASV1901',dictionary=null,dictionaryPromise=null,activeRequest=0,asvRequest=0;
function add(tag,text,parent,cls){
  const n=document.createElement(tag);
  n.textContent=text;
  if(cls)n.className=cls;
  parent.appendChild(n);
  return n;
}
function normalize(word){
  return String(word||'').trim().replace(/[\u2018\u2019]/g,"'").replace(/\s+/g,' ').toLowerCase();
}
function tokenPieces(text){
  return text.match(/[A-Za-z]+(?:['\u2019][A-Za-z]+)*|[^A-Za-z]+/g)||[];
}
function message(text){$('status').textContent=text}
function pressed(){
  document.querySelectorAll('[data-book]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.book===book)));
  document.querySelectorAll('[data-edition]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.edition===edition)));
}
function initialDetails(){
  const d=$('details');d.replaceChildren();
  add('div','Choose a study tool',d,'marker');
  add('h3','Select a word',d);
  add('p',"Tap any English word for Webster's 1828 dictionary. Small H/G badges on BSB/KJV come from that edition's native sources. Outlined H/G badges on ASV/Webster are limited supported KJV-derived research associations. Neither selects a contextual sense.",d);
}
function clearSelected(){document.querySelectorAll('.word.selected').forEach(b=>b.classList.remove('selected'))}
function show(){
  if(!sample)return;
  ++activeRequest;++asvRequest;
  pressed();initialDetails();
  const p=sample.passages[book];
  $('reading-title').textContent=p.title+' · '+editionLabels[edition];
  $('origin').textContent=edition==='ASV1901'?'Pinned ASV GitHub source with sample fallback':edition==='BSB'?'BSB archived source sample':edition==='KJV1769'?'KJV source-tagged USFM sample':'Webster 1833 archived source sample';
  const r=$('reader');r.replaceChildren();
  for(const verse of p.editions[edition]){
    const para=add('p','',r,'verse');
    add('span',verse.id.split('.')[2],para,'vnum');
    let wordIndex=0;
    for(const piece of tokenPieces(verse.text)){
      if(/^[A-Za-z]/.test(piece)){
        ++wordIndex;
        const w=add('button',piece,para,'word');
        w.type='button';
        w.title='Open Webster 1828: '+piece;
        w.setAttribute('aria-label','Webster 1828 lookup for '+piece);
        w.addEventListener('click',()=>websterLookup(piece,w));
        const native=verse.native_links&&verse.native_links[String(wordIndex)];
        const derived=verse.kjv_derived_links&&verse.kjv_derived_links[String(wordIndex)];
        if(native||derived){
          const associations=native||derived;
          const associationType=native?'native':'kjv_derived';
          for(const id of associations){
            const tag=add('button',id,para,associationType==='native'?'strong':'strong derived');
            tag.type='button';
            tag.title=associationType==='native'?"Source-native Strong's "+id:"Supported KJV-derived research association "+id+" (not a native tag)";
            tag.setAttribute('aria-label',(associationType==='native'?"Source-native Strong's ":"KJV-derived association ")+id+' for '+piece);
            tag.addEventListener('click',()=>showStrongs(id,piece,verse.id,associationType));
          }
        }
      }else para.appendChild(document.createTextNode(piece));
    }
  }
  if(edition==='ASV1901')verifyASV(book,asvRequest);
  else if(edition==='WEBSTER1833') message('Webster 1833 is a limited archived text sample. Outlined H/G badges are source-checked KJV-derived research associations, not Webster native Strong’s tags.');
  else message('Small source-archived verse excerpt. Filled H/G badges represent the selected edition’s own native tags; no complete Bible repository is implied.');
}
async function verifyASV(selected,request){
  const segment=selected==='GEN'?'genesis':'john';
  const url=asvBase+sample.asv_pin+'/data/asv1901/'+segment+'/chapters/01.json';
  message('Checking ASV text against pinned GitHub chapter JSON…');
  try{
    const response=await fetch(url);
    if(!response.ok)throw Error('HTTP '+response.status);
    const chapter=await response.json();
    const preview=sample.passages[selected].editions.ASV1901;
    let count=0;
    for(const verse of preview){
      const upstream=chapter.verses.find(item=>item.id===verse.id);
      if(!upstream)throw Error('Missing '+verse.id);
      const text=upstream.spans.filter(item=>item.kind==='text').map(item=>item.text).join('');
      if(text!==verse.text)throw Error('Source/sample mismatch: '+verse.id);
      ++count;
    }
    if(request===asvRequest&&edition==='ASV1901'&&book===selected)
      message('ASV pinned GitHub source checked: '+count+'/'+preview.length+' displayed verses match exactly.');
  }catch(err){
    if(request===asvRequest&&edition==='ASV1901'&&book===selected)
      message('ASV live source verification unavailable ('+err.message+'). The already checked fallback sample remains displayed; no silent substitution.');
  }
}
function details(type,title,sub){
  const d=$('details');d.replaceChildren();
  add('div',type,d,'marker');
  add('h3',title,d);
  if(sub)add('p',sub,d,'secondary');
  return d;
}
function showStrongs(id,english,verse,associationType){
  ++activeRequest;clearSelected();
  const record=sample.lexicon[id];
  if(!record){details('Historical Strong’s · '+id,'No entry in this limited sample');return;}
  const derived=associationType==='kjv_derived';
  const inventory=associationType==='review_only';
  const subtitle=inventory?'Public sample inventory, no verse assertion':record.transliteration+' · '+verse+' · English word: '+english;
  const d=details("Strong's "+id+' · original-language entry',record.headword,subtitle);
  const evidence=inventory?'Full inspection of this selected sample record; no word alignment asserted.':derived?
    'KJV-derived research association · not a native ASV/Webster Strong’s tag':
    'Source-native BSB/KJV association · no contextual sense selected';
  add('div',evidence,d,'source evidence-note');

  // Always show both definition layers clearly. The Greek selected source has no separately numbered long list.
  add('h4',"1 · Strong’s concise definition (source-authored)",d);
  add('div',record.concise_definition||'Not present in this selected source record.',d,'concise-field');

  const extra=record.source_long_form||{};
  add('h4',"2 · Strong’s expanded / full source material",d);
  if(extra.expanded_senses&&extra.expanded_senses.length){
    add('div',extra.expanded_senses.join('\n'),d,'definition expanded-field');
    add('p','Numbered Hebrew sense alternatives as present in the selected digital source. These are not an automatic interpretation of the verse.',d,'secondary');
  }else{
    add('p',id.startsWith('G')?'No separately numbered long-sense list exists in the selected Greek XML v1.9. Its complete available source fields for this sample are presented below.':'No separate numbered expanded-sense field exists for this selected source entry.',d,'secondary');
  }

  add('h4',"3 · Source derivation / grammar note",d);
  add('div',extra.derivation||'Not present in selected source record.',d,'definition');
  add('h4',"4 · Strong’s source-recorded KJV renderings",d);
  add('div',extra.kjv_rendering||'Not present in selected source record.',d,'definition');
  add('h4',"5 · Additional source-authored notes",d);
  add('p',extra.supplemental_text||'No separate supplemental note for this selected record.',d,'secondary');

  const meta=record.source_details||{};
  add('h4',"6 · Original-language and editorial metadata",d);
  const metadata=[];
  if(record.transliteration)metadata.push('Transliteration: '+record.transliteration);
  if(meta.unpointed_form)metadata.push('Unpointed Hebrew form: '+meta.unpointed_form);
  if(meta.source_POS_attribute_as_encoded)metadata.push('Hebrew source POS attribute (as encoded): '+meta.source_POS_attribute_as_encoded);
  if(meta.source_morph_code)metadata.push('Hebrew source morphology code: '+meta.source_morph_code);
  if(meta.source_beta_code)metadata.push('Greek source Beta Code: '+meta.source_beta_code);
  if(meta.source_pronunciation)metadata.push('Greek source pronunciation: '+meta.source_pronunciation);
  if(meta.source_TWOT_reference_candidate)metadata.push('Source TWOT reference candidate (reference only, NOT TWOT text): '+meta.source_TWOT_reference_candidate);
  if(meta.literal_strongs_references?.length)metadata.push('Literal Strong’s cross-references in source: '+meta.literal_strongs_references.join(', ')+' (not verified verse/meaning links)');
  if(meta.source_entry_sha256_research)metadata.push('Source research entry SHA-256: '+meta.source_entry_sha256_research);
  add('div',metadata.length?metadata.join('\n'):'No additional metadata in this bounded sample.',d,'definition metadata-field');

  add('h4',"7 · Source attribution and rights",d);
  const lock=id.startsWith('H')?sample.source_locks?.strongs_hebrew:sample.source_locks?.strongs_greek;
  add('div','Historical author: James Strong\nSelected digital source: '+record.source_id+
      '\nSource file: '+(lock?.source||'See demo README')+
      '\nXML SHA-256: '+(lock?.source_xml_sha256||'Not shown')+
      '\nRights basis: '+(lock?.source_edition||'See source manifest')+
      (id.startsWith('G')?'\nGreek XML digital-editor attribution: Ulrik Sandborg-Petersen; version 1.9.':''),
      d,'definition metadata-field');
  add('p',inventory?'This record is one of 13 public preview examples. Full pre-beta Hebrew/Greek research corpora are NOT published on this page.':
    derived?'This exact English token was conservatively aligned from a KJV source tag. It is not the target Bible’s own native tag and is not proof of contextual meaning.':
    'This selected link comes from the displayed edition’s native source. The lexical meanings remain alternatives, not a verse-specific interpretation.',d,'secondary');
  if(english){
    const button=add('button',"Look up '"+english+"' in Webster 1828",d,'pill');
    button.type='button';button.addEventListener('click',()=>websterLookup(english,null));
  }
  const sourceLink=add('a','Review all 13 entries and attribution ledger',d,'review-back');
  sourceLink.href='#source-review';
}
function reviewInventory(){
  const catalog=$('entry-catalog'),table=$('field-audit');
  if(!catalog||!table||!sample)return;
  catalog.replaceChildren();table.replaceChildren();
  const ids=Object.keys(sample.lexicon).sort((a,b)=>a[0]===b[0]?Number(a.slice(1))-Number(b.slice(1)):a[0]==='H'?-1:1);
  $('inventory-summary').textContent=ids.length+' selected historical Strong’s records: '+
    ids.filter(id=>id[0]==='H').length+' Hebrew and '+ids.filter(id=>id[0]==='G').length+
    ' Greek. This is the COMPLETE inventory of the demo sample, not the underlying full research library.';
  const thead=document.createElement('thead'),headrow=document.createElement('tr');
  for(const label of ['Entry','Concise','Numbered senses','Derivation','KJV renderings','Extra note','Source metadata']){
    add('th',label,headrow);
  }
  thead.appendChild(headrow);table.appendChild(thead);
  const tbody=document.createElement('tbody');
  for(const id of ids){
    const r=sample.lexicon[id],x=r.source_long_form||{},m=r.source_details||{};
    const b=add('button',id+' · '+r.headword+' ('+r.transliteration+')',catalog,'pill inventory-link');
    b.type='button';
    b.addEventListener('click',()=>{
      showStrongs(id,null,null,'review_only');
      if(typeof $('details').scrollIntoView==='function')$('details').scrollIntoView({behavior:'smooth',block:'start'});
    });
    const row=document.createElement('tr');
    const status=(v)=>v?'Present':'Not in selected source';
    const vals=[id,status(r.concise_definition),x.expanded_senses?.length?x.expanded_senses.length+' senses':'No numbered list',
      status(x.derivation),status(x.kjv_rendering),status(x.supplemental_text),
      (id.startsWith('H')?'Hebrew form/morph/TWOT ref':'Greek Beta Code/pronunciation')];
    for(const v of vals)add('td',String(v),row);
    tbody.appendChild(row);
  }
  table.appendChild(tbody);
  $('source-summary').textContent='The research checkpoint catalogs 8,674 Hebrew and 5,624 Greek source records; this public page includes just 5 Hebrew + 8 Greek examples. The original source libraries, private Inspector and full word-alignment research are not exposed here.';
  const locks=$('source-locks');locks.replaceChildren();
  const h=sample.source_locks.strongs_hebrew,g=sample.source_locks.strongs_greek;
  for(const [title,p] of [
    ['Hebrew Strong’s | James Strong',h],
    ['Greek Strong’s | James Strong; XML editor Ulrik Sandborg-Petersen',g]
  ]){
    const card=add('div','',locks,'source-card');
    add('h3',title,card);
    add('p',p.source_edition,card,'secondary');
    add('p','Source: '+p.source,card,'source');
    add('p','XML SHA-256: '+p.source_xml_sha256,card,'source');
  }
}
async function loadDictionary(){
  if(dictionary)return dictionary;
  if(dictionaryPromise)return dictionaryPromise;
  dictionaryPromise=fetch('../../webster1828.json').then(r=>{
    if(!r.ok)throw Error('HTTP '+r.status);
    return r.json();
  }).then(j=>{dictionary=j;return j}).finally(()=>dictionaryPromise=null);
  return dictionaryPromise;
}
async function websterLookup(word,button){
  const request=++activeRequest;
  clearSelected();if(button)button.classList.add('selected');
  let d=details('Webster 1828 · direct English lookup',word,'Searching an exact historical English headword');
  add('p','Loading the existing 1828 dictionary from this site…',d,'secondary');
  try{
    const dict=await loadDictionary();
    if(request!==activeRequest)return;
    const rows=dict[normalize(word)];
    d=details('Webster 1828 · exact headword',word,editionLabels[edition]+' · historical English');
    if(!rows||!rows.length){
      add('p','No exact entry for this spelling. Try its base dictionary form. We do not invent stemming or contextual senses.',d);
      return;
    }
    add('p',rows.length+' source '+(rows.length===1?'entry':'entries')+' found. The original dictionary content is shown as text rather than executed as HTML.',d,'secondary');
    for(const row of rows){
      add('h4','Source row '+row[2],d);
      add('div',row[1],d,'definition');
    }
    add('p','Noah Webster (1828) · digital transcription CC BY-SA 4.0. An English headword does not automatically identify the meaning of a Greek/Hebrew word in context.',d,'secondary');
  }catch(err){
    if(request!==activeRequest)return;
    d=details('Webster 1828','Dictionary unavailable');
    add('p','Unable to load the site dictionary: '+err.message+'. Please refresh the page.',d);
  }
}
document.querySelectorAll('[data-book]').forEach(b=>b.addEventListener('click',()=>{book=b.dataset.book;show()}));
document.querySelectorAll('[data-edition]').forEach(b=>b.addEventListener('click',()=>{edition=b.dataset.edition;show()}));
fetch('sample-data.json?v=1.2').then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()})
.then(result=>{
  if(result.schema!=='sotw-public-safe-word-study-demo-v1')throw Error('Unknown sample schema');
  if(Object.keys(result.passages).length!==2)throw Error('Unexpected passage count');
  sample=result;show();reviewInventory();
}).catch(err=>{add('p','Sample data failed to load: '+err.message,$('reader'));message('Demo cannot start until sample-data.json is deployed alongside index.html.')});
