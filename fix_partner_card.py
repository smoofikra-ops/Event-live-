import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the card container classes
# Old: className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-[#111] shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_20px_40px_rgba(255,138,0,0.15)] hover:-translate-y-2 p-4 sm:p-6"
# New: p-4 sm:p-6 is removed, overflow-hidden added if missing (though the image itself can have rounded-2xl)

old_card = r'className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-\[#111\] shadow-\[0_10px_30px_rgba\(0,0,0,0\.05\)\] dark:shadow-\[0_10px_30px_rgba\(0,0,0,0\.5\)\] hover:shadow-\[0_20px_40px_rgba\(255,138,0,0\.15\)\] hover:-translate-y-2 p-4 sm:p-6"'
new_card = r'className="group/card relative mx-3 sm:mx-6 w-32 sm:w-64 h-20 sm:h-36 rounded-2xl flex items-center justify-center transition-all duration-500 cursor-pointer select-none bg-white dark:bg-[#111] shadow-[0_10px_30px_rgba(0,0,0,0.05)] dark:shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:shadow-[0_20px_40px_rgba(255,138,0,0.15)] hover:-translate-y-2 overflow-hidden"'

content = re.sub(old_card, new_card, content)

# Also update the img class
old_img = r'className="w-full h-full object-contain relative z-10 transition-transform duration-500 group-hover/card:scale-110 drop-shadow-sm dark:drop-shadow-\[0_0_15px_rgba\(255,255,255,0\.15\)\]"'
new_img = r'className="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover/card:scale-110"'

content = re.sub(old_img, new_img, content)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

