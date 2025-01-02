#!/usr/bin/python
from collections import deque

n = int(raw_input())
g = [[] for i in xrange(n)]
for _ in xrange(n-1):
	a, b = [int(i)-1 for i in raw_input().split()]
	g[a].append(b)
	g[b].append(a)

v = map(int, raw_input().split())
root, used, p = [[] for i in xrange(n)], [False] * n, [-1] * n

queue = deque([0])
while len(queue) > 0:
	c = queue.popleft()
	used[c] = True
	for i in g[c]:
		if not used[i]:
			root[c].append(i)
			queue.append(i)
			p[i] = c

pos, neg = [0] * n, [0] * n
for i in xrange(n):
	used[i] = False
	if len(root[i]) == 0:
		queue.append(i)

while len(queue) > 0:
	c = queue.popleft()
	used[c] = True

	max1, max2 = 0, 0
	for i in root[c]:
		max1 = max(max1, pos[i])
		max2 = max(max2, neg[i])

	pos[c] = max1
	neg[c] = max2
	s = v[c] - max1 + max2
	if s > 0:
		pos[c]+=s
	else:
		neg[c]+=-s

	if p[c] != -1:
		canAdd = True
		for i in root[p[c]]:
			if not used[i]:
				canAdd = False
				break
		if canAdd:
			queue.append(p[c])

print (pos[0] + neg[0])
