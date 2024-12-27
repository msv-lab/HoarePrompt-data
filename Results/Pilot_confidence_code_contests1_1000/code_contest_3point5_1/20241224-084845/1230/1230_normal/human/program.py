from __future__ import division, print_function

def main():
    n = int(input())
    a = input_as_list()
    q = int(input())
    
    h = n.bit_length()
    tb = array_of(int, h, n)
    
    for lv in range(h):
        for i in range(n):
            if lv == 0 and i < n-1:
                tb[lv][i] = a[i] + a[i+1]
            elif i < n-2**lv:
                tb[lv][i] = tb[lv-1][i] + tb[lv-1][i+2**lv]
    
    debug_print(*tb, sep='\n')
    
    for _ in range(q):
        l, r = input_as_list()
        l -= 1
        print(tb[(r-l).bit_length()-2][l]//10)
    

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