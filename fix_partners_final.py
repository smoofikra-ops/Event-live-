import re
import json

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Replace images
urls = [
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982655/ALJAZIRA_CAPITAL_LOGO_qssrgs.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982666/ALRAJHI_CAPITAL_LOGO_y5vptj.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982645/ARDARA_LOGO_cmkut0.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982656/BADAEL_LOGO_vfxatu.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982648/DIGITAL_GOVERNMENT_AUTHORITY_qaysvp.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982659/INDUSTRIAL_CENTER_LOGO_bb1maq.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982667/INILEVEN_LOGO_wgttos.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982663/MINISTRY_OF_CULTURE_LOGO_o0m8qb.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982698/MINISTRY_OF_HOUSING_LOGO_bwwxcp.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982699/MINISTRY_OF_INDUSTRYAND_MINERAL_RESOURCES_LOGO_zng54u.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982700/MINISTRY_OF_SPORT_LOGO_xx9iub.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982701/MOIA_LOGO_dmz1sd.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982702/MONSHAAT_LOGO_qwnlwh.jpg",
  "https://res.cloudinary.com/ozd726ro/image/upload/v1783982703/NADEC_LOGO_e9tlii.jpg"
]

partners_list = ",\n".join([f"    {{ id: '{i+1}', name: 'Partner {i+1}', logo: '{url}' }}" for i, url in enumerate(urls)])

# Use regex to replace the entire partners array block in the initial state
pattern = re.compile(r'partners:\s*\[\s*\{ id: \'1\'.*?\}\s*\],', re.DOTALL)
replacement = f"partners: [\n{partners_list}\n  ],"
content = pattern.sub(replacement, content)

# Change img className back to object-cover filling the card
content = content.replace(
    'className="w-full h-full object-contain p-2 sm:p-4 relative z-10 transition-transform duration-500 group-hover/card:scale-110"',
    'className="w-full h-full object-cover relative z-10 transition-transform duration-500 group-hover/card:scale-110"'
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

