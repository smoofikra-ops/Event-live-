with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    """          <button
            key={cat}
            onClick={() => setActiveCategory(cat)}
            className={`px-4 sm:px-6 py-2 rounded-full font-bold transition-all whitespace-nowrap flex-shrink-0 text-sm sm:text-base ${activeCategory === cat ? 'bg-amber-500 text-black' : 'bg-black/5 dark:bg-white/5 text-black/70 dark:text-white/70 hover:bg-black/10 dark:hover:bg-white/10'}`}
          >
            {cat}
          </button>""",
    """          <button
            key={cat}
            onClick={() => setActiveCategory(cat)}
            className={`px-4 sm:px-6 py-2 rounded-full font-bold transition-all whitespace-nowrap flex-shrink-0 text-sm sm:text-base ${activeCategory === cat ? 'bg-amber-500 text-black' : 'bg-black/5 dark:bg-white/5 text-black/70 dark:text-white/70 hover:bg-black/10 dark:hover:bg-white/10'}`}
          >
            {cat === 'portfolio.all' ? t(cat) : cat}
          </button>"""
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
