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
