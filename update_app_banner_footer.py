import re

with open("src/index.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Make marquee faster (35s -> 20s)
css_content = css_content.replace("animation: marquee 35s linear infinite;", "animation: marquee 20s linear infinite;")

# Add gradient-x animation if it doesn't exist
if "gradient-x" not in css_content:
    css_content += """
@keyframes gradient-x {
  0%, 100% {
      background-size: 200% 200%;
      background-position: left center;
  }
  50% {
      background-size: 200% 200%;
      background-position: right center;
  }
}
.animate-gradient-x {
  animation: gradient-x 3s ease infinite;
}
"""

with open("src/index.css", "w", encoding="utf-8") as f:
    f.write(css_content)

with open("src/App.tsx", "r", encoding="utf-8") as f:
    app_content = f.read()

# Update Footer phone number
app_content = app_content.replace(
    """<a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">""",
    """<a href="tel:0536753679" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">"""
)
app_content = app_content.replace(
    """<span className="font-medium text-sm" dir="ltr">+966 50 000 0000</span>""",
    """<span className="font-medium text-sm" dir="ltr">0536753679</span>"""
)

# Update Announcement Banner
old_banner = """const AnnouncementBanner = () => {
  const { t, language } = useLanguage();
  return (
    <div className="fixed top-0 left-0 right-0 h-10 bg-gradient-to-r from-amber-500 to-[#FFC300] text-black flex items-center overflow-hidden z-[110] border-b border-black/10 shadow-md">
      <div className="flex animate-marquee whitespace-nowrap min-w-full" dir="ltr">
        {Array.from({ length: 4 }).map((_, i) => (
          <div key={i} className={`flex items-center gap-8 px-4 ${language === 'ar' ? 'flex-row-reverse' : ''}`}>
            <span className="font-bold flex items-center gap-2"><Star className="w-4 h-4" /> {t('banner.1')}</span>
            <span className="font-bold flex items-center gap-2"><Building2 className="w-4 h-4" /> {t('banner.2')}</span>
            <span className="font-bold flex items-center gap-2"><Video className="w-4 h-4" /> {t('banner.3')}</span>
            <span className="font-bold flex items-center gap-2"><Radio className="w-4 h-4" /> {t('banner.4')}</span>
            <span className="font-bold flex items-center gap-2"><Camera className="w-4 h-4" /> {t('banner.5')}</span>
          </div>
        ))}
      </div>
    </div>
  );
};"""

new_banner = """const AnnouncementBanner = () => {
  const { t, language } = useLanguage();
  return (
    <div className="fixed top-0 left-0 right-0 h-10 bg-gradient-to-r from-[#FF0080] via-[#FF8C00] to-[#40E0D0] animate-gradient-x text-white flex items-center overflow-hidden z-[110] shadow-md border-b border-white/20">
      <div className="flex animate-marquee whitespace-nowrap min-w-full" dir="ltr">
        {Array.from({ length: 8 }).map((_, i) => (
          <div key={i} className={`flex items-center gap-6 px-4 text-[10px] md:text-xs ${language === 'ar' ? 'flex-row-reverse' : ''}`}>
            <span className="font-bold flex items-center gap-1.5"><Star className="w-3.5 h-3.5 animate-[spin_3s_linear_infinite] text-yellow-300" /> {t('banner.1')}</span>
            <span className="font-bold flex items-center gap-1.5"><Building2 className="w-3.5 h-3.5 animate-pulse text-blue-200" /> {t('banner.2')}</span>
            <span className="font-bold flex items-center gap-1.5"><Video className="w-3.5 h-3.5 animate-[bounce_2s_infinite] text-green-300" /> {t('banner.3')}</span>
            <span className="font-bold flex items-center gap-1.5"><Radio className="w-3.5 h-3.5 animate-pulse text-red-200" /> {t('banner.4')}</span>
            <span className="font-bold flex items-center gap-1.5"><Camera className="w-3.5 h-3.5 animate-[spin_4s_linear_infinite] text-purple-200" /> {t('banner.5')}</span>
          </div>
        ))}
      </div>
    </div>
  );
};"""

app_content = app_content.replace(old_banner, new_banner)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(app_content)
