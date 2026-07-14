import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

filter_code = """  const filteredWorks = works.filter(w => {
    if (activeCategory === 'portfolio.all') return true;
    const catMap: Record<string, string> = {
      'portfolio.photography': 'تصوير',
      'portfolio.video': 'فيديو',
      'portfolio.livestream': 'بث مباشر'
    };
    return w.category === catMap[activeCategory];
  });"""

content = re.sub(r'const filteredWorks = activeCategory === \'الكل\' \? works : works\.filter\(w => w\.category === activeCategory\);', filter_code, content)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

