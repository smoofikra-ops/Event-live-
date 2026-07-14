import React, { useState } from 'react';
import { motion } from 'framer-motion';

export const HoverLinkGroup = ({ links }: { links: { label: string, href: string }[] }) => {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <ul className="space-y-2 relative" onMouseLeave={() => setHoveredIndex(null)}>
      {links.map((link, idx) => (
        <li key={idx} className="relative" onMouseEnter={() => setHoveredIndex(idx)}>
          <a href={link.href} className="relative z-10 block px-4 py-2 text-black/60 dark:text-white/60 hover:text-white transition-colors">
            {link.label}
          </a>
          {hoveredIndex === idx && (
            <motion.div
              layoutId="mercury-footer"
              className="absolute inset-0 bg-gradient-to-r from-gray-400 via-gray-300 to-gray-500 dark:from-gray-700 dark:via-gray-600 dark:to-gray-800 rounded-lg -z-0 opacity-80 backdrop-blur-md mix-blend-difference"
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
