"""Crawl di un sito statico: link, stati, title, description, canonical, h1, alt, JSON-LD.
uso: python crawl.py https://www.edos.it [out.json]"""
import sys, json, re, urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser

BASE = sys.argv[1].rstrip('/')
OUT = sys.argv[2] if len(sys.argv) > 2 else None
HOST = urllib.parse.urlparse(BASE).netloc

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None
opener = urllib.request.build_opener(NoRedirect)

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 edos-audit', 'Cookie': __import__('os').environ.get('CK', '')})
    try:
        r = opener.open(req, timeout=20)
        return r.status, r.headers.get('Location'), r.read().decode('utf-8', 'replace'), r.headers.get('Content-Type', '')
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get('Location'), '', e.headers.get('Content-Type', '')
    except Exception as e:
        return 0, None, str(e), ''

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.links=[]; s.res=[]; s.title=''; s.in_t=False; s.desc=None; s.canon=None
        s.h1=0; s.imgs_noalt=[]; s.ld=[]; s.in_ld=False; s.buf=''; s.robots=None; s.og={}; s.lang=None; s.h=[]; s.in_h=None; s.text=[]; s.skip=0
    def handle_starttag(s, t, a):
        a = dict(a)
        if t=='html': s.lang=a.get('lang')
        if t=='a' and a.get('href'): s.links.append(a['href'])
        if t=='img':
            s.res.append(a.get('src') or '')
            if a.get('alt') is None or not a.get('alt','').strip():
                if a.get('aria-hidden')!='true' and a.get('alt') is None or (a.get('alt')=='' and a.get('role')!='presentation'):
                    s.imgs_noalt.append((a.get('src'), a.get('alt')))
        if t=='link' and a.get('href'):
            if a.get('rel')=='canonical': s.canon=a['href']
            elif a.get('rel') in ('stylesheet','icon','preload','apple-touch-icon','manifest'): s.res.append(a['href'])
        if t=='script':
            if a.get('src'): s.res.append(a['src'])
            if a.get('type')=='application/ld+json': s.in_ld=True; s.buf=''
            else: s.skip+=1
        if t=='style': s.skip+=1
        if t=='meta':
            n=(a.get('name') or a.get('property') or '').lower()
            if n=='description': s.desc=a.get('content')
            if n=='robots': s.robots=a.get('content')
            if n.startswith('og:'): s.og[n]=a.get('content')
        if t=='title': s.in_t=True
        if t=='h1': s.h1+=1
        if t in ('h1','h2','h3'): s.in_h=t; s.h.append([t,''])
    def handle_endtag(s, t):
        if t=='title': s.in_t=False
        if t=='script':
            if s.in_ld: s.ld.append(s.buf); s.in_ld=False
            else: s.skip=max(0,s.skip-1)
        if t=='style': s.skip=max(0,s.skip-1)
        if t in ('h1','h2','h3'): s.in_h=None
    def handle_data(s, d):
        if s.in_t: s.title+=d
        if s.in_ld: s.buf+=d
        elif not s.skip: s.text.append(d)
        if s.in_h and s.h: s.h[-1][1]+=d

def norm(u, page):
    u = urllib.parse.urljoin(page, u)
    p = urllib.parse.urlparse(u)
    if p.scheme not in ('http','https'): return None
    return urllib.parse.urlunparse((p.scheme, p.netloc, p.path, '', p.query, ''))

seen, queue, pages, checked = set(), [BASE + '/'], {}, {}
extra = []
while queue:
    url = queue.pop(0)
    if url in seen: continue
    seen.add(url)
    st, loc, body, ct = fetch(url)
    checked[url] = (st, loc)
    if st in (301,302,307,308) and loc:
        nxt = norm(loc, url)
        if nxt and urllib.parse.urlparse(nxt).netloc == HOST: queue.append(nxt)
        continue
    if st != 200 or 'html' not in ct: continue
    p = P(); p.feed(body)
    words = len(re.findall(r'\w+', ' '.join(p.text)))
    lds = []
    for raw in p.ld:
        try: lds.append(json.loads(raw))
        except Exception as e: lds.append({'_ERROR': str(e)})
    pages[url] = dict(title=p.title.strip(), desc=p.desc, canon=p.canon, h1=p.h1, noalt=p.imgs_noalt,
                      ld=lds, robots=p.robots, og=p.og, lang=p.lang, words=words, links=[], res=[],
                      heads=[(t, ' '.join(x.split())) for t,x in p.h])
    for l in p.links:
        n = norm(l, url)
        if not n: continue
        pages[url]['links'].append(n)
        if urllib.parse.urlparse(n).netloc == HOST and n not in seen: queue.append(n)
        elif urllib.parse.urlparse(n).netloc != HOST: extra.append((url, n))
    for r in p.res:
        n = norm(r, url)
        if n: pages[url]['res'].append(n)

# risorse e link esterni
res_all = {r for pg in pages.values() for r in pg['res']}
for r in res_all:
    if r not in checked: checked[r] = fetch(r)[:2]
ext = {}
for src, n in extra:
    if n not in ext:
        st, loc, _, _ = fetch(n); ext[n] = (st, loc, src)

json.dump(dict(pages=pages, checked=checked, ext=ext), open(OUT or 'crawl.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('pagine html 200:', len(pages), ' url controllati:', len(checked), ' esterni:', len(ext))
