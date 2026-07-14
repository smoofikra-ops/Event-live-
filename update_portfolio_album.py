import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace category definition
old_cats = """  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
  const albums = categories.filter(c => c !== 'portfolio.all').map(cat => ({
    name: cat,
    works: works.filter(w => w.category === cat)
  })).filter(album => album.works.length > 0);

  const filteredWorks = works.filter(w => {
    if (activeCategory === 'portfolio.all') return true;
    return w.category === activeCategory;
  });
    
  const selectedWork = selectedIndex !== null ? filteredWorks[selectedIndex] : null;"""

new_cats = """  const filteredWorks = works;
  const selectedWork = selectedIndex !== null ? filteredWorks[selectedIndex] : null;"""

content = content.replace(old_cats, new_cats)

# Replace the Grid
old_grid_start = """      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 md:gap-8 w-full">"""
old_grid_end = """      <AnimatePresence>"""

pattern_grid = re.compile(re.escape(old_grid_start) + r".*?(?=      <AnimatePresence>)", re.DOTALL)

new_grid = """      <div className="flex justify-center items-center w-full min-h-[400px] md:min-h-[500px] py-10 overflow-hidden">
        <div 
          className="relative group cursor-pointer w-full max-w-[280px] sm:max-w-sm md:max-w-md aspect-[4/5] mx-auto"
          style={{ perspective: '1000px' }}
          onClick={() => {
            setSelectedIndex(0);
          }}
        >
          {/* Stack effect images (shadows/depth) */}
          <div className="absolute inset-0 bg-white dark:bg-[#222] rounded-2xl transform rotate-[8deg] translate-x-8 md:translate-x-12 translate-y-4 scale-90 shadow-2xl transition-all duration-700 group-hover:rotate-[15deg] group-hover:translate-x-16 group-hover:translate-y-6 overflow-hidden border border-black/10 dark:border-white/10 opacity-60">
             {works[2] && <img src={works[2].img} className="w-full h-full object-cover blur-[2px] grayscale-[30%]" alt="bg" />}
             <div className="absolute inset-0 bg-black/30"></div>
          </div>
          
          <div className="absolute inset-0 bg-gray-100 dark:bg-[#1a1a1a] rounded-2xl transform -rotate-[6deg] -translate-x-6 md:-translate-x-10 translate-y-2 scale-95 shadow-2xl transition-all duration-700 group-hover:-rotate-[12deg] group-hover:-translate-x-14 group-hover:translate-y-4 overflow-hidden border border-black/10 dark:border-white/10 opacity-80">
             {works[1] && <img src={works[1].img} className="w-full h-full object-cover blur-[1px] grayscale-[20%]" alt="bg" />}
             <div className="absolute inset-0 bg-black/20"></div>
          </div>

          {/* Main Cover */}
          <div className="absolute inset-0 bg-white dark:bg-[#111] rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] transition-all duration-700 group-hover:-translate-y-4 group-hover:scale-[1.02] overflow-hidden border border-black/5 dark:border-white/10 z-10 flex flex-col">
            {works[0] && (
              <img 
                src={works[0].img} 
                alt="Main Album"
                className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-110"
              />
            )}
            <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent flex flex-col justify-end p-6 md:p-8">
              <div className="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500 flex flex-col items-center text-center">
                <div className="flex justify-center mb-4">
                  <span className="inline-flex items-center justify-center w-12 h-12 md:w-16 md:h-16 rounded-full bg-amber-500 text-black shadow-[0_0_20px_rgba(255,138,0,0.5)] animate-pulse">
                    <Camera className="w-6 h-6 md:w-8 md:h-8" />
                  </span>
                </div>
                <h3 className="text-2xl sm:text-3xl md:text-4xl font-black text-white mb-2 drop-shadow-md">{language === 'ar' ? 'ألبوم الأعمال' : 'Our Portfolio'}</h3>
                <p className="text-white/80 text-sm md:text-base font-bold mb-4">{works.length} {language === 'ar' ? 'صورة ومقطع مرئي' : 'Photos & Videos'}</p>
                <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/20 backdrop-blur-md border border-white/30 text-white text-xs font-bold opacity-0 group-hover:opacity-100 transition-opacity delay-100 uppercase tracking-wider">
                   {language === 'ar' ? 'انقر لاستعراض الألبوم' : 'Click to Browse Album'}
                   <ArrowLeft className="w-4 h-4 rtl:rotate-0 ltr:rotate-180" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

"""

if pattern_grid.search(content):
    content = pattern_grid.sub(new_grid, content)
else:
    print("WARNING: Grid pattern not found!")

# Replace Infinite Loop controls & Category Tags inside Modal
old_prev = """            {/* Prev Button */}
            {selectedIndex !== null && selectedIndex > 0 && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex - 1); }}
                className="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-0 rtl:rotate-180" />
              </button>
            )}"""

new_prev = """            {/* Prev Button */}
            {selectedIndex !== null && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex > 0 ? selectedIndex - 1 : filteredWorks.length - 1); }}
                className="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-0 rtl:rotate-180" />
              </button>
            )}"""
content = content.replace(old_prev, new_prev)


old_next = """            {/* Next Button */}
            {selectedIndex !== null && selectedIndex < filteredWorks.length - 1 && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex + 1); }}
                className="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-180 rtl:rotate-0" />
              </button>
            )}"""

new_next = """            {/* Next Button */}
            {selectedIndex !== null && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex < filteredWorks.length - 1 ? selectedIndex + 1 : 0); }}
                className="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-180 rtl:rotate-0" />
              </button>
            )}"""
content = content.replace(old_next, new_next)

old_drag = """              onDragEnd={(e, { offset, velocity }) => {
                const swipe = offset.x;
                const isRtl = language === 'ar';
                if (swipe < -50 && selectedIndex !== null) {
                  if (isRtl && selectedIndex > 0) setSelectedIndex(selectedIndex - 1);
                  else if (!isRtl && selectedIndex < filteredWorks.length - 1) setSelectedIndex(selectedIndex + 1);
                } else if (swipe > 50 && selectedIndex !== null) {
                  if (isRtl && selectedIndex < filteredWorks.length - 1) setSelectedIndex(selectedIndex + 1);
                  else if (!isRtl && selectedIndex > 0) setSelectedIndex(selectedIndex - 1);
                }
              }}"""

new_drag = """              onDragEnd={(e, { offset, velocity }) => {
                const swipe = offset.x;
                const isRtl = language === 'ar';
                if (swipe < -50 && selectedIndex !== null) {
                  if (isRtl) setSelectedIndex(selectedIndex > 0 ? selectedIndex - 1 : filteredWorks.length - 1);
                  else setSelectedIndex(selectedIndex < filteredWorks.length - 1 ? selectedIndex + 1 : 0);
                } else if (swipe > 50 && selectedIndex !== null) {
                  if (isRtl) setSelectedIndex(selectedIndex < filteredWorks.length - 1 ? selectedIndex + 1 : 0);
                  else setSelectedIndex(selectedIndex > 0 ? selectedIndex - 1 : filteredWorks.length - 1);
                }
              }}"""
content = content.replace(old_drag, new_drag)


old_text = """              <div className="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black to-transparent pointer-events-none">
                <h3 className="text-2xl font-bold text-white">{selectedWork.title}</h3>
              </div>"""

new_text = """              <div className="absolute bottom-0 left-0 right-0 p-6 md:p-10 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none">
                <div className="transform translate-y-0">
                  {selectedWork.category && (
                    <span className="inline-block px-3 py-1.5 bg-amber-500 text-black text-xs font-black uppercase tracking-wider rounded-full mb-3 shadow-[0_0_15px_rgba(255,138,0,0.4)]">
                      {selectedWork.category}
                    </span>
                  )}
                  <h3 className="text-2xl md:text-3xl font-bold text-white drop-shadow-md">{selectedWork.title}</h3>
                  <div className="text-white/60 text-sm mt-2 font-medium">
                    {selectedIndex + 1} / {filteredWorks.length}
                  </div>
                </div>
              </div>"""
content = content.replace(old_text, new_text)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
