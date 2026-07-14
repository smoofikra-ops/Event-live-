import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const typewriterComponent = `
const TypewriterText = ({ text, isHovered }: { text: string, isHovered: boolean }) => {
  const [displayedText, setDisplayedText] = useState(text);
  
  useEffect(() => {
    if (isHovered) {
      setDisplayedText('');
      let i = 0;
      const interval = setInterval(() => {
        setDisplayedText(text.substring(0, i + 1));
        i++;
        if (i >= text.length) clearInterval(interval);
      }, 30);
      return () => clearInterval(interval);
    } else {
      setDisplayedText(text);
    }
  }, [isHovered, text]);

  return <span>{displayedText}{isHovered && displayedText.length < text.length && <span className="animate-pulse">|</span>}</span>;
};

const TestimonialCard = ({ testimonial }: { testimonial: any }) => {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div 
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="glass-card p-8 rounded-2xl w-[350px] mx-4 relative overflow-hidden transition-all duration-300 hover:scale-105 hover:bg-white/10 hover:border-amber-500/30 flex-shrink-0"
    >
      <Quote className="w-12 h-12 text-amber-500/10 absolute top-4 left-4" />
      <div className="flex gap-1 mb-6 text-amber-500">
        {[...Array(5)].map((_, i) => <Star key={i} className="w-4 h-4 fill-current" />)}
      </div>
      <p className="text-white/80 leading-relaxed text-[15px] mb-8 min-h-[100px]">
        <TypewriterText text={testimonial.text} isHovered={isHovered} />
      </p>
      <div className="flex items-center gap-4 mt-auto">
        <div className="w-12 h-12 rounded-full bg-gradient-to-tr from-[#FF8A00] to-[#FFC300] p-[2px]">
          <div className="w-full h-full bg-[#111] rounded-full flex items-center justify-center font-bold text-lg">
            {testimonial.name.charAt(0)}
          </div>
        </div>
        <div>
          <h4 className="font-bold">{testimonial.name}</h4>
          <p className="text-white/50 text-sm">{testimonial.role}</p>
        </div>
      </div>
    </div>
  );
};
`;

const testimonialsComponent = `
const Testimonials = () => {
  const testimonials = [
    { name: "أحمد محمد", role: "مدير فعاليات", text: "تجربة رائعة مع فريق EventLive. الاحترافية في التعامل وجودة التصوير كانت تفوق التوقعات. شكراً لكم على توثيق فعاليتنا بأجمل صورة." },
    { name: "سارة العتيبي", role: "منظمة مؤتمرات", text: "فريق مبدع ومحترف جداً. التغطية كانت شاملة لكل تفاصيل المؤتمر، والمونتاج النهائي كان مذهلاً." },
    { name: "عبدالله السالم", role: "صاحب شركة", text: "من أفضل الشركات اللي تعاملنا معاها في مجال التغطية الإعلامية. التزام بالوقت وجودة في المخرجات لا يُعلى عليها." },
    { name: "نورة الخالد", role: "مديرة علاقات عامة", text: "خدماتهم في البث المباشر كانت استثنائية. الجودة عالية ولم نواجه أي مشاكل تقنية خلال الحدث بأكمله." },
    { name: "فهد العبدالله", role: "مؤسس مؤسسة", text: "أشكركم على التغطية المميزة لحفل الافتتاح. الفريق كان متعاوناً جداً وقدموا لنا أفكاراً إبداعية أضافت قيمة للحدث." }
  ];

  return (
    <SectionWrapper id="testimonials" className="bg-[#050505] py-24 overflow-hidden relative">
      <div className="max-w-7xl mx-auto px-6 mb-16 text-center">
        <ScrollReveal>
          <AnimatedTitle text="قالوا عنا" className="text-[40px] font-semibold title-accent-center heading-gradient mb-4" />
          <p className="text-white/50 text-lg">نفخر بثقة عملائنا ونعتز بآرائهم</p>
        </ScrollReveal>
      </div>

      <div className="relative w-full overflow-hidden flex bg-white/5 py-10 border-y border-white/10 group" dir="ltr">
        <div className="flex w-max animate-marquee group-hover:[animation-play-state:paused]">
          {[...testimonials, ...testimonials, ...testimonials].map((t, index) => (
            <TestimonialCard key={index} testimonial={t} />
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
};
`;

appTsx = appTsx.replace(/const Testimonials = \(\) => {[\s\S]*?(?=const Contact = \(\) => {)/, typewriterComponent + '\n' + testimonialsComponent + '\n');

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Testimonials updated!');
