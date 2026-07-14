import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Custom X Icon
x_icon_code = """const XIcon = ({ className }: { className?: string }) => (
  <svg viewBox="0 0 24 24" className={className} fill="currentColor">
    <path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z" />
  </svg>
);"""

if "const XIcon" not in content:
    # Insert it before ThemeToggle or somewhere top
    content = content.replace("const ThemeToggle = () => {", x_icon_code + "\n\nconst ThemeToggle = () => {")

old_iconmap = """                const IconMapLocal: Record<string, any> = {
                  twitter: Twitter,
                  instagram: Instagram,
                  linkedin: Linkedin,
                  youtube: Youtube,
                  facebook: Facebook,
                  tiktok: Music2,
                  snapchat: Ghost,
                  website: Globe
                };"""
new_iconmap = """                const IconMapLocal: Record<string, any> = {
                  twitter: XIcon,
                  instagram: Instagram,
                  linkedin: Linkedin,
                  youtube: Youtube,
                  facebook: Facebook,
                  tiktok: Music2,
                  snapchat: Ghost,
                  website: Globe
                };"""
content = content.replace(old_iconmap, new_iconmap)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
