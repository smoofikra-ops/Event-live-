import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(
    r'<ul className="flex items-center gap-2 md:gap-4" onMouseLeave=\{\(\) => setHoveredIndex\(null\)\}>.*?</motion\.div>\s*\)\}\s*</li>\s*\)\}\)\}\s*</ul>',
    re.DOTALL
)

new_ul = """<ul className="flex items-center gap-2 md:gap-4" onMouseLeave={() => setHoveredIndex(null)}>
            {navLinks.map((link, idx) => (
              <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
                <a 
                  href={link.href} 
                  className="relative z-10 flex items-center gap-2 px-4 py-2 font-bold text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white transition-colors duration-300 text-sm lg:text-base"
                >
                  {link.icon}
                  {link.label}
                </a>
                {hoveredIndex === idx && (
                  <motion.div
                    layoutId="mercury-desktop-nav"
                    className="absolute inset-0 bg-gradient-to-r from-amber-500/80 to-amber-300/80 dark:from-amber-600/50 dark:to-orange-500/50 rounded-xl -z-0 backdrop-blur-md shadow-[0_0_15px_rgba(255,138,0,0.5)]"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
                  />
                )}
              </li>
            ))}
          </ul>"""

new_content = pattern.sub(new_ul, content, count=1)

if content != new_content:
    with open("src/App.tsx", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Desktop ul fixed!")
else:
    print("Desktop ul pattern not matched.")
