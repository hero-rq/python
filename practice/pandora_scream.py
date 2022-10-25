#아무거나 주세요 
#아무거나 3개 주세요 

from random import * 
random_num = range(0, 10) 
menu = ["chicken", "muffin", "cookie", "sandwiches", "salads", "ice cream", "meat", "vitamin flusher", "codak", "pizza"]

random_num = list(random_num) 

shuffle(random_num) 

in_number = sample(random_num, 3) 

choicesss = [menu[int(in_number[0])], menu[int(in_number[1])], menu[int(in_number[2])]]
chossess = str(choicesss[0]) + ", " + str(choicesss[1]) + ", " + str(choicesss[2])
print(chossess, "주세요")
