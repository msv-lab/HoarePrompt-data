for s in [*open(0)][1:]:
    (k, x, a) = map(int, s.split())
    if x < k - 1:
        if a >= x + 1:
            print('YES')
        else:
            print('NO')
    elif x == k - 1:
        if a >= x + 2:
            print('YES')
        else:
            print('NO')
    else:
        z = k - 2
        for i in range(x - k + 3):
            z += z // (k - 1) + 1
        if a >= z:
            print('YES')
        else:
            print('NO')