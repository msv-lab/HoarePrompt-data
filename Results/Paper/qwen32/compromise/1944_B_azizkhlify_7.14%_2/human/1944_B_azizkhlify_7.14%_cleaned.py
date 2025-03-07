for _ in range(int(input())):
    (n, k) = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    l = [0] * n
    r = [0] * n
    re = ul = ur = 0
    res = []
    for i in range(n):
        l[a[i] - 1] += 1
    for i in range(n, 2 * n):
        r[a[i] - 1] += 1
    for i in range(n):
        if l[a[i] - 1] == 2:
            print(a[i], a[i], end=' ')
            ul += 2
        if ul == k * 2:
            break
    k = 2 * k - ul
    if k:
        for i in range(n):
            if l[a[i] - 1] == 1:
                print(a[i], end=' ')
                re += 1
                res.append(a[i])
            if re == k:
                break
    print()
    for i in res:
        print(i, end=' ')
    if ul != ur:
        for i in range(n, 2 * n):
            if r[a[i] - 1] == 2:
                print(a[i], a[i], end=' ')
                ur += 2
            if ul == ur:
                break
    print()