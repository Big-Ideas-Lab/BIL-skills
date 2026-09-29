#!/usr/bin/env python3
"""Dependency-free BIL V3 catalog contract validator."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
IDS=['person-marker','inline-citation','source-footer','reference-block','page-turner','section-label','progress-cue','media-frame','image-grid','key-metric','comparison','process-sequence','card']
def main():
 h=(ROOT/'index.html').read_text(); css=(ROOT/'catalog.css').read_text(); tok=(ROOT/'tokens.css').read_text(); e=[]
 def c(ok,msg):
  if not ok:e.append(msg);print('[FAIL]',msg)
 c(h.count('<h1')==1,'catalog must have one H1')
 c('href="catalog.css?v=40"' in h and 'href="bil-components.css?v=6"' in h and 'catalog.js?v=16' in h,'catalog cache version mismatch')
 order=['color','typography','assets','motion','components','slides']
 c(h.count('<h1')==1 and 'class="visually-hidden">BIG IDEAs Lab Design System</h1>' in h and '<span>Design System</span>' in h,'catalog H1/header mismatch')
 c(all('id="'+x+'"' in h for x in order),'required IA sections missing')
 c([h.index('id="'+x+'"') for x in order]==sorted(h.index('id="'+x+'"') for x in order),'exact IA order mismatch')
 c('<a aria-current="location" href="#color">Color</a>' in h,'Color must be initially active')
 c('id="buttons"' not in h and '>Buttons<' not in h,'button catalog section must be absent')
 c(all(x in h for x in ['<strong>Display</strong><span>Source Serif 4</span>','<strong>Interface</strong><span>Inter</span>','<strong>Data</strong><span>IBM Plex Mono</span>','Three self-hosted, free, open-source families','SIL Open Font License']) and h.count('class="license"')==3,'font role overview incomplete')
 c(not any(x in h for x in ['PP Neue Montreal','Sharp Type','licensed','Georgia','Helvetica Neue','SFMono-Regular']),'catalog must not reference licensed or system fallback fonts')
 faces=re.findall(r'@font-face\s*\{[^}]*\}',h+tok)
 c(len(faces)==4 and all("url(\"assets/fonts/" in f for f in faces) and sorted(re.findall(r'font-family:\s*([^;]+);',x)[0].strip().strip('"') for x in faces)==['IBM Plex Mono','IBM Plex Mono','Inter','Source Serif 4'],'webfont contract must be four self-hosted faces across three free families')
 c(re.search(r'--font-display:\s*"Source Serif 4",\s*serif',tok) and re.search(r'--font-sans:\s*"Inter",\s*sans-serif',tok) and re.search(r'--font-mono:\s*"IBM Plex Mono",\s*monospace',tok),'type-role families must be Source Serif 4, Inter, IBM Plex Mono')
 c(not re.search(r'fonts\.(googleapis|gstatic)\.com',h+css+tok),'catalog must self-host fonts instead of hotlinking a CDN')
 c(re.search(r'\.catalog-section>h2,[^{]*\{[^}]*var\(--font-display\)',css) and '[style*="font-family"]' not in h and ' font-family:"' not in h,'section headings must use the display family without inline font overrides')
 c(h.count('class="agent-example"')==6 and h.count('aria-label="Example agent prompt"')==6,'each catalog section needs one agent prompt example')
 hw=h.replace('<wbr>','')
 c('Using assets with an agent' in h and h.count('data-copy-text=')==12 and hw.count('<span class="asset-file"><b>design-system/assets/')==12 and h.count('<span class="asset-open">Agent prompt</span>')==12 and h.count('<wbr>')==12 and 'design-system/assets/' in h,'asset agent guidance incomplete')
 c(h.count('data-component="')==13 and all(x in h for x in IDS),'13 component specimens missing')
 c(h.count('data-motion=')==3,'motion contract incomplete')
 c(all(x in h for x in ['data-layout="title"','data-layout="title-media"','data-layout="regular"','id="inspect-title"','id="inspect-title-media"','id="inspect-regular"']),'slide picker incomplete')
 c(h.count('class="thumb-stage slide-stage title-media"')==2 and 'id="inspect-title-media" class="thumb-stage slide-stage title-media"' in h,'catalog Title with Media stage wiring mismatch')
 turners=re.findall(r'<nav class="slide-page-turner"[^>]*>.*?</nav>',h,re.S)
 c(len(turners)==6,'catalog must contain exactly six static slide turners')
 c(all(t.count('<output')==1 for t in turners),'catalog slide turners must contain one tracker each')
 c(all('aria-label="Media placeholder"' in x for x in re.findall(r'<div class="slide-media".*?</div>',h,re.S)),'catalog media placeholder label mismatch')
 c(h.count('aria-label="Slide 1 of 3"')==2 and h.count('aria-label="Slide 2 of 3"')==2 and h.count('aria-label="Slide 3 of 3"')==2,'catalog slide turner positions mismatch')
 c(h.count('Presenter Name</span> · <span data-slot="date">Presentation Date')>=4,'catalog metadata specimens missing')
 thumb_buttons=re.findall(r'<button class="layout-option".*?</button>',h,re.S)
 c(len(thumb_buttons)==3 and all(b.count('<button')==1 for b in thumb_buttons),'thumbnail layout buttons malformed')
 c(all(re.search(r'<nav class="slide-page-turner"[^>]*>\s*<span class="slide-page-turner-icon',b,re.S) and b.count('slide-page-turner-icon')==2 and b.count('<output')==1 for b in thumb_buttons),'thumbnail turners must use visual spans')
 inspect=h[h.index('id="inspect-title"'):]
 c(inspect.count('<button type="button" aria-label="Previous slide"')==3 and inspect.count('<button type="button" aria-label="Next slide"')==3 and inspect.count('<output')==3,'inspect turners must retain real controls')
 regular_button=h[h.index('data-layout="regular"'):h.index('</button>',h.index('data-layout="regular"'))]; regular_preview=h[h.index('id="inspect-regular"'):h.index('</div>',h.index('id="inspect-regular"'))]
 asset='assets/decor/bil-opening-sunburst-spectral-edge.png'
 c(h.count(asset)==4 and asset not in regular_button and asset not in regular_preview,'catalog optical scope mismatch')
 c('.bil-bend' not in css and '.bil-ribbon' not in css and '.opening-optical' in css,'catalog optical class mismatch')
 c('inset:0;width:100%;height:100%;object-fit:contain' in css and '.slide-logo{position:absolute;right:44px;top:39px;width:422px;z-index:5}' in css,'catalog opening geometry mismatch')
 c('.title-copy' in css and 'font-size:80px;line-height:1.08' in css and 'margin:25px 0 0;width:1100px;max-width:1100px;white-space:nowrap' in css,'catalog Title screenshot geometry/type mismatch')
 c('title-media h3{position:absolute;left:120px;top:54px;max-width:960px;margin:0;font:600 60px/1.02 Inter,sans-serif;letter-spacing:-.03em' in css and 'title-media p{position:absolute;left:120px;top:196px' in css and '.slide-stage.title-media .slide-media{left:370px;top:270px;width:1180px;height:660px' in css and 'object-fit:contain;background:#E5E7EB' in css and 'regular h3{position:absolute;left:120px;top:60px;max-width:960px;margin:0;font:600 60px/1.02 Inter,sans-serif;letter-spacing:-.03em' in css and '.slide-stage.regular p' not in css,'catalog comparison heading geometry mismatch')
 c('title-opening h3{position:relative;left:auto;top:auto;max-width:none;margin:0;font-size:80px;line-height:1.08' in css and '.slide-stage.title-opening .title-copy{position:absolute;left:134px;top:378px' in css,'opening Title geometry changed')
 c('right:300px;top:72px;width:240px' not in css and 'right:120px;top:72px;width:270px' not in css,'catalog legacy logo geometry leaked')
 c('title-copy' in h and 'Presenter Name' in h and 'Presentation Date' in h and 'data-slot="presenter"' in h and 'data-slot="date"' in h and 'data-slot="institution"' not in h,'catalog Title metadata contract mismatch')
 c('Ideas that move<br>the world.' in h and h.count('title-opening')==2 and 'font-size:108px' not in css,'catalog Title specimen mismatch')
 c((ROOT/'assets/decor/bil-opening-sunburst-spectral-edge.png').exists(),'decorative optical asset missing')
 for name in ['title.html','title-media.html']:
  t=(ROOT.parent/'slide-templates/starters'/name).read_text(); starter_geometry=('right:44px;top:39px;width:422px' in t and 'right:300px;top:72px;width:240px' not in t and 'right:120px;top:72px;width:270px' not in t and '.title-copy{position:absolute;left:134px;top:378px;width:672px;max-width:672px' in t and 'margin:25px 0 0;width:1100px;max-width:1100px;white-space:nowrap' in t and 'font:400 80px/1.08' in t and 'top:620px' not in t and 'Presenter · Date' not in t) if name=='title.html' else ('right:44px;top:39px;width:422px' in t and 'right:300px;top:72px;width:240px' not in t and 'right:120px;top:72px;width:270px' not in t); c(asset in t and '.bend' not in t and '.ribbon' not in t and '.opening-optical{' in t and 'inset:0;width:100%;height:100%;object-fit:contain' in t and starter_geometry and t.count('black_duke_bigideaslab.png')==1,'starter opening geometry mismatch '+name)
  if name=='title-media.html': c('left:370px;top:270px;width:1180px;height:660px' in t and 'left:120px;top:54px;z-index:4;max-width:960px' in t and 'left:120px;top:196px' in t and 'object-fit:contain' in t and 'font:600 60px/1.02 Inter,sans-serif;letter-spacing:-.03em' in t and 'Presenter · Date' not in t,'starter media geometry mismatch')
 reg=(ROOT.parent/'slide-templates/starters/regular.html').read_text(); c(asset not in reg and 'opening-optical' not in reg and 'left:120px;top:60px;max-width:960px' in reg and 'font:600 60px/1.02 Inter,sans-serif;letter-spacing:-.03em' in reg and 'Study overview' in reg and 'data-slot="main"' in reg and 'Presenter Name' not in reg and 'Presentation Date' not in reg and 'class="meta"' not in reg,'Regular starter contract mismatch')
 combo=(ROOT.parent/'slide-templates/bil-lab-presentation-template.html').read_text(); c(combo.count(asset)==2 and '.bend' not in combo and combo.count('inset:0;width:100%;height:100%;object-fit:contain')==1 and combo.count('black_duke_bigideaslab.png')==3 and combo.count('.logo{position:absolute;right:44px;top:39px;width:422px;z-index:5}')==1 and 'right:300px;top:72px;width:240px' not in combo and 'right:120px;top:72px;width:270px' not in combo,'combined starter opening geometry mismatch'); c('Presenter Name' in combo and 'Presentation Date' in combo and '<div class="title-copy"><h1 class="title">Ideas that move<br>the world.</h1><p class="meta">' in combo and 'left:370px;top:270px;width:1180px;height:660px' in combo and 'object-fit:contain' in combo and 'Optional side rail' not in combo,'combined layout contracts mismatch')
 c('<h2 class="title">Study overview</h2><div class="main" data-slot="main"></div>' in combo and combo[combo.index('<section id="regular"'):].count('Presenter Name')==0 and combo[combo.index('<section id="regular"'):].count('Presentation Date')==0 and combo[combo.index('<section id="regular"'):].count('class="meta"')==0 and '.regular .meta' not in combo,'combined Regular content contract mismatch')
 c('Title + Media' not in combo and 'Title + media' not in combo and 'Ideas that move<br>the world.' in combo and 'aria-label="Media placeholder"' in combo and '<span>MEDIA</span>' not in combo and 'background:#E5E7EB' in combo and 'width:96px;height:96px' in combo and 'data-page-turner-slide' in combo and 'height:56px' in combo,'combined template visible contract mismatch')
 c(re.search(r'--radius-card:\s*16px', tok) and 'border-radius:var(--radius-card' in (ROOT/'bil-components.css').read_text(),'card radius contract mismatch: the rounded card edge must come from --radius-card')
 c('--media-radius:32px' in (ROOT/'bil-components.css').read_text() and 'border:0;outline:0;border-radius:var(--media-radius)' in css,'shared media contract mismatch')
 c(asset not in reg and 'right:300px;top:72px;width:240px' not in reg,'Regular starter geometry exclusion mismatch')
 m=json.loads((ROOT/'components-manifest.json').read_text());c([x['id'] for x in m['components']]==IDS,'component manifest mismatch');c('buttons' in m,'button manifest missing')
 c('index.html#components' in (ROOT/'components.html').read_text() and 'index.html#slides' in (ROOT/'slides.html').read_text(),'fallback redirects missing')
 if e: print('Validation failed:',len(e));return 1
 print('Validation complete: 1 canonical catalog, button section omitted, 13 components, 3 motion patterns, 3 layouts passed.');return 0
if __name__=='__main__':sys.exit(main())
