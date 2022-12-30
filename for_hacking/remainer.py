alice_candies = 121
bob_candies = 77
carol_candies = 109

total_candies = alice_candies + bob_candies + carol_candies
remainder = total_candies % 3

# Calculate the number of candies to smash by subtracting the remainder from 3

if remainder == 0:
    to_smash = 0
else:
    to_smash = 3 - remainder
