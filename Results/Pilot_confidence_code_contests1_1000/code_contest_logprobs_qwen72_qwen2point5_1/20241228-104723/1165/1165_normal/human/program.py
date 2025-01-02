#   Author: yumtam
#   Created at: 2020-10-11 02:16

from __future__ import division, print_function
_interactive = False

def main():
    n = int(input())

    def parse(n):
        return [int(c) for c in bin(n)[2:]]

    s = parse(n)

    ans = []
    def padd(a, b):
        ans.append(str(a) + ' + ' + str(b))
        return a + b

    def pxor(a, b):
        ans.append(str(a) + ' ^ ' + str(b))
        return a ^ b

    if s[-2] == 1:
        n2 = padd(n, n)
        n = pxor(n2, n)
        s = parse(n)

    k = len(s)
    pn = n
    for _ in range(k-1):
        pn = padd(pn, pn)

    t = padd(pn, n)
    t = pxor(t, pn)
    base = pxor(t, n)

    for ki in reversed(range(k)):
        pn = n
        for _ in range(ki):
            pn = padd(pn, pn)
            if base & pn == base:
                pn = pxor(pn, base)
        base = pn
        if base & n == base:
            n = pxor(n, base)
            if n == 1:
                break

    print(len(ans))
    print('\n'.join(ans))


# Constants
INF = float('inf')
MOD = 10**9+7

# Python3 equivalent names
import os, sys, itertools
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

# print-flush in interactive problems
if _interactive:
    flush = sys.stdout.flush
    def printf(*args, **kwargs):
        print(*args, **kwargs)
        flush()

# Debug print, only works on local machine
LOCAL = "LOCAL_" in os.environ
debug_print = (print) if LOCAL else (lambda *x, **y: None)

# Fast IO
if (not LOCAL) and (not _interactive):
    from io import BytesIO
    from atexit import register
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))
    input = lambda: sys.stdin.readline().rstrip('\r\n')

# Some utility functions(Input, N-dimensional lists, ...)
def input_as_list():
    return [int(x) for x in input().split()]

def input_with_offset(o):
    return [int(x)+o for x in input().split()]

def input_as_matrix(n, m):
    return [input_as_list() for _ in range(n)]

def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

# Start of external code templates...
# End of external code templates.

main()
