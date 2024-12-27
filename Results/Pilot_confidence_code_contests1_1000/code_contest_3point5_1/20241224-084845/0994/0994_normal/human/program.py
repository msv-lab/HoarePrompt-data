from __future__ import division, print_function

def main():
    from bisect import bisect_left
    INF = 200001
    n, m, k, q = input_as_list()
    
    grid = dict()
    for _ in range(k):
        r, c = input_as_list()
        if r not in grid:
            grid[r] = [c, c]
        else:
            grid[r][0] = min(grid[r][0], c)
            grid[r][1] = max(grid[r][1], c)
        
    b = input_as_list()
    b.sort()
    
    g = list(grid.items())
    g.sort()
    
    def f(l, r):
        if l > r: l, r = r, l
        
        lb = bisect_left(b, l)
        rb = bisect_left(b, r)
        
        if lb < rb:
            return r - l
        else:
            left, right = INF, INF
            if lb > 0:
                left = l - b[lb-1]
            if rb < len(g):
                right = b[rb] - r
            
            return r - l + 2*min(left, right)
        
    L, R = 0, 0
    Lpos, Rpos = 1, 1
    curlv = 1
    for lv, bd in g:
        l, r = bd
        
        if lv == 1:
            L = 2*r - l - 1
            R = r - 1
            Lpos = l
            Rpos = r
            continue
        
        R_ = min(f(Lpos, l)+L, f(Rpos, l)+R) + (lv - curlv) + (r - l)
        L_ = min(f(Lpos, r)+L, f(Rpos, r)+R) + (lv - curlv) + (r - l)
        
        L, R = L_, R_
        Lpos = l
        Rpos = r
        curlv = lv
    
    print(min(L, R))
        
    
    
    

INF = float('inf')
MOD = 10**9 + 7

import os, sys
from atexit import register
from io import BytesIO
import itertools

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

if "LOCAL_" in os.environ:
    debug_print = print
else:
    sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
    sys.stdout = BytesIO()
    register(lambda: os.write(1, sys.stdout.getvalue()))

    input = lambda: sys.stdin.readline().rstrip('\r\n')
    debug_print = lambda *x, **y: None


def input_as_list():
    return list(map(int, input().split()))

def array_of(f, *dim):
    return [array_of(f, *dim[1:]) for _ in range(dim[0])] if dim else f()

main()