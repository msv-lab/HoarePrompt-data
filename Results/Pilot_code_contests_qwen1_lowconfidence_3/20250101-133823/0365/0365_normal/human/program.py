from sys import stdin

rints = lambda: [int(x) for x in stdin.readline().split()]
rints_2d = lambda n: [rints() for _ in range(n)]

n, m = rints()
mem, edges, weight = [0] * (n + 1), rints_2d(m), [[] for _ in range(10 ** 5 + 1)]

for u, v, w in edges:
    weight[w].append((u, v))

for i in range(1, 10 ** 5 + 1):
    all = [(v, mem[u]) for u, v in weight[i]]
    for v, du in all:
        mem[v] = max(mem[v], du + 1)

print(max(mem))
