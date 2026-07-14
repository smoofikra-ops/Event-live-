import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix hamburger button position
content = content.replace("ltr:right-4 rtl:left-4", "left-4 rtl:right-4")
# We'll just use fixed left/right depending on language or just use standard Tailwind.
# Actually, Tailwind v4 supports `ltr:` and `rtl:` but only if `dir` is set.
# Let's just use standard React style or simpler classes.
# Better yet, use `left-0` for AR and `right-0` for EN?
