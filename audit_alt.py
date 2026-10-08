import re
import glob

print("=== IMAGE ALT AUDIT RESULTS ===")
for filename in glob.glob("*.php"):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    
    matches = re.findall(r'<img[^>]*>', text)
    issues = []
    for m in matches:
        if 'alt=""' in m or 'alt=' not in m:
            issues.append(("Empty/Missing", m))
        elif 'alt="Wall Panel Image' in m or 'alt="About PVC' in m or 'alt="About Wall' in m or 'alt="image"' in m:
            issues.append(("Generic", m))
            
    if issues:
        print(f"\nFile: {filename} ({len(issues)} issues)")
        for reason, tag in issues:
            print(f"  [{reason}]: {tag}")
