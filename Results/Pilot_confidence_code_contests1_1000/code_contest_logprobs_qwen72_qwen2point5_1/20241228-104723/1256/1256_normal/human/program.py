from sys import stdin
from collections import *


class graph:
    def __init__(self):
        self.gdict, self.edges, self.l = defaultdict(list), defaultdict(int), defaultdict(int)

    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)

    def dfsUtil(self, v):
        stack, cost = [v], a[v]

        while (stack):
            s = stack.pop()
            cost = min(cost, a[s])

            for i1 in self.gdict[s]:
                if not self.visit[i1]:
                    stack.append(i1)
                    self.visit[i1] = True
        return cost

    def dfs(self):
        self.visit, ans = [False] * (n + 1), 0

        for i in range(n):
            if not self.visit[i]:
                self.visit[i] = True
                ans += self.dfsUtil(i)
        print(ans)


rints = lambda: [int(x) for x in stdin.readline().split()]
n, m = rints()
a, g = rints(), graph()
for _ in range(m):
    u, v = rints()
    g.addEdge(u - 1, v - 1)
g.dfs()
