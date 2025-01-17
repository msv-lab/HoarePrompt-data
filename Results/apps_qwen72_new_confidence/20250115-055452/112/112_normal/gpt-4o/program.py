# Read input values for n and k
n, k = map(int, input().split())

# List to store divisors
divisors = []

# Find all divisors of n up to its square root
i = 1
while i * i <= n:
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)
    i += 1

# Sort the divisors in ascending order
divisors.sort()

# Check if k-th smallest divisor exists
if len(divisors) < k:
    print(-1)
else:
    print(divisors[k-1])
