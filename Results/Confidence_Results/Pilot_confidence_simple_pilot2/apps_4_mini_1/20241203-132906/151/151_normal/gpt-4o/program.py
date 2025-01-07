import math

def find_minimum_tax(n):
    if n % 2 == 0:
        return n // 2
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return n // i
    return 1

# Read input
n = int(input().strip())

# Output the result
print(find_minimum_tax(n))
