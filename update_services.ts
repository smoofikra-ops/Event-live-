import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

const servicesComponentReplacement = `
const Services = ({ services }: { services: Service[] }) => {
  const [tick, setTick] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setTick(prev => prev + 1);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  const fallbackImages = [
    'https://images.unsplash.com/photo-1511578314322-379afb476865?auto=format&fit=crop&q=80&w=800',
    'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=800',
    'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&q=80&w=800',
    'https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&q=80&w=800',
    'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&q=80&w=800',
    'https://images.unsplash.com/photo-1533174000255-124b17551000?auto=format&fit=crop&q=80&w=800',
  ];

  const getYoutubeEmbedUrl = (url: string) => {
    if (!url) return '';
    const regExp = /^.*(youtu.be\\/|v\\/|u\\/\\w\\/|embed\\/|watch\\?v=|\\&v=)([^#\\&\\?]*).*/;
    const match = url.match(regExp);
    if (match && match[2].length === 11) {
      return \`https://www.youtube.com/embed/\${match[2]}?autoplay=1&mute=1&loop=1&playlist=\${match[2]}&controls=0&showinfo=0&rel=0&iv_load_policy=3\`;
    }
    return url;
  };

  return (
    <SectionWrapper id="services" className="bg-white dark:bg-[#0a0a0a]">
      <div className="text-center mb-20">
        <h2 className="text-[40px] font-semibold mb-8 title-accent-center heading-gradient">خدماتنا <span className="text-gradient">المتميزة</span></h2>
        <p className="text-black/50 dark:text-white/50 max-w-[70ch] mx-auto text-[18px] font-normal">
          نقدم مجموعة شاملة من خدمات التصوير والإنتاج البصري لجميع أنواع الفعاليات بأعلى معايير الجودة العالمية.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12">
        {services.map((s, i) => {
          const Icon = IconMap[s.iconName] || Layout;
          const renderMedia = () => {
            if (s.mediaType === 'image' || s.mediaType === 'url') {
              const images = [s.mediaValue, fallbackImages[(i * 2) % fallbackImages.length], fallbackImages[(i * 2 + 1) % fallbackImages.length]].filter(Boolean);
              const currentImage = images[tick % images.length];

              return (
                <div className="w-full h-full overflow-hidden rounded-xl relative">
                  <AnimatePresence mode="wait">
                    <motion.img 
                      key={currentImage}
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 1 }}
                      src={currentImage} 
                      className="w-full h-full object-cover aspect-video absolute inset-0" 
                      alt={s.title} 
                      referrerPolicy="no-referrer" 
                      loading="lazy" 
                    />
                  </AnimatePresence>
                </div>
              );
            }
            if (s.mediaType === 'video') {
              const embedUrl = getYoutubeEmbedUrl(s.mediaValue || '');
              const isYoutube = embedUrl.includes('youtube.com');
              return (
                <div className="w-full h-full overflow-hidden rounded-xl bg-black relative">
                  {isYoutube ? (
                    <iframe 
                      src={embedUrl}
                      className="w-full h-full pointer-events-none scale-150 absolute inset-0"
                      allow="autoplay; encrypted-media"
                      title={s.title}
                    ></iframe>
                  ) : (
                    <video 
                      src={s.mediaValue} 
                      autoPlay 
                      muted 
                      loop 
                      playsInline 
                      className="w-full h-full object-cover absolute inset-0"
                    />
                  )}
                </div>
              );
            }
            
            const icons = [Icon, Camera, Video, Star, Users, Building2];
            const CurrentIcon = icons[(i + tick) % icons.length];
            return (
              <AnimatePresence mode="wait">
                <motion.div
                  key={tick}
                  initial={{ opacity: 0, scale: 0.8 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.8 }}
                  transition={{ duration: 0.5 }}
                  className="w-full h-full flex items-center justify-center"
                >
                  <CurrentIcon className="w-8 h-8 md:w-12 md:h-12" />
                </motion.div>
              </AnimatePresence>
            );
          };

          return (
            <motion.div 
              key={s.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.6, delay: i * 0.1 }}
              whileHover={{ 
                y: -10, 
                scale: 1.02, 
                boxShadow: "0 20px 40px rgba(0,0,0,0.1), 0 0 20px rgba(255,138,0,0.2)"
              }}
              className="glass-card p-10 transition-all duration-500 group cursor-pointer relative overflow-hidden"
            >
              {/* Radial Light Effect */}
              <div className="absolute -top-24 -right-24 w-48 h-48 bg-amber-500/5 dark:bg-amber-500/10 blur-[80px] rounded-full group-hover:bg-amber-500/10 dark:group-hover:bg-amber-500/20 transition-colors duration-500"></div>
              
              <div className="mb-8 p-6 rounded-[22px] glass-icon w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/30 blur-2xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                
                <motion.div whileHover={bounceAnimation} animate={{ y: [0, -8, 0] }} transition={{ duration: 4, repeat: Infinity, ease: "easeInOut", delay: i * 0.1 }} className="relative z-10 w-10 h-10 md:w-14 md:h-14 flex items-center justify-center">
                  {renderMedia()}
                </motion.div>
                {/* Inner Light Reflection */}
                <div className="absolute inset-0 bg-gradient-to-tr from-black/5 dark:from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-20 pointer-events-none rounded-[22px]"></div>
              </div>
              
              <h3 className="text-[22px] font-medium mb-6 group-hover:text-amber-500 transition-colors duration-300">{s.title}</h3>
              <p className="text-black/50 dark:text-white/50 text-[16px] leading-[1.75] font-normal">{s.desc}</p>
              
              {/* Bottom Gradient Line */}
              <div className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-transparent via-amber-500/50 to-transparent scale-x-0 group-hover:scale-x-100 transition-transform duration-500"></div>
            </motion.div>
          );
        })}
      </div>
    </SectionWrapper>
  );
};
`;

appTsx = appTsx.replace(/const Services = \(\{ services \}: \{ services: Service\[\] \}\) => \{[\s\S]*?(?=const Portfolio =)/, servicesComponentReplacement + '\n');

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Services updated with glow and auto-cycle effects');
