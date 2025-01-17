N = int(input())
ans = []
a = [int(x) for x in input().split()]
b = [(i, a[i]) for i in range(len(a))]
S = sorted(b, key=lambda x: x[1])
m = max(a)
bits = [0] + [1] * N + [0]
wtr = [[] for q in range(N)]
f = []
g = 1
last = 0
for (i, num) in S:
    for e in range(num - last):
        f.append(g)
    last = num
    bits[i + 1] = 0
    g += bits[i] + bits[i + 2] - 1
for d in range(1, m + 1):
    print(sum([f[d * x] for x in range(1 + (m - 1) // d)]), end=' ')