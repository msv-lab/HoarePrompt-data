import math

def sum_Of_product(n):
    total_sum = 0
    for k in range(n):
        total_sum += math.comb(n, k) * math.comb(n, k + 1)
    return total_sum

# Testing the function with the provided test cases
assert sum_Of_product(3) == 15
assert sum_Of_product(4) == 56
assert sum_Of_product(1) == 1
