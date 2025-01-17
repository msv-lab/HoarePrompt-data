for _ in range(int(input())):
	n = int(input())
	adj = [set() for _ in range(n)]
	deg = [0] * n
	for _ in range(n - 1):
		u, v = map(int, input().split())
		u -= 1; v -= 1
		adj[u].add(v); adj[v].add(u)
		deg[u] += 1; deg[v] += 1
	leaves = list(filter(lambda x: deg[x] <= 1, [i for i in range(n)]))
	
	cnt = n; rad = 0
	while cnt > 2:
		cnt -= len(leaves)
		rad += 1
		nls = []
		for u in leaves:
			v = min(adj[u])
			adj[v].remove(u)
			deg[v] -= 1
			if deg[v] == 1: nls.append(v)
		leaves = nls
	if cnt == 1:
		print(rad + 1)
		for i in range(rad + 1): print(leaves[0] + 1, i)
	else:
		if rad % 2:
			print(rad + 1)
			for i in range(1, rad + 2, 2):
				print(leaves[0] + 1, i)
				print(leaves[1] + 1, i)
		else:
			print(rad + 2)
			for i in range(rad + 2):
				print(leaves[0] + 1, i)
				