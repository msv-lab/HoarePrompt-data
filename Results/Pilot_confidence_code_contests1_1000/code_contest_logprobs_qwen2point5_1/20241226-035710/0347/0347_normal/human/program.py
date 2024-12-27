#!/usr/bin/env python
from __future__ import division, print_function

# Testing code by c1729

import os
import random
import sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip
else:
    _str = str
    str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

MX = 2 * 10 ** 5 + 10
lt = [0] * MX
rt = [0] * MX
k = [0] * MX
pr = [0.0] * MX
cur = 1

def merge(left, right):
    tmp = [0]
    where, pos = tmp, 0
    while left and right:
        if pr[left] > pr[right]:
            where[pos] = left
            where, pos = rt, left
            left = rt[left]
        else:
            where[pos] = right
            where, pos = lt, right
            right = lt[right]
    where[pos] = left and right
    return tmp[0]


def erase(n, key):
    if k[n] == key:
        return merge(lt[n], rt[n])
    m = n
    while 1:
        if key < k[n]:
            if not lt[n]:
                break
            if k[lt[n]] == key:
                lt[n] = merge(lt[lt[n]], rt[lt[n]])
                break
            n = lt[n]
        else:
            if not rt[n]:
                break
            if  k[rt[n]] == key:
                rt[n] = merge(lt[rt[n]], rt[rt[n]])
                break
            n = rt[n]
    return m

def lower_bound(n, key):
    while n and k[n] < key: 
        n = rt[n]
    if not n: return 0
    best_node = n
    best = k[n]
    while n:
        if k[n] < key:
            n = rt[n]
        else:
            if k[n] < best:
                best = k[n]
                best_node = n
            n = lt[n]
    return best_node


def main():
    n = int(readline())
    a = readlist()
    _b = sorted(map(int, readline().split()))

    def build(i, j):
        global cur
        if i == j:
            return 0
        mid = (i + j) // 2
        root = cur
        cur += 1
        pr[root] = random.random()
        k[root] = _b[mid]
        lt[root] = build(i, mid)
        rt[root] = build(mid + 1, j)
        return root

    b = build(0, len(_b))
    for ai in a:
        it = lower_bound(b, n - ai)
        if not it:
            ptr = b
            while lt[ptr]:
                ptr = lt[ptr]
            it = ptr
        print((k[it] + ai) % n, end=' ')
        b = erase(b, k[it])


# region template

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._buffer = BytesIO()
        self._fd = file.fileno()
        self._writable = "x" in file.mode or "r" not in file.mode
        self.write = self._buffer.write if self._writable else None

    def read(self):
        if self._buffer.tell():
            return self._buffer.read()
        return os.read(self._fd, os.fstat(self._fd).st_size)

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self._buffer.tell()
            self._buffer.seek(0, 2), self._buffer.write(b), self._buffer.seek(ptr)
        self.newlines -= 1
        return self._buffer.readline()

    def flush(self):
        if self._writable:
            os.write(self._fd, self._buffer.getvalue())
            self._buffer.truncate(0), self._buffer.seek(0)


class ostream:
    def __lshift__(self, a):
        if a is endl:
            sys.stdout.write(b"\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(str(a))
        return self


def print(*args, **kwargs):
    sep, file = kwargs.pop("sep", b" "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", b"\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
cout, endl = ostream(), object()

readline = sys.stdin.readline
readlist = lambda var=int: [var(n) for n in readline().split()]
input = lambda: readline().rstrip(b"\r\n")

# endregion

if __name__ == "__main__":
    main()