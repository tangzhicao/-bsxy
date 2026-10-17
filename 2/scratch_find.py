import urllib.request, re

url = 'https://www.findagrave.com/memorial/140942520/william-james-morrison'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        images = re.findall(r'https://images\.findagrave\.com/[^"\'>\s]+', html)
        for img in set(images):
            print('Find a grave image:', img)
except Exception as e:
    print('Error:', e)
