

from Queue import Queue
def bfs(l, r):
    mark = [False] * n
    cola = Queue()
    cola.put(0)
    mark[0] = True
    while not cola.empty():
        u = cola.get()
        if u == n - 1:
            return True
        for v, e in graph[u]:
            if not mark[v] and edges[e][0] <= l <= r <= edges[e][1]:
                mark[v] = True
                cola.put(v)
    return False


n, m = map(int, raw_input().split())
graph = [[] for _ in range(n)]
edges = []
events = []

for i in range(m):
    ak, bk, lk, rk = map(int, raw_input().split())
    edges.append((lk, rk))
    graph[ak - 1].append((bk - 1, i))
    graph[bk - 1].append((ak - 1, i))
    events.append(lk)
    events.append(rk)


l = 0
r = 0
resp = 0
while r < len(events):
    if r < l:
        r = l
    while r < len(events) and bfs(events[l], events[r]):
        resp = max(resp, events[r] - events[l] + 1)
        r += 1
    l += 1


if resp > 0:
    print(resp)
else:
    print('Nice work, Dima!')
