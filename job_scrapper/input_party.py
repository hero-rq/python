#문자열을 입력받으면 총 단어의 갯수를 출력하는 프로그램 

p = input()
count = 0
for i in range(0, len(p)):
  if p[i] == ' ':
    count += 1
print(count+1)    
