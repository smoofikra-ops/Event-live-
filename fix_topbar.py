import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    """<div className="flex justify-between items-start w-full mt-24 md:mt-20">""",
    """<div className="flex justify-between items-start w-full mt-[120px] md:mt-[140px]">"""
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
