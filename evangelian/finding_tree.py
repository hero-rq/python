import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def finding_answer():
    n = int(input())
    s = 0  # Initialize 's' outside the loop
    for _ in range(n):
        k = int(input())
        if is_prime(k):  # No need to compare with True
            s += 1
    print(s)        
        
finding_answer()
