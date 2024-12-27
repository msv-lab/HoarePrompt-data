from __future__ import print_function, division
from sys import stdin, stdout
from fractions import gcd
# from math import *
from collections import *
from operator import mul
from functools import reduce
from copy import copy

rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = defaultdict(list)
        self.gdict, self.edges, self.l = gdict, defaultdict(int), defaultdict(int)

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)

    def subtree(self, v):
        queue, visit = deque([[v, 0]]), [0] * (n + 1)
        visit[v], level, self.nodes, ans = 1, [0] * (n + 1), [0] * (n + 1), 0

        while queue:
            s, lev = queue.popleft()
            level[lev] = (level[lev] + 1) % 2

            for i in self.gdict[s]:
                if not visit[i]:
                    queue.append([i, lev + 1])
                    visit[i] = 1

        print(sum(level))



n, a = int(input()), rints()
g = graph()
for i in range(n - 1):
    g.addEdge(a[i], i + 2)

g.subtree(1)
