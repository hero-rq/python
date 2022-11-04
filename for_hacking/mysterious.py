import webbrowser

import time


list1 = [

"https://blog.naver.com/PostView.naver?blogId=jarid2292",

"https://jarid2292.tistory.com/1888",

]

url = "https://jarid2292.tistory.com/1888"


chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


webbrowser.get('chrome').open("https://www.google.com")

webbrowser.get('chrome').open(url)

#webbrowser.open("https://jarid2292.tistory.com/1888")


#for url in list1:

# webbrowser.open(url)

# time.sleep(2)
