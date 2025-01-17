mod = 1000000009
n, m, k = map(int, input().split())

res = 0
cur = 0
for i in range(m, -1, -1):
    cur += 1
    if cur == k:
        cur = 0
        res = (res * 2 + 1) % mod
    res = (res + 1) % mod

print(res)
