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
  if(!record){
    details('Historical Strong’s · '+id,'No entry in this limited sample');
    return;
  }
  const kind=associationType==='kjv_derived';
  const d=details("Strong's "+id,record.headword,record.transliteration+' · '+verse+' · selected English word: '+english);
  add('div',kind?'KJV-derived supported research association · not a native tag':'Native source-linked association',d,kind?'source evidence-note':'source evidence-note');
  add('h4','Historical Strong’s source-authored explanation',d);
  add('p',record.concise_definition,d);
  const extra=record.source_long_form||{};
  if(extra.expanded_senses&&extra.expanded_senses.length){
    add('h4','Expanded Hebrew senses · same selected digital source',d);
    add('div',extra.expanded_senses.join('\n'),d,'definition');
    add('p','Numbered alternatives are reproduced as recorded. They are not automatically selected as the meaning of this verse.',d,'secondary');
  }
  if(extra.derivation){add('h4','Source derivation or grammatical note',d);add('p',extra.derivation,d);}
  if(extra.kjv_rendering){add('h4','Source-recorded KJV renderings',d);add('div',extra.kjv_rendering,d,'definition');}
  if(extra.supplemental_text){add('h4','Other source-authored note',d);add('p',extra.supplemental_text,d);}
  if(id.startsWith('G'))add('p','The selected Greek Strong’s XML does not contain a separate numbered extended-sense list. Its other source fields are shown above; no external long lexicon has been substituted.',d,'secondary');
  add('h4','Source and evidence',d);
  add('p',record.source_id,d,'source');
  add('p',kind?'This badge is based on an exact unique English-word alignment from native KJV tags into this translation. It is research evidence, not this edition’s own Strong’s tag or proof of contextual semantic equivalence.':'This badge comes from the selected edition’s own native source data. A Strong’s entry does not independently prove which historical sense the verse means.',d,'secondary');
  const button=add('button',"Look up '"+english+"' in Webster 1828",d,'pill');
  button.type='button';button.addEventListener('click',()=>websterLookup(english,null));
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
fetch('sample-data.json').then(r=>{if(!r.ok)throw Error('HTTP '+r.status);return r.json()})
.then(result=>{
  if(result.schema!=='sotw-public-safe-word-study-demo-v1')throw Error('Unknown sample schema');
  if(Object.keys(result.passages).length!==2)throw Error('Unexpected passage count');
  sample=result;show();
}).catch(err=>{add('p','Sample data failed to load: '+err.message,$('reader'));message('Demo cannot start until sample-data.json is deployed alongside index.html.')});
