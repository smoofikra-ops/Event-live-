import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Change selectedWork to selectedIndex
content = content.replace("const [selectedWork, setSelectedWork] = useState<Work | null>(null);", "const [selectedIndex, setSelectedIndex] = useState<number | null>(null);\n  const selectedWork = selectedIndex !== null ? filteredWorks[selectedIndex] : null;")

# In onClick for the grid items:
content = content.replace("onClick={() => setSelectedWork(w)}", "onClick={() => setSelectedIndex(i)}")

# Update the AnimatePresence block
old_modal = """      <AnimatePresence>
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
              className="absolute top-8 rtl:right-8 ltr:left-8 text-white hover:text-amber-500"
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
                isYoutube(selectedWork.videoUrl) ? (
                  <iframe 
                    src={getYoutubeEmbedUrl(selectedWork.videoUrl, true)}
                    className="w-full h-full"
                    allow="autoplay; encrypted-media"
                    allowFullScreen
                  ></iframe>
                ) : (
                  <video 
                    src={selectedWork.videoUrl} 
                    autoPlay 
                    controls 
                    playsInline
                    poster={selectedWork.img}
                    className="w-full h-full object-contain bg-black" 
                  />
                )
              ) : (
                <img src={selectedWork.img} className="w-full h-full object-contain" alt={selectedWork.title} />
              )}
              <div className="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black to-transparent">
                <h3 className="text-2xl font-bold text-white">{selectedWork.title}</h3>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>"""

new_modal = """      <AnimatePresence>
        {selectedWork && (
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedIndex(null)}
            className="fixed inset-0 z-[200] bg-black/95 flex items-center justify-center p-4 md:p-12"
          >
            <motion.button 
              whileHover={{ scale: 1.1, rotate: 90 }}
              className="absolute top-8 rtl:right-8 ltr:left-8 text-white hover:text-amber-500 z-[210]"
            >
              <X className="w-8 h-8" />
            </motion.button>
            
            {/* Prev Button */}
            {selectedIndex !== null && selectedIndex > 0 && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex - 1); }}
                className="absolute left-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-0 rtl:rotate-180" />
              </button>
            )}

            {/* Next Button */}
            {selectedIndex !== null && selectedIndex < filteredWorks.length - 1 && (
              <button 
                onClick={(e) => { e.stopPropagation(); setSelectedIndex(selectedIndex + 1); }}
                className="absolute right-4 top-1/2 -translate-y-1/2 w-12 h-12 bg-black/50 hover:bg-amber-500 text-white flex items-center justify-center rounded-full backdrop-blur-md transition-colors z-[210] hidden md:flex"
              >
                <ArrowLeft className="w-6 h-6 ltr:rotate-180 rtl:rotate-0" />
              </button>
            )}

            <motion.div 
              key={selectedWork.id}
              initial={{ scale: 0.9, y: 50, opacity: 0 }}
              animate={{ scale: 1, y: 0, opacity: 1 }}
              exit={{ scale: 0.9, y: -50, opacity: 0 }}
              drag="x"
              dragConstraints={{ left: 0, right: 0 }}
              dragElastic={0.2}
              onDragEnd={(e, { offset, velocity }) => {
                const swipe = offset.x;
                if (swipe < -50 && selectedIndex !== null && selectedIndex < filteredWorks.length - 1) {
                  setSelectedIndex(selectedIndex + 1);
                } else if (swipe > 50 && selectedIndex !== null && selectedIndex > 0) {
                  setSelectedIndex(selectedIndex - 1);
                }
              }}
              onClick={(e) => e.stopPropagation()}
              className="relative w-full max-w-5xl aspect-video bg-[#111] rounded-2xl overflow-hidden shadow-[0_0_50px_rgba(0,0,0,0.5)] border border-white/10 touch-none cursor-grab active:cursor-grabbing"
            >
              {selectedWork.videoUrl ? (
                isYoutube(selectedWork.videoUrl) ? (
                  <iframe 
                    src={getYoutubeEmbedUrl(selectedWork.videoUrl, true)}
                    className="w-full h-full pointer-events-auto"
                    allow="autoplay; encrypted-media"
                    allowFullScreen
                  ></iframe>
                ) : (
                  <video 
                    src={selectedWork.videoUrl} 
                    autoPlay 
                    controls 
                    playsInline
                    poster={selectedWork.img}
                    className="w-full h-full object-contain bg-black pointer-events-auto" 
                  />
                )
              ) : (
                <img src={selectedWork.img} className="w-full h-full object-contain pointer-events-none" alt={selectedWork.title} />
              )}
              <div className="absolute bottom-0 left-0 right-0 p-8 bg-gradient-to-t from-black to-transparent pointer-events-none">
                <h3 className="text-2xl font-bold text-white">{selectedWork.title}</h3>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>"""

content = content.replace(old_modal, new_modal)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
