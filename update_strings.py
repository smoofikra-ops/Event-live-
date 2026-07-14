import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# StatsSection
content = re.sub(
    r'(const StatsSection = \(\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('أرقام تتحدث', '{t("stats.title")}')
content = content.replace('فعالية موثقة', '{t("stats.events")}')
content = content.replace('سنوات خبرة', '{t("stats.years")}')
content = content.replace('رضا العملاء', '{t("stats.clients")}')

# Services
content = re.sub(
    r'(const Services = \({ services }: { services: Service\[\] }\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('خدماتنا المتميزة', '{t("services.title")}')
content = content.replace('نقدم مجموعة شاملة من خدمات التصوير والإنتاج البصري لجميع أنواع الفعاليات بأعلى معايير الجودة العالمية.', '{t("services.subtitle")}')

# Process
content = re.sub(
    r'(const Process = \(\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('>كيف نعمل<', '>{t("process.title")}<')
content = content.replace('>عملية بسيطة ومنظمة لضمان الحصول على أفضل النتائج لعملائنا.<', '>{t("process.subtitle")}<')
content = content.replace('التواصل والاستشارة', '{t("process.step1.title")}')
content = content.replace('التخطيط والتحضير', '{t("process.step2.title")}')
content = content.replace('التنفيذ والتسليم', '{t("process.step3.title")}')

content = content.replace('نتواصل معك لفهم احتياجاتك ومتطلبات فعاليتك بالتفصيل لضمان تقديم الخدمة الأمثل.', '{t("process.step1.desc")}')
content = content.replace('نضع خطة شاملة للتصوير ونحضر المعدات المناسبة والكوادر المتخصصة لفعاليتك.', '{t("process.step2.desc")}')
content = content.replace('ننفذ التصوير بأعلى جودة ونقوم بعمليات المونتاج الاحترافية ونسلمك النتائج في الوقت المحدد.', '{t("process.step3.desc")}')

# Partners
content = re.sub(
    r'(const Partners = \({ partners }: { partners: Partner\[\] }\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('>شركاء النجاح<', '>{t("partners.title")}<')
content = content.replace('>نفتخر بالعمل مع نخبة من الشركات والجهات الحكومية في المملكة.<', '>{t("partners.subtitle")}<')

# Testimonials
content = re.sub(
    r'(const Testimonials = \(\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('>قالوا عنا<', '>{t("testimonials.title")}<')
content = content.replace('>آراء عملائنا وشركاء نجاحنا<', '>{t("testimonials.desc")}<')


# Portfolio
content = re.sub(
    r'(const Portfolio = \({ works }: { works: Work\[\] }\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('>معرض الأعمال | Portfolio<', '>{t("portfolio.title")}<')
content = content.replace('>نفتخر بمشاركة جزء من رحلتنا في توثيق أهم الفعاليات والمناسبات في المملكة.<', '>{t("portfolio.subtitle")}<')
content = content.replace('مشاهدة العمل', '{t("portfolio.watch")}')


# Contact
content = re.sub(
    r'(const Contact = \(\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('تواصل معنا اليوم', '{t("contact.title")}')
content = content.replace('نحن هنا للإجابة على استفساراتك ومساعدتك في تغطية فعاليتك بأفضل صورة.', '{t("contact.subtitle")}')

# Footer
content = re.sub(
    r'(const Footer = \({ socialLinks }: { socialLinks: SocialLink\[\] }\) => {)',
    r'\1\n  const { t } = useLanguage();',
    content
)
content = content.replace('جميع الحقوق محفوظة.', '{t("footer.rights")}')
content = content.replace('الشروط والأحكام', '{t("footer.terms")}')
content = content.replace('سياسة الخصوصية', '{t("footer.privacy")}')
# 'تواصل معنا' might be replaced differently. 
content = content.replace('>تواصل معنا<', '>{t("contact.title")}<')
content = content.replace('>نقدم لك أحدث حلول التصوير والإنتاج للفعاليات في السعودية. توثيق احترافي، بث مباشر بجودة عالية، وإنتاج مرئي متكامل.<', '>{t("footer.desc")}<')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
