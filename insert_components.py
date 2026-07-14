import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

camera_frame = """
const CameraFrameOverlay = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds(s => s + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const formatTime = (totalSeconds: number) => {
    const h = Math.floor(totalSeconds / 3600);
    const m = Math.floor((totalSeconds % 3600) / 60);
    const s = totalSeconds % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  return (
    <div className="absolute inset-0 pointer-events-none z-[60] p-4 md:p-8 flex flex-col justify-between" dir="ltr">
      {/* Corner Brackets */}
      <div className="absolute top-4 left-4 w-12 h-12 md:w-20 md:h-20 border-t-2 border-l-2 border-white/50"></div>
      <div className="absolute top-4 right-4 w-12 h-12 md:w-20 md:h-20 border-t-2 border-r-2 border-white/50"></div>
      <div className="absolute bottom-4 left-4 w-12 h-12 md:w-20 md:h-20 border-b-2 border-l-2 border-white/50"></div>
      <div className="absolute bottom-4 right-4 w-12 h-12 md:w-20 md:h-20 border-b-2 border-r-2 border-white/50"></div>

      {/* Top Bar */}
      <div className="flex justify-between items-start w-full">
        <div className="flex flex-col gap-2">
          <div className="flex items-center gap-3 bg-black/40 backdrop-blur-sm border border-white/10 px-3 md:px-4 py-1.5 md:py-2 rounded-full shadow-[0_0_15px_rgba(0,0,0,0.5)]">
            <span className="w-3 h-3 md:w-4 md:h-4 bg-red-600 rounded-full animate-pulse shadow-[0_0_15px_rgba(220,38,38,1)]"></span>
            <span className="text-white text-xs md:text-sm font-black tracking-widest uppercase">REC</span>
            <span className="text-white/80 text-xs md:text-sm font-mono ml-2 border-l border-white/20 pl-2 md:pl-3">{formatTime(seconds)}</span>
          </div>
          <div className="flex items-center gap-2 text-white/70 text-[10px] md:text-xs font-mono bg-black/20 backdrop-blur-sm px-2 py-1 rounded w-fit">
            <span>4K 60FPS</span>
            <span>•</span>
            <span>RAW</span>
          </div>
        </div>
        
        <div className="flex flex-col items-end gap-2 text-white/80 font-mono text-[10px] md:text-xs bg-black/20 backdrop-blur-sm px-2 py-1 rounded">
          <div className="flex items-center gap-2"><span>ISO</span> <span className="font-bold text-white">800</span></div>
          <div className="flex items-center gap-2"><span>F</span> <span className="font-bold text-white">2.8</span></div>
          <div className="flex items-center gap-2"><span>SHUTTER</span> <span className="font-bold text-white">1/120</span></div>
          <div className="flex items-center gap-2"><span>AWB</span> <span className="font-bold text-white">5600K</span></div>
        </div>
      </div>

      {/* Center Reticle */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex items-center justify-center opacity-30">
        <div className="w-[100px] h-[100px] md:w-[200px] md:h-[200px] border border-white/50 rounded-full relative">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-2 h-2 bg-white/80 rounded-full"></div>
          <div className="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 border-l border-white/30"></div>
          <div className="absolute left-0 right-0 top-1/2 -translate-y-1/2 border-t border-white/30"></div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="flex justify-between items-end w-full">
        <div className="flex items-end gap-2 bg-black/20 backdrop-blur-sm px-2 py-1 rounded">
          <div className="h-2 md:h-3 w-1 bg-green-500"></div>
          <div className="h-3 md:h-4 w-1 bg-green-500"></div>
          <div className="h-4 md:h-5 w-1 bg-green-400"></div>
          <div className="h-5 md:h-6 w-1 bg-yellow-400"></div>
          <div className="h-4 md:h-5 w-1 bg-white/20"></div>
          <div className="h-3 md:h-4 w-1 bg-white/20"></div>
          <div className="h-2 md:h-3 w-1 bg-white/20"></div>
          <span className="text-white/70 text-[8px] md:text-[10px] font-mono ml-2">CH1</span>
        </div>
        <div className="flex items-center gap-4 text-white/70 text-[10px] md:text-xs font-mono bg-black/20 backdrop-blur-sm px-2 py-1 rounded">
          <span>SD1 [1H 24M]</span>
          <div className="flex gap-1">
            <div className="w-4 h-2 border border-white/50 rounded-sm"></div>
            <div className="w-4 h-2 border border-white/50 rounded-sm bg-white/50"></div>
          </div>
          <span>BATT 78%</span>
        </div>
      </div>
    </div>
  );
};

const AnnouncementBanner = () => {
  const { t, language } = useLanguage();
  return (
    <div className="fixed top-0 left-0 right-0 h-10 bg-gradient-to-r from-amber-500 to-[#FFC300] text-black flex items-center overflow-hidden z-[110] border-b border-black/10 shadow-md">
      <div className="flex animate-marquee whitespace-nowrap min-w-full" dir="ltr">
        {Array.from({ length: 4 }).map((_, i) => (
          <div key={i} className={`flex items-center gap-8 px-4 ${language === 'ar' ? 'flex-row-reverse' : ''}`}>
            <span className="font-bold flex items-center gap-2"><Star className="w-4 h-4" /> {t('banner.1')}</span>
            <span className="font-bold flex items-center gap-2"><Building2 className="w-4 h-4" /> {t('banner.2')}</span>
            <span className="font-bold flex items-center gap-2"><Video className="w-4 h-4" /> {t('banner.3')}</span>
            <span className="font-bold flex items-center gap-2"><Radio className="w-4 h-4" /> {t('banner.4')}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
"""

target = "export default function App() {"
if target in content and "CameraFrameOverlay" not in content:
    content = content.replace(target, camera_frame + "\n" + target)
    with open("src/App.tsx", "w", encoding="utf-8") as f:
        f.write(content)
        print("Success")
else:
    print("Already exists or target not found")
