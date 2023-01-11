#공백을 기준으로 숫자열이 주어진다 
#이 숫자열을 재배열하는 것은 허용된다 
#이 숫자열이 연속된 숫자인지 아닌지 yes/no로 구별
'''
num_string = input()
num_list = [int(x) for x in num_string.split()]
#print(num_list)
num_list.sort()
a = min(num_list)
b = max(num_list)
#print(a)
print(num_list)
for s in range(a, b+1):
  if s in num_list:
    s += 1
  else:
    s += 0

if s == (b-a+1):
  print('yes')
else:
  print('no')
'''

num_string = input()
num_list = [int(x) for x in num_string.split()]
#sort the list
num_list.sort()
#find the min and max value
a = min(num_list)
b = max(num_list)
# check if all numbers in the range from min to max are in the list
is_consecutive = all(s in num_list for s in range(a, b+1))
#print the result
if is_consecutive:
    print('yes')
else:
    print('no')
