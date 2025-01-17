class Comp:
    def __init__(self, g, root, tin):
        self.t = 0
        self.bridges = []
        def dfs(u, v):
            assert tin[v] is None
            low[v] = tin[v] = self.t
            self.t += 1
            for w in g[v]:
                if w is u:
                    continue
                if tin[w] is None:
                    low[v] = min(low[v], dfs(v, w))
                    sz[v] += sz[w]
                else:
                    low[v] = min(low[v], tin[w])
            if u is None:
                return
            if low[v] == tin[v]:
                self.bridges.append(v)
            return low[v]
        dfs(None, root)
 
t = int(input())
for _ in range(t):
    n, m, c = map(int,input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u-1].add(v-1)
        g[v-1].add(u-1)
    tin = [None]*n
    low = [None]*n
    sz = [1]*n
    comps = []
    for u in range(n):
        if tin[u] is None:
            comps.append(Comp(g, u, tin))
    kk = {0}
    for comp in comps:
        kk |= {k+comp.t for k in kk}
    for comp0 in comps:
        rr = {r for u in comp0.bridges for r in {sz[u], comp0.t-sz[u]}}
        kk0 = {0}
        for comp1 in comps:
            if comp1 is not comp0:
                kk0 |= {k+comp1.t for k in kk0}
        kk |= {k+r for k in kk0 for r in rr}
    res = c*(len(comps)-1) + min(k*k+(n-k)*(n-k) for k in kk) if len(comps)>1 or comps[0].bridges else -1
    print(res)