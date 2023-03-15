import random 
wordlist = ['cookie', 'panda', 'abcd', 'zebra', 'cola']

for word in wordlist:
    k = random.randint(1, 200)
    counter = 0
    while counter < k:
        print(f'{word}{counter}')
        counter = counter + 1
