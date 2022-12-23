#입력받은 문자열 중에 어떠한 것이 가장 많이 나왔는지 
#그 가장 많이 나온 문자열을 "~이 ~표를 받아 당선되었습니다"로 출력

data = input().split()
data_set = set(data)
data_dict = {}
for key in data:
  data_dict[key] = data.count(key)

print(f'{max(data_dict, key=data_dict.get)}가 {max(data_dict.values())} 표를 받아 당선이 되었습니다')
