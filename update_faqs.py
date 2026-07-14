import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace Arabic FAQs
arabic_faqs_replacement = """    'faq.q1': 'ما هي مناطق الخدمة التي تغطونها؟',
    'faq.a1': 'نحن نغطي جميع مناطق المملكة العربية السعودية، ولدينا فرق جاهزة للتنقل لأي مدينة لتوثيق فعاليتكم.',
    'faq.q2': 'كم يستغرق تسليم العمل النهائي؟',
    'faq.a2': 'يعتمد ذلك على حجم الفعالية، ولكن عادة ما يتم تسليم الصور خلال 48 ساعة، والفيديو المونتاج خلال 5-7 أيام عمل.',
    'faq.q3': 'هل توفرون خدمة البث المباشر؟',
    'faq.a3': 'نعم، نوفر خدمات البث المباشر باحترافية عالية لمنصات التواصل الاجتماعي أو المواقع الخاصة بجودة 4K.',
    'faq.q4': 'كيف يمكنني حجز موعد لفعاليتي؟',
    'faq.a4': 'يمكنكم التواصل معنا عبر نموذج الاتصال في الموقع أو عبر الواتساب مباشرة لتحديد الموعد ومناقشة التفاصيل.',
    'faq.q5': 'هل تقدمون خدمات التصوير الجوي (الدرون)؟',
    'faq.a5': 'نعم، نوفر خدمات التصوير الجوي باستخدام أحدث طائرات الدرون المرخصة لضمان لقطات استثنائية وشاملة لفعالياتكم.',
    'faq.q6': 'هل يمكن تعديل الفيديو بعد التسليم؟',
    'faq.a6': 'بالتأكيد، نوفر للعميل فرصة لإبداء الملاحظات وإجراء التعديلات المطلوبة لضمان رضاكم التام عن المخرج النهائي.',
    'faq.q7': 'ما هي المعدات التي تستخدمونها في التصوير؟',
    'faq.a7': 'نستخدم أحدث الكاميرات السينمائية ومعدات الإضاءة والصوت الاحترافية لضمان أعلى جودة ممكنة في جميع تغطياتنا.',
    'faq.q8': 'هل توفرون طاقم تصوير نسائي؟',
    'faq.a8': 'نعم، لدينا طاقم نسائي متكامل ومحترف لتغطية الفعاليات والمناسبات النسائية بخصوصية واحترافية تامة.',"""

content = re.sub(
    r"'faq\.q1': 'ما هي مناطق الخدمة التي تغطونها\؟',.*?faq\.a4': 'يمكنكم التواصل معنا عبر نموذج الاتصال في الموقع أو عبر الواتساب مباشرة لتحديد الموعد ومناقشة التفاصيل\.',",
    arabic_faqs_replacement,
    content,
    flags=re.DOTALL
)

# Replace English FAQs
english_faqs_replacement = """    'faq.q1': 'What service areas do you cover?',
    'faq.a1': 'We cover all regions of Saudi Arabia, and we have teams ready to travel to any city to document your event.',
    'faq.q2': 'How long does it take to deliver the final work?',
    'faq.a2': 'It depends on the size of the event, but usually photos are delivered within 48 hours, and edited video within 5-7 working days.',
    'faq.q3': 'Do you provide live streaming services?',
    'faq.a3': 'Yes, we provide highly professional live streaming services for social media platforms or private websites in 4K quality.',
    'faq.q4': 'How can I book an appointment for my event?',
    'faq.a4': 'You can contact us via the contact form on the website or directly via WhatsApp to schedule an appointment and discuss details.',
    'faq.q5': 'Do you provide aerial (drone) photography services?',
    'faq.a5': 'Yes, we provide aerial photography services using the latest licensed drones to ensure exceptional and comprehensive shots of your events.',
    'faq.q6': 'Can the video be edited after delivery?',
    'faq.a6': 'Absolutely, we provide the client with the opportunity to give feedback and make the required modifications to ensure your complete satisfaction with the final output.',
    'faq.q7': 'What equipment do you use for shooting?',
    'faq.a7': 'We use the latest cinematic cameras and professional lighting and audio equipment to ensure the highest possible quality in all our coverage.',
    'faq.q8': 'Do you provide a female photography crew?',
    'faq.a8': 'Yes, we have a complete and professional female crew to cover female events and occasions with complete privacy and professionalism.',"""

content = re.sub(
    r"'faq\.q1': 'What service areas do you cover\?',.*?faq\.a4': 'You can contact us via the contact form on the website or directly via WhatsApp to schedule an appointment and discuss details\.',",
    english_faqs_replacement,
    content,
    flags=re.DOTALL
)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write(content)
