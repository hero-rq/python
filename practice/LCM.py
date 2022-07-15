t = int(input())

def GCD(x,y):
	while(y):
		x,y=y,x%y
	return x

def LCM(x,y):
	result = (x*y)//GCD(x,y)
	print(result)

for i in range(1, t+1):
  x, y = map(int, input().split())
  LCM(x, y)
