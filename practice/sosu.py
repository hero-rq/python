n = int(input())

for i in range(1, n):
  if n == 1:
    exit()
  if n % i == 0:
    print(i)
