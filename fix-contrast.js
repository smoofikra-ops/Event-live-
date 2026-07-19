import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

// Replace /50 with /70 for better contrast on text
code = code.replace(/text-black\/50 dark:text-white\/50/g, 'text-black/70 dark:text-white/80');

// Replace /60 with /80
code = code.replace(/text-black\/60 dark:text-white\/60/g, 'text-black/80 dark:text-white/90');

// Increase text sizes for subheadings
code = code.replace(/text-base md:text-\[18px\]/g, 'text-lg md:text-xl font-medium');
code = code.replace(/text-\[16px\] md:text-\[18px\]/g, 'text-lg md:text-xl font-medium');
code = code.replace(/text-\[18px\]/g, 'text-lg md:text-xl font-medium');

fs.writeFileSync('src/App.tsx', code);
