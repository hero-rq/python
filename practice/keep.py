n = int(input())
s = 0

for i in range(0, n):
  k = int(input())
  if k == 0:
    s += 0
  elif k == 1:
    s += 1

if s > n/2:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")
