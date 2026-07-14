import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('name="name"', 'name="name" dir="auto"')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
