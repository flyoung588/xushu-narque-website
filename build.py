#!/usr/bin/env python3
"""NARQUE website v1.0 staging build — source-driven from content-canon.json.

- Content blocks are read without paraphrase.
- Generates seven Chinese and seven English static pages.
- Does not modify a live website.
"""
from __future__ import annotations
from pathlib import Path
from html import escape
import json
import posixpath
import re
import hashlib

ROOT = Path(__file__).resolve().parent
CANON = json.loads((ROOT/'content-canon.json').read_text(encoding='utf-8'))
BASE_URL = 'https://flyoung588.github.io/xushu-narque-website/'
COPY_VER = CANON.get('version','1.0.0')
PAGES = CANON['pages']
NAV = {p['id']:p for p in PAGES}
NAV_ORDER = ['metre','xrem','aios','research','collaboration','about']
LABEL = {
'zh': {'home':'首页','discover':'了解更多','explore':'继续探索','read':'深入了解','collab':'国际科研合作','contact':'建立联系','menu':'菜单','close':'关闭菜单','lang':'EN','download':'下载公司介绍','framework':'理论 · 发现 · 资本','all':'阅读研究成果','mission':'文明级使命','copyright':'序束 NARQUE · 机器经济时代的理论、科学发现与资本探索','skip':'跳至正文'},
'en': {'home':'Home','discover':'Explore further','explore':'Explore','read':'Learn more','collab':'Global Collaboration','contact':'Get in touch','menu':'Menu','close':'Close menu','lang':'中文','download':'Company overview PDF','framework':'THEORY · DISCOVERY · CAPITAL','all':'Explore research','mission':'SCIENTIFIC MISSIONS','copyright':'NARQUE · Theory, discovery and capital research for the machine economy','skip':'Skip to content'}
}
NUM = {'home':'00','metre':'01','xrem':'02','aios':'03','research':'04','collaboration':'05','about':'06'}
KIND = {'metre':'theory','xrem':'science','aios':'capital','research':'archive','collaboration':'global','about':'identity'}


def e(x): return escape(str(x), quote=True)
def ptag(text, cls=''):
    return ''.join(f'<p class="{cls}">{e(y.strip())}</p>' for y in text.split('\n') if y.strip())

def url_for(path:str, lang:str)->str:
    """Transform a canon rooted file URL to locale-correct relative path."""
    if not path: return '#'
    if path.startswith(('http://','https://','mailto:','#','tel:')): return path
    from_path = 'index.html' if lang=='zh' else 'en/index.html'
    return posixpath.relpath(path, posixpath.dirname(from_path) or '.')

def link_from(b:dict,lang:str)->str:
    val=b.get('links',{}).get(lang) if b.get('links') else None
    if val:return url_for(val,lang)
    return ''

def mk_cta(b,lang,label=None,cls='text-cta'):
    link=link_from(b,lang)
    if not link:return ''
    return f'<a class="{cls}" href="{e(link)}"><span>{e(label or LABEL[lang]["read"])}</span><span aria-hidden="true">↗</span></a>'

def numbering(i): return str(i).zfill(2)
def the_icon(which):
    d={
      'arrow':'<path d="M3 12h17m0 0-6-6m6 6-6 6"/>',
      'spark':'<path d="m12 2 2.3 7.7L22 12l-7.7 2.3L12 22l-2.3-7.7L2 12l7.7-2.3Z"/>',
      'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c6 5 6 13 0 18M12 3c-6 5-6 13 0 18"/>',
    }
    return '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4">'+d[which]+'</svg>'

def brand(lang):
    return '<a class="brand" href="'+ ('index.html' if lang=='zh' else 'index.html')+'" aria-label="NARQUE home"><span class="brand-cn" lang="zh-CN">序<span class="brand-rule">｜</span>束</span><span class="brand-en">NARQUE</span></a>'

def make_header(page,lang):
    paths={'zh':{},'en':{}}
    for p in PAGES:
        paths['zh'][p['id']]=url_for(p['path'],lang)
        paths['en'][p['id']]=url_for(p['path_en'],lang)
    other=page['path_en'] if lang=='zh' else page['path']
    switch=url_for(other,lang)
    links=''.join(f'<a class="nav-link {"active" if page["id"]==key else ""}" href="{e(paths[lang][key])}" {"aria-current=\"page\"" if page["id"]==key else ""}>{e(NAV[key]["nav_zh"] if lang=="zh" else NAV[key]["nav_en"])}</a>' for key in NAV_ORDER)
    mobile=links+f'<a class="mobile-lang" href="{e(switch)}">{e(LABEL[lang]["lang"])}</a>'
    return f'''<a class="skip-link" href="#main">{LABEL[lang]['skip']}</a>
<header class="site-header" id="top"><div class="shell header-inner">{brand(lang)}
  <nav class="site-nav" aria-label="{'主导航' if lang=='zh' else 'Primary navigation'}">{links}</nav>
  <div class="header-actions"><a class="language-switch" href="{e(switch)}" lang="{'en' if lang=='zh' else 'zh-CN'}" aria-label="{'Switch to English' if lang=='zh' else '切换到中文'}">{e(LABEL[lang]['lang'])}<span class="lang-arrow">↗</span></a>
   <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav"><span class="menu-icon"><i></i><i></i></span><span>{LABEL[lang]['menu']}</span></button></div></div>
 <nav class="mobile-nav" id="mobile-nav" aria-label="{'移动导航' if lang=='zh' else 'Mobile navigation'}" hidden>{mobile}</nav></header>'''


def hero_visual(page_id):
    """Fully CSS/SVG art with no network dependencies or raster placeholders."""
    if page_id in ('home','metre'):
        return '''<div class="hero-visual hero-orbit" aria-hidden="true"><div class="orbital-halo"></div><div class="orbital-core"></div><div class="orbital-ring ring-a"></div><div class="orbital-ring ring-b"></div><div class="orbital-ring ring-c"></div><div class="orbital-point pt-a"></div><div class="orbital-point pt-b"></div><div class="orbital-point pt-c"></div><div class="vector-axis axis-x"></div><div class="vector-axis axis-y"></div><div class="visual-caption">THEORY / REALITY<br>01—∞</div></div>'''
    if page_id=='xrem':
        return '''<div class="hero-visual hero-science" aria-hidden="true"><div class="discovery-field"></div><div class="discover-slab slab-one"></div><div class="discover-slab slab-two"></div><div class="discover-slab slab-three"></div><div class="discovery-beacon"></div><div class="science-track">OBSERVE · EXPLORE · VERIFY</div></div>'''
    if page_id=='aios':
        return '''<div class="hero-visual hero-capital" aria-hidden="true"><div class="capital-stack c-one"></div><div class="capital-stack c-two"></div><div class="capital-stack c-three"></div><div class="capital-line cl-a"></div><div class="capital-line cl-b"></div><div class="capital-line cl-c"></div><div class="capital-pulse"></div><span class="capital-note">SCARCITY / RIGHTS / VALUE</span></div>'''
    if page_id=='research':
        return '''<div class="hero-visual hero-research" aria-hidden="true"><div class="paper-form pf-a"></div><div class="paper-form pf-b"></div><div class="paper-form pf-c"><span>01</span><span>THE<br>MACHINE<br>ECONOMY</span></div><div class="research-plate">A CONTINUING BODY OF WORK</div></div>'''
    if page_id=='collaboration':
        return '''<div class="hero-visual hero-global" aria-hidden="true"><svg class="constellation" viewBox="0 0 560 500" preserveAspectRatio="xMidYMid meet"><g stroke="currentColor" stroke-width="1" fill="none" opacity=".33"><path d="M40 170 168 90 320 149 498 78M40 170 178 316 320 149 478 340M168 90 178 316 498 78 478 340M40 170 478 340"/></g><g fill="currentColor"><circle cx="40" cy="170" r="5"/><circle cx="168" cy="90" r="9"/><circle cx="320" cy="149" r="6"/><circle cx="498" cy="78" r="4"/><circle cx="178" cy="316" r="6"/><circle cx="478" cy="340" r="9"/></g><circle cx="280" cy="224" r="161" fill="none" stroke="currentColor" opacity=".24"/><circle cx="280" cy="224" r="210" fill="none" stroke="currentColor" opacity=".13"/></svg><div class="global-label">OPEN QUESTIONS. SHARED FRONTIERS.</div></div>'''
    return '''<div class="hero-visual hero-about" aria-hidden="true"><div class="identity-symbol"><span>序</span><i></i><span>束</span></div><div class="identity-caption">ORDER EMERGES THROUGH CONSTRAINT.</div></div>'''


def make_hero(page,lang):
    b=page['blocks'][0]; c=b[lang]
    label={'home':'NARQUE / MACHINE ECONOMY','metre':'01 / THEORETICAL RESEARCH','xrem':'02 / SCIENTIFIC DISCOVERY','aios':'03 / INVESTMENT REASONING','research':'04 / RESEARCH & PUBLICATIONS','collaboration':'05 / GLOBAL COLLABORATION','about':'06 / NARQUE IDENTITY'}[page['id']]
    # zh homepage contains deliberate clause boundaries; big headline with three lines
    if page['id']=='home':
        title='<span>'+('探索机器经济时代。' if lang=='zh' else 'Explore the Machine-Economy Era.')+'</span><span class="hero-title-em">'+('发现新的生产力。' if lang=='zh' else 'Discover What Comes Next.')+'</span><span>'+('布局未来的稀缺资本。' if lang=='zh' else 'Position for What Matters.')+'</span>'
    else:
        title=e(c['title'])
    btn=(f'<a class="action-primary" href="{e(url_for("metre.html" if lang=="zh" else "en/metre.html",lang))}">{e("探索三大体系" if lang=="zh" else "Explore the three systems")}{the_icon("arrow")}</a>' if page['id']=='home' else '')
    secondary=f'<a class="action-secondary" href="{e(url_for("collaboration.html" if lang=="zh" else "en/collaboration.html",lang))}">{e("国际科研合作" if lang=="zh" else "Research collaboration")} <span aria-hidden="true">↗</span></a>' if page['id']=='home' else ''
    return f'''<section class="page-hero {page['id']}-hero" aria-labelledby="page-title">{hero_visual(page['id'])}
 <div class="hero-ambient"></div><div class="shell hero-inner"><div class="hero-left"><div class="eyebrow"><span class="eyebrow-line"></span>{label}</div>
 <h1 id="page-title" class="hero-title">{title}</h1><div class="hero-deck">{ptag(c['text'])}</div>
 <div class="hero-links">{btn}{secondary}</div></div><span class="hero-count">{NUM[page['id']]} / 06</span></div>
 <div class="hero-bottom shell"><span>NARQUE · 2026</span><span>{e(LABEL[lang]['framework'])}</span><span>SCROLL TO EXPLORE ↓</span></div>
 </section>'''


def card_items(block,lang):
    lines=[line.strip() for line in block[lang]['text'].split('\n') if line.strip()]
    out=[]
    for line in lines:
        sep='｜' if '｜' in line else (' | ' if ' | ' in line else (': ' if ': ' in line else '：' if '：' in line else None))
        if sep: headline,body=line.split(sep,1)
        else:headline,body=line,''
        # preserve the full wording except the delimiter represented by heading/body treatment
        out.append((headline.strip(),body.strip()))
    return out


def make_cards(page_id,b,lang,index):
    c=b[lang]; key=b['id'].split('.')[-1]
    variants={'topics':'four','missions':'three','mechanism':'three','three':'three','scarcity':'three'}
    kind=variants.get(key,'three')
    cards=[]
    for i,(head,body) in enumerate(card_items(b,lang)):
        cards.append(f'''<article class="concept-card"><span class="concept-index">{numbering(i+1)} <span class="little-arrow">↗</span></span><h3>{e(head)}</h3><p>{e(body)}</p></article>''')
    return f'''<section class="section cards-section mode-{e(kind)}" id="{e(key)}"><div class="shell"><div class="section-heading"><span class="section-index">{numbering(index)} / {page_id.upper()}</span><h2>{e(c['title'])}</h2></div>
 <div class="concept-grid">{''.join(cards)}</div>{mk_cta(b,lang)}</div></section>'''


def make_essay(page_id,b,lang,index):
    c=b[lang]; key=b['id'].split('.')[-1]
    thesis=b['type']=='thesis'
    return f'''<section class="section essay-section {'thesis-section' if thesis else ''}" id="{e(key)}"><div class="shell essay-layout"><div class="essay-rail"><span class="section-index">{numbering(index)} / {page_id.upper()}</span><span class="rail-dot" aria-hidden="true"></span></div>
 <div class="essay-main"><h2>{e(c['title'])}</h2><div class="body-copy">{ptag(c['text'])}</div>{mk_cta(b,lang)}</div></div></section>'''


def make_feature(page_id,b,lang,index):
    c=b[lang]; key=b['id'].split('.')[-1]
    feature_name=b['id'].split('.')[1]
    accent='gold' if feature_name in ('metre','book','papers') else 'turquoise' if feature_name in ('xrem','mfd') else 'violet' if feature_name in ('aios','station','field') else 'neutral'
    # book without unverifiable sales URL: text is from canon, internal research CTA only.
    btn=mk_cta(b,lang)
    art=('<span class="feature-art-label">'+('MACHINE / ECONOMICS' if key in ('book','papers') else ('SCIENTIFIC / FRONTIER' if key in ('xrem','mfd') else ('VALUE / CAPITAL' if key in ('aios','bridge') else 'NARQUE / RESEARCH')))+'</span>'+
          '<div class="feature-art-glyph">'+('◇' if key in ('book','papers') else '✳' if key in ('mfd','xrem') else '∿' if key in ('aios','bridge') else '↗')+'</div>')
    return f'''<section class="section feature-section feature-{e(accent)}" id="{e(key)}"><div class="shell feature-grid"><div class="feature-content"><span class="section-index">{numbering(index)} / {page_id.upper()}</span><h2>{e(c['title'])}</h2><div class="body-copy">{ptag(c['text'])}</div>{btn}</div>
 <div class="feature-art" aria-hidden="true">{art}</div></div></section>'''


def make_partner(page_id,b,lang,index):
    c=b[lang]; key=b['id'].split('.')[-1]
    return f'''<section class="section partner-section" id="{e(key)}"><div class="shell partner-grid"><span class="partner-no">{numbering(index-1)}</span><div><span class="section-index">GLOBAL RESEARCH / {e(key.upper())}</span><h2>{e(c['title'])}</h2><div class="body-copy">{ptag(c['text'])}</div>{mk_cta(b,lang)}</div><span class="partner-star" aria-hidden="true">✳</span></div></section>'''


def make_framework(page_id,b,lang,index):
    c=b[lang]; key=b['id'].split('.')[-1]
    if page_id=='home':
        cards=''.join(f'<a class="engine-panel {kind}" href="{e(url_for("xrem.html" if kind=="xrem" else "aios.html" if kind=="aios" else "metre.html",lang))}"><span class="panel-num">{num}</span><span class="panel-tag">{tag[lang]}</span><strong>{kind.upper()}</strong><span class="panel-action">↗</span></a>' for num,kind,tag in [('02','xrem',{'zh':'找金矿 · 自主科学发现','en':'DISCOVER NEW KNOWLEDGE'}),('03','aios',{'zh':'抢码头 · 自主投资研究','en':'POSITION FOR SCARCITY'})])
        return f'''<section class="section framework-section" id="framework"><div class="shell"><span class="section-index">{numbering(index)} / THE ARCHITECTURE</span><h2>{e(c['title'])}</h2><p class="framework-intro">{e(c['text'])}</p>
 <div class="architecture"><a class="theory-stratum" href="{e(url_for('metre.html' if lang=='zh' else 'en/metre.html',lang))}"><span class="theory-num">01</span><div><span class="panel-tag">{e('机器经济基础理论 / THEORY' if lang=='zh' else 'THEORY FOUNDATION / MACHINE ECONOMICS')}</span><strong>METRE</strong></div><span class="stratum-arrow">↗</span></a>
 <div class="interlayer" aria-hidden="true"><span></span><b>{e('指导 · 验证 · 反馈' if lang=='zh' else 'GUIDANCE · EVIDENCE · FEEDBACK')}</b><span></span></div>
 <div class="engine-grid">{cards}</div></div></div></section>'''
    else:
        chunks=card_items(b,lang)
        cards=''.join(f'<div class="synthesis-row"><span>{numbering(i+1)}</span><h3>{e(h)}</h3><p>{e(txt)}</p></div>' for i,(h,txt) in enumerate(chunks))
        return f'''<section class="section framework-section about-framework" id="{e(key)}"><div class="shell"><span class="section-index">{numbering(index)} / THE ARCHITECTURE</span><h2>{e(c['title'])}</h2><div class="synthesis-grid">{cards}</div></div></section>'''


def make_closing(page_id,b,lang,index):
    c=b[lang];key=b['id'].split('.')[-1]
    cta=mk_cta(b,lang, LABEL[lang]['contact'],'closing-link')
    if page_id=='about':cta=f'<a class="closing-link" href="mailto:hello@narque.ai">hello@narque.ai <span aria-hidden="true">↗</span></a>'
    return f'''<section class="section closing-section" id="{e(key)}"><div class="shell closing-inner"><span class="section-index">{numbering(index)} / THE NEXT FRONTIER</span><h2>{e(c['title'])}</h2><p>{e(c['text'])}</p>{cta}<span class="closing-symbol" aria-hidden="true">N<span>／</span></span></div></section>'''


def make_home(page,lang):
    by_id={b['id']:b for b in page['blocks']}
    seg=[make_hero(page,lang),make_framework('home',by_id['home.framework'],lang,1)]
    # framework already exposes engine doors; three feature blocks add editorial depth and re-read the same fixed text.
    seg += [make_feature('home',by_id['home.metre'],lang,2)]
    seg += ['<div class="two-feature-doors">'+make_feature('home',by_id['home.xrem'],lang,3)+make_feature('home',by_id['home.aios'],lang,4)+'</div>']
    seg += [make_cards('home',by_id['home.missions'],lang,5)]
    seg += ['<div class="two-feature-doors">'+make_feature('home',by_id['home.publications'],lang,6)+make_feature('home',by_id['home.collaboration'],lang,7)+'</div>']
    seg += [make_closing('home',by_id['home.closing'],lang,8)]
    return ''.join(seg)


def make_page(page,lang):
    if page['id']=='home':return make_home(page,lang)
    html=[make_hero(page,lang)]
    for index,b in enumerate(page['blocks'][1:],start=1):
        tp=b['type']
        fn={'framework':make_framework,'essay':make_essay,'thesis':make_essay,'cards':make_cards,'feature':make_feature,'partner':make_partner,'closing':make_closing}[tp]
        html.append(fn(page['id'],b,lang,index))
    return ''.join(html)


def footer(page,lang):
    home=url_for('index.html' if lang=='zh' else 'en/index.html',lang)
    contact=url_for('about.html#contact' if lang=='zh' else 'en/about.html#contact',lang)
    pdf=url_for('NARQUE_Company_Introduction_Approved_FullText.pdf',lang)
    return f'''<footer class="site-footer"><div class="shell footer-grid"><div><a class="footer-wordmark" href="{e(home)}"><span lang="zh-CN">序｜束</span><b>NARQUE</b></a><p>{e(LABEL[lang]['copyright'])}</p></div><div class="footer-links"><a href="{e(contact)}">{e(LABEL[lang]['contact'])} ↗</a><a href="{e(pdf)}" download>{e(LABEL[lang]['download'])} ↓</a></div></div><div class="shell footer-bottom"><span>© 2026 NARQUE</span><span>METRE · XREM · AIOS</span><a href="#top">BACK TO TOP ↑</a></div></footer>'''


def page_output(page,lang):
    is_en=(lang=='en')
    outpath=page['path_en'] if is_en else page['path']
    localized_path=page['path_en'] if is_en else page['path']
    absolute=BASE_URL+localized_path
    lang_other=BASE_URL+(page['path'] if is_en else page['path_en'])
    css='../styles-v1.css' if is_en else 'styles-v1.css'
    js='../app-v1.js' if is_en else 'app-v1.js'
    subheader='en' if is_en else 'zh-CN'
    d=page['description_en'] if is_en else page['description_zh']
    title=page['seo_en'] if is_en else page['seo_zh']
    jsonld={"@context":"https://schema.org","@type":"WebPage","name":title,"url":absolute,"isPartOf":{"@type":"WebSite","name":"NARQUE","url":BASE_URL}}
    # Live canonical link is NOT included in staging output. Publish pipeline adds it when the user approves production, to avoid treating local branch as production.
    meta=f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0c1019"><title>{e(title)}</title><meta name="description" content="{e(d)}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(d)}"><meta property="og:url" content="{e(absolute)}">
<meta name="twitter:card" content="summary"><link rel="alternate" hreflang="zh-CN" href="{e(BASE_URL+page['path'])}"><link rel="alternate" hreflang="en" href="{e(BASE_URL+page['path_en'])}">
<link rel="alternate" hreflang="x-default" href="{e(BASE_URL+page['path'])}"><link rel="icon" type="image/svg+xml" href="{'../favicon.svg' if is_en else 'favicon.svg'}"><link rel="stylesheet" href="{e(css)}"><script type="application/ld+json">{json.dumps(jsonld,ensure_ascii=False).replace('</','<\\/')}</script>'''
    body=make_header(page,lang)+f'<main id="main" data-page-id="{e(page["id"])}">'+make_page(page,lang)+'</main>'+footer(page,lang)+f'<script defer src="{e(js)}"></script>'
    return '<!DOCTYPE html><html lang="'+subheader+'"><head>'+meta+'</head><body class="page-'+page['id']+' locale-'+lang+'">'+body+'</body></html>',outpath


def write_redirect(original:str,dest:str,lang:str):
    h=('<!DOCTYPE html><html lang="'+('en' if lang=='en' else 'zh-CN')+'"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><meta name="viewport" content="width=device-width,initial-scale=1">'
      +'<meta http-equiv="refresh" content="0; url='+e(dest)+'"><title>Moved / 页面已迁移</title></head><body><main><p>'+('This page has moved.' if lang=='en' else '页面已迁移。')+'</p><p><a href="'+e(dest)+'">'+('View new page' if lang=='en' else '前往新页面')+'</a></p></main></body></html>')
    path=ROOT/original;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(h,encoding='utf-8')


def main():
    files=[]
    for p in PAGES:
        for lang in ('zh','en'):
            html,outpath=page_output(p,lang)
            path=ROOT/outpath;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(html,encoding='utf-8');files.append(path)
    old=CANON['legacy_path_map'];keep={p['path'] for p in PAGES}|{p['path_en'] for p in PAGES}
    # no legacy bilingual pages in staging when they have not existed before; preserve old CN paths.
    for legacy,target in old.items():
        if legacy in keep:continue
        write_redirect(legacy,url_for(target,'zh'),'zh')
    # en.html legacy welcome currently points to English main
    write_redirect('en.html','en/index.html','en')
    # English legacy paths go to their locale equivalents
    for legacy,target in old.items():
        lp='en/'+legacy
        if lp in keep:continue
        # targets listed as root paths; keep within English when a corresponding new page exists
        base,_,hash_part=target.partition('#')
        en_target='en/'+base
        if en_target in keep:target='../'+en_target
        else:target='../'+base
        if hash_part:target+='#'+hash_part
        write_redirect(lp,target,'en')
    # Self-contained, crawlable site map: 14 canonical language pages, no legacy redirects.
    import datetime
    nodes=[]
    for pg in PAGES:
        for loc,alt in [(pg['path'],pg['path_en']),(pg['path_en'],pg['path'])]:
            pref='en' if loc.startswith('en/') else 'zh-CN'
            target='zh-CN' if pref=='en' else 'en'
            nodes.append('<url><loc>'+e(BASE_URL+loc)+'</loc><xhtml:link rel="alternate" hreflang="'+target+'" href="'+e(BASE_URL+alt)+'"/></url>')
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join(nodes)+'</urlset>',encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+BASE_URL+'sitemap.xml\n',encoding='utf-8')
    (ROOT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#101b23"/><path d="M13 47V17h7l16 21V17h7v30h-7L20 27v20Z" fill="#f7f5ed"/><path d="M49 15 42 49" stroke="#e1b96b" stroke-width="3"/></svg>',encoding='utf-8')
    r={'version':COPY_VER,'pages':len(PAGES),'languages':['zh','en'],'generated_html':len(files),'approved_parent_sha256':CANON['approved_parent_sha256'],'homepage':str(ROOT/'index.html'),'status':'STAGING_ONLY / NOT_DEPLOYED'}
    (ROOT/'build-manifest.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(r,ensure_ascii=False))

if __name__=='__main__':main()
