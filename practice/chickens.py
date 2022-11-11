#맛있는 치킨집 자동 주문 시스템 
#조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어오면 error로 처리 
 #         "아따 주문이 이상하구망" 출력
#조건 2 : 대기 손님이 주문할 수 있는 하루 총 치킨양은 70마리 
 #          치킨 모두 소진 시 오늘 장사 끝났다고 출력
#소진된 경우 남은만큼만 판다고 가정 

chicken = 70 

while(1):
  print("몇 마리 주문하실라우?")
  x = int(input())
  if x >= 1 or x <=70:
    print("아따 {0} 마리 시키구마잉 곧 가져다 주갔소\n".format(x))
    chicken -= x
    if chicken < 1:
      print("오늘 장사 끝나구마잉 재료가 다 소진되어 부랐소")
      print("아따 {0} 마리 이거라도 드리겠구마잉".format(chicken+x))
      quit()
    else:
      pass
  else:
    print("아따 주문이 이상하구망") 
