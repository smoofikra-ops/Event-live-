import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_grid = '<div className="grid grid-cols-2 lg:grid-cols-3 gap-2 sm:gap-4 md:gap-6">'
new_grid = '<div className="grid grid-cols-3 gap-2 sm:gap-4 md:gap-6">'
content = content.replace(old_grid, new_grid)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
