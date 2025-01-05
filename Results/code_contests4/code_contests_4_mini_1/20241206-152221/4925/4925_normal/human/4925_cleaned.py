def func_1():
    (n, m) = func_4()
    p = list(range(n))
    r = func_7(int, n)

    def find(v):
        vc = v
        while v != p[v]:
            v = p[v]
        while vc != v:
            (p[vc], vc) = (v, p[vc])
        return v

    def union(u, v):
        (u, v) = (find(u), find(v))
        if u == v:
            return
        if r[u] < r[v]:
            (u, v) = (v, u)
        p[u] = v
        if r[u] == r[v]:
            r[u] += 1
    sg = func_7(set, n)
    for _ in range(m):
        (x, y) = func_5(-1)
        sg[x].add(y)
        sg[y].add(x)
    v = min(range(n), key=lambda i: len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)
    roots = set()
    for i in range(n):
        roots.add(find(i))
    print(len(roots) - 1)
INF = float('inf')
MOD = 10 ** 9 + 7
__interactive = False
sys.modules['hashlib'] = sys.sha512 = sys
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
if 'LOCAL_' in os.environ:
    debug_print = print
else:
    if not __interactive:
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda : os.write(1, sys.stdout.getvalue()))
        input = lambda : sys.stdin.readline().rstrip('\r\n')
    debug_print = lambda *x, **y: None
flush = sys.stdout.flush

def func_2(x):
    return pow(x, MOD - 2, MOD)

def func_3(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_4():
    return list(map(int, input().split()))

def func_5(o):
    return list(map(lambda x: int(x) + o, input().split()))

def func_6(n, m):
    return [func_4() for _ in range(n)]

def func_7(f, *dim):
    return [func_7(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

def func_8(start, step, count):
    return range(start, start + step * count, step)

def func_9(l, start=0, end=0):
    return range(start, len(l) + end)

def func_10(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** (n - 1).bit_length()

def func_11(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r
func_1()