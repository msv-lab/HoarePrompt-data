import sys
from collections import deque

def bfs(start):
	pq = deque()
	visited = set({start})
	pq.appendleft(start)
	while pq:
		u = pq.pop()
		for v in g[u]:
			if v not in visited:
				visited.add(v)
				pq.appendleft(v)
				parent[v] = u

	path_f_b = set({})
	u = f
	while u != b:
		path_f_b.add(u)
		u = parent[u]
	path_f_b.add(u)
	return path_f_b

def sol(visited):
	fs = bs = 1
	pq = deque()
	pq.appendleft(f)
	while pq:
		u = pq.pop()
		for v in g[u]:
			if v not in visited:
				visited.add(v)
				fs += 1
				pq.appendleft(v)
	pq.appendleft(b)
	while pq:
		u = pq.pop()
		for v in g[u]:
			if v not in visited:
				visited.add(v)
				bs += 1
				pq.appendleft(v)

	return (n * (n-1)) - (bs*fs)



n,f,b = map(int, sys.stdin.readline().strip().split(' '))
g = {i:[] for i in range(1,n+1)}
parent = {i:-1 for i in range(1,n+1)}
for n0 in range(n-1):
	u,v = map(int, sys.stdin.readline().strip().split(' '))
	g[u].append(v)
	g[v].append(u)

print(sol(bfs(b)))

