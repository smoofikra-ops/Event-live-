import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

appTsx = appTsx.replace(
  'className="glass-card p-8 rounded-2xl w-[350px] mx-4 relative overflow-hidden transition-all duration-300 hover:scale-105 hover:bg-white/10 hover:border-amber-500/30 flex-shrink-0"',
  'className="glass-card p-8 rounded-2xl w-[350px] mx-4 relative overflow-hidden transition-all duration-300 hover:scale-105 hover:bg-white/10 hover:border-amber-500/30 flex-shrink-0" dir="rtl"'
);

fs.writeFileSync('src/App.tsx', appTsx);
console.log('App.tsx RTL fixed!');
