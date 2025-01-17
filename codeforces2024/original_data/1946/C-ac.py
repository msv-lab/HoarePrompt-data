# Consulted editorial & ChatGPT
from sys import stdin, setrecursionlimit
import threading
setrecursionlimit(10000000)
threading.stack_size(10**8)

def main():
    def dfs(r, p, g):
        s = 1
        for v in a[r]:
            if v != p:
                s += dfs(v, r, g)
        if s >= g:
            c[0] += 1
            return 0
        return s
    
    d = stdin.read().splitlines()
    i = 1
    li = len(d)
    o = []
    while i < li:
        n, k = map(int, d[i].split())
        i += 1
        a = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, d[i].split())
            a[u].append(v)
            a[v].append(u)
            i += 1

        l, r = 1, (n >> 1) + 1
        while l <= r:
            m = (l + r) >> 1
            c = [0]
            dfs(1, 0, m)
            if c[0] >= k + 1:
                l = m + 1
            else:
                r = m - 1
        o.append(r)
    print('\n'.join(map(str, o)))

threading.Thread(target=main).start()