import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_cats = """  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];"""

new_cats = """  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
  
  const getCategoryTranslation = (cat: string) => {
    if (cat === 'portfolio.all') return t('portfolio.all');
    if (cat === 'المعارض') return t('service.1.title') || 'Exhibitions';
    if (cat === 'حفلات الافتتاح') return t('service.4.title') || 'Opening Ceremonies';
    if (cat === 'الفعاليات الوطنية') return t('service.3.title') || 'National Events';
    if (cat === 'المؤتمرات والمهرجانات') return language === 'ar' ? 'المؤتمرات والمهرجانات' : 'Conferences & Festivals';
    return cat;
  };"""

content = content.replace(old_cats, new_cats)

old_cat_btn = """            <button 
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`px-6 py-2.5 rounded-full text-sm font-bold transition-all duration-300 backdrop-blur-md border ${
                activeCategory === cat 
                  ? 'bg-amber-500 text-black border-amber-400 shadow-[0_0_20px_rgba(255,138,0,0.4)]' 
                  : 'bg-white/5 dark:bg-white/5 text-black/60 dark:text-white/60 border-black/10 dark:border-white/10 hover:bg-white/20 dark:hover:bg-white/10 hover:text-black dark:hover:text-white hover:border-black/20 dark:hover:border-white/20'
              }`}
            >
              {cat === 'portfolio.all' ? t('portfolio.all') : cat}
            </button>"""

new_cat_btn = """            <button 
              key={cat}
              onClick={() => setActiveCategory(cat)}
              className={`px-6 py-2.5 rounded-full text-sm font-bold transition-all duration-300 backdrop-blur-md border ${
                activeCategory === cat 
                  ? 'bg-amber-500 text-black border-amber-400 shadow-[0_0_20px_rgba(255,138,0,0.4)]' 
                  : 'bg-white/5 dark:bg-white/5 text-black/60 dark:text-white/60 border-black/10 dark:border-white/10 hover:bg-white/20 dark:hover:bg-white/10 hover:text-black dark:hover:text-white hover:border-black/20 dark:hover:border-white/20'
              }`}
            >
              {getCategoryTranslation(cat)}
            </button>"""

content = content.replace(old_cat_btn, new_cat_btn)

# Fix selectedWork category display
old_selected = """                  {selectedWork.category && (
                    <span className="inline-block px-3 py-1.5 bg-amber-500 text-black text-xs font-black uppercase tracking-wider rounded-full mb-3 shadow-[0_0_15px_rgba(255,138,0,0.4)]">
                      {selectedWork.category}
                    </span>
                  )}"""

new_selected = """                  {selectedWork.category && (
                    <span className="inline-block px-3 py-1.5 bg-amber-500 text-black text-xs font-black uppercase tracking-wider rounded-full mb-3 shadow-[0_0_15px_rgba(255,138,0,0.4)]">
                      {getCategoryTranslation(selectedWork.category)}
                    </span>
                  )}"""

content = content.replace(old_selected, new_selected)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
