import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

ar_final = """
    'contact.whatsappText': 'مرحباً، أنا مهتم جداً ومتحمس لخدماتكم، أرجو التواصل معي.',
    'contact.alertSuccess': 'تم حفظ التغييرات بنجاح!',
    'process.stepsDesc': 'خطوات بسيطة تضمن لكم أفضل النتائج',
    'partners.trustDesc': 'نفخر بالعمل مع نخبة من الشركات والجهات الحكومية',
    'testimonials.trustDesc': 'نفخر بثقة عملائنا ونعتز بآرائهم',
    'contact.formDesc': 'نحن هنا للإجابة على استفساراتكم ومساعدتكم في تغطية فعالياتكم بأفضل شكل ممكن.',
"""

en_final = """
    'contact.whatsappText': 'Hello, I am very interested in your services. Please contact me.',
    'contact.alertSuccess': 'Changes saved successfully!',
    'process.stepsDesc': 'Simple steps that guarantee the best results',
    'partners.trustDesc': 'We are proud to work with top companies and government entities',
    'testimonials.trustDesc': 'We take pride in our clients trust and value their feedback',
    'contact.formDesc': 'We are here to answer your questions and help you cover your events in the best way possible.',
"""

content = content.replace("'contact.detailsPlaceholder': 'اكتب تفاصيل طلبك هنا...',", "'contact.detailsPlaceholder': 'اكتب تفاصيل طلبك هنا...',\n" + ar_final)
content = content.replace("'contact.detailsPlaceholder': 'Write the details of your request here...',", "'contact.detailsPlaceholder': 'Write the details of your request here...',\n" + en_final)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)

with open("src/App.tsx", "r", encoding="utf-8") as f:
    app_content = f.read()

app_content = app_content.replace(">خطوات بسيطة تضمن لكم أفضل النتائج<", ">{t('process.stepsDesc')}<")
app_content = app_content.replace(">نفخر بالعمل مع نخبة من الشركات والجهات الحكومية<", ">{t('partners.trustDesc')}<")
app_content = app_content.replace(">نفخر بثقة عملائنا ونعتز بآرائهم<", ">{t('testimonials.trustDesc')}<")
app_content = app_content.replace(">نحن هنا للإجابة على استفساراتكم ومساعدتكم في تغطية فعالياتكم بأفضل شكل ممكن.<", ">{t('contact.formDesc')}<")
app_content = app_content.replace("مرحباً، أنا مهتم جداً ومتحمس لخدماتكم، أرجو التواصل معي.", "{t('contact.whatsappText')}")
app_content = app_content.replace("'تم حفظ التغييرات بنجاح!'", "t('contact.alertSuccess')")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(app_content)
