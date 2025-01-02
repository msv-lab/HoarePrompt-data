#!/usr/bin/env python3
# Submit as pypy2


from __future__ import print_function, division, unicode_literals

__metaclass__ = type

try:
    input = raw_input
    range = xrange
except NameError:
    pass


import sys


# Test code requires python3
# from hypothesis import given
# from hypothesis import strategies as st
#
#
# def debug(*args, **kwargs):
#     print(*args, *('{}={}'.format(k, v) for k, v in kwargs.items()),
#           sep='; ', file=sys.stderr)


def f(A, B, N):
    rem = N % 3
    if rem == 0:
        return A
    elif rem == 1:
        return B
    else:
        return A ^ B


T = int(input())
for _ in range(T):
    A, B, N = map(int, input().split())
    print(f(A, B, N))
