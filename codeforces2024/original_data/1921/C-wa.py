for i in range(int(input())):
    n, f, a, b = map(int, input().split())
    l = list(map(int, input().split()))
    t = min(l[0], b)
    for i in range(n - 1):
        d = (l[i+1] - l[i])*a
        if d < b:
            t += d
        else:
            t += b
    if t < f:
        print('YES')
    else:
        print('NO')