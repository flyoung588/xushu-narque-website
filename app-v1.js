/* NARQUE Website v1.0.0 staging. Lightweight progressive enhancement. */
(()=>{
  'use strict';
  const header=document.querySelector('.site-header');
  const menu=document.querySelector('.menu-toggle');
  const mobile=document.querySelector('#mobile-nav');
  if(!header||!menu||!mobile)return;
  const setMenu=(open)=>{
    menu.setAttribute('aria-expanded',String(open));
    mobile.hidden=!open;
    header.classList.toggle('nav-open',open);
    if(!open)menu.focus({preventScroll:true});
  };
  menu.addEventListener('click',()=>setMenu(menu.getAttribute('aria-expanded')!=='true'));
  mobile.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
  window.addEventListener('keydown',(e)=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true')setMenu(false)});
  const onScroll=()=>{
    if(header.classList.contains('nav-open'))return;
    header.classList.toggle('is-scrolled',window.scrollY>64);
  };
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
})();
