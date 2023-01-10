#괄호 문자열이 양측으로 대칭을 이루는지 파악해보라(짝이 맞느냐) 
#즉 정확히 열고 닫혔는지 yes/no 로 구별

p = input()
m = p.replace(" ", "")
#print(m)
a = 0
b = 0

# (로 시작하지 않는 경우, (가 들어오면 ( 입력되는 만큼 숫자로 받아서 ) 숫자와 비교 일치하면 yes, 아니면 no

for i in range(0, len(m)):
  if m[i] == '(':
    a += 1
  elif m[i] == ')':
    b += 1

print(a, b)
if a == b :
  print('yes')
else:
  print('no')
  

''' stack = []
for i in range(0, len(m)):
    if m[i] == '(':
        stack.append(m[i])
    elif m[i] == ')':
        if not stack:
            print('no')
            exit()
        stack.pop()
if not stack:
    print('yes')
else:
    print('no')
'''
