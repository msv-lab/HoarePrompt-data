x, y = map(int, input().split())
n = int(input())

MOD = 10**9 + 7

if n == 1:
    print(x % MOD)
elif n == 2:
    print(y % MOD)
else:
    a, b = x, y
    for _ in range(3, n + 1):
        a, b = b, (b * 2 - a) % MOD
    print(b)
