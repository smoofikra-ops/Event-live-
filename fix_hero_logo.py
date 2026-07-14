import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_hero_badge = """          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-white/10 dark:bg-white/5 backdrop-blur-md border border-black/10 dark:border-white/20 text-amber-500 md:text-amber-400 text-sm font-black mb-8"
          >"""

new_hero_badge = """          <div className="md:hidden flex justify-center mb-8">
            <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-16 object-contain drop-shadow-[0_0_20px_rgba(255,138,0,0.4)]" />
          </div>

          <motion.div 
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.2 }}
            className="inline-flex items-center gap-3 px-5 py-2.5 rounded-full bg-white/10 dark:bg-white/5 backdrop-blur-md border border-black/10 dark:border-white/20 text-amber-500 md:text-amber-400 text-sm font-black mb-8"
          >"""
content = content.replace(old_hero_badge, new_hero_badge)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
