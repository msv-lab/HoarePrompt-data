def power_mod(base, exp, mod):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power_mod(base, exp // 2, mod)
        return (half * half) % mod
    else:
        half = power_mod(base, (exp - 1) // 2, mod)
        return (half * half * base) % mod

# Read input
n, m = map(int, input().split())
MOD = 10**9 + 7

# Calculate the number of ways
result = (power_mod(m, n, MOD) - 1 + MOD) % MOD

# Print the result
print(result)
