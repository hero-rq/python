x = int(input())
lst=list(map(int, input().split()))
max = max(lst)

lst_2 = []
for score in lst:
  lst_2.append(score/max*100)
new_avg = sum(lst_2)/x 
print(new_avg)
