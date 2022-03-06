def plus(*args):
  result = 0
  for nums in args:
    result += nums 
  print(result)

plus(3, 4, 5, 1, 2, 3, 123)
