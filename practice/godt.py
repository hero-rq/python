import requests 
import json

def find_ip():
  address = input()
  url = 'http://ip-api.com/json/'+address
  response = requests.get(url)
  re = json.loads(response.text)
  print(re)

find_ip()
