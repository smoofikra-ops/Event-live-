import urllib.request
import re
import json

url = "https://collection.cloudinary.com/ozd726ro/a998b2ca26105e0c043b9c2672fb4a86"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print("Fetched HTML length:", len(html))
        # Look for window.__INITIAL_STATE__ or similar JSON data
        match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\});', html)
        if match:
            print("Found state!")
        else:
            print("Could not find state in HTML.")
            # print some of it
            print(html[:1000])
except Exception as e:
    print("Error:", e)

