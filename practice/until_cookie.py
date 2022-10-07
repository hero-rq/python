import requests
import xmltodict
import pandas as pd

for i in range(1, 5):
  url = f'http://openapi.seoul.go.kr:8088/4d7&*&*&*&*&*&*56a61&*&*&*&*&*&*&*&*72526352/xml/tbLn&*&*&*&*&*&*&*sV/1/{i}/'
  #Here_is_Private_token
  content = requests.get(url).content
  dict = xmltodict.parse(content)
  dict.update(dict)
  df = pd.DataFrame(dict)
  
#print(dict)
print(df)
