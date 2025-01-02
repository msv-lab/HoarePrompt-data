#!/usr/bin/env pypy
from __future__ import division, print_function
from collections import defaultdict, Counter, deque
from future_builtins import ascii, filter, hex, map, oct, zip
from itertools import imap as map, izip as zip, permutations, combinations, combinations_with_replacement,product
from __builtin__ import xrange as range
from math import ceil, factorial, log,tan,pi,cos,sin,radians
from _continuation import continulet
from cStringIO import StringIO
from io import IOBase
import __pypy__
from bisect import bisect, insort, bisect_left, bisect_right
from fractions import Fraction
from functools import reduce
from decimal import *
import copy
import string
import sys
import os
import re
inf = float('inf')
mod = int(1e9) + 7
mod_ = 998244353

def factors(n):
    from functools import reduce
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sieve(n):
    arr=[True]*n
    for i in range(2,int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i,n,i):
                arr[j]=False
    primes=[]
    for i in range(n):
        if arr[i]:
            primes.append(i)

    return primes



def main():
    def cost(arr):
        cst=0
        for i in range(len(arr)-1,0,-1):
            cst+=abs(arr[i]-arr[i-1])
        return cst
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        temp=list(arr)
        temp[0]=temp[1]
        cost1=cost(temp)
        temp=list(arr)
        temp[1]=temp[0]
        cost1=min(cost1,cost(temp))
        temp=list(arr)
        temp[-2]=temp[-1]
        cost1=min(cost1,cost(temp))
        temp=list(arr)
        temp[-1]=temp[-2]
        cost1=min(cost1,cost(temp))
        print(cost1)
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