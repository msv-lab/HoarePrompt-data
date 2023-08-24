def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
data = list(map(int, input().split()))

# find all prime factors for each piece of data
prime_factors = []
for d in data:
    factors = []
    for i in range(2, d+1):
        if is_prime(i) and d % i == 0:
            factors.append(i)
    prime_factors.append(factors)

# find maximum revenue using dynamic programming
dp = [0] * (2**N)
for i in range(1, 2**N):
    for j in range(N):
        if (i >> j) & 1:
            dp[i] = max(dp[i], dp[i ^ (1 << j)] + len(set(prime_factors[j])))

print(dp[-1])