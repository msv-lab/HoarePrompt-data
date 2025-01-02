(n, m) = map(int, stdin.readline().rstrip().split())
graph = {}
for i in range(n):
    graph[i + 1] = []
for i in range(m):
    edge = map(int, stdin.readline().rstrip().split())
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
leftToCheck = set([i + 1 for i in range(n)])
isGood = True
while len(leftToCheck) > 0:
    checkMe = leftToCheck.pop()
    neighbors = graph[checkMe]
    cliqueSize = len(neighbors)
    for neighbor in neighbors:
        if len(graph[neighbor]) != cliqueSize:
            isGood = False
            leftToCheck = set([])
            break
    leftToCheck.discard(set(neighbors))
if isGood:
    print('YES')
else:
    print('NO')