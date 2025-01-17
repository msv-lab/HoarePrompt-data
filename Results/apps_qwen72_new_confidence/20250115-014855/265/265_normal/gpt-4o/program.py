MOD = 10**9 + 7

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i % MOD
    return result

def number_of_ways(n, m):
    # Compute factorial(n) and factorial(n-m)
    fact_n = factorial(n)
    fact_n_m = factorial(n - m)
    
    # The number of ways to assign tickets to passengers and ensure no one gets angry:
    # This is computed as 2^m * factorial(n) // factorial(n-m)
    ways = pow(2, m, MOD) * fact_n % MOD * pow(fact_n_m, MOD-2, MOD) % MOD
    
    return ways

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
m = int(data[1])

# Calculate the number of ways
result = number_of_ways(n, m)

# Output the result
print(result)
