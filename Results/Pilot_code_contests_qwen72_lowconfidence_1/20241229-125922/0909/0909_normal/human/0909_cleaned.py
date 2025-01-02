_interactive = False

def func_1():
    (n, m) = func_2()
    (x, k, y) = func_2()
    a = func_2()
    b = func_2()
    j = 0
    for (i, ax) in enumerate(a):
        if j < m and ax == b[j]:
            j += 1
    if j < m:
        print(-1)
        return
    sa = set(a)
    sb = set(b)
    if sa == sb:
        print(0)
        return
    mx = max(sa - sb)
    gaps = []
    j = 0
    gl = 0
    special = False
    for (i, ax) in enumerate(a):
        if j < m and ax == b[j]:
            j += 1
            if special:
                specialgap = gl
            gaps.append(gl)
            gl = 0
            special = False
        else:
            if ax == mx:
                special = True
            gl += 1
    if special:
        specialgap = gl
    gaps.append(gl)
    debug_print(gaps)
    if specialgap < k:
        print(-1)
        return
    ans = 0
    if x < y * k:
        for g in gaps:
            ans += x * (g // k) + y * (g % k)
    else:
        for g in gaps:
            ans += y * g
    print(ans)
INF = float('inf')
MOD = 10 ** 9 + 7
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
if _interactive:
    flush = sys.stdout.flush

    def printf(*args, **kwargs):
        print(*args, **kwargs)
        flush()
LOCAL = 'LOCAL_' in os.environ
debug_print = print if LOCAL else lambda *x, **y: None
if not LOCAL and (not _interactive):
    from io import BytesIO
    from atexit import register
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda : os.write(1, sys.stdout.getvalue()))
    input = lambda : sys.stdin.readline().rstrip('\r\n')

def func_2():
    return [int(x) for x in input().split()]

def func_3(o):
    return [int(x) + o for x in input().split()]

def func_4(n, m):
    return [func_2() for _ in range(n)]

def func_5(f, *dim):
    return [func_5(f, *dim[1:]) for _ in range(dim[0])] if dim else f()
func_1()