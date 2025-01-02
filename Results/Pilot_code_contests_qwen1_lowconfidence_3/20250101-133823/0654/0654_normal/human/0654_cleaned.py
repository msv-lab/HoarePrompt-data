"""
This file is part of https://github.com/Cheran-Senthil/PyRival.

Copyright 2018 Cheran Senthilkumar all rights reserved,
Cheran Senthilkumar <hello@cheran.io>
Permission to use, modify, and distribute this software is given under the
terms of the MIT License.

"""
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from functools import reduce
    from io import StringIO as stream
    from math import gcd
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

    def gcd(x, y):
        """gcd(x, y) -> int
        greatest common divisor of x and y
        """
        while y:
            (x, y) = (y, x % y)
        return x
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def func_1(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.

    Args:
        sync (bool, optional): The new synchronization setting.

    """
    global input, flush
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda : sys.stdin.readline().rstrip('\r\n')
        sys.stdout = stream()
        register(lambda : sys.__stdout__.write(sys.stdout.getvalue()))
MOD = 998244353

def func_2():
    (n, m, k) = map(int, input().split())
    a = 1
    for i in range(n - 1 - k + 1, n):
        a *= i
        a %= MOD
    b = 1
    for i in range(1, k + 1):
        b *= i
        b %= MOD
    nck = a // b
    print(m * pow(m - 1, k, MOD) * nck % MOD)
if __name__ == '__main__':
    func_1(False)
    func_2()