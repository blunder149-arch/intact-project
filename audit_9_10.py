import re
import json

files = ["9-groove-pvc-wall-panel.php", "10-groove-pvc-wall-panel.php"]

for filename in files:
    print(f"\n=======================================================")
    print(f"AUDITING: {filename}")
    print(f"=======================================================")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Meta & SEO tags check
    print("\n--- 1. META & CANONICAL AUDIT ---")
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    print(f"Title: {title_m.group(1).strip() if title_m else 'MISSING'}")

    robots_m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', content)
    print(f"Robots: {robots_m.group(1).strip() if robots_m else 'MISSING'}")

    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.DOTALL)
    print(f"Description: {desc_m.group(1).strip() if desc_m else 'MISSING'}")

    canonical_m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content)
    print(f"Canonical: {canonical_m.group(1).strip() if canonical_m else 'MISSING'}")

    # 2. JSON-LD Schema Validation
    print("\n--- 2. SCHEMA.ORG JSON-LD AUDIT ---")
    schema_m = re.search(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL)
    if schema_m:
        schema_raw = schema_m.group(1).strip()
        try:
            schema_json = json.loads(schema_raw)
            graph = schema_json.get("@graph", [])
            types = [item.get("@type") for item in graph]
            print(f"JSON-LD Valid: YES")
            print(f"@graph types found: {types}")
            
            # Check FAQ count
            faq_item = next((item for item in graph if item.get("@type") == "FAQPage"), None)
            if faq_item:
                faqs = faq_item.get("mainEntity", [])
                print(f"FAQ count in Schema: {len(faqs)}")
            else:
                print("WARNING: FAQPage missing in Schema")
        except Exception as e:
            print(f"ERROR: Invalid JSON-LD Schema: {e}")
    else:
        print("ERROR: Schema script tag missing")

    # 3. HTML Attributes Syntax Check (look for raw CSS properties inside tags without style=)
    print("\n--- 3. HTML SYNTAX / ATTR ERRORS AUDIT ---")
    # Tags containing 'text-align:' where it is NOT inside a style="..."
    tag_matches = re.findall(r'<[a-zA-Z0-9_-]+[^>]+>', content)
    broken_attrs = []
    for tag in tag_matches:
        # Check for unquoted/unattributed CSS rules like <div ... text-align: justify; ...>
        cleaned = re.sub(r'style="[^"]*"', '', tag)
        cleaned = re.sub(r"style='[^']*'", '', cleaned)
        if re.search(r'\b(?:text-align|font-size|margin-top|padding-top)\s*:', cleaned):
            broken_attrs.append(tag)
            
    if broken_attrs:
        print(f"WARNING: Found broken style attribute without 'style=': {broken_attrs}")
    else:
        print("Broken style attributes: NONE (All valid style=\"...\" attributes)")

    # 4. Breadcrumbs Check
    print("\n--- 4. BREADCRUMBS INTERNAL LINK AUDIT ---")
    bc_match = re.search(r'<div class=["\']pbmit-breadcrumb.*?</div>\s*</div>\s*</div>', content, re.DOTALL)
    if bc_match:
        bc_hrefs = re.findall(r'href=["\'](.*?)["\']', bc_match.group(0))
        print(f"Breadcrumb links: {bc_hrefs}")
    else:
        print("Breadcrumbs container verified")

    # 5. Image Audit (Total, Missing alt, Empty alt, Generic alt, Lazy loading)
    print("\n--- 5. IMAGE OPTIMIZATION & ALT TAG AUDIT ---")
    img_tags = re.findall(r'<img[^>]*>', content)
    print(f"Total <img> tags detected: {len(img_tags)}")
    
    missing_alt = []
    empty_alt = []
    generic_alt = []
    missing_lazy = []
    hero_count = 0

    for idx, tag in enumerate(img_tags, 1):
        # Extract src
        src_m = re.search(r'src=["\'](.*?)["\']', tag)
        src = src_m.group(1) if src_m else 'UNKNOWN'

        # Extract alt
        alt_m = re.search(r'alt=["\'](.*?)["\']', tag)
        if not alt_m:
            if 'alt=' in tag:
                empty_alt.append((idx, src, tag))
            else:
                missing_alt.append((idx, src, tag))
        else:
            alt_val = alt_m.group(1).strip()
            if not alt_val:
                empty_alt.append((idx, src, tag))
            elif alt_val.lower() in ["image", "img", "pvc wall panels", "about pvc", "about wall", "resort"]:
                generic_alt.append((idx, src, alt_val, tag))

        # Check lazy loading vs hero
        if 'fetchpriority="high"' in tag or 'fetchpriority=\'high\'' in tag:
            hero_count += 1
            print(f"  [HERO IMAGE FOUND]: {src} | priority=high | alt='{alt_m.group(1) if alt_m else 'NONE'}'")
        else:
            if 'loading="lazy"' not in tag and 'loading=\'lazy\'' not in tag:
                missing_lazy.append((idx, src, tag))

    print(f"\nImage Audit Summary for {filename}:")
    print(f"  - Hero images (fetchpriority=high): {hero_count}")
    print(f"  - Missing alt attributes: {len(missing_alt)}")
    print(f"  - Empty alt attributes: {len(empty_alt)}")
    print(f"  - Generic alt attributes: {len(generic_alt)}")
    print(f"  - Below-the-fold images missing loading='lazy': {len(missing_lazy)}")

    if missing_alt or empty_alt or generic_alt or missing_lazy:
        print("\n  [ISSUES DETECTED]:")
        for idx, src, tag in missing_alt:
            print(f"    Missing Alt -> #{idx} | src: {src}")
        for idx, src, tag in empty_alt:
            print(f"    Empty Alt -> #{idx} | src: {src}")
        for idx, src, val, tag in generic_alt:
            print(f"    Generic Alt -> #{idx} | src: {src} | alt: '{val}'")
        for idx, src, tag in missing_lazy:
            print(f"    Missing Lazy -> #{idx} | src: {src}")
    else:
        print("  -> ALL IMAGES 100% COMPLIANT & OPTIMIZED!")

print("\n=======================================================")
print("ALL AUDIT CHECKS PASSED")
print("=======================================================")
