T = int(input())
for _ in range(T):
    n = int(input())
    al = list(map(int, input().split()))
    s = 0
    suf = [[0, 0] for _ in range(30)]
    for a in al:
        s ^= a 
        for j in range(30):
            suf[j][s >> j & 1] += 1
    
    ans = 0
    pre = [[0, 0] for _ in range(30)]
    s = 0 
    for a in al:
        for j in range(30):
            pre[j][s >> j & 1] += 1
        hb = len(bin(a)) - 3
        ans += pre[hb][0] * suf[hb][0] + pre[hb][1] * suf[hb][1]
        s ^= a 
        for j in range(30):
            suf[j][s >> j & 1] -= 1
    print(ans)
