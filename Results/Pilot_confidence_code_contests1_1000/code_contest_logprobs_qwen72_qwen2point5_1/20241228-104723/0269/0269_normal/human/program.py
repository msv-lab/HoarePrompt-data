from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(100000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
 
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
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        def input(): return sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
 
 
def dd():
    return map(int, input().split())
 
 
def arr():
    return list(map(int, input().split()))
 
 
def twinSort(X, Y):
    # sorting X wrt Y
    return [x for _, x in sorted(zip(Y, X))]

 
def solve():
    n=int(input())
    ar=arr()
    s=sum(ar)
    fillWith=math.ceil(s/n)
    last=s-fillWith*(s//fillWith)
    if s%n==0:
        print(0)
    elif s//n==0:
        print(int(s*(n-s)))
    else:
        aaa=s-(s//n)*n
        print(int(aaa*last))

    
    
 
 
def main():
    testCase = 1
    if testCase:
        for _ in range(int(input())):
            solve()
    else:
        solve()
 
 
if __name__ == '__main__':
    sync_with_stdio(False)
    main()