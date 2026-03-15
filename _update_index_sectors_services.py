#!/usr/bin/env python3
"""Update /case-study/index.html, sector pages, service pages with new 30 case studies."""
import os, re

BASE = '/home/user/edoswebsite'

# Import data from generator script
exec(open(os.path.join(BASE, '_generate_case_studies.py')).read())

# ─── 1. UPDATE /case-study/index.html ───
def gen_index_page():
    cards_html = []
    for cs in CASES:
        cards_html.append(f'''    <a href="/case-study/{cs['slug']}" class="c-item reveal-scale" data-type="{cs['data_type']}" data-sector="{cs['data_sector']}">
      <div class="c-num">{cs['num']}</div>
      <p class="c-title">{cs['card_title']}</p>
      <p class="c-desc">{cs['card_desc']}</p>
      <div class="c-meta">
        <div class="c-meta-item">
          <div class="c-meta-label">Settore</div>
          <div class="c-meta-value">{cs['card_sector']}</div>
        </div>
        <div class="c-meta-item">
          <div class="c-meta-label">Servizio</div>
          <div class="c-meta-value">{cs['card_service']}</div>
        </div>
      </div>
      <span class="c-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
    </a>
''')
    
    index_path = os.path.join(BASE, 'case-study', 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace filters section
    old_filters = re.search(r'(<div class="cases-filters.*?</div>\s*</div>\s*</div>)', html, re.DOTALL)
    new_filters = '''<div class="cases-filters reveal">
      <div class="cf-row">
        <span class="cf-label">Per servizio</span>
        <button class="cf-btn active" data-filter="all">Tutti</button>
        <button class="cf-btn" data-filter="type:ecommerce">E-commerce</button>
        <button class="cf-btn" data-filter="type:platform">Piattaforme</button>
        <button class="cf-btn" data-filter="type:ai">AI</button>
        <button class="cf-btn" data-filter="type:app">App</button>
        <button class="cf-btn" data-filter="type:web">Web</button>
        <button class="cf-btn" data-filter="type:advisory">Advisory</button>
      </div>
      <div class="cf-row">
        <span class="cf-label">Per settore</span>
        <button class="cf-btn" data-filter="sector:retail">Retail</button>
        <button class="cf-btn" data-filter="sector:energy">Energy</button>
        <button class="cf-btn" data-filter="sector:fashion">Fashion</button>
        <button class="cf-btn" data-filter="sector:tech">Tech</button>
        <button class="cf-btn" data-filter="sector:health">Health</button>
        <button class="cf-btn" data-filter="sector:industry">Industry</button>
        <button class="cf-btn" data-filter="sector:food">Food</button>
        <button class="cf-btn" data-filter="sector:finance">Finance</button>
        <button class="cf-btn" data-filter="sector:hospitality">Hospitality</button>
        <button class="cf-btn" data-filter="sector:automotive">Automotive</button>
        <button class="cf-btn" data-filter="sector:wellness">Wellness</button>
      </div>
    </div>'''
    
    if old_filters:
        html = html.replace(old_filters.group(1), new_filters)
    
    # Replace grid content
    grid_match = re.search(r'(<div class="cases-grid"[^>]*>)(.*?)(</div>\s*<div class="cases-empty")', html, re.DOTALL)
    if grid_match:
        html = html.replace(grid_match.group(0), 
            grid_match.group(1) + '\n\n' + '\n'.join(cards_html) + '\n  ' + grid_match.group(3))
    
    # Replace footer with new footer
    footer_match = re.search(r'<footer class="footer">.*?</footer>', html, re.DOTALL)
    if footer_match:
        html = html.replace(footer_match.group(0), FOOTER)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated /case-study/index.html with 30 cards and new filters")

gen_index_page()

# ─── 2. UPDATE SECTOR PAGES ───
SECTOR_CASES = {}
for cs in CASES:
    sector_path = cs['sector_link'].replace('/settori/', '')
    if sector_path not in SECTOR_CASES:
        SECTOR_CASES[sector_path] = []
    SECTOR_CASES[sector_path].append(cs)

for sector_slug, cases in SECTOR_CASES.items():
    sector_file = os.path.join(BASE, 'settori', sector_slug, 'index.html')
    if not os.path.exists(sector_file):
        print(f"  Sector page not found: {sector_slug}")
        continue
    
    with open(sector_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build new case study cards
    cards = []
    for cs in cases:
        cards.append(f'''      <a href="/case-study/{cs['slug']}" class="cs-card reveal">
        <p class="cs-card-title">{cs['card_title']}</p>
        <p class="cs-card-desc">{cs['card_desc']}</p>
        <div class="cs-card-meta"><span>{cs['card_sector']}</span></div>
      </a>''')
    
    new_grid = '<div class="cs-grid">\n' + '\n'.join(cards) + '\n    </div>'
    
    # Replace the cs-grid section
    grid_match = re.search(r'<div class="cs-grid">.*?</div>\s*</div>\s*</div>\s*</section>', html, re.DOTALL)
    if grid_match:
        old = grid_match.group(0)
        # Keep the closing tags
        new = new_grid + '\n  </div>\n</div>\n</section>'
        html = html.replace(old, new)
    
    # Also update footer
    footer_match = re.search(r'<footer class="footer">.*?</footer>', html, re.DOTALL)
    if footer_match:
        html = html.replace(footer_match.group(0), FOOTER)
    
    with open(sector_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Updated settori/{sector_slug} with {len(cases)} case studies")

# ─── 3. UPDATE SERVICE PAGES ───
SERVICE_CASES = {}
for cs in CASES:
    service_path = cs['service_link'].replace('/servizi/', '')
    if service_path not in SERVICE_CASES:
        SERVICE_CASES[service_path] = []
    SERVICE_CASES[service_path].append(cs)

for service_slug, cases in SERVICE_CASES.items():
    service_file = os.path.join(BASE, 'servizi', service_slug, 'index.html')
    if not os.path.exists(service_file):
        print(f"  Service page not found: {service_slug}")
        continue
    
    with open(service_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build new case study cards (max 4 for service pages)
    display_cases = cases[:4]
    cards = []
    for cs in display_cases:
        cards.append(f'''      <a href="/case-study/{cs['slug']}" class="cs-card reveal">
        <p class="cs-card-title">{cs['card_title']}</p>
        <p class="cs-card-desc">{cs['card_desc']}</p>
        <div class="cs-card-meta"><span>{cs['card_sector']}</span></div>
      </a>''')
    
    new_grid = '<div class="cs-grid">\n' + '\n'.join(cards) + '\n    </div>'
    
    # Replace the cs-grid section
    grid_match = re.search(r'<div class="cs-grid">.*?</div>\s*</div>\s*</div>\s*</section>', html, re.DOTALL)
    if grid_match:
        old = grid_match.group(0)
        new = new_grid + '\n  </div>\n</div>\n</section>'
        html = html.replace(old, new)
    
    # Also update footer
    footer_match = re.search(r'<footer class="footer">.*?</footer>', html, re.DOTALL)
    if footer_match:
        html = html.replace(footer_match.group(0), FOOTER)
    
    with open(service_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Updated servizi/{service_slug} with {len(display_cases)} case studies")

print("\nAll updates complete!")
