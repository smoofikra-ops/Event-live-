import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

// Update Work interface
appTsx = appTsx.replace(
  'videoUrl?: string;',
  'videoUrl?: string;\n  category?: string;'
);

// Update INITIAL_DATA works
const updatedWorks = `works: [
    { id: '1', title: "معرض الزراعة", category: "فيديو", img: "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&q=80&w=800", videoUrl: "https://www.youtube.com/watch?v=dQw4w9WgXcQ" },
    { id: '2', title: "كشتة موظفين", category: "تصوير", img: "https://images.unsplash.com/photo-1523580494863-6f3031224c94?auto=format&fit=crop&q=80&w=800" },
    { id: '3', title: "مؤتمر التعدين", category: "تصوير", img: "https://images.unsplash.com/photo-1475721027785-f74eccf877e2?auto=format&fit=crop&q=80&w=800" },
    { id: '4', title: "مطعم جاردن لايت", category: "بث مباشر", img: "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&q=80&w=800" },
    { id: '5', title: "بنك الجزيرة كابيتال", category: "تصوير", img: "https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&q=80&w=800" },
    { id: '6', title: "مهرجان الجولف", category: "فيديو", img: "https://images.unsplash.com/photo-1535131749006-b7f58c99034b?auto=format&fit=crop&q=80&w=800" },
  ],`;

appTsx = appTsx.replace(/works: \[\s*\{ id: '1'[\s\S]*?\],/, updatedWorks);

const portfolioComponent = `
const Portfolio = ({ works }: { works: Work[] }) => {
  const [selectedWork, setSelectedWork] = useState<Work | null>(null);
  const [activeCategory, setActiveCategory] = useState<string>('الكل');

  const categories = ['الكل', 'تصوير', 'فيديو', 'بث مباشر'];
  const filteredWorks = activeCategory === 'الكل' ? works : works.filter(w => w.category === activeCategory);

  const getYoutubeEmbedUrl = (url: string, isLightbox = false) => {
    if (!url) return '';
    const regExp = /^.*(youtu.be\\/|v\\/|u\\/\\w\\/|embed\\/|watch\\?v=|\\&v=)([^#\\&\\?]*).*/;
    const match = url.match(regExp);
    if (match && match[2].length === 11) {
      return isLightbox 
        ? \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&rel=0\`
        : \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&mute=1&loop=1&playlist=\${match[2]}&controls=0\`;
    }
    return url;
  };

  return (
    <SectionWrapper id="portfolio">
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-8">
        <div>
          <h2 className="text-[40px] font-semibold mb-6 title-accent heading-gradient">أعمالنا <span className="text-gradient">السابقة</span></h2>
          <p className="text-black/50 dark:text-white/50 max-w-[60ch] text-[18px] font-normal">
            نفتخر بسجل حافل من الإنجازات والفعاليات التي قمنا بتوثيقها بأعلى معايير الجودة والإبداع.
          </p>
        </div>
        <div className="flex gap-4">
          <div className="w-16 h-16 rounded-full border border-black/10 dark:border-white/10 flex items-center justify-center text-amber-500 group hover:border-amber-500 transition-colors cursor-pointer">
            <ArrowLeft className="w-6 h-6 rotate-45 group-hover:rotate-0 transition-transform" />
          </div>
        </div>
      </div>

      <div className="flex flex-wrap gap-4 mb-12">
        {categories.map(cat => (
          <button
            key={cat}
            onClick={() => setActiveCategory(cat)}
            className={\`px-6 py-2 rounded-full font-bold transition-all \${activeCategory === cat ? 'bg-amber-500 text-black' : 'bg-black/5 dark:bg-white/5 text-black/70 dark:text-white/70 hover:bg-black/10 dark:hover:bg-white/10'}\`}
          >
            {cat}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <AnimatePresence mode="popLayout">
          {filteredWorks.map((w, i) => {
            const hasVideo = !!w.videoUrl;
            return (
              <motion.div
                layout
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.9 }}
                transition={{ duration: 0.3 }}
                key={w.id}
                className="group cursor-pointer"
                onClick={() => setSelectedWork(w)}
              >
                <div className="relative aspect-video rounded-2xl overflow-hidden mb-6 bg-black/5 dark:bg-[#111]">
                  {hasVideo && !selectedWork ? (
                    <iframe 
                      src={getYoutubeEmbedUrl(w.videoUrl!)}
                      className="w-full h-full pointer-events-none scale-150"
                      allow="autoplay; encrypted-media"
                      title={w.title}
                      loading="lazy"
                    ></iframe>
                  ) : (
                    <img 
                      src={w.img} 
                      className="w-full h-full object-cover aspect-video transition-transform duration-700 group-hover:scale-110" 
                      alt={w.title}
                      loading="lazy"
                    />
                  )}
                  
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-all duration-500 flex flex-col justify-end p-8">
                    <div className="transform translate-y-8 group-hover:translate-y-0 transition-transform duration-500">
                      {w.category && (
                        <span className="inline-block px-3 py-1 bg-amber-500 text-black text-xs font-bold rounded-full mb-3">
                          {w.category}
                        </span>
                      )}
                      <h3 className="text-2xl font-bold text-white mb-2">{w.title}</h3>
                      <div className="flex items-center gap-2 text-white/70 text-sm font-bold">
                        <span className="w-8 h-[1px] bg-amber-500"></span>
                        {hasVideo ? 'عرض الفيديو' : 'عرض التفاصيل'}
                      </div>
                    </div>
                  </div>

                  {hasVideo && (
                    <div className="absolute top-4 right-4 w-10 h-10 bg-amber-500 rounded-full flex items-center justify-center text-black shadow-lg">
                      <Video className="w-5 h-5" />
                    </div>
                  )}
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>
      </div>

      <AnimatePresence>
        {selectedWork && (
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedWork(null)}
            className="fixed inset-0 z-[200] bg-black/95 flex items-center justify-center p-4 md:p-12"
          >
            <motion.button 
              whileHover={{ scale: 1.1, rotate: 90 }}
              className="absolute top-8 right-8 text-white hover:text-amber-500"
            >
              <X className="w-8 h-8" />
            </motion.button>
            <motion.div 
              initial={{ scale: 0.9, y: 50 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.9, y: 50 }}
              onClick={(e) => e.stopPropagation()}
              className="relative w-full max-w-5xl aspect-video bg-[#111] rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(0,0,0,0.5)] border border-white/10"
            >
              {selectedWork.videoUrl ? (
                <iframe 
                  src={getYoutubeEmbedUrl(selectedWork.videoUrl, true)}
                  className="w-full h-full"
                  allow="autoplay; encrypted-media"
                  allowFullScreen
                ></iframe>
              ) : (
                <img src={selectedWork.img} className="w-full h-full object-contain" alt={selectedWork.title} />
              )}
              <div className="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black to-transparent">
                <h3 className="text-2xl font-bold text-white">{selectedWork.title}</h3>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </SectionWrapper>
  );
};
`;

appTsx = appTsx.replace(/const Portfolio = \(\{ works \}: \{ works: Work\[\] \}\) => \{[\s\S]*?(?=const FAQ = \(\) => \{)/, portfolioComponent + '\n');

if (!appTsx.includes('import { X')) {
  appTsx = appTsx.replace('import { ', 'import { X, ');
}

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Portfolio updated');
