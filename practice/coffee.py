customer = "손님"
index = 7 
while index > 0:
  print("{0} 커피 완료되었습니다, 호출 {1} 번 남았어요".format(customer, index))
  index = index - 1
  if index == 0:
    print("호출이 expire 되었습니다.")
