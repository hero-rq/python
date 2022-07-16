x = input()
s = 0

for i in range(len(x) - 1): 
  if x[i] != x[i+1]:
    s += 1
print((s+1)//2)
