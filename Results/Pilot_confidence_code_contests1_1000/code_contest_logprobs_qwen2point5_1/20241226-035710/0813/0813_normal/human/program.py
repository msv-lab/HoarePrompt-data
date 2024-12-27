import heapq
from collections import defaultdict
n,m = [int(x) for x in raw_input().split(' ')]

arr = list()

d = defaultdict(list)
for _ in range(m):
    el = [int(x) for x in raw_input().split(' ')]
    d[el[0]].append(el[1])
    d[el[1]].append(el[0])
vis = []
cur = set()
q = []
heapq.heappush(q, 1)
cur.add(1)
while len(q) > 0:
    m = heapq.heappop(q)
    vis.append(m)
    for x in d[m]:
        if x not in cur:
            cur.add(x)
            heapq.heappush(q,x)
print(' '.join([str(x) for x in vis]))