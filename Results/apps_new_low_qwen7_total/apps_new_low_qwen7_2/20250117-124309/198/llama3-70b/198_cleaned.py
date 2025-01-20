MOD = 998244353

def func_1(a, b):
    return a * b % MOD

def func_2(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = func_1(res, a)
        a = func_1(a, a)
        b >>= 1
    return res

def func_3(a):
    return func_2(a, MOD - 2)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 1
for i in range(n):
    cnt = 1
    for j in range(i + 1, n):
        if a[i][0] <= a[j][1]:
            cnt = func_1(cnt, a[j][1] - a[i][0] + 1)
    res = func_1(res, cnt)
for i in range(n):
    res = func_1(res, func_3(a[i][1] - a[i][0] + 1))
print(res)