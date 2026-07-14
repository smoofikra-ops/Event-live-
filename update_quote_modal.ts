import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const quoteModalCode = `
const QuoteModal = ({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) => {
  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData(e.target as HTMLFormElement);
    const data = Object.fromEntries(formData.entries());
    
    const message = \`*طلب عرض سعر جديد*
الاسم: \${data.name}
البريد: \${data.email}
الهاتف: \${data.phone}
نوع العميل: \${data.clientType}
نوع الفعالية: \${data.eventType}\`;

    const encodedMessage = encodeURIComponent(message);
    window.open(\`https://wa.me/966536753679?text=\${encodedMessage}\`, '_blank');
    onClose();
  };

  const clientTypes = [
    'جهة حكومية',
    'شركة',
    'مؤسسة',
    'فرد'
  ];

  const eventTypes = [
    'معرض',
    'مهرجان',
    'مؤتمر',
    'فعاليات',
    'مناسبات شركات',
    'حفل افتتاح',
    'مناسبة وطنية',
    'تصوير',
    'عقاري',
    'إعلان',
    'حفلة زواج',
    'مناسبات شخصية',
    'نوع آخر'
  ];

  return (
    <div className="fixed inset-0 z-[300] bg-black/80 flex items-center justify-center p-4">
      <motion.div 
        initial={{ opacity: 0, y: 50, scale: 0.9 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        exit={{ opacity: 0, y: 50, scale: 0.9 }}
        className="bg-[#111] border border-white/10 rounded-2xl p-6 w-full max-w-xl shadow-2xl relative overflow-y-auto max-h-[90vh]"
      >
        <button onClick={onClose} className="absolute top-4 right-4 text-white/50 hover:text-white transition-colors">
          <X className="w-6 h-6" />
        </button>
        <h3 className="text-2xl font-bold mb-6 text-amber-500">اطلب عرض سعر</h3>
        <form onSubmit={handleSubmit} className="space-y-4 text-right" dir="rtl">
          <div>
            <label className="block text-sm font-medium mb-1">الاسم</label>
            <input required name="name" type="text" className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-amber-500 transition-colors" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">البريد الإلكتروني</label>
            <input required name="email" type="email" className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-amber-500 transition-colors" dir="ltr" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">رقم الجوال</label>
            <input required name="phone" type="tel" className="w-full bg-white/5 border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-amber-500 transition-colors" dir="ltr" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">نوع العميل</label>
            <select required name="clientType" className="w-full bg-[#222] border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-amber-500 transition-colors">
              <option value="">اختر نوع العميل</option>
              {clientTypes.map((type, i) => <option key={i} value={type}>{type}</option>)}
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">نوع الفعالية</label>
            <select required name="eventType" className="w-full bg-[#222] border border-white/10 rounded-lg px-4 py-2 focus:outline-none focus:border-amber-500 transition-colors">
              <option value="">اختر نوع الفعالية</option>
              {eventTypes.map((type, i) => <option key={i} value={type}>{type}</option>)}
            </select>
          </div>
          <button type="submit" className="w-full py-3 mt-4 bg-gradient-to-r from-[#FF8A00] to-[#FFC300] text-black font-black rounded-lg hover:shadow-[0_0_20px_rgba(255,138,0,0.4)] transition-all">
            إرسال الطلب عبر واتساب
          </button>
        </form>
      </motion.div>
    </div>
  );
};
`;

if (appTsx.includes('export default function App() {')) {
  appTsx = appTsx.replace('export default function App() {', quoteModalCode + '\nexport default function App() {');
} else if (appTsx.includes('const App = () => {')) {
  appTsx = appTsx.replace('const App = () => {', quoteModalCode + '\nconst App = () => {');
}

// State in App
if (appTsx.includes('const [data, setData] = useState<AppData>(INITIAL_DATA);')) {
  appTsx = appTsx.replace('const [data, setData] = useState<AppData>(INITIAL_DATA);', 'const [data, setData] = useState<AppData>(INITIAL_DATA);\n  const [isQuoteOpen, setIsQuoteOpen] = useState(false);');
}

// Navbar button update
appTsx = appTsx.replace(
  'const Navbar = ({ onAdminClick, isAdminMode }: { onAdminClick: () => void, isAdminMode: boolean }) => {',
  'const Navbar = ({ onAdminClick, isAdminMode, onQuoteClick }: { onAdminClick: () => void, isAdminMode: boolean, onQuoteClick: () => void }) => {'
);
appTsx = appTsx.replace(
  '<a href="#contact" className="px-6 py-2.5 bg-gradient-to-r from-[#FF8A00] to-[#FFC300] text-black text-sm font-black rounded-full hover:shadow-[0_0_20px_rgba(255,138,0,0.4)] transition-all hover:scale-105 active:scale-95">\n            اطلب عرض سعر\n          </a>',
  '<button onClick={onQuoteClick} className="px-6 py-2.5 bg-gradient-to-r from-[#FF8A00] to-[#FFC300] text-black text-sm font-black rounded-full hover:shadow-[0_0_20px_rgba(255,138,0,0.4)] transition-all hover:scale-105 active:scale-95">\n            اطلب عرض سعر\n          </button>'
);
appTsx = appTsx.replace(
  '<Navbar onAdminClick={() => setIsAdminOpen(true)} isAdminMode={isAdminOpen} />',
  '<Navbar onAdminClick={() => setIsAdminOpen(true)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />'
);

// Hero button update
appTsx = appTsx.replace(
  'const Hero = ({ videoUrl }: { videoUrl?: string }) => {',
  'const Hero = ({ videoUrl, onQuoteClick }: { videoUrl?: string, onQuoteClick: () => void }) => {'
);
appTsx = appTsx.replace(
  'onClick={() => document.getElementById(\'contact\')?.scrollIntoView()}',
  'onClick={onQuoteClick}'
);
appTsx = appTsx.replace(
  '<Hero videoUrl={data.heroVideoUrl} />',
  '<Hero videoUrl={data.heroVideoUrl} onQuoteClick={() => setIsQuoteOpen(true)} />'
);

// Add QuoteModal to App return
appTsx = appTsx.replace(
  '<Navbar onAdminClick={() => setIsAdminOpen(true)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />',
  '<Navbar onAdminClick={() => setIsAdminOpen(true)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />\n      <AnimatePresence>{isQuoteOpen && <QuoteModal isOpen={isQuoteOpen} onClose={() => setIsQuoteOpen(false)} />}</AnimatePresence>'
);

fs.writeFileSync('src/App.tsx', appTsx);
console.log('App.tsx updated!');
