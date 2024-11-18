import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])

max_divisor = gcd
for i in range(1, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        max_divisor = max(max_divisor, i)
        if i * i != gcd:
            max_divisor = max(max_divisor, gcd // i)

print(max_divisor)
