import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('rtl:left-4 ltr:right-4 ltr:right-4 ltr:left-4', 'rtl:left-4 ltr:right-4')
content = content.replace('rtl:-right-2 ltr:right-24 ltr:left-2', 'rtl:-right-2 ltr:-left-2')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
