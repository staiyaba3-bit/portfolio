import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'<!-- Projects Grid -->\s*<div class="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-12">'
# Find the start
match = re.search(start_marker, content)
if not match:
    print("Could not find projects grid start.")
    exit(1)

start_idx = match.end()

# The grid closes right before `<!-- Contact Section -->` or similar. Let's find the `</section>` of the projects section and work backwards.
end_marker = r'<!-- Contact Section -->'
match_end = re.search(end_marker, content)
if not match_end:
    print("Could not find contact section.")
    exit(1)

# we need to find the `</div>\n        </div>\n    </section>` before contact section
# The content to replace is between `start_idx` and some `</div>`s.
# Let's just use regex to replace the content between `<!-- Projects Grid -->` and the end of the Projects section `</section>` (with care).

# A safer approach is string slicing since we know exact lines roughly.
# Or just build the exact replacement HTML.

html = """
                <!-- Project 1: Bakery Website -->
                <div class="reveal h-full" style="transition-delay: 0.1s;">
                    <div class="project-card glass p-6 rounded-[2rem] group hover:border-primary/40 transition-all duration-500 hover:shadow-2xl hover:shadow-primary/15 hover:-translate-y-2 flex flex-col h-full"
                        style="perspective: 1000px;">
                    <div class="project-card-inner h-full flex flex-col justify-between transition-transform duration-200 ease-out"
                        style="transform-style: preserve-3d;">
                        <!-- Image / Preview -->
                        <div class="project-card-image relative w-full h-44 md:h-52 rounded-2xl overflow-hidden mb-6 bg-white/5 border border-primary/20 group-hover:border-primary/40 transition-all duration-500">
                            <img src="bakery-preview.jpg" alt="Bakery Website"
                                class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                                onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <!-- Fallback background if image is missing -->
                            <div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/10 flex items-center justify-center"
                                style="display: none;">
                                <span class="text-white/30 font-bold text-lg tracking-widest uppercase text-center px-4">Bakery Preview</span>
                            </div>
                        </div>

                        <!-- Project Title & Content -->
                        <div class="project-card-content px-2 flex flex-col flex-grow justify-between">
                            <div class="mb-6">
                                <h3 class="text-xl font-extrabold text-white mb-3 group-hover:text-primary transition-colors duration-300">
                                    Bakery Website
                                </h3>
                                <p class="text-slate-300 text-sm leading-relaxed">
                                    A modern bakery website with product browsing and WhatsApp ordering functionality.
                                </p>
                            </div>

                            <div>
                                <!-- Tags -->
                                <div class="flex flex-wrap gap-2 mb-6">
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">React</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">Tailwind CSS</span>
                                </div>

                                <!-- Buttons -->
                                <div class="flex items-center gap-4">
                                    <a href="https://my-bakery-tau.vercel.app/" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 bg-primary hover:bg-[#164e63] text-dark hover:text-primary border border-primary hover:border-primary py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 shadow-[0_0_15px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:scale-[1.05] active:scale-[0.95]">
                                        Live Demo
                                    </a>
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 glass py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 hover:bg-white/10 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] hover:scale-[1.05] active:scale-[0.95] border border-primary/20 hover:border-primary text-white">
                                        View Code
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>

                <!-- Project 2: Cafe Website -->
                <div class="reveal h-full" style="transition-delay: 0.2s;">
                    <div class="project-card glass p-6 rounded-[2rem] group hover:border-primary/40 transition-all duration-500 hover:shadow-2xl hover:shadow-primary/15 hover:-translate-y-2 flex flex-col h-full"
                        style="perspective: 1000px;">
                    <div class="project-card-inner h-full flex flex-col justify-between transition-transform duration-200 ease-out"
                        style="transform-style: preserve-3d;">
                        <!-- Image / Preview -->
                        <div class="project-card-image relative w-full h-44 md:h-52 rounded-2xl overflow-hidden mb-6 bg-white/5 border border-primary/20 group-hover:border-primary/40 transition-all duration-500">
                            <img src="cafe-preview.jpg" alt="Cafe Website"
                                class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                                onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <!-- Fallback background if image is missing -->
                            <div class="absolute inset-0 bg-gradient-to-br from-secondary/10 to-primary/10 flex items-center justify-center"
                                style="display: none;">
                                <span class="text-white/30 font-bold text-lg tracking-widest uppercase text-center px-4">Cafe Preview</span>
                            </div>
                        </div>

                        <!-- Project Title & Content -->
                        <div class="project-card-content px-2 flex flex-col flex-grow justify-between">
                            <div class="mb-6">
                                <h3 class="text-xl font-extrabold text-white mb-3 group-hover:text-primary transition-colors duration-300">
                                    Cafe Website
                                </h3>
                                <p class="text-slate-300 text-sm leading-relaxed">
                                    A beautifully designed modern responsive cafe website showcasing the cafe and its offerings with WhatsApp contact.
                                </p>
                            </div>

                            <div>
                                <!-- Tags -->
                                <div class="flex flex-wrap gap-2 mb-6">
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">HTML</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">CSS</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">JavaScript</span>
                                </div>

                                <!-- Buttons -->
                                <div class="flex items-center gap-4">
                                    <a href="https://cafe-website-five-kappa.vercel.app/" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 bg-primary hover:bg-[#164e63] text-dark hover:text-primary border border-primary hover:border-primary py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 shadow-[0_0_15px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:scale-[1.05] active:scale-[0.95]">
                                        Live Demo
                                    </a>
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 glass py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 hover:bg-white/10 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] hover:scale-[1.05] active:scale-[0.95] border border-primary/20 hover:border-primary text-white">
                                        View Code
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>

                <!-- Project 3: APEX Fitness Website -->
                <div class="reveal h-full" style="transition-delay: 0.1s;">
                    <div class="project-card glass p-6 rounded-[2rem] group hover:border-primary/40 transition-all duration-500 hover:shadow-2xl hover:shadow-primary/15 hover:-translate-y-2 flex flex-col h-full"
                        style="perspective: 1000px;">
                    <div class="project-card-inner h-full flex flex-col justify-between transition-transform duration-200 ease-out"
                        style="transform-style: preserve-3d;">
                        <!-- Image / Preview -->
                        <div class="project-card-image relative w-full h-44 md:h-52 rounded-2xl overflow-hidden mb-6 bg-white/5 border border-primary/20 group-hover:border-primary/40 transition-all duration-500">
                            <img src="gym-preview.jpg" alt="APEX Fitness Website"
                                class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                                onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <!-- Fallback background if image is missing -->
                            <div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/10 flex items-center justify-center"
                                style="display: none;">
                                <span class="text-white/30 font-bold text-lg tracking-widest uppercase text-center px-4">Gym Preview</span>
                            </div>
                        </div>

                        <!-- Project Title & Content -->
                        <div class="project-card-content px-2 flex flex-col flex-grow justify-between">
                            <div class="mb-6">
                                <h3 class="text-xl font-extrabold text-white mb-3 group-hover:text-primary transition-colors duration-300">
                                    APEX Fitness Website
                                </h3>
                                <p class="text-slate-300 text-sm leading-relaxed">
                                    A modern responsive gym and fitness website featuring a BMI calculator and fitness-focused UI.
                                </p>
                            </div>

                            <div>
                                <!-- Tags -->
                                <div class="flex flex-wrap gap-2 mb-6">
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">HTML</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">CSS</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">JavaScript</span>
                                </div>

                                <!-- Buttons -->
                                <div class="flex items-center gap-4">
                                    <a href="https://apex-fitness-club-beryl.vercel.app/#home" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 bg-primary hover:bg-[#164e63] text-dark hover:text-primary border border-primary hover:border-primary py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 shadow-[0_0_15px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:scale-[1.05] active:scale-[0.95]">
                                        Live Demo
                                    </a>
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 glass py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 hover:bg-white/10 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] hover:scale-[1.05] active:scale-[0.95] border border-primary/20 hover:border-primary text-white">
                                        View Code
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>

                <!-- Project 4: Mini Challenges App -->
                <div class="reveal h-full" style="transition-delay: 0.2s;">
                    <div class="project-card glass p-6 rounded-[2rem] group hover:border-primary/40 transition-all duration-500 hover:shadow-2xl hover:shadow-primary/15 hover:-translate-y-2 flex flex-col h-full"
                        style="perspective: 1000px;">
                    <div class="project-card-inner h-full flex flex-col justify-between transition-transform duration-200 ease-out"
                        style="transform-style: preserve-3d;">
                        <!-- Image / Preview -->
                        <div class="project-card-image relative w-full h-44 md:h-52 rounded-2xl overflow-hidden mb-6 bg-white/5 border border-primary/20 group-hover:border-primary/40 transition-all duration-500">
                            <img src="challenges-preview.jpg" alt="Mini Challenges App"
                                class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                                onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <!-- Fallback background if image is missing -->
                            <div class="absolute inset-0 bg-gradient-to-br from-secondary/10 to-primary/10 flex items-center justify-center"
                                style="display: none;">
                                <span class="text-white/30 font-bold text-lg tracking-widest uppercase text-center px-4">Challenges Preview</span>
                            </div>
                        </div>

                        <!-- Project Title & Content -->
                        <div class="project-card-content px-2 flex flex-col flex-grow justify-between">
                            <div class="mb-6">
                                <h3 class="text-xl font-extrabold text-white mb-3 group-hover:text-primary transition-colors duration-300">
                                    Mini Challenges App
                                </h3>
                                <p class="text-slate-300 text-sm leading-relaxed">
                                    A collection of interactive frontend coding challenges designed around a clean and responsive UI.
                                </p>
                            </div>

                            <div>
                                <!-- Tags -->
                                <div class="flex flex-wrap gap-2 mb-6">
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">React</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">JavaScript</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">CSS</span>
                                </div>

                                <!-- Buttons -->
                                <div class="flex items-center gap-4">
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 bg-primary hover:bg-[#164e63] text-dark hover:text-primary border border-primary hover:border-primary py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 shadow-[0_0_15px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:scale-[1.05] active:scale-[0.95]">
                                        Live Demo
                                    </a>
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 glass py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 hover:bg-white/10 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] hover:scale-[1.05] active:scale-[0.95] border border-primary/20 hover:border-primary text-white">
                                        View Code
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>

                <!-- Project 5: Birthday Website -->
                <div class="reveal h-full" style="transition-delay: 0.1s;">
                    <div class="project-card glass p-6 rounded-[2rem] group hover:border-primary/40 transition-all duration-500 hover:shadow-2xl hover:shadow-primary/15 hover:-translate-y-2 flex flex-col h-full"
                        style="perspective: 1000px;">
                    <div class="project-card-inner h-full flex flex-col justify-between transition-transform duration-200 ease-out"
                        style="transform-style: preserve-3d;">
                        <!-- Image / Preview -->
                        <div class="project-card-image relative w-full h-44 md:h-52 rounded-2xl overflow-hidden mb-6 bg-white/5 border border-primary/20 group-hover:border-primary/40 transition-all duration-500">
                            <img src="birthday-preview.jpg" alt="Birthday Website"
                                class="w-full h-full object-cover opacity-80 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                                onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                            <!-- Fallback background if image is missing -->
                            <div class="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/10 flex items-center justify-center"
                                style="display: none;">
                                <span class="text-white/30 font-bold text-lg tracking-widest uppercase text-center px-4">Birthday Preview</span>
                            </div>
                        </div>

                        <!-- Project Title & Content -->
                        <div class="project-card-content px-2 flex flex-col flex-grow justify-between">
                            <div class="mb-6">
                                <h3 class="text-xl font-extrabold text-white mb-3 group-hover:text-primary transition-colors duration-300">
                                    Birthday Website
                                </h3>
                                <p class="text-slate-300 text-sm leading-relaxed">
                                    A personalized celebration page featuring custom timelines, animations, and interactive elements.
                                </p>
                            </div>

                            <div>
                                <!-- Tags -->
                                <div class="flex flex-wrap gap-2 mb-6">
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">HTML</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">CSS</span>
                                    <span class="px-3 py-1 text-xs font-semibold rounded-full bg-white/5 text-slate-300 border border-primary/20 group-hover:border-primary/20 transition-colors">GSAP</span>
                                </div>

                                <!-- Buttons -->
                                <div class="flex items-center gap-4">
                                    <a href="https://birthday-website-beta-opal.vercel.app/cake-page.html" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 bg-primary hover:bg-[#164e63] text-dark hover:text-primary border border-primary hover:border-primary py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 shadow-[0_0_15px_rgba(34,211,238,0.2)] hover:shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:scale-[1.05] active:scale-[0.95]">
                                        Live Demo
                                    </a>
                                    <a href="#" target="_blank" rel="noopener noreferrer"
                                        class="flex-1 glass py-3 rounded-2xl font-bold text-sm text-center transition-all duration-300 hover:bg-white/10 hover:shadow-[0_0_20px_rgba(255,255,255,0.05)] hover:scale-[1.05] active:scale-[0.95] border border-primary/20 hover:border-primary text-white">
                                        View Code
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>\n"""

new_content = content[:start_idx] + "\n" + html + content[content.find('            </div>\n        </div>\n    </section>\n\n    <!-- Contact Section -->'):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html successfully.")
