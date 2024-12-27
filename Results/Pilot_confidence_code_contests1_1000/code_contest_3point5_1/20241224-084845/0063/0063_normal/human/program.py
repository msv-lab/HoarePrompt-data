#!/usr/bin/env pypy
from __future__ import division, print_function
from collections import defaultdict, Counter, deque
from future_builtins import ascii, filter, hex, map, oct, zip
from itertools import imap as map, izip as zip, permutations, combinations, combinations_with_replacement
from __builtin__ import xrange as range
from math import ceil, factorial
from _continuation import continulet
from cStringIO import StringIO
from io import IOBase
import __pypy__
from bisect import bisect, insort, bisect_left, bisect_right
from fractions import Fraction
from functools import reduce
import string
import sys
import os
import re
inf = float('inf')
mod_ = int(1e9) + 7
mod = 998244353

def factors(n):
    from functools import reduce
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sieve():
    n,m=1,10**6
    primes = {}
    arr=set([])
    for i in range(2, round(m ** 0.5) + 1):
        a = n // i
        b = m // i
        for k in range(max(2, a), b + 1):
            c = i * k
            primes[c] = 1

    for i in range(max(n, 2), m + 1):
        if i not in primes:
            arr.add(i)

    return arr

def nc2(x):
    return (x*(x-1))//2
def main():
    n=int(input())
    arr=list(map(int,input().split()))
    if sum(arr)%2==0:
        print("YES")
    else:
        print("NO")

        


   
    






# region fastio

BUFSIZE = 8192

class FastI(IOBase):
    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = StringIO()
        self.newlines = 0

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

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

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

sys.stdin, sys.stdout = FastI(sys.stdin), FastO(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()