import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const quoteModalComponent = `
const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    clientType: '',
    eventType: ''
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  if (!isOpen) return null;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    if (errors[e.target.name]) {
      setErrors({ ...errors, [e.target.name]: '' });
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const newErrors: Record<string, string> = {};
    
    if (!formData.name.trim()) newErrors.name = 'الاسم مطلوب';
    if (!formData.email.trim()) {
      newErrors.email = 'البريد الإلكتروني مطلوب';
    } else if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(formData.email)) {
      newErrors.email = 'يرجى إدخال بريد إلكتروني صحيح';
    }
    
    if (!formData.phone.trim()) {
      newErrors.phone = 'رقم الهاتف مطلوب';
    } else if (!/^05\\d{8}$/.test(formData.phone)) {
      newErrors.phone = 'يجب أن يبدأ الرقم بـ 05 ويتكون من 10 أرقام';
    }
    
    if (!formData.clientType) newErrors.clientType = 'يرجى اختيار نوع العميل';
    if (!formData.eventType) newErrors.eventType = 'يرجى اختيار نوع الفعالية';

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    const message = \`*طلب عرض سعر جديد*\\nالاسم: \${formData.name}\\nالبريد: \${formData.email}\\nالهاتف: \${formData.phone}\\nنوع العميل: \${formData.clientType}\\nنوع الفعالية: \${formData.eventType}\`;

    const encodedMessage = encodeURIComponent(message);
    window.open(\`https://wa.me/966536753679?text=\${encodedMessage}\`, '_blank');
    onClose();
  };

  const clientTypes = ['جهة حكومية', 'شركة', 'مؤسسة', 'فرد'];
  const eventTypes = ['معرض', 'مهرجان', 'مؤتمر', 'فعاليات', 'مناسبات شركات', 'حفل افتتاح', 'مناسبة وطنية', 'تصوير', 'عقاري', 'إعلان', 'حفلة زواج', 'مناسبات شخصية', 'نوع آخر'];

  return (
    <div className="fixed inset-0 z-[300] bg-black/80 flex items-center justify-center p-4">
      <motion.div 
        initial={{ opacity: 0, y: 50, scale: 0.9 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        exit={{ opacity: 0, y: 50, scale: 0.9 }}
        className="bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-2xl p-8 w-full max-w-xl shadow-2xl relative overflow-y-auto max-h-[90vh]"
      >
        <button onClick={onClose} className="absolute top-6 right-6 text-black/50 dark:text-white/50 hover:text-amber-500 transition-colors bg-black/5 dark:bg-white/5 p-2 rounded-full">
          <X className="w-5 h-5" />
        </button>
        <h2 className="text-3xl font-black mb-2 text-black dark:text-white">طلب عرض سعر</h2>
        <p className="text-black/60 dark:text-white/60 mb-8">يسعدنا تواصلكم معنا. يرجى تعبئة النموذج التالي لنتمكن من خدمتكم بشكل أفضل.</p>
        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">الاسم</label>
              <input name="name" value={formData.name} onChange={handleChange} type="text" className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.name ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} />
              {errors.name && <p className="text-red-500 text-xs mt-1">{errors.name}</p>}
            </div>
            <div>
              <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">البريد الإلكتروني</label>
              <input name="email" value={formData.email} onChange={handleChange} type="email" className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.email ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} dir="ltr" />
              {errors.email && <p className="text-red-500 text-xs mt-1 text-right">{errors.email}</p>}
            </div>
          </div>
          <div>
            <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">رقم الجوال (يبدأ بـ 05)</label>
            <input name="phone" value={formData.phone} onChange={handleChange} type="tel" placeholder="05xxxxxxxx" className={\`w-full bg-black/5 dark:bg-white/5 border \${errors.phone ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`} dir="ltr" />
            {errors.phone && <p className="text-red-500 text-xs mt-1 text-right">{errors.phone}</p>}
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">نوع العميل</label>
              <div className="relative">
                <select name="clientType" value={formData.clientType} onChange={handleChange} className={\`w-full appearance-none bg-black/5 dark:bg-[#222] border \${errors.clientType ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`}>
                  <option value="" className="text-black/50 dark:text-white/50 bg-white dark:bg-[#222]">اختر نوع العميل</option>
                  {clientTypes.map((type, i) => <option key={i} value={type} className="bg-white dark:bg-[#222] text-black dark:text-white">{type}</option>)}
                </select>
                <ChevronDown className="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-black/50 dark:text-white/50 pointer-events-none" />
              </div>
              {errors.clientType && <p className="text-red-500 text-xs mt-1">{errors.clientType}</p>}
            </div>
            <div>
              <label className="block text-sm font-bold mb-2 text-black/80 dark:text-white/80">نوع الفعالية</label>
              <div className="relative">
                <select name="eventType" value={formData.eventType} onChange={handleChange} className={\`w-full appearance-none bg-black/5 dark:bg-[#222] border \${errors.eventType ? 'border-red-500' : 'border-black/10 dark:border-white/10'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors\`}>
                  <option value="" className="text-black/50 dark:text-white/50 bg-white dark:bg-[#222]">اختر نوع الفعالية</option>
                  {eventTypes.map((type, i) => <option key={i} value={type} className="bg-white dark:bg-[#222] text-black dark:text-white">{type}</option>)}
                </select>
                <ChevronDown className="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-black/50 dark:text-white/50 pointer-events-none" />
              </div>
              {errors.eventType && <p className="text-red-500 text-xs mt-1">{errors.eventType}</p>}
            </div>
          </div>
          <button type="submit" className="w-full py-4 mt-6 bg-amber-500 text-black font-bold text-lg rounded-xl hover:shadow-[0_0_30px_rgba(255,138,0,0.4)] hover:bg-amber-400 transition-all flex items-center justify-center gap-2">
            إرسال الطلب عبر واتساب
          </button>
        </form>
      </motion.div>
    </div>
  );
};
`;

appTsx = appTsx.replace(/const QuoteModal = \(\{ isOpen, onClose \}[\s\S]*?(?=export default function App\(\) \{)/, quoteModalComponent + '\n\n');

if (!appTsx.includes('ChevronDown')) {
  appTsx = appTsx.replace('import { ', 'import { ChevronDown, ');
}

fs.writeFileSync('src/App.tsx', appTsx);
console.log('QuoteModal updated!');
