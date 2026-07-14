import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# 1. TestimonialCard wrapper
# From:
# <div key={index} className="mx-2 sm:mx-4 w-[85vw] sm:w-[50vw] md:w-[40vw] lg:w-[35vw]">
#   <TestimonialCard testimonial={t} />
# </div>
# To:
# <div key={index} className="mx-2 sm:mx-4 w-[85vw] sm:w-[50vw] md:w-[40vw] lg:w-[35vw]" dir={language === 'ar' ? 'rtl' : 'ltr'}>
content = content.replace(
    '<div key={index} className="mx-2 sm:mx-4 w-[85vw] sm:w-[50vw] md:w-[40vw] lg:w-[35vw]">',
    '<div key={index} className="mx-2 sm:mx-4 w-[85vw] sm:w-[50vw] md:w-[40vw] lg:w-[35vw]" dir={language === \'ar\' ? \'rtl\' : \'ltr\'}>'
)

# 2. Contact form email input
# Remove dir="ltr"
content = content.replace(
    'className={`w-full bg-black/5 dark:bg-white/5 border ${errors.email ? \'border-red-500\' : \'border-black/10 dark:border-white/10\'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors text-black dark:text-white focus:bg-white dark:focus:bg-black/40 shadow-sm`} dir="ltr"',
    'className={`w-full bg-black/5 dark:bg-white/5 border ${errors.email ? \'border-red-500\' : \'border-black/10 dark:border-white/10\'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors text-black dark:text-white focus:bg-white dark:focus:bg-black/40 shadow-sm text-start`} dir="auto"'
)

# 3. Contact form phone input
content = content.replace(
    'className={`w-full bg-black/5 dark:bg-white/5 border ${errors.phone ? \'border-red-500\' : \'border-black/10 dark:border-white/10\'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors text-black dark:text-white focus:bg-white dark:focus:bg-black/40 shadow-sm`} dir="ltr"',
    'className={`w-full bg-black/5 dark:bg-white/5 border ${errors.phone ? \'border-red-500\' : \'border-black/10 dark:border-white/10\'} rounded-xl px-4 py-3 focus:outline-none focus:border-amber-500 transition-colors text-black dark:text-white focus:bg-white dark:focus:bg-black/40 shadow-sm text-start`} dir="auto"'
)

# 4. Footer phone and email links
# Replace:
# <a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors" dir="ltr">
# with:
# <a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">
content = content.replace(
    '<a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors" dir="ltr">',
    '<a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">'
)
# And set dir="ltr" on the span
content = content.replace(
    '<span className="font-medium text-sm">+966 50 000 0000</span>',
    '<span className="font-medium text-sm" dir="ltr">+966 50 000 0000</span>'
)

# Replace email link:
content = content.replace(
    '<a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors" dir="ltr">',
    '<a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">'
)
content = content.replace(
    '<span className="font-medium text-sm">info@eventliveksa.com</span>',
    '<span className="font-medium text-sm" dir="ltr">info@eventliveksa.com</span>'
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

