import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const faqComponent = `
const FAQ = () => {
  const [openIndex, setOpenIndex] = useState<number | null>(0);
  const faqs = [
    { q: "ما هي مناطق الخدمة التي تغطونها؟", a: "نحن نغطي جميع مناطق المملكة العربية السعودية، ولدينا فرق جاهزة للتنقل لأي مدينة لتوثيق فعاليتكم بأعلى احترافية." },
    { q: "كم يستغرق تسليم العمل النهائي؟", a: "يعتمد ذلك على حجم الفعالية، ولكن عادة ما يتم تسليم الصور خلال 48 ساعة، والفيديو المونتاج خلال 5-7 أيام عمل كحد أقصى لضمان الجودة." },
    { q: "هل توفرون خدمة البث المباشر للفعاليات الكبرى؟", a: "نعم، نوفر خدمات البث المباشر باحترافية عالية وبأحدث أجهزة البث لمنصات التواصل الاجتماعي أو المواقع الخاصة بجودة 4K مع تغطية متعددة الكاميرات." },
    { q: "كيف يمكنني حجز موعد لفعاليتي أو طلب تسعيرة؟", a: "يمكنكم النقر على زر 'اطلب عرض سعر' وتعبئة النموذج، وسيتم تحويلكم مباشرة للتواصل مع فريق المبيعات عبر الواتساب لتحديد الموعد ومناقشة كافة التفاصيل." },
    { q: "هل لديكم تصاريح رسمية للتصوير بالدرون؟", a: "بالتأكيد، نحن جهة مرخصة ولدينا كافة التصاريح اللازمة للطيران والتصوير الجوي (درون) لضمان تغطية قانونية وآمنة للفعاليات." }
  ];

  return (
    <SectionWrapper id="faq" className="bg-[#0a0a0a]">
      <script type="application/ld+json" dangerouslySetInnerHTML={{__html: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faqs.map(faq => ({
          "@type": "Question",
          "name": faq.q,
          "acceptedAnswer": {
            "@type": "Answer",
            "text": faq.a
          }
        }))
      })}} />
      <div className="text-center mb-16">
        <ScrollReveal>
          <AnimatedTitle text="الأسئلة الشائعة" className="text-[40px] font-semibold mb-6 title-accent-center heading-gradient" />
          <p className="text-white/50 max-w-[70ch] mx-auto text-[18px] font-normal">إليك بعض الإجابات على التساؤلات الأكثر شيوعاً حول خدماتنا.</p>
        </ScrollReveal>
      </div>

      <div className="max-w-3xl mx-auto space-y-4 relative z-10">
        {faqs.map((faq, index) => (
          <ScrollReveal key={index} delay={index * 0.1}>
            <div 
              className={\`glass-card rounded-2xl overflow-hidden transition-all duration-300 border \${openIndex === index ? 'border-amber-500/50 bg-white/10' : 'border-white/10 hover:border-white/20'}\`}
            >
              <button
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
                className="w-full px-6 py-5 flex items-center justify-between text-right"
              >
                <h3 className={\`text-lg font-bold transition-colors \${openIndex === index ? 'text-amber-500' : 'text-white'}\`}>
                  {faq.q}
                </h3>
                <div className={\`w-8 h-8 rounded-full flex items-center justify-center transition-all duration-300 \${openIndex === index ? 'bg-amber-500 text-black rotate-180' : 'bg-white/10 text-white/50'}\`}>
                  <ChevronLeft className="w-5 h-5 -rotate-90" />
                </div>
              </button>
              <AnimatePresence>
                {openIndex === index && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                  >
                    <div className="px-6 pb-6 pt-0 text-white/70 leading-relaxed text-[15px]">
                      {faq.a}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </ScrollReveal>
        ))}
      </div>
    </SectionWrapper>
  );
};
`;

appTsx = appTsx.replace(/const FAQ = \(\) => {[\s\S]*?(?=const Process = \(\) => {)/, faqComponent + '\n');

fs.writeFileSync('src/App.tsx', appTsx);
console.log('FAQ updated!');
