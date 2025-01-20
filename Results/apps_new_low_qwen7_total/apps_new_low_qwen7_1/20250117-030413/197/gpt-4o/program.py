MOD = 10**9 + 7

def power_mod(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

def expected_dresses(x, k):
    if x == 0:
        return 0
    # Calculate (2^(k+1) - 1) % MOD
    power = power_mod(2, k + 1, MOD)
    result = (x * (power - 1) % MOD) % MOD
    return result

# Read input
import sys
input = sys.stdin.read
x, k = map(int, input().split())

# Print the result
print(expected_dresses(x, k))
