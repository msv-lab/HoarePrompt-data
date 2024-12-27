from __future__ import division, print_function
__interactive = False

def main():
    def add(x, y):
        return (x+y)%MOD
    n, k = input_as_list()
    a = n-k
    ans = pow(a, n, MOD)
    m = 1
    p = -1
    for i in range(1, a):
        b = pow(a-i, n, MOD)
        m = mulmod(mulmod(m, a-i+1), modinv(i))
        m = mulmod(m, p)
        ans = add(ans, mulmod(m, b))
    lm = 1 if k==0 else 2
    for i in range(n-a+1, n+1):
        lm = mulmod(lm, i)
    for i in range(1, a+1):
        lm = mulmod(lm, modinv(i))
    print(mulmod(ans, lm))


INF = float('inf')
MOD = 998244353
alphabets = 'abcdefghijklmnopqrstuvwxyz'

import os, sys
sys.modules["hashlib"] = sys.sha512 = sys
from atexit import register
from io import BytesIO
import itertools
import __pypy__

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

if "LOCAL_" in os.environ:
    debug_print = print
else:
    if not __interactive:
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda: os.write(1, sys.stdout.getvalue()))

        input = lambda: sys.stdin.readline().rstrip('\r\n')
    debug_print = lambda *x, **y: None

flush = sys.stdout.flush

def mulmod(x, y):
    return __pypy__.intop.int_mulmod(x, y, MOD)

def modinv(x):
    return pow(x, MOD-2, MOD)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def input_as_list():
    return [int(x) for x in input().split()]

def input_with_offset(o):
    return [int(x)+o for x in input().split()]

def input_as_matrix(n, m):
    return [input_as_list() for _ in range(n)]

def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

def range_with_count(start, step, count):
    return range(start, start + step * count, step)

def indices(l, start=0, end=0):
    return range(start, len(l)+end)

def ceil_power_of_2(n):
    """ [0, 1, 2, 4, 4, 8, 8, 8, 8, 16, 16, ...] """
    return 2 ** ((n - 1).bit_length())

def ceil_div(x, r):
    """ = ceil(x / r) """
    return (x + r - 1) // r

main()