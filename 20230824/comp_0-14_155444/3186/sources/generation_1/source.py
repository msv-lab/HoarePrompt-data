
# Read input
N, M, K = map(int, input().split())

# Initialize factorials
fact = [1]
for i in range(1, N+1):
    fact.append((fact[-1] * i) % (10**6 + 7))

# Calculate the number of ways
ways = (fact[N] * pow((fact[K] * fact[N-K]) % (10**6 + 7), (10**6 + 5), (10**6 + 7))) % (10**6 + 7)

print(ways)