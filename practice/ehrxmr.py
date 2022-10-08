a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
s = a + b + c + d
  #print(s)
  #한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력한다.
if s == 1:
  print("A")
elif s == 2:
  print("B")
elif s == 3:
  print("C")
elif s == 4:
  print("D")
else:
  print("E")
