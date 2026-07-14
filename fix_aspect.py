import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update PortfolioMediaContent img to remove aspect-video
old_img = """        <img 
          src={w.img} 
          className={`w-full h-full object-cover aspect-video transition-all duration-700 group-hover:scale-105 relative z-10 ${isLoaded ? 'opacity-100' : 'opacity-0'}`} 
          alt={w.title}"""

new_img = """        <img 
          src={w.img} 
          className={`w-full h-full object-cover transition-all duration-700 group-hover:scale-105 relative z-10 ${isLoaded ? 'opacity-100' : 'opacity-0'}`} 
          alt={w.title}"""

content = content.replace(old_img, new_img)

# 2. Update the grid item aspect ratio to aspect-square
old_item = """            >
              <div className="relative aspect-video rounded-xl sm:rounded-2xl overflow-hidden bg-black/5 dark:bg-[#111] shadow-lg border border-black/5 dark:border-white/5">
                <PortfolioMediaContent"""

new_item = """            >
              <div className="relative aspect-square rounded-xl sm:rounded-2xl overflow-hidden bg-black/5 dark:bg-[#111] shadow-lg border border-black/5 dark:border-white/5">
                <PortfolioMediaContent"""

content = content.replace(old_item, new_item)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
