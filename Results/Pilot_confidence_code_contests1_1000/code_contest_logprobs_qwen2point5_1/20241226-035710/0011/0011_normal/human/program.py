import io
import os

from collections import Counter, defaultdict, deque

MOD = 10 ** 9 + 7


class UnionFind:
    def __init__(self, N):
        # Union find with component size
        # Negative means is a root where value is component size
        # Otherwise is index to parent
        self.p = [-1 for i in range(N)]

    def find(self, i):
        # Find root with path compression
        if self.p[i] >= 0:
            self.p[i] = self.find(self.p[i])
            return self.p[i]
        else:
            return i

    def union(self, i, j):
        # Union by size
        root1 = self.find(j)
        root2 = self.find(i)
        if root1 == root2:
            return
        size1 = -self.p[root1]
        size2 = -self.p[root2]
        if size1 < size2:
            self.p[root1] = root2
            self.p[root2] = -(size1 + size2)
        else:
            self.p[root2] = root1
            self.p[root1] = -(size1 + size2)

    def getComponentSize(self, i):
        return -self.p[self.find(i)]


def solve(N, M, vectors):
    uf = UnionFind(M)
    allCoords = set()
    single = set()
    for i, v in enumerate(vectors):
        allCoords.update(v)
        if len(v) == 1:
            (a,) = v
            single.add(a)
        else:
            a, b = v
            uf.union(a, b)
    trees = defaultdict(list)
    for x in allCoords:
        if uf.getComponentSize(x) > 1:
            trees[uf.find(x)].append(x)
    T = 1
    treeCoords = set()
    for coords in trees.values():
        for x in coords:
            if x in single:
                break
        else:
            treeCoords.update(coords)
            T *= pow(2, len(coords) - 1, MOD)
            T %= MOD
    T *= pow(2, len(allCoords) - len(treeCoords), MOD)
    T %= MOD

    uf = UnionFind(M)
    ans = []
    seen = set()
    for i, v in enumerate(vectors):
        if len(v) == 1:
            (a,) = v
            if a not in seen and a not in treeCoords:
                seen.add(a)
                ans.append(i)
        else:
            assert len(v) == 2
            a, b = v
            if a in treeCoords:
                assert b in treeCoords
                if uf.find(a) != uf.find(b):
                    uf.union(a, b)
                    ans.append(i)
            else:
                if a not in seen or b not in seen:
                    seen.add(a)
                    seen.add(b)
                    ans.append(i)

    return str(T) + " " + str(len(ans)) + "\n" + " ".join(str(i + 1) for i in ans)


if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    TC = 1  # int(input())
    for tc in range(1, TC + 1):
        (N, M) = [int(x) for x in input().split()]
        vectors = [[int(x) - 1 for x in input().split()][1:] for i in range(N)]
        ans = solve(N, M, vectors)
        print(ans)
