import re
import os
from PIL import Image
import numpy as np

with open(r'c:\xampp\htdocs\intact\ceiling.php', 'r', encoding='utf-8') as f:
    html = f.read()

card_matches = re.findall(r'<article class="ceiling-finish-item finish-item ([^"]+)">([\s\S]*?)</article>', html)

def classify_img(pil_img):
    img = np.array(pil_img.resize((500, 500)))
    # Sample groove columns at x=171 and x=330
    g1 = img[:, 168:174, :].mean(axis=(0,1))
    g2 = img[:, 327:333, :].mean(axis=(0,1))
    groove = (g1 + g2) / 2
    r, g, b = groove
    bright = (r + g + b) / 3
    if bright < 60:
        return 'SIMPLE (Black)', groove
    # If yellow hue (R and G high, B low)
    if (g - b) > 28:
        return 'GOLDEN', groove
    if (r - g) > 15:
        return 'COPPER', groove
    return f'OTHER ({r:.0f},{g:.0f},{b:.0f})', groove

errors = []
for i, (cat, content) in enumerate(card_matches):
    title_m = re.search(r'<h3 class="finish-card-title">\s*([^<]+)<span class="finish-code">\(([^)]+)\)</span>', content)
    title = title_m.group(1).strip() if title_m else 'Unknown'
    code = title_m.group(2).strip() if title_m else 'Unknown'
    
    img_m = re.search(r'<img [^>]*src="([^"]+)"[^>]*data-simple="([^"]+)"[^>]*data-golden="([^"]+)"[^>]*data-copper="([^"]+)"', content)
    src, simple, golden, copper = img_m.groups()
    
    s_img = Image.open(r'c:\xampp\htdocs\intact\\' + simple.replace('/', os.sep)).convert('RGB')
    g_img = Image.open(r'c:\xampp\htdocs\intact\\' + golden.replace('/', os.sep)).convert('RGB')
    c_img = Image.open(r'c:\xampp\htdocs\intact\\' + copper.replace('/', os.sep)).convert('RGB')
    
    s_cls, s_rgb = classify_img(s_img)
    g_cls, g_rgb = classify_img(g_img)
    c_cls, c_rgb = classify_img(c_img)
    
    is_ok = True
    if 'SIMPLE' not in s_cls:
        is_ok = False
        errors.append(f'Card {i+1} ({title} {code}): Simple mapped to {simple} which is {s_cls}')
    if 'GOLDEN' not in g_cls:
        is_ok = False
        errors.append(f'Card {i+1} ({title} {code}): Golden mapped to {golden} which is {g_cls}')
    if 'COPPER' not in c_cls:
        is_ok = False
        errors.append(f'Card {i+1} ({title} {code}): Copper mapped to {copper} which is {c_cls}')
        
    status = 'OK' if is_ok else 'WRONG'
    print(f'Card {i+1:02d} [{code}] {title:25s}: {status}')
    if not is_ok:
        print(f'   data-simple = {simple:30s} -> {s_cls}')
        print(f'   data-golden = {golden:30s} -> {g_cls}')
        print(f'   data-copper = {copper:30s} -> {c_cls}')

print('\nTotal errors found:', len(errors))
for e in errors:
    print(' -', e)
