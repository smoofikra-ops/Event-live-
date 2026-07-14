import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the entire home section to implement the responsive layout
old_hero = """  return (
    <section id="home" className="relative min-h-[50svh] md:min-h-[100svh] flex items-center pt-16 md:pt-20 overflow-hidden dark border-b border-white/10">
      {/* Background Video/Image */}
      <div className="absolute inset-0 z-0 overflow-hidden">
        {videoUrl ? (
          isYoutube ? (
            <div className="w-full h-full scale-110">
              <iframe 
                src={embedUrl}
                className="w-full h-full pointer-events-none object-cover"
                allow="autoplay; encrypted-media"
                title="Hero Background"
              ></iframe>
            </div>
          ) : (
            <div className="w-full h-full">
              <video 
                src={videoUrl}
                autoPlay
                muted={isMuted}
                loop
                playsInline
                poster="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2070"
                className="w-full h-full max-md:object-contain object-cover bg-black/10 dark:bg-black"
                style={{ objectPosition: 'center center' }}
              />
              <button 
                onClick={() => setIsMuted(!isMuted)}
                className="absolute bottom-8 rtl:right-8 ltr:left-8 z-50 p-4 rounded-full bg-black/30 backdrop-blur-md border border-white/10 text-white hover:bg-black/50 transition-colors hover:scale-110 active:scale-95 group"
                aria-label={isMuted ? "فتح الصوت" : "إغلاق الصوت"}
              >
                {isMuted ? (
                  <VolumeX className="w-6 h-6 group-hover:text-amber-500 transition-colors" />
                ) : (
                  <Volume2 className="w-6 h-6 group-hover:text-amber-500 transition-colors" />
                )}
              </button>
            </div>
          )
        ) : (
          <img 
            src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2070" 
            className="w-full h-full object-cover opacity-40"
            alt="خلفية لفعالية حية"
            loading="eager"
            referrerPolicy="no-referrer"
          />
        )}
        {/* Dark Overlay for text clarity - Lightened as requested */}
        <div className="absolute inset-0 bg-black/20 dark:bg-black/30 pointer-events-none"></div>
        <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent pointer-events-none"></div>
        
        {/* Animated Light Beams */}
        <div className="absolute inset-0 opacity-30 pointer-events-none">
          <motion.div 
            animate={{ 
              x: ["-100%", "100%"],
              opacity: [0, 1, 0]
            }}
            transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
            className="absolute top-0 bottom-0 w-[500px] bg-gradient-to-r from-transparent via-[#FF8A00]/20 to-transparent skew-x-12"
          />
        </div>

        {/* Floating Particles */}
        <div className="absolute inset-0 pointer-events-none">
          {[...Array(20)].map((_, i) => (
            <motion.div
              key={i}
              initial={{ 
                x: Math.random() * 100 + "%", 
                y: Math.random() * 100 + "%",
                opacity: Math.random()
              }}
              animate={{ 
                y: [null, "-20px", "20px"],
                opacity: [0.2, 0.5, 0.2]
              }}
              transition={{ 
                duration: 3 + Math.random() * 2, 
                repeat: Infinity, 
                ease: "easeInOut" 
              }}
              className="absolute w-1 h-1 bg-amber-500 rounded-full blur-[1px]"
            />
          ))}
        </div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-6 w-full py-20">
        <motion.div 
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
          className="max-w-4xl"
        >
          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-amber-400 text-sm font-black mb-8"
          >
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500 animate-pulse"></span>
            {t('hero.badge')}
          </motion.div>
          
          <CustomHeroSequence />
          
          <div className="flex flex-wrap gap-6 relative z-10 mt-6">
            <motion.button 
              whileHover={{ scale: 1.05, boxShadow: "0 0 30px rgba(255,138,0,0.5)" }}
              whileTap={{ scale: 0.95 }}
              onClick={onQuoteClick} 
              className="btn-primary text-lg px-10 py-5 relative"
            >
              {t('hero.cta')}
            </motion.button>
            <motion.button 
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => document.getElementById('portfolio')?.scrollIntoView()} 
              className="btn-glass text-lg px-10 py-5"
            >
              {t('hero.portfolio')}
            </motion.button>
          </div>
        </motion.div>
      </div>
    </section>
  );"""

new_hero = """  return (
    <section id="home" className="relative md:min-h-[100svh] flex flex-col md:flex-row md:items-center pt-20 md:pt-20 overflow-hidden dark border-b border-white/10 bg-[#0a0a0a]">
      {/* Background Video/Image (Desktop) & Inline Video (Mobile) */}
      <div className="relative md:absolute md:inset-0 z-0 w-full md:h-full md:overflow-hidden aspect-video md:aspect-auto">
        {videoUrl ? (
          isYoutube ? (
            <div className="w-full h-full md:scale-110">
              <iframe 
                src={embedUrl}
                className="w-full h-full pointer-events-none object-cover"
                allow="autoplay; encrypted-media"
                title="Hero Background"
              ></iframe>
            </div>
          ) : (
            <div className="w-full h-full relative">
              <video 
                src={videoUrl}
                autoPlay
                muted={isMuted}
                loop
                playsInline
                poster="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2070"
                className="w-full h-full object-cover bg-black"
                style={{ objectPosition: 'center center' }}
              />
              <button 
                onClick={() => setIsMuted(!isMuted)}
                className="absolute bottom-4 rtl:right-4 ltr:left-4 md:bottom-8 md:rtl:right-8 md:ltr:left-8 z-50 p-2 md:p-4 rounded-full bg-black/30 backdrop-blur-md border border-white/10 text-white hover:bg-black/50 transition-colors hover:scale-110 active:scale-95 group"
                aria-label={isMuted ? "فتح الصوت" : "إغلاق الصوت"}
              >
                {isMuted ? (
                  <VolumeX className="w-4 h-4 md:w-6 md:h-6 group-hover:text-amber-500 transition-colors" />
                ) : (
                  <Volume2 className="w-4 h-4 md:w-6 md:h-6 group-hover:text-amber-500 transition-colors" />
                )}
              </button>
            </div>
          )
        ) : (
          <img 
            src="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2070" 
            className="w-full h-full object-cover opacity-60 md:opacity-40"
            alt="خلفية لفعالية حية"
            loading="eager"
            referrerPolicy="no-referrer"
          />
        )}
        
        {/* Dark Overlay for text clarity on desktop */}
        <div className="hidden md:block absolute inset-0 bg-black/20 dark:bg-black/30 pointer-events-none"></div>
        <div className="hidden md:block absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent pointer-events-none"></div>
      </div>

      {/* Mobile background decorative */}
      <div className="md:hidden absolute inset-0 bottom-0 bg-[#0a0a0a] z-0 -mt-20"></div>

      {/* Animated Light Beams (Desktop only) */}
      <div className="hidden md:block absolute inset-0 opacity-30 pointer-events-none z-0">
        <motion.div 
          animate={{ 
            x: ["-100%", "100%"],
            opacity: [0, 1, 0]
          }}
          transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
          className="absolute top-0 bottom-0 w-[500px] bg-gradient-to-r from-transparent via-[#FF8A00]/20 to-transparent skew-x-12"
        />
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-7xl mx-auto px-6 w-full py-10 md:py-20 flex-1 flex flex-col justify-center">
        <motion.div 
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
          className="max-w-4xl"
        >
          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-white/10 dark:bg-white/5 backdrop-blur-md border border-black/10 dark:border-white/20 text-amber-500 md:text-amber-400 text-sm font-black mb-8"
          >
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500 animate-pulse"></span>
            {t('hero.badge')}
          </motion.div>
          
          <CustomHeroSequence />
          
          <div className="flex flex-wrap gap-4 md:gap-6 relative z-10 mt-6">
            <motion.button 
              whileHover={{ scale: 1.05, boxShadow: "0 0 30px rgba(255,138,0,0.5)" }}
              whileTap={{ scale: 0.95 }}
              onClick={onQuoteClick} 
              className="btn-primary text-base md:text-lg px-8 py-4 md:px-10 md:py-5 relative w-full sm:w-auto"
            >
              {t('hero.cta')}
            </motion.button>
            <motion.button 
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => document.getElementById('portfolio')?.scrollIntoView()} 
              className="btn-glass text-base md:text-lg px-8 py-4 md:px-10 md:py-5 w-full sm:w-auto text-center"
            >
              {t('hero.portfolio')}
            </motion.button>
          </div>
        </motion.div>
      </div>
    </section>
  );"""

if old_hero in content:
    content = content.replace(old_hero, new_hero)
else:
    print("Could not find the old hero section to replace. It might have been modified.")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

