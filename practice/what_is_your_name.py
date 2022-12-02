#이름이 주어지면 
# '안녕하세요 저는 ooo입니다'라고 출력 

name = input('본인의 이름을 소개해주세요: ')
age = input('본인 나이를 말해주세요: ')

print('안녕하세요 저는', name,'입니다')
print('안녕하세요 저는', name, '입니다', age, '살이에요')
print('안녕하세요 저는 {}입니다 저는 {}살입니다'.format(name, age))
print(f'안녕하세요 저는 {name + age}입니다')
