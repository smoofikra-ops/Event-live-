import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const target = 'className={`flex w-max ${isHovered ? \\'[animation-play-state:paused]\\' : \\'[animation-play-state:running]\\'} animate-marquee-slow py-4`}';
const repl = 'className={`flex w-max ${isHovered || justLeft ? \\'[animation-play-state:paused]\\' : \\'[animation-play-state:running]\\'} animate-marquee-slow py-4`}';

code = code.replace(target, repl);
fs.writeFileSync('src/App.tsx', code);
