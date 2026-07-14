import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# We need to change selectedWork to the index in filteredWorks
# and add next/prev functions.
# First, let's see how selectedWork is used.
