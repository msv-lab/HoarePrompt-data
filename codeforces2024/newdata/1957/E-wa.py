# Define the modulo constant
M = 10**9 + 7

# Initialize arrays for precomputation
f = [0] * (10**6 + 1)
g = [0] * (10**6 + 1)

# Precompute f and g arrays
for i in range(2, 10**6 + 1):
    # Compute f[i] using the given formula
    f[i] = (2 * g[i-1] - f[i-1] + 2 * (i-1) + 2) % M
    
    # Compute g[i] as the cumulative sum of f
    g[i] = (g[i-1] + f[i]) % M

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read n for the current test case
    n = int(input())
    
    # Output the precomputed result for n
    print(g[n])