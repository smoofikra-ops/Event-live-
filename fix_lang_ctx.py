import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Since TypeScript complains about object literal having multiple properties, let's keep only the LAST one, or FIRST one.
# Wait, actually, let's just write a script that parses the file, grabs the keys and values, and rewrites the whole thing.
# Better to do a simple string replace for the old keys that were there:
# In `ar`, lines 42 to 78 have the old keys for process, faq, testimonial.
# Let's just find `process.step1.title': 'التواصل والاستشارة'` and delete it.
