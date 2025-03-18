import sys
 
MOD = 1000000007
 
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    s = sum(a)
    t, tmp = 0, 0
    for x in a:
        tmp += x
        if tmp < 0:
            tmp = 0
        t = max(tmp ,t)
    ans = ((s + t) % MOD + MOD) % MOD
    for i in range(k - 1):
        t *= 2
        t %= MOD
        ans += t
        ans %= MOD
    print(ans)