import re
import json

with open("cloudinary_imgs.json", "r") as f:
    images = json.load(f)

# exclude cloudinary logos
valid_images = [img.split("?")[0] for img in images if "ALJAZIRA" in img or "ALRAJHI" in img or "ARDARA" in img or "BADAEL" in img or "DIGITAL" in img or "INDUSTRIAL" in img or "INILEVEN" in img or "MINISTRY" in img or "MOIA" in img or "MONSHAAT" in img or "NADEC" in img]

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

partners_str = "  partners: [\n"
for i, img in enumerate(valid_images):
    partners_str += f'    {{ id: "{i+1}", name: "Partner {i+1}", logo: "{img}" }},\n'
partners_str += "  ],\n"

# add right after socialLinks in INITIAL_DATA
if "socialLinks: [" in content:
    content = content.replace("  socialLinks: [\n", partners_str + "  socialLinks: [\n")
    with open("src/App.tsx", "w", encoding="utf-8") as f:
        f.write(content)
    print("Partners added to INITIAL_DATA")
else:
    print("Could not find socialLinks: [")

