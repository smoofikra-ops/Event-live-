import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

ar_errors = """
    'error.name': 'الاسم مطلوب',
    'error.email': 'البريد الإلكتروني مطلوب',
    'error.emailInvalid': 'يرجى إدخال بريد إلكتروني صحيح',
    'error.phone': 'رقم الهاتف مطلوب',
    'error.phoneInvalid': 'يجب أن يبدأ الرقم بـ 05 ويتكون من 10 أرقام',
    'error.clientType': 'يرجى اختيار نوع العميل',
    'error.eventType': 'يرجى اختيار نوع الفعالية',
"""

en_errors = """
    'error.name': 'Name is required',
    'error.email': 'Email is required',
    'error.emailInvalid': 'Please enter a valid email address',
    'error.phone': 'Phone number is required',
    'error.phoneInvalid': 'Number must start with 05 and contain 10 digits',
    'error.clientType': 'Please select a client type',
    'error.eventType': 'Please select an event type',
"""

content = content.replace("'quote.title': 'طلب عرض سعر',", "'quote.title': 'طلب عرض سعر',\n" + ar_errors)
content = content.replace("'quote.title': 'Request a Quote',", "'quote.title': 'Request a Quote',\n" + en_errors)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)

with open("src/App.tsx", "r", encoding="utf-8") as f:
    app_content = f.read()

app_content = app_content.replace("'الاسم مطلوب'", "t('error.name')")
app_content = app_content.replace("'البريد الإلكتروني مطلوب'", "t('error.email')")
app_content = app_content.replace("'يرجى إدخال بريد إلكتروني صحيح'", "t('error.emailInvalid')")
app_content = app_content.replace("'رقم الهاتف مطلوب'", "t('error.phone')")
app_content = app_content.replace("'يجب أن يبدأ الرقم بـ 05 ويتكون من 10 أرقام'", "t('error.phoneInvalid')")
app_content = app_content.replace("'يرجى اختيار نوع العميل'", "t('error.clientType')")
app_content = app_content.replace("'يرجى اختيار نوع الفعالية'", "t('error.eventType')")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(app_content)
