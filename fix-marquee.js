const fs = require('fs');
let css = fs.readFileSync('src/index.css', 'utf-8');
css = css.replace('animation: marquee 60s linear infinite;', 'animation: marquee 20s linear infinite;');
fs.writeFileSync('src/index.css', css);
