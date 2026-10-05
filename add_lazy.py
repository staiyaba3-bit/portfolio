import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add loading="lazy" to project images
text = re.sub(r'(<img src="[^"]+-preview\.jpg" alt="[^"]+")', r'\1 loading="lazy"', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added lazy loading to images")
