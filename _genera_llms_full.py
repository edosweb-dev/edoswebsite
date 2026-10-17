"""Rigenera llms-full.txt con il testo intero delle pagine pubbliche. Dalla radice del repo."""
import re, html
from html.parser import HTMLParser

SITE = 'https://www.edos.it'
SKIP = {'script', 'style', 'svg', 'nav', 'footer', 'form', 'noscript', 'button', 'select', 'template', 'header', 'dialog'}
BLOCK = {'p', 'li', 'h1', 'h2', 'h3', 'h4', 'figcaption', 'blockquote', 'dt', 'dd', 'td', 'th', 'summary'}
VOID = {'img', 'br', 'hr', 'input', 'meta', 'link', 'source', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon'}

class T(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.skip = 0; s.stack = []; s.out = []; s.cur = None; s.buf = ''
    def handle_starttag(s, t, a):
        a = dict(a); cls = a.get('class') or ''
        if t in VOID: return
        hide = t in SKIP or a.get('aria-hidden') == 'true' or re.search(r'\b(mm-|cookie|cs-lb|nav-|mega|sr-only|marquee|logos?-strip|hn-scena|hn-modello|hn-pratica|chat-mock|az-telefono)', cls)
        s.stack.append((t, bool(hide)))
        if hide: s.skip += 1
        kind = t if t in BLOCK else ('num' if 'res-card-num' in cls else 'li' if re.search(r'(stack-item-name|svc-item)', cls) else None)
        if not s.skip and kind: s.flush(); s.cur = kind; s.stack[-1] = (t, False, True)
    def handle_endtag(s, t):
        if t in VOID: return
        if not s.skip and s.cur: s.buf += ' '
        while s.stack:
            e = s.stack.pop(); tt, hide = e[0], e[1]
            if hide: s.skip -= 1
            if len(e) > 2 and not s.skip: s.flush()
            if tt == t: break
        if not s.skip and t in BLOCK: s.flush()
    def handle_data(s, d):
        if not s.skip and s.cur: s.buf += d
    def flush(s):
        txt = ' '.join(s.buf.split())
        if txt and s.cur:
            pre = {'h1': '# ', 'h2': '## ', 'h3': '### ', 'h4': '#### ', 'li': '- '}.get(s.cur, '')
            if s.cur == 'num': s.out.append('§' + txt)
            elif s.out and s.out[-1].startswith('§') and pre.startswith('#'): s.out[-1] = pre + s.out[-1][1:] + ' · ' + txt
            elif not (s.out and s.out[-1] == pre + txt): s.out.append(pre + txt)
        s.cur = None; s.buf = ''

def page(f):
    raw = open(f, encoding='utf-8').read()
    body = raw[raw.find('<body'):]
    p = T(); p.feed(body); p.flush()
    lines = [l.lstrip('§') for l in p.out if len(l) > 2 or l.startswith('§')]
    # titoli una sola volta, h1 portato a h2 nella raccolta
    out = []
    for l in lines:
        if l.startswith('# '): l = '#' + l
        elif l.startswith('#'): l = '#' + l
        out.append(l)
    return out

def meta(f, name):
    raw = open(f, encoding='utf-8').read()
    m = re.search(r'<meta name="%s" content="([^"]*)"' % name, raw)
    return html.unescape(m.group(1)) if m else ''

ORDER = ['index.html', 'azienda/index.html', 'servizi/index.html'] + \
    ['servizi/%s/index.html' % s for s in ['gestionali-su-misura', 'ai-nelle-pratiche', 'app-web-app', 'interfacce-semplici', 'assistenza-evoluzione', 'siti-ecommerce']] + \
    ['per-le-agenzie/index.html', 'case-study/index.html']
import glob
ORDER += sorted(f.replace('\\', '/') for f in glob.glob('case-study/*/index.html'))
ORDER += ['contatti/index.html']

head = open('llms.txt', encoding='utf-8').read().split('\n## ')[0].strip()
parts = [head.replace('# Edos', '# Edos · testo completo del sito', 1),
         'Questo file raccoglie il testo delle pagine pubbliche di www.edos.it, una dopo l’altra. L’indice breve è in https://www.edos.it/llms.txt.',
         'Edos Srl · P.IVA 14030760962 · Via Giovanni Gioacchino Winckelmann 1, 20146 Milano · info@edos.it · +39 388 342 4454']
for f in ORDER:
    url = SITE + '/' + f.removesuffix('index.html')
    body = page(f)
    if f.startswith('case-study/') and f != 'case-study/index.html':
        # le card «altri progetti» in fondo ripetono le altre case study
        for i, l in enumerate(body):
            if re.match(r'#+ (Altri case study|Altri progetti|Altre case study|Progetti correlati|Potrebbe interessarvi)', l): body = body[:i]; break
    parts.append('\n---\n\nURL: ' + url + '\n' + ('Descrizione: ' + meta(f, 'description') + '\n' if meta(f, 'description') else '') + '\n' + '\n\n'.join(body))
open('llms-full.txt', 'w', encoding='utf-8', newline='\n').write('\n\n'.join(parts).strip() + '\n')
print(sum(len(x) for x in parts), 'caratteri')
