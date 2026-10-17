import urllib.request, re

url = 'https://www.alamy.com/the-fairy-floss-candy-machine-motor-with-casing-removed-made-by-the-general-electric-co-schenectady-new-york-the-fairy-floss-candy-machine-by-the-electric-candy-machine-co-nashville-tennessee-image366299168.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        m = re.findall(r'https://[a-zA-Z0-9\.\-_/]+2CEFGKT[a-zA-Z0-9\.\-_/]*', html)
        for u in set(m):
            print('Found image URL:', u)
except Exception as e:
    print('Error:', e)
