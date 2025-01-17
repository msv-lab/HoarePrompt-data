MOD = 999999893


def inverse(x):
    return pow(x, MOD - 2, MOD)


t = int(input())
for i in range(t):
    n = int(input())

    a = c = (pow(2, n // 2 + 1, MOD) - 2) % MOD
    b = d = (pow(2, (n - 1) // 2 + 1, MOD) - 2) % MOD
    b = (b + 2) % MOD
    ans = (a * d - b * c) * inverse(a * a - 2 * b * b) % MOD
    print(ans)