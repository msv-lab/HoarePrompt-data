import heapq
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        adj = defaultdict(list)
        col = 1
        color_map = {}
        for _ in range(m):
            u, v, c = map(int, input().split())
            if c not in color_map:
                color_map[c] = n + col
                col += 1
            adj[u].append((v, c))
            adj[v].append((u, c))
        
        b, e = map(int, input().split())
        if b == e:
            print(0)
            continue
        
        total_nodes = n + len(color_map)
        adj1 = defaultdict(set)
        
        for i in range(1, n + 1):
            for v, c in adj[i]:
                adj1[i].add(color_map[c])
                adj1[v].add(color_map[c])
                adj1[color_map[c]].add(i)
                adj1[color_map[c]].add(v)
        
        # Initialize distances with infinity
        dist = [float('inf')] * (total_nodes + 1)
        dist[b] = 0
        
        # Min heap for priority queue
        pq = []
        heapq.heappush(pq, (0, b))
        
        while pq:
            dis, node = heapq.heappop(pq)
            if dis > dist[node]:
                continue
            for neighbor in adj1[node]:
                if dis + 1 < dist[neighbor]:
                    dist[neighbor] = dis + 1
                    heapq.heappush(pq, (dis + 1, neighbor))
        
        # Since the answer needs to be divided by 2 and reduced by 1
        if dist[e] == float('inf'):
            print(-1)
        else:
            print((dist[e] // 2) - 1)

# Call the function to execute
solve()