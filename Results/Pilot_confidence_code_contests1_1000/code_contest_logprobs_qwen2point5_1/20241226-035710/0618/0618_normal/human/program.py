from __future__ import division, print_function

def main():
    a, b, c, d = input_as_list()
    s1 = b-a
    s2 = c-d
    if s1 == s2:
        out = [1, 0]*a + [1, 2]*(b-a) + [3, 2]*d
    elif s1+1 == s2:
        if a > 0:
            a -= 1
            out = [0] + [1, 0]*a + [1, 2]*(b-a) + [3, 2]*d
        else:
            c -= 1
            out = [2] + [1, 0]*a + [1, 2]*(b-a) + [3, 2]*d
    elif s1 == s2+1:
        if d > 0:
            d -= 1
            out = [1, 0]*a + [1, 2]*(b-a) + [3, 2]*d + [3]
        else:
            b -= 1
            out = [1, 0]*a + [1, 2]*(b-a) + [3, 2]*d + [1]
    else:
        print("NO")
        return
    print("YES")
    print(*out)

INF = float('inf')
MOD = 10 ** 9 + 7
__interactive = False

import os, sys
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

mulmod = __pypy__.intop.int_mulmod

if "LOCAL_" in os.environ:
    debug_print = print
else:
    if not __interactive:
        sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
        sys.stdout = BytesIO()
        register(lambda: os.write(1, sys.stdout.getvalue()))

        input = lambda: sys.stdin.readline().rstrip('\r\n')
    else:
        flush = sys.stdout.flush
    debug_print = lambda *x, **y: None


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def input_as_list():
    return list(map(int, input().split()))

def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

def range_with_count(start, step, count):
    return range(start, start + step * count, step)

def indices(l, start=0, end=0):
    return range(start, len(l)+end)

def ceil_power_of_2(n):
    return 2 ** ((n - 1).bit_length())

def ceil_div(x, r):
    return (x + r - 1) // r

main()