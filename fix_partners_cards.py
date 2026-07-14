import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_partners_div = """      <div className="relative w-full overflow-hidden flex bg-black/5 dark:bg-white/5 py-10 border-y border-black/10 dark:border-white/10 group" dir="ltr">
        <div className="flex w-max animate-marquee group-hover:[animation-play-state:paused] py-4">
          {[...partners, ...partners, ...partners].map((p, index) => (
            <div 
              key={index} 
              className="group/card relative mx-2 sm:mx-8 w-24 sm:w-72 h-16 sm:h-40 flex items-center justify-center transition-all duration-500 cursor-pointer select-none"
            >
              {/* إضاءات خلفية من زوايا مختلفة في الوضع الداكن */}
              <div className="absolute inset-0 opacity-0 dark:opacity-100 pointer-events-none transition-all duration-500">
                <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-tr from-amber-500/10 via-transparent to-blue-500/10 blur-xl rounded-full transform scale-150"></div>
                <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3/4 h-3/4 bg-white/5 blur-2xl rounded-full"></div>
              </div>
              
              <img 
                src={p.logo} 
                alt={p.name} 
                className={`w-full h-full object-contain relative z-10 transition-all duration-500 group-hover/card:scale-110 group-hover/card:-translate-y-2 ${index % 2 === 0 ? 'group-hover/card:rotate-3' : 'group-hover/card:-rotate-3'} drop-shadow-[0_4px_15px_rgba(0,0,0,0.15)] dark:drop-shadow-[0_0_20px_rgba(255,255,255,0.25)]`} 
              />
            </div>
          ))}
        </div>
      </div>"""

new_partners_div = """      <div className="relative w-full overflow-hidden flex bg-transparent py-12 group" dir="ltr">
        {/* Animated gradient fade at the edges for smoothness */}
        <div className="absolute left-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-r from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        <div className="absolute right-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-l from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        
        <div className="flex w-max animate-marquee group-hover:[animation-play-state:paused] py-4">
          {[...partners, ...partners, ...partners].map((p, index) => (
            <div 
              key={index} 
              className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-[#111] shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_20px_40px_rgba(255,138,0,0.15)] hover:-translate-y-2 p-4 sm:p-6"
            >
              {/* 3D Border Effects */}
              <div className="absolute inset-0 rounded-2xl border-t border-l border-white/80 dark:border-white/10 pointer-events-none transition-colors duration-500 group-hover/card:border-amber-500/30"></div>
              <div className="absolute inset-0 rounded-2xl border-b-2 border-r-2 border-black/5 dark:border-black/40 pointer-events-none transition-colors duration-500 group-hover/card:border-amber-500/20"></div>
              
              {/* Background Lights for dark mode */}
              <div className="absolute inset-0 opacity-0 dark:opacity-100 pointer-events-none transition-all duration-500 overflow-hidden rounded-2xl">
                <div className="absolute -top-1/2 -left-1/2 w-full h-full bg-amber-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
                <div className="absolute -bottom-1/2 -right-1/2 w-full h-full bg-blue-500/10 blur-2xl transform group-hover/card:scale-150 transition-transform duration-700"></div>
              </div>
              
              <img 
                src={p.logo} 
                alt={p.name} 
                className="w-full h-full object-contain relative z-10 transition-transform duration-500 group-hover/card:scale-110 drop-shadow-sm dark:drop-shadow-[0_0_15px_rgba(255,255,255,0.15)]" 
              />
            </div>
          ))}
        </div>
      </div>"""

content = content.replace(old_partners_div, new_partners_div)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
