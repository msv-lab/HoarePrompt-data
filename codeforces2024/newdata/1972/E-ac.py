MOD = 998244353
a = [0] * 200010
b = [0] * 200010
p = [0] * 41
revp = [0] * 41


def lowbit(x):
    return x & -x


def ksm(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = (res * x) % MOD
        x = (x * x) % MOD
        y >>= 1
    return res


def C(x, y):
    ans = 1
    for i in range(x, x - y, -1):
        ans = (ans * i) % MOD
    return (ans * revp[y]) % MOD


def solve():
    n, k = map(int, input().split())
    s = list(map(int, input().strip().split()))
    for i in range(1, n + 1):
        b[i] = s[i - 1]

    for i in range(1, n + 1):
        a[i] = b[i]
        c = 1
        j = i + lowbit(i)
        while j <= n:
            b[j] = (b[j] + MOD - (C(c + k - 1, c) * a[i]) % MOD) % MOD
            c = c + 1
            j = j + lowbit(j)

    for i in range(1, n + 1):
        print(a[i], end=" ")
    print()


p[0] = 1
revp[0] = 1
for i in range(1, 41):
    p[i] = (p[i - 1] * i) % MOD

revp[40] = ksm(p[40], MOD - 2)
for i in range(39, 0, -1):
    revp[i] = (revp[i + 1] * (i + 1)) % MOD

T = int(input().strip())
for _ in range(T):
    solve()
