import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update section class
old_section = '<section id="home" className="relative md:min-h-[100svh] flex flex-col md:flex-row md:items-center pt-20 md:pt-20 overflow-hidden dark border-b border-white/10 bg-[#0a0a0a]">'
new_section = '<section id="home" className="relative min-h-[100svh] flex flex-col md:flex-row md:items-center pt-20 overflow-hidden dark border-b border-white/10 bg-[#0a0a0a]">'
content = content.replace(old_section, new_section)

# 2. Update video container class
old_video_container = '<div className="relative md:absolute md:inset-0 z-0 w-full md:h-full md:overflow-hidden aspect-video md:aspect-auto">'
new_video_container = '<div className="absolute inset-0 z-0 w-full h-full overflow-hidden">'
content = content.replace(old_video_container, new_video_container)

# 3. Update dark overlays
old_overlay1 = '<div className="hidden md:block absolute inset-0 bg-black/20 dark:bg-black/30 pointer-events-none"></div>'
new_overlay1 = '<div className="absolute inset-0 bg-black/40 dark:bg-black/50 pointer-events-none"></div>'
content = content.replace(old_overlay1, new_overlay1)

old_overlay2 = '<div className="hidden md:block absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent pointer-events-none"></div>'
new_overlay2 = '<div className="absolute inset-0 bg-gradient-to-t from-[#0a0a0a] via-black/40 to-transparent pointer-events-none"></div>'
content = content.replace(old_overlay2, new_overlay2)

# Also fix the iframe container
old_iframe_container = '<div className="w-full h-full md:scale-110">'
new_iframe_container = '<div className="w-full h-full scale-110">'
content = content.replace(old_iframe_container, new_iframe_container)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
