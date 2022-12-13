#입력되는 값을 전부 대문자로 출력 (입력 : 소문자, 대문자)
#string = input()
#print(string.upper())

#r = int(input())
#s = r*r*3.14 # r ** 2
#print(s)

x = {1, 2, 3, 4, 5}
print(type(x))
x = set('python')
print(type(x))
x = set(range(6))
print(type(x))
x = set()
print(type(x))

a = {1, 2, 3}
b = {5, 6, 3}
print(a | b)
print(a & b)
print(a - b)
