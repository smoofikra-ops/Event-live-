import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the floating button with a fixed mobile navbar
old_mobile_btn = """      <button 
        onClick={() => setIsOpen(!isOpen)}
        className={`md:hidden fixed top-4 z-[100] w-12 h-12 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-xl hover:bg-amber-500 hover:text-black transition-colors ${language === "ar" ? "left-4" : "right-4"}`}
      >
        {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
      </button>"""

new_mobile_btn = """      {/* Mobile Navigation Header */}
      <div className="md:hidden fixed top-0 left-0 right-0 z-[100] h-16 flex items-center justify-between px-4 bg-white/60 dark:bg-[#0a0a0a]/60 backdrop-blur-xl border-b border-black/10 dark:border-white/10 shadow-sm">
        <div className="flex-1"></div>
        <a href="#home" className="flex items-center justify-center flex-1">
          <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-8 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
        </a>
        <div className="flex-1 flex justify-end">
          <button 
            onClick={() => setIsOpen(!isOpen)}
            className="w-10 h-10 bg-black/80 dark:bg-white/10 backdrop-blur-md rounded-full flex items-center justify-center text-white border border-white/10 shadow-md hover:bg-amber-500 hover:text-black transition-colors"
          >
            {isOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>"""
content = content.replace(old_mobile_btn, new_mobile_btn)

# Remove the logo from Hero section
old_hero_logo = """          <div className="md:hidden flex justify-center mb-8">
            <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-16 object-contain drop-shadow-[0_0_20px_rgba(255,138,0,0.4)]" />
          </div>"""

content = content.replace(old_hero_logo, "")

# Add recording label to hero video
old_video = """        <video 
          autoPlay 
          muted 
          loop 
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
          poster="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2000"
        >
          <source src={heroVideoUrl} type="video/mp4" />
        </video>"""

new_video = """        <div className="absolute inset-0 w-full h-full">
          <video 
            autoPlay 
            muted 
            loop 
            playsInline
            className="w-full h-full object-cover"
            poster="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2000"
          >
            <source src={heroVideoUrl} type="video/mp4" />
          </video>
          {/* Recording indicator overlay */}
          <div className="absolute top-24 rtl:right-8 ltr:left-8 md:top-24 md:rtl:right-12 md:ltr:left-12 flex items-center gap-2 bg-black/40 backdrop-blur-sm border border-white/10 px-3 py-1.5 rounded-full z-[10]">
            <span className="w-3 h-3 bg-red-600 rounded-full animate-pulse shadow-[0_0_10px_rgba(220,38,38,0.8)]"></span>
            <span className="text-white text-xs font-bold tracking-widest uppercase">REC</span>
          </div>
        </div>"""

content = content.replace(old_video, new_video)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
