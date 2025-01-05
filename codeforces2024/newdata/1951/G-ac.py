MOD = 10**9 + 7
inv_2 = (MOD + 1) // 2
inv_3 = pow(3, MOD - 2, MOD)

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    inv_m = pow(m, MOD - 2, MOD)
    ans = 0
    for i in range(n):
        dist = (a[(i + 1) % n] - a[i]) % m
        prob_last = dist * inv_m % MOD
        expected_getting_moved = n * inv_2 % MOD
        expected_time = (m * m - dist * dist) * inv_3 % MOD
        ans += prob_last * expected_getting_moved % MOD * expected_time % MOD
        ans %= MOD

    print(ans)
