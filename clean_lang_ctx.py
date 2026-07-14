import re

with open("src/LanguageContext.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Let's extract the `ar: { ... }` block and `en: { ... }` block and remove duplicate keys by building a dict and then regenerating the string.

def remove_duplicates_from_block(match):
    block = match.group(0)
    lines = block.split('\n')
    
    seen_keys = set()
    new_lines = []
    
    # Process lines backwards to keep the last defined key (which is our new addition, wait, our new addition was added to the top of the block? Let's check.)
    # In `add_translations.py` I did: content.replace("ar: {", "ar: {" + ar_additions)
    # So the new ones are at the top. This means we want to keep the TOP ones, not the BOTTOM ones!
    
    for line in lines:
        m = re.search(r"'([^']+)'\s*:", line)
        if m:
            key = m.group(1)
            if key in seen_keys:
                continue # Skip duplicate
            seen_keys.add(key)
        new_lines.append(line)
        
    return '\n'.join(new_lines)

# Apply this to the ar: and en: blocks. They are nested, but maybe we can just do a simpler search:
lines = content.split('\n')
ar_start = -1
en_start = -1
for i, line in enumerate(lines):
    if "ar: {" in line:
        ar_start = i
    elif "en: {" in line:
        en_start = i

def process_block(start_idx, end_idx):
    seen = set()
    result = []
    for i in range(start_idx, end_idx):
        line = lines[i]
        m = re.search(r"'([^']+)'\s*:", line)
        if m:
            key = m.group(1)
            if key in seen:
                continue
            seen.add(key)
        result.append(line)
    return result

# Find end of en block:
# It's right before '};' at the end of the file or similar.
# Actually, let's just do it cleanly:
new_lines = []
in_ar = False
in_en = False
ar_seen = set()
en_seen = set()

for line in lines:
    if line.strip().startswith('ar: {'):
        in_ar = True
        in_en = False
        new_lines.append(line)
        continue
    elif line.strip().startswith('en: {'):
        in_en = True
        in_ar = False
        new_lines.append(line)
        continue
    elif line.strip().startswith('};'):
        in_ar = False
        in_en = False
        new_lines.append(line)
        continue
    elif line.strip() == '},':
        in_ar = False
        in_en = False
        new_lines.append(line)
        continue

    m = re.search(r"'([^']+)'\s*:", line)
    if m:
        key = m.group(1)
        if in_ar:
            if key in ar_seen:
                continue
            ar_seen.add(key)
        elif in_en:
            if key in en_seen:
                continue
            en_seen.add(key)
            
    new_lines.append(line)

with open("src/LanguageContext.tsx", "w", encoding="utf-8") as f:
    f.write('\n'.join(new_lines))

