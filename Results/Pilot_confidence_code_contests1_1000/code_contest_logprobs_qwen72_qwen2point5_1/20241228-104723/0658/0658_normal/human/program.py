from sys import stdin
from collections import *


def prime(n):
    if n in [2, 3]:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict, self.edges, self.l = gdict, [], defaultdict(int)

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)

    def dfsUtil(self, v):
        stack, all, cur = [v], [v], ['a', float('inf')]

        while (stack):
            s = stack.pop()

            for i in self.gdict[s]:
                if not self.visit[i]:
                    stack.append(i)
                    all.append(i)
                    self.visit[i] = 1

        for i, j in mem.items():
            if j >= len(all) and j < cur[1]:
                cur = [i, j]

        if cur[1] == float('inf'):
            print('NO')
            exit()
        else:
            for i in all:
                ans[i - 1] = cur[0]
                mem[cur[0]] -= 1

    def dfs(self):
        self.cnt, self.visit = 0, [0] * (n + 1)

        for i in range(1, n + 1):
            if self.visit[i] == 0:
                self.visit[i] = 1
                self.dfsUtil(i)


rstr = lambda: stdin.readline().strip()
s = rstr()
n, g, mem = len(s), graph(), Counter(s)
ans = [''] * (n)

for i in range(1, n + 1):
    if prime(i):
        for j in range(i * 2, n + 1, i):
            g.addEdge(j, j - i)

g.dfs()
print('YES')
print(''.join(ans))
