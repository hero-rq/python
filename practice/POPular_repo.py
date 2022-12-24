data = input().split()
data_set = list(data)
count = 0
for i in range(0, 3):
    max_number = max(data_set)
    while max_number in data_set:
        data_set.remove(max_number)
        count += 1
print(count)
