import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HERO SECTION
old_hero = r"<p class=\"text-slate-300 text-lg md:text-xl max-w-xl leading-relaxed reveal font-medium\"\s*style=\"transition-delay: 0\.1s;\">\s*Crafting immersive digital experiences through clean code and modern design\. Specializing in building\s*scalable web applications that push the boundaries of the possible\.\s*</p>"
new_hero = """<p class="text-slate-300 text-lg md:text-xl max-w-xl leading-relaxed reveal font-medium"
                style="transition-delay: 0.1s;">
                I build modern, responsive and interactive websites with clean UI and thoughtful frontend development.
            </p>"""
html = re.sub(old_hero, new_hero, html)

# 2. ABOUT SECTION
old_about_ul = r"<ul class=\"space-y-3\">[\s\S]*?</ul>"
new_about_ul = """<ul class="space-y-3">
                            <li class="flex items-start gap-3">
                                <div class="mt-1 w-5 h-5 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                </div>
                                <span class="text-slate-300 font-medium text-base">Check my personal details before downloading resume</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <div class="mt-1 w-5 h-5 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                </div>
                                <span class="text-slate-300 font-medium text-base">Built real-world projects like My Bakery and Mini Challenges</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <div class="mt-1 w-5 h-5 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                </div>
                                <span class="text-slate-300 font-medium text-base">Focus on clean UI and premium user experience</span>
                            </li>
                            <li class="flex items-start gap-3">
                                <div class="mt-1 w-5 h-5 rounded-full bg-primary/20 flex items-center justify-center flex-shrink-0 text-primary">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12" /></svg>
                                </div>
                                <span class="text-slate-300 font-medium text-base">Continuously learning and exploring new technologies</span>
                            </li>
                        </ul>"""
html = re.sub(old_about_ul, new_about_ul, html)

# Fix role in About section if it mentions Frontend + Backend
# Currently it says "Frontend Developer", let's make it exactly "Frontend Software Developer"
html = html.replace(">Frontend Developer</span>", ">Frontend Software Developer</span>")
html = html.replace("Frontend Developer<", "Frontend Software Developer<")
html = html.replace("I'm Taiyaba Fatma, a Web Developer", "I'm Taiyaba Fatma, a Frontend Software Developer")
html = html.replace("Role:</p>\n                                    <p class=\"text-slate-300 font-medium text-base\">Web Developer", "Role:</p>\n                                    <p class=\"text-slate-300 font-medium text-base\">Frontend Software Developer")

# 3. PROJECT DESCRIPTIONS
# 3.1 Bakery
html = html.replace("Bakery Website\n                                </h3>\n                                <p class=\"text-slate-300 text-sm leading-relaxed\">\n                                    A modern bakery website with product browsing and WhatsApp ordering functionality.",
                    "My Bakery\n                                </h3>\n                                <p class=\"text-slate-300 text-sm leading-relaxed\">\n                                    A modern responsive bakery website with interactive product browsing and a seamless WhatsApp ordering system.")
html = html.replace("Bakery Website", "My Bakery") # Any remaining

# 3.2 Cafe
html = html.replace("A beautifully designed modern responsive cafe website showcasing the cafe and its offerings with WhatsApp contact.",
                    "A beautifully designed, responsive cafe website showcasing the menu and ambiance, featuring direct WhatsApp contact.")

# 3.3 APEX Fitness
html = html.replace("A modern responsive gym and fitness website featuring a BMI calculator and fitness-focused UI.",
                    "A responsive gym and fitness website featuring a clean UI, built-in BMI calculator, and easy contact options.")

# 3.4 Mini Challenges
html = html.replace("A collection of interactive frontend coding challenges designed around a clean and responsive UI.",
                    "A web application featuring interactive frontend coding challenges with a clean, responsive, and engaging user interface.")

# Remove Birthday Website block
birthday_regex = r"<!-- Project 5: Birthday Website -->[\s\S]*?</div>\s*</div>\s*</div>\s*</div>"
html = re.sub(birthday_regex, "", html)

# 4. AI ASSISTANT
old_getBotReply = r"const getBotReply = \(userMsg\) => \{[\s\S]*?// Default Unknown\s*return \"[^\"]*\";\s*\};"
new_getBotReply = """const getBotReply = (userMsg) => {
            const lowerMsg = userMsg.toLowerCase();
            
            if (lowerMsg.includes('about') || lowerMsg.includes('who is') || lowerMsg.includes('what does she do')) {
                return "Taiyaba is a BSc graduate and a Frontend Software Developer who builds modern, responsive and interactive websites.";
            }
            if (lowerMsg.includes('skill') || lowerMsg.includes('tech') || lowerMsg.includes('technologies') || lowerMsg.includes('what does she know') || lowerMsg.includes('tools') || lowerMsg.includes('build') || lowerMsg.includes('frontend')) {
                return "Taiyaba's skills include HTML, CSS, JavaScript, React, TypeScript, Tailwind CSS, Next.js, Git, Responsive Web Design, UI/UX Design, and Figma.";
            }
            if (lowerMsg.includes('bakery')) {
                return "My Bakery is a modern responsive site with interactive product browsing and a WhatsApp ordering system.";
            }
            if (lowerMsg.includes('cafe')) {
                return "The Cafe Website is a beautifully designed, responsive site showcasing the menu with direct WhatsApp contact.";
            }
            if (lowerMsg.includes('apex') || lowerMsg.includes('fitness') || lowerMsg.includes('gym')) {
                return "The APEX Fitness Website is a modern responsive gym site featuring a BMI calculator and clean fitness UI.";
            }
            if (lowerMsg.includes('challenge')) {
                return "The Mini Challenges App is a web application featuring interactive frontend coding challenges.";
            }
            if (lowerMsg.includes('project') || lowerMsg.includes('portfolio') || lowerMsg.includes('what has she made')) {
                return "Taiyaba's portfolio includes 4 projects: My Bakery, a Cafe Website, APEX Fitness, and a Mini Challenges App.";
            }
            if (lowerMsg.includes('service') || lowerMsg.includes('what can she do')) {
                return "Taiyaba provides services for responsive business websites, landing pages, portfolio websites, and frontend development.";
            }
            if (lowerMsg.includes('hire') || lowerMsg.includes('freelance') || lowerMsg.includes('contact') || lowerMsg.includes('discuss') || lowerMsg.includes('email') || lowerMsg.includes('whatsapp') || lowerMsg.includes('phone') || lowerMsg.includes('availability')) {
                return "Taiyaba is open to freelance opportunities. You can contact her directly through the Email or WhatsApp options available on this portfolio!";
            }
            
            return "I don't have that information available here. You can contact Taiyaba directly through Email or WhatsApp for more details.";
        };"""
html = re.sub(old_getBotReply, new_getBotReply, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully")
