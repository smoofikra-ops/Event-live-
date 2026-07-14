import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the whole Portfolio slider part to make it 3x3 grid
old_slider = """      <div className="relative w-full">
        <div className="flex overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-8 w-full" id="portfolio-slider" onScroll={(e) => {
          const target = e.target as HTMLElement;
          const scrollLeft = target.scrollLeft;
          const width = target.offsetWidth;
          const page = Math.round(Math.abs(scrollLeft) / width);
          const dots = document.querySelectorAll('.portfolio-dot');
          dots.forEach((dot, idx) => {
            if (idx === page) {
              dot.classList.add('bg-amber-500', 'scale-125');
              dot.classList.remove('bg-black/20', 'dark:bg-white/20');
            } else {
              dot.classList.remove('bg-amber-500', 'scale-125');
              dot.classList.add('bg-black/20', 'dark:bg-white/20');
            }
          });
        }}>
          {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, pageIndex) => (
            <div key={pageIndex} className="min-w-full flex-shrink-0 snap-center px-2 sm:px-4">
              <div className="grid grid-cols-3 gap-2 sm:gap-4 md:gap-6">
              {filteredWorks.slice(pageIndex * 9, (pageIndex + 1) * 9).map((w, pageI) => {
                const i = pageIndex * 9 + pageI;
                const hasVideo = !!w.videoUrl;
                return (
            <div
              key={w.id}
              className="group cursor-pointer transition-transform duration-300 w-full" 
              onClick={() => setSelectedIndex(i)}
            >
              <div className="relative aspect-square rounded-xl sm:rounded-2xl overflow-hidden bg-black/5 dark:bg-[#111] shadow-lg border border-black/5 dark:border-white/5">
                <PortfolioMediaContent w={w} isYoutube={isYoutube} getYoutubeEmbedUrl={getYoutubeEmbedUrl} selectedWork={selectedWork} />
                
                <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent opacity-80 group-hover:opacity-100 transition-all duration-500 flex flex-col justify-end p-3 sm:p-6 md:p-8">
                  <div className="transform translate-y-2 sm:translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    {w.category && (
                      <span className="inline-block px-2 py-1 bg-amber-500 text-black text-[8px] sm:text-xs font-bold rounded-full mb-1 sm:mb-3 shadow-md">
                        {w.category}
                      </span>
                    )}
                    <h3 className="text-[10px] sm:text-xl md:text-2xl font-bold text-white mb-1 sm:mb-2 line-clamp-1">{w.title}</h3>
                    <div className="flex items-center gap-1 sm:gap-2 text-white/90 text-[8px] sm:text-sm font-bold opacity-0 group-hover:opacity-100 transition-opacity">
                      <span className="w-4 sm:w-8 h-[2px] bg-amber-500"></span>
                      {hasVideo ? (language === 'ar' ? 'تشغيل' : 'Play') : (language === 'ar' ? 'عرض' : 'View')}
                    </div>
                  </div>
                </div>

                {hasVideo && (
                  <div className="absolute top-2 rtl:right-2 ltr:left-2 sm:top-4 sm:rtl:right-4 ltr:left-4 w-6 h-6 sm:w-12 sm:h-12 bg-amber-500/90 backdrop-blur-sm rounded-full flex items-center justify-center text-black shadow-xl scale-90 group-hover:scale-100 transition-transform">
                    <Video className="w-3 h-3 sm:w-6 sm:h-6" />
                  </div>
                )}
              </div>
            </div>
          );
        })}
              </div>
            </div>
          ))}
        </div>
        {Math.ceil(filteredWorks.length / 9) > 1 && (
          <div className="flex justify-center items-center gap-2 mt-4">
            {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, idx) => (
              <button 
                key={idx}
                className={`portfolio-dot w-2.5 h-2.5 rounded-full transition-all duration-300 ${idx === 0 ? 'bg-amber-500 scale-125' : 'bg-black/20 dark:bg-white/20'}`}
                onClick={() => {
                  const slider = document.getElementById('portfolio-slider');
                  if (slider) {
                    slider.scrollTo({
                      left: (document.dir === 'rtl' ? -1 : 1) * idx * slider.offsetWidth,
                      behavior: 'smooth'
                    });
                  }
                }}
              />
            ))}
          </div>
        )}
      </div>"""

new_slider = """      <div className="relative w-full">
        <div 
          className="flex overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-8 w-full" 
          id="portfolio-slider" 
          style={{ scrollBehavior: 'smooth' }}
          onScroll={(e) => {
            const target = e.target as HTMLElement;
            const scrollLeft = target.scrollLeft;
            const width = target.offsetWidth;
            const page = Math.round(Math.abs(scrollLeft) / width);
            const dots = document.querySelectorAll('.portfolio-dot');
            dots.forEach((dot, idx) => {
              if (idx === page) {
                dot.classList.add('bg-amber-500', 'scale-125');
                dot.classList.remove('bg-black/20', 'dark:bg-white/20');
              } else {
                dot.classList.remove('bg-amber-500', 'scale-125');
                dot.classList.add('bg-black/20', 'dark:bg-white/20');
              }
            });
          }}
        >
          {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, pageIndex) => (
            <div key={pageIndex} className="min-w-full flex-shrink-0 snap-center px-1 sm:px-4">
              <div className="grid grid-cols-3 grid-rows-3 gap-1.5 sm:gap-4 md:gap-6">
                {filteredWorks.slice(pageIndex * 9, (pageIndex + 1) * 9).map((w, pageI) => {
                  const i = pageIndex * 9 + pageI;
                  const hasVideo = !!w.videoUrl;
                  return (
                    <div
                      key={w.id}
                      className="group cursor-pointer transition-transform duration-300 w-full" 
                      onClick={() => setSelectedIndex(i)}
                    >
                      <div className="relative aspect-square rounded-lg sm:rounded-2xl overflow-hidden bg-black/5 dark:bg-[#111] shadow-md border border-black/5 dark:border-white/5">
                        <PortfolioMediaContent w={w} isYoutube={isYoutube} getYoutubeEmbedUrl={getYoutubeEmbedUrl} selectedWork={selectedWork} />
                        
                        <div className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-300 flex flex-col justify-end p-2 sm:p-6 md:p-8">
                          <div className="transform translate-y-2 group-hover:translate-y-0 transition-transform duration-300">
                            {w.category && (
                              <span className="hidden sm:inline-block px-2 py-1 bg-amber-500 text-black text-[8px] sm:text-xs font-bold rounded-full mb-1 sm:mb-3 shadow-md">
                                {w.category}
                              </span>
                            )}
                            <h3 className="text-[9px] sm:text-xl md:text-2xl font-bold text-white mb-0.5 sm:mb-2 line-clamp-1">{w.title}</h3>
                          </div>
                        </div>

                        {hasVideo && (
                          <div className="absolute top-1.5 rtl:right-1.5 ltr:left-1.5 sm:top-4 sm:rtl:right-4 sm:ltr:left-4 w-5 h-5 sm:w-10 sm:h-10 bg-amber-500/90 backdrop-blur-sm rounded-full flex items-center justify-center text-black shadow-lg scale-90 group-hover:scale-100 transition-transform">
                            <Video className="w-2.5 h-2.5 sm:w-5 sm:h-5" />
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
        
        {Math.ceil(filteredWorks.length / 9) > 1 && (
          <div className="flex justify-center items-center gap-2 mt-2">
            {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, idx) => (
              <button 
                key={idx}
                className={`portfolio-dot w-2 h-2 sm:w-2.5 sm:h-2.5 rounded-full transition-all duration-300 ${idx === 0 ? 'bg-amber-500 scale-125' : 'bg-black/20 dark:bg-white/20'}`}
                onClick={() => {
                  const slider = document.getElementById('portfolio-slider');
                  if (slider) {
                    slider.scrollTo({
                      left: (document.dir === 'rtl' ? -1 : 1) * idx * slider.offsetWidth,
                      behavior: 'smooth'
                    });
                  }
                }}
              />
            ))}
          </div>
        )}
      </div>"""

if old_slider in content:
    content = content.replace(old_slider, new_slider)
else:
    print("WARNING: Could not find old slider to replace.")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
