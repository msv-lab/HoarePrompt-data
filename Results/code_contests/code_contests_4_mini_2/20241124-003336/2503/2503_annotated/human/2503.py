#!/usr/bin/env python2
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
from __future__ import division, print_function

import itertools
import math
import os
import sys
from atexit import register
from io import BytesIO


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


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


range = xrange

filter = itertools.ifilter
map = itertools.imap
zip = itertools.izip

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')


def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if (x1 == x2)  and (y1 == y2):
        print(0)
        return

    n = int(input())
    s = input()

    pref_sums = [[0, 0] for _ in range(n)]

    u, r = 0, 0
    if s[0] == 'U':
        u = 1
    if s[0] == 'D':
        u = -1
    if s[0] == 'R':
        r = 1
    if s[0] == 'L':
        r = -1

    pref_sums[0] = [r, u]
    new_x, new_y = x1 + r, y1 + u

    dist = abs(new_x - x2) + abs(new_y - y2) - 1
    if dist <= 0:
        print(1)
        return

    min_dist = dist
    for i in range(1, n):
        u, r = 0, 0
        if s[i] == 'U':
            u = 1
        if s[i] == 'D':
            u = -1
        if s[i] == 'R':
            r = 1
        if s[i] == 'L':
            r = -1

        pref_sums[i] = [pref_sums[i - 1][0] + r, pref_sums[i - 1][1] + u]
        new_x, new_y = x1 + pref_sums[i][0], y1 + pref_sums[i][1]
        dist = abs(new_x - x2) + abs(new_y - y2) - i - 1

        if dist <= 0:
            print(i + 1)
            return

        if dist < min_dist:
            min_dist = dist

    moves_toward = abs(x1 - x2) + abs(y1 - y2) - (abs(new_x - x2) + abs(new_y - y2) - n)

    if moves_toward <= 0:
        print(-1)
        return

    cycles = (abs(x1 - x2) + abs(y1 - y2) - min_dist) // moves_toward
    res = n * cycles

    x1, y1 = x1 + cycles * pref_sums[-1][0], y1 + cycles * pref_sums[-1][1]

    if abs(x1 - x2) + abs(y1 - y2) - n * cycles <= 0:
        print(res)
        return

    for i in range(n):
        new_x, new_y = x1 + pref_sums[i][0], y1 + pref_sums[i][1]
        dist = abs(new_x - x2) + abs(new_y - y2) - i - n * cycles - 1
        if dist <= 0:
            print(res + i + 1)
            return

    return



if __name__ == '__main__':
    main()
