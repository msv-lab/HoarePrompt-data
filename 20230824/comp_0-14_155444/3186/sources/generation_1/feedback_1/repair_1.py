# Read input
N, M, K = map(int, input().split())

# Initialize factorials
fact = [1]
for i in range(2, N+1):
    fact.append((fact[-1] * i))

# Calculate the number of ways
ways = fact[N] // (fact[K] * fact[N-K])

print(ways % (10**6 + 7))