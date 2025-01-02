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
            result_append(list(read().split()))
    return result


####################################################
import math
sqrt = math.sqrt
from collections import deque


[n] = r(int)
xs = r(int)
xss = set(xs)

if n <= 2:
    w("-1")
    sys.exit()

if len(xss) == 1:
    w("-1")
    sys.exit()

if len(xs) == 3 and xs[0] == xs[2]:
    w("-1")
    sys.exit()


def check(xs, k):
    k2 = 0 # malejąco
    k1 = 0
    for i in xrange(0, n-1, 1):
        if xs[i] < xs[i+1]:
            k2 += 1
        if xs[i] > xs[i+1]:
            k1 += 1

    if k2 >= 2:
        for i in xrange(0, n-1, 1):
            if xs[i] < xs[i+1]:
                w("%s %s" % (abs(i+1+k), abs(i+2+k)))
                sys.exit()

    if k2 == 1 and k1 >= 1 and len(xss) < n:
        for i in xrange(0, n-1, 1):
            if xs[i] > xs[i+1]:
                w("%s %s" % (abs(i+1+k), abs(i+2+k)))
                sys.exit()
            if xs[i] < xs[i+1]:
                w("%s %s" % (abs(i+1+k), abs(i+2+k)))
                sys.exit()

    if k2 == 1 and k1 == 0 and len(xs) >= 3:
        for i in xrange(0, n-1, 1):
            if xs[i] < xs[i+1]:
                w("%s %s" % (abs(i+1+k), abs(i+2+k)))
                sys.exit()

    if k2 == 0:
        for i in xrange(0, n-1, 1):
            if xs[0] != xs[i]:
                w("%s %s" % (abs(1+k), abs(i+1+k)))
                sys.exit()

check(xs, 0)
xs.reverse()
check(xs, -1*n)


w("-1")
    






