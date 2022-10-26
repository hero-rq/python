#30명의 승객과 매칭 기회가 있을 때, 총 탑승 가능 승객 수 

#조건 1 : 승객별 운행 소요 시간은 5 ~ 30분 사이의 난수
#조건 2 : 소요 시간 5~15분 사이의 승객만 매칭 가능 

#출력 "총 탑승 승객 : 몇 명" 

from random import * 
s = 0
k = [] 
for i in range(0, 30):
  k.append(randrange(5, 31))

for i in range(0, 30):
  if k[i] >= 5 and k[i] <= 15:
    s = s + 1
  elif k[i] < 5 and k[i] > 15:
    s = s

#print(s)
#print(k) 
print("총 탑승 승객 :", s, "명")
