from __future__ import print_function
from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
n, m = rints()
edges, ans = [rints() for _ in range(m)], [[] for _ in range(n)]

for i in range(1, n + 1):
    ans[i - 1].append([i, i])

for i, j in enumerate(edges):
    ans[j[0] - 1].append([i + n + 1, j[0]])
    ans[j[1] - 1].append([i + n + 1, j[1]])

for i in range(n):
    print(len(ans[i]))
    for j in ans[i]:
        print(*j)
