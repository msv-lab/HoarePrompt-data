####################################################
# -*- coding: utf-8 -*-
import sys

w = sys.stdout.write
read = sys.stdin.readline
reads = sys.stdin.read

def r(f=None):
    if f:
        return map(f, read().split())
    else:
        return read().split()

def rs(t,f=None):
    result = []
    result_append = result.append
    for i in xrange(t):
        if f:
            result_append(tuple(map(f, read().split())))
        else:
            result_append(read().replace('\n', ''))
    return result


####################################################
import math
sqrt = math.sqrt
from collections import deque


[n, x, y, c] = r(int)
c -= 1
o = [x - 1, n - x, y - 1, n - y]
cc = 0
k = max([x-1+y-1, x-1+n-y, n-x+y-1, n-x+n-y])
oo = [x-1+ n-y+2, y-1+x-1+2, n-x+x-1+2, n-x+n-y+2]
#print oo
def su(x):
    return (x + 1) * x / 2

def val(t):
    res = 2 * t * t + 2 * t
    for x in o:
        if x < t:
            res -= (t-x+1) * (t-x+1) - (2 * (t-x+1) - 1)
    for x in oo:
        if x <= t:
            res += su(t+1-x)
    
    return res
    
#print [val(t) for t in range(1, k+1)]

def binary_search():
    mi = 1; ma = k
    while mi < ma:
        m = (mi + ma) / 2
        tt = val(m)
        if tt < c:
            mi = m + 1
        elif tt > c:
            ma = m
        else:
            return m
    return mi

if c == 0:
    w("0")
else:
    result = binary_search()
    w("%s" % (result, ))


    