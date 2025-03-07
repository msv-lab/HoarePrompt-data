from functools import reduce
import math
from collections import deque
 
 
def testcase():
	n, t = map(int, input().split())
	tree = deque()
	empty = True
	for i in range(n - 1):
		u, v = map(int, input().split())
		if empty:
			tree.append(u)
			tree.append(v)
			empty = False
		else:
			if v == tree[0]:
				tree.appendleft(u)
			elif v == tree[-1]:
				tree.append(u)
			elif u == tree[0]:
				tree.appendleft(v)
			elif u == tree[-1]:
				tree.append(v)
	start = int(input())
	idx = tree.index(start)
	moves = [min(t, idx), min(t, n - idx - 1)]
	if any([move % 2 == 1 for move in moves]):
		print("Ron")
	else:
		print("Hermione")
 
 
t = 1 # int(input())
 
for i in range(t):
	testcase()