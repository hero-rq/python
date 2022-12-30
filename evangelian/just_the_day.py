#2020년 내에 a좌표와 b좌표가 주어진다 (윤년)
#a좌표는 월을 뜻하고 b좌표는 일을 뜻한다 
#각각의 숫자가 주어지면 해당 날짜의 요일을 출력하면 된다 
from datetime import date

a = int(input())
b = int(input())

d = date(2020, a, b)

day_name = d.strftime('%A')
print(day_name)  

'''
import gettext

#just for fun my friend
fr = gettext.translation('myapp', localedir='locale', languages=['fr'])
fr.install()

from datetime import date
d = date(2020, 1, 1)

day_name = fr.gettext(d.strftime('%A'))
print(day_name)
'''
