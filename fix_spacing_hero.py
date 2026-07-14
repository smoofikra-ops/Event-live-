import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix spacing in sections: replace py-24 with py-16 md:py-24 and add borders
content = content.replace('className="bg-gray-50 dark:bg-[#050505]"', 'className="bg-gray-50 dark:bg-[#050505] py-12 md:py-16 border-b border-black/5 dark:border-white/5"')
content = content.replace('className="bg-white dark:bg-[#0a0a0a]"', 'className="bg-white dark:bg-[#0a0a0a] py-12 md:py-16 border-b border-black/5 dark:border-white/5"')

content = content.replace('className="bg-gray-50 dark:bg-[#050505] py-16 md:py-24"', 'className="bg-gray-50 dark:bg-[#050505] py-12 md:py-16 border-b border-black/5 dark:border-white/5"')
content = content.replace('className="bg-white dark:bg-[#0a0a0a] py-20 overflow-hidden"', 'className="bg-white dark:bg-[#0a0a0a] py-12 md:py-16 overflow-hidden border-b border-black/5 dark:border-white/5"')
content = content.replace('className="bg-gray-50 dark:bg-[#050505] py-24 overflow-hidden relative"', 'className="bg-gray-50 dark:bg-[#050505] py-12 md:py-16 overflow-hidden relative border-b border-black/5 dark:border-white/5"')
content = content.replace('className="bg-white dark:bg-[#0a0a0a] py-24"', 'className="bg-white dark:bg-[#0a0a0a] py-12 md:py-16 border-b border-black/5 dark:border-white/5"')
content = content.replace('<SectionWrapper id="portfolio">', '<SectionWrapper id="portfolio" className="py-12 md:py-16 border-b border-black/5 dark:border-white/5">')

# Hero Video
content = content.replace('className="w-full h-full object-cover"', 'className="w-full h-full max-md:object-contain object-cover bg-black/10 dark:bg-black"')
content = content.replace('className="relative min-h-[60svh] md:min-h-[100svh] flex items-center pt-16 md:pt-20 overflow-hidden dark"', 'className="relative min-h-[50svh] md:min-h-[100svh] flex items-center pt-16 md:pt-20 overflow-hidden dark border-b border-white/10"')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
