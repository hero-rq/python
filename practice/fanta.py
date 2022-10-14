import numpy as np

number = []

for i in range(5):
    number.append(int(input()))
number.sort()

val_average = np.average(number)
print(val_average)

val_median = np.median(number)
print(val_median)
