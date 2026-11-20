import os
import re

images = os.listdir("images")
print(f"Total files in images/: {len(images)}")

with open("IMAGE-GENERATION-GUIDE.md", "r", encoding="utf-8") as f:
    text = f.read()

placeholders = re.findall(r"### Image \d+:\s*`([^`]+)`", text)
print(f"Total guide placeholders: {len(placeholders)}")

image_map = {}
for img in images:
    stem = img
    for ext in [".webp.jpg", ".jpeg", ".jpg", ".png", ".webp"]:
        if stem.endswith(ext):
            stem = stem[:-len(ext)]
            break
    image_map[stem] = img

matched = []
unmatched = []
for p in placeholders:
    stem = p.replace(".webp", "")
    if stem in image_map:
        matched.append((p, image_map[stem]))
    else:
        unmatched.append(p)

print(f"Matched count: {len(matched)}")
print(f"Unmatched count: {len(unmatched)}")
if unmatched:
    print("Unmatched items:", unmatched)
else:
    print("ALL 71 IMAGES MATCHED PERFECTLY!")
