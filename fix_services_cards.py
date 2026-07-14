import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace service card wrapper
old_card_class = r'className={`glass-card p-3 sm:p-5 md:p-8 transition-all duration-500 group cursor-pointer relative overflow-hidden flex flex-col justify-between min-h-\[160px\] sm:min-h-\[250px\] md:min-h-\[350px\] flex-shrink-0 w-full \$\{spanClass\}`}'
new_card_class = r'className={`bg-white dark:bg-[#111] p-5 md:p-8 rounded-[2rem] transition-all duration-500 group cursor-pointer relative overflow-hidden flex flex-col justify-between min-h-[160px] sm:min-h-[250px] md:min-h-[350px] flex-shrink-0 w-full shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] border-t border-l border-white/80 dark:border-white/10 border-b-4 border-r-4 border-black/5 dark:border-black/40 hover:-translate-y-2 hover:border-amber-500/30 dark:hover:border-amber-500/30 hover:shadow-[0_20px_40px_rgba(255,138,0,0.15)] ${spanClass}`}'

content = re.sub(old_card_class, new_card_class, content)

# Remove the whileHover properties that conflict since we handle hover in Tailwind
# whileHover={{ y: -10, scale: 1.02, boxShadow: "0 20px 40px rgba(0,0,0,0.1), 0 0 20px rgba(255,138,0,0.2)" }}
content = re.sub(
    r'whileHover=\{\{\s*y:\s*-10,\s*scale:\s*1.02,\s*boxShadow:\s*"[^"]+"\s*\}\}',
    r'',
    content
)

# Replace icon wrapper
old_icon_wrapper = """              <div className="mb-2 sm:mb-4 md:mb-8 p-2 sm:p-4 md:p-6 rounded-[12px] sm:rounded-[22px] glass-icon w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/30 blur-xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                <Icon className="w-5 h-5 sm:w-8 sm:h-8 md:w-10 md:h-10 text-black dark:text-white group-hover:text-amber-500 transition-colors drop-shadow-sm relative z-10" />
              </div>"""

new_icon_wrapper = """              <div className="mb-4 sm:mb-6 md:mb-8 p-3 sm:p-4 md:p-5 rounded-2xl bg-gradient-to-br from-white dark:from-[#222] to-gray-50 dark:to-[#111] border-t border-l border-white/80 dark:border-white/10 border-b-2 border-r-2 border-black/5 dark:border-black/40 shadow-lg w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/20 blur-xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                <Icon className="w-6 h-6 sm:w-8 sm:h-8 md:w-10 md:h-10 text-amber-500 group-hover:text-amber-400 transition-colors relative z-10 drop-shadow-md" />
              </div>"""

content = content.replace(old_icon_wrapper, new_icon_wrapper)


with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

