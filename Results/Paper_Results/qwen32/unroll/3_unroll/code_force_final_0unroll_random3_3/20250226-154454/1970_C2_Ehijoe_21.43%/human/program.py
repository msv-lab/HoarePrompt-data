from functools import reduce
import math
from collections import deque, defaultdict
 
 
def dfs(nodes, start, parent=None):
	if len(nodes[start]) == 1 and nodes[start][0] == parent:
		return [0]
	distances = []
	for node in nodes[start]:
		if node != parent:
			distances.extend([1 + dist for dist in dfs(nodes, node, start)])
	return distances
 
 
def testcase():
	n, t = map(int, input().split())
	edges = []
	empty = True
	nodes = defaultdict(list)
	for i in range(n - 1):
		u, v = map(int, input().split())
		nodes[u].append(v)
		nodes[v].append(u)
	
	leaves = deque()
	for key in nodes:
		if len(nodes[key]) == 1:
			leaves.append(key)
	
	start = int(input())
	moves = dfs(nodes, start)
	
	if any([move % 2 == 1 for move in moves]):
		print("Ron")
	else:
		print("Hermione")
 
 
t = 1 # int(input())
 
for i in range(t):
	testcase()