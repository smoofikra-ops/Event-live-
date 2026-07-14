import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix ColorMapLocal
old_colormap = """                const ColorMapLocal: Record<string, string> = {
                  twitter: 'hover:bg-black dark:hover:bg-white hover:text-white dark:hover:text-black border-black/10 dark:border-white/10',
                  instagram: 'hover:bg-gradient-to-tr hover:from-[#f09433] hover:via-[#dc2743] hover:to-[#bc1888] hover:text-white border-black/10 dark:border-white/10 hover:border-transparent',
                  linkedin: 'hover:bg-[#0077b5] hover:text-white border-black/10 dark:border-white/10 hover:border-transparent',
                  snapchat: 'hover:bg-[#FFFC00] hover:text-black border-black/10 dark:border-white/10 hover:border-transparent',
                  tiktok: 'hover:bg-black dark:hover:bg-white hover:text-white dark:hover:text-black border-black/10 dark:border-white/10',
                };"""
new_colormap = """                const ColorMapLocal: Record<string, string> = {
                  twitter: 'bg-black text-white dark:bg-white dark:text-black hover:opacity-80',
                  instagram: 'bg-gradient-to-tr from-[#f09433] via-[#dc2743] to-[#bc1888] text-white hover:opacity-80',
                  linkedin: 'bg-[#0077b5] text-white hover:opacity-80',
                  snapchat: 'bg-[#FFFC00] text-black hover:opacity-80',
                  tiktok: 'bg-black text-white dark:bg-white dark:text-black hover:opacity-80',
                };"""
content = content.replace(old_colormap, new_colormap)

# Remove border-transparent from hoverColorClass if it exists
old_return = """                const hoverColorClass = ColorMapLocal[link.platform] || 'hover:bg-amber-500 hover:text-black';

                return (
                  <a key={i} href={link.url} target="_blank" rel="noopener noreferrer" className={`w-10 h-10 rounded-full bg-black/5 dark:bg-white/5 flex items-center justify-center text-black/60 dark:text-white/60 transition-all border border-transparent ${hoverColorClass}`}>"""
new_return = """                const colorClass = ColorMapLocal[link.platform] || 'bg-amber-500 text-black hover:opacity-80';

                return (
                  <a key={i} href={link.url} target="_blank" rel="noopener noreferrer" className={`w-10 h-10 rounded-full flex items-center justify-center transition-opacity border border-transparent ${colorClass}`}>"""
content = content.replace(old_return, new_return)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
