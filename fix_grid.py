import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_grid_start = """      <div className="grid grid-cols-2 lg:grid-cols-3 gap-2 sm:gap-4 md:gap-6 pb-8 w-full px-2 sm:px-4">
        {filteredWorks.map((w, i) => {
          const hasVideo = !!w.videoUrl;
          return ("""

new_grid_start = """      <div className="flex overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-8 w-full">
        {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, pageIndex) => (
          <div key={pageIndex} className="min-w-full flex-shrink-0 snap-center px-2 sm:px-4">
            <div className="grid grid-cols-2 lg:grid-cols-3 gap-2 sm:gap-4 md:gap-6">
              {filteredWorks.slice(pageIndex * 9, (pageIndex + 1) * 9).map((w, pageI) => {
                const i = pageIndex * 9 + pageI;
                const hasVideo = !!w.videoUrl;
                return ("""

content = content.replace(old_grid_start, new_grid_start)

old_grid_end = """            </div>
          );
        })}
      </div>"""

new_grid_end = """            </div>
          );
        })}
            </div>
          </div>
        ))}
      </div>"""

content = content.replace(old_grid_end, new_grid_end)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
