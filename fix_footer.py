import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix pointer-events on dynamic background
old_bg = '<div className="absolute inset-0 z-0">'
new_bg = '<div className="absolute inset-0 z-0 pointer-events-none">'
if old_bg in content:
    content = content.replace(old_bg, new_bg, 1) # Only replace the first occurrence (which is in Footer based on the line numbers, wait, there might be others. Let's be precise)

old_footer_bg = """      {/* Dynamic Backgrounds */}
      <div className="absolute inset-0 z-0">"""
new_footer_bg = """      {/* Dynamic Backgrounds */}
      <div className="absolute inset-0 z-0 pointer-events-none">"""
content = content.replace(old_footer_bg, new_footer_bg)

# Ensure contact links have explicit z-10 and pointer-events-auto
old_phone = '<a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">'
new_phone = '<a href="tel:+966500000000" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">'
content = content.replace(old_phone, new_phone)

old_email = '<a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors">'
new_email = '<a href="mailto:info@eventliveksa.com" className="flex items-center gap-3 text-black/60 dark:text-white/60 hover:text-amber-500 transition-colors relative z-10 pointer-events-auto">'
content = content.replace(old_email, new_email)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
