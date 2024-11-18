#   Author: yumtam
#   Created at: 2020-09-10 23:03

from __future__ import division, print_function
_interactive = False

def main():
    n, m = input_as_list()
    x, k, y = input_as_list()
    a = input_as_list()
    b = input_as_list()

    j = 0
    for i, ax in enumerate(a):
        if j < m and ax == b[j]:
            j += 1

    if j < m:
        print(-1)
        return

    sa = set(a)
    sb = set(b)
    if sa == sb:
        print(0)
        return

    mx = max(sa-sb)

    gaps = []
    j = 0
    gl = 0
    special = False
    for i, ax in enumerate(a):
        if j < m and ax == b[j]:
            j += 1
            if special:
                specialgap = gl
            gaps.append(gl)
            gl = 0
            special = False
        else:
            if ax == mx:
                special = True
            gl += 1
    if special:
        specialgap = gl
    gaps.append(gl)

    debug_print(gaps)

    if specialgap < k:
        print(-1)
        return

    ans = 0
    if x < y*k:
        for g in gaps:
            ans += x*(g//k) + y*(g%k)
    else:
        for g in gaps:
            ans += y*g

    print(ans)


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
