#   Template by yumtam
#   Author: babaiserror
#   Created at: 2021-01-25 11:04

from __future__ import division, print_function
_interactive = False

fact = [1]

def mod_mul(a, b):
    return (a*b) % MOD

def mod_fact(n):
    if len(fact) >= n:
        return fact[n-1]
    else:
        i = len(fact) + 1
        while i <= n:
            fact.append(mod_mul(fact[-1],i))
            i += 1
        return fact[-1]

def pow_mod(x, n):
    y = 1
    while n > 0:
        if n % 2:
            y = mod_mul(y,x)
        n = n // 2
        x = mod_mul(x,x)
    return y

def nCr(n, r):
    if n == r: return 1
    return mod_mul(mod_fact(n), pow_mod(mod_mul(mod_fact(r), mod_fact(n-r)), MOD-2))


def main():
    for _ in range(int(input())):
        n,k = input_as_list()
        freq = {}
        A = input_as_list()
        for elem in A:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1

        ans = 0
        for elem in sorted(freq.keys(), reverse=True):
            if freq[elem] < k:
                k -= freq[elem]
            else:
                ans = nCr(freq[elem], k)
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