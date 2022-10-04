from random import randint

print("It is random game !")
pc_choice = randint(1, 30)
user_choice = int(input("choose your number : "))
n = 10
while n > 0:
  if user_choice > pc_choice:
    print("sorry it is too big")
    user_choice = int(input("choose your number : "))
  elif user_choice < pc_choice:
    print("it is too small")
    user_choice = int(input("choose your number : "))
  else:
    print("wow you are a number magician")
    user_choice = int(input("choose your number : "))
  n = n - 1  
