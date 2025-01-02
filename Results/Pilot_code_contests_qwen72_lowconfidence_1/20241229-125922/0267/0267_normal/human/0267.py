from sys import stdin


class disjointset:
    def __init__(self, n):
        self.rank, self.parent, self.n, self.nsets = [0] * (n + 1), [i for i in range(n + 1)], n, [1] * (n + 1)

    def find(self, x):
        xcopy = x
        while x != self.parent[x]:
            x = self.parent[x]

        while xcopy != x:
            self.parent[xcopy], xcopy = x, self.parent[xcopy]

        return x

    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)

        # already union
        if xpar == ypar:
            return
        # perform union by rank
        par, child = xpar, ypar
        if self.rank[xpar] < self.rank[ypar]:
            par, child = ypar, xpar

        elif self.rank[xpar] == self.rank[ypar]:
            self.rank[xpar] += 1

        self.parent[child] = par
        self.nsets[par] += self.nsets[child]
        self.n -= 1

    # find min total weight tree
    def kruskal(self, edges):
        result, all, rem = 0, [], []

        # loop over v-1
        for u, v, w in edges:
            upar, vpar = self.find(u), self.find(v)

            # no cycle
            if upar != vpar:
                all.append(w)
                self.union(upar, vpar)
                result += max(0, w - k)
            else:
                rem.append(w)

        if all and all[-1] < k:
            try:
                result += min([abs(i - k) for i in rem])
            except:
                result += k - all[-1]
        print(result)


rints = lambda: tuple([int(x) for x in stdin.readline().split()])
rints_2d = lambda n: [rints() for _ in range(n)]
out = []
for _ in range(int(input())):
    n, m, k = rints()
    dis = disjointset(n)
    a = sorted(rints_2d(m), key=lambda x: x[-1])
    dis.kruskal(a)
