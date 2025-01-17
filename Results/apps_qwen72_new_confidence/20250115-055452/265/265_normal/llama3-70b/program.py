mod = 10**9 + 7
n, m = map(int, input().split())

res = 1
for _ in range(m):
    res = (res * (n * 2)) % mod
    n -= 1

print(res)
