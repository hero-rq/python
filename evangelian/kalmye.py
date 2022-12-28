# 제한 수를 상수로 설정한다  
# 1~37 내에 무작위로 수를 만든다(무작위 수 하나는 단위 하나로 간주한다) 
# 무작위 수의 합이 제한 수를 넘지 않는 최대의 단위를 구한다
import random

l = 120
k = int(input())
t = []

for i in range(k):
  random_number = random.randint(1, 37)
  t.append(random_number)
  print(random_number)
  
count = 0
s = 0
#print(type(random_number))
for i in range(0, k):
  s += t[i]
  count += 1
  if s == l:
    print(count)
  if s > l:
    count -= 1
    print(count)
    break

'''
import random

l = 120
k = int(input())
t = [random.randint(1, 37) for _ in range(k)]

s = 0
count = 0
for i in t:
    s += i
    if s == l:
        count += 1
        break
    elif s > l:
        break
    count += 1

print(count)'''
