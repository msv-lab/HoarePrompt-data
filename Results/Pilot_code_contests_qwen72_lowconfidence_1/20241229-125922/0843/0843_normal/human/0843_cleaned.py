class UnionFind:

    def __init__(self, elems=None):

        class KeyDict(dict):

            def __missing__(self, key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)
        if elems is not None:
            for elem in elems:
                (_, _) = (self.parent[elem], self.rank[elem])

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for (x, x_par) in self.parent.items()]
        root = operator.itemgetter(1)
        for (_, group) in itertools.groupby(sorted(roots, key=root), root):
            yield [x for (x, _) in group]
(N, M) = map(int, raw_input().split())
uf = UnionFind(range(1, N + 1))
for i in range(M):
    (x, y, z) = map(int, raw_input().split())
    uf.unite(x, y)
F = set()
for i in range(1, N + 1):
    F.add(uf.find(i))
print(len(F))