import requests
import json

url = 'http://ip-api.com/json/naver.com'
response = requests.get(url)

a = json.loads(response.text)
print(a)
