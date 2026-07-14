import json

with open('cloudinary_imgs_portfolio.json') as f:
    data = json.load(f)

urls = [u.replace('h_250,fl_preserve_transparency/', '').split('?')[0] for u in data if 'ozd726ro' in u]
for url in urls:
    print(url)
