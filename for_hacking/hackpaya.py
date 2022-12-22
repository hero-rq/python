import requests
import re
from bs4 import BeautifulSoup

page_url = 'http://68.183.47.198:30748'

resp = requests.get(page_url)
html = resp.content.decode()
soup = BeautifulSoup(html, "html.parser")
raw_text = soup.get_text()
all_words = re.findall(r'\w+', raw_text)
#print(all_words)
papa = []

for word in all_words:
        papa.append(word)
print(papa)

count={}

for i in papa:
    try: count[i] += 1
    except: count[i]=1
print(count)
