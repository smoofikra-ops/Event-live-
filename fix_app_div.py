import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_div = '<div className="font-sans selection:bg-amber-500/30 selection:text-amber-500 bg-gray-50 dark:bg-[#050505] text-black dark:text-white" lang="ar" dir="rtl">'
new_div = '<div className="font-sans selection:bg-amber-500/30 selection:text-amber-500 bg-gray-50 dark:bg-[#050505] text-black dark:text-white">'

content = content.replace(old_div, new_div)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
