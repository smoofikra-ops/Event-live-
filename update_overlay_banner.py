import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Update CameraFrameOverlay
old_top_bar = """      {/* Top Bar */}
      <div className="flex justify-between items-start w-full">"""

new_top_bar = """      {/* Top Bar */}
      <div className="flex justify-between items-start w-full mt-24 md:mt-20">"""

content = content.replace(old_top_bar, new_top_bar)

# Update AnnouncementBanner texts
old_banner_content = """            <span className="font-bold flex items-center gap-2"><Star className="w-4 h-4" /> {t('banner.1')}</span>
            <span className="font-bold flex items-center gap-2"><Building2 className="w-4 h-4" /> {t('banner.2')}</span>
            <span className="font-bold flex items-center gap-2"><Video className="w-4 h-4" /> {t('banner.3')}</span>
            <span className="font-bold flex items-center gap-2"><Radio className="w-4 h-4" /> {t('banner.4')}</span>"""

new_banner_content = """            <span className="font-bold flex items-center gap-2"><Star className="w-4 h-4" /> {t('banner.1')}</span>
            <span className="font-bold flex items-center gap-2"><Building2 className="w-4 h-4" /> {t('banner.2')}</span>
            <span className="font-bold flex items-center gap-2"><Video className="w-4 h-4" /> {t('banner.3')}</span>
            <span className="font-bold flex items-center gap-2"><Radio className="w-4 h-4" /> {t('banner.4')}</span>
            <span className="font-bold flex items-center gap-2"><Camera className="w-4 h-4" /> {t('banner.5')}</span>"""

content = content.replace(old_banner_content, new_banner_content)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
