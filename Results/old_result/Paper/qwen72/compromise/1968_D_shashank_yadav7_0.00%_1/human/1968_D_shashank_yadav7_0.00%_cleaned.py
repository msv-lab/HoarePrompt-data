t = int(input())
for i in range(t):
    (n, k, b, s) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b -= 1
    s -= 1
    sp = a[s]
    bp = a[b]
    bm = a[b] * k
    sm = a[s] * k
    for i in range(n):
        k -= 1
        if k == 0:
            break
        b = p[b] - 1
        s = p[s] - 1
        bm += max(bm, a[b] * k + bp)
        sm += max(sm, a[s] * k + sp)
        sp += a[s]
        bp += a[b]
    if bm > sm:
        print('Bodya')
    elif bm < sm:
        print('Sasha')
    else:
        print('Draw')