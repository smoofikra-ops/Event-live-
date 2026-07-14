import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix social links clickable
old_social_link = 'className={`w-10 h-10 rounded-full flex items-center justify-center transition-opacity border border-transparent ${colorClass}`}'
new_social_link = 'className={`relative z-10 pointer-events-auto w-10 h-10 rounded-full flex items-center justify-center transition-opacity border border-transparent ${colorClass}`}'
content = content.replace(old_social_link, new_social_link)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
