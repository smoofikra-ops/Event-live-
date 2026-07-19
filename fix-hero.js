import fs from 'fs';
let code = fs.readFileSync('src/CustomHeroSequence.tsx', 'utf-8');

// Fix 1: change w-full sm:w-auto to just w-auto
code = code.replace(/className="text-gradient w-full sm:w-auto"/g, 'className="text-gradient w-auto"');

// Fix 2: adjust font sizes on mobile
// Main heading text-[20px] -> text-[18px] sm:text-[28px]
code = code.replace(/text-\[20px\] sm:text-\[32px\] md:text-\[44px\]/g, 'text-[18px] sm:text-[28px] md:text-[44px]');

// Subheadings text-[13px] -> text-[12px]
code = code.replace(/text-\[13px\] sm:text-\[16px\] md:text-\[20px\]/g, 'text-[12px] sm:text-[16px] md:text-[20px]');

// also, prevent min-height from taking too much space on mobile
code = code.replace(/min-h-\[60px\] sm:min-h-\[100px\]/g, 'min-h-[40px] sm:min-h-[80px]');
code = code.replace(/min-h-\[60px\] sm:min-h-\[90px\]/g, 'min-h-[40px] sm:min-h-[80px]');

// and the subtitle margin
code = code.replace(/mb-8 sm:mb-12/g, 'mb-4 sm:mb-8');

fs.writeFileSync('src/CustomHeroSequence.tsx', code);
