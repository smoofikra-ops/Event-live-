import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace AnimatedTitle class name logic if we want
content = content.replace(
    'text-[40px] font-semibold title-accent-center heading-gradient mb-4',
    'text-2xl sm:text-3xl md:text-[40px] font-semibold title-accent-center heading-gradient mb-4 truncate w-full max-w-full'
)

# And the other h2s
content = content.replace('text-[40px] font-semibold mb-6 title-accent heading-gradient', 'text-2xl sm:text-3xl md:text-[40px] font-semibold mb-6 title-accent heading-gradient truncate w-full max-w-full block')
content = content.replace('text-[32px] md:text-[40px] font-semibold mb-6 title-accent-center heading-gradient', 'text-2xl sm:text-3xl md:text-[40px] font-semibold mb-6 title-accent-center heading-gradient truncate w-full max-w-full block')
content = content.replace('text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent-center heading-gradient', 'text-2xl sm:text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent-center heading-gradient truncate w-full max-w-full block')
content = content.replace('text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent heading-gradient', 'text-2xl sm:text-3xl md:text-[40px] font-semibold mb-6 md:mb-8 title-accent heading-gradient truncate w-full max-w-full block')
content = content.replace('text-3xl font-bold text-center text-black dark:text-white mb-4', 'text-2xl sm:text-3xl md:text-[40px] font-semibold title-accent-center heading-gradient mb-4 truncate w-full max-w-full block text-black dark:text-white')

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
