from __future__ import division, print_function

def main():
    n, m = input_as_list()
    p = list(range(n))
    r = array_of(int, n)
    def find(v):
        vc = v
        while v != p[v]:
            v = p[v]
        while vc != v:
            p[vc], vc = v, p[vc]
        return v
    def union(u, v):
        u, v = find(u), find(v)
        if u == v: return
        if r[u] < r[v]: u, v = v, u
        p[u] = v
        if r[u] == r[v]: r[u] += 1

    sg = array_of(set, n)
    for _ in range(m):
        x, y = input_with_offset(-1)
        sg[x].add(y)
        sg[y].add(x)

    v = min(range(n), key=lambda i:len(sg[i]))
    for i in range(n):
        if i not in sg[v]:
            union(i, v)
        else:
            for j in range(n):
                if j not in sg[i]:
                    union(i, j)

    roots = set()
    for i in range(n):
        roots.add(find(i))

    print(len(roots)-1)
    

INF = float('inf')
MOD = 10 ** 9 + 7
__interactive = False

import os, sys
sys.modules["hashlib"] = sys.sha512 = sys
from atexit import register
from io import BytesIO
import itertools
#import __pypy__

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

#def mulmod(x, y):
#    return __pypy__.intop.int_mulmod(x, y, MOD)

def modinv(x):
    return pow(x, MOD-2, MOD)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
    
def input_as_list():
    return list(map(int, input().split()))

def input_with_offset(o):
    return list(map(lambda x:int(x)+o, input().split()))
    
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