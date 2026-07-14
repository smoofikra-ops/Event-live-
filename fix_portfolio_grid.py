import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the grid in Portfolio
old_grid_start = '<div className="grid grid-cols-6 gap-2 sm:gap-4 md:gap-6 pb-8 w-full px-2 sm:px-4">'
new_grid_start = '<div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 md:gap-6 pb-8 w-full px-2 sm:px-4">'
content = content.replace(old_grid_start, new_grid_start)

# Remove spanClass usage
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
              className="group cursor-pointer transition-transform duration-300 w-full relative" """
content = content.replace(old_map, new_map)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
