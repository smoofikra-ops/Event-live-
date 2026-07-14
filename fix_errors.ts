import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

// Fix Error 2
appTsx = appTsx.replace(
  '<Navbar onAdminClick={() => setIsAdminOpen(!isAdminOpen)} isAdminMode={isAdminOpen} />',
  '<Navbar onAdminClick={() => setIsAdminOpen(!isAdminOpen)} isAdminMode={isAdminOpen} onQuoteClick={() => setIsQuoteOpen(true)} />'
);

// Fix Error 1
appTsx = appTsx.replace(
  'const TestimonialCard = ({ testimonial }: { testimonial: any }) => {',
  'const TestimonialCard: React.FC<{ testimonial: any }> = ({ testimonial }) => {'
);

fs.writeFileSync('src/App.tsx', appTsx);
console.log('App.tsx errors fixed!');
