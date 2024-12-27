from sys import stdin, stdout
n, m = map(int, stdin.readline().rstrip().split())
#n, m = 4,3
graph = {}
for i in range(n):
    graph[i+1] = []
for i in range(m):
    edge = map(int, stdin.readline().rstrip().split())
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
#graph = {1:[3,4], 2:[], 3:[1,4], 4:[1,3]}

leftToCheck = set([i+1 for i in range(n)])
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


