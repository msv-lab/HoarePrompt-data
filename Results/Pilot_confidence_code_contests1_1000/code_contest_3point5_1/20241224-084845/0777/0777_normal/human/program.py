from sys import stdin
from collections import *
from copy import copy
from bisect import *


class graph:
    # initialize graph
    def __init__(self, gdict=None):
        self.gdict = defaultdict(list)

    # add edge
    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)

    def subtree(self, v):
        queue, visit, ans, order = deque([v]), [0] * (n + 1), [], [[] for i in range(n + 1)]
        visit[v], self.nodes = 1, [0] * (n + 1)

        while queue:
            s = queue.popleft()

            for i in self.gdict[s]:
                if not visit[i]:
                    queue.append(i)
                    visit[i] = 1
                    ans.append([i, s])

        for i, j in ans[::-1]:
            self.nodes[j] += self.nodes[i] + 1

        while ans:
            cur, par = ans.pop()
            visit[cur] = 0
            if c[cur] > self.nodes[cur]:
                print('NO')
                exit()

            for i in self.gdict[cur]:
                if not visit[i]:
                    order[cur].extend(order[i])

            order[cur].sort()
            order[cur].insert(c[cur], [c[cur] + 1, cur])

            for i in range(c[cur] + 1, len(order[cur])):
                order[cur][i][0] += 1
            # print(order[cur])

        order[self.gdict[0][0]].sort(key=lambda x: x[1])
        # print(order[self.gdict[0][0]])
        print('YES')
        print(' '.join(map(str, [x for x,y in order[self.gdict[0][0]]])))


rints = lambda: [int(x) for x in stdin.readline().split()]
n = int(input())
g, c = graph(), [0]

for i in range(1, n + 1):
    x, y = rints()
    c.append(y)
    g.addEdge(i, x)

g.subtree(0)
