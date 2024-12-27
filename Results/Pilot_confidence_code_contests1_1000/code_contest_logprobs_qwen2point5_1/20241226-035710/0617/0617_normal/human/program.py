from sys import stdin
from collections import defaultdict
from itertools import permutations


def fast2():
    import os, sys, atexit
    from cStringIO import StringIO as BytesIO
    # range = xrange
    sys.stdout = BytesIO()
    atexit.register(lambda: os.write(1, sys.stdout.getvalue()))
    return BytesIO(os.read(0, os.fstat(0).st_size)).readline


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict, self.edges, self.l = gdict, defaultdict(int), [0] * (n + 1)

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)
        self.l[node1] += 1
        self.l[node2] += 1

    def dfsUtil(self, v, per):
        global ans, out
        stack, self.visit = [[v, 0]], [0] * (n + 1)
        self.visit[v], tem = per[0] + 1, color[per[0]][v - 1]

        while (stack):
            s, c = stack.pop()

            for i in self.gdict[s]:
                if not self.visit[i]:
                    val = (c + 1) % 3
                    stack.append([i, val])
                    self.visit[i] = per[val] + 1
                    tem += color[per[val]][i - 1]

        if tem < ans:
            ans, out = tem, self.visit[1:]

    def dfs(self):
        v = 0

        for i in range(1, n + 1):
            if self.l[i] == 1:
                v = i
                break

        for per in permutations([0, 1, 2], 3):
            self.dfsUtil(v, per)


input = fast2()
rints = lambda: [int(x) for x in input().split()]
n = int(input())
color = [rints() for _ in range(3)]
g, ans, out = graph(), float('inf'), []

for _ in range(n - 1):
    u, v = rints()
    g.addEdge(u, v)

if list(filter(lambda x: x > 2, g.l)):
    print(-1)
else:
    g.dfs()
    print('%d\n%s' % (ans, ' '.join(map(str, out))))
