import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_block = """  const selectedWork = selectedIndex !== null ? filteredWorks[selectedIndex] : null;
  const [activeCategory, setActiveCategory] = useState<string>('portfolio.all');

  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
    const filteredWorks = works.filter(w => {
    if (activeCategory === 'portfolio.all') return true;
    return w.category === activeCategory;
  });"""

new_block = """  const [activeCategory, setActiveCategory] = useState<string>('portfolio.all');

  const categories = ['portfolio.all', 'المعارض', 'حفلات الافتتاح', 'الفعاليات الوطنية', 'المؤتمرات والمهرجانات'];
  const filteredWorks = works.filter(w => {
    if (activeCategory === 'portfolio.all') return true;
    return w.category === activeCategory;
  });
  
  const selectedWork = selectedIndex !== null ? filteredWorks[selectedIndex] : null;"""

content = content.replace(old_block, new_block)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
