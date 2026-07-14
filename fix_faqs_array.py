import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

faqs_replacement = """  const faqs = [
    { q: t('faq.q1'), a: t('faq.a1') },
    { q: t('faq.q2'), a: t('faq.a2') },
    { q: t('faq.q3'), a: t('faq.a3') },
    { q: t('faq.q4'), a: t('faq.a4') },
    { q: t('faq.q5'), a: t('faq.a5') },
    { q: t('faq.q6'), a: t('faq.a6') },
    { q: t('faq.q7'), a: t('faq.a7') },
    { q: t('faq.q8'), a: t('faq.a8') },
  ];"""

content = re.sub(
    r"  const faqs = \[\s*\{ q: t\('faq\.q1'\), a: t\('faq\.a1'\) \},\s*\{ q: t\('faq\.q2'\), a: t\('faq\.a2'\) \},\s*\{ q: t\('faq\.q3'\), a: t\('faq\.a3'\) \},\s*\{ q: t\('faq\.q4'\), a: t\('faq\.a4'\) \},\s*\];",
    faqs_replacement,
    content,
    flags=re.DOTALL
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
