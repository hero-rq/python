dic = {'kin' : {'korean' : 100, 'panda' : 200}, 'panda' : {'cookie' : 200, 'attack' : 300}}
print(dic)
print('value : ', dic.values())
print('keys : ', dic.keys())
print(dic['panda']['cookie'])
dic['panda']['padora'] = 200
print(dic)

for i in dic.keys():
    print(i, ":", dic[i])
