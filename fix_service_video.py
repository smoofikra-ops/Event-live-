import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_service_video = """                    <video 
                      src={s.mediaValue} 
                      autoPlay 
                      muted 
                      loop 
                      playsInline 
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                    />"""

new_service_video = """                    <video 
                      src={s.mediaValue} 
                      autoPlay 
                      muted 
                      loop 
                      playsInline 
                      poster="https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=2070"
                      className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700"
                    />"""

content = content.replace(old_service_video, new_service_video)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
