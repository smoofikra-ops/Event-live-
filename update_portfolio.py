import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add albums derivation after categories
old_categories = """  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
  const filteredWorks = works.filter(w => {"""

new_categories = """  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
  const albums = categories.filter(c => c !== 'portfolio.all').map(cat => ({
    name: cat,
    works: works.filter(w => w.category === cat)
  })).filter(album => album.works.length > 0);

  const filteredWorks = works.filter(w => {"""
content = content.replace(old_categories, new_categories)

# Replace everything from tabs to the end of the slider
old_ui_start = """      <div className="flex overflow-x-auto hide-scrollbar gap-2 sm:gap-4 mb-8 sm:mb-12 pb-2 w-full">"""
old_ui_end = """      <AnimatePresence>
        {selectedWork && ("""

# We need to extract the exact text between these two, so we'll use regex.
pattern = re.compile(re.escape(old_ui_start) + r".*?(?=      <AnimatePresence>\s*\{selectedWork && \()", re.DOTALL)

new_ui = """      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8 w-full">
        {albums.map((album, idx) => {
          const coverWork = album.works[0];
          return (
            <div 
              key={album.name} 
              className="relative group cursor-pointer"
              onClick={() => {
                setActiveCategory(album.name);
                setSelectedIndex(0);
              }}
            >
              <div className="absolute inset-0 bg-amber-500/10 dark:bg-amber-500/5 rounded-2xl transform -rotate-3 scale-95 group-hover:-rotate-6 transition-transform duration-500 origin-bottom"></div>
              <div className="absolute inset-0 bg-black/5 dark:bg-white/5 rounded-2xl transform rotate-3 scale-95 group-hover:rotate-6 transition-transform duration-500 origin-bottom"></div>
              
              <div className="relative aspect-[4/5] rounded-2xl overflow-hidden bg-black/5 dark:bg-[#111] shadow-xl border border-black/10 dark:border-white/10 z-10">
                <img 
                  src={coverWork.img} 
                  alt={album.name}
                  className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent flex flex-col justify-end p-6 md:p-8">
                  <div className="transform translate-y-2 group-hover:translate-y-0 transition-transform duration-500">
                    <div className="flex items-center gap-2 mb-2">
                      <span className="inline-flex items-center justify-center w-8 h-8 rounded-full bg-amber-500 text-black shadow-md">
                        <Camera className="w-4 h-4" />
                      </span>
                    </div>
                    <h3 className="text-xl sm:text-2xl font-bold text-white mb-1">{album.name}</h3>
                    <p className="text-white/70 text-sm font-medium">{album.works.length} {language === 'ar' ? 'صور / فيديو' : 'Photos / Videos'}</p>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

"""

if pattern.search(content):
    content = pattern.sub(new_ui, content)
else:
    print("Pattern not found!")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
