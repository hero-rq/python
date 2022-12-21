#어떤 숫자들이 입력되었을 때 그게 오름차순인지 파악 

def is_ascending(numbers):
  for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
      return False
  return True

numbers_str = input("숫자들을 입력해주세요: ")

numbers_str_list = numbers_str.split()

numbers = []
for number_str in numbers_str_list:
  numbers.append(int(number_str))

print(is_ascending(numbers))
