def can_make_acyclic(n, m, edges):
    from collections import defaultdict, deque
    
    def has_cycle(graph):
        in_degree = {i: 0 for i in range(1, n + 1)}
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
        
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count != n
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    if not has_cycle(graph):
        return 'YES'
    
    for u, v in edges:
        graph[u].remove(v)
        if not has_cycle(graph):
            return 'YES'
        graph[u].append(v)
    
    return 'NO'


# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
edges = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]

# Solve the problem
result = can_make_acyclic(n, m, edges)
print(result)
