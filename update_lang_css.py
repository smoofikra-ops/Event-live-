import re

# Update LanguageContext.tsx
with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    lang_content = f.read()

ar_banner4 = "    'banner.4': 'تصوير جوي وأرضي وبث مباشر بأعلى جودة',"
en_banner4 = "    'banner.4': 'Aerial, Ground Filming & High-Quality Live Streaming',"

lang_content = lang_content.replace(ar_banner4, ar_banner4 + "\n    'banner.5': 'لدينا خدمة التصوير بالدرون ولدينا قسم كامل للمونتاج',")
lang_content = lang_content.replace(en_banner4, en_banner4 + "\n    'banner.5': 'Professional Drone Photography & Full Editing Department',")

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(lang_content)

# Update index.css for marquee animation speed
with open("src/index.css", "r", encoding="utf-8") as f:
    css_content = f.read()

old_marquee = """animation: marquee 80s linear infinite;"""
new_marquee = """animation: marquee 35s linear infinite;"""

css_content = css_content.replace(old_marquee, new_marquee)

with open("src/index.css", "w", encoding="utf-8") as f:
    f.write(css_content)

