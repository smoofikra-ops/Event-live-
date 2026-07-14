import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix conflicting ltr properties
content = content.replace('rtl:right-8 ltr:left-8 ltr:right-8', 'rtl:right-8 ltr:left-8')
content = content.replace('ltr:left-2 ltr:right-24', 'ltr:right-24 ltr:left-2') # Wait, let's just see.
content = content.replace('rtl:-right-2 ltr:left-2 ltr:right-24', 'rtl:-right-2 ltr:left-2') # If left-2 and right-24 are both there, we just want left-2 probably?
content = content.replace('rtl:right-2 ltr:left-2 ltr:right-2', 'rtl:right-2 ltr:left-2')
content = content.replace('rtl:right-4 ltr:left-4 ltr:right-4', 'rtl:right-4 ltr:left-4')
content = content.replace('rtl:origin-right ltr:origin-left ltr:origin-right', 'rtl:origin-right ltr:origin-left')
content = content.replace('ltr:left-6 ltr:right-6', 'ltr:left-6')
content = content.replace('ltr:left-4 ltr:right-4', 'ltr:left-4')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
