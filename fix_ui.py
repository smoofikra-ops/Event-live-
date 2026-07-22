import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remove the solid black overlay (dimming) from Services cards, replace with a subtle bottom gradient for text readability
dimming_old = '<div className="absolute inset-0 bg-black/60 group-hover:bg-black/40 transition-colors duration-500 z-0"></div>'
dimming_new = '<div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition-opacity duration-500 z-0"></div>'

code = code.replace(dimming_old, dimming_new)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Applied UI fixes.")
