#띄어쓰기 게임 
#입력을 받아 띄어쓰기를 기준으로 가장 앞글자들만 모아서 출력한다 

s = input()
k = ''
k += s[0]

for i in range(len(s)):
  if s[i] == ' ':
    if i+1 < len(s):
        k += s[i+1]
      
print(k)
