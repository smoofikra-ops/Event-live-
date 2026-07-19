import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useLanguage } from './LanguageContext';

export const CustomHeroSequence = () => {
  const { language } = useLanguage();

  // States for text
  const [title1, setTitle1] = useState('');
  const [showHeart, setShowHeart] = useState(false);
  const [showCamera, setShowCamera] = useState(false);
  const [title2, setTitle2] = useState('');
  
  const [sub1, setSub1] = useState('');
  const [sub2, setSub2] = useState('');
  const [sub3, setSub3] = useState('');
  
  const [showArrow, setShowArrow] = useState(false);

  // Full texts (Arabic)
  const fullTitle1 = 'نوثق لحظتك';
  const fullTitle2 = ' باحترافية عالية';
  
  const fullSub1 = 'تصوير فوتوغرافي';
  const fullSubVideo = ' وفيديو';
  const fullSub3 = ' وبث مباشر احترافي للمهرجانات، المؤتمرات، الفعاليات الوطنية، وغير ذلك في جميع أنحاء المملكة. ✨';

  useEffect(() => {
    if (language !== 'ar') {
       setTitle1('Documenting your moments');
       setTitle2(' with high professionalism');
       setSub1('Photography');
       setSub2(' and video');
       setSub3(' and professional live streaming for festivals, conferences, national events, and more across the Kingdom. ✨');
       setShowArrow(true);
       return;
    }

    let isMounted = true;
    const typeText = async (
      text: string, 
      setFn: React.Dispatch<React.SetStateAction<string>>, 
      speed: number = 50,
      initialText: string = ''
    ) => {
      let current = initialText;
      for (let i = 0; i < text.length; i++) {
        if (!isMounted) return;
        current += text[i];
        setFn(current);
        await new Promise(r => setTimeout(r, speed));
      }
    };

    const deleteText = async (
      currentLength: number,
      targetLength: number,
      setFn: React.Dispatch<React.SetStateAction<string>>,
      textToSlice: string,
      speed: number = 25
    ) => {
      for (let i = currentLength; i >= targetLength; i--) {
        if (!isMounted) return;
        setFn(textToSlice.slice(0, i));
        await new Promise(r => setTimeout(r, speed));
      }
    }

    const runSequence = async () => {
      while (isMounted) {
        // Reset
        setTitle1(''); setTitle2(''); setSub1(''); setSub2(''); setSub3('');
        setShowHeart(false); setShowCamera(false); setShowArrow(false);

        // 1. Type "نوثق لحظتك"
        await typeText(fullTitle1, setTitle1, 80);
        await new Promise(r => setTimeout(r, 200));

        // 2. Show ❤️
        if (!isMounted) return;
        setShowHeart(true);
        await new Promise(r => setTimeout(r, 800));
        if (!isMounted) return;
        setShowHeart(false);

        // 3. Show 📸 and disappear
        if (!isMounted) return;
        setShowCamera(true);
        await new Promise(r => setTimeout(r, 800));
        if (!isMounted) return;
        setShowCamera(false);

        // 4. Type " باحترافية عالية"
        await typeText(fullTitle2, setTitle2, 80);
        await new Promise(r => setTimeout(r, 400));

        // 5. Type "تصوير فوتوغرافي"
        await typeText(fullSub1, setSub1, 50);
        await new Promise(r => setTimeout(r, 200));

        // 6. Type " وفيديو"
        await typeText(fullSubVideo, setSub2, 50);
        await new Promise(r => setTimeout(r, 400));

        // 7. Delete "فيديو"
        await deleteText(fullSubVideo.length, 2, setSub2, fullSubVideo, 50); 
        await new Promise(r => setTimeout(r, 300));

        // 8. Rewrite "فيديو"
        await typeText(fullSubVideo.slice(2), setSub2, 50, " و");
        await new Promise(r => setTimeout(r, 200));

        // 9. Type rest of subtitle
        await typeText(fullSub3, setSub3, 40);
        await new Promise(r => setTimeout(r, 500));

        // 10. Show arrow
        if (!isMounted) return;
        setShowArrow(true);
        
        // 11. Pause before erasing
        await new Promise(r => setTimeout(r, 4000));
        if (!isMounted) return;
        setShowArrow(false);
        
        // 12. Erase everything backwards smoothly
        await deleteText(fullSub3.length, 0, setSub3, fullSub3, 20);
        await deleteText(fullSubVideo.length, 0, setSub2, fullSubVideo, 25);
        await deleteText(fullSub1.length, 0, setSub1, fullSub1, 25);
        await deleteText(fullTitle2.length, 0, setTitle2, fullTitle2, 35);
        await deleteText(fullTitle1.length, 0, setTitle1, fullTitle1, 35);
        
        // Brief pause before rewriting
        await new Promise(r => setTimeout(r, 800));
      }
    };

    runSequence();
    return () => { isMounted = false; };
  }, [language]);

  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 1.5, ease: "easeOut" }}
      className="relative"
    >
      {/* Particles Overlay Behind Text */}
      <div className="absolute -inset-10 z-[-1] pointer-events-none overflow-hidden">
        {[...Array(15)].map((_, i) => (
          <motion.div
            key={i}
            initial={{ 
              x: Math.random() * 100 + "%", 
              y: Math.random() * 100 + "%",
              opacity: 0,
              scale: 0
            }}
            animate={{ 
              x: Math.random() * 100 + "%",
              y: Math.random() * 100 + "%",
              opacity: [0, 0.8, 0],
              scale: [0, Math.random() * 1.5 + 0.5, 0]
            }}
            transition={{ 
              duration: 4 + Math.random() * 4, 
              repeat: Infinity, 
              ease: "easeInOut",
              delay: Math.random() * 2
            }}
            className="absolute w-2 h-2 bg-amber-500/40 rounded-full blur-[2px]"
          />
        ))}
      </div>

      <h1 className="text-[18px] sm:text-[28px] md:text-[44px] font-bold leading-[1.4] sm:leading-[1.2] mb-4 sm:mb-6 tracking-tight hero-heading-gradient min-h-[40px] sm:min-h-[80px] flex flex-wrap items-center gap-x-1 sm:gap-x-2">
        <span>{title1}</span>
        <AnimatePresence mode="wait">
          {showHeart && (
            <motion.span 
              key="heart"
              initial={{ scale: 0, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0, opacity: 0 }}
              className="inline-block text-red-500 text-[24px] sm:text-[40px]"
            >
              ❤️
            </motion.span>
          )}
          {showCamera && (
            <motion.span 
              key="camera"
              initial={{ scale: 0, opacity: 0, rotate: -20 }}
              animate={{ scale: 1.2, opacity: 1, rotate: 0 }}
              exit={{ scale: 0, opacity: 0, rotate: 20 }}
              className="inline-block text-[24px] sm:text-[40px]"
            >
              📸
            </motion.span>
          )}
        </AnimatePresence>
        <span className="text-gradient w-auto">{title2}</span>
      </h1>
      
      <p className="text-[12px] sm:text-[16px] md:text-[20px] text-white/90 mb-4 sm:mb-8 leading-[1.6] sm:leading-[1.75] max-w-[70ch] font-normal min-h-[40px] sm:min-h-[80px]">
        {sub1}
        <span className="text-amber-500 font-bold">{sub2}</span>
        {sub3}
      </p>

      <AnimatePresence>
        {showArrow && (
          <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="absolute -bottom-16 right-20 md:right-40 text-amber-500 pointer-events-none"
          >
             <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className="animate-bounce drop-shadow-[0_0_8px_rgba(255,138,0,0.5)]">
                <path d="M12 5v14M19 12l-7 7-7-7"/>
             </svg>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};
