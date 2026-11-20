import os
import glob
import re

html_files = sorted(glob.glob("*.html"))
print(f"Found {len(html_files)} HTML files to update.")

# Regex to match the placeholder wrapper and its inner contents
# <div class="img-placeholder-wrapper ratio-xxx">
#   <div class="img-placeholder">
#     ...
#     <code class="img-placeholder-filename">hero-management-consulting.webp</code>
#     ...
#   </div>
# </div>

placeholder_re = re.compile(
    r'<div class="img-placeholder-wrapper\s+([^"]+)">\s*'
    r'<div class="img-placeholder">.*?'
    r'<code class="img-placeholder-filename">([^<]+)</code>.*?'
    r'</div>\s*</div>',
    re.DOTALL
)

def make_alt(stem):
    # Convert "hero-management-consulting" to "Hero Management Consulting"
    words = stem.replace("-", " ").replace("_", " ").split()
    return " ".join(w.capitalize() for w in words)

total_replaced = 0
file_counts = {}

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    matches = placeholder_re.findall(content)
    if not matches:
        continue

    def replace_func(m):
        ratio_class = m.group(1).strip()
        filename = m.group(2).strip()
        
        # Stem
        stem = filename
        for ext in [".webp.jpg", ".jpeg", ".jpg", ".png", ".webp"]:
            if stem.endswith(ext):
                stem = stem[:-len(ext)]
                break

        alt_text = make_alt(stem)
        
        # Eager load for hero images
        loading_attr = 'loading="eager"' if "hero" in stem else 'loading="lazy"'

        return (
            f'<div class="img-placeholder-wrapper {ratio_class}">\n'
            f'  <img src="images/{stem}.jpeg" alt="{alt_text}" {loading_attr}>\n'
            f'</div>'
        )

    new_content, count = placeholder_re.subn(replace_func, content)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    total_replaced += count
    file_counts[html_file] = count
    print(f"Updated {html_file}: {count} placeholders replaced with images.")

print(f"\nCompleted! Total placeholders replaced across all files: {total_replaced}")
