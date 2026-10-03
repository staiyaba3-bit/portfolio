import re

html = """
                <!-- HTML -->
                <div class="reveal h-full" style="transition-delay: 0.1s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#E34F26]/40 group-hover:shadow-[0_0_20px_rgba(227,79,38,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#E34F26] drop-shadow-[0_0_8px_rgba(227,79,38,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(227,79,38,0.8)] transition-all duration-500">
                                    <polyline points="16 18 22 12 16 6" />
                                    <polyline points="8 6 2 12 8 18" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">HTML</h3>
                    </div>
                </div>

                <!-- CSS -->
                <div class="reveal h-full" style="transition-delay: 0.2s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#1572B6]/40 group-hover:shadow-[0_0_20px_rgba(21,114,182,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#1572B6] drop-shadow-[0_0_8px_rgba(21,114,182,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(21,114,182,0.8)] transition-all duration-500">
                                    <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
                                    <line x1="3" y1="9" x2="21" y2="9" />
                                    <line x1="9" y1="21" x2="9" y2="9" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">CSS</h3>
                    </div>
                </div>

                <!-- JavaScript -->
                <div class="reveal h-full" style="transition-delay: 0.3s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#F7DF1E]/40 group-hover:shadow-[0_0_20px_rgba(247,223,30,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#F7DF1E] drop-shadow-[0_0_8px_rgba(247,223,30,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(247,223,30,0.8)] transition-all duration-500">
                                    <polyline points="4 17 10 11 4 5" />
                                    <line x1="12" y1="19" x2="20" y2="19" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">JavaScript</h3>
                    </div>
                </div>

                <!-- React -->
                <div class="reveal h-full" style="transition-delay: 0.4s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#61DAFB]/40 group-hover:shadow-[0_0_20px_rgba(97,218,251,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-spin-very-slow text-[#61DAFB] drop-shadow-[0_0_8px_rgba(97,218,251,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(97,218,251,0.8)] transition-all duration-500">
                                    <circle cx="12" cy="12" r="2" />
                                    <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(30 12 12)" />
                                    <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(90 12 12)" />
                                    <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(150 12 12)" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">React</h3>
                    </div>
                </div>

                <!-- TypeScript -->
                <div class="reveal h-full" style="transition-delay: 0.5s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#3178C6]/40 group-hover:shadow-[0_0_20px_rgba(49,120,198,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#3178C6] drop-shadow-[0_0_8px_rgba(49,120,198,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(49,120,198,0.8)] transition-all duration-500">
                                    <path d="M4 4v16h16V4H4zm10.73 12.18c-.85.83-2.09 1.25-3.35 1.25-1.57 0-2.88-.63-3.6-1.78l1.3-1c.43.68 1.09 1.15 2.15 1.15 1.01 0 1.63-.48 1.63-1.15 0-1.8-4.63-.78-4.63-3.9 0-1.28.98-2.3 2.85-2.3 1.3 0 2.25.43 2.95 1.25l-1.18 1.18c-.43-.53-.98-.83-1.7-.83-.85 0-1.35.45-1.35 1.05 0 1.68 4.65.68 4.65 3.93.02.43-.02.83-.22 1.15zM17.5 7h-5.25v1.75h1.75v7.25h1.75V8.75h1.75V7z" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">TypeScript</h3>
                    </div>
                </div>

                <!-- Tailwind CSS -->
                <div class="reveal h-full" style="transition-delay: 0.6s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#38B2AC]/40 group-hover:shadow-[0_0_20px_rgba(56,178,172,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#38B2AC] drop-shadow-[0_0_8px_rgba(56,178,172,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(56,178,172,0.8)] transition-all duration-500">
                                    <path d="M12.03 4.5c-2.85 0-5.1 1.7-6 5.1 1.65-2.55 3.45-3.4 5.4-2.55 1.14.51 1.95 1.34 2.87 2.29C15.82 10.93 17.57 12.75 21 12.75c2.85 0 5.1-1.7 6-5.1-1.65 2.55-3.45 3.4-5.4 2.55-1.14-.51-1.95-1.34-2.87-2.29-1.52-1.59-3.27-3.41-6.7-3.41zm-6 8.25c-2.85 0-5.1 1.7-6 5.1 1.65-2.55 3.45-3.4 5.4-2.55 1.14.51 1.95 1.34 2.87 2.29 1.52 1.59 3.27 3.41 6.7 3.41 2.85 0 5.1-1.7 6-5.1-1.65 2.55-3.45 3.4-5.4 2.55-1.14-.51-1.95-1.34-2.87-2.29-1.52-1.59-3.27-3.41-6.7-3.41z" transform="translate(-3 -2) scale(0.9)"/>
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Tailwind CSS</h3>
                    </div>
                </div>

                <!-- Next.js -->
                <div class="reveal h-full" style="transition-delay: 0.7s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-white/40 group-hover:shadow-[0_0_20px_rgba(255,255,255,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-white drop-shadow-[0_0_8px_rgba(255,255,255,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(255,255,255,0.8)] transition-all duration-500">
                                    <circle cx="12" cy="12" r="10" />
                                    <path d="M15 9l-6 6V9H7v6h2l6-6v6h2V9h-2z" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Next.js</h3>
                    </div>
                </div>

                <!-- Git -->
                <div class="reveal h-full" style="transition-delay: 0.8s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#F05032]/40 group-hover:shadow-[0_0_20px_rgba(240,80,50,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#F05032] drop-shadow-[0_0_8px_rgba(240,80,50,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(240,80,50,0.8)] transition-all duration-500">
                                    <circle cx="6" cy="18" r="3" />
                                    <circle cx="6" cy="6" r="3" />
                                    <circle cx="18" cy="18" r="3" />
                                    <path d="M6 9v6" />
                                    <path d="M15.88 15.88L9 9" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Git</h3>
                    </div>
                </div>

                <!-- Responsive Web Design -->
                <div class="reveal h-full" style="transition-delay: 0.9s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#8B5CF6]/40 group-hover:shadow-[0_0_20px_rgba(139,92,246,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#8B5CF6] drop-shadow-[0_0_8px_rgba(139,92,246,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(139,92,246,0.8)] transition-all duration-500">
                                    <rect width="16" height="12" x="4" y="4" rx="2" />
                                    <rect width="6" height="10" x="14" y="10" rx="1" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Responsive Web Design</h3>
                    </div>
                </div>

                <!-- UI/UX Design -->
                <div class="reveal h-full" style="transition-delay: 1.0s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#EC4899]/40 group-hover:shadow-[0_0_20px_rgba(236,72,153,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#EC4899] drop-shadow-[0_0_8px_rgba(236,72,153,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(236,72,153,0.8)] transition-all duration-500">
                                    <path d="M12 20h9" />
                                    <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">UI/UX Design</h3>
                    </div>
                </div>

                <!-- Frontend Development -->
                <div class="reveal h-full" style="transition-delay: 1.1s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
                        <div
                            class="w-14 h-14 rounded-2xl bg-white/5 border border-primary/20 flex items-center justify-center mb-4 group-hover:border-[#10B981]/40 group-hover:shadow-[0_0_20px_rgba(16,185,129,0.15)] transition-all duration-500">
                            <div class="transition-all duration-500 group-hover:scale-110 group-hover:brightness-125">
                                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="animate-float-icon text-[#10B981] drop-shadow-[0_0_8px_rgba(16,185,129,0.4)] group-hover:drop-shadow-[0_0_20px_rgba(16,185,129,0.8)] transition-all duration-500">
                                    <polyline points="16 18 22 12 16 6" />
                                    <polyline points="8 6 2 12 8 18" />
                                </svg>
                            </div>
                        </div>
                        <h3 class="text-white font-extrabold text-lg">Frontend Development</h3>
                    </div>
                </div>

                <!-- Website UI Implementation -->
                <div class="reveal h-full" style="transition-delay: 1.2s;">
                    <div class="glass p-8 md:p-10 rounded-[2rem] flex flex-col items-center justify-center text-center group hover:bg-primary/5 hover:border-primary/30 transition-all duration-500 hover:shadow-xl hover:shadow-primary/10 hover:scale-[1.02] h-full">
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
                </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'<!-- Skills Grid -->\s*<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">'
match = re.search(start_marker, content)
if not match:
    print("Could not find skills grid start.")
    exit(1)

start_idx = match.end()

end_marker = r'<!-- Projects Section -->'
match_end = re.search(end_marker, content)
if not match_end:
    print("Could not find projects section.")
    exit(1)

end_of_skills_section = content.rfind('</div>\n        </div>\n    </section>', start_idx, match_end.start())

new_content = content[:start_idx] + "\n" + html + "\n            " + content[end_of_skills_section:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html successfully.")
