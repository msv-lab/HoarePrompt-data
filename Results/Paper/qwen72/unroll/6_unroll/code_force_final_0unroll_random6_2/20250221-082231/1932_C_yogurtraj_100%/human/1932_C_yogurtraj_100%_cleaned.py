for ii in range(int(input())):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    t = input()
    l = t.count('L')
    k = 0
    q1 = 0
    q2 = 0
    if t[-1] == 'L':
        k = a[l - 1] % m
        q1 = l - 2
        q2 = l
    else:
        k = a[l] % m
        q1 = l - 1
        q2 = l + 1
    y = [0] * n
    y[-1] = k
    for i in range(n - 2, -1, -1):
        if t[i] == 'R':
            k = k * a[q2] % m
            q2 += 1
        else:
            k = k * a[q1] % m
            q1 -= 1
        y[i] = k
    print(*y)