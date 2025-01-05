_interactive = False

def func_1():
    (n, m) = func_2()
    robbers = func_4(n, 2)
    lights = func_4(m, 2)
    rel_lights_x = []
    rel_lights_y = []
    for (rx, ry) in robbers:
        for (lx, ly) in lights:
            (x, y) = (lx - rx, ly - ry)
            if x >= 0 and y >= 0:
                rel_lights_x.append(x)
                rel_lights_y.append(y)
    n = len(rel_lights_x)
    (l, r) = (0, 10 ** 6 + 1)
    avail = [0] * (10 ** 6 + 1 + 1)
    while l < r:
        ans = l + (r - l) // 2
        for i in range(ans + 1):
            avail[i] = 0
        for i in range(n):
            x = rel_lights_x[i]
            y = rel_lights_y[i]
            if x + y >= ans:
                sp = max(0, x - (x + y - ans))
                ep = min(ans, x)
                avail[sp] += 1
                if ep < ans:
                    avail[ep + 1] -= 1
        psum_min = INF
        psum = 0
        for ax in avail:
            psum += ax
            psum_min = min(psum_min, psum)
        if psum_min == 0:
            r = ans
        else:
            l = ans + 1
    print(l)
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