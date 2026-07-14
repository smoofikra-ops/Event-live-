import * as fs from 'fs';

let appTsx = fs.readFileSync('src/App.tsx', 'utf8');

// Colors replacement mapping
const replacements = [
  { from: 'bg-[#050505]', to: 'bg-gray-50 dark:bg-[#050505]' },
  { from: 'bg-[#0a0a0a]', to: 'bg-white dark:bg-[#0a0a0a]' },
  { from: 'bg-[#111]', to: 'bg-gray-100 dark:bg-[#111]' },
  { from: 'bg-[#222]', to: 'bg-gray-200 dark:bg-[#222]' },
  { from: 'text-white', to: 'text-black dark:text-white' },
  { from: 'text-white/50', to: 'text-black/50 dark:text-white/50' },
  { from: 'text-white/70', to: 'text-black/70 dark:text-white/70' },
  { from: 'text-white/80', to: 'text-black/80 dark:text-white/80' },
  { from: 'text-white/40', to: 'text-black/40 dark:text-white/40' },
  { from: 'text-white/20', to: 'text-black/20 dark:text-white/20' },
  { from: 'text-white/10', to: 'text-black/10 dark:text-white/10' },
  { from: 'bg-white/5', to: 'bg-black/5 dark:bg-white/5' },
  { from: 'bg-white/10', to: 'bg-black/10 dark:bg-white/10' },
  { from: 'bg-white/20', to: 'bg-black/20 dark:bg-white/20' },
  { from: 'border-white/5', to: 'border-black/5 dark:border-white/5' },
  { from: 'border-white/10', to: 'border-black/10 dark:border-white/10' },
  { from: 'border-white/20', to: 'border-black/20 dark:border-white/20' },
  { from: 'hover:bg-white/10', to: 'hover:bg-black/10 dark:hover:bg-white/10' },
  { from: 'hover:border-white/20', to: 'hover:border-black/20 dark:hover:border-white/20' },
  { from: 'bg-black/40', to: 'bg-black/40 dark:bg-black/40' },
];

replacements.forEach(({ from, to }) => {
  const parts = appTsx.split(from);
  appTsx = parts.join(to);
});

const themeToggleComponent = `
const ThemeToggle = () => {
  const [isDark, setIsDark] = useState(true);

  useEffect(() => {
    if (document.documentElement.classList.contains('dark')) {
      setIsDark(true);
    } else {
      setIsDark(false);
    }
  }, []);

  const toggleTheme = () => {
    if (isDark) {
      document.documentElement.classList.remove('dark');
      setIsDark(false);
    } else {
      document.documentElement.classList.add('dark');
      setIsDark(true);
    }
  };

  return (
    <button onClick={toggleTheme} className="p-2 rounded-full bg-black/5 dark:bg-white/5 hover:bg-black/10 dark:hover:bg-white/10 transition-colors text-amber-500">
      {isDark ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
    </button>
  );
};
`;

if (!appTsx.includes('ThemeToggle')) {
  appTsx = appTsx.replace(
    'const Navbar = ({ onAdminClick, isAdminMode, onQuoteClick }: { onAdminClick: () => void, isAdminMode: boolean, onQuoteClick: () => void }) => {',
    themeToggleComponent + '\nconst Navbar = ({ onAdminClick, isAdminMode, onQuoteClick }: { onAdminClick: () => void, isAdminMode: boolean, onQuoteClick: () => void }) => {'
  );

  if (!appTsx.includes('Sun,') && !appTsx.includes(' Sun ')) {
    appTsx = appTsx.replace('import { ', 'import { Sun, Moon, ');
  }

  appTsx = appTsx.replace(
    '<button onClick={onQuoteClick}',
    '<ThemeToggle />\n          <button onClick={onQuoteClick}'
  );
}

fs.writeFileSync('src/App.tsx', appTsx);
console.log('App.tsx theme support added!');

let indexHtml = fs.readFileSync('index.html', 'utf8');
if (!indexHtml.includes('class="dark"')) {
  indexHtml = indexHtml.replace('<html lang="ar" dir="rtl">', '<html lang="ar" dir="rtl" class="dark">');
  fs.writeFileSync('index.html', indexHtml);
  console.log('index.html updated with dark class!');
}

let indexCss = fs.readFileSync('src/index.css', 'utf8');
if (!indexCss.includes('.dark .glass-card')) {
  indexCss = indexCss.replace(
    '.glass-card {\n  backdrop-filter: blur(20px);\n  background: rgba(255, 255, 255, 0.06);\n  border: 1px solid rgba(255, 255, 255, 0.1);\n  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);\n}',
    `.glass-card {
  backdrop-filter: blur(20px);
  background: rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
}
.dark .glass-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}`
  );
  fs.writeFileSync('src/index.css', indexCss);
  console.log('index.css glass-card updated!');
}
