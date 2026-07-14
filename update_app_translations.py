import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace hardcoded services titles/descriptions
# In App.tsx: 
#    { id: '1', title: "المعارض", desc: "نبرز حضوركم المميز من خلال تغطية احترافية تشمل أجنحة الزوار والفعاليات المصاحبة، بواسطة كاميرات احترافية ودرون.", iconName: 'Layout', ...
# But these are part of INITIAL_DATA. We shouldn't change INITIAL_DATA directly because user might change them. 
# Instead, in the render methods, we do: 
# t(`service.${service.id}.title`) || service.title

content = content.replace(
    '<h3 className="text-xl md:text-2xl font-bold mb-4 text-black dark:text-white group-hover:text-amber-500 transition-colors drop-shadow-sm">{service.title}</h3>',
    '<h3 className="text-xl md:text-2xl font-bold mb-4 text-black dark:text-white group-hover:text-amber-500 transition-colors drop-shadow-sm">{t(`service.${service.id}.title`) !== `service.${service.id}.title` ? t(`service.${service.id}.title`) : service.title}</h3>'
)

content = content.replace(
    '<p className="text-black/70 dark:text-white/70 text-sm md:text-base leading-relaxed drop-shadow-sm font-medium">{service.desc}</p>',
    '<p className="text-black/70 dark:text-white/70 text-sm md:text-base leading-relaxed drop-shadow-sm font-medium">{t(`service.${service.id}.desc`) !== `service.${service.id}.desc` ? t(`service.${service.id}.desc`) : service.desc}</p>'
)

# Portfolio Categories
content = content.replace(
    "['الكل', 'تصوير', 'فيديو', 'بث مباشر']",
    "['portfolio.all', 'portfolio.photography', 'portfolio.video', 'portfolio.livestream']"
)
content = content.replace(
    "<button\n                key={category}",
    "<button\n                key={category}"
)

# In the render of categories:
content = re.sub(
    r'<button\s*key=\{category\}\s*onClick=\{\(\) => setActiveCategory\(category\)\}\s*className=\{`([^`]+)`\s*\+\s*\(\s*activeCategory === category\s*\?\s*\'([^\']+)\'\s*:\s*\'([^\']+)\'\s*\)\}\s*>',
    r'<button\n                key={category}\n                onClick={() => setActiveCategory(category)}\n                className={`\1` + (activeCategory === category ? \'\2\' : \'\3\')}\n              >\n                {t(category)}',
    content
)

# The activeCategory starts with 'الكل'. Let's change the initial state.
content = content.replace("useState<string>('الكل');", "useState<string>('portfolio.all');")

# Filtering works
# if (activeCategory !== 'الكل')
content = content.replace("if (activeCategory !== 'الكل')", "if (activeCategory !== 'portfolio.all')")

# The condition: 
#   if (activeCategory === 'تصوير' && w.category !== 'تصوير') return false;
# Let's fix the logic for filtering works:
# The `w.category` is still in Arabic in `INITIAL_DATA` ("فيديو", "تصوير", "بث مباشر").
# So we need to map activeCategory to Arabic to filter if activeCategory is 'portfolio.video' etc.
filter_code = """
              const catMap: Record<string, string> = {
                'portfolio.photography': 'تصوير',
                'portfolio.video': 'فيديو',
                'portfolio.livestream': 'بث مباشر'
              };
              if (activeCategory !== 'portfolio.all' && w.category !== catMap[activeCategory]) return false;
"""
content = re.sub(
    r'if \(activeCategory !== \'portfolio.all\'\) \{.*?\n\s*\}',
    filter_code.strip(),
    content,
    flags=re.DOTALL
)

# Works titles
content = content.replace(
    '<h3 className="text-white font-bold text-lg md:text-xl">{work.title}</h3>',
    '<h3 className="text-white font-bold text-lg md:text-xl">{t(`work.${work.id}.title`) !== `work.${work.id}.title` ? t(`work.${work.id}.title`) : work.title}</h3>'
)

# Process
content = content.replace('const faqs = [', """
  const faqs = [
    { q: t('faq.q1'), a: t('faq.a1') },
    { q: t('faq.q2'), a: t('faq.a2') },
    { q: t('faq.q3'), a: t('faq.a3') },
    { q: t('faq.q4'), a: t('faq.a4') },
  ];
//""")
content = content.replace('//\n    { q: "ما هي مناطق الخدمة التي تغطونها؟"', '/*')
content = content.replace('    { q: "كيف يمكنني حجز موعد لفعاليتي؟", a: "يمكنكم التواصل معنا عبر نموذج الاتصال في الموقع أو عبر الواتساب مباشرة لتحديد الموعد ومناقشة التفاصيل." },\n  ];', '*/')

content = content.replace('const steps = [', """
  const steps = [
    { num: "01", title: t('process.step1.title'), desc: t('process.step1.desc') },
    { num: "02", title: t('process.step2.title'), desc: t('process.step2.desc') },
    { num: "03", title: t('process.step3.title'), desc: t('process.step3.desc') },
    { num: "04", title: t('process.step4.title'), desc: t('process.step4.desc') }
  ];
/*""")
content = content.replace('    { num: "04", title: "التسليم", desc: "المونتاج النهائي" }\n  ];', '*/')

content = content.replace('const testimonials = [', """
  const testimonials = [
    { name: t('testimonial.1.name'), role: t('testimonial.1.role'), text: t('testimonial.1.text') },
    { name: t('testimonial.2.name'), role: t('testimonial.2.role'), text: t('testimonial.2.text') },
    { name: t('testimonial.3.name'), role: t('testimonial.3.role'), text: t('testimonial.3.text') },
    { name: t('testimonial.4.name'), role: t('testimonial.4.role'), text: t('testimonial.4.text') },
    { name: t('testimonial.5.name'), role: t('testimonial.5.role'), text: t('testimonial.5.text') }
  ];
/*""")
content = content.replace('    { name: "فهد العبدالله", role: "مؤسس مؤسسة", text: "أشكركم على التغطية المميزة لحفل الافتتاح. الفريق كان متعاوناً جداً وقدموا لنا أفكاراً إبداعية أضافت قيمة للحدث." }\n  ];', '*/')

content = content.replace('<h2 className="text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent-center heading-gradient">آلية العمل</h2>', '<h2 className="text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent-center heading-gradient">{t("process.title")}</h2>')
content = content.replace('<AnimatedTitle text="قالوا عنا" className="text-[40px] font-semibold title-accent-center heading-gradient mb-4" />', '<AnimatedTitle text={t("testimonials.title")} className="text-[40px] font-semibold title-accent-center heading-gradient mb-4" />')


with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
