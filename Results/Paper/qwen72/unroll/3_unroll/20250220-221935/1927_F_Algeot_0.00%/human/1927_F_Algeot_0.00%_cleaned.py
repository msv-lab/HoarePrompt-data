sys.setrecursionlimit(10 ** 6)

class UnionFind:

    def __init__(self, N):
        self.p = [-1] * N

    def find(self, x):
        y = self.p[x]
        while y >= 0:
            x = y
            y = self.p[y]
        return x

    def unite(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x == y:
            return
        if -self.p[x] < -self.p[y]:
            (x, y) = (y, x)
        self.p[x] += self.p[y]
        self.p[y] = x
T = int(input())
for _ in range(T):
    (N, M) = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: -x[2])
    g = [[] for _ in range(N)]
    uf = UnionFind(N)
    ans = 10 ** 6
    (v0, v1) = (0, 0)
    for (v, w, c) in edges:
        v -= 1
        w -= 1
        g[v].append(w)
        g[w].append(v)
        if uf.find(v) == uf.find(w):
            ans = min(ans, c)
            (v0, v1) = (v, w)
            continue
        uf.unite(v, w)
    'dfs start'
    d = [0] * N
    d[v0] = 1
    dfs_route = [v0 + 1]
    cycle_detected = 0
    cycle = []

    def dfs(v):
        global cycle, cycle_detected
        d[v] = 1
        dfs_route.append(v)
        for w in g[v]:
            if d[w]:
                if w == v0 and len(dfs_route) > 2 and (not cycle_detected):
                    cycle = [v for v in dfs_route]
                    flag = 1
                continue
            d[w] = 1
            dfs(w)
        dfs_route.pop()
    dfs(v1)
    'dfs end'
    print(ans, len(cycle))
    print(*cycle)