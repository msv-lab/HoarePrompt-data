from typing import List, Tuple
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def gcd(x: int, y: int) -> int:
    while y > 0:
        x, y = y, x % y
    return x

class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0]*N

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
        self.parent[rv] = ru
        self.rank[ru] += self.rank[rv]
        return True

def solve() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dsu = DSU(n*n)
    for i in range(n):
        for j in range(n):
            for di in range(-k, k+1):
                for dj in range(-k, k+1):
                    ni, nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < n and abs(di)+abs(dj) <= k and gcd(a[(ni+1)%n], a[(j+1)%n]) > 1:
                        dsu.union((i)*n+(j), (ni)*n+(nj))

    print(sum([1 for r in dsu.rank if r > 0]))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()