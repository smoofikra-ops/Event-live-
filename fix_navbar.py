import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_nav = """      {/* Desktop Navigation */}
      <div className="hidden md:flex fixed top-0 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all">
        <a href="#home" className="flex items-center gap-2">
          <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-10 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
        </a>
        
        <div className="flex-1 flex justify-center">
          <ul className="flex items-center gap-2" onMouseLeave={() => setHoveredIndex(null)}>
            {navLinks.map((link, idx) => (
              <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
                <a 
                  href={link.href} 
                  className="relative z-10 flex items-center gap-2 px-4 py-2 font-bold text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white transition-colors duration-300 text-sm lg:text-base"
                >
                  {link.icon}
                  {link.label}
                </a>
                {hoveredIndex === idx && (
                  <motion.div
                    layoutId="mercury-desktop-nav"
                    className="absolute inset-0 bg-gradient-to-r from-amber-500/80 to-amber-300/80 dark:from-amber-600/50 dark:to-orange-500/50 rounded-xl -z-0 backdrop-blur-md shadow-[0_0_15px_rgba(255,138,0,0.5)]"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
              </li>
            ))}
          </ul>
        </div>"""

new_nav = """      {/* Desktop Navigation */}
      <div className="hidden md:flex fixed top-0 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all justify-between">
        {/* Empty left space to balance the right side controls */}
        <div className="w-[100px] xl:w-[200px]"></div>
        
        <div className="flex-1 flex justify-center relative">
          <ul className="flex items-center gap-2 md:gap-4" onMouseLeave={() => setHoveredIndex(null)}>
            {navLinks.slice(0, 2).map((link, idx) => (
              <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
                <a 
                  href={link.href} 
                  className="relative z-10 flex items-center gap-2 px-4 py-2 font-bold text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white transition-colors duration-300 text-sm lg:text-base"
                >
                  {link.icon}
                  {link.label}
                </a>
                {hoveredIndex === idx && (
                  <motion.div
                    layoutId="mercury-desktop-nav"
                    className="absolute inset-0 bg-gradient-to-r from-amber-500/80 to-amber-300/80 dark:from-amber-600/50 dark:to-orange-500/50 rounded-xl -z-0 backdrop-blur-md shadow-[0_0_15px_rgba(255,138,0,0.5)]"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
              </li>
            ))}
            
            <li className="mx-2 lg:mx-6 flex items-center justify-center relative z-10">
              <a href="#home" className="flex items-center">
                <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-10 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)] transition-transform hover:scale-105 duration-300" />
              </a>
            </li>

            {navLinks.slice(2).map((link, i) => {
              const idx = i + 2;
              return (
              <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
                <a 
                  href={link.href} 
                  className="relative z-10 flex items-center gap-2 px-4 py-2 font-bold text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white transition-colors duration-300 text-sm lg:text-base"
                >
                  {link.icon}
                  {link.label}
                </a>
                {hoveredIndex === idx && (
                  <motion.div
                    layoutId="mercury-desktop-nav"
                    className="absolute inset-0 bg-gradient-to-r from-amber-500/80 to-amber-300/80 dark:from-amber-600/50 dark:to-orange-500/50 rounded-xl -z-0 backdrop-blur-md shadow-[0_0_15px_rgba(255,138,0,0.5)]"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
              </li>
            )})}
          </ul>
        </div>"""

if old_nav in content:
    content = content.replace(old_nav, new_nav)
else:
    print("Pattern not found!")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
