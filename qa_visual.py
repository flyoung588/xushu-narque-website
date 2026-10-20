import asyncio,json,sys,re
from pathlib import Path
from playwright.async_api import async_playwright
BASE=str(Path(__file__).resolve().parent)+'/'
CSS=open(BASE+'styles-v1.css',encoding='utf-8').read()
JS=open(BASE+'app-v1.js',encoding='utf-8').read()
OUT=Path(BASE)/'qa';OUT.mkdir(parents=True,exist_ok=True)
PAGES=['index.html','metre.html','xrem.html','aios.html','research.html','collaboration.html','about.html','en/index.html','en/metre.html','en/xrem.html','en/aios.html','en/research.html','en/collaboration.html','en/about.html']
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'])
  problems=[];stats=[]
  for w,h,label in [(1440,900,'desktop'),(390,844,'mobile'),(320,740,'small')]:
   context=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=1,reduced_motion='reduce')
   for i,path in enumerate(PAGES):
    page=await context.new_page()
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    html=open(BASE+path,encoding='utf-8').read()
    html=re.sub(r'<link[^>]+rel=\"stylesheet\"[^>]*>','',html)
    html=re.sub(r'<script defer src=\"[^\"]+\"></script>','',html)
    html=html.replace('</head>','<style>'+CSS+'</style></head>')
    await page.set_content(html,wait_until='domcontentloaded',timeout=25000)
    await page.add_script_tag(content=JS)
    await page.wait_for_timeout(80)
    dims=await page.evaluate('''()=>({width:document.documentElement.scrollWidth,view:window.innerWidth,body:document.body.scrollWidth,nav:!!document.querySelector('.site-nav'),h1:document.querySelectorAll('h1').length,h2:document.querySelectorAll('h2').length})''')
    stat={'path':path,'viewport':label,'dims':dims,'js_errors':errors}
    stats.append(stat)
    if errors:problems.append({'path':path,'viewport':label,'issue':'JS errors','errors':errors})
    if dims['width']>w+3:problems.append({'path':path,'viewport':label,'issue':'horizontal-overflow','scrollWidth':dims['width'],'viewport_width':w})
    if dims['h1']!=1:problems.append({'path':path,'issue':'h1-count','count':dims['h1']})
    if i in [0,1,2,3,4,5,6] and label=='desktop':await page.screenshot(path=str(OUT/(path.replace('/','_')[:-5]+'_'+label+'.png')),full_page=(path in ['index.html','en/index.html'] and label!='desktop'))
    if path in ['index.html','en/index.html'] and label in ['mobile','small']:
     await page.screenshot(path=str(OUT/(path.replace('/','_')[:-5]+'_'+label+'.png')),full_page=(path in ['index.html','en/index.html'] and label!='desktop'))
     mb=page.locator('.menu-toggle'); await mb.click();
     was_visible=await page.locator('#mobile-nav').is_visible()
     if not was_visible:problems.append({'path':path,'viewport':label,'issue':'menu-not-visible'})
     await page.screenshot(path=str(OUT/(path.replace('/','_')[:-5]+'_'+label+'_nav.png')),full_page=False)
     await page.keyboard.press('Escape');
     if await page.locator('#mobile-nav').is_visible():problems.append({'path':path,'viewport':label,'issue':'menu-not-closed-on-escape'})
    await page.close()
   await context.close()
  await b.close()
  (OUT/'browser-qa.json').write_text(json.dumps({'stats':stats,'problems':problems},ensure_ascii=False,indent=2),encoding='utf-8')
  print('pages/viewports:',len(stats),'problems:',len(problems));print(json.dumps(problems,ensure_ascii=False,indent=2)[:10000])
asyncio.run(main())
