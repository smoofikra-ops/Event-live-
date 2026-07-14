import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace footer items
content = content.replace('شركة سعودية متخصصة في خدمات التصوير الفوتوغرافي والفيديو والبث المباشر للفعاليات والمؤتمرات بأعلى معايير الجودة.', '{t("footer.companyDesc")}')
content = content.replace('>روابط سريعة<', '>{t("footer.quickLinks")}<')
content = content.replace('>الرئيسية<', '>{t("nav.home")}<')
content = content.replace('>الخدمات<', '>{t("nav.services")}<')
content = content.replace('>أعمالنا<', '>{t("nav.portfolio")}<')
content = content.replace('>الأسئلة الشائعة<', '>{t("nav.faq")}<')

content = content.replace('>خدماتنا<', '>{t("nav.services")}<')
content = content.replace('>التصوير الفوتوغرافي<', '>{t("footer.service1")}<')
content = content.replace('>تصوير الفيديو<', '>{t("footer.service2")}<')
content = content.replace('>البث المباشر<', '>{t("footer.service3")}<')
content = content.replace('>تغطية المؤتمرات<', '>{t("footer.service4")}<')

# Quote Request Modal
content = content.replace('طلب عرض سعر', '{t("quote.title")}')
content = content.replace('يسعدنا تواصلكم معنا. يرجى تعبئة النموذج التالي لنتمكن من خدمتكم بشكل أفضل.', '{t("quote.subtitle")}')
content = content.replace('>الاسم<', '>{t("quote.name")}<')
content = content.replace('>البريد الإلكتروني<', '>{t("quote.email")}<')
content = content.replace('>رقم الجوال (يبدأ بـ 05)<', '>{t("quote.phone")}<')
content = content.replace('>نوع العميل<', '>{t("quote.clientType")}<')
content = content.replace('اختر نوع العميل', '{t("quote.selectClientType")}')
content = content.replace('>نوع الفعالية<', '>{t("quote.eventType")}<')
content = content.replace('اختر نوع الفعالية', '{t("quote.selectEventType")}')
content = content.replace('إرسال الطلب عبر واتساب', '{t("quote.submit")}')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
