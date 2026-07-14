import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("const FloatingActionButtons = () => {", "const FloatingActionButtons = () => {\n  const { t } = useLanguage();")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
