import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# QuoteModal updates
old_quote_wrapper = '<div className="fixed inset-0 z-[300] bg-black/80 flex items-center justify-center p-4">'
new_quote_wrapper = '<div className="fixed inset-0 z-[300] bg-black/80 flex items-center justify-center p-4" onClick={onClose}>'
content = content.replace(old_quote_wrapper, new_quote_wrapper)

old_quote_inner = 'className="bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-2xl p-8 w-full max-w-xl shadow-2xl relative overflow-y-auto max-h-[90vh]"'
new_quote_inner = 'className="bg-white dark:bg-[#111] border border-black/10 dark:border-white/10 rounded-2xl p-8 w-full max-w-xl shadow-2xl relative overflow-y-auto max-h-[90vh]"\n        onClick={(e) => e.stopPropagation()}'
content = content.replace(old_quote_inner, new_quote_inner)

old_quote_close = '<button onClick={onClose} className="absolute top-6 rtl:right-6 ltr:left-6 text-black/50 dark:text-white/50 hover:text-amber-500 transition-colors bg-black/5 dark:bg-white/5 p-2 rounded-full">'
new_quote_close = '<button onClick={onClose} className="absolute top-6 rtl:left-6 ltr:right-6 text-black/50 dark:text-white/50 hover:text-amber-500 transition-colors bg-black/5 dark:bg-white/5 p-2 rounded-full">'
content = content.replace(old_quote_close, new_quote_close)

# AdminPage updates
old_admin_wrapper = '<div className="fixed inset-0 z-[500] bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">'
new_admin_wrapper = '<div className="fixed inset-0 z-[500] bg-black/80 backdrop-blur-sm flex items-center justify-center p-4" onClick={onClose}>'
content = content.replace(old_admin_wrapper, new_admin_wrapper)

old_admin_inner = '<div className="bg-white dark:bg-[#111] rounded-2xl w-full max-w-4xl h-[80vh] flex flex-col shadow-2xl overflow-hidden border border-black/10 dark:border-white/10">'
new_admin_inner = '<div className="bg-white dark:bg-[#111] rounded-2xl w-full max-w-4xl h-[80vh] flex flex-col shadow-2xl overflow-hidden border border-black/10 dark:border-white/10" onClick={(e) => e.stopPropagation()}>'
content = content.replace(old_admin_inner, new_admin_inner)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
