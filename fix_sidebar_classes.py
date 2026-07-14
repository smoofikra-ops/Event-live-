import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix hamburger button
old_hamburger = 'className="fixed top-4 ltr:right-4 rtl:left-4 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 hover:text-black transition-colors"'
new_hamburger = 'className={`fixed top-4 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 hover:text-black transition-colors ${language === "ar" ? "left-4" : "right-4"}`}'
content = content.replace(old_hamburger, new_hamburger)

# Fix sidebar panel
old_panel = 'className="fixed top-0 bottom-0 ltr:right-0 rtl:left-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-l rtl:border-r rtl:border-l-0 border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl"'
new_panel = 'className={`fixed top-0 bottom-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl ${language === "ar" ? "left-0 border-r" : "right-0 border-l"}`}'
content = content.replace(old_panel, new_panel)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
