def quicksort(array):
  if len(array) < 2:
    return array

  pivot = array[0]
  less = []
  greater = []

  for i in array[1:]:
    if i <= pivot:
      less.append(i)
    else:
      greater.append(i)
      
  return quicksort(less) + [pivot] + quicksort(greater)

s = [12, 25, 37, 47, 48, 37, 27, 59]
print(quicksort(s))
