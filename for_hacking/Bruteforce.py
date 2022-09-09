import itertools

numbers = '0123456789'

#for i in numbers:
#    for j in numbers:
#        print(i+j)

for length in range(1, 5):
    for password in itertools.product(numbers, repeat=length):
        #print(password)        
        print(''.join(password))
