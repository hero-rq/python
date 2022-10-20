n = int(input())
s = []
for i in range(1, n+1):
  x, y, z = map(int, input().split())
  d = [] 
  d.append(x)
  d.append(y)
  d.append(z)
  cnt = d.count(x) 
  if d.count(y) > cnt:
    cnt = d.count(y)
  if cnt == 3:
    s.append(10000+x*1000)
  if cnt == 2:
    if x == y:
      s.append(1000+x*100)
    elif y == z:
      s.append(1000+y*100)
    else:
      s.append(1000+z*100)
  if cnt == 1:
    s.append(max(d)*100)
 
print(max(s))
