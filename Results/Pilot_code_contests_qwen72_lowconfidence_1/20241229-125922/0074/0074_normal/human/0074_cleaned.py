def func_1():
    import os, sys, atexit
    from cStringIO import StringIO as BytesIO
    sys.stdout = BytesIO()
    atexit.register(lambda : os.write(1, sys.stdout.getvalue()))
    return BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = func_1()
rints = lambda : [int(x) for x in input().split()]
rints_2d = lambda n: [tuple(rints()) for _ in range(n)]
(n, k, s, t) = rints()
(a, g) = (sorted(rints_2d(n), key=lambda x: (x[1], x[0])), sorted(rints()) + [s])
(be, en, ans) = (0, n - 1, float('inf'))
while be <= en:
    md = be + en >> 1
    (fuel, point, time) = (a[md][1], 0, 0)
    for i in range(k + 1):
        dist = g[i] - point
        rem = fuel - dist
        if rem < 0:
            time = float('inf')
            break
        else:
            x = min(dist, rem)
            time += x + (dist - x) * 2
        point = g[i]
    if time > t:
        be = md + 1
    else:
        en = md - 1
        ans = min(ans, a[md][0])
print(-1 if ans == float('inf') else ans)