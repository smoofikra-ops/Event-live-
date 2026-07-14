import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Portfolio Grid
old_portfolio_grid = 'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6 pb-8 w-full px-2 sm:px-4"'
new_portfolio_grid = 'className="grid grid-cols-2 lg:grid-cols-3 gap-2 sm:gap-4 md:gap-6 pb-8 w-full px-2 sm:px-4"'
content = content.replace(old_portfolio_grid, new_portfolio_grid)

# 2. Fix Navigation
# First, hide the hamburger on md:
old_hamburger = 'className={`fixed top-4 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 hover:text-black transition-colors ${language === "ar" ? "left-4" : "right-4"}`}'
new_hamburger = 'className={`md:hidden fixed top-4 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 hover:text-black transition-colors ${language === "ar" ? "left-4" : "right-4"}`}'
content = content.replace(old_hamburger, new_hamburger)

# Then, hide the sidebar panel on md: (optional, but good for safety)
old_panel = 'className={`fixed top-0 bottom-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl ${language === "ar" ? "left-0 border-r" : "right-0 border-l"}`}'
new_panel = 'className={`md:hidden fixed top-0 bottom-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl ${language === "ar" ? "left-0 border-r" : "right-0 border-l"}`}'
content = content.replace(old_panel, new_panel)

# Also hide the AnimatePresence backdrop on md:
old_backdrop = 'className="fixed inset-0 bg-black/60 backdrop-blur-sm z-[90]"'
new_backdrop = 'className="md:hidden fixed inset-0 bg-black/60 backdrop-blur-sm z-[90]"'
content = content.replace(old_backdrop, new_backdrop)

# Add DesktopNav right before the hamburger button
desktop_nav_code = """
      {/* Desktop Navigation */}
      <div className="hidden md:flex fixed top-0 left-0 right-0 z-[90] h-20 items-center px-8 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm transition-all">
        <div className="flex items-center gap-2">
          <Camera className="w-8 h-8 text-amber-500" />
          <span className="text-2xl font-black text-gradient">EventLive</span>
        </div>
        
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
        </div>
        
        <div className="flex items-center gap-4">
          <button 
            onClick={() => setLanguage(language === 'ar' ? 'en' : 'ar')}
            className="px-4 py-2 rounded-full bg-black/5 dark:bg-white/5 hover:bg-black/10 dark:hover:bg-white/10 transition-colors font-bold text-sm"
          >
            {language === 'ar' ? 'English' : 'عربي'}
          </button>
          <ThemeToggle />
          <button 
            onClick={onQuoteClick}
            className="btn-primary px-6 py-2 text-sm hidden lg:block"
          >
            {t('hero.cta')}
          </button>
        </div>
      </div>
"""

# Insert DesktopNav before the hamburger
content = content.replace("<>\n      <button", "<>\n" + desktop_nav_code + "      <button")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

