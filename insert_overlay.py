import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_hero_bg = """      {/* Background Video/Image (Desktop) & Inline Video (Mobile) */}
      <div className="absolute inset-0 z-0 w-full h-full overflow-hidden">
        {videoUrl ? ("""

new_hero_bg = """      {/* Background Video/Image (Desktop) & Inline Video (Mobile) */}
      <div className="absolute inset-0 z-0 w-full h-full overflow-hidden">
        <CameraFrameOverlay />
        {videoUrl ? ("""

content = content.replace(old_hero_bg, new_hero_bg)

# Remove the old simple recording indicator
old_rec_indicator = """          {/* Recording indicator overlay */}
          <div className="absolute top-24 rtl:right-8 ltr:left-8 md:top-24 md:rtl:right-12 md:ltr:left-12 flex items-center gap-2 bg-black/40 backdrop-blur-sm border border-white/10 px-3 py-1.5 rounded-full z-[10]">
            <span className="w-3 h-3 bg-red-600 rounded-full animate-pulse shadow-[0_0_10px_rgba(220,38,38,0.8)]"></span>
            <span className="text-white text-xs font-bold tracking-widest uppercase">REC</span>
          </div>"""

content = content.replace(old_rec_indicator, "")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
