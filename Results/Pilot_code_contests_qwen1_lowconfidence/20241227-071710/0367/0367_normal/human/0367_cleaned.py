class graph:

    def __init__(self):
        (self.gdict, self.edges) = (defaultdict(list), set())

    def addEdge(self, node1, node2, w=None):
        self.gdict[node1].append(node2)
        self.gdict[node2].append(node1)
        self.edges.add(tuple(sorted([node1, node2])))

    def bfs_util(self, i):
        self.visit = [0] * (n + 1)
        (queue, self.visit[i]) = (deque([[i, 0]]), 1)
        while queue:
            (s, lev) = queue.popleft()
            if s == n:
                ans.append(lev)
                break
            for i1 in self.gdict[s]:
                if self.visit[i1] == 0:
                    queue.append([i1, lev + 1])
                    self.visit[i1] = 1
rint = lambda : int(stdin.readline())
rints = lambda : [int(x) for x in stdin.readline().split()]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
(n, m) = rints()
(g, g1, ans) = (graph(), graph(), [])
for _ in range(m):
    (u, v) = rints()
    g.addEdge(u, v)
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if (i, j) not in g.edges:
            g1.addEdge(i, j)
g.bfs_util(1)
g1.bfs_util(1)
print(-1 if len(ans) < 2 else max(ans))