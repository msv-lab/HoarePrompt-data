import heapq
import sys
input = sys.stdin.read

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        max_cost, u = heapq.heappop(heap)
        if max_cost > dist[u]:
            continue
        for v, weight in graph[u]:
            max_w = max(max_cost, weight)
            if max_w < dist[v]:
                dist[v] = max_w
                heapq.heappush(heap, (max_w, v))
    
    return dist

def main():
    data = input().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    special_vertices = []
    for _ in range(k):
        special_vertices.append(int(data[idx]))
        idx += 1
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    result = []
    for s_vertex in special_vertices:
        dist = dijkstra(n, graph, s_vertex)
        max_dist = 0
        for t_vertex in special_vertices:
            if s_vertex != t_vertex:
                max_dist = max(max_dist, dist[t_vertex])
        result.append(max_dist)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
