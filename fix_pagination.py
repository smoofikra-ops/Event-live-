import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_slider = """      <div className="flex overflow-x-auto snap-x snap-mandatory hide-scrollbar pb-8 w-full">
        {Array.from({ length: Math.ceil(filteredWorks.length / 9) }).map((_, pageIndex) => (
          <div key={pageIndex} className="min-w-full flex-shrink-0 snap-center px-2 sm:px-4">
            <div className="grid grid-cols-3 gap-2 sm:gap-4 md:gap-6">"""

new_slider = """      <div className="relative w-full">
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
              <div className="grid grid-cols-3 gap-2 sm:gap-4 md:gap-6">"""

content = content.replace(old_slider, new_slider)

old_slider_end = """              </div>
            </div>
          );
        })}
            </div>
          </div>
        ))}
      </div>"""

new_slider_end = """              </div>
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

content = content.replace(old_slider_end, new_slider_end)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
