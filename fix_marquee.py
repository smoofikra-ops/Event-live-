import re

with open("src/index.css", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("animation: marquee 20s linear infinite;", "animation: marquee 60s linear infinite;")

with open("src/index.css", "w", encoding="utf-8") as f:
    f.write(content)
