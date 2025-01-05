MOD = 10**9 + 7

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    _sum = 0
    _max = 0

    for i in range(n):
        _sum = max(0, _sum + a[i])
        _max = max(_max, _sum)

    _acc = 0
    for i in range(k):
        _acc += (_acc + _max) % MOD

    print((sum(a) + _acc) % MOD)
