import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const processComponent = `
const Process = () => {
  const steps = [
    { num: "01", title: "الطلب والاستشارة", desc: "نتواصل معكم لفهم احتياجاتكم وتقديم الاستشارة المناسبة." },
    { num: "02", title: "التخطيط والتجهيز", desc: "نضع خطة عمل تفصيلية ونجهز المعدات اللازمة للفعالية." },
    { num: "03", title: "التصوير والتوثيق", desc: "نقوم بتغطية الحدث باحترافية عالية مع التركيز على أهم التفاصيل." },
    { num: "04", title: "المونتاج والتسليم", desc: "تتم معالجة المواد وإخراجها بصيغتها النهائية للتسليم." }
  ];

  return (
    <SectionWrapper id="process" className="bg-gray-50 dark:bg-[#050505] py-24">
      <div className="text-center mb-20">
        <ScrollReveal>
          <h2 className="text-[40px] font-semibold mb-8 title-accent-center heading-gradient">آلية <span className="text-gradient">العمل</span></h2>
          <p className="text-black/50 dark:text-white/50 max-w-[70ch] mx-auto text-[18px]">خطوات بسيطة تضمن لكم أفضل النتائج</p>
        </ScrollReveal>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-8 relative max-w-7xl mx-auto px-6">
        <div className="hidden md:block absolute top-12 left-[10%] right-[10%] h-[2px] bg-gradient-to-r from-transparent via-amber-500/30 to-transparent"></div>
        {steps.map((step, i) => (
          <ScrollReveal key={i} delay={i * 0.2}>
            <div className="relative z-10 flex flex-col items-center text-center group">
              <div className="w-24 h-24 rounded-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 flex items-center justify-center text-3xl font-black text-black/20 dark:text-white/20 group-hover:text-amber-500 group-hover:border-amber-500 transition-all duration-500 mb-6 shadow-xl">
                {step.num}
              </div>
              <h3 className="text-xl font-bold mb-4 text-black dark:text-white">{step.title}</h3>
              <p className="text-black/60 dark:text-white/60">{step.desc}</p>
            </div>
          </ScrollReveal>
        ))}
      </div>
    </SectionWrapper>
  );
};
`;

const partnersComponent = `
const Partners = () => {
  const partners = [
    { name: "شريك 1", logo: "https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=100&fit=crop&q=80" },
    { name: "شريك 2", logo: "https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=100&fit=crop&q=80" },
    { name: "شريك 3", logo: "https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=100&fit=crop&q=80" },
    { name: "شريك 4", logo: "https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=100&fit=crop&q=80" },
    { name: "شريك 5", logo: "https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=100&fit=crop&q=80" }
  ];

  return (
    <SectionWrapper id="partners" className="bg-white dark:bg-[#0a0a0a] py-20 overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 mb-12">
        <ScrollReveal>
          <h2 className="text-3xl font-bold text-center text-black dark:text-white mb-4">شركاء <span className="text-gradient">النجاح</span></h2>
          <p className="text-center text-black/50 dark:text-white/50">نفخر بالعمل مع نخبة من الشركات والجهات الحكومية</p>
        </ScrollReveal>
      </div>
      <div className="relative w-full overflow-hidden flex bg-black/5 dark:bg-white/5 py-10 border-y border-black/10 dark:border-white/10" dir="ltr">
        <div className="flex w-max animate-marquee">
          {[...partners, ...partners, ...partners].map((p, index) => (
            <div key={index} className="mx-8 w-40 h-20 opacity-50 hover:opacity-100 transition-opacity grayscale hover:grayscale-0 flex items-center justify-center">
              <img src={p.logo} alt={p.name} className="max-w-full max-h-full object-contain" />
            </div>
          ))}
        </div>
      </div>
    </SectionWrapper>
  );
};
`;

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
      className="glass-card p-8 rounded-2xl w-[350px] mx-4 relative overflow-hidden transition-all duration-300 hover:scale-105 hover:bg-black/5 dark:hover:bg-white/10 hover:border-amber-500/30 flex-shrink-0"
    >
      <Quote className="w-12 h-12 text-amber-500/10 absolute top-4 left-4" />
      <div className="flex gap-1 mb-6 text-amber-500">
        {[...Array(5)].map((_, i) => <Star key={i} className="w-4 h-4 fill-current" />)}
      </div>
      <p className="text-black/80 dark:text-white/80 leading-relaxed text-[15px] mb-8 min-h-[100px]">
        <TypewriterText text={testimonial.text} isHovered={isHovered} />
      </p>
      <div className="flex items-center gap-4 mt-auto">
        <div className="w-12 h-12 rounded-full bg-gradient-to-tr from-[#FF8A00] to-[#FFC300] p-[2px]">
          <div className="w-full h-full bg-white dark:bg-[#111] rounded-full flex items-center justify-center font-bold text-lg text-black dark:text-white">
            {testimonial.name.charAt(0)}
          </div>
        </div>
        <div>
          <h4 className="font-bold text-black dark:text-white">{testimonial.name}</h4>
          <p className="text-black/50 dark:text-white/50 text-sm">{testimonial.role}</p>
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
    <SectionWrapper id="testimonials" className="bg-gray-50 dark:bg-[#050505] py-24 overflow-hidden relative">
      <div className="max-w-7xl mx-auto px-6 mb-16 text-center">
        <ScrollReveal>
          <AnimatedTitle text="قالوا عنا" className="text-[40px] font-semibold title-accent-center heading-gradient mb-4" />
          <p className="text-black/50 dark:text-white/50 text-lg">نفخر بثقة عملائنا ونعتز بآرائهم</p>
        </ScrollReveal>
      </div>

      <div className="relative w-full overflow-hidden flex bg-black/5 dark:bg-white/5 py-10 border-y border-black/10 dark:border-white/10 group" dir="ltr">
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

const contactComponent = `
const Contact = () => {
  const [formData, setFormData] = useState({ name: '', email: '', phone: '', eventType: '', date: '', details: '' });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const validate = () => {
    const newErrors: Record<string, string> = {};
    if (!formData.name.trim()) newErrors.name = 'الاسم مطلوب';
    if (!formData.email.trim()) {
      newErrors.email = 'البريد الإلكتروني مطلوب';
    } else if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(formData.email)) {
      newErrors.email = 'بريد إلكتروني غير صالح';
    }
    if (!formData.phone.trim()) {
      newErrors.phone = 'رقم الهاتف مطلوب';
    }
    return newErrors;
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    if (errors[e.target.name]) {
      setErrors({ ...errors, [e.target.name]: '' });
    }
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const newErrors = validate();
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }
    setIsSubmitting(true);
    
    // Simulate API call
    setTimeout(() => {
      setIsSubmitting(false);
      setIsSuccess(true);
      setFormData({ name: '', email: '', phone: '', eventType: '', date: '', details: '' });
      setTimeout(() => setIsSuccess(false), 5000);
    }, 1500);
  };

  return (
    <SectionWrapper id="contact" className="bg-white dark:bg-[#0a0a0a] py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
          <ScrollReveal>
            <h2 className="text-[40px] font-semibold mb-8 title-accent heading-gradient">تواصل معنا <span className="text-gradient">اليوم</span></h2>
            <p className="text-black/60 dark:text-white/60 mb-12 text-lg">نحن هنا للإجابة على استفساراتكم ومساعدتكم في تغطية فعالياتكم بأفضل شكل ممكن.</p>
            
            <div className="space-y-8">
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-full bg-amber-500/10 flex items-center justify-center flex-shrink-0">
                  <Phone className="w-6 h-6 text-amber-500" />
                </div>
                <div>
                  <h4 className="font-bold text-black dark:text-white mb-1">رقم الهاتف</h4>
                  <p className="text-black/60 dark:text-white/60" dir="ltr">053 675 3679</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-full bg-amber-500/10 flex items-center justify-center flex-shrink-0">
                  <Mail className="w-6 h-6 text-amber-500" />
                </div>
                <div>
                  <h4 className="font-bold text-black dark:text-white mb-1">البريد الإلكتروني</h4>
                  <p className="text-black/60 dark:text-white/60">info@eventliveksa.com</p>
                </div>
              </div>
              <div className="flex items-start gap-4">
                <div className="w-12 h-12 rounded-full bg-amber-500/10 flex items-center justify-center flex-shrink-0">
                  <MapPin className="w-6 h-6 text-amber-500" />
                </div>
                <div>
                  <h4 className="font-bold text-black dark:text-white mb-1">الموقع</h4>
                  <p className="text-black/60 dark:text-white/60">الرياض، المملكة العربية السعودية</p>
                </div>
              </div>
            </div>
          </ScrollReveal>
          
          <ScrollReveal delay={0.2}>
            <form onSubmit={handleSubmit} className="glass-card p-8 rounded-3xl space-y-6 relative overflow-hidden">
              {isSuccess && (
                <div className="absolute inset-0 bg-green-500/10 backdrop-blur-sm z-10 flex flex-col items-center justify-center text-green-500 font-bold p-8 text-center rounded-3xl border border-green-500/20">
                  <CheckCircle className="w-16 h-16 mb-4" />
                  <p className="text-xl">تم إرسال رسالتك بنجاح!</p>
                  <p className="text-sm mt-2 opacity-80">سنتواصل معك في أقرب وقت ممكن.</p>
                </div>
              )}
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-bold text-black/80 dark:text-white/80 mb-2">الاسم</label>
                  <input name="name" value={formData.name} onChange={handleChange} className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.name ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} />
                  {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name}</p>}
                </div>
                <div>
                  <label className="block text-sm font-bold text-black/80 dark:text-white/80 mb-2">البريد الإلكتروني</label>
                  <input name="email" value={formData.email} onChange={handleChange} type="email" className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.email ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} dir="ltr" />
                  {errors.email && <p className="text-red-500 text-xs mt-1 text-right">{errors.email}</p>}
                </div>
              </div>
              <div>
                <label className="block text-sm font-bold text-black/80 dark:text-white/80 mb-2">رقم الجوال</label>
                <input name="phone" value={formData.phone} onChange={handleChange} type="tel" className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.phone ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} dir="ltr" />
                {errors.phone && <p className="text-red-500 text-xs mt-1 text-right">{errors.phone}</p>}
              </div>
              <div>
                <label className="block text-sm font-bold text-black/80 dark:text-white/80 mb-2">الرسالة أو التفاصيل</label>
                <textarea name="details" value={formData.details} onChange={handleChange} rows={4} className="w-full bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors resize-none"></textarea>
              </div>
              <button disabled={isSubmitting} type="submit" className="w-full py-4 bg-amber-500 text-black font-bold text-lg rounded-xl hover:bg-amber-400 transition-colors flex items-center justify-center gap-2">
                {isSubmitting ? <span className="animate-spin w-5 h-5 border-2 border-black border-t-transparent rounded-full"></span> : 'إرسال الرسالة'}
              </button>
            </form>
          </ScrollReveal>
        </div>
      </div>
    </SectionWrapper>
  );
};
`;

const footerComponent = `
const Footer = ({ socialLinks }: { socialLinks: SocialLink[] }) => {
  return (
    <footer className="bg-gray-100 dark:bg-[#020202] border-t border-black/5 dark:border-white/5 pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          <div>
            <a href="#home" className="text-2xl font-black tracking-tighter text-amber-500 flex items-center gap-2 mb-6">
              <Camera className="w-6 h-6" />
              <span className="text-gradient">EventLive</span>
            </a>
            <p className="text-black/60 dark:text-white/60 mb-6 leading-relaxed">
              شركة سعودية متخصصة في خدمات التصوير الفوتوغرافي والفيديو والبث المباشر للفعاليات والمؤتمرات بأعلى معايير الجودة.
            </p>
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">روابط سريعة</h4>
            <ul className="space-y-4">
              <li><a href="#home" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">الرئيسية</a></li>
              <li><a href="#services" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">الخدمات</a></li>
              <li><a href="#portfolio" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">أعمالنا</a></li>
              <li><a href="#faq" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">الأسئلة الشائعة</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">خدماتنا</h4>
            <ul className="space-y-4">
              <li><a href="#" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">التصوير الفوتوغرافي</a></li>
              <li><a href="#" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">تصوير الفيديو</a></li>
              <li><a href="#" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">البث المباشر</a></li>
              <li><a href="#" className="text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">تغطية المؤتمرات</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-bold text-lg mb-6 text-black dark:text-white">تواصل معنا</h4>
            <div className="flex gap-4">
              {socialLinks.map((link, i) => {
                if (!link.url || link.url === '#') return null;
                const IconMapLocal: Record<string, any> = {
                  twitter: Twitter,
                  instagram: Instagram,
                  linkedin: Linkedin,
                  youtube: Youtube,
                  facebook: Facebook,
                  tiktok: Music2,
                  website: Globe
                };
                const Icon = IconMapLocal[link.platform] || Globe;
                return (
                  <a key={i} href={link.url} target="_blank" rel="noopener noreferrer" className="w-10 h-10 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-black/60 dark:text-white/60 hover:bg-amber-500 hover:text-black transition-all">
                    <Icon className="w-5 h-5" />
                  </a>
                );
              })}
            </div>
          </div>
        </div>
        <div className="border-t border-black/5 dark:border-white/5 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-black/40 dark:text-white/40">
          <p>© {new Date().getFullYear()} EventLive KSA. جميع الحقوق محفوظة.</p>
          <div className="flex gap-4">
            <a href="#" className="hover:text-amber-500 transition-colors">الشروط والأحكام</a>
            <a href="#" className="hover:text-amber-500 transition-colors">سياسة الخصوصية</a>
          </div>
        </div>
      </div>
    </footer>
  );
};
`;

const adminPanelComponent = `
const AdminPanel = ({ data, onSave, onClose }: { data: AppData, onSave: (data: AppData) => void, onClose: () => void }) => {
  const [localData, setLocalData] = useState<AppData>(data);
  const [activeTab, setActiveTab] = useState('services');

  const handleUpdateServiceIcon = (id: string, iconName: string) => {
    setLocalData({
      ...localData,
      services: localData.services.map(s => s.id === id ? { ...s, iconName } : s)
    });
  };

  const handleUpdateServiceMedia = (id: string, type: 'icon' | 'image' | 'video' | 'url', value: string) => {
    setLocalData({
      ...localData,
      services: localData.services.map(s => s.id === id ? { ...s, mediaType: type, mediaValue: value } : s)
    });
  };

  const handleUpdateSocial = (platform: string, url: string) => {
    setLocalData({
      ...localData,
      socialLinks: localData.socialLinks.map(s => s.platform === platform ? { ...s, url } : s)
    });
  };

  const handleAddWork = () => {
    const newWork: Work = {
      id: Date.now().toString(),
      title: 'عمل جديد',
      img: 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=800'
    };
    setLocalData({ ...localData, works: [newWork, ...localData.works] });
  };

  const handleRemoveWork = (id: string) => {
    setLocalData({ ...localData, works: localData.works.filter(w => w.id !== id) });
  };

  const handleUpdateWork = (id: string, field: keyof Work, value: string) => {
    setLocalData({
      ...localData,
      works: localData.works.map(w => w.id === id ? { ...w, [field]: value } : w)
    });
  };

  return (
    <div className="fixed inset-0 z-[500] bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white dark:bg-[#111] rounded-2xl w-full max-w-4xl h-[80vh] flex flex-col shadow-2xl overflow-hidden border border-black/10 dark:border-white/10">
        <div className="p-6 border-b border-black/10 dark:border-white/10 flex items-center justify-between bg-gray-50 dark:bg-[#0a0a0a]">
          <h2 className="text-2xl font-bold flex items-center gap-2 text-black dark:text-white"><Settings className="w-6 h-6" /> لوحة التحكم</h2>
          <div className="flex gap-4">
            <button onClick={() => onSave(localData)} className="px-6 py-2 bg-amber-500 text-black font-bold rounded-lg hover:bg-amber-400 transition-colors">حفظ التغييرات</button>
            <button onClick={onClose} className="p-2 text-black/50 dark:text-white/50 hover:text-black dark:hover:text-white bg-black/5 dark:bg-white/5 rounded-lg"><X className="w-5 h-5" /></button>
          </div>
        </div>
        
        <div className="flex flex-1 overflow-hidden">
          <div className="w-64 bg-gray-50 dark:bg-[#0a0a0a] border-l border-black/10 dark:border-white/10 p-4 flex flex-col gap-2 overflow-y-auto">
            {['services', 'portfolio', 'social', 'hero'].map(tab => (
              <button key={tab} onClick={() => setActiveTab(tab)} className={\`text-right px-4 py-3 rounded-lg font-bold transition-colors \${activeTab === tab ? 'bg-amber-500 text-black' : 'text-black/60 dark:text-white/60 hover:bg-black/5 dark:hover:bg-white/5'}\`}>
                {tab === 'services' && 'الخدمات'}
                {tab === 'portfolio' && 'الأعمال'}
                {tab === 'social' && 'التواصل الاجتماعي'}
                {tab === 'hero' && 'الرئيسية'}
              </button>
            ))}
          </div>
          
          <div className="flex-1 p-6 overflow-y-auto bg-white dark:bg-[#111]">
            {activeTab === 'hero' && (
              <div className="space-y-6">
                <h3 className="text-xl font-bold mb-4 text-black dark:text-white">إعدادات القسم الرئيسي</h3>
                <div>
                  <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">رابط فيديو الخلفية (YouTube)</label>
                  <input type="text" value={localData.heroVideoUrl || ''} onChange={(e) => setLocalData({...localData, heroVideoUrl: e.target.value})} className="w-full bg-black/5 dark:bg-[#222] border border-black/10 dark:border-white/10 rounded-lg px-4 py-3" dir="ltr" placeholder="https://www.youtube.com/watch?v=..." />
                </div>
              </div>
            )}
            
            {activeTab === 'services' && (
              <div className="space-y-8">
                {localData.services.map(service => (
                  <div key={service.id} className="p-6 bg-gray-50 dark:bg-[#222] rounded-xl border border-black/5 dark:border-white/5 space-y-4">
                    <input type="text" value={service.title} onChange={(e) => setLocalData({...localData, services: localData.services.map(s => s.id === service.id ? {...s, title: e.target.value} : s)})} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-4 py-2 font-bold text-lg" />
                    <textarea value={service.desc} onChange={(e) => setLocalData({...localData, services: localData.services.map(s => s.id === service.id ? {...s, desc: e.target.value} : s)})} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-4 py-2 text-sm" rows={2} />
                    
                    <div className="flex gap-4">
                      <select value={service.mediaType || 'icon'} onChange={(e) => handleUpdateServiceMedia(service.id, e.target.value as any, service.mediaValue || '')} className="bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-4 py-2 text-sm">
                        <option value="icon">أيقونة</option>
                        <option value="image">صورة</option>
                        <option value="video">فيديو</option>
                      </select>
                      {service.mediaType !== 'icon' && (
                        <input type="text" value={service.mediaValue || ''} onChange={(e) => handleUpdateServiceMedia(service.id, service.mediaType as any, e.target.value)} placeholder={service.mediaType === 'image' ? 'رابط الصورة' : 'رابط الفيديو (يوتيوب أو مباشر)'} className="flex-1 bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-4 py-2 text-sm" dir="ltr" />
                      )}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {activeTab === 'portfolio' && (
              <div className="space-y-6">
                <button onClick={handleAddWork} className="w-full py-4 border-2 border-dashed border-amber-500/50 text-amber-500 rounded-xl hover:bg-amber-500/10 transition-colors flex items-center justify-center gap-2 font-bold">
                  <Plus className="w-5 h-5" /> إضافة عمل جديد
                </button>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {localData.works.map(work => (
                    <div key={work.id} className="p-4 bg-gray-50 dark:bg-[#222] rounded-xl border border-black/5 dark:border-white/5 relative group">
                      <button onClick={() => handleRemoveWork(work.id)} className="absolute top-2 left-2 p-2 bg-red-500/10 text-red-500 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity">
                        <Trash2 className="w-4 h-4" />
                      </button>
                      <input type="text" value={work.title} onChange={(e) => handleUpdateWork(work.id, 'title', e.target.value)} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-3 py-2 mb-2 font-bold" />
                      <input type="text" value={work.img} onChange={(e) => handleUpdateWork(work.id, 'img', e.target.value)} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-3 py-2 text-sm mb-2" placeholder="رابط الصورة" dir="ltr" />
                      <input type="text" value={work.videoUrl || ''} onChange={(e) => handleUpdateWork(work.id, 'videoUrl', e.target.value)} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-3 py-2 text-sm" placeholder="رابط الفيديو (يوتيوب)" dir="ltr" />
                      <input type="text" value={work.category || ''} onChange={(e) => handleUpdateWork(work.id, 'category', e.target.value)} className="w-full bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-3 py-2 text-sm mt-2" placeholder="التصنيف (مثال: تصوير)" />
                    </div>
                  ))}
                </div>
              </div>
            )}

            {activeTab === 'social' && (
              <div className="space-y-4">
                {localData.socialLinks.map(link => (
                  <div key={link.platform} className="flex items-center gap-4 bg-gray-50 dark:bg-[#222] p-4 rounded-xl border border-black/5 dark:border-white/5">
                    <div className="w-24 capitalize font-bold text-black/50 dark:text-white/50">{link.platform}</div>
                    <input type="text" value={link.url} onChange={(e) => handleUpdateSocial(link.platform, e.target.value)} className="flex-1 bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-lg px-4 py-2" dir="ltr" placeholder="https://..." />
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
`;

const injection = `
${processComponent}

${partnersComponent}

${typewriterComponent}

${testimonialsComponent}

${contactComponent}

${footerComponent}

${adminPanelComponent}
`;

if (!appTsx.includes('const Process =')) {
  appTsx = appTsx.replace(/<\/SectionWrapper>\s*\);\s*\};\s*(?=const ScrollProgress = \(\))/, '</SectionWrapper>\n  );\n};\n\n' + injection);
  appTsx = appTsx.replace('<FAQ />', '<FAQ />\n        <Process />\n        <Partners />\n        <Testimonials />\n        <Contact />');
  
  if (!appTsx.includes('<Footer')) {
    appTsx = appTsx.replace('</main>', '</main>\n      <Footer socialLinks={data.socialLinks} />\n      <AnimatePresence>\n        {isAdminOpen && <AdminPanel data={data} onSave={handleSaveData} onClose={() => setIsAdminOpen(false)} />}\n      </AnimatePresence>');
  }
}

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Restored to App.tsx');
