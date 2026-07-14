import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    app_content = f.read()

# Remove partners from its old position and put it after Hero
app_content = app_content.replace('        <Partners partners={data.partners} />\n', '')
app_content = app_content.replace(
    '<Hero videoUrl={data.heroVideoUrl} onQuoteClick={() => setIsQuoteOpen(true)} />\n',
    '<Hero videoUrl={data.heroVideoUrl} onQuoteClick={() => setIsQuoteOpen(true)} />\n        <Partners partners={data.partners} />\n'
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(app_content)

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    lang_content = f.read()

lang_content = lang_content.replace(
    "'partners.trustDesc': 'نفخر بالعمل مع نخبة من الشركات والجهات الحكومية'",
    "'partners.trustDesc': 'نفخر بالعمل مع الجهات الحكومية ونخبة من الشركات والمؤسسات'"
)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(lang_content)

