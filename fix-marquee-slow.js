import fs from 'fs';
let css = fs.readFileSync('src/index.css', 'utf-8');

if (!css.includes('.animate-marquee-slow')) {
  css = css.replace(
    /\\.animate-marquee \\{\\s*animation: marquee 15s linear infinite;\\s*display: flex;\\s*\\}/g,
    \`.animate-marquee {
  animation: marquee 15s linear infinite;
  display: flex;
}
.animate-marquee-slow {
  animation: marquee 40s linear infinite;
  display: flex;
}\`
  );
  fs.writeFileSync('src/index.css', css);
}
