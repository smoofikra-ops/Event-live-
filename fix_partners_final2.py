import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_div = """            <div 
              key={index} 
              className="group/card relative mx-3 sm:mx-8 w-28 sm:w-72 h-20 sm:h-40 flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >"""

new_div = """            <div 
              key={index} 
              className="group/card relative mx-2 sm:mx-8 w-24 sm:w-72 h-16 sm:h-40 flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >"""

content = content.replace(old_div, new_div)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
