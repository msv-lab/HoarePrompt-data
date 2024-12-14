MOD = 10**9 + 7

def factorial_mod(n, mod):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % mod
    return result

# Read input
n = int(input())

# Compute the result
if n == 2:
    result = 1
else:
    result = factorial_mod(n-1, MOD)

# Print the result
print(result)
