import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

map_section_code = """
const MapSection = () => {
  return (
    <SectionWrapper id="map" className="bg-white dark:bg-[#0a0a0a] py-12 md:py-20 border-b border-black/5 dark:border-white/5">
      <div className="max-w-7xl mx-auto px-6">
        <ScrollReveal>
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-5xl font-bold heading-gradient title-accent-center mb-6">حياكم</h2>
            <p className="text-black/60 dark:text-white/60 max-w-2xl mx-auto text-lg">نسعد بزيارتكم لنا في مقرنا</p>
          </div>
        </ScrollReveal>
        <ScrollReveal className="delay-100">
          <div className="relative max-w-5xl mx-auto">
            {/* 3D Shadow underneath */}
            <div className="absolute -inset-4 bg-gradient-to-r from-amber-500/20 to-amber-600/20 blur-xl opacity-50 dark:opacity-30 rounded-[3rem] -z-10"></div>
            
            <div className="animated-border-container shadow-[0_20px_50px_rgba(0,0,0,0.2)] dark:shadow-[0_20px_50px_rgba(0,0,0,0.5)]">
              <div className="animated-border-gradient"></div>
              <div className="relative bg-white dark:bg-[#111] rounded-[22px] overflow-hidden z-10 h-[400px] md:h-[500px] p-2">
                <div className="w-full h-full rounded-[16px] overflow-hidden relative">
                  <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4242.39251162464!2d46.5761172!3d24.5809918!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e2f0fef903a6473%3A0xa51160831c34a8c0!2z2LTYsdmD2Kkg2KfZitmB2YbYqiDZhNin2YrZgQ!5e1!3m2!1sar!2ssa!4v1784041066433!5m2!1sar!2ssa" 
                    width="100%" 
                    height="100%" 
                    style={{ border: 0 }} 
                    allowFullScreen={True} 
                    loading="lazy" 
                    referrerPolicy="no-referrer-when-downgrade"
                    className="absolute inset-0 grayscale-[0.2] contrast-125 dark:invert-[0.9] dark:hue-rotate-180 dark:contrast-100 transition-all duration-700 hover:grayscale-0"
                  ></iframe>
                </div>
              </div>
            </div>
          </div>
        </ScrollReveal>
      </div>
    </SectionWrapper>
  );
};
"""

content = content.replace("const AnnouncementBanner = () => {", map_section_code + "\nconst AnnouncementBanner = () => {")

content = content.replace("<Contact />\n      </main>", "<Contact />\n        <MapSection />\n      </main>")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
