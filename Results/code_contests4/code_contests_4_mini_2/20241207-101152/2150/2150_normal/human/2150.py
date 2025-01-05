from __future__ import print_function,division
import sys
if sys.version_info < (3, 0):
    range = xrange
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

from collections import defaultdict as dd, deque

n = int(input())

edges = []
E = dd(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    E[a].append(b)
    E[b].append(a)
    edges.append((a,b))

if n%2 == 1:
    print(-1)
    sys.exit()

def count(a,b):
    Q = deque()
    Q.append(a)
    seen = {b}
    cnt = 0
    while Q:
        a = Q.popleft()
        if a in seen:
            continue
        cnt += 1
        seen.add(a)

        for b in E[a]:
            Q.append(b)
    return cnt

leafs = [e for e in E if len(E[e])==1]

sz = {}
seen = set()

def dfs(node):
    print(node)
    if node in seen:
        return 0
    seen.add(node)

    sz[node] = 1

    for neigh in E[node]:
        print(neigh)
        sz[node] += dfs(neigh)
    return sz[node]

root = leafs[0]
dfs(root)

cuts = 0
for a,b in edges:
    val = min(sz[a], sz[b])
    if val%2 == 0:
        cuts += 1
print(cuts)
