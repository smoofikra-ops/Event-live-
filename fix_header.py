import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Desktop Navigation changes:
old_desktop_start = """      {/* Desktop Navigation */}
      <div className="hidden md:flex fixed top-10 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all justify-between">
        {/* Empty left space to balance the right side controls */}
        <div className="w-[100px] xl:w-[200px]"></div>"""
new_desktop_start = """      {/* Desktop Navigation */}
      <div className="hidden md:flex fixed top-10 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all justify-between">
        <div className="w-[100px] xl:w-[200px] flex justify-start items-center">
          <a href="#home" className="flex items-center">
            <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-10 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)] transition-transform hover:scale-105 duration-300" />
          </a>
        </div>"""

if old_desktop_start in content:
    content = content.replace(old_desktop_start, new_desktop_start)
else:
    print("Desktop start not found")

# Replace navLinks iteration
old_desktop_ul = """          <ul className="flex items-center gap-2 md:gap-4" onMouseLeave={() => setHoveredIndex(null)}>
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
          </ul>"""

new_desktop_ul = """          <ul className="flex items-center gap-2 md:gap-4" onMouseLeave={() => setHoveredIndex(null)}>
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
          </ul>"""

if old_desktop_ul in content:
    content = content.replace(old_desktop_ul, new_desktop_ul)
else:
    print("Desktop ul not found")


# Mobile Navigation changes:
old_mobile = """      {/* Mobile Navigation Header */}
      <div className="md:hidden fixed top-10 left-0 right-0 z-[100] h-16 flex items-center justify-between px-4 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm">
        <div className="flex-1"></div>
        <a href="#home" className="flex items-center justify-center flex-1">
          <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-8 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
        </a>
        <div className="flex-1 flex justify-end">"""

new_mobile = """      {/* Mobile Navigation Header */}
      <div className="md:hidden fixed top-10 left-0 right-0 z-[100] h-16 flex items-center justify-between px-4 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm">
        <div className="flex-1 flex justify-start">
          <a href="#home" className="flex items-center">
            <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-8 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
          </a>
        </div>
        <div className="flex-1 flex justify-center"></div>
        <div className="flex-1 flex justify-end">"""

if old_mobile in content:
    content = content.replace(old_mobile, new_mobile)
else:
    print("Mobile nav not found")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
