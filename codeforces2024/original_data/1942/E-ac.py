mod = 998244353
N = 10**6 + 10
fc = [0] * N  # Array to store factorials
ifc = [0] * N  # Array to store inverse factorials

def inv(x):
    # Function to compute modular inverse using Fermat's Little Theorem
    p = mod - 2
    ans = 1
    res = x
    while p:
        if p & 1:
            ans = (ans * res) % mod
        res = (res * res) % mod
        p >>= 1
    return ans

def init():
    # Precompute factorials and inverse factorials
    n = N - 5
    fc[0] = 1
    for i in range(1, n + 1):
        fc[i] = (fc[i - 1] * i) % mod
    ifc[n] = inv(fc[n])
    for i in range(n - 1, -1, -1):
        ifc[i] = (ifc[i + 1] * (i + 1)) % mod

def C(n, m):
    # Function to compute combinations n choose m
    if n < m:
        return 0
    if m == 0:
        return 1
    return (fc[n] * ifc[n - m] * ifc[m]) % mod

def solve():
    l, n = map(int, input().split())

    # Calculate total configurations
    ans = C(l, 2 * n)
    for x in range(0, l - 2 * n + 1, 2):
        # Subtract configurations where FJ cannot win
        ans -= (C(x // 2 + n - 1, n - 1) * C(l - x - n, n)) % mod
        ans %= mod
    # Multiply by 2 for both initial configurations
    print((2 * ans) % mod)

init()

T = int(input())
for _ in range(T):
    solve()