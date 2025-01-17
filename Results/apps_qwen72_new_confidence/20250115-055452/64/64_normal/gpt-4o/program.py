def count_valid_decks(n, k, cards):
    from math import gcd
    from functools import reduce
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def product(arr):
        return reduce(lambda x, y: x * y, arr, 1)
    
    total_product = product(cards)
    
    if total_product % k != 0:
        return 0
    
    right_product = [1] * (n + 1)
    for i in range(n - 1, -1, -1):
        right_product[i] = right_product[i + 1] * cards[i]
    
    valid_ways = 0
    left_product = 1
    
    for x in range(n):
        if left_product * right_product[x + 1] % k == 0:
            valid_ways += 1
        left_product *= cards[x]
    
    return valid_ways

# Reading input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
cards = list(map(int, data[2:]))

# Calculating and printing the number of valid ways
print(count_valid_decks(n, k, cards))
