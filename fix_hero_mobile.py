import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the mobile background that covers the video
old_mobile_bg = """      {/* Mobile background decorative */}
      <div className="md:hidden absolute inset-0 bottom-0 bg-[#0a0a0a] z-0 -mt-20"></div>"""
content = content.replace(old_mobile_bg, "")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
