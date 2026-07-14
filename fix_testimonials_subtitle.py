import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("'testimonials.title': 'قالوا عنا',", "'testimonials.title': 'قالوا عنا',\n    'testimonials.subtitle': 'تعليقات عملائنا ونحن نعتز بآرائهم',")
content = content.replace("'testimonials.title': 'Testimonials',", "'testimonials.title': 'Testimonials',\n    'testimonials.subtitle': 'Our customers comments and we cherish their opinions.',")

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)
