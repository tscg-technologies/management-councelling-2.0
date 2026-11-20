import glob
import re

placeholders = []
for html_path in sorted(glob.glob("*.html")):
    with open(html_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Find all placeholder filenames
    matches = re.findall(r'<code class="img-placeholder-filename">([^<]+)</code>', text)
    for m in matches:
        placeholders.append((html_path, m))

print(f"Total placeholder instances across all pages: {len(placeholders)}")
unique = sorted(list(set(p[1] for p in placeholders)))
print(f"Total unique image assets: {len(unique)}")
print("\nInventory:")
for idx, (page, fname) in enumerate(placeholders, 1):
    print(f"{idx:02d}. [{page}] -> {fname}")
