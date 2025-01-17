import heapq

n, m, k = map(int, input().split())
special = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if max(d, w) < dist[v]:
                dist[v] = max(d, w)
                heapq.heappush(pq, (dist[v], v))
    return dist

ans = []
for x in special:
    dist = dijkstra(x)
    mx = 0
    for y in special:
        if x != y:
            mx = max(mx, dist[y])
    ans.append(mx)

print(*ans)
