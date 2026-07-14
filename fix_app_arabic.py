import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '<h2 className="text-[40px] font-semibold mb-6 title-accent heading-gradient">أعمالنا السابقة</h2>',
    '<h2 className="text-[40px] font-semibold mb-6 title-accent heading-gradient">{t(\'portfolio.title\')}</h2>'
)

content = content.replace(
    'نفتخر بسجل حافل من الإنجازات والفعاليات التي قمنا بتوثيقها بأعلى معايير الجودة والإبداع.',
    '{t(\'portfolio.subtitle\')}'
)

content = content.replace(
    '<p className="text-black/50 dark:text-white/50 max-w-[70ch] mx-auto text-[16px] md:text-[18px] font-normal">إليك بعض الإجابات على التساؤلات الأكثر شيوعاً حول خدماتنا.</p>',
    '<p className="text-black/50 dark:text-white/50 max-w-[70ch] mx-auto text-[16px] md:text-[18px] font-normal">{t(\'faq.subtitle\')}</p>'
)

content = content.replace(
    "{hasVideo ? 'تشغيل' : 'عرض'}",
    "{hasVideo ? (language === 'ar' ? 'تشغيل' : 'Play') : (language === 'ar' ? 'عرض' : 'View')}"
)

# And language needs to be extracted from `useLanguage()` in Portfolio.
# Wait, `Portfolio` component might not have `language` from `useLanguage()`.
# Let's check `Portfolio` component.
with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

