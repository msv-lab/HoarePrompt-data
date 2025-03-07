t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    s = input()
    ans = 0
    p = 'ABCDEF'
    hmp = Counter(s)
    for i in p:
        if i not in hmp:
            ans += m
    for i in hmp:
        if hmp[i] < m:
            ans += m - hmp[i]
    print(ans)