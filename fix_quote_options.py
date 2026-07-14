import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Fix clientTypes
content = content.replace("const clientTypes = ['جهة حكومية', 'شركة', 'مؤسسة', 'فرد'];", "const clientTypes = [{id: 'gov', name: t('client.gov')}, {id: 'company', name: t('client.company')}, {id: 'org', name: t('client.org')}, {id: 'individual', name: t('client.individual')}];")
content = content.replace("clientTypes.map(type => (", "clientTypes.map(type => (")
content = content.replace("<option key={type} value={type} className=\"text-black dark:text-white bg-white dark:bg-[#222]\">{type}</option>", "<option key={type.id} value={type.name} className=\"text-black dark:text-white bg-white dark:bg-[#222]\">{type.name}</option>")

# Fix eventTypes
content = content.replace("const eventTypes = ['معرض', 'مهرجان', 'مؤتمر', 'فعاليات', 'مناسبات شركات', 'حفل افتتاح', 'مناسبة وطنية', 'تصوير', 'عقاري', 'إعلان', 'حفلة زواج', 'مناسبات شخصية', 'نوع آخر'];", "const eventTypes = [{id: 'exhibition', name: t('event.exhibition')}, {id: 'festival', name: t('event.festival')}, {id: 'conference', name: t('event.conference')}, {id: 'events', name: t('event.events')}, {id: 'corp', name: t('event.corp')}, {id: 'opening', name: t('event.opening')}, {id: 'national', name: t('event.national')}, {id: 'photography', name: t('event.photography')}, {id: 'realestate', name: t('event.realestate')}, {id: 'ad', name: t('event.ad')}, {id: 'wedding', name: t('event.wedding')}, {id: 'personal', name: t('event.personal')}, {id: 'other', name: t('event.other')}];")
content = content.replace("eventTypes.map(type => (", "eventTypes.map(type => (")
content = content.replace("<option key={type} value={type} className=\"text-black dark:text-white bg-white dark:bg-[#222]\">{type}</option>", "<option key={type.id} value={type.name} className=\"text-black dark:text-white bg-white dark:bg-[#222]\">{type.name}</option>")

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
