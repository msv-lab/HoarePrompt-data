import math

# Read input
a, b, x, y = map(int, input().split())

# Reduce the ratio x/y to its irreducible form
g = math.gcd(x, y)
x = x // g
y = y // g

# Calculate the maximum k that satisfies the conditions
max_k = min(a // x, b // y)

# Print the result
print(max_k)
