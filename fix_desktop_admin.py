import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_desktop_actions = """        <div className="flex items-center gap-4">
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
        </div>"""

new_desktop_actions = """        <div className="flex items-center gap-4">
          <button 
            onClick={() => setLanguage(language === 'ar' ? 'en' : 'ar')}
            className="px-4 py-2 rounded-full bg-black/5 dark:bg-white/5 hover:bg-black/10 dark:hover:bg-white/10 transition-colors font-bold text-sm"
          >
            {language === 'ar' ? 'English' : 'عربي'}
          </button>
          <ThemeToggle />
          <button 
            onClick={onAdminClick}
            className={`w-10 h-10 rounded-full flex items-center justify-center transition-colors ${isAdminMode ? 'bg-amber-500 text-black' : 'bg-black/5 dark:bg-white/5 text-black/70 dark:text-white/70 hover:bg-black/10 dark:hover:bg-white/10'}`}
          >
            <Settings className="w-5 h-5" />
          </button>
          <button 
            onClick={onQuoteClick}
            className="btn-primary px-6 py-2 text-sm hidden lg:block"
          >
            {t('hero.cta')}
          </button>
        </div>"""

content = content.replace(old_desktop_actions, new_desktop_actions)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
