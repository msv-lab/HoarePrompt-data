from __future__ import division, print_function

MOD = 998244353
mod = 10**9 + 7

# import resource
# resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])

def prepare_factorial():
    fact = [1]
    for i in range(1, 20):
        fact.append((fact[-1] * i) % mod)
    ifact = [0] * 105
    ifact[104] = pow(fact[104], mod - 2, mod)
    for i in range(104, 0, -1):
        ifact[i - 1] = (i * ifact[i]) % mod

    return fact, ifact

# import threading
# threading.stack_size(1<<27)
import sys
# sys.setrecursionlimit(10000)

from bisect import bisect_left, bisect_right, insort
from math import floor, ceil, sqrt, degrees, atan, pi, log, sin, radians, factorial
from heapq import heappop, heapify, heappush
from collections import Counter, defaultdict, deque
# from itertools import permutations


def modinv(n, p):
    return pow(n, p - 2, p)

def ncr(n, r, fact, ifact):    # for using this uncomment the lines calculating fact and ifact
    t = (fact[n] * (ifact[r] * ifact[n-r]) % mod) % mod
    return t

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()

"""*****************************************************************************************"""

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y)//(GCD(x, y))

def get_xor(n):
    return [n, 1, n+1, 0][n % 4]

def get_n(P):    # this function returns the maximum n for which Summation(n) <= Sum
    ans = (-1 + sqrt(1 + 8*P))//2
    return ans

""" ********************************************************************************************* """

def main():

    for _ in range(int(input())):
        l, r = get_ints()
        print(min(l, r, (l + r) // 3))


""" -------- Python 2 and 3 footer by Pajenegod and c1729 ---------"""

py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange

import os, sys
from io import IOBase, BytesIO

BUFSIZE = 8192

class FastIO(BytesIO):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0, 2), super(FastIO, self).write(s))[0])
        return s

    def read(self):
        while self._fill(): pass
        return super(FastIO, self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill();
            self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)


class IOWrapper(IOBase):

    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s: self.buffer.write(s.encode('ascii'))
            self.read = lambda: self.buffer.read().decode('ascii')
            self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

if __name__ == '__main__':
    main()
    # threading.Thread(target=main).start()
	  	 			 			   				 	 			 			