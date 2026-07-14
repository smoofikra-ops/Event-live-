import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('<input type="text" value={service.title}', '<input dir="auto" type="text" value={service.title}')
content = content.replace('<input type="text" value={work.title}', '<input dir="auto" type="text" value={work.title}')
content = content.replace('<input type="text" value={work.category || \'\'}', '<input dir="auto" type="text" value={work.category || \'\'}')
content = content.replace('<input type="text" value={partner.name}', '<input dir="auto" type="text" value={partner.name}')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
