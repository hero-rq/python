#입력된 문자열에서 모든 a를 k로 변환하여 출력
'''
p = input()

result = ""
for c in p:
    if c == 'a':
        result += 'k'
    elif c == 'b':
        result += 'n'
    else:
        result += c

print(result)
'''

p = input()

result = ""
for i in range(len(p)):
    if p[i] == 'a':
        result += 'k'
    else:
        result += p[i]

print(result)
