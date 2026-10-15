/* Generated from the individual JavaScript feature files. */

// navigation
(function () {
"use strict";
const header=document.querySelector('header'), menu=document.querySelector('.menu'),nav=document.querySelector('nav');
const current=location.pathname.split('/').pop()||'index.html';
nav.querySelectorAll('a').forEach(a=>{if(a.getAttribute('href')===current&&current!=='404.html')a.setAttribute('aria-current','page')});
function close(){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Open navigation')}
menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Close navigation':'Open navigation')});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){close();menu.focus()}});
document.addEventListener('click',e=>{if(!header.contains(e.target))close()});
nav.addEventListener('click',e=>{if(e.target.closest('a'))close()});
const progress=document.querySelector('.progress'),topButton=document.querySelector('.to-top');
let queued=false;function update(){header.classList.toggle('scrolled',scrollY>30);const max=document.documentElement.scrollHeight-innerHeight;progress.style.width=(max>0?scrollY/max*100:0)+'%';topButton.classList.toggle('visible',scrollY>600);queued=false}
addEventListener('scroll',()=>{if(!queued){requestAnimationFrame(update);queued=true}},{passive:true});update();
topButton.addEventListener('click',()=>window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'}));

})();

// animations
(function () {
"use strict";
if('IntersectionObserver' in window){document.body.classList.add('js-ready');const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in-view');observer.unobserve(e.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(e=>observer.observe(e))}

})();

// counters
(function () {
"use strict";
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
function run(el){const end=Number(el.dataset.target),suffix=el.dataset.suffix;let start;function frame(time){start??=time;const t=Math.min((time-start)/1400,1);el.textContent=Math.round(end*(1-Math.pow(1-t,3)))+suffix;if(t<1)requestAnimationFrame(frame)}if(reduced)el.textContent=end+suffix;else requestAnimationFrame(frame)}
if('IntersectionObserver'in window){const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){run(e.target);observer.unobserve(e.target)}}));document.querySelectorAll('.counter').forEach(e=>observer.observe(e))}else document.querySelectorAll('.counter').forEach(run);

})();

// charts
(function () {
"use strict";
const svg=document.querySelector('#chart'),select=document.querySelector('#chart-select');
if(svg&&select){const series=[[100,106,103,115,122,118,133,142,139,150,161,174],[100,103,109,117,125,137,148,163,181,202,224,250],[28,22,18,14,10,8],[35,25,20,12,8]];function draw(){const idx=select.selectedIndex,data=series[idx],labels=idx<2?['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']:idx===2?['Technology','Healthcare','Financials','Energy','Consumer','Other']:['Equity','Debt','Private','Real assets','Cash'];const max=idx<2?Math.max(...data)*1.1:40;let content='';for(let i=0;i<5;i++){const y=20+i*48;content+=`<line x1="48" y1="${y}" x2="880" y2="${y}" stroke="#e4e8ed"/><text x="3" y="${y+4}">${Math.round(max*(1-i/4))}${idx>1?'%':''}</text>`}const points=data.map((v,i)=>[60+i*(800/(data.length-1)),212-v/max*192]);if(idx<2){content+=`<path d="M${points.map(p=>p.join(',')).join(' L')} L860,212 L60,212 Z" fill="#c9a45c12"/><polyline class="chart-line" points="${points.map(p=>p.join(',')).join(' ')}" fill="none" stroke="#b38b46" stroke-width="3"/>`;points.forEach(([x,y],i)=>{content+=`<circle cx="${x}" cy="${y}" r="4" fill="#b38b46"><title>${labels[i]}: ${data[i]}</title></circle>`})}else{data.forEach((v,i)=>{const x=65+i*800/data.length,h=v/max*192;content+=`<rect x="${x}" y="${212-h}" width="${500/data.length}" height="${h}" fill="${i%2?'#15324c':'#c9a45c'}"><title>${labels[i]}: ${v}%</title></rect>`})}labels.forEach((l,i)=>{const x=idx<2?60+i*800/(data.length-1):65+i*800/data.length;content+=`<text x="${x}" y="244" text-anchor="${idx<2?'middle':'start'}">${l}</text>`});svg.innerHTML=content;svg.setAttribute('aria-label',select.value+': '+data.map((v,i)=>labels[i]+' '+v+(idx>1?'%':'')).join(', '));document.querySelector('#chart-title').textContent=select.value;document.querySelector('#chart-note').textContent=idx<2?'Illustrative index · January = 100 · Not historical returns or a forecast.':'Illustrative allocation percentages · Not an investment recommendation.'}select.addEventListener('change',draw);draw()}

})();

// filters
(function () {
"use strict";
const search=document.querySelector('#search'),filter=document.querySelector('#filter');
if(search&&filter){const items=[...document.querySelectorAll('.filter-item')];function update(){let count=0;for(const el of items){const show=el.textContent.toLowerCase().includes(search.value.trim().toLowerCase())&&(filter.value==='all'||el.dataset.category===filter.value);el.hidden=!show;if(show)count++}document.querySelector('#result-count').textContent=`${count} results`;document.querySelector('#empty').hidden=count!==0}search.addEventListener('input',update);filter.addEventListener('change',update);update()}

})();

// carousel
(function () {
"use strict";
const quote=document.querySelector('#quote');if(quote){const messages=['“Clarity in the moments that matter. Confidence in the decisions that follow.”','“A thoughtful perspective on opportunity, complexity and long-term value.”','“Strong partnerships begin with listening and grow through trust.”'];let index=0;const change=delta=>{index=(index+delta+messages.length)%messages.length;quote.textContent=messages[index]};document.querySelector('.quote-prev').addEventListener('click',()=>change(-1));document.querySelector('.quote-next').addEventListener('click',()=>change(1));quote.setAttribute('aria-live','polite')}

})();

// forms
(function () {
"use strict";
document.querySelectorAll('.demo-form').forEach(form=>{const file=form.querySelector('[type=file]');if(file)file.addEventListener('change',()=>{const f=file.files[0];file.setCustomValidity(f&&(f.size>5*1024*1024||!f.name.toLowerCase().endsWith('.pdf'))?'Choose a PDF smaller than 5 MB.':'')});form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;form.querySelector('.form-status').textContent='Validation complete. This is a frontend demonstration; nothing has been sent or stored.'})});
const role=new URLSearchParams(location.search).get('role');const position=document.querySelector('[name=position]');if(position&&role!==null&&[...position.options].some(o=>o.value===role))position.value=role;

})();
