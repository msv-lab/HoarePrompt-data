import math

def k_rounding(n, k):
    # Calculate the minimum number that ends with at least k zeros
    multiplier = 10**k
    # Find the smallest number x that is a multiple of n and also ends with k zeros
    x = (n * (multiplier // math.gcd(n, multiplier)))
    return x

# Read input
n, k = map(int, input().split())
# Print the k-rounding of n
print(k_rounding(n, k))
