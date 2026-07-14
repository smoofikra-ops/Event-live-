import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_partners_div = """            <div 
              key={index} 
              className="group/card mx-4 sm:mx-6 w-40 sm:w-56 h-20 sm:h-28 bg-white rounded-xl sm:rounded-2xl shadow-[0_4px_15px_rgba(0,0,0,0.05)] border border-black/5 flex items-center justify-center p-2 sm:p-4 transition-all duration-500 hover:scale-110 sm:hover:scale-115 hover:shadow-[0_12px_30px_rgba(255,138,0,0.25)] hover:border-amber-500/30 cursor-pointer select-none"
            >
              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain transition-transform duration-500 group-hover/card:scale-110 filter-none" 
              />
            </div>"""

new_partners_div = """            <div 
              key={index} 
              className="group/card mx-2 sm:mx-6 w-28 sm:w-56 h-16 sm:h-28 bg-transparent flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >
              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain transition-all duration-500 grayscale opacity-70 group-hover/card:grayscale-0 group-hover/card:opacity-100 drop-shadow-sm group-hover/card:drop-shadow-md" 
              />
            </div>"""

content = content.replace(old_partners_div, new_partners_div)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
