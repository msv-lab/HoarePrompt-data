#!/usr/bin/env python2
"""
This file is part of https://github.com/cheran-senthil/PyRival
Copyright 2019 Cheran Senthilkumar <hello@cheran.io>

"""
from __future__ import division, print_function

import itertools
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
    n, m = map(int, input().split())

    station = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        station[a - 1].append(b - 1)

    max_candy = [0] * n
    for i in range(n):
        try:
            max_candy[i] = min(station[i], key=lambda x: x + n - i if x < i else x - i)
        except ValueError:
            pass

    for i in range(n):
        res = 0

        for j in range(i, i + n):
            if len(station[j % n]) == 0:
                continue

            dist = j - i
            j %= n
            dist += (len(station[j]) - 1) * n + (max_candy[j] + n - j if max_candy[j] < j else max_candy[j] - j)

            res = max(res, dist)

        print(res, end=' ')


if __name__ == '__main__':
    main()
