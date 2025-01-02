#!/usr/bin/env pypy
from __future__ import division, print_function

import os
import sys
from __builtin__ import xrange as range
from cStringIO import StringIO
from future_builtins import ascii, filter, hex, map, oct, zip
from io import IOBase

import __pypy__


def discrete_ternary_search(func, lo, hi):
    """ Find the first maximum of unimodal function func() within [lo, hi] """
    while lo <= hi:
        lo_third = lo + (hi - lo) // 3
        hi_third = lo + (hi - lo) // 3 + (1 if 0 < hi - lo < 3 else (hi - lo) // 3)

        if func(lo_third) < func(hi_third):
            lo = lo_third + 1
        else:
            hi = hi_third - 1

    return lo


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = [int(x) for x in input().split()]

        def cond(x):
            a1 = [abs(ai - x) for ai in a]
            a1.sort()
            return -a1[k]

        print(discrete_ternary_search(cond, -10**9, 10**9))


# region fastio

BUFSIZE = 8192


class FastI(IOBase):
    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = StringIO()
        self.newlines = 0

    def read(self):
        if self._buffer.tell():
            return self._buffer.read()
        return os.read(self._fd, os.fstat(self._fd).st_size)

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count("\n") + (not b)
            ptr = self._buffer.tell()
            self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)
        self.newlines -= 1
        return self._buffer.readline()


class FastO(IOBase):
    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = __pypy__.builders.StringBuilder()
        self.write = lambda s: self._buffer.append(s)

    def flush(self):
        os.write(self._fd, self._buffer.build())
        self._buffer = __pypy__.builders.StringBuilder()


def print(*args, **kwargs):
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = FastI(sys.stdin), FastO(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
