def func_1():
    for _ in range(int(input())):
        (a, b) = func_3()
        s = list(input())
        s.append('X')
        cnt = 0
        this = 0
        flag = False
        try:
            for c in s:
                if c == 'X' and this > 0:
                    if b <= this < a or a + 4 * b - 1 <= this:
                        raise
                    if 2 * b <= this:
                        if flag:
                            raise
                        flag = True
                        if this < a:
                            raise
                    cnt += 1
                    this = 0
                elif c == '.':
                    this += 1
            print('NO' if cnt % 2 else 'YES')
        except:
            print('NO')
INF = float('inf')
MOD = 10 ** 9 + 7
__interactive = False
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
mulmod = __pypy__.intop.int_mulmod
if 'LOCAL_' in os.environ:
    debug_print = print
else:
    if not __interactive:
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda : os.write(1, sys.stdout.getvalue()))
        input = lambda : sys.stdin.readline().rstrip('\r\n')
    else:
        flush = sys.stdout.flush
    debug_print = lambda *x, **y: None

def func_2(x, y):
    while y:
        (x, y) = (y, x % y)
    return x

def func_3():
    return list(map(int, input().split()))

def func_4(f, *dim):
    return [func_4(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

def func_5(start, step, count):
    return range(start, start + step * count, step)

def func_6(l, start=0, end=0):
    return range(start, len(l) + end)

def func_7(n):
    return 2 ** (n - 1).bit_length()

def func_8(x, r):
    return (x + r - 1) // r
func_1()