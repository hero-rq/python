n = int(input())
s1 = 100
s2 = 100

for i in range(0, n):
  x, y = map(int,input().split())
  if x > y:
    s2 = s2 - x
  elif y > x:
    s1 = s1 - y
  else:
    pass
  i = i + 1 

print(s1, s2, sep = "\n")
