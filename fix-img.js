import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

// Fix the syntax errors
code = code.replace(/\/ loading="lazy">/g, ' loading="lazy" />');

fs.writeFileSync('src/App.tsx', code);
