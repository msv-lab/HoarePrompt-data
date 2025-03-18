MOD = 1000000007
T = int(input())
for _ in range(T):
    (n, p, k) = map(int, input().split())
    S = 0
    for i in range(p):
        S += int(input().split()[2])
    C = n * (n - 1) // 2
    num = p * k * k - p * k + 2 * k * C * S
    den = 2 * C * C
    g = math.gcd(num, den)
    num = num // g
    den = den // g
    den = pow(den, -1, MOD)
    ans = num * den % MOD
    print(ans)