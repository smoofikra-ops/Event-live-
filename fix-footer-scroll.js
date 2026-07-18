import fs from 'fs';
let code = fs.readFileSync('src/App.tsx', 'utf-8');

const oldFooterStart = `        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 md:gap-16 mb-12 relative z-10">`;
const newFooterStart = `        <ScrollReveal className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 md:gap-16 mb-12 relative z-10">`;

const oldFooterEnd = `        </div>

        {/* Decorative elements */}`;
const newFooterEnd = `        </ScrollReveal>

        {/* Decorative elements */}`;

code = code.replace(oldFooterStart, newFooterStart);
code = code.replace(oldFooterEnd, newFooterEnd);
fs.writeFileSync('src/App.tsx', code);
