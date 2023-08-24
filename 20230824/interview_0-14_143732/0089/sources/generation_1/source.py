n = int(input())

# The number of layers required is equal to the sum of the first N natural numbers.
# We can calculate this sum using the formula (N * (N + 1)) / 2.

layers = (n * (n + 1)) // 2
print(layers)