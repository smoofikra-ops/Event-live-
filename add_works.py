import re

urls = """https://drive.google.com/file/d/12LLdo2omfRxTTnWZxEZ1zm0OXV_8a4AL/preview
https://drive.google.com/file/d/14ksSKzvbbzChCUp_HQbJJAUazg9R3nvb/preview
https://drive.google.com/file/d/17stbEtgqVoTMqw-ZF9XLq-WkRcqZXjRz/preview
https://drive.google.com/file/d/1L_fhoUyf3DsJV-Zm_cG7x9-opEKOY1Hd/preview
https://drive.google.com/file/d/1TWqX9bix2n7hjfyOX4xMpvcpa0QLnUtM/preview
https://drive.google.com/file/d/1eOSZ4RacrZwtCD8JW_o6zEC7N7Cpmx3Y/preview
https://drive.google.com/file/d/1iJMWPk5FNJpzD7hZ0OZsQtavTy7Y5-9C/preview
https://drive.google.com/file/d/1ndvNPiH-WplY1W_IUkJi4LDMUJ-Q7frJ/preview
https://drive.google.com/file/d/1-bKKZ4v6ZxXs9lcDtJBSMGFZApj9oKbE/preview
https://drive.google.com/file/d/14Of_YSY1UJUXSQegz5JxDcMQYwIiL-S8/preview
https://drive.google.com/file/d/1Pl6FhnhgKSJt2aU3JJ9siYd1is6ru8JT/preview
https://drive.google.com/file/d/1aIeBp6Mt7Dwvk4xY98PYrblXCqE40vM8/preview
https://drive.google.com/file/d/115Ah5uWJqfEXoG-lFFr-nNZumJ8zKFaG/preview
https://drive.google.com/file/d/1OK5g5z946BAUQvh6JG-KyFmuCUyxVsmm/preview
https://drive.google.com/file/d/1blk2SY4jzFF0qi-be6k7g4w8FhjjGIK0/preview
https://drive.google.com/file/d/12OPuZ6b3J5Lq_khlql_B_Ir2fckfU4C0/preview
https://drive.google.com/file/d/1DQCdGcNndosQy8ZNYQTtdptAOqjhZXRW/preview
https://drive.google.com/file/d/1GXt9db_Yl1MIQZhlBwC4qKCdon-kVesp/preview
https://drive.google.com/file/d/1W5eJg_yFXFYOM_lDq-cqXfaRoUkmWvoM/preview
https://drive.google.com/file/d/1Y4mZXifjPJ6EOUFac2aCA6bdH3gDkrcq/preview
https://drive.google.com/file/d/1coEpY0WT8ItsPlW91tp7p6gI_lKczt5s/preview
https://drive.google.com/file/d/1luJw9fV28M_jwZK1mn4N3bXYcH2A_aML/preview
https://drive.google.com/file/d/13KfsaYPTs6DE5dID6fyQydwCjgCiKHgQ/preview
https://drive.google.com/file/d/1L72tPeWdORgsoZKbJNeCjlBtxFvufnZz/preview
https://drive.google.com/file/d/1AbM9VKcYqVyFMR2pFlygRTX5TgUvrped/preview
https://drive.google.com/file/d/1kBae6J4Y2ep08Yc7PMDkj88yKyHaii8m/preview
https://drive.google.com/file/d/1lLaZESlFXjvxxzz5JvkRMTn8KLugbJfI/preview
https://drive.google.com/file/d/109AkQL1X4IepmrRk_XEPkxuliLAooOrZ/preview
https://drive.google.com/file/d/18r144zqdcZUUmUP_KDGJTbaolej_tWvt/preview
https://drive.google.com/file/d/1C_UylLtxWh5dAu9gR5jnC_XAOy9m0w_9/preview
https://drive.google.com/file/d/1IGu15ZLIvPEvq7d-jRO3dIS9z8m4ImIp/preview
https://drive.google.com/file/d/1I_5y5kyQXOy7fOhL33ruHqcSfa1VAhyv/preview
https://drive.google.com/file/d/1KkhQIBw6Y7x_1rTl6YRRoO2HjKo2AW2q/preview
https://drive.google.com/file/d/1QK6x7CBd8_mi16jhgOt7qClsyyVLFKj9/preview
https://drive.google.com/file/d/1QuHezy4XiPjdOje2FpjvPz2fm3ZQK83E/preview
https://drive.google.com/file/d/1Uxwet14ii7krk42gYQxHHADNVxfaXC_c/preview
https://drive.google.com/file/d/1Y1IHDR5Jzvu79EqEXxX3DT_y-iH_4QLY/preview
https://drive.google.com/file/d/1kHiMH2jkMvypytPWmSOt1d2KQE_bGHyO/preview
https://drive.google.com/file/d/1vRhbTLjyznbr9S0cDsFRKrAP2bNCCO_U/preview
https://drive.google.com/file/d/12YJ0Ve7pMEflWVmc3ShjRqNcvzkdMlWl/preview
https://drive.google.com/file/d/1OYIrmsECCgC19KxerwCXxJZowu2HY9BA/preview
https://drive.google.com/file/d/1hxKa8hgecJt2ziQd0275UvN4sBndxmX6/preview
https://drive.google.com/file/d/1mFXBkq_3AVEW2amc-cNjBCNM_RA_eeso/preview
https://drive.google.com/file/d/1x866FbDXGv04HwdztPuoljJR4uiDjqLQ/preview
https://drive.google.com/file/d/1-qaSg8DfHuqSnyK0EpNUDuNK5idDT0oV/preview
https://drive.google.com/file/d/1I_OnhVKeU2pCxwd46iAt5AqUhg1bpRVI/preview
https://drive.google.com/file/d/1JjjveS8JVim1hNRlvPuewhfKseimYcsT/preview
https://drive.google.com/file/d/1NH8FvcE9wVFubAzpD9HxaPOROmjmRtOC/preview
https://drive.google.com/file/d/1U84IK5Zkz5wDsSw45ga8i-WpPTRxjhwn/preview
https://drive.google.com/file/d/1X62IXzTl9MxGrb4g8PNKxiJefCG7Cy0F/preview
https://drive.google.com/file/d/1hwsPzKr9fSLUJfnXLBeR3dbzJ2IrVyj2/preview
https://drive.google.com/file/d/1y9R8BGNJGos64lOYM8hrfQP0ZlYOcPGv/preview""".split()

with open("src/App.tsx", "r", encoding="utf-8") as f:
    content = f.read()

new_works = []
start_id = 18

for idx, url in enumerate(urls):
    new_id = start_id + idx
    # Default category for new videos could be 'فيديو'
    new_works.append(f'    {{ id: "{new_id}", title: "فيديو", category: "أعمال فيديو", img: "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&q=80&w=800", videoUrl: "{url}" }}')

new_works_str = ",\n".join(new_works)

# find the end of works array
content = re.sub(
    r'(    \{ id: "17", title: "حفل افتتاح", category: "حفلات الافتتاح", img: "https://res.cloudinary.com/ozd726ro/image/upload/v1783983603/%D9%86%D8%B3%D8%AE%D8%A9_%D9%85%D9%86_%D8%A7%D9%81%D8%AA%D8%AA%D8%A7%D8%AD%D8%A7%D8%AA_%D9%85%D8%B7%D8%B9%D9%85_%D8%AD%D8%A7%D8%B4%D9%8A%D9%83%D9%85_zgrbpg.jpg" \}\n  \])',
    f'    {{ id: "17", title: "حفل افتتاح", category: "حفلات الافتتاح", img: "https://res.cloudinary.com/ozd726ro/image/upload/v1783983603/%D9%86%D8%B3%D8%AE%D8%A9_%D9%85%D9%86_%D8%A7%D9%81%D8%AA%D8%AA%D8%A7%D8%AD%D8%A7%D8%AA_%D9%85%D8%B7%D8%B9%D9%85_%D8%AD%D8%A7%D8%B4%D9%8A%D9%83%D9%85_zgrbpg.jpg" }},\n{new_works_str}\n  ]',
    content
)

with open("src/App.tsx", "w", encoding="utf-8") as f:
    f.write(content)

