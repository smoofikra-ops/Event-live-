import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

// Fix Services Close Button
code = code.replace(
  `className="fixed top-4 right-4 rtl:left-4 rtl:right-auto z-[250] p-2 bg-black/50 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-colors border border-white/10"`,
  `className="absolute top-4 right-4 rtl:left-4 rtl:right-auto z-[250] p-2 bg-black/50 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-colors border border-white/10 shadow-lg"`
);

// Fix Portfolio Close Button
code = code.replace(
  `className="fixed top-4 right-4 rtl:left-4 rtl:right-auto text-white hover:text-amber-500 z-[250] p-2 bg-black/50 rounded-full"`,
  `className="absolute top-4 right-4 rtl:left-4 rtl:right-auto text-white hover:text-amber-500 z-[250] p-2 bg-black/50 rounded-full shadow-lg"`
);

// Remove the standalone button in Portfolio and put it inside the container
const oldPortfolioModal = `          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedIndex(null)}
            className="fixed inset-0 z-[200] bg-black/95 flex items-center justify-center p-4 md:p-12"
          >
            <motion.button 
              whileHover={{ scale: 1.1, rotate: 90 }}
              onClick={(e) => { e.stopPropagation(); setSelectedIndex(null); }}
              className="absolute top-4 right-4 rtl:left-4 rtl:right-auto text-white hover:text-amber-500 z-[250] p-2 bg-black/50 rounded-full shadow-lg"
            >
              <X className="w-8 h-8" />
            </motion.button>
            
            {/* Prev Button */}`;

const newPortfolioModal = `          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedIndex(null)}
            className="fixed inset-0 z-[200] bg-black/95 flex items-center justify-center p-4 md:p-12"
          >
            
            {/* Prev Button */}`;

code = code.replace(oldPortfolioModal, newPortfolioModal);

const oldVideoContainer = `ref={videoContainerRef} className="relative w-full h-[90vh] md:h-auto max-w-5xl md:aspect-video bg-[#111] rounded-xl md:rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(0,0,0,0.5)] border border-white/10 touch-none cursor-grab active:cursor-grabbing flex flex-col items-center justify-center"
            >
              {selectedWork.videoUrl ? (`;

const newVideoContainer = `ref={videoContainerRef} className="relative w-full h-[90vh] md:h-auto max-w-5xl md:aspect-video bg-[#111] rounded-xl md:rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(0,0,0,0.5)] border border-white/10 touch-none cursor-grab active:cursor-grabbing flex flex-col items-center justify-center"
            >
              <motion.button 
                whileHover={{ scale: 1.1, rotate: 90 }}
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(null); }}
                className="absolute top-4 right-4 rtl:left-4 rtl:right-auto text-white hover:text-amber-500 z-[250] p-2 bg-black/50 rounded-full shadow-lg"
              >
                <X className="w-8 h-8" />
              </motion.button>
              {selectedWork.videoUrl ? (`;

code = code.replace(oldVideoContainer, newVideoContainer);

// Make sure videos have preload="auto" and loading is improved
code = code.replace(/<video /g, '<video preload="auto" ');
// Fix if duplicate preload auto exists
code = code.replace(/preload="auto" preload="auto"/g, 'preload="auto"');

fs.writeFileSync('src/App.tsx', code);
