import sys
from itertools import combinations

n, m = map(int, input().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
arr = []

for i in range(0, m):
  arr.append(words[i])

arr.sort()  
print(arr)
print(list(combinations(arr,n)))
