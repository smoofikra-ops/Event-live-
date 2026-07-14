import re

sidebar = """
const Sidebar = ({ onAdminClick, isAdminMode, onQuoteClick }: { onAdminClick: () => void, isAdminMode: boolean, onQuoteClick: () => void }) => {
  const { language, setLanguage, t } = useLanguage();
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { label: t('nav.home'), href: '#home', icon: <Home className="w-5 h-5" /> },
    { label: t('nav.services'), href: '#services', icon: <Layout className="w-5 h-5" /> },
    { label: t('nav.portfolio'), href: '#portfolio', icon: <Image className="w-5 h-5" /> },
    { label: t('nav.faq'), href: '#faq', icon: <MessageSquare className="w-5 h-5" /> },
    { label: t('nav.contact'), href: '#contact', icon: <Phone className="w-5 h-5" /> }
  ];

  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <>
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className="fixed top-6 ltr:right-6 rtl:left-6 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 transition-colors"
      >
        {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
      </button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setIsOpen(false)}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-[90]"
          />
        )}
      </AnimatePresence>

      <motion.div
        initial={{ x: language === 'ar' ? "100%" : "-100%" }}
        animate={{ x: isOpen ? 0 : (language === 'ar' ? "100%" : "-100%") }}
        transition={{ type: "spring", damping: 25, stiffness: 200 }}
        className="fixed top-0 bottom-0 ltr:left-0 rtl:right-0 w-72 bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-r rtl:border-l rtl:border-r-0 border-black/10 dark:border-white/10 flex flex-col p-8 shadow-2xl"
      >
        <div className="flex items-center gap-2 mb-12">
          <Camera className="w-8 h-8 text-amber-500" />
          <span className="text-2xl font-black text-gradient">EventLive</span>
        </div>

        <ul className="space-y-2 flex-1" onMouseLeave={() => setHoveredIndex(null)}>
          {navLinks.map((link, idx) => (
            <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
              <a 
                href={link.href} 
                onClick={(e) => {
                  setIsOpen(false);
                }}
                className="relative z-10 flex items-center gap-4 px-4 py-3 font-bold text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white transition-colors duration-300"
              >
                {link.icon}
                {link.label}
              </a>
              {hoveredIndex === idx && (
                <motion.div
                  layoutId="mercury-sidebar"
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

        <div className="flex flex-col gap-4 mt-8 pt-8 border-t border-black/10 dark:border-white/10">
          <div className="flex items-center justify-between">
            <button 
              onClick={() => setLanguage(language === 'ar' ? 'en' : 'ar')}
              className="px-4 py-2 rounded-full bg-black/5 dark:bg-white/5 font-bold hover:bg-black/10 dark:hover:bg-white/10 transition-colors"
            >
              {language === 'ar' ? 'English' : 'عربي'}
            </button>
            <ThemeToggle />
          </div>
          
          <button onClick={onQuoteClick} className="w-full py-3 bg-gradient-to-r from-[#FF8A00] to-[#FFC300] text-black font-black rounded-xl hover:shadow-[0_0_20px_rgba(255,138,0,0.4)] transition-all">
            {t('hero.cta')}
          </button>
        </div>
      </motion.div>
    </>
  );
};
"""

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Navbar component definition
pattern = re.compile(r'const Navbar = \(\{.*?</nav>\n\s*\}\n\s*;\n', re.DOTALL)
# Actually just matching till the end of the Navbar might be hard with regex. I'll just use simple replace if possible.
