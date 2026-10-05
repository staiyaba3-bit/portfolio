import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix html, body overflow in CSS
css_search = r'body\s*{\s*([^}]*)\s*}'
def replace_body(match):
    inner = match.group(1)
    if 'overflow-x: hidden' not in inner:
        inner += '\n    overflow-x: hidden;\n    width: 100%;\n    position: relative;'
    return f'html, body {{\n    overflow-x: hidden;\n    width: 100%;\n    position: relative;\n}}\n\nbody {{\n{inner}\n}}'

if 'html, body {' not in content:
    content = re.sub(css_search, replace_body, content)

# 2. Fix body classes
content = content.replace('<body class="custom-gradient-bg min-h-screen">', '<body class="custom-gradient-bg min-h-screen overflow-x-hidden w-full">')

# 3. Fix Navbar structure to put Mobile Menu Btn and Voice Btn together
nav_pattern = r'(<!-- Mobile Menu Toggle -->\s*<button id="mobile-menu-btn"[^>]*>[\s\S]*?</button>)\s*(<div class="flex items-center gap-4">\s*<button id="voice-btn")'
# Wait, the current order in file is: Mobile Menu Toggle, then div with voice btn.
# Let's just find them and replace.
# Actually I can just replace the whole nav block because it's simpler and safer.

nav_regex = re.compile(r'<nav class="fixed top-0 w-full z-50[^>]*>([\s\S]*?)</nav>')
nav_match = nav_regex.search(content)
if nav_match:
    new_nav = '''
    <nav class="fixed top-0 w-full z-50 px-4 sm:px-6 md:px-12 py-4 sm:py-6 flex items-center justify-between bg-black/10 backdrop-blur-md border-b border-white/5">
        <div class="flex items-center gap-2">
            <div class="w-8 h-8 sm:w-10 sm:h-10 bg-gradient-to-br from-primary to-secondary rounded-lg flex items-center justify-center font-bold text-lg sm:text-xl text-white">T</div>
            <span class="font-poppins font-bold text-lg sm:text-xl tracking-tight hidden sm:block text-white">Taiyaba<span class="text-primary">.</span></span>
        </div>

        <div class="hidden md:flex items-center gap-6 lg:gap-10 glass px-6 lg:px-10 py-2 lg:py-3 rounded-full text-[10px] lg:text-[11px] font-bold uppercase tracking-[0.2em] text-slate-300">
            <a href="#home" class="nav-link active hover:text-primary transition-colors">Home</a>
            <a href="#about" class="nav-link hover:text-primary transition-colors">About</a>
            <a href="#skills" class="nav-link hover:text-primary transition-colors">Skills</a>
            <a href="#projects" class="nav-link hover:text-primary transition-colors">Projects</a>
            <a href="#contact" class="nav-link hover:text-primary transition-colors">Contact</a>
        </div>

        <div class="flex items-center gap-2 sm:gap-4">
            <button id="voice-btn" class="glass px-3 py-1.5 sm:px-4 sm:py-2 flex items-center gap-2 hover:bg-white/10 transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-primary">
                    <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
                    <line x1="12" x2="12" y1="19" y2="22" />
                </svg>
                <div class="text-left leading-tight hidden sm:block">
                    <p class="text-[8px] sm:text-[9px] uppercase tracking-widest text-slate-400 font-bold">Voice</p>
                    <p class="text-[10px] sm:text-[11px] font-bold text-white">Intro</p>
                </div>
            </button>
            <button id="mobile-menu-btn" class="md:hidden glass p-2 rounded-lg text-primary hover:bg-white/10 transition-colors focus:outline-none">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="3" y1="12" x2="21" y2="12"></line>
                    <line x1="3" y1="6" x2="21" y2="6"></line>
                    <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
            </button>
        </div>
    </nav>'''
    content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

# 4. Break word for long emails in about section
content = content.replace('<span class="text-white font-medium text-right">staiyaba3@gmail.com</span>', '<span class="text-white font-medium text-right break-all break-words text-sm sm:text-base">staiyaba3@gmail.com</span>')

# 5. Break word for long emails in contact section
content = content.replace('<a href="mailto:staiyaba3@gmail.com" class="text-slate-300 hover:text-primary transition-colors font-medium text-base">staiyaba3@gmail.com</a>', '<a href="mailto:staiyaba3@gmail.com" class="text-slate-300 hover:text-primary transition-colors font-medium text-sm sm:text-base break-all break-words">staiyaba3@gmail.com</a>')

# 6. Hero background glow size (w-80 might be 320px and overflow if slightly offset)
content = content.replace('w-80 h-80 bg-primary/20', 'w-64 h-64 sm:w-80 sm:h-80 bg-primary/20')

# 7. AI Chat window absolute width (remove calc(100vw) because it is unsafe when inside a right-4 container)
chat_window_pattern = r'class="bg-black/60 backdrop-blur-2xl border border-primary/30 absolute bottom-20 right-0 [^"]*rounded-\[2rem\]'
new_chat_classes = 'class="bg-black/60 backdrop-blur-2xl border border-primary/30 absolute bottom-20 right-0 w-[280px] sm:w-[320px] md:w-96 rounded-[2rem]'
content = re.sub(chat_window_pattern, new_chat_classes, content)

# 8. Force image max-width in project cards to 100% just in case
content = content.replace('class="w-full h-full object-cover object-top opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"', 'class="w-full h-full object-cover object-top opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700 max-w-full"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Ultimate responsive fix applied.")
