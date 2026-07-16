import React, { createContext, useContext, useState, useEffect } from 'react';

type Language = 'ar' | 'en';

interface LanguageContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
}

const translations: Record<Language, Record<string, string>> = {
  ar: {
    'banner.1': 'موثقون لأكبر الفعاليات والمؤتمرات',
    'banner.2': 'ثقة كبرى العلامات التجارية',
    'banner.3': 'فريق متخصص ومعدات سينمائية جاهزة لتغطية فعالياتكم في جميع مدن ومناطق المملكة',
    'banner.4': 'تصوير جوي وأرضي وبث مباشر بأعلى جودة',
    'banner.5': 'لدينا خدمة التصوير بالدرون ولدينا قسم كامل للمونتاج',
    'portfolio.all': 'الكل',
    'portfolio.video': 'فيديو',
    'portfolio.photography': 'تصوير',
    'portfolio.livestream': 'بث مباشر',

    'service.1.title': 'المعارض',
    'service.1.desc': 'نبرز حضوركم المميز من خلال تغطية احترافية تشمل أجنحة الزوار والفعاليات المصاحبة، بواسطة كاميرات احترافية ودرون.',
    'service.2.title': 'المهرجانات',
    'service.2.desc': 'نوثق أجواء المهرجانات بكل تفاصيلها، من لحظات التفاعل الجماهيري إلى العروض الترفيهية، مع إنتاج فيديوهات مميزة.',
    'service.3.title': 'الفعاليات الوطنية',
    'service.3.desc': 'نعيش معكم روح المناسبة وننقل مشاعر الفخر والانتماء بعدسة فنية، نوثق الفقرات الرسمية والجماهير بأسلوب يليق بالوطن.',
    'service.4.title': 'حفلات الافتتاح',
    'service.4.desc': 'نحوّل لحظات الافتتاح إلى قصة مرئية تُحكى، نوثق استقبال الضيوف، لحظة قص الشريط، ونصنع فيديو مختصر «هايلايت».',
    'service.5.title': 'المؤتمرات',
    'service.5.desc': 'نقدم تغطية مؤتمرات ومعارض احترافية، نوثق كل لحظة من الكلمات الرسمية إلى جلسات النقاش، مع إمكانيات البث المباشر.',
    'service.6.title': 'الفعاليات المؤسسية',
    'service.6.desc': 'نُقدّم تغطيات احترافية لفعاليات الشركات، المؤتمرات والاجتماعات، مع إبراز الهوية المؤسسية وتوفير خدمة البث المباشر.',
    'service.7.title': 'البث المباشر',
    'service.7.desc': 'نقدم خدمات البث المباشر الاحترافية للفعاليات والمؤتمرات بجودة عالية وتغطية شاملة تضمن وصول رسالتكم لأوسع جمهور.',
    'service.8.title': 'الإعلانات التجارية',
    'service.8.desc': 'نصمم محتوى بصري إبداعي يُبرز كل منتج بأفضل صورة، مع إعداد ستايل تصوير مميز وإخراج احترافي.',

    'work.1.title': 'معرض الزراعة',
    'work.2.title': 'كشتة موظفين',
    'work.3.title': 'مؤتمر التعدين',
    'work.4.title': 'مطعم جاردن لايت',
    'work.5.title': 'بنك الجزيرة كابيتال',
    'work.6.title': 'مهرجان الجولف',

    'process.title': 'آلية العمل',
    'process.step1.title': 'الاستشارة',
    'process.step1.desc': 'فهم احتياجاتكم',
    'process.step2.title': 'التخطيط',
    'process.step2.desc': 'تجهيز المعدات',
    'process.step3.title': 'التصوير',
    'process.step3.desc': 'تغطية الحدث',
    'process.step4.title': 'التسليم',
    'process.step4.desc': 'المونتاج النهائي',

        'faq.q1': 'ما هي مناطق الخدمة التي تغطونها؟',
    'faq.a1': 'نحن نغطي جميع مناطق المملكة العربية السعودية، ولدينا فرق جاهزة للتنقل لأي مدينة لتوثيق فعاليتكم.',
    'faq.q2': 'كم يستغرق تسليم العمل النهائي؟',
    'faq.a2': 'يعتمد ذلك على حجم الفعالية، ولكن عادة ما يتم تسليم الصور خلال 12 ساعة، والفيديو المونتاج خلال 24 ساعة.',
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
    'faq.a8': 'نعم، لدينا طاقم نسائي متكامل ومحترف لتغطية الفعاليات والمناسبات النسائية بخصوصية واحترافية تامة.',

    'testimonials.title': 'قالوا عنا',
    'testimonials.subtitle': 'تعليقات عملائنا ونحن نعتز بآرائهم',
    'testimonial.1.name': 'أحمد محمد',
    'testimonial.1.role': 'مدير فعاليات',
    'testimonial.1.text': 'تجربة رائعة مع فريق EventLive. الاحترافية في التعامل وجودة التصوير كانت تفوق التوقعات. شكراً لكم على توثيق فعاليتنا بأجمل صورة.',
    'testimonial.2.name': 'سارة العتيبي',
    'testimonial.2.role': 'منظمة مؤتمرات',
    'testimonial.2.text': 'فريق مبدع ومحترف جداً. التغطية كانت شاملة لكل تفاصيل المؤتمر، والمونتاج النهائي كان مذهلاً.',
    'testimonial.3.name': 'عبدالله السالم',
    'testimonial.3.role': 'صاحب شركة',
    'testimonial.3.text': 'من أفضل الشركات اللي تعاملنا معاها في مجال التغطية الإعلامية. التزام بالوقت وجودة في المخرجات لا يُعلى عليها.',
    'testimonial.4.name': 'نورة الخالد',
    'testimonial.4.role': 'مديرة علاقات عامة',
    'testimonial.4.text': 'خدماتهم في البث المباشر كانت استثنائية. الجودة عالية ولم نواجه أي مشاكل تقنية خلال الحدث بأكمله.',
    'testimonial.5.name': 'فهد العبدالله',
    'testimonial.5.role': 'مؤسس مؤسسة',
    'testimonial.5.text': 'أشكركم على التغطية المميزة لحفل الافتتاح. الفريق كان متعاوناً جداً وقدموا لنا أفكاراً إبداعية أضافت قيمة للحدث.',

    'nav.home': 'الرئيسية',
    'nav.services': 'الخدمات',
    'nav.portfolio': 'الأعمال',
    'nav.faq': 'الأسئلة الشائعة',
    'nav.contact': 'تواصل معنا',
    'nav.admin': 'الإدارة',
    
    'hero.badge': 'نوثق لحظتك ونوصلها بصوت وصورة',
    'hero.title.1': 'نوثق',
    'hero.title.2': 'لحظتك',
    'hero.title.3': 'باحترافية',
    'hero.title.4': 'عالية',
    'hero.desc': 'تصوير فوتوغرافي وفيديو وبث مباشر احترافي للمهرجانات، المؤتمرات، الفعاليات الوطنية، وغير ذلك في جميع أنحاء المملكة.',
    'hero.cta': 'اطلب عرض سعر',
    'hero.portfolio': 'عرض الأعمال',
    
    'services.title': 'خدماتنا المتميزة',
    'services.subtitle': 'نقدم مجموعة شاملة من خدمات التصوير والإنتاج البصري لجميع أنواع الفعاليات بأعلى معايير الجودة العالمية.',
    'services.discover': 'اكتشف المزيد',
    
    'portfolio.title': 'معرض الأعمال | Portfolio',
    'portfolio.subtitle': 'نفتخر بمشاركة جزء من رحلتنا في توثيق أهم الفعاليات والمناسبات في المملكة.',
    'portfolio.watch': 'مشاهدة العمل',
    
    'faq.title': 'الأسئلة الشائعة | FAQ',
    'faq.subtitle': 'إليك بعض الإجابات على الأسئلة الأكثر شيوعاً حول خدماتنا.',
    
    'contact.title': 'تواصل معنا',
    'contact.subtitle': 'نحن هنا للإجابة على استفساراتك ومساعدتك في تغطية فعاليتك بأفضل صورة.',

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

    'contact.whatsappText': 'مرحباً، أنا مهتم جداً ومتحمس لخدماتكم، أرجو التواصل معي.',
    'contact.alertSuccess': 'تم حفظ التغييرات بنجاح!',
    'process.stepsDesc': 'خطوات بسيطة تضمن لكم أفضل النتائج',
    'partners.trustDesc': 'نفخر بالعمل مع الجهات الحكومية ونخبة من الشركات والمؤسسات',
    'testimonials.trustDesc': 'نفخر بثقة عملائنا ونعتز بآرائهم',
    'contact.formDesc': 'نحن هنا للإجابة على استفساراتكم ومساعدتكم في تغطية فعالياتكم بأفضل شكل ممكن.',

    'contact.submitBtn': 'إرسال الآن',

    
    'partners.title': 'شركاء النجاح',
    'partners.subtitle': 'نفتخر بالعمل مع نخبة من الشركات والجهات الحكومية في المملكة.',
    
    'process.subtitle': 'عملية بسيطة ومنظمة لضمان الحصول على أفضل النتائج لعملائنا.',
    
    'stats.title': 'أرقام تتحدث',
    'stats.desc': 'سجل حافل بالنجاحات والإنجازات التي نفخر بها',
    'stats.events': 'فعالية موثقة',
    'stats.years': 'سنوات خبرة',
    'stats.clients': 'رضا العملاء',
    'stats.hours': 'ساعة تصوير',
    
    'testimonials.desc': 'آراء عملائنا وشركاء نجاحنا',
    
    'footer.rights': 'جميع الحقوق محفوظة.',
    'footer.terms': 'الشروط والأحكام',
    'footer.privacy': 'سياسة الخصوصية',
    'footer.contact': 'تواصل معنا',
    'footer.desc': 'نقدم لك أحدث حلول التصوير والإنتاج للفعاليات في السعودية. توثيق احترافي، بث مباشر بجودة عالية، وإنتاج مرئي متكامل.',
    'footer.powered': 'تطوير',
    
    'footer.companyDesc': 'شركة سعودية متخصصة في خدمات التصوير الفوتوغرافي والفيديو والبث المباشر للفعاليات والمؤتمرات بأعلى معايير الجودة.',
    'footer.quickLinks': 'روابط سريعة',
    'footer.service1': 'التصوير الفوتوغرافي',
    'footer.service2': 'تصوير الفيديو',
    'footer.service3': 'البث المباشر',
    'footer.service4': 'تغطية المؤتمرات',
    'quote.title': 'طلب عرض سعر',

    'error.name': 'الاسم مطلوب',
    'error.email': 'البريد الإلكتروني مطلوب',
    'error.emailInvalid': 'يرجى إدخال بريد إلكتروني صحيح',
    'error.phone': 'رقم الهاتف مطلوب',
    'error.phoneInvalid': 'يجب أن يبدأ الرقم بـ 05 ويتكون من 10 أرقام',
    'error.clientType': 'يرجى اختيار نوع العميل',
    'error.eventType': 'يرجى اختيار نوع الفعالية',

    'quote.subtitle': 'يسعدنا تواصلكم معنا. يرجى تعبئة النموذج التالي لنتمكن من خدمتكم بشكل أفضل.',
    'quote.name': 'الاسم',
    'quote.email': 'البريد الإلكتروني',
    'quote.phone': 'رقم الجوال (يبدأ بـ 05)',
    'quote.clientType': 'نوع العميل',
    'quote.selectClientType': 'اختر نوع العميل',
    'quote.eventType': 'نوع الفعالية',
    'quote.selectEventType': 'اختر نوع الفعالية',
    'quote.submit': 'إرسال الطلب عبر واتساب',
    'client.gov': 'جهة حكومية',
    'client.company': 'شركة',
    'client.org': 'مؤسسة',
    'client.individual': 'فرد',
    'event.exhibition': 'معرض',
    'event.festival': 'مهرجان',
    'event.conference': 'مؤتمر',
    'event.events': 'فعاليات',
    'event.corp': 'مناسبات شركات',
    'event.opening': 'حفل افتتاح',
    'event.national': 'مناسبة وطنية',
    'event.photography': 'تصوير',
    'event.realestate': 'عقاري',
    'event.ad': 'إعلان',
    'event.wedding': 'حفلة زواج',
    'event.personal': 'مناسبات شخصية',
    'event.other': 'نوع آخر',
  },
  en: {
    'banner.1': 'Documenting Major Events & Conferences',
    'banner.2': 'Trusted by Top Brands',
    'banner.3': 'Specialized Team & Cinematic Equipment Ready Across the Kingdom',
    'banner.4': 'Aerial, Ground Filming & High-Quality Live Streaming',
    'banner.5': 'Professional Drone Photography & Full Editing Department',
    'portfolio.all': 'All',
    'portfolio.video': 'Video',
    'portfolio.photography': 'Photography',
    'portfolio.livestream': 'Live Stream',

    'service.1.title': 'Exhibitions',
    'service.1.desc': 'We highlight your distinguished presence through professional coverage that includes visitor pavilions and accompanying events, using professional cameras and drones.',
    'service.2.title': 'Festivals',
    'service.2.desc': 'We document the atmosphere of festivals in all their details, from moments of public interaction to entertainment shows, producing distinctive videos.',
    'service.3.title': 'National Events',
    'service.3.desc': 'We live the spirit of the occasion with you and convey feelings of pride and belonging through an artistic lens, documenting the official segments and the audience in a style worthy of the nation.',
    'service.4.title': 'Opening Ceremonies',
    'service.4.desc': 'We turn the moments of the opening into a visual story to be told, documenting the reception of guests, the moment the ribbon is cut, and creating a short "highlight" video.',
    'service.5.title': 'Conferences',
    'service.5.desc': 'We provide professional coverage of conferences and exhibitions, documenting every moment from official speeches to discussion sessions, with live streaming capabilities.',
    'service.6.title': 'Corporate Events',
    'service.6.desc': 'We offer professional coverage for corporate events, conferences, and meetings, highlighting corporate identity and providing live streaming services.',
    'service.7.title': 'Live Broadcasting',
    'service.7.desc': 'We provide professional live broadcasting services for events and conferences with high quality and comprehensive coverage ensuring your message reaches the widest audience.',
    'service.8.title': 'Commercial Ads',
    'service.8.desc': 'We design creative visual content that highlights each product in the best way, with a distinctive photography style setup and professional directing.',

    'work.1.title': 'Agriculture Exhibition',
    'work.2.title': 'Employees Retreat',
    'work.3.title': 'Mining Conference',
    'work.4.title': 'Garden Light Restaurant',
    'work.5.title': 'AlJazira Capital Bank',
    'work.6.title': 'Golf Festival',

    'process.title': 'Our Process',
    'process.step1.title': 'Consultation',
    'process.step1.desc': 'Understanding your needs',
    'process.step2.title': 'Planning',
    'process.step2.desc': 'Preparing equipment',
    'process.step3.title': 'Shooting',
    'process.step3.desc': 'Event coverage',
    'process.step4.title': 'Delivery',
    'process.step4.desc': 'Final editing',

        'faq.q1': 'What service areas do you cover?',
    'faq.a1': 'We cover all regions of Saudi Arabia, and we have teams ready to travel to any city to document your event.',
    'faq.q2': 'How long does it take to deliver the final work?',
    'faq.a2': 'It depends on the size of the event, but usually photos are delivered within 12 hours, and edited video within 24 hours.',
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
    'faq.a8': 'Yes, we have a complete and professional female crew to cover female events and occasions with complete privacy and professionalism.',

    'testimonials.title': 'Testimonials',
    'testimonials.subtitle': 'Our customers comments and we cherish their opinions.',
    'testimonial.1.name': 'Ahmed Mohammed',
    'testimonial.1.role': 'Event Manager',
    'testimonial.1.text': 'A great experience with the EventLive team. The professionalism in handling and the quality of photography exceeded expectations. Thank you for documenting our event beautifully.',
    'testimonial.2.name': 'Sarah Al-Otaibi',
    'testimonial.2.role': 'Conference Organizer',
    'testimonial.2.text': 'A very creative and highly professional team. The coverage was comprehensive for all details of the conference, and the final editing was amazing.',
    'testimonial.3.name': 'Abdullah Al-Salem',
    'testimonial.3.role': 'Company Owner',
    'testimonial.3.text': 'One of the best companies we have dealt with in media coverage. Unmatched commitment to time and quality of output.',
    'testimonial.4.name': 'Noura Al-Khaled',
    'testimonial.4.role': 'PR Manager',
    'testimonial.4.text': 'Their live streaming services were exceptional. High quality and we faced no technical issues throughout the entire event.',
    'testimonial.5.name': 'Fahad Al-Abdullah',
    'testimonial.5.role': 'Foundation Founder',
    'testimonial.5.text': 'Thank you for the distinguished coverage of the opening ceremony. The team was very cooperative and provided us with creative ideas that added value to the event.',

    'nav.home': 'Home',
    'nav.services': 'Services',
    'nav.portfolio': 'Portfolio',
    'nav.faq': 'FAQ',
    'nav.contact': 'Contact',
    'nav.admin': 'Admin',
    
    'hero.badge': 'We document your moment with sound and vision',
    'hero.title.1': 'Documenting',
    'hero.title.2': 'Your Moments',
    'hero.title.3': 'With High',
    'hero.title.4': 'Professionalism',
    'hero.desc': 'Professional photography, videography, and live streaming for festivals, conferences, national events, and more across the Kingdom.',
    'hero.cta': 'Get a Quote',
    'hero.portfolio': 'View Portfolio',
    
    'services.title': 'Our Premium Services',
    'services.subtitle': 'We offer a comprehensive range of photography and visual production services for all types of events at the highest global quality standards.',
    'services.discover': 'Discover More',
    
    'portfolio.title': 'Our Past Works',
    'portfolio.subtitle': 'We are proud to share a part of our journey in documenting the most important events and occasions in the Kingdom.',
    'portfolio.watch': 'Watch Work',
    
    'faq.title': 'Common Questions',
    'faq.subtitle': 'Here are some answers to the most common questions about our services.',
    
    'contact.title': 'Contact Us Today',
    'contact.subtitle': 'We are here to answer your inquiries and help you cover your events in the best possible way.',

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

    'contact.whatsappText': 'Hello, I am very interested in your services. Please contact me.',
    'contact.alertSuccess': 'Changes saved successfully!',
    'process.stepsDesc': 'Simple steps that guarantee the best results',
    'partners.trustDesc': 'We are proud to work with top companies and government entities',
    'testimonials.trustDesc': 'We take pride in our clients trust and value their feedback',
    'contact.formDesc': 'We are here to answer your questions and help you cover your events in the best way possible.',

    'contact.submitBtn': 'Send Now',

    
    'partners.title': 'Success Partners',
    'partners.subtitle': 'We are proud to work with an elite group of companies and government entities.',
    
    'process.subtitle': 'A simple and organized process to ensure the best results for our clients.',
    
    'stats.title': 'Numbers Talk',
    'stats.desc': 'A proven track record of successes and achievements we are proud of.',
    'stats.events': 'Documented Events',
    'stats.years': 'Years Experience',
    'stats.clients': 'Client Satisfaction',
    'stats.hours': 'Hours of Filming',
    
    'testimonials.desc': 'Reviews from our clients and success partners.',
    
    'footer.rights': 'All rights reserved.',
    'footer.terms': 'Terms & Conditions',
    'footer.privacy': 'Privacy Policy',
    'footer.contact': 'Contact Us',
    'footer.desc': 'We offer the latest photography and production solutions for events in Saudi Arabia. Professional documentation, high-quality live streaming, and integrated visual production.',
    'footer.powered': 'Powered by',

    'footer.companyDesc': 'A Saudi company specialized in photography, videography, and live streaming services for events and conferences with the highest quality standards.',
    'footer.quickLinks': 'Quick Links',
    'footer.service1': 'Photography',
    'footer.service2': 'Videography',
    'footer.service3': 'Live Streaming',
    'footer.service4': 'Conference Coverage',
    'quote.title': 'Request a Quote',

    'error.name': 'Name is required',
    'error.email': 'Email is required',
    'error.emailInvalid': 'Please enter a valid email address',
    'error.phone': 'Phone number is required',
    'error.phoneInvalid': 'Number must start with 05 and contain 10 digits',
    'error.clientType': 'Please select a client type',
    'error.eventType': 'Please select an event type',

    'quote.subtitle': 'We are happy to hear from you. Please fill out the form below so we can serve you better.',
    'quote.name': 'Name',
    'quote.email': 'Email',
    'quote.phone': 'Phone Number (starts with 05)',
    'quote.clientType': 'Client Type',
    'quote.selectClientType': 'Select Client Type',
    'quote.eventType': 'Event Type',
    'quote.selectEventType': 'Select Event Type',
    'quote.submit': 'Submit via WhatsApp',
    'client.gov': 'Government Entity',
    'client.company': 'Company',
    'client.org': 'Organization',
    'client.individual': 'Individual',
    'event.exhibition': 'Exhibition',
    'event.festival': 'Festival',
    'event.conference': 'Conference',
    'event.events': 'Events',
    'event.corp': 'Corporate Events',
    'event.opening': 'Opening Ceremony',
    'event.national': 'National Event',
    'event.photography': 'Photography',
    'event.realestate': 'Real Estate',
    'event.ad': 'Advertisement',
    'event.wedding': 'Wedding',
    'event.personal': 'Personal Events',
    'event.other': 'Other',
  }
};

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export const LanguageProvider = ({ children }: { children: React.ReactNode }) => {
  const [language, setLanguageState] = useState<Language>('ar');

  useEffect(() => {
    const savedLang = localStorage.getItem('app_language') as Language;
    if (savedLang && (savedLang === 'ar' || savedLang === 'en')) {
      setLanguageState(savedLang);
      document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';
      document.documentElement.lang = savedLang;
    } else {
      document.documentElement.dir = 'rtl';
      document.documentElement.lang = 'ar';
    }
  }, []);

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem('app_language', lang);
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    document.documentElement.lang = lang;
  };

  const t = (key: string) => {
    return translations[language][key] || key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};
