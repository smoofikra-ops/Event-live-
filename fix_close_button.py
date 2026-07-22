import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

# Pattern for the internal close button
internal_btn_pattern = re.compile(r'\s*\{\/\* Floating Clear Close Button \(X\) \*\/\}\s*<button\s*onClick=\{\(e\) => \{ e\.stopPropagation\(\); (setSelectedServiceIndex|setSelectedIndex)\(null\); \}\}\s*className="absolute top-3 right-3[^"]*"\s*title=\{language === \'ar\' \? \'إغلاق\' : \'Close\'\}\s*aria-label="Close"\s*>\s*<X className="w-6 h-6[^"]*" />\s*</button>', re.MULTILINE)

code = internal_btn_pattern.sub('', code)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Removed duplicate internal close buttons.")
