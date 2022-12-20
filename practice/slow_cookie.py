#한 줄에 여러 개의 숫자를 입력받는다 그 후 역순으로 그 숫자들을 하나씩 출력한다 

p = input()
s = []
p.split()
for i in range(0, len(p)):
  if p[i] != ' ':
    s.append(p[i])
  else:
    pass
s.reverse()
print(s)
