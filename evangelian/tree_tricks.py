yeah = "*"
k = int(input())
n = k

for i in range(1, k+1, 2):
  print(" "*(n), yeah*(i), " "*(n))
  n = n-1
