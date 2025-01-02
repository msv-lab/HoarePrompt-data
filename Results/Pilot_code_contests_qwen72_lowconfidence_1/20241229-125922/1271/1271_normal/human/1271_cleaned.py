"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
if sys.version_info[0] < 3:

    class dict(dict):
        """dict() -> new empty dictionary"""

        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)

        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)

        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        (x, y) = (y, x % y)
    return x
INP_FILE = 0
OUT_FILE = 1
if sys.version_info[0] < 3:
    sys.stdin = BytesIO(FileIO(INP_FILE).read())
    sys.stdout = BytesIO()
    register(lambda : FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue()))
else:
    sys.stdin = StringIO(FileIO(INP_FILE).read().decode())
    sys.stdout = StringIO()
    register(lambda : FileIO(OUT_FILE, 'w').write(sys.stdout.getvalue().encode()))
input = lambda : sys.stdin.readline().rstrip('\r\n')

def func_2(f):
    """ Memoization decorator for a function taking a single argument. """

    class memodict(dict):

        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return func_2().__getitem__

@memodict
def func_3(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

def func_4():
    n = int(input())
    a = list(map(int, input().split()))
    sa = sum(a)
    ma = min(a)
    res = sa
    for i in range(n):
        if a[i] == ma:
            continue
        for fi in func_3(a[i]):
            res = min(res, sa - ma - a[i] + ma * fi + a[i] // fi)
    print(res)
if __name__ == '__main__':
    func_4()