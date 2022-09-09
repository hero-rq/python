import requests
import json

def find_ip():
    panda = input()
    url = 'http://ip-api.com/json/'+panda
    response = requests.get(url)
    a = json.loads(response.text)
    print(a)

find_ip()    
