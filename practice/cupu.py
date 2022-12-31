for i in range(20):
    for j in range(20 - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(20):
    print("{:^40}".format("*" * (2 * i + 1)))
