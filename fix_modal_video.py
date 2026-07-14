import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_modal_video = """                  <video 
                    src={selectedWork.videoUrl} 
                    autoPlay 
                    controls 
                    className="w-full h-full object-contain bg-black" 
                  />"""

new_modal_video = """                  <video 
                    src={selectedWork.videoUrl} 
                    autoPlay 
                    controls 
                    playsInline
                    poster={selectedWork.img}
                    className="w-full h-full object-contain bg-black" 
                  />"""

content = content.replace(old_modal_video, new_modal_video)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
