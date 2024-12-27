"""
________        _____________              ______
___  __ \____  ____  __ \__(_)__   _______ ___  /
__  /_/ /_  / / /_  /_/ /_  /__ | / /  __ `/_  /
_  ____/_  /_/ /_  _, _/_  / __ |/ // /_/ /_  /
/_/     _\__, / /_/ |_| /_/  _____/ \__,_/ /_/
        /____/

https://github.com/Cheran-Senthil/PyRival
Copyright (c) 2018 Cheran Senthilkumar
"""
from __future__ import division, print_function

import cmath
import itertools
import math
import operator as op
import sys
from atexit import register
from bisect import bisect_left, bisect_right

# import random
# from collections import Counter, MutableSequence, defaultdict, deque
# from copy import deepcopy
# from decimal import Decimal
# from difflib import SequenceMatcher
# from heapq import heappop, heappush

if sys.version_info[0] < 3:
    from io import BytesIO as stream
    # from fractions import Fraction
    # from fractions import gcd
    # from cPickle import dumps
    # from Queue import PriorityQueue, Queue
else:
    from io import StringIO as stream
    # from functools import reduce
    # from fractions import Fraction
    # from math import gcd
    # from pickle import dumps
    # from queue import PriorityQueue, Queue


if sys.version_info[0] < 3:
    class dict(dict):
        def items(self):
            return dict.iteritems(self)

        def keys(self):
            return dict.iterkeys(self)

        def values(self):
            return dict.itervalues(self)

    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip


def sync_with_stdio(sync=True):
    """
    Sets whether the standard Python streams are allowed to buffer their I/O.

    Parameters
    ----------
    sync : bool, optional
        The new synchronization setting. Default is True.
    """
    global input, flush

    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')

        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))


def main():
    n, m = map(int, input().split(' '))
    if n > m:
        print('YES')
    else:
        a = list(map(lambda x: int(x) % m, input().split(' ')))
        dp = [[False] * m for _ in range(n)]
        dp[0][a[0]] = True
        for i in range(1, n):
            dp[i][a[i]] = True
            for j, flag in enumerate(dp[i - 1]):
                if flag:
                    dp[i][j] = True
                    dp[i][(j + a[i]) % m] = True

        if dp[-1][0]:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    sync_with_stdio(False)
    main()
