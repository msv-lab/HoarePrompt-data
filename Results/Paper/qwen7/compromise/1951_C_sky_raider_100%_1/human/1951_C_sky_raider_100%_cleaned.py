for i in range(int(input())):
    (n, m, k) = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    t = 0
    s = 0
    c = 0
    for i in range(n):
        s = min(m, k)
        c += s * (l[i] + t)
        t += s
        k -= s
    print(int(c))