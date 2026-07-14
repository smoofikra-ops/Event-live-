import * as fs from 'fs';
const content = fs.readFileSync('src/App.tsx', 'utf8');
const lines = content.split('\n');
lines.splice(681, 32); // Removing lines 682 to 713 (0-indexed 681)
fs.writeFileSync('src/App.tsx', lines.join('\n'));
console.log('Done!');
