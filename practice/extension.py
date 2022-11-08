#무한 echo 프로그램 
#> 일반적인 문자열 입력 -> 해당 내용 3번 반복 출력 
#> help 입력 -> 'echo를 해주는 프로그램임' 출력
#> quit 입력하면 '종료할거임? (Y/n)' 출력
#> 위 질문에서 Y를 입력하면 종료, n을 입력하면 계속 실행 

while(1):
  x = input()
  if x == 'help':
    print('It is made for echo')
    continue

  if x == 'quit':
    print('You wanna exit?(Y/n)')
    z = input()
    if z == 'Y':
      break
    else:
      continue

  y = x + x + x
  print(y)
