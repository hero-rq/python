p = input()
print(f'p : {p}')

p_list = list(p)
p_list.reverse()

p = ''.join(p_list)
print(f'거꾸로 : {p}')

k = input()
m = ''

for c in k:
  m = c + m

print(m)
