import urllib.request

try:
    url = "https://api.cloudinary.com/v1_1/ozd726ro/search?expression=collection:a998b2ca26105e0c043b9c2672fb4a86"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
    
try:
    url = "https://api.cloudinary.com/v1_1/ozd726ro/resources/search?expression=collection:a998b2ca26105e0c043b9c2672fb4a86"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
