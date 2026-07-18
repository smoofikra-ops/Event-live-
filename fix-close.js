import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

// Services modal close button
code = code.replace(
  `onClick={(e) => { e.stopPropagation(); setSelectedVideo(null); }}
                className="absolute top-4 right-4 rtl:left-4 rtl:right-auto z-50 p-2 bg-black/50 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-colors border border-white/10"`,
  `onClick={(e) => { e.stopPropagation(); setSelectedVideo(null); }}
                className="fixed top-4 right-4 rtl:left-4 rtl:right-auto z-[250] p-2 bg-black/50 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-colors border border-white/10"`
);

// Portfolio modal close button
code = code.replace(
  `onClick={(e) => { e.stopPropagation(); setSelectedIndex(null); }}
              className="absolute top-8 right-8 rtl:right-auto rtl:left-8 text-white hover:text-amber-500 z-[210] p-2 bg-black/50 rounded-full"`,
  `onClick={(e) => { e.stopPropagation(); setSelectedIndex(null); }}
              className="fixed top-4 right-4 rtl:left-4 rtl:right-auto text-white hover:text-amber-500 z-[250] p-2 bg-black/50 rounded-full"`
);

fs.writeFileSync('src/App.tsx', code);
