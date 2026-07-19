import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const targetStr = `                            <div className="mb-2 sm:mb-4 md:mb-8 p-2 sm:p-4 md:p-6 rounded-[12px] sm:rounded-[22px] bg-gradient-to-br from-white dark:from-[#222] to-gray-50 dark:to-[#111] border-t border-l border-white/80 dark:border-white/10 border-b-2 border-r-2 border-black/5 dark:border-black/40 shadow-lg w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/30 blur-xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                
                <motion.div whileHover={bounceAnimation} animate={{ y: [0, -4, 0] }} transition={{ duration: 4, repeat: Infinity, ease: "easeInOut", delay: i * 0.1 }} className={\`relative z-10 w-6 h-6 sm:w-10 sm:h-10 md:w-14 md:h-14 flex items-center justify-center \${s.cardBgImage ? 'text-white' : 'text-[#111] dark:text-white'}\`}>
                  <Icon className="w-8 h-8 md:w-12 md:h-12" />
                </motion.div>
                {/* Inner Light Reflection */}
                <div className="absolute inset-0 bg-gradient-to-tr from-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 z-20 pointer-events-none rounded-[12px] sm:rounded-[22px]"></div>
              </div>`;

const replacement = `                            <div className="mb-2 sm:mb-4 md:mb-8 w-fit group-hover:scale-110 transition-transform duration-500 relative flex items-center justify-center z-10">
                {/* Glow Effect Behind Icon */}
                <div className="absolute inset-0 bg-amber-500/0 group-hover:bg-amber-500/30 blur-xl transition-all duration-500 rounded-full scale-50 group-hover:scale-150 z-0"></div>
                
                <motion.div whileHover={bounceAnimation} animate={{ y: [0, -4, 0] }} transition={{ duration: 4, repeat: Infinity, ease: "easeInOut", delay: i * 0.1 }} className={\`relative z-10 flex items-center justify-center \${s.cardBgImage ? 'text-white drop-shadow-md' : 'text-amber-500 dark:text-amber-400'}\`}>
                  <Icon className="w-10 h-10 md:w-16 md:h-16" />
                </motion.div>
              </div>`;

code = code.replace(targetStr, replacement);
fs.writeFileSync('src/App.tsx', code);
