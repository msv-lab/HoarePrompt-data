from __future__ import print_function # for PyPy2
from collections import Counter, OrderedDict
from itertools import permutations as perm
from collections import deque
from sys import stdin
from bisect import *
from heapq import *
import math
 
g   = lambda : stdin.readline().strip()
gl  = lambda : g().split()
gil = lambda : [int(var) for var in gl()]
gfl = lambda : [float(var) for var in gl()]
gcl = lambda : list(g())
gbs = lambda : [int(var) for var in g()]
mod = int(1e9)+7
inf = float("inf")

t, = gil()

for _ in range(t):
	# print()
	n, = gil()
	val = gbs()
	idx = list(xrange(n))
	idx.sort(key=lambda x : [val[x], x])
	# print(idx) 
	one = []
	to = []

	for ix in idx:
		if ix > (one[-1] if one else -1) and val[ix] <= (val[to[0]] if to else inf):
			one.append(ix)
		elif ix > (to[-1] if to else -1):
			to.append(ix)
		else:
			break

	if len(one) + len(to) == n:
		# print(one, to)
		for ix in one:
			val[ix] = 1
		for ix in to:
			val[ix] = 2
		for v in val:
			print(v, end="")
		print()
	else:
		# print(one, to)
		print("-")