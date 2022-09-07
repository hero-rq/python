b = {'name' : 'John', 'phone' : '0123115', 'email' : 'test@test.com', 'birty' : 11111}
print(b)
print('value : ', b.values())
print('keys : ', b.keys())
print(b['name'])
b['birty'] = 101010
b['city'] = 'Seoul'
print(b)

for i in b.keys():
    print(i, ":", b[i])
