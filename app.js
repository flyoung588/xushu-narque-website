const reveals=document.querySelectorAll('.reveal');
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting)entry.target.classList.add('visible')}),{threshold:.16});
reveals.forEach(el=>observer.observe(el));

const canvas=document.getElementById('field');
const ctx=canvas?.getContext('2d');
let points=[];
function resize(){const dpr=Math.min(devicePixelRatio||1,2);const box=canvas.getBoundingClientRect();canvas.width=box.width*dpr;canvas.height=box.height*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);seed(box.width,box.height)}
function seed(w,h){points=[];const colors=['#1854bd','#b92e3b','#008c72','#bd7a17','#6b4aa0','#77736d'];for(let i=0;i<115;i++){const x=28+Math.random()*w*.62;const y=45+Math.random()*(h-80);points.push({x,y,baseY:y,r:Math.random()*2.7+1,color:colors[i%colors.length],speed:.003+Math.random()*.005,phase:Math.random()*6.28})}for(let i=0;i<3;i++)points.push({x:w*.84+i*38,y:h*.5+(i-1)*54,baseY:h*.5+(i-1)*54,r:5,color:colors[i],speed:.003,phase:i})}
function draw(t=0){const w=canvas.clientWidth,h=canvas.clientHeight;ctx.clearRect(0,0,w,h);ctx.lineWidth=.7;points.forEach((p,i)=>{p.y=p.baseY+Math.sin(t*p.speed+p.phase)*4;if(p.x<w*.7){const targetX=w*.71,targetY=h*.5+(p.baseY-h*.5)*.22;ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.bezierCurveTo(p.x+55,p.y,targetX-70,targetY,targetX,targetY);ctx.strokeStyle=p.color+'28';ctx.stroke()}ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.color;ctx.globalAlpha=p.x>w*.75?1:.68;ctx.fill();ctx.globalAlpha=1});requestAnimationFrame(draw)}
if(canvas&&ctx){window.addEventListener('resize',resize);resize();draw()}

const nav=document.querySelector('.nav');
if(nav)window.addEventListener('scroll',()=>{const dark=scrollY>innerHeight*.78;nav.style.position=dark?'fixed':'absolute';nav.style.background=dark?'rgba(244,239,230,.9)':'transparent';nav.style.color=dark?'#171a1e':'#fff';nav.style.borderColor=dark?'rgba(23,26,30,.14)':'rgba(255,255,255,.32)';nav.style.backdropFilter=dark?'blur(18px)':'none'});
