a = 1
b = 1
while (a != 0 and b !=0):
  a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
  if a == 0 or b == 0:
    break
  print(a + b)
