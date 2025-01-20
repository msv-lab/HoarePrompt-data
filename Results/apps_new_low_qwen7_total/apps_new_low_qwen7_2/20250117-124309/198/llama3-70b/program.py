import math

MOD = 998244353

def mul(a, b):
    return (a * b) % MOD

def power(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = mul(res, a)
        a = mul(a, a)
        b >>= 1
    return res

def inv(a):
    return power(a, MOD - 2)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 1
for i in range(n):
    cnt = 1
    for j in range(i + 1, n):
        if a[i][0] <= a[j][1]:
            cnt = mul(cnt, a[j][1] - a[i][0] + 1)
    res = mul(res, cnt)

for i in range(n):
    res = mul(res, inv(a[i][1] - a[i][0] + 1))

print(res)
