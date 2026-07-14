import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix sidebar animation logic
old_motion = """      <motion.div
        initial={{ x: language === 'ar' ? "100%" : "-100%" }}
        animate={{ x: isOpen ? 0 : (language === 'ar' ? "100%" : "-100%") }}
        transition={{ type: "spring", damping: 25, stiffness: 200 }}
        className="fixed top-0 bottom-0 ltr:right-0 rtl:left-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-l rtl:border-r rtl:border-l-0 border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl"
      >"""

new_motion = """      <motion.div
        initial={{ x: language === 'ar' ? "-100%" : "100%" }}
        animate={{ x: isOpen ? 0 : (language === 'ar' ? "-100%" : "100%") }}
        transition={{ type: "spring", damping: 25, stiffness: 200 }}
        className="fixed top-0 bottom-0 ltr:right-0 rtl:left-0 w-[280px] bg-white/90 dark:bg-[#0a0a0a]/90 backdrop-blur-3xl z-[95] border-l rtl:border-r rtl:border-l-0 border-black/10 dark:border-white/10 flex flex-col p-6 shadow-2xl"
      >"""

content = content.replace(old_motion, new_motion)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
