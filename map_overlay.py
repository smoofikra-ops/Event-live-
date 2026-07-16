import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

overlay_code = """
import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Star } from 'lucide-react';

const mockReviews = [
  { author: "أحمد عبدالله", text: "فريق احترافي جداً وتغطية مميزة للفعالية، شكراً لكم!" },
  { author: "سارة فهد", text: "جودة عالية في التصوير والمونتاج والتزام تام بالوقت." },
  { author: "شركة الرواد", text: "أفضل شركة تغطية إعلامية تعاملنا معها، شكراً لجهودكم." },
  { author: "محمد الخالد", text: "بث مباشر احترافي وبدون أي تقطيع، تجربة ممتازة." },
  { author: "نورة سعد", text: "تصوير الدرون كان رائع وأعطى بعد مختلف لتغطية المعرض." }
];

const MapReviewsOverlay = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % mockReviews.length);
    }, 4500);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="absolute inset-0 pointer-events-none flex items-center justify-center pb-24 z-20 overflow-hidden">
      <AnimatePresence mode="wait">
        <motion.div
          key={currentIndex}
          initial={{ opacity: 0, y: 20, scale: 0.8 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          exit={{ opacity: 0, y: -20, scale: 0.8 }}
          transition={{ duration: 0.5, type: "spring", bounce: 0.4 }}
          className="bg-white/95 dark:bg-black/90 backdrop-blur-md px-4 py-3 rounded-2xl shadow-2xl border border-black/10 dark:border-white/10 max-w-[250px] md:max-w-[300px] text-center relative"
        >
          {/* Tail of the speech bubble */}
          <div className="absolute -bottom-3 left-1/2 -translate-x-1/2 w-0 h-0 border-l-[10px] border-l-transparent border-t-[14px] border-t-white/95 dark:border-t-black/90 border-r-[10px] border-r-transparent drop-shadow-md"></div>
          
          <div className="flex justify-center gap-0.5 mb-1.5 text-amber-400">
            {[...Array(5)].map((_, i) => (
              <Star key={i} className="w-3.5 h-3.5 fill-current" />
            ))}
          </div>
          <p className="text-black/80 dark:text-white/80 text-xs md:text-sm font-medium mb-1.5 leading-relaxed" dir="rtl">
            "{mockReviews[currentIndex].text}"
          </p>
          <span className="text-[10px] text-black/50 dark:text-white/50 font-bold block">
            {mockReviews[currentIndex].author} - عبر جوجل ماب
          </span>
        </motion.div>
      </AnimatePresence>
    </div>
  );
};
"""

content = content.replace("const MapSection = () => {", overlay_code + "\nconst MapSection = () => {")
content = content.replace("                  ></iframe>", "                  ></iframe>\n                  <MapReviewsOverlay />")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
