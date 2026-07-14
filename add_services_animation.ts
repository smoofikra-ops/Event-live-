import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

appTsx = appTsx.replace(
  '<motion.div whileHover={bounceAnimation} className="relative z-10 w-10 h-10 md:w-14 md:h-14 flex items-center justify-center">',
  '<motion.div whileHover={bounceAnimation} animate={{ y: [0, -8, 0] }} transition={{ duration: 4, repeat: Infinity, ease: "easeInOut", delay: i * 0.1 }} className="relative z-10 w-10 h-10 md:w-14 md:h-14 flex items-center justify-center">'
);

fs.writeFileSync('src/App.tsx', appTsx);
console.log('Services icon float animation added!');
