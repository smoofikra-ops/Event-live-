import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('ltr:rtl:left-8', 'ltr:left-8')
content = content.replace('-rtl:right-2', 'rtl:-right-2')
content = content.replace('ltr:rtl:left-2', 'ltr:left-2')
content = content.replace('ltr:rtl:left-4', 'ltr:left-4')
content = content.replace('ltr:rtl:right-4', 'ltr:right-4')
content = content.replace('rtl:rtl:left-4', 'rtl:left-4')
content = content.replace('ltr:rtl:origin-left', 'ltr:origin-left')

# In ChevronDown: "rtl:rtl:left-4 ltr:right-4 ltr:rtl:right-4 ltr:rtl:left-4 ltr:right-4"
# Let's just fix it globally:
content = content.replace('rtl:rtl:', 'rtl:')
content = content.replace('ltr:rtl:', 'ltr:')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
