n, x, pos = map(int, input().split())
MOD = 10**9 + 7

def comb(n, k):
    if k > n - k: k = n - k
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res % MOD

res = comb(pos, x - 1) * comb(n - pos - 1, x)
print(res % MOD)
