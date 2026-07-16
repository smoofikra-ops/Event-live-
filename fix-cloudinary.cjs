const fs = require('fs');
let code = fs.readFileSync('src/App.tsx', 'utf-8');
code = code.replace(/https:\/\/res\.cloudinary\.com\/[^/]+\/image\/upload\/(v[0-9]+\/)/g, (match, v) => {
  return match.replace(v, 'f_auto,q_auto,w_1080/' + v);
});
code = code.replace(/https:\/\/res\.cloudinary\.com\/[^/]+\/video\/upload\/(v[0-9]+\/)/g, (match, v) => {
  return match.replace(v, 'f_auto,q_auto/' + v);
});
fs.writeFileSync('src/App.tsx', code);
