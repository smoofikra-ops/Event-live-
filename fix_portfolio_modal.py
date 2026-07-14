import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_btn = 'className="absolute top-8 rtl:right-8 ltr:left-8 text-white hover:text-amber-500 z-[210]"'
new_btn = 'className="absolute top-8 rtl:left-8 ltr:right-8 text-white hover:text-amber-500 z-[210]"'
content = content.replace(old_btn, new_btn)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
