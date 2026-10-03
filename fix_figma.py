import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <!-- Website UI Implementation -->
                <div class="reveal h-full" style="transition-delay: 1.2s;">
                    <div class="glass p-6 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#F59E0B]/40 group-hover:shadow-[0_0_20px_rgba(245,158,11,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#F59E0B] drop-shadow-[0_0_8px_rgba(245,158,11,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(245,158,11,0.8)] transition-all duration-500">
                                    <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
                                    <line x1="3" y1="9" x2="21" y2="9" />
                                    <path d="M9 21V9" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Website UI Implementation</h3>
                    </div>
                </div>"""

replacement = """                <!-- Figma -->
                <div class="reveal h-full" style="transition-delay: 1.2s;">
                    <div class="glass p-6 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#F24E1E]/40 group-hover:shadow-[0_0_20px_rgba(242,78,30,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#F24E1E] drop-shadow-[0_0_8px_rgba(242,78,30,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(242,78,30,0.8)] transition-all duration-500">
                                    <path d="M5 5.5A3.5 3.5 0 0 1 8.5 2H12v7H8.5A3.5 3.5 0 0 1 5 5.5z"/>
                                    <path d="M12 2h3.5a3.5 3.5 0 1 1 0 7H12V2z"/>
                                    <path d="M12 12.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 1 1-7 0z"/>
                                    <path d="M5 19.5A3.5 3.5 0 0 1 8.5 16H12v3.5a3.5 3.5 0 1 1-7 0z"/>
                                    <path d="M5 12.5A3.5 3.5 0 0 1 8.5 9H12v7H8.5A3.5 3.5 0 0 1 5 12.5z"/>
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Figma</h3>
                    </div>
                </div>"""

# Replace keeping line endings intact
# First try exact match, but Windows line endings may interfere
content_crlf = target.replace('\n', '\r\n')
if content_crlf in content:
    content = content.replace(content_crlf, replacement)
elif target in content:
    content = content.replace(target, replacement)
else:
    # Use regex if exact match fails
    # strip whitespace for matching
    regex_target = r"<!-- Website UI Implementation -->[\s\S]*?<h3 class=\"text-white font-extrabold text-lg\">Website UI Implementation</h3>\s*</div>\s*</div>"
    content = re.sub(regex_target, replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced Website UI Implementation with Figma")
