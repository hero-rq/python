#3의 배수인가요? 
#3의 배수이면 'ok' 출력, 3의 배수가 아니라면 입력한 값 그대로 출력 

n = int(input())

if n % 3 == 0:
  print('ok')
else:
  print(n)
