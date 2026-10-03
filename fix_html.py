import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the key highlights text
content = content.replace('Built real-world projects like Dad Bakery and Mini Challenges', 'Check my personal details before download resume')

# 2. Update the GSAP configuration
old_gsap_pattern = r"gsap\.utils\.toArray\('\.reveal'\)\.forEach\(\(elem\) => \{\s*let delayVal[^\}]+\}\s*\);\s*\}\s*\);\s*\}\s*\);"
# Since it's easier to just use regex:
old_gsap_regex = r"gsap\.utils\.toArray\('\.reveal'\)\.forEach\(\(elem\) => \{[\s\S]*?ease: \"power2\.out\"\s*\}\);\s*\}\);"

# Actually I can just replace the whole block by exact substring if I ignore whitespace, but replacing it via Python regex is easier.
new_gsap = """gsap.utils.toArray('.reveal').forEach((elem) => {
            gsap.to(elem, {
                scrollTrigger: {
                    trigger: elem,
                    start: "top 95%",
                    once: true
                },
                opacity: 1,
                y: 0,
                duration: 0.3,
                ease: "power2.out"
            });
        });"""
content = re.sub(r"gsap\.utils\.toArray\('\.reveal'\)\.forEach\(\(elem\) => \{[\s\S]*?ease:\s*\"power2\.out\"\s*\}\);\s*\}\);", new_gsap, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
