"""
This file is part of https://github.com/Cheran-Senthil/PyRival.
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

def func_1():
    (b, k) = map(int, input().split())
    a = list(map(int, input().split()))
    n = k % 2
    m = a[-1] % 2
    if n == 1:
        for i in a[:-1]:
            if i % 2 == 1:
                m = not m
    print('odd' if m else 'even')
if __name__ == '__main__':
    func_1()