import urllib.request
import re

url = "https://collection.cloudinary.com/ozd726ro/a998b2ca26105e0c043b9c2672fb4a86"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
except Exception as e:
    print(e)
