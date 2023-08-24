n = int(input())
mod = 1000000007

# Calculate the number of pairs of permutations
result = ((n+1)**n % mod - (n**n) % mod) % mod

print(result)