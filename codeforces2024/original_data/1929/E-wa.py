import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n+1)]
        self.depth = [0] * (n+1)
        self.parent = [0] * (n+1)
        self.lca = [[-1] * 20 for _ in range(n+1)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, u, p):
        self.parent[u] = p
        self.depth[u] = self.depth[p] + 1
        for v in self.adj[u]:
            if v != p:
                self.dfs(v, u)

    def preprocess(self):
        self.dfs(1, 0)
        for i in range(1, self.n+1):
            self.lca[i][0] = self.parent[i]
        for j in range(1, 20):
            for i in range(1, self.n+1):
                self.lca[i][j] = self.lca[self.lca[i][j-1]][j-1]

    def get_lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for i in range(19, -1, -1):
            if self.depth[u] - (1 << i) >= self.depth[v]:
                u = self.lca[u][i]
        if u == v:
            return u
        for i in range(19, -1, -1):
            if self.lca[u][i] != self.lca[v][i]:
                u = self.lca[u][i]
                v = self.lca[v][i]
        return self.lca[u][0]

    def min_colored_edges(self, pairs):
        colored_edges = set()
        for a, b in pairs:
            lca = self.get_lca(a, b)
            colored_edges.add((a, self.parent[a]))
            colored_edges.add((b, self.parent[b]))
            colored_edges.add((lca, self.parent[lca]))
        return len(colored_edges)

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        tree = Tree(n)
        for _ in range(n-1):
            u = int(data[pos])
            v = int(data[pos+1])
            tree.add_edge(u, v)
            pos += 2
        k = int(data[pos])
        pos += 1
        pairs = []
        for _ in range(k):
            a = int(data[pos])
            b = int(data[pos+1])
            pairs.append((a, b))
            pos += 2
        tree.preprocess()
        print(tree.min_colored_edges(pairs))

if __name__ == "__main__":
    main()