from bisect import bisect_left
t = int(input())
 
for _ in range(t):
    n, k, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    ad = [0]
    bd = [0]
    for i in range(1, len(a)):
        ad.append(a[i]-a[i-1])
    for i in range(1, len(b)):
        bd.append(b[i]-b[i-1])
    v = [0]
    for i in range(1,len(a)):
        v.append(ad[i]/bd[i])    
    for l in range(q):
        m = 0
        i = 1
        ql = int(input())
        s = bisect_left(a, ql)
        if a[s] == ql:
            print(b[s], end=' ')
            continue
        ql -= a[s-1]
        m += b[s-1]
        m += bd[s] * ql/ad[s]
        print(int(m), end=' ')
    print()