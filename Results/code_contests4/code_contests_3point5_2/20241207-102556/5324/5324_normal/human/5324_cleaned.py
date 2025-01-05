"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""

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

def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        (x, y) = (y, x % y)
    return x
range = xrange
filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda : os.write(1, sys.stdout.getvalue()))
input = lambda : sys.stdin.readline().rstrip('\r\n')

def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        dist += abs(pos - prev)
        prev = pos
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        dist += abs(pos - prev)
        prev = pos
    print(dist)
if __name__ == '__main__':
    func_2()