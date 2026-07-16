import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add state
content = re.sub(
    r"const Services = \(\{ services \}: \{ services: Service\[\] \}\) => \{\n  const \{ t, language \} = useLanguage\(\);\n  const \[tick, setTick\] = useState\(0\);",
    "const Services = ({ services }: { services: Service[] }) => {\n  const { t, language } = useLanguage();\n  const [tick, setTick] = useState(0);\n  const [selectedVideo, setSelectedVideo] = useState<string | null>(null);",
    content
)

content = content.replace(
    'transition={{ duration: 0.6, delay: i * 0.1 }}',
    'transition={{ duration: 0.6, delay: i * 0.1 }}\n              onClick={() => { if (s.id === \'1\') setSelectedVideo(\'https://drive.google.com/file/d/1ndvNPiH-WplY1W_IUkJi4LDMUJ-Q7frJ/preview\'); }}'
)

# Add modal
modal_code = """      <AnimatePresence>
        {selectedVideo && (
          <div className="fixed inset-0 z-[200] flex items-center justify-center p-4 sm:p-6 md:p-12">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="absolute inset-0 bg-black/90 backdrop-blur-xl"
              onClick={() => setSelectedVideo(null)}
            />
            
            <motion.div
              initial={{ opacity: 0, scale: 0.9, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.9, y: 20 }}
              transition={{ type: "spring", damping: 25, stiffness: 300 }}
              className="relative w-full max-w-5xl aspect-video bg-black rounded-2xl overflow-hidden shadow-2xl ring-1 ring-white/20"
            >
              <button
                onClick={(e) => { e.stopPropagation(); setSelectedVideo(null); }}
                className="absolute top-4 right-4 rtl:left-4 rtl:right-auto z-50 p-2 bg-black/50 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-colors border border-white/10"
              >
                <X className="w-6 h-6" />
              </button>
              
              <iframe
                src={selectedVideo}
                className="w-full h-full"
                allow="autoplay; encrypted-media"
                allowFullScreen
              ></iframe>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </SectionWrapper>"""

content = content.replace("    </SectionWrapper>\n  );\n};\n\nconst PortfolioMediaContent", modal_code + "\n  );\n};\n\nconst PortfolioMediaContent")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
