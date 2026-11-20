import glob
import os
import re

html_files = sorted(glob.glob("*.html"))
print(f"Total HTML files found: {len(html_files)}")
assert len(html_files) == 35, "Expected 35 HTML files!"

all_targets = set(html_files)
broken_links = []
missing_images = []
img_count = 0
remaining_placeholders = 0

for f in html_files:
    with open(f, encoding="utf-8") as fp:
        content = fp.read()

    # Check internal links
    links = re.findall(r'href=[\"\']([a-zA-Z0-9\-_]+\.html)[\"\']', content)
    for l in links:
        if l not in all_targets:
            broken_links.append((f, l))

    # Check img tags
    images_found = re.findall(r'<img[^>]+src=[\"\']([^\"\']+)[\"\']', content)
    for img_path in images_found:
        img_count += 1
        local_path = img_path.replace("/", os.sep)
        if not os.path.exists(local_path):
            missing_images.append((f, img_path))

    # Check placeholder badges
    badges = re.findall(r'class="img-placeholder-badge"', content)
    remaining_placeholders += len(badges)

print(f"Total image tags across site: {img_count}")
print(f"Missing images on disk: {len(missing_images)}")
if missing_images:
    for src, img in missing_images:
        print(f"  Missing: {src} -> {img}")
else:
    print("ALL image paths in all HTML files exist on disk!")

print(f"Remaining placeholder badges: {remaining_placeholders}")
print(f"Broken internal HTML links: {len(broken_links)}")
if broken_links:
    for src, tgt in broken_links:
        print(f"  Broken: {src} -> {tgt}")
else:
    print("ALL internal HTML links are 100% valid!")

# Check CSS & JS references
missing_assets = []
for f in html_files:
    with open(f, encoding="utf-8") as fp:
        content = fp.read()
    css_refs = re.findall(r'href=[\"\'](assets/css/[a-zA-Z0-9\-_]+\.css)[\"\']', content)
    for c in css_refs:
        if not os.path.exists(c.replace("/", os.sep)):
            missing_assets.append((f, c))
    js_refs = re.findall(r'src=[\"\'](assets/js/[a-zA-Z0-9\-_]+\.js)[\"\']', content)
    for j in js_refs:
        if not os.path.exists(j.replace("/", os.sep)):
            missing_assets.append((f, j))

print(f"Missing CSS/JS references: {len(missing_assets)}")
if not missing_assets:
    print("ALL CSS and JS references exist on disk!")
