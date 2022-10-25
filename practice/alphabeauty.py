#1부터 10000까지 8이라는 숫자가 총 몇 번 나오는가? (8이 나올때마다 카운팅) 

s = 0 

for i in range(1, 10000):
  for j in str(i):
    if j == "8":
      s += 1

print(s)
