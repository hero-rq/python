# 자연수가 입력되어지면 소수인지 아닌지 판별 
# 소수가 맞으면 1 소수가 아니면 0 출력 

k = int(input())

for i in range(2, k):
  if k % i == 0:
    print("0")
    break
else:
  print("1")
