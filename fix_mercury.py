import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# I will add NavLinks with mercury effect
mercury_comp = """
const HoverLinkGroup = ({ links, className = "space-y-4" }: { links: { label: string, href: string }[], className?: string }) => {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <ul className={`relative ${className}`} onMouseLeave={() => setHoveredIndex(null)}>
      {links.map((link, idx) => (
        <li key={idx} className="relative z-10" onMouseEnter={() => setHoveredIndex(idx)}>
          <a href={link.href} className="relative z-10 block px-4 py-2 font-bold text-black/60 dark:text-white/60 hover:text-black dark:hover:text-white transition-colors duration-300">
            {link.label}
          </a>
          {hoveredIndex === idx && (
            <motion.div
              layoutId="mercury-footer"
              className="absolute inset-0 bg-gradient-to-r from-amber-500/80 to-amber-300/80 dark:from-amber-600/50 dark:to-orange-500/50 rounded-lg -z-0 backdrop-blur-md shadow-[0_0_15px_rgba(255,138,0,0.5)]"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ type: "spring", bounce: 0.2, duration: 0.6 }}
            />
          )}
        </li>
      ))}
    </ul>
  );
};
"""

content = content.replace("// --- Components ---", "// --- Components ---\n" + mercury_comp)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

