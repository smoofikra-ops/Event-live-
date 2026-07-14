import re
import json

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add cardBgImage to all services in INITIAL_DATA
# I will use a simple string replace for those missing it
missing_bg = [
    """{ id: '5', title: "المؤتمرات", desc: "نقدم تغطية مؤتمرات ومعارض احترافية، نوثق كل لحظة من الكلمات الرسمية إلى جلسات النقاش، مع إمكانيات البث المباشر.", iconName: 'Radio', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '6', title: "الفعاليات المؤسسية", desc: "نُقدّم تغطيات احترافية لفعاليات الشركات، المؤتمرات والاجتماعات، مع إبراز الهوية المؤسسية وتوفير خدمة البث المباشر.", iconName: 'Building2', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '7', title: "العقارات", desc: "نُبرز جماليات العقار بدقة عالية من الداخل والخارج باستخدام التصوير الأرضي والجوي، مع مونتاج احترافي جاذب.", iconName: 'Home', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '8', title: "الإعلانات التجارية", desc: "نصمم محتوى بصري إبداعي يُبرز كل منتج بأفضل صورة، مع إعداد ستايل تصوير مميز وإخراج احترافي.", iconName: 'Megaphone', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800' }"""
]

fixed_bg = [
    """{ id: '5', title: "المؤتمرات", desc: "نقدم تغطية مؤتمرات ومعارض احترافية، نوثق كل لحظة من الكلمات الرسمية إلى جلسات النقاش، مع إمكانيات البث المباشر.", iconName: 'Radio', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&q=80&w=800', cardBgImage: 'https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '6', title: "الفعاليات المؤسسية", desc: "نُقدّم تغطيات احترافية لفعاليات الشركات، المؤتمرات والاجتماعات، مع إبراز الهوية المؤسسية وتوفير خدمة البث المباشر.", iconName: 'Building2', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?auto=format&fit=crop&q=80&w=800', cardBgImage: 'https://images.unsplash.com/photo-1515162816999-a0c47dc192f7?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '7', title: "العقارات", desc: "نُبرز جماليات العقار بدقة عالية من الداخل والخارج باستخدام التصوير الأرضي والجوي، مع مونتاج احترافي جاذب.", iconName: 'Home', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800', cardBgImage: 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&q=80&w=800' }""",
    """{ id: '8', title: "الإعلانات التجارية", desc: "نصمم محتوى بصري إبداعي يُبرز كل منتج بأفضل صورة، مع إعداد ستايل تصوير مميز وإخراج احترافي.", iconName: 'Megaphone', mediaType: 'image', mediaValue: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800', cardBgImage: 'https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&q=80&w=800' }"""
]

for old, new in zip(missing_bg, fixed_bg):
    content = content.replace(old, new)

# Update render logic
# remove `renderMedia` completely
render_media_block = """          const renderMedia = () => {
            if (s.mediaType === 'image' || s.mediaType === 'url') {
              const images = [s.mediaValue, fallbackImages[(i * 2) % fallbackImages.length], fallbackImages[(i * 2 + 1) % fallbackImages.length]].filter(Boolean);
              const currentImage = images[tick % images.length];

              return (
                <div className="w-full h-full overflow-hidden rounded-xl relative">
                  <div className="absolute inset-0 bg-black/10 dark:bg-white/10 animate-pulse"></div>
                  <AnimatePresence mode="wait">
                    <motion.img 
                      key={currentImage}
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ duration: 1 }}
                      src={currentImage} 
                      className="w-full h-full object-cover aspect-video absolute inset-0 relative z-10" 
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
                  <div className="absolute inset-0 bg-white/10 animate-pulse z-0"></div>
                  {isYoutube ? (
                    <iframe 
                      src={embedUrl}
                      className="w-full h-full pointer-events-none scale-150 absolute inset-0 z-10"
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
                      className="w-full h-full object-cover absolute inset-0 z-10"
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
          };"""

content = content.replace(render_media_block, "")

# replace image rendering in the card with the blurred background effect
old_card_bg = """              {s.cardBgImage && (
                <>
                  <img 
                    src={s.cardBgImage} 
                    alt={s.title} 
                    className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 z-0"
                    loading="lazy"
                  />
                  <div className="absolute inset-0 bg-black/60 group-hover:bg-black/50 transition-colors duration-500 z-0 backdrop-blur-[2px]"></div>
                </>
              )}"""

new_card_bg = """              {s.cardBgImage && (
                <>
                  <img 
                    src={s.cardBgImage} 
                    alt={s.title} 
                    className="absolute inset-0 w-full h-full object-cover transition-all duration-700 blur-[8px] group-hover:blur-none group-hover:scale-110 z-0 scale-105"
                    loading="lazy"
                  />
                  <div className="absolute inset-0 bg-black/60 group-hover:bg-black/40 transition-colors duration-500 z-0"></div>
                </>
              )}"""

content = content.replace(old_card_bg, new_card_bg)

# replace `{renderMedia()}` with the icon
content = content.replace("{renderMedia()}", '<Icon className="w-8 h-8 md:w-12 md:h-12" />')

# replace `s.title` with `t(\`service.${s.id}.title\`) || s.title` and same for desc
old_title = "{s.title}</h3>"
new_title = "{t(`service.${s.id}.title`) || s.title}</h3>"

old_desc = "{s.desc}</p>"
new_desc = "{t(`service.${s.id}.desc`) || s.desc}</p>"

content = content.replace(old_title, new_title)
content = content.replace(old_desc, new_desc)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
