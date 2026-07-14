import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

ar_contact = """
    'contact.phone': 'رقم الهاتف',
    'contact.location': 'الموقع',
    'contact.locationDesc': 'الرياض، المملكة العربية السعودية',
    'contact.nameLabel': 'الاسم (إلزامي)',
    'contact.namePlaceholder': 'أدخل اسمك الكريم',
    'contact.emailLabel': 'البريد الإلكتروني (اختياري)',
    'contact.phoneLabel': 'رقم الجوال',
    'contact.clientIndividuals': 'أفراد',
    'contact.clientCompanies': 'شركات ومؤسسات',
    'contact.clientGov': 'جهات حكومية',
    'contact.serviceLabel': 'الخدمة المطلوبة',
    'contact.serviceVideo': 'تصوير فيديو ومونتاج',
    'contact.servicePhoto': 'تصوير فوتوغرافي',
    'contact.serviceLive': 'بث مباشر للفعاليات',
    'contact.serviceCoverage': 'تغطية شاملة للمعارض والمؤتمرات',
    'contact.serviceOther': 'أخرى',
    'contact.detailsLabel': 'الرسالة أو التفاصيل',
    'contact.dictationHint': 'تحدث لإدخال النص',
    'contact.dictationListening': 'جاري الاستماع...',
    'contact.dictationBtn': 'إملاء صوتي',
    'contact.detailsPlaceholder': 'اكتب تفاصيل طلبك هنا...',
    'contact.submitBtn': 'إرسال الآن',
"""

en_contact = """
    'contact.phone': 'Phone Number',
    'contact.location': 'Location',
    'contact.locationDesc': 'Riyadh, Kingdom of Saudi Arabia',
    'contact.nameLabel': 'Name (Required)',
    'contact.namePlaceholder': 'Enter your full name',
    'contact.emailLabel': 'Email Address (Optional)',
    'contact.phoneLabel': 'Phone Number',
    'contact.clientIndividuals': 'Individuals',
    'contact.clientCompanies': 'Companies & Establishments',
    'contact.clientGov': 'Government Entities',
    'contact.serviceLabel': 'Requested Service',
    'contact.serviceVideo': 'Videography & Editing',
    'contact.servicePhoto': 'Photography',
    'contact.serviceLive': 'Live Streaming for Events',
    'contact.serviceCoverage': 'Comprehensive Coverage for Exhibitions',
    'contact.serviceOther': 'Other',
    'contact.detailsLabel': 'Message or Details',
    'contact.dictationHint': 'Speak to input text',
    'contact.dictationListening': 'Listening...',
    'contact.dictationBtn': 'Voice Dictation',
    'contact.detailsPlaceholder': 'Write the details of your request here...',
    'contact.submitBtn': 'Send Now',
"""

content = content.replace("'contact.subtitle': 'نحن هنا للإجابة على استفساراتك ومساعدتك في تغطية فعاليتك بأفضل صورة.',", "'contact.subtitle': 'نحن هنا للإجابة على استفساراتك ومساعدتك في تغطية فعاليتك بأفضل صورة.',\n" + ar_contact)
content = content.replace("'contact.subtitle': 'We are here to answer your inquiries and help you cover your events in the best possible way.',", "'contact.subtitle': 'We are here to answer your inquiries and help you cover your events in the best possible way.',\n" + en_contact)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)

with open("src/App.tsx", "r", encoding="utf-8") as f:
    app_content = f.read()

app_content = app_content.replace(">رقم الهاتف<", ">{t('contact.phone')}<")
app_content = app_content.replace(">الموقع<", ">{t('contact.location')}<")
app_content = app_content.replace(">الرياض، المملكة العربية السعودية<", ">{t('contact.locationDesc')}<")
app_content = app_content.replace(">الاسم (إلزامي)<", ">{t('contact.nameLabel')}<")
app_content = app_content.replace('placeholder="أدخل اسمك الكريم"', 'placeholder={t("contact.namePlaceholder")}')
app_content = app_content.replace(">البريد الإلكتروني (اختياري)<", ">{t('contact.emailLabel')}<")
app_content = app_content.replace(">رقم الجوال<", ">{t('contact.phoneLabel')}<")
app_content = app_content.replace(">أفراد<", ">{t('contact.clientIndividuals')}<")
app_content = app_content.replace('value="أفراد"', 'value={t("contact.clientIndividuals")}')
app_content = app_content.replace(">شركات ومؤسسات<", ">{t('contact.clientCompanies')}<")
app_content = app_content.replace('value="شركات"', 'value={t("contact.clientCompanies")}')
app_content = app_content.replace(">جهات حكومية<", ">{t('contact.clientGov')}<")
app_content = app_content.replace('value="جهات حكومية"', 'value={t("contact.clientGov")}')
app_content = app_content.replace(">الخدمة المطلوبة<", ">{t('contact.serviceLabel')}<")
app_content = app_content.replace(">تصوير فيديو ومونتاج<", ">{t('contact.serviceVideo')}<")
app_content = app_content.replace('value="تصوير فيديو"', 'value={t("contact.serviceVideo")}')
app_content = app_content.replace(">تصوير فوتوغرافي<", ">{t('contact.servicePhoto')}<")
app_content = app_content.replace('value="تصوير فوتوغرافي"', 'value={t("contact.servicePhoto")}')
app_content = app_content.replace(">بث مباشر للفعاليات<", ">{t('contact.serviceLive')}<")
app_content = app_content.replace('value="بث مباشر"', 'value={t("contact.serviceLive")}')
app_content = app_content.replace(">تغطية شاملة للمعارض والمؤتمرات<", ">{t('contact.serviceCoverage')}<")
app_content = app_content.replace('value="تغطية شاملة"', 'value={t("contact.serviceCoverage")}')
app_content = app_content.replace(">أخرى<", ">{t('contact.serviceOther')}<")
app_content = app_content.replace('value="أخرى"', 'value={t("contact.serviceOther")}')
app_content = app_content.replace(">الرسالة أو التفاصيل<", ">{t('contact.detailsLabel')}<")
app_content = app_content.replace('title="تحدث لإدخال النص"', 'title={t("contact.dictationHint")}')
app_content = app_content.replace("'جاري الاستماع...'", 't("contact.dictationListening")')
app_content = app_content.replace("'إملاء صوتي'", 't("contact.dictationBtn")')
app_content = app_content.replace('placeholder="اكتب تفاصيل طلبك هنا..."', 'placeholder={t("contact.detailsPlaceholder")}')
app_content = app_content.replace("'إرسال الآن'", 't("contact.submitBtn")')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(app_content)
