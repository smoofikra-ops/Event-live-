import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

old_client = '{clientTypes.map((type, i) => <option key={i} value={type} className="bg-white dark:bg-[#222] text-black dark:text-white">{type}</option>)}'
new_client = '{clientTypes.map((type, i) => <option key={i} value={type.name} className="bg-white dark:bg-[#222] text-black dark:text-white">{type.name}</option>)}'
content = content.replace(old_client, new_client)

old_event = '{eventTypes.map((type, i) => <option key={i} value={type} className="bg-white dark:bg-[#222] text-black dark:text-white">{type}</option>)}'
new_event = '{eventTypes.map((type, i) => <option key={i} value={type.name} className="bg-white dark:bg-[#222] text-black dark:text-white">{type.name}</option>)}'
content = content.replace(old_event, new_event)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
