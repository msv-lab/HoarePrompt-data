#!/usr/bin/env pypy
# Author : prayushd
# Language : Python
 
from __future__ import division, print_function
from collections import defaultdict, Counter, deque
from future_builtins import ascii, filter, hex, map, oct, zip
from itertools import imap as map, izip as zip
from __builtin__ import xrange as range
from math import ceil
from _continuation import continulet
from cStringIO import StringIO
from io import IOBase
import __pypy__
from bisect import bisect, insort, bisect_left, bisect_right
import sys
import os
import re
inf = float('inf')
mod = int(1e9) + 7
mod_ = 998244353
 
'''
Check for special cases (n=1)
One wrong submission = 10 mins penalty!
do smth instead of nothing and stay organized
'''

def main():
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	c = [deque() for i in range(m)]
	free = deque()
	target = n//m
	cost = 0
	for i in range(n):
		c[arr[i]%m].append((i, arr[i]%m))

	for i in range(m):
		while len(c[i]) > target:
			free.append(c[i].popleft())

	for i in range(m):
		while len(c[i]) < target:
			cost += (i-free[0][1])%m
			arr[free[0][0]] += (i-free[0][1])%m
			c[i].append(free.popleft())
			
	print(cost)
	print(*arr)


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
			self._buffer.seek(0, 2), self._buffer.write(
				b), self._buffer.seek(ptr)
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
def input(): return sys.stdin.readline().rstrip("\r\n")
if __name__ == "__main__":
	def bootstrap(cont):
		call, arg = cont.switch()
		while True:
			call, arg = cont.switch(to=continulet(
				lambda _, f, args: f(*args), call, arg))
	cont = continulet(bootstrap)
	cont.switch()
	main()