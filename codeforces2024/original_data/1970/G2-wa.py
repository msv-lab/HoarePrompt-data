def find_components(n, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    components = []
    
    def bfs(start):
        queue = deque([start])
        component = []
        visited[start] = True
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component
    
    for i in range(1, n + 1):
        if not visited[i]:
            components.append(bfs(i))
    
    return components

def min_funding(n, m, c, corridors):
    if n == 2:
        return 4  # Only two cells, they must be connected directly
    
    min_cost = float('inf')
    for i in range(m):
        # Try removing each corridor and see if it splits the graph into two components
        u, v = corridors[i]
        # Remove the edge u-v
        new_edges = [corridors[j] for j in range(m) if j != i]
        
        components = find_components(n, new_edges)
        
        if len(components) == 2:
            # Calculate the cost
            size1 = len(components[0])
            size2 = len(components[1])
            cost = size1**2 + size2**2
            min_cost = min(min_cost, cost)
    
    return min_cost if min_cost != float('inf') else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        
        corridors = []
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            corridors.append((u, v))
        
        result = min_funding(n, m, c, corridors)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()