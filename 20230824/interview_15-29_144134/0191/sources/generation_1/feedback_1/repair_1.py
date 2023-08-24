MOD = 10**9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))

sorted = True
num_zeros = a.count(0)
num_ones = a.count(1)

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            sorted = False

            # Swap elements a[i] and a[j]
            num_zeros += a[i] - a[j]
            num_ones += a[j] - a[i]

p = 0
q = 1

if sorted:
    print(1)
else:
    for i in range(1, num_zeros + num_ones - 1):
        q = (q * i) % MOD

    for i in range(1, num_zeros - 1):
        q = (q * pow(i, MOD - 2, MOD)) % MOD

    p = (num_zeros * (num_zeros - 1) // 2) % MOD

    if p == 0 or q == 0:
        print(0)
    else:
        q_inv = pow(q, MOD - 2, MOD)
        result = (p * q_inv) % MOD
        print(result)