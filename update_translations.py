import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

ar_banner = """    'banner.1': 'موثقون لأكبر الفعاليات والمؤتمرات',
    'banner.2': 'ثقة كبرى العلامات التجارية',
    'banner.3': 'فريق متخصص ومعدات سينمائية جاهزة لتغطية فعالياتكم في جميع مدن ومناطق المملكة',
    'banner.4': 'تصوير جوي وأرضي وبث مباشر بأعلى جودة',"""

en_banner = """    'banner.1': 'Documenting Major Events & Conferences',
    'banner.2': 'Trusted by Top Brands',
    'banner.3': 'Specialized Team & Cinematic Equipment Ready Across the Kingdom',
    'banner.4': 'Aerial, Ground Filming & High-Quality Live Streaming',"""

content = content.replace("    'portfolio.all': 'الكل',", ar_banner + "\n    'portfolio.all': 'الكل',")
content = content.replace("    'portfolio.all': 'All',", en_banner + "\n    'portfolio.all': 'All',")

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)
