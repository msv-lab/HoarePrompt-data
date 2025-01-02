MOD = 10 ** 9 + 7
INF = float('+inf')
if sys.subversion[0] == 'PyPy':
    import io, atexit
    sys.stdout = io.BytesIO()
    atexit.register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
    sys.stdin = io.BytesIO(sys.stdin.read())
    raw_input = lambda : sys.stdin.readline().rstrip()
pr = lambda *args: sys.stdout.write(' '.join((str(x) for x in args)) + '\n')
epr = lambda *args: sys.stderr.write(' '.join((str(x) for x in args)) + '\n')
die = lambda *args: pr(*args) ^ exit(0)
read_str = raw_input
read_strs = lambda : raw_input().split()
read_int = lambda : int(raw_input())
read_ints = lambda : map(int, raw_input().split())
read_float = lambda : float(raw_input())
read_floats = lambda : map(float, raw_input().split())
'---------------------------------------------------------------'
n = read_int()
arr = read_ints()
res = [arr.pop()]
arr = set(arr)
while arr:
    a = res[0]
    if a % 2 == 0 and a / 2 in arr:
        arr.remove(a / 2)
        res = [a / 2] + res
        continue
    elif a * 3 in arr:
        arr.remove(a * 3)
        res = [a * 3] + res
        continue
    a = res[-1]
    if a % 3 == 0 and a / 3 in arr:
        arr.remove(a / 3)
        res = res + [a / 3]
        continue
    elif a * 2 in arr:
        arr.remove(a * 2)
        res = res + [a * 2]
        continue
pr(*res)