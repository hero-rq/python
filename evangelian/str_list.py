#1부터 100까지 쭉 각 자릿수를 그대로 더하는 프로그램 작성 
s = 0
def add_digits(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

for i in range(1, 101):
  s += add_digits(i)

print(s)
print(str(list(range(1, 101))))
