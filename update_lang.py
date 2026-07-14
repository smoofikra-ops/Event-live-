import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

ar_insert = """
    'footer.companyDesc': 'شركة سعودية متخصصة في خدمات التصوير الفوتوغرافي والفيديو والبث المباشر للفعاليات والمؤتمرات بأعلى معايير الجودة.',
    'footer.quickLinks': 'روابط سريعة',
    'footer.service1': 'التصوير الفوتوغرافي',
    'footer.service2': 'تصوير الفيديو',
    'footer.service3': 'البث المباشر',
    'footer.service4': 'تغطية المؤتمرات',
    'quote.title': 'طلب عرض سعر',
    'quote.subtitle': 'يسعدنا تواصلكم معنا. يرجى تعبئة النموذج التالي لنتمكن من خدمتكم بشكل أفضل.',
    'quote.name': 'الاسم',
    'quote.email': 'البريد الإلكتروني',
    'quote.phone': 'رقم الجوال (يبدأ بـ 05)',
    'quote.clientType': 'نوع العميل',
    'quote.selectClientType': 'اختر نوع العميل',
    'quote.eventType': 'نوع الفعالية',
    'quote.selectEventType': 'اختر نوع الفعالية',
    'quote.submit': 'إرسال الطلب عبر واتساب',
"""

en_insert = """
    'footer.companyDesc': 'A Saudi company specialized in photography, videography, and live streaming services for events and conferences with the highest quality standards.',
    'footer.quickLinks': 'Quick Links',
    'footer.service1': 'Photography',
    'footer.service2': 'Videography',
    'footer.service3': 'Live Streaming',
    'footer.service4': 'Conference Coverage',
    'quote.title': 'Request a Quote',
    'quote.subtitle': 'We are happy to hear from you. Please fill out the form below so we can serve you better.',
    'quote.name': 'Name',
    'quote.email': 'Email',
    'quote.phone': 'Phone Number (starts with 05)',
    'quote.clientType': 'Client Type',
    'quote.selectClientType': 'Select Client Type',
    'quote.eventType': 'Event Type',
    'quote.selectEventType': 'Select Event Type',
    'quote.submit': 'Submit via WhatsApp',
"""

content = content.replace("'footer.powered': 'تطوير',", "'footer.powered': 'تطوير',\n" + ar_insert)
content = content.replace("'footer.powered': 'Powered by',", "'footer.powered': 'Powered by',\n" + en_insert)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)
