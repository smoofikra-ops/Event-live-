import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldPartners = `const Partners = ({ partners = [] }: { partners?: Partner[] }) => {
  const { t, language } = useLanguage();
  if (!partners || partners.length === 0) return null;`;

const newPartners = `const Partners = ({ partners = [] }: { partners?: Partner[] }) => {
  const { t, language } = useLanguage();
  const [isHovered, setIsHovered] = useState(false);
  const [justLeft, setJustLeft] = useState(false);
  if (!partners || partners.length === 0) return null;`;

code = code.replace(oldPartners, newPartners);

const oldPartnersDiv = `<div className="relative w-full overflow-hidden flex bg-transparent py-12 group" dir="ltr">
        {/* Animated gradient fade at the edges for smoothness */}
        <div className="absolute left-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-r from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        <div className="absolute right-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-l from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        
        <div className="flex w-max animate-marquee group-hover:[animation-play-state:paused] py-4">
          {[...partners, ...partners, ...partners].map((p, index) => (
            <div 
              key={index} 
              className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-[#111] shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_20px_40px_rgba(255,138,0,0.15)] hover:-translate-y-2 overflow-hidden"
            >`;

const newPartnersDiv = `<div 
        className="relative w-full overflow-hidden flex bg-transparent py-12" 
        dir="ltr"
        onMouseEnter={() => {
          setIsHovered(true);
          setJustLeft(false);
        }}
        onMouseLeave={() => {
          setIsHovered(false);
          setJustLeft(true);
          setTimeout(() => setJustLeft(false), 500);
        }}
      >
        {/* Animated gradient fade at the edges for smoothness */}
        <div className="absolute left-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-r from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        <div className="absolute right-0 top-0 bottom-0 w-24 sm:w-48 bg-gradient-to-l from-white dark:from-[#0a0a0a] to-transparent z-10 pointer-events-none"></div>
        
        <div className={\`transition-transform duration-700 ease-in-out \${justLeft ? 'translate-x-8' : 'translate-x-0'}\`}>
          <div className={\`flex w-max \${isHovered ? '[animation-play-state:paused]' : '[animation-play-state:running]'} animate-marquee-slow py-4\`}>
            {[...partners, ...partners, ...partners].map((p, index) => (
              <div 
                key={index} 
                className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-[#111] shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_30px_50px_rgba(255,138,0,0.2)] hover:scale-110 hover:-translate-y-4 hover:z-50 overflow-hidden"
              >`;

code = code.replace(oldPartnersDiv, newPartnersDiv);
fs.writeFileSync('src/App.tsx', code);
