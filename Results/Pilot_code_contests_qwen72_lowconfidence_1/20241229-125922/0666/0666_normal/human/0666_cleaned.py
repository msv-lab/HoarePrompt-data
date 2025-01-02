def func_1():
    (n, q) = map(int, stdin.readline().split())
    a = [0] + map(int, stdin.readline().split(), repeat(10, n)) + [0]
    b = [map(int, stdin.readline().split(), (10, 10)) for _ in xrange(q)]
    s = 0
    for i in xrange(1, n + 1):
        if a[i - 1] < a[i] > a[i + 1]:
            s += a[i]
        if a[i - 1] > a[i] < a[i + 1]:
            s -= a[i]
    stdout.write('%d\n' % s)
    if not q:
        return
    ans = [0] * q
    d = 0
    for (i, x) in enumerate(b):
        (l, r) = x
        if r == l:
            ans[i] = d
            continue
        (Ll, L, Lr) = (a[l - 1], a[l], a[l + 1])
        (Rl, R, Rr) = (a[r - 1], a[r], a[r + 1])
        if l > 1:
            if a[l - 2] < Ll > L:
                d -= Ll
            elif a[l - 2] > Ll < L:
                d += Ll
        if Ll < L > Lr:
            d -= L
        elif Ll > L < Lr:
            d += L
        if r - l > 1:
            if a[l + 2] < Lr > L:
                d -= Lr
            elif a[l + 2] > Lr < L:
                d += Lr
        if r - l > 2:
            if a[r - 2] < Rl > R:
                d -= Rl
            elif a[r - 2] > Rl < R:
                d += Rl
        if Rl < R > Rr:
            d -= R
        elif Rl > R < Rr:
            d += R
        if r < n:
            if a[r + 2] < Rr > R:
                d -= Rr
            elif a[r + 2] > Rr < R:
                d += Rr
        (a[l], a[r]) = (a[r], a[l])
        (Ll, L, Lr) = (a[l - 1], a[l], a[l + 1])
        (Rl, R, Rr) = (a[r - 1], a[r], a[r + 1])
        if l > 1:
            if a[l - 2] < Ll > L:
                d += Ll
            elif a[l - 2] > Ll < L:
                d -= Ll
        if Ll < L > Lr:
            d += L
        elif Ll > L < Lr:
            d -= L
        if r - l > 1:
            if a[l + 2] < Lr > L:
                d += Lr
            elif a[l + 2] > Lr < L:
                d -= Lr
        if r - l > 2:
            if a[r - 2] < Rl > R:
                d += Rl
            elif a[r - 2] > Rl < R:
                d -= Rl
        if Rl < R > Rr:
            d += R
        elif Rl > R < Rr:
            d -= R
        if r < n:
            if a[r + 2] < Rr > R:
                d += Rr
            elif a[r + 2] > Rr < R:
                d -= Rr
        ans[i] = d
    stdout.write(''.join(('%d\n' % (s + x) for x in ans)))
T = int(stdin.readline())
for _ in xrange(T):
    func_1()