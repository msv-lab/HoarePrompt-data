from sys import stdin
from collections import *


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        self.gdict = [[] for _ in range(n)]

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)

    def find_SCC(self):
        SCC, S, P, d = [], [], [], 0
        depth, stack = [0] * n, list(range(n))

        while stack:
            # print(stack, S, P)
            node = stack.pop()
            if node < 0:
                if P[-1] == depth[~node]:
                    P.pop()
                    scc = []
                    SCC.append(scc)

                    root = ~node
                    while node != root:
                        node = S.pop()
                        scc.append(node)
                        depth[node] = -1

            elif depth[node] > 0:
                while P[-1] > depth[node]:
                    P.pop()

            elif depth[node] == 0:
                depth[node] = d = d + 1
                P.append(d)
                S.append(node)
                stack.append(~node)
                stack += g.gdict[node]

        return SCC[::-1]


rints = lambda: [int(x) for x in stdin.readline().split()]
n, c, a = int(input()), rints(), rints()
g = graph()
for i in range(n):
    g.addEdge(i, a[i] - 1)

ans = 0
for cnt in g.find_SCC():
    if len(cnt) == 1 and a[cnt[0]] == cnt[0] + 1:
        ans += c[cnt[0]]

    elif len(cnt) > 1:
        ans += min([c[i] for i in cnt])

print(ans)
