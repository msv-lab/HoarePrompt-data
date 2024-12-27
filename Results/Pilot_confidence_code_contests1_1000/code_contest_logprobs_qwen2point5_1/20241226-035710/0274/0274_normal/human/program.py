from sys import stdin
from collections import *


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        self.gdict = [[] for _ in range(n + 1)]

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)

    def dfsUtil(self, v):
        stack, self.visit = v, [-1] * (n + 1)
        ans, d = [], 0

        while (stack):
            ans.append(stack)
            self.visit[stack] = d
            d += 1

            for i in self.gdict[stack]:
                if self.visit[i] == -1:
                    stack = i
                    break
            else:
                be = ans.index(min(self.gdict[stack], key=lambda x: self.visit[x]))
                print('%d\n%s' % (len(ans) - be, ' '.join(map(str, ans[be:]))))
                exit()


rints = lambda: [int(x) for x in stdin.readline().split()]
n, m, k = rints()
g = graph()
for _ in range(m):
    u, v = rints()
    g.addEdge(u, v)

g.dfsUtil(1)
