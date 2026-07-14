import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Let's replace the icon wrapper using regex
content = re.sub(
    r'<div className="mb-2 sm:mb-4 md:mb-8 p-2 sm:p-4 md:p-6 rounded-\[12px\] sm:rounded-\[22px\] glass-icon w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">.*?</div>\s*<Icon',
    r'''<div className="mb-4 sm:mb-6 md:mb-8 p-3 sm:p-4 md:p-5 rounded-2xl bg-gradient-to-br from-white dark:from-[#222] to-gray-50 dark:to-[#111] border-t border-l border-white/80 dark:border-white/10 border-b-2 border-r-2 border-black/5 dark:border-black/40 shadow-lg w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/20 blur-xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                <Icon''',
    content,
    flags=re.DOTALL
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

