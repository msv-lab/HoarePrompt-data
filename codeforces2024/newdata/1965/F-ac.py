# LUOGU_RID: 162825576
import heapq

# 使用元组替代Node类
n = int(input().strip())
nnn = n

a = [(0, 0) for _ in range(n + 1)]
vc = [[] for _ in range(200005)]
b = [0] * 200005
c = [0] * 200005
d = [0] * 200005
ans = [0] * 200005

m = 0

for i in range(1, n + 1):
    line = input().strip().split()
    l = int(line[0])
    r = int(line[1])
    a[i] = (l, r)
    m = max(m, r)

pq = []
for i in range(1, n + 1):
    vc[a[i][0]].append(a[i][1])

n = 0
for i in range(1, m + 1):
    for j in vc[i]:
        heapq.heappush(pq, j)
    while pq and pq[0] < i:
        heapq.heappop(pq)
    if pq:
        n += 1
        a[n] = (i, heapq.heappop(pq))

for i in range(1, n + 1):
    l, r = a[i]
    b[l] = r
    c[r] += 1
    d[l] += 1
    d[r + 1] -= 1

s = 0
j = m
for i in range(m, 0, -1):
    s += c[i]
    while j >= i and s < j - i + 1:
        s -= (1 if b[j] else 0)
        j -= 1
    if j <= m:
        ans[j - i + 1] += 1

for i in range(max(m, n), 0, -1):
    ans[i] += ans[i + 1]

for i in range(1, nnn + 1):
    print(ans[i])
