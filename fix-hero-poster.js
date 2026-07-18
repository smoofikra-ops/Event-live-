import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

code = code.replace(
  `className="w-full h-full object-cover bg-black"`,
  `poster="https://res.cloudinary.com/ozd726ro/image/upload/f_auto,q_auto,w_1920/v1783983460/%D9%86%D8%B3%D8%AE%D8%A9_%D9%85%D9%86_IMG_9484_siyppe.jpg"
                className="w-full h-full object-cover bg-black"`
);

fs.writeFileSync('src/App.tsx', code);
