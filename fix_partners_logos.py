import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_div = """            <div 
              key={index} 
              className="group/card mx-2 sm:mx-6 w-28 sm:w-56 h-16 sm:h-28 bg-transparent flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >
              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain transition-all duration-500 grayscale opacity-70 group-hover/card:grayscale-0 group-hover/card:opacity-100 drop-shadow-sm group-hover/card:drop-shadow-md" 
              />
            </div>"""

new_div = """            <div 
              key={index} 
              className="group/card relative mx-4 sm:mx-8 w-40 sm:w-72 h-24 sm:h-40 flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >
              <div className="absolute inset-0 opacity-0 dark:opacity-100 pointer-events-none transition-all duration-500 group-hover/card:opacity-100 group-hover/card:scale-110">
                <div className="absolute top-1/4 -left-2 w-16 h-16 bg-amber-500/20 blur-2xl rounded-full"></div>
                <div className="absolute bottom-1/4 -right-2 w-16 h-16 bg-blue-500/20 blur-2xl rounded-full"></div>
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-24 h-24 bg-white/10 blur-3xl rounded-full"></div>
              </div>
              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain relative z-10 transition-transform duration-500 group-hover/card:scale-110 drop-shadow-[0_4px_10px_rgba(0,0,0,0.1)] dark:drop-shadow-[0_0_15px_rgba(255,255,255,0.4)]" 
              />
            </div>"""

content = content.replace(old_div, new_div)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
