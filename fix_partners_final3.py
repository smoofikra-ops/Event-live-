import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_img = """              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain relative z-10 transition-transform duration-500 group-hover/card:scale-110 drop-shadow-[0_4px_15px_rgba(0,0,0,0.15)] dark:drop-shadow-[0_0_20px_rgba(255,255,255,0.25)]" 
              />"""

new_img = """              <img 
                src={p.logo} 
                alt={p.name} 
                className={`w-full h-full object-contain relative z-10 transition-all duration-500 group-hover/card:scale-110 group-hover/card:-translate-y-2 ${index % 2 === 0 ? 'group-hover/card:rotate-3' : 'group-hover/card:-rotate-3'} drop-shadow-[0_4px_15px_rgba(0,0,0,0.15)] dark:drop-shadow-[0_0_20px_rgba(255,255,255,0.25)]`} 
              />"""

content = content.replace(old_img, new_img)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
