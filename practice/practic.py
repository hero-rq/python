m = int(input())
n = int(input())
x = 0

def issquare(n):
	temp = n ** 0.5
	if int(temp) == temp:
		if temp ** 2 == n:
			return True
	return False

for i in range(m-1, n+1):
  if issquare(i) == True:
    x += i

if x > 0:
  print(x)
else:
  print(-1)
