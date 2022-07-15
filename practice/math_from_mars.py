#@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다

t = int(input())
for i in range(t): 
  p = list(map(str, input().split()))
  sum = 0
  for i in range(len(p)):
    if i == 0:
      sum = float(p[i])
    else:
      if p[i] == "@":
        sum = sum * 3
      elif p[i] == "%":
        sum = sum + 5
      elif p[i] == "#":
        sum = sum - 7
        
  print("%0.2f" % sum)
