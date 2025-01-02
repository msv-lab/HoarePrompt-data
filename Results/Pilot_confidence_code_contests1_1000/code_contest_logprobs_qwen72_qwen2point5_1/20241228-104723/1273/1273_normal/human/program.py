from collections import*
n = int(raw_input())
e = [[] for i in range(n+1)]
for i in range(n - 1):
	u, v = map(int, raw_input().split())
	e[u].append(v)
	e[v].append(u)
dep = [-1] * (n + 1)
dep[1] = 0
q = deque([1])
cur = 1
while q:
	cur = q.popleft()
	for to in e[cur]:
		if dep[to] == -1:
			dep[to] = dep[cur] + 1
			q.append(to)
dep = [-1] * (n + 1)
pred = [0] * (n + 1)
dep[cur] = 0
q = deque([cur])
end = cur
while q:
	end = q.popleft()
	for to in e[end]:
		if dep[to] == -1:
			dep[to] = dep[end] + 1
			pred[to] = end
			q.append(to)
deg = [-1] * (n + 1)
bad = False
for i in range(1, n + 1):
	if deg[dep[i]] == -1:
		deg[dep[i]] = len(e[i])
	else:
		if deg[dep[i]] != len(e[i]):
			bad = True
			break
if not bad:
	print(cur)
	exit()
center = end
for i in range(dep[end] // 2):
	center = pred[center]
dep = [-1] * (n + 1)
dep[end] = 0
q = deque([end])
while q:
	cur = q.popleft()
	for to in e[cur]:
		if dep[to] == -1:
			dep[to] = dep[cur] + 1
			q.append(to)
deg = [-1] * (n + 1)
bad = False
for i in range(1, n + 1):
	if deg[dep[i]] == -1:
		deg[dep[i]] = len(e[i])
	else:
		if deg[dep[i]] != len(e[i]):
			bad = True
			break
if not bad:
	print(end)
	exit()
top = center
dep = [-1] * (n + 1)
dep[center] = 0
q = deque([center])
while q:
	cur = q.popleft()
	for to in e[cur]:
		if dep[to] == -1:
			if len(e[to]) == 2:
				dep[to] = dep[cur] + 1
				q.append(to)
			elif len(e[to]) == 1:
				top = to
				q.clear()
				break
deg = [-1] * (n + 1)
bad = False
for i in range(1, n + 1):
	if deg[dep[i]] == -1:
		deg[dep[i]] = len(e[i])
	else:
		if deg[dep[i]] != len(e[i]):
			bad = True
			break
if not bad:
	print(center)
	exit()
dep = [-1] * (n + 1)
dep[top] = 0
q = deque([top])
while q:
	cur = q.popleft()
	for to in e[cur]:
		if dep[to] == -1:
			dep[to] = dep[cur] + 1
			q.append(to)
deg = [-1] * (n + 1)
bad = False
for i in range(1, n + 1):
	if deg[dep[i]] == -1:
		deg[dep[i]] = len(e[i])
	else:
		if deg[dep[i]] != len(e[i]):
			bad = True
			break
if not bad:
	print(top)
	exit()
print(-1)