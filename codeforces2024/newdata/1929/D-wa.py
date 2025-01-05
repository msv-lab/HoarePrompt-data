

for _ in range(int(input())):
    n = int(input())
    roads = dict()
    degree = [0 for _ in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        degree[a] += 1
        degree[b] += 1

        if a not in roads:
            roads[a] = [b]
        else:
            roads[a].append(b)
        
        if b not in roads:
            roads[b] = [a]
        else:
            roads[b].append(a)
    degreeOneNodes = []

    for i in range(n):
        if degree[i] == 1:
            degreeOneNodes.append(i)

    goodPaths = [1 for _ in range(n)]

    ans = 0

    for v in degreeOneNodes:
        degree[v] -= 1
        for u in roads[v]:
            if degree[u] == 0:
                ans = (ans + goodPaths[u]) % 998244353
                continue
            degree[u] -= 1
            if degree[u] == 1:
                degreeOneNodes.append(u)
            goodPaths[u] = (goodPaths[u] * (goodPaths[v] + 1)) % 998244353
    ans = (ans + goodPaths[degreeOneNodes[-1]]) % 998244353
    print(ans+1)