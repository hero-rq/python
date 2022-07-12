import sys
n = int(sys.stdin.readline())

k = [0]*10001

for i in range(n):
    b = int(sys.stdin.readline())
    k[b] += 1 

for i in range(10001): 
  if k[i] != 0:
    for j in range(k[i]):
        print(i)
