from __future__ import division, print_function

def main():
    for _ in range(int(input())):
        a, b = input_as_list()
        s = list(input())
        s.append('X')

        cnt = 0
        this = 0
        flag = False
        try:
            for c in s:
                if c == 'X' and this > 0:
                    if b <= this < a or a + 4*b - 1 <= this:
                        raise
                    if 2*b <= this:
                        if flag:
                            raise
                        flag = True
                        if this < a:
                            raise
                    cnt += 1
                    this = 0
                elif c == '.':
                    this += 1
            print("NO" if cnt%2 else "YES")
        except:
            print("NO")

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