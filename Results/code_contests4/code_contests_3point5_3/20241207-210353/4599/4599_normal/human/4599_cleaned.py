_interactive = False

def func_1():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        print(s[::2])
INF = float('inf')
MOD = 10 ** 9 + 7
alphabets = 'abcdefghijklmnopqrstuvwxyz'
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