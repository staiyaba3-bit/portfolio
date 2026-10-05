import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The original navbar has:
# <div class="hidden md:flex items-center gap-10 glass px-10 py-3 rounded-full text-[11px] font-bold uppercase tracking-[0.2em] text-slate-300">
# and:
# <div class="flex items-center gap-4">
#     <button id="voice-btn" ...>

nav_search = r'(<nav[^>]*>[\s\S]*?)(\s*<div class="flex items-center gap-4">)'
nav_replace = r'''\1
        <!-- Mobile Menu Toggle -->
        <button id="mobile-menu-btn" class="md:hidden glass p-2 rounded-lg text-primary hover:bg-white/10 transition-colors focus:outline-none focus:ring-2 focus:ring-primary ml-auto mr-4" aria-label="Toggle Menu">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
            </svg>
        </button>
\2'''

if 'id="mobile-menu-btn"' not in content:
    content = re.sub(nav_search, nav_replace, content)

mobile_menu_html = '''
    <!-- Mobile Menu (Hidden by default) -->
    <div id="mobile-menu" class="fixed inset-0 z-40 bg-black/90 backdrop-blur-xl flex flex-col items-center justify-center gap-8 text-xl font-bold uppercase tracking-[0.2em] text-slate-300 opacity-0 pointer-events-none transition-all duration-300">
        <button id="close-mobile-menu" class="absolute top-6 right-6 p-2 text-primary hover:text-white transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
        </button>
        <a href="#home" class="mobile-nav-link hover:text-primary transition-colors">Home</a>
        <a href="#about" class="mobile-nav-link hover:text-primary transition-colors">About</a>
        <a href="#skills" class="mobile-nav-link hover:text-primary transition-colors">Skills</a>
        <a href="#projects" class="mobile-nav-link hover:text-primary transition-colors">Projects</a>
        <a href="#contact" class="mobile-nav-link hover:text-primary transition-colors">Contact</a>
    </div>
'''

if 'id="mobile-menu"' not in content:
    content = content.replace('<!-- Hero Section -->', mobile_menu_html + '\n    <!-- Hero Section -->')

js_code = '''
        // Mobile Menu Logic
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const closeMobileMenuBtn = document.getElementById('close-mobile-menu');
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

        const toggleMobileMenu = () => {
            const isHidden = mobileMenu.classList.contains('opacity-0');
            if (isHidden) {
                mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
                mobileMenu.classList.add('opacity-100');
                document.body.style.overflow = 'hidden';
            } else {
                mobileMenu.classList.add('opacity-0', 'pointer-events-none');
                mobileMenu.classList.remove('opacity-100');
                document.body.style.overflow = '';
            }
        };

        if (mobileMenuBtn && closeMobileMenuBtn && mobileMenu) {
            mobileMenuBtn.addEventListener('click', toggleMobileMenu);
            closeMobileMenuBtn.addEventListener('click', toggleMobileMenu);
            mobileNavLinks.forEach(link => {
                link.addEventListener('click', () => {
                    toggleMobileMenu();
                });
            });
        }
'''

if 'const mobileMenuBtn =' not in content:
    content = content.replace('// AI Chat Logic', js_code + '\n        // AI Chat Logic')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Mobile menu added.")
