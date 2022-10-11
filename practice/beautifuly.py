n = int(input())
s1 = []
s2 = []
s3 = []

for i in range(1, n+1):
  x, y, z = input().split()
  x = int(x)
  y = int(y)
  z = int(z)
  s1.append(x)
  s2.append(y)
  s3.append(z)

if (sum(s1) > sum(s2) and sum(s1) > sum(s3)):
  print(1, sum(s1))
elif(sum(s2) > sum(s1) and sum(s2) > sum(s3)):
  print(2, sum(s2))
elif(sum(s3) > sum(s1) and sum(s3) > sum(s2)):
  print(3, sum(s3))
elif(sum(s3) == sum(s2) and sum(s3) > sum(s1)):
  if(s3.count(3) > s2.count(3)):
    print(3, sum(s3))
  elif(s3.count(3) < s2.count(3)):
    print(2, sum(s2))
  elif(s3.count(2) > s2.count(2)):
    print(3, sum(s3))
  elif(s3.count(2) < s2.count(2)):
    print(2, sum(s2))
  else:
    print(0, sum(s2))
elif(sum(s1) == sum(s2) and sum(s1) > sum(s3)):
  if(s1.count(3) > s2.count(3)):
    print(1, sum(s1))
  elif(s1.count(3) < s2.count(3)):
    print(2, sum(s2))
  elif(s1.count(2) > s2.count(2)):
    print(1, sum(s1))
  elif(s1.count(2) < s2.count(2)):
    print(2, sum(s2))
  else:
    print(0, sum(s2))
elif(sum(s3) == sum(s1) and sum(s1) > sum(s2)):
  if(s3.count(3) > s1.count(3)):
    print(3, sum(s3))
  elif(s3.count(3) < s1.count(3)):
    print(1, sum(s1))
  elif(s3.count(2) > s1.count(2)):
    print(3, sum(s3))
  elif(s3.count(2) < s1.count(2)):
    print(1, sum(s1))
  else:
    print(0, sum(s1))
else:
  print(0, sum(s2))
