import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

# Read input
n = int(input())
a = list(map(int, input().split()))

# Initialize result array and the count of added elements
result = [a[0]]
count = 0

# Iterate through the array to check adjacent pairs
for i in range(1, n):
    if not is_coprime(result[-1], a[i]):
        # Insert a number to make the pair co-prime
        # We can always insert 1 because 1 is co-prime with any number
        result.append(1)
        count += 1
    result.append(a[i])

# Print the results
print(count)
print(" ".join(map(str, result)))
