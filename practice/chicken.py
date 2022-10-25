#30명의 댓글 참여자들 중에 추첨 3명은 치킨, 3명은 피자 

#조건 1 : 30명이 댓글 작성 아이디는 1~30
#조건 2 : 무작위 추첨, 중복 불가 
#조건 3 : random 모듈과 shuffle과 sample을 활용 

from random import * #random 라이브러리를 import 함
random_num = range(1, 31) 

random_num = list(random_num) 

shuffle(random_num) 

win_number = sample(random_num, 6) 

pizza_number = [win_number[0], win_number[1], win_number[2]]
chicken_number = [win_number[3], win_number[4], win_number[5]]
print("피자는 " , pizza_number, "이분들이 get\n" , "치킨은 ", chicken_number, "이분들이 get") 
