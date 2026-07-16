import re

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

new_reviews = """const mockReviews = [
  { author: "Mohammed", text: "خدمة احترافية بمعنى الكلمة! تعاملت مع \\"ايفنت لايف\\" بقيادة الأستاذ سامر العبسي، وكان التعامل راقٍ جدًا والتنظيم ممتاز. التغطية كانت بجودة عالية سواء في التصوير الفوتوغرافي أو الفيديو، وكل التفاصيل كانت مدروسة بعناية. أنصح أي شخص يبحث عن توثيق احترافي لأي مناسبة يتواصل معهم بدون تردد" },
  { author: "محمد عبده الحطامي", text: "كل الشكر والتقدير لطاقم ايفنت لايف مبدعين و متميزين" },
  { author: "abdalkrim abdalkrim", text: "ممتاز جداً ملابس جديده ووحدات تصوير كامله باحدث الاجهزة والكامرات انصحكم به وتجربته بقياده الاخ صلاح الصنعاني" },
  { author: "Sweed R", text: "شغل ممتاز وشباب نشيطين وسعر معقول بالنسبه للشغل انصح فيهم 👍🏽👍🏽" }
];"""

content = re.sub(
    r"const mockReviews = \[.*?\];",
    new_reviews,
    content,
    flags=re.DOTALL
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)
