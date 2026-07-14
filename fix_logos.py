import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Desktop Nav
old_desktop = """        <div className="flex items-center gap-2">
          <Camera className="w-8 h-8 text-amber-500" />
          <span className="text-2xl font-black text-gradient">EventLive</span>
        </div>"""
new_desktop = """        <a href="#home" className="flex items-center gap-2">
          <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-10 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
        </a>"""
content = content.replace(old_desktop, new_desktop)

# Sidebar
old_sidebar = """        <div className="flex items-center gap-2 mb-10 mt-2">
          <Camera className="w-8 h-8 text-amber-500" />
          <span className="text-2xl font-black text-gradient">EventLive</span>
        </div>"""
new_sidebar = """        <div className="flex items-center gap-2 mb-10 mt-2">
          <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-10 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
        </div>"""
content = content.replace(old_sidebar, new_sidebar)

# Footer
old_footer = """            <a href="#home" className="text-2xl font-black tracking-tighter text-amber-500 flex items-center gap-2 mb-6">
              <Camera className="w-6 h-6" />
              <span className="text-gradient">EventLive</span>
            </a>"""
new_footer = """            <a href="#home" className="flex items-center gap-2 mb-6">
              <img src="https://res.cloudinary.com/ozd726ro/image/upload/v1784025230/74dbadce-8a3f-4270-b985-83a0cad432e1.png" alt="EventLive" className="h-12 object-contain drop-shadow-[0_0_15px_rgba(255,138,0,0.3)]" />
            </a>"""
content = content.replace(old_footer, new_footer)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
