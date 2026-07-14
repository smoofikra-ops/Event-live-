import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Remove spanClass usage from Portfolio
old_map = """        {filteredWorks.map((w, i) => {
          const hasVideo = !!w.videoUrl;
          const spanClass = getGridSpanClass(i, filteredWorks.length);
          return (
            <div
              key={w.id}
              className={`group cursor-pointer transition-transform duration-300 w-full ${spanClass}`}"""
new_map = """        {filteredWorks.map((w, i) => {
          const hasVideo = !!w.videoUrl;
          return (
            <div
              key={w.id}
              className="group cursor-pointer transition-transform duration-300 w-full" """

content = content.replace(old_map, new_map)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
