from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin
from collections import namedtuple
Point = namedtuple('Point', 'x y')

def make_test(p1, p2):
    gradient = (p1.y - p2.y) / (p1.x - p2.x)
    y_intercept = p1.y - gradient * p1.x
    return lambda p: gradient * p.x + y_intercept > p.y

for line in stdin:
    it = (float(s) for s in line.split(','))
    A, B, C, D = (Point(next(it), next(it)) for _ in xrange(4))

    f = make_test(A, C)
    g = make_test(B, D)
    if f(B) == f(D) or g(A) == g(C):
        print('NO')
    else:
        print('YES')