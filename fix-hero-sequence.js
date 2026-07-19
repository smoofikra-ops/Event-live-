import fs from 'fs';
let code = fs.readFileSync('src/CustomHeroSequence.tsx', 'utf-8');

const targetStr = `      <h1 className="text-[40px] font-bold leading-[1.2] mb-6 tracking-tight hero-heading-gradient min-h-[130px] flex flex-wrap items-center gap-x-2">
        <span style={{ fontSize: '31px', lineHeight: '64.6px', height: '39.6016px' }}>{title1}</span>
        <AnimatePresence mode="wait">
          {showHeart && (
            <motion.span 
              key="heart"
              initial={{ scale: 0, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0, opacity: 0 }}
              className="inline-block text-red-500"
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
              className="inline-block"
            >
              📸
            </motion.span>
          )}
        </AnimatePresence>
        <span className="text-gradient" style={{ fontSize: '34px', lineHeight: '61.6px', height: '49.6016px' }}>{title2}</span>
      </h1>
      
      <p className="text-[16px] text-white/90 mb-12 leading-[1.75] max-w-[70ch] font-normal min-h-[90px]" style={{ height: '82px' }}>
        {sub1}
        <span className="text-amber-500 font-bold">{sub2}</span>
        {sub3}
      </p>`;

const replacement = `      <h1 className="text-[20px] sm:text-[32px] md:text-[44px] font-bold leading-[1.4] sm:leading-[1.2] mb-4 sm:mb-6 tracking-tight hero-heading-gradient min-h-[60px] sm:min-h-[100px] flex flex-wrap items-center gap-x-1 sm:gap-x-2">
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
        <span className="text-gradient w-full sm:w-auto">{title2}</span>
      </h1>
      
      <p className="text-[13px] sm:text-[16px] md:text-[20px] text-white/90 mb-8 sm:mb-12 leading-[1.6] sm:leading-[1.75] max-w-[70ch] font-normal min-h-[60px] sm:min-h-[90px]">
        {sub1}
        <span className="text-amber-500 font-bold">{sub2}</span>
        {sub3}
      </p>`;

code = code.replace(targetStr, replacement);
fs.writeFileSync('src/CustomHeroSequence.tsx', code);
