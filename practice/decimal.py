#10진수를 입력받아 2진수로 출력 
p = int(input())

def decimal_to_binary(decimal):
    binary = []
    while decimal > 0:
        binary.append(decimal % 2)
        decimal //= 2

    for item in reversed(binary):
      print(item, end="")    

decimal_to_binary(p)      

'''
p = int(input())

s = []
for i in (0, 100):
  s.append(p % 2)
  p = p // 2
  i += 1
  if p == 1:
    s.append(1)
    quit()
  if p == 0:
    quit() 

for item in reversed(s):
    # Print the item without any blank lines
    print(item, end="")   
    
p = int(input())

def decimal_to_binary(decimal):
    return bin(decimal)[2:] 

# Test the function
print(decimal_to_binary(p)) 
'''
