import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_div = '<div className="mb-2 sm:mb-4 md:mb-8 p-2 sm:p-4 md:p-6 rounded-[12px] sm:rounded-[22px] glass-icon w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">'
new_div = '<div className="mb-2 sm:mb-4 md:mb-8 p-2 sm:p-4 md:p-6 rounded-[12px] sm:rounded-[22px] bg-gradient-to-br from-white dark:from-[#222] to-gray-50 dark:to-[#111] border-t border-l border-white/80 dark:border-white/10 border-b-2 border-r-2 border-black/5 dark:border-black/40 shadow-lg w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">'

content = content.replace(old_div, new_div)

# While we are at it, let's fix the dark mode/light mode issues in index.css if any?
with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

